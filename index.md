# Exploitation Report

The current threat landscape reveals several critical exploitation activities targeting enterprise systems and developer infrastructure. Most notably, threat actors are conducting sophisticated phishing campaigns against Microsoft 365 environments using advanced techniques including Axios HTTP client abuse and 2FA bypass methods. A significant supply chain attack has compromised 20 popular npm packages with over 2 billion weekly downloads through a successful phishing attack against a maintainer. Additionally, new Android malware variants are demonstrating advanced capabilities including NFC relay attacks and automated banking fraud, while cryptojacking operations continue to expand through misconfigured Docker APIs using TOR networks for obfuscation.

## Active Exploitation Details

### Microsoft 365 Phishing Campaign with Axios Abuse
- **Description**: Advanced phishing attacks targeting Microsoft 365 environments using HTTP client tools like Axios in conjunction with Microsoft's Direct Send feature to create highly efficient attack pipelines
- **Impact**: Successful credential harvesting and 2FA bypass leading to unauthorized access to corporate Microsoft 365 accounts
- **Status**: Active exploitation with new "Salty 2FA Kits" being deployed in the wild

### npm Supply Chain Attack
- **Description**: Large-scale supply chain compromise affecting 20 popular npm packages through a successful phishing attack against maintainer Josh Junon (Qix)
- **Impact**: Potential code injection and malicious payload distribution to millions of applications using the compromised packages
- **Status**: Active compromise with over 2 billion weekly downloads at risk

### SAP NetWeaver Command Execution Vulnerability
- **Description**: Maximum severity command execution flaw in SAP NetWeaver software solution
- **Impact**: Remote code execution allowing attackers to gain complete system control
- **Status**: Recently patched by SAP as part of 21 vulnerability fixes including three critical severity issues

### RatOn Android Malware
- **Description**: Sophisticated Android malware evolved from basic NFC relay attack tool to full remote access trojan with Automated Transfer System (ATS) banking fraud capabilities
- **Impact**: Financial fraud through automated banking transactions and NFC-based payment system exploitation
- **Status**: Active in the wild with expanding capabilities

### TOR-Based Cryptojacking Campaign
- **Description**: Cryptojacking attacks targeting misconfigured Docker APIs using TOR network for command and control obfuscation
- **Impact**: Unauthorized cryptocurrency mining consuming system resources and potentially providing persistent access
- **Status**: Active campaign with expanding infrastructure

### MostereRAT Banking Malware Campaign
- **Description**: Phishing campaign delivering MostereRAT, a banking malware that has evolved into a remote access trojan
- **Impact**: Financial data theft and remote system control capabilities
- **Status**: Active distribution through sophisticated phishing techniques

## Affected Systems and Products

- **Microsoft 365**: Exchange Online and Microsoft Teams environments targeted by advanced phishing campaigns
- **npm Ecosystem**: 20 popular packages with 2 billion weekly downloads compromised in supply chain attack
- **SAP NetWeaver**: Enterprise software solution with critical command execution vulnerabilities
- **Android Devices**: Mobile platforms targeted by RatOn malware with NFC and banking fraud capabilities
- **Docker Environments**: Misconfigured Docker APIs being exploited for cryptojacking operations
- **Banking Applications**: Android banking apps targeted by multiple malware families including MostereRAT

## Attack Vectors and Techniques

- **Advanced Phishing**: Multi-stage phishing campaigns using legitimate tools like Axios for credential harvesting
- **2FA Bypass**: "Salty 2FA Kits" enabling circumvention of two-factor authentication mechanisms
- **Supply Chain Compromise**: Targeted phishing against package maintainers to inject malicious code into popular libraries
- **NFC Relay Attacks**: Exploitation of Near Field Communication for payment fraud and data theft
- **API Exploitation**: Targeting misconfigured Docker APIs for unauthorized access and resource abuse
- **TOR Network Abuse**: Using anonymization networks for command and control infrastructure
- **Social Engineering**: Sophisticated phishing techniques targeting developers and system administrators

## Threat Actor Activities

- **Microsoft 365 Attackers**: Conducting large-scale phishing campaigns with advanced 2FA bypass capabilities targeting enterprise environments
- **Supply Chain Attackers**: Successfully compromised high-value npm maintainer accounts to distribute malicious code to millions of applications
- **Mobile Banking Fraudsters**: Deploying sophisticated Android malware with automated transfer capabilities and NFC exploitation
- **Cryptojacking Groups**: Expanding TOR-based infrastructure to target containerized environments through API misconfigurations
- **Banking Malware Operators**: Distributing evolved RAT capabilities through traditional phishing vectors with enhanced persistence mechanisms