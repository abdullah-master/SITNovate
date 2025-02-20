# VidwanCheck - Blockchain Certificate Verification System

A secure and efficient blockchain-based solution for certificate verification and management. VidwanCheck allows institutions to issue tamper-proof digital certificates and enables instant verification through QR codes and blockchain technology.

## Features

- Secure certificate issuance with blockchain integration
- QR code generation and scanning for instant verification
- Admin dashboard for certificate management
- Mobile-responsive design
- Chrome extension for quick verification
- Real-time blockchain validation
- Modern, intuitive user interface

## Technology Stack

- *Frontend*: HTML5, CSS3, JavaScript
- *Backend*: Flask (Python)
- *Blockchain*: Ethereum (Solidity Smart Contracts)
- *Database*: MongoDB
- *Additional Tools*: 
  - Web3.py for blockchain interaction
  - HTML5-QRCode for QR scanning
  - Chrome Extension APIs

## Project Structure


blockchain-certification/
├── app.py                 # Main Flask application
├── contracts/            # Ethereum smart contracts
│   └── Certificate.sol   # Certificate smart contract
├── extension/           # Chrome extension files
│   ├── manifest.json
│   ├── popup.html
│   ├── popup.js
│   └── styles.css
├── migrations/          # Truffle migration scripts
├── static/             # Static assets
│   ├── css/
│   ├── js/
│   └── images/
├── templates/          # HTML templates
│   ├── index.html
│   ├── login-admin.html
│   └── verify.html
├── test/              # Smart contract tests
├── truffle-config.js  # Truffle configuration
└── README.md


## Installation

1. Clone the repository:
bash
git clone https://github.com/yourusername/blockchain-certification.git
cd blockchain-certification


2. Install Python dependencies:
bash
pip install -r requirements.txt


3. Install and configure MongoDB:
- Download and install MongoDB
- Start MongoDB service
- Create a database named 'certificate_db'

4. Configure Ethereum environment:
bash
npm install -g truffle
npm install
truffle compile
truffle migrate


5. Start the Flask application:
bash
python app.py


6. Install Chrome Extension (Developer Mode):
- Open Chrome and go to chrome://extensions/
- Enable "Developer mode"
- Click "Load unpacked"
- Select the extension folder

## Usage

1. *Admin Access*:
   - Navigate to /login-admin
   - Login with admin credentials
   - Issue new certificates
   - Manage existing certificates

2. *Certificate Verification*:
   - Scan QR code using the web interface or Chrome extension
   - Enter certificate hash manually
   - View verification results instantly

3. *Chrome Extension*:
   - Click the VidwanCheck extension icon
   - Choose between QR scanning or manual hash input
   - View verification results in a popup

## Contributing

1. Fork the repository
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Your Name - your.email@example.com
Project Link: [https://github.com/yourusername/blockchain-certification](https://github.com/yourusername/blockchain-certification)