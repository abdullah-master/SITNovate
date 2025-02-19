from flask import Flask, render_template, request, jsonify
from web3 import Web3
import hashlib
from pymongo import MongoClient

app = Flask(__name__, static_url_path='/static')

# Connect to Ganache
ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Set contract address and ABI (replace with your contract details)
contract_address = "0x34005CF103E7546451cc9c43357942d12ca78540"
contract_abi = [
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "string",
                "name": "certificateHash",
                "type": "string"
            }
        ],
        "name": "CertificatePublished",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "name": "certificates",
        "outputs": [
            {"internalType": "string", "name": "awardeeName", "type": "string"},
            {"internalType": "string", "name": "certificateName", "type": "string"},
            {"internalType": "string", "name": "certificateCode", "type": "string"},
            {"internalType": "string", "name": "certificateHash", "type": "string"},
            {"internalType": "uint256", "name": "timestamp", "type": "uint256"}
        ],
        "stateMutability": "view",
        "type": "function",
        "constant": True
    },
    {
        "inputs": [
            {"internalType": "string", "name": "awardeeName", "type": "string"},
            {"internalType": "string", "name": "certificateName", "type": "string"},
            {"internalType": "string", "name": "certificateCode", "type": "string"},
            {"internalType": "string", "name": "certificateHash", "type": "string"}
        ],
        "name": "publishCertificate",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "string", "name": "certificateHash", "type": "string"}
        ],
        "name": "verifyCertificate",
        "outputs": [
            {"internalType": "bool", "name": "", "type": "bool"},
            {
                "components": [
                    {"internalType": "string", "name": "awardeeName", "type": "string"},
                    {"internalType": "string", "name": "certificateName", "type": "string"},
                    {"internalType": "string", "name": "certificateCode", "type": "string"},
                    {"internalType": "string", "name": "certificateHash", "type": "string"},
                    {"internalType": "uint256", "name": "timestamp", "type": "uint256"}
                ],
                "internalType": "tuple",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function",
        "constant": True
    }
]

# Create contract instance
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Default account for transactions
default_account = "0x24af5Ae5400781935b5d26611c671432AE41D098"

# ------------------ MongoDB Integration ------------------
# Connect to MongoDB (ensure MongoDB is running on your machine)
client = MongoClient("mongodb://localhost:27017/")
# Database name: VidwanCheckDB
db = client["VidwanCheckDB"]
# Collection name: admins (store admin credentials here)
admins_collection = db["admins"]
# ---------------------------------------------------------

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verify')
def verify():
    return render_template('verify.html')

@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/login_admin')
def login_admin():
    return render_template('login-admin.html')

@app.route('/admin_login', methods=['POST'])
def admin_login():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    username = data['username']
    try:
        # Expect password to be an integer
        password = int(data['password'])
    except ValueError:
        return jsonify({'success': False, 'message': 'Password must be an integer'}), 400

    # Query the admins collection for matching credentials
    admin = admins_collection.find_one({'username': username, 'password': password})
    if admin:
        return jsonify({'success': True, 'message': 'Login successful'})
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials'}), 401

@app.route('/publish', methods=['POST'])
def publish():
    data = request.get_json()
    required_fields = ["awardee_name", "certificate_name", "certificate_code"]

    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    awardee_name = data["awardee_name"]
    certificate_name = data["certificate_name"]
    certificate_code = data["certificate_code"]

    certificate_hash = hashlib.sha512((certificate_code + certificate_name).encode()).hexdigest()

    try:
        tx_hash = contract.functions.publishCertificate(
            awardee_name, certificate_name, certificate_code, certificate_hash
        ).transact({'from': default_account})

        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

        return jsonify({
            "message": "Certificate published successfully",
            "certificate_hash": certificate_hash,
            "transaction_hash": tx_hash.hex()
        }), 201
    except Exception as e:
        return jsonify({"error": f"Failed to publish certificate: {str(e)}"}), 500

@app.route('/verify_certificate', methods=['GET'])
def verify_certificate():
    certificate_hash = request.args.get('certificate_hash')
    if not certificate_hash:
        return jsonify({"error": "Missing certificate_hash parameter"}), 400

    try:
        verified, cert = contract.functions.verifyCertificate(certificate_hash).call()

        if not verified:
            return jsonify({"verified": False, "message": "Certificate not found or invalid"}), 200

        return jsonify({
            "verified": True,
            "certificate": {
                "awardee_name": cert[0],
                "certificate_name": cert[1],
                "certificate_code": cert[2],
                "certificate_hash": cert[3],
                "timestamp": cert[4]
            }
        }), 200
    except Exception as e:
        return jsonify({"error": f"Verification failed: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
