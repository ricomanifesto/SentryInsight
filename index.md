# Exploitation Report

Critical zero-day vulnerabilities are currently under active exploitation across multiple platforms, with CISA issuing emergency directives for federal agencies. The most significant threats include an unpatched Gogs Git service zero-day that has compromised over 700 servers globally, a Windows RasMan service denial-of-service vulnerability, and a GeoServer XXE injection flaw added to CISA's Known Exploited Vulnerabilities catalog. Additionally, threat actors are leveraging React Server Components vulnerabilities for large-scale attacks, while sophisticated phishing kits are using AI-enhanced techniques to bypass multi-factor authentication and steal credentials at unprecedented scales.

## Active Exploitation Details

### Gogs Git Service Zero-Day
- **Description**: An unpatched high-severity vulnerability in the self-hosted Git service Gogs that bypasses a previous RCE bug disclosed last year
- **Impact**: Remote code execution allowing attackers to gain complete control over Internet-facing Gogs instances
- **Status**: Currently unpatched and under active exploitation with over 700 compromised servers identified globally

### Windows RasMan Service Zero-Day
- **Description**: A denial-of-service vulnerability affecting the Windows Remote Access Connection Manager (RasMan) service
- **Impact**: Attackers can crash the RasMan service, disrupting remote access functionality
- **Status**: Zero-day with free unofficial patches available from security researchers

### GeoServer XXE Injection Vulnerability
- **Description**: A critical XML External Entity (XXE) injection vulnerability in OSGeo GeoServer
- **Impact**: Allows attackers to perform XXE attacks potentially leading to data disclosure and system compromise
- **Status**: Actively exploited and added to CISA's Known Exploited Vulnerabilities catalog with mandatory patching deadline for federal agencies

### React Server Components (RSC) Vulnerabilities
- **Description**: Two new types of flaws in React Server Components that can be exploited through the React2Shell vulnerability
- **Impact**: Denial-of-service attacks and source code exposure
- **Status**: Under widespread exploitation forcing CISA to issue emergency mitigation orders with December 12, 2025 patching deadline

### Gladinet CentreStack Cryptographic Flaw
- **Description**: An undocumented vulnerability in the cryptographic algorithm implementation of Gladinet's CentreStack and Triofox products
- **Impact**: Remote code execution on systems using these secure remote file access solutions
- **Status**: Actively exploited in RCE attacks

## Affected Systems and Products

- **Gogs Self-Hosted Git Service**: All versions currently vulnerable with 700+ Internet-facing instances compromised
- **Windows Systems**: RasMan service across multiple Windows versions affected by zero-day DoS vulnerability
- **OSGeo GeoServer**: Critical XXE vulnerability affecting geospatial data servers
- **React Applications**: Applications using React Server Components vulnerable to DoS and source code exposure
- **Gladinet CentreStack/Triofox**: Secure file access platforms with cryptographic implementation flaws
- **Notepad++**: WinGUp update tool vulnerability allowing malicious update delivery (patched in version 8.8.9)
- **VSCode Marketplace**: 19 malicious extensions distributing trojans hidden in fake PNG files

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple unpatched vulnerabilities being actively exploited including Gogs RCE and Windows RasMan DoS
- **XXE Injection**: GeoServer vulnerability exploited through XML External Entity attacks
- **Supply Chain Attacks**: Malicious VSCode extensions and compromised Notepad++ updates targeting developers
- **AI-Enhanced Phishing**: Advanced phishing kits (BlackForce, GhostFrame, InboxPrime AI, Spiderman) using artificial intelligence to bypass MFA
- **OAuth Abuse**: ConsentFix attacks hijacking Microsoft accounts via Azure CLI without passwords or MFA bypass
- **DLL Sideloading**: WIRTE APT group using AshenLoader for sideloading attacks
- **API Abuse**: NANOREMOTE malware leveraging Google Drive API for command and control

## Threat Actor Activities

- **WIRTE APT Group**: Targeting government and diplomatic entities across the Middle East using AshenLoader sideloading to deploy AshTag espionage backdoor
- **Hamas-Linked Hackers**: Probing Middle Eastern diplomatic targets with improved malware capabilities and expanded regional attack scope
- **Supply Chain Attackers**: Targeting developers through malicious VSCode marketplace extensions active since February 2025
- **Phishing Kit Operators**: Deploying AI-enhanced credential theft tools capable of large-scale operations with MFA bypass capabilities
- **Gogs Exploitation Campaign**: Widespread attacks against self-hosted Git services resulting in 700+ compromised servers globally