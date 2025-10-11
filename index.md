# Exploitation Report

Current threat landscape analysis reveals several critical active exploitation campaigns targeting enterprise infrastructure and software products. The most significant concerns include zero-day exploitation of Gladinet CentreStack and TrioFox file sharing software, widespread compromise of SonicWall VPN devices affecting over 100 customer accounts, and sophisticated abuse of legitimate security tools like Velociraptor DFIR by Chinese threat actors in ransomware operations. Additionally, CL0P-linked hackers have exploited Oracle E-Business Suite vulnerabilities to breach dozens of organizations, while various botnets including RondoDox and Aisuru are conducting large-scale exploitation campaigns against edge devices and IoT infrastructure.

## Active Exploitation Details

### Gladinet CentreStack and TrioFox Zero-Day Vulnerability
- **Description**: Local file inclusion vulnerability that can be escalated to remote code execution, allowing attackers to access system files without authentication
- **Impact**: Unauthorized access to sensitive system files and potential complete system compromise
- **Status**: Actively exploited zero-day vulnerability with no patch currently available
- **CVE ID**: CVE-2025-11371

### SonicWall SSL VPN Device Compromise
- **Description**: Widespread compromise of SonicWall SSL VPN infrastructure enabling unauthorized access to multiple customer environments
- **Impact**: Authentication bypass allowing threat actors to access over 100 customer accounts and environments
- **Status**: Active exploitation campaign with widespread impact across multiple organizations

### Oracle E-Business Suite Zero-Day Exploitation
- **Description**: Zero-day vulnerability in Oracle's E-Business Suite software that has been exploited since August 9, 2025
- **Impact**: Complete organizational compromise with dozens of entities affected
- **Status**: Active exploitation by CL0P-linked threat actors with significant organizational impact

### Fortra GoAnywhere MFT Vulnerability
- **Description**: Critical security flaw in GoAnywhere Managed File Transfer software
- **Impact**: Unauthorized access to managed file transfer systems and potential data exfiltration
- **Status**: Previously exploited vulnerability with detailed timeline of exploitation now disclosed
- **CVE ID**: CVE-2025-10035

## Affected Systems and Products

- **SonicWall SSL VPN Devices**: Over 100 customer environments compromised with ongoing authentication bypass attacks
- **Gladinet CentreStack and TrioFox**: File sharing and collaboration platforms vulnerable to zero-day local file inclusion attacks
- **Oracle E-Business Suite**: Enterprise resource planning software targeted in zero-day campaign affecting dozens of organizations
- **Fortra GoAnywhere MFT**: Managed file transfer software previously exploited with detailed attack timeline revealed
- **Consumer Edge Devices**: IoT devices and edge infrastructure targeted by RondoDox botnet exploitation campaigns
- **US ISP Networks**: AT&T, Comcast, and Verizon networks affected by Aisuru botnet leveraging compromised IoT devices
- **Velociraptor DFIR Tool**: Legitimate digital forensics tool weaponized for persistent network access

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple zero-day vulnerabilities actively exploited including Oracle EBS and Gladinet products
- **VPN Infrastructure Compromise**: Authentication bypass techniques targeting SonicWall SSL VPN devices for widespread network access
- **DFIR Tool Weaponization**: Abuse of legitimate Velociraptor forensics tool for persistent access and lateral movement
- **Payroll Diversion Attacks**: HR SaaS account hijacking to redirect employee salary payments to attacker-controlled accounts
- **Botnet Exploitation**: Shotgun approach to exploiting edge device vulnerabilities for DDoS and compromise operations
- **Supply Chain Targeting**: Malicious npm packages (175 packages with 26,000 downloads) used for credential harvesting
- **Social Engineering**: Android spyware campaigns using fake popular app interfaces to target mobile users

## Threat Actor Activities

- **Storm-2603 (CL-CRI-1040)**: Chinese threat group weaponizing Velociraptor DFIR tool in LockBit and Babuk ransomware attacks for persistent network access
- **Storm-2657**: Cybercrime gang conducting "payroll pirate" attacks targeting university HR employees to hijack salary payments since March 2025
- **CL0P-Linked Actors**: Ransomware group exploiting Oracle E-Business Suite zero-day vulnerability affecting dozens of organizations since August 2025
- **ShinyHunters Group**: Operators of BreachForums portal used for Salesforce extortion before FBI takedown, with ongoing extortion threats remaining active
- **RondoDox Botnet Operators**: Conducting widespread exploitation campaigns using shotgun approach against consumer edge devices globally
- **Aisuru Botnet**: Operating world's largest DDoS botnet primarily using compromised IoT devices on US ISP networks for record-breaking attacks