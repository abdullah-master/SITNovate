// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CertificateVerification {
    struct Certificate {
        string awardeeName;
        string certificateName;
        string certificateCode;
        string certificateHash;
        uint256 timestamp;
    }

    mapping(string => Certificate) public certificates;
    string[] public certificateHashes;

    event CertificatePublished(string certificateHash);

    function publishCertificate(
        string memory awardeeName,
        string memory certificateName,
        string memory certificateCode,
        string memory certificateHash
    ) public {
        require(bytes(certificateHash).length > 0, "Certificate hash cannot be empty");
        require(bytes(certificates[certificateHash].certificateHash).length == 0, "Certificate already exists");

        certificates[certificateHash] = Certificate({
            awardeeName: awardeeName,
            certificateName: certificateName,
            certificateCode: certificateCode,
            certificateHash: certificateHash,
            timestamp: block.timestamp
        });

        certificateHashes.push(certificateHash);
        emit CertificatePublished(certificateHash);
    }

    function verifyCertificate(string memory certificateHash) public view returns (bool, Certificate memory) {
        Certificate memory cert = certificates[certificateHash];
        if (bytes(cert.certificateHash).length == 0) {
            return (false, cert);
        }
        return (true, cert);
    }
}