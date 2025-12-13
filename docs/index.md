# Exploitation Report

Critical zero-day vulnerabilities are being actively exploited across multiple platforms, with Apple releasing emergency patches for two WebKit zero-days used in sophisticated attacks, while widespread exploitation of React2Shell, GeoServer XXE, and Windows RasMan vulnerabilities continues to impact organizations globally. The React2Shell vulnerability has escalated into large-scale global attacks forcing emergency mitigation measures from CISA, while attackers are also leveraging supply chain attacks through malicious GitHub repositories and VSCode Marketplace extensions to distribute remote access trojans and other malware.

## Active Exploitation Details

### **Apple WebKit Zero-Day Vulnerabilities**
- **Description**: Two zero-day vulnerabilities in WebKit affecting iOS, iPadOS, macOS, tvOS, watchOS, visionOS, and Safari
- **Impact**: Exploitation in sophisticated attacks targeting specific individuals
- **Status**: Emergency security updates released by Apple

### **React2Shell Vulnerability**
- **Description**: Critical vulnerability enabling remote code execution through React Server Components
- **Impact**: Large-scale global attacks with denial-of-service and source code exposure capabilities
- **Status**: Under active exploitation with CISA-mandated patching deadline of December 12, 2025
- **CVE ID**: CVE-2025-55182

### **GeoServer XXE Vulnerability**
- **Description**: XML External Entity (XXE) injection vulnerability in OSGeo GeoServer
- **Impact**: Allows attackers to perform XXE injection attacks
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog due to active exploitation

### **Windows RasMan Zero-Day**
- **Description**: Zero-day vulnerability affecting Windows Remote Access Connection Manager (RasMan) service
- **Impact**: Allows attackers to crash the RasMan service leading to denial of service
- **Status**: Currently unpatched by Microsoft, but unofficial patches available

### **Gladinet CentreStack Cryptographic Flaw**
- **Description**: Undocumented vulnerability in cryptographic algorithm implementation
- **Impact**: Remote code execution attacks against secure remote file access systems
- **Status**: Actively exploited in RCE attacks

## Affected Systems and Products

- **Apple Products**: iOS, iPadOS, macOS, tvOS, watchOS, visionOS, and Safari web browser
- **React Applications**: Applications using React Server Components (RSC)
- **GeoServer**: OSGeo GeoServer installations
- **Windows Systems**: Windows machines running Remote Access Connection Manager service
- **Gladinet Products**: CentreStack and Triofox secure file access solutions
- **Development Tools**: VSCode Marketplace extensions and GitHub repositories
- **Notepad++**: WinGUp update tool component

## Attack Vectors and Techniques

- **WebKit Exploitation**: Sophisticated attacks targeting specific individuals through web browsers
- **XXE Injection**: XML External Entity attacks against GeoServer implementations
- **Supply Chain Attacks**: Malicious GitHub repositories distributing PyStoreRAT malware and fake VSCode extensions
- **Social Engineering**: Fake torrents hiding malware in subtitle files targeting popular movies
- **Phishing Campaigns**: Advanced phishing kits using AI and MFA bypass tactics
- **Remote Code Execution**: Exploitation of cryptographic flaws in file access systems
- **Update Mechanism Abuse**: Manipulation of software update processes to deliver malicious payloads

## Threat Actor Activities

- **Hamas-Linked Hackers**: Targeting Middle Eastern diplomats with improved malware capabilities and wider regional attack scope
- **Supply Chain Attackers**: Leveraging GitHub Actions and VSCode Marketplace for distributing malware through legitimate-appearing repositories
- **Phishing Kit Operators**: Deploying BlackForce, GhostFrame, InboxPrime AI, and Spiderman kits for large-scale credential theft
- **Malware Distributors**: Using fake movie torrents and subtitle files to spread Agent Tesla RAT malware
- **Insider Threats**: Former employees retaining system access leading to data breaches affecting millions of customers