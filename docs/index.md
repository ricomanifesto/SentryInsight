# Exploitation Report

Critical zero-day exploitation activity dominates the current threat landscape, with Adobe Acrobat and Reader being actively exploited through malicious PDF files for at least four months before emergency patches were released. The pre-authentication remote code execution vulnerability in Marimo is now under active exploitation for credential theft, while the wolfSSL library contains a critical flaw enabling certificate forgery attacks. Meanwhile, threat actors are leveraging sophisticated malware campaigns including JanelaRAT targeting Latin American banks with over 14,000 attacks in Brazil, and APT41's deployment of zero-detection backdoors to harvest cloud credentials from major providers.

## Active Exploitation Details

### Adobe Acrobat and Reader Zero-Day
- **Description**: Critical zero-day vulnerability in Adobe Acrobat and Reader exploited through maliciously crafted PDF files
- **Impact**: Remote code execution allowing attackers full system compromise
- **Status**: Emergency patches released after months of active exploitation
- **CVE ID**: CVE-2026-34621

### Marimo Pre-Authentication RCE
- **Description**: Critical pre-authentication remote code execution vulnerability in the Marimo platform
- **Impact**: Complete system compromise without authentication, enabling credential theft
- **Status**: Currently under active exploitation with no authentication required

### wolfSSL Certificate Forgery Vulnerability
- **Description**: Critical vulnerability enabling improper verification of hash algorithms in Elliptic Curve Digital Signature Algorithm (ECDSA) implementations
- **Impact**: Attackers can use forged certificates to bypass SSL/TLS security controls
- **Status**: Critical vulnerability affecting SSL/TLS security implementations

## Affected Systems and Products

- **Adobe Acrobat and Reader**: All versions prior to emergency security update affected by zero-day exploitation
- **Marimo Platform**: Pre-authentication remote code execution affecting all exposed instances
- **wolfSSL Library**: Critical cryptographic vulnerability affecting ECDSA certificate verification
- **CPUID Website**: Hardware monitoring tools including CPU-Z, HWMonitor, HWMonitor Pro, and PerfMonitor compromised
- **OpenAI macOS Applications**: Code-signing workflow compromised through malicious Axios package
- **AWS, Google Cloud, Microsoft Azure, Alibaba Cloud**: Targeted by APT41 credential harvesting campaigns

## Attack Vectors and Techniques

- **Malicious PDF Exploitation**: Zero-day attacks using crafted PDF files to exploit Adobe Reader vulnerabilities
- **Pre-Authentication RCE**: Direct remote code execution without requiring user authentication
- **Certificate Forgery**: Exploitation of cryptographic verification weaknesses in SSL/TLS implementations
- **Supply Chain Compromise**: Trojanized software downloads through compromised legitimate websites
- **Social Engineering**: Facebook-based approaches by APT37 to deliver RokRAT malware
- **Session Hijacking**: Storm infostealer bypassing passwords and MFA through server-side decryption
- **Typosquatting**: APT41 using domain spoofing to obscure command and control communications

## Threat Actor Activities

- **APT41**: Deploying zero-detection backdoors targeting cloud environments including AWS, Google, Azure, and Alibaba for credential harvesting
- **APT37 (ScarCruft)**: North Korean group conducting multi-stage social engineering campaigns via Facebook to deliver RokRAT malware
- **JanelaRAT Operators**: Targeting Latin American banks with 14,739 attacks recorded in Brazil during 2025
- **ShinyHunters**: Extortion gang leaking Rockstar Games analytics data following Anodot security incident
- **W3LL Phishing Network**: Global operation dismantled by FBI and Indonesian authorities after attempting $20M in fraud
- **Unknown Actors**: Compromising CPUID website to distribute STX RAT through trojanized hardware monitoring tools
- **Storm Infostealer Operators**: Deploying advanced session hijacking malware with server-side decryption capabilities