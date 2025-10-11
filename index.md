# Exploitation Report

The cybersecurity landscape is experiencing intense exploitation activity across multiple critical vulnerabilities, with several zero-day attacks targeting enterprise systems. Most concerning is the active exploitation of CVE-2025-11371 in Gladinet file sharing software, allowing attackers to escalate from local file inclusion to remote code execution without authentication. Additionally, CVE-2025-10035 in Fortra's GoAnywhere MFT has been actively exploited, while threat actors linked to the CL0P ransomware group have been exploiting an Oracle E-Business Suite zero-day since August 2025. The RondoDox botnet continues its widespread exploitation of edge device vulnerabilities, and sophisticated threat groups are weaponizing legitimate tools like Velociraptor DFIR for ransomware deployment.

## Active Exploitation Details

### Gladinet CentreStack and TrioFox Zero-Day Vulnerability
- **Description**: A zero-day vulnerability allowing local attackers to access system files without authentication, escalating from local file inclusion (LFI) to remote code execution (RCE)
- **Impact**: Unauthorized access to system files, potential for complete system compromise and remote code execution
- **Status**: Actively exploited in the wild, currently unpatched
- **CVE ID**: CVE-2025-11371

### Fortra GoAnywhere MFT Critical Security Flaw
- **Description**: Critical security vulnerability in GoAnywhere Managed File Transfer software that has been actively exploited
- **Impact**: Potential compromise of file transfer systems and sensitive data exposure
- **Status**: Under active exploitation, full timeline of exploitation disclosed by Fortra
- **CVE ID**: CVE-2025-10035

### Oracle E-Business Suite Zero-Day Exploitation
- **Description**: Zero-day security flaw in Oracle's E-Business Suite (EBS) software that has been exploited by CL0P-linked hackers
- **Impact**: Dozens of organizations compromised, potential data theft and system compromise
- **Status**: Actively exploited since August 9, 2025 by threat actors linked to CL0P ransomware group

### RondoDox Botnet Edge Device Vulnerabilities
- **Description**: Widespread exploitation of vulnerabilities in consumer edge devices using a "hit-and-run, shotgun approach"
- **Impact**: Compromise of edge devices worldwide, potential botnet recruitment
- **Status**: Ongoing active exploitation campaign targeting consumer edge infrastructure

## Affected Systems and Products

- **Gladinet CentreStack and TrioFox**: File sharing software products vulnerable to authentication bypass and RCE
- **Fortra GoAnywhere MFT**: Managed File Transfer solutions experiencing critical exploitation
- **Oracle E-Business Suite (EBS)**: Enterprise business software targeted in zero-day attacks
- **Consumer Edge Devices**: Various edge devices worldwide targeted by RondoDox botnet
- **Windows 11 23H2 Home and Pro**: Approaching end-of-support status creating security risks
- **SonicWall Firewall Systems**: 100% of cloud backup configurations compromised in recent breach
- **npm Package Registry**: 175 malicious packages with 26,000 downloads used for credential harvesting

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple unpatched vulnerabilities being actively exploited across enterprise software
- **Authentication Bypass**: Local attackers accessing system files without proper authentication in Gladinet products
- **Supply Chain Attacks**: Malicious npm packages used for credential phishing and harvesting
- **Legitimate Tool Abuse**: Velociraptor DFIR tool weaponized for ransomware deployment by Storm-2603
- **Social Engineering**: ClayRat Android spyware masquerading as popular applications like WhatsApp and TikTok
- **AI-Powered Attacks**: CamoLeak attack targeting GitHub Copilot for data exfiltration
- **Node.js SEA Abuse**: Stealit malware leveraging Single Executable Application feature for payload distribution

## Threat Actor Activities

- **Storm-2603**: Chinese hackers using Velociraptor DFIR tool in LockBit and Babuk ransomware attacks
- **Storm-2657**: "Payroll Pirates" targeting university HR employees to hijack salary payments since March 2025
- **CL0P-Linked Hackers**: Exploiting Oracle EBS zero-day to breach dozens of organizations
- **ShinyHunters Group**: Operating BreachForums portal for Salesforce extortion before FBI takedown
- **RondoDox Operators**: Conducting widespread botnet campaigns against edge devices globally
- **Stealit Campaign**: Distributing malware through game and VPN installers using Node.js exploitation
- **ClayRat Developers**: Creating Android spyware campaigns targeting users through app impersonation
- **Aisuru Botnet**: Launching record-breaking DDoS attacks against US ISPs using compromised IoT devices