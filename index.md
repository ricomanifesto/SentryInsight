# Exploitation Report

Recent cybersecurity developments reveal significant exploitation activities across multiple platforms and services. The most critical incidents include sophisticated phishing campaigns targeting Microsoft 365 environments utilizing advanced 2FA bypass techniques and HTTP client tools, a major supply chain attack compromising 20 popular npm packages with over 2 billion weekly downloads, and the emergence of advanced Android malware with NFC relay capabilities. Additionally, critical vulnerabilities in SAP NetWeaver and Microsoft Exchange Online services are creating substantial attack surfaces for threat actors seeking to compromise enterprise environments.

## Active Exploitation Details

### Microsoft 365 Phishing Campaign via Axios Abuse
- **Description**: Threat actors are exploiting HTTP client tools like Axios in conjunction with Microsoft's Direct Send feature to create highly efficient phishing attack pipelines targeting Microsoft 365 environments
- **Impact**: Attackers can bypass traditional email security measures and conduct advanced phishing attacks with improved success rates
- **Status**: Actively being exploited in ongoing campaigns with enhanced evasion techniques

### Salty 2FA Kit Exploitation
- **Description**: Advanced phishing kits specifically designed to bypass two-factor authentication mechanisms are being deployed in sophisticated social engineering attacks
- **Impact**: Complete compromise of protected accounts despite 2FA protections, leading to unauthorized access to sensitive systems and data
- **Status**: Actively exploited in targeted campaigns against developers and high-value targets

### npm Supply Chain Compromise
- **Description**: A coordinated supply chain attack compromised 20 popular npm packages following a successful phishing attack against maintainer Josh Junon's account
- **Impact**: Over 2 billion weekly downloads potentially affected, creating massive potential for downstream compromise across the JavaScript ecosystem
- **Status**: Packages have been compromised and malicious code distributed to downstream users

### SAP NetWeaver Command Execution Vulnerability
- **Description**: Critical severity command execution flaw in SAP NetWeaver software solution allowing arbitrary command execution
- **Impact**: Complete system compromise and potential lateral movement within enterprise environments
- **Status**: Recently patched by SAP as part of 21 vulnerability fixes, including three critical severity issues

## Affected Systems and Products

- **Microsoft 365 Services**: Exchange Online and Microsoft Teams environments experiencing URL blocking and email quarantine issues
- **npm Ecosystem**: 20 popular packages with 2 billion weekly downloads compromised in supply chain attack
- **SAP NetWeaver**: Critical command execution vulnerabilities affecting enterprise installations
- **Android Devices**: RatOn malware targeting banking applications with NFC relay capabilities
- **Docker APIs**: Misconfigured Docker installations being exploited for TOR-based cryptojacking operations

## Attack Vectors and Techniques

- **Phishing Pipeline**: Combination of Axios HTTP client tools and Microsoft Direct Send to create efficient phishing attack chains
- **2FA Bypass**: Sophisticated kits designed to circumvent two-factor authentication protections through social engineering
- **Supply Chain Poisoning**: Compromise of maintainer accounts to inject malicious code into widely-used software packages
- **NFC Relay Attacks**: Android malware utilizing Near Field Communication relay techniques for banking fraud
- **Cryptojacking via TOR**: Exploitation of misconfigured Docker APIs to deploy cryptocurrency mining operations through TOR networks

## Threat Actor Activities

- **Microsoft 365 Phishing Groups**: Conducting advanced campaigns using novel combination of legitimate tools and Microsoft services for evasion
- **Supply Chain Attackers**: Successfully compromised high-profile npm maintainer accounts to distribute malicious packages at scale
- **RatOn Operators**: Deploying sophisticated Android banking malware with remote access trojan capabilities and automated transfer system fraud features
- **Cryptojacking Campaigns**: Expanding operations through Docker API exploitation using TOR network infrastructure for anonymity and persistence