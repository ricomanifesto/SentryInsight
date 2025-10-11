# Exploitation Report

The current threat landscape reveals several critical zero-day vulnerabilities under active exploitation, with particularly concerning activity targeting enterprise file sharing systems and Oracle business applications. Most notably, threat actors are exploiting CVE-2025-11371 in Gladinet file sharing software to gain unauthorized system access, while CL0P-linked hackers have compromised dozens of organizations through a zero-day flaw in Oracle's E-Business Suite since August 2025. Additionally, the RondoDox botnet continues its "shotgun" approach to exploiting edge device vulnerabilities, and sophisticated threat actors are leveraging legitimate DFIR tools like Velociraptor for ransomware deployment. The emergence of novel attack vectors includes AI-powered threats, supply chain compromises through malicious npm packages, and targeted payroll hijacking campaigns against universities.

## Active Exploitation Details

### Gladinet CentreStack and TrioFox Zero-Day Vulnerability
- **Description**: A zero-day vulnerability allowing local file inclusion (LFI) to remote code execution (RCE) exploitation in Gladinet CentreStack and TrioFox file sharing products
- **Impact**: Local attackers can access system files without authentication and escalate to remote code execution capabilities
- **Status**: Currently being exploited in the wild with no patch available at the time of disclosure
- **CVE ID**: CVE-2025-11371

### Oracle E-Business Suite Zero-Day Exploitation
- **Description**: A security flaw in Oracle's E-Business Suite (EBS) software being exploited by CL0P-linked threat actors
- **Impact**: Dozens of organizations have been breached, with attackers gaining unauthorized access to enterprise systems
- **Status**: Active exploitation detected since August 9, 2025, with ongoing campaigns targeting multiple organizations

### Fortra GoAnywhere MFT Critical Vulnerability
- **Description**: A critical security flaw in GoAnywhere Managed File Transfer system that came under active exploitation
- **Impact**: Unauthorized access to managed file transfer systems, potentially exposing sensitive data transfers
- **Status**: Exploitation timeline and remediation details have been fully disclosed by Fortra
- **CVE ID**: CVE-2025-10035

## Affected Systems and Products

- **Gladinet CentreStack and TrioFox**: File sharing and synchronization platforms vulnerable to authentication bypass
- **Oracle E-Business Suite (EBS)**: Enterprise resource planning software targeted in widespread zero-day campaign
- **Fortra GoAnywhere MFT**: Managed file transfer solutions affected by critical vulnerability
- **Consumer Edge Devices**: Various IoT and network edge devices targeted by RondoDox botnet
- **npm Registry**: 175 malicious packages with 26,000+ downloads affecting Node.js environments
- **SonicWall Cloud Backup Service**: 100% of firewall configuration backups compromised
- **Windows 11 23H2**: Home and Pro editions reaching end-of-support, creating potential security gaps

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple unpatched vulnerabilities being actively exploited across file sharing and enterprise software
- **Shotgun Approach**: RondoDox botnet employing hit-and-run tactics against diverse edge device vulnerabilities
- **Supply Chain Attacks**: Malicious npm packages used for credential phishing campaigns targeting developer environments
- **DFIR Tool Abuse**: Storm-2603 threat group weaponizing legitimate Velociraptor incident response tool for persistent access
- **AI Agent Exploitation**: Novel attacks targeting AI browser agents and code completion tools like GitHub Copilot
- **Social Engineering**: ClayRat Android spyware disguised as popular applications like WhatsApp, TikTok, and YouTube
- **Node.js SEA Abuse**: Stealit malware leveraging Single Executable Application feature for payload distribution

## Threat Actor Activities

- **Storm-2603**: Chinese threat group using Velociraptor DFIR tool in LockBit and Babuk ransomware attacks for persistent network access
- **Storm-2657**: "Payroll Pirates" specifically targeting university HR employees to hijack salary payments since March 2025
- **CL0P-linked Hackers**: Exploiting Oracle EBS zero-day vulnerability in widespread campaign affecting dozens of organizations
- **ShinyHunters Group**: Operating BreachForums portal for Salesforce extortion until FBI takedown
- **RondoDox Botnet Operators**: Conducting broad-spectrum exploitation campaigns against consumer edge devices worldwide
- **Aisuru Botnet**: Leveraging compromised IoT devices on major US ISPs for record-breaking DDoS attacks