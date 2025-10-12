# Exploitation Report

Current cybersecurity activities reveal several critical exploitation campaigns targeting enterprise infrastructure and file-sharing systems. Most notably, threat actors are actively exploiting zero-day vulnerabilities in Gladinet CentreStack and TrioFox products (CVE-2025-11371) that allow unauthorized system file access, while Oracle E-Business Suite systems face widespread compromise through zero-day exploitation affecting dozens of organizations. Additionally, Storm-2603 has weaponized legitimate digital forensics tools in ransomware operations, and multiple VPN infrastructure compromises are enabling broad network access across enterprise environments.

## Active Exploitation Details

### Gladinet CentreStack and TrioFox Zero-Day
- **Description**: Local file inclusion vulnerability enabling unauthorized access to system files without authentication
- **Impact**: Attackers can escalate from local file inclusion to remote code execution, gaining complete system control
- **Status**: Currently being actively exploited in the wild with no patch available
- **CVE ID**: CVE-2025-11371

### Oracle E-Business Suite Zero-Day
- **Description**: Critical security flaw in Oracle's E-Business Suite software enabling unauthorized access
- **Impact**: Mass compromise affecting dozens of organizations with potential data exfiltration and system access
- **Status**: Active exploitation detected since August 9, 2025, linked to CL0P ransomware operations
- **CVE ID**: Not specified in articles

### Fortra GoAnywhere MFT Vulnerability
- **Description**: Critical security flaw in GoAnywhere Managed File Transfer system
- **Impact**: Enables unauthorized file transfer system access and potential data exfiltration
- **Status**: Under active exploitation with full timeline investigation completed
- **CVE ID**: CVE-2025-10035

### SonicWall SSL VPN Compromise
- **Description**: Widespread compromise of SonicWall SSL VPN devices enabling persistent network access
- **Impact**: Threat actors authenticating into multiple customer environments through compromised VPN infrastructure
- **Status**: Active widespread compromise affecting over 100 accounts
- **CVE ID**: Not specified in articles

## Affected Systems and Products

- **Gladinet CentreStack and TrioFox**: File sharing and cloud storage solutions vulnerable to authentication bypass
- **Oracle E-Business Suite**: Enterprise resource planning software experiencing zero-day exploitation
- **SonicWall SSL VPN Devices**: Network access appliances compromised for persistent access
- **Fortra GoAnywhere MFT**: Managed file transfer solutions under active attack
- **Consumer Edge Devices**: IoT and networking devices targeted by RondoDox botnet operations
- **Node.js Applications**: Single Executable Applications abused for malware distribution
- **npm Registry Packages**: 175 malicious packages with 26,000 downloads facilitating credential harvesting

## Attack Vectors and Techniques

- **Digital Forensics Tool Abuse**: Storm-2603 weaponizing Velociraptor DFIR tool for persistent access and ransomware deployment
- **Zero-Day Exploitation**: Multiple unpatched vulnerabilities being actively exploited for initial access
- **Supply Chain Attacks**: Malicious npm packages distributed through legitimate software repositories
- **VPN Infrastructure Compromise**: Mass compromise of enterprise VPN systems for network persistence
- **Social Engineering**: Payroll piracy attacks targeting HR employees through account takeover
- **Malware Distribution**: Stealit malware campaign using Node.js features via game and VPN installers
- **Shotgun Exploit Approach**: RondoDox botnet using automated vulnerability scanning against edge devices

## Threat Actor Activities

- **Storm-2603 (CL-CRI-1040)**: Chinese threat group conducting ransomware operations using legitimate security tools like Velociraptor for LockBit and Babuk deployment
- **Storm-2657**: Cybercrime group executing "payroll pirate" attacks against university HR systems to divert salary payments since March 2025
- **CL0P-Linked Actors**: Ransomware operators exploiting Oracle E-Business Suite zero-day vulnerabilities affecting dozens of organizations
- **ShinyHunters**: Cybercrime group operating BreachForums portal for data extortion, particularly targeting Salesforce environments before FBI takedown
- **Aisuru Botnet Operators**: Managing world's largest DDoS botnet primarily composed of compromised IoT devices on US ISP networks
- **Unknown Threat Actors**: Conducting widespread SonicWall VPN compromise campaign affecting over 100 enterprise accounts