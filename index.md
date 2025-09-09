# Exploitation Report

The current threat landscape reveals multiple active exploitation campaigns targeting diverse platforms and attack vectors. Most concerning are sophisticated phishing operations leveraging Microsoft 365 infrastructure abuse, supply chain attacks compromising popular npm packages with billions of weekly downloads, advanced Android malware campaigns with banking fraud capabilities, and the exploitation of critical SAP NetWeaver vulnerabilities. Threat actors are increasingly utilizing legitimate tools and services to bypass security controls, while mobile malware has evolved to incorporate NFC relay attacks and automated transfer system fraud. Additionally, cryptojacking attacks are expanding through misconfigured Docker APIs via TOR networks, demonstrating the persistent threat to cloud infrastructure.

## Active Exploitation Details

### SAP NetWeaver Command Execution Vulnerability
- **Description**: A critical command execution flaw in SAP NetWeaver software solution that has been assigned maximum severity rating
- **Impact**: Attackers can execute arbitrary commands on affected SAP systems, potentially leading to complete system compromise
- **Status**: Patched by SAP as part of their latest security update addressing 21 vulnerabilities, including three critical severity issues

### Microsoft 365 Phishing via Axios Abuse
- **Description**: Advanced phishing campaigns abusing HTTP client tools like Axios in conjunction with Microsoft's Direct Send feature
- **Impact**: Highly efficient attack pipeline enabling credential theft and 2FA bypass through sophisticated phishing kits
- **Status**: Active exploitation observed in ongoing campaigns targeting Microsoft 365 users

### npm Package Supply Chain Compromise
- **Description**: Software supply chain attack targeting npm packages with over 2 billion weekly downloads after maintainer account compromise
- **Impact**: Potential code injection into applications using compromised packages, affecting millions of downstream users
- **Status**: 20 popular npm packages compromised following successful phishing attack against maintainer Josh Junon

### RatOn Android Banking Malware
- **Description**: Sophisticated Android malware evolved from basic NFC relay tool to full-featured remote access trojan with Automated Transfer System (ATS) banking fraud capabilities
- **Impact**: Banking credential theft, NFC relay attacks for payment fraud, and remote device control
- **Status**: Actively distributed and evolving with enhanced fraud capabilities

### Docker API Cryptojacking Campaign
- **Description**: TOR-based cryptojacking attacks targeting misconfigured Docker APIs for unauthorized cryptocurrency mining
- **Impact**: Unauthorized resource consumption, potential lateral movement, and infrastructure compromise
- **Status**: Active campaign with expanding variants discovered by security researchers

## Affected Systems and Products

- **SAP NetWeaver**: Critical severity vulnerabilities affecting the enterprise software solution
- **Microsoft 365 Services**: Exchange Online and Microsoft Teams affected by phishing campaigns and anti-spam service bugs
- **npm Package Registry**: 20 popular packages with 2 billion weekly downloads compromised
- **Android Devices**: Mobile devices targeted by RatOn malware with banking and NFC fraud capabilities
- **Docker Environments**: Misconfigured Docker APIs vulnerable to cryptojacking attacks
- **Windows 11**: File Explorer experiencing anti-spam service issues blocking legitimate URLs

## Attack Vectors and Techniques

- **Phishing with 2FA Bypass**: Advanced phishing kits incorporating "Salty 2FA" techniques to bypass multi-factor authentication
- **HTTP Client Abuse**: Legitimate tools like Axios leveraged to create efficient attack pipelines
- **Supply Chain Compromise**: Targeted phishing against package maintainers to compromise widely-used software libraries
- **NFC Relay Attacks**: Mobile malware utilizing Near Field Communication for payment fraud
- **TOR Network Abuse**: Cryptojacking operations leveraging anonymization networks for persistence
- **Direct Send Feature Abuse**: Microsoft's email service features exploited for phishing distribution
- **Automated Transfer Systems**: Banking malware incorporating ATS fraud capabilities for financial theft

## Threat Actor Activities

- **Microsoft 365 Phishing Groups**: Sophisticated campaigns targeting enterprise users with advanced 2FA bypass techniques and legitimate service abuse
- **Mobile Banking Fraudsters**: Android malware operators evolving RatOn malware with enhanced NFC relay and automated banking fraud capabilities
- **Supply Chain Attackers**: Threat actors successfully compromising high-value npm package maintainers through targeted phishing to affect billions of downloads
- **Cryptojacking Operations**: TOR-based mining groups expanding attacks through misconfigured Docker environments with persistent infrastructure abuse