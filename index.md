# Exploitation Report

Current cybersecurity landscape reveals several critical active exploitation campaigns targeting enterprise infrastructure and file-sharing systems. The most significant threats include zero-day exploitation of Gladinet CentreStack and TrioFox products (CVE-2025-11371), widespread compromise of SonicWall SSL VPN devices affecting over 100 accounts, and Oracle E-Business Suite zero-day exploitation by CL0P-linked threat actors. Additionally, threat actors are weaponizing legitimate DFIR tools like Velociraptor for ransomware deployment, while the massive Aisuru botnet is launching record-breaking DDoS attacks using compromised IoT devices.

## Active Exploitation Details

### Gladinet CentreStack and TrioFox Zero-Day Vulnerability
- **Description**: Local file inclusion (LFI) vulnerability that escalates to remote code execution (RCE), allowing attackers to access system files without authentication
- **Impact**: Complete system compromise, unauthorized access to sensitive files, potential for lateral movement within networks
- **Status**: Actively exploited in the wild, currently unpatched
- **CVE ID**: CVE-2025-11371

### Fortra GoAnywhere Managed File Transfer Critical Flaw
- **Description**: Critical security vulnerability in GoAnywhere MFT that has undergone active exploitation
- **Impact**: Potential unauthorized access to managed file transfer systems and sensitive data
- **Status**: Exploitation detected and patched following investigation
- **CVE ID**: CVE-2025-10035

### Oracle E-Business Suite Zero-Day Exploitation
- **Description**: Zero-day vulnerability in Oracle's E-Business Suite software that has been actively exploited since August 9, 2025
- **Impact**: Organizational breaches affecting dozens of entities, potential data theft and system compromise
- **Status**: Active exploitation by CL0P-linked hackers, patch status unclear

### SonicWall SSL VPN Widespread Compromise
- **Description**: Authentication bypass or credential compromise affecting SonicWall SSL VPN devices
- **Impact**: Unauthorized network access, potential lateral movement, compromise of multiple customer environments
- **Status**: Actively exploited across more than 100 accounts, widespread campaign detected

## Affected Systems and Products

- **Gladinet CentreStack and TrioFox**: File sharing and collaboration platforms vulnerable to LFI/RCE attacks
- **SonicWall SSL VPN Devices**: Network security appliances compromised for unauthorized access
- **Oracle E-Business Suite**: Enterprise resource planning software targeted in zero-day attacks
- **Fortra GoAnywhere MFT**: Managed file transfer solutions affected by critical vulnerability
- **Consumer Edge Devices**: Targeted by RondoDox botnet using exploit shotgun approach
- **IoT Devices on US ISPs**: Compromised devices on AT&T, Comcast, and Verizon networks used in DDoS attacks
- **npm Registry Packages**: 175 malicious packages with 26,000 downloads used for credential harvesting

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in enterprise software
- **VPN Compromise**: Authentication bypass techniques targeting SSL VPN infrastructure
- **DFIR Tool Weaponization**: Abuse of Velociraptor digital forensics tool for persistent access and ransomware deployment
- **Supply Chain Attacks**: Malicious npm packages distributing credential harvesting malware
- **Social Engineering**: Targeting HR employees for payroll redirection attacks
- **Botnet DDoS**: Massive distributed denial of service attacks using compromised IoT devices
- **Malware Distribution**: Stealit malware leveraging Node.js Single Executable Application feature through game and VPN installers

## Threat Actor Activities

- **Storm-2603 (CL-CRI-1040)**: Chinese threat group weaponizing Velociraptor DFIR tool in LockBit and Babuk ransomware attacks
- **Storm-2657**: "Payroll pirates" targeting university HR employees to hijack salary payments since March 2025
- **CL0P-linked Hackers**: Exploiting Oracle E-Business Suite zero-day affecting dozens of organizations since August 2025
- **ShinyHunters Group**: Operating BreachForums for data extortion, recently disrupted by FBI takedown
- **RondoDox Botnet Operators**: Running exploit shotgun campaigns against consumer edge devices worldwide
- **Aisuru Botnet**: Orchestrating record-breaking DDoS attacks using compromised US ISP-hosted IoT devices
- **Unknown Threat Actors**: Conducting widespread SonicWall VPN compromise affecting 100+ accounts and actively exploiting Gladinet/TrioFox zero-day