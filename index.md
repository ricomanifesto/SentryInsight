# Exploitation Report

Critical exploitation activity is currently targeting multiple enterprise environments through zero-day vulnerabilities and sophisticated attack techniques. Active exploitation includes a zero-day vulnerability in Gladinet file sharing software allowing local attackers to access system files without authentication, widespread compromise of SonicWall SSL VPN devices affecting over 100 customer accounts, and zero-day exploitation of Oracle E-Business Suite software potentially impacting dozens of organizations. Threat actors are also weaponizing legitimate tools like Velociraptor DFIR software for ransomware deployment and conducting targeted payroll diversion attacks against university employees.

## Active Exploitation Details

### Gladinet CentreStack and TrioFox Zero-Day Vulnerability
- **Description**: A zero-day vulnerability allowing local file inclusion (LFI) to remote code execution (RCE) exploitation
- **Impact**: Local attackers can access system files without authentication and potentially execute remote code
- **Status**: Currently being actively exploited in the wild; unpatched at time of reporting
- **CVE ID**: CVE-2025-11371

### Oracle E-Business Suite Zero-Day Exploitation
- **Description**: Security flaw in Oracle's E-Business Suite (EBS) software being exploited by CL0P-linked hackers
- **Impact**: Complete organizational compromise allowing data theft and system access
- **Status**: Active exploitation since August 9, 2025, affecting dozens of organizations
- **CVE ID**: CVE-2025-10035

### SonicWall SSL VPN Compromise
- **Description**: Widespread compromise of SonicWall SSL VPN devices allowing unauthorized access to customer environments
- **Impact**: Authentication bypass enabling access to multiple customer accounts and networks
- **Status**: Active exploitation affecting over 100 accounts across multiple organizations

## Affected Systems and Products

- **Gladinet CentreStack and TrioFox**: File sharing software products vulnerable to local file inclusion attacks
- **Oracle E-Business Suite**: Enterprise resource planning software targeted in zero-day attacks
- **SonicWall SSL VPN Devices**: Network security appliances compromised for unauthorized access
- **Velociraptor DFIR Tool**: Digital forensics tool being weaponized for ransomware deployment
- **npm Registry**: 175 malicious packages with 26,000 downloads used for credential harvesting
- **University HR Systems**: Payroll and human resources systems targeted for salary diversion

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched vulnerabilities in enterprise software
- **VPN Compromise**: Authentication bypass techniques targeting SSL VPN infrastructure
- **Tool Weaponization**: Legitimate DFIR tools repurposed for malicious ransomware deployment
- **Supply Chain Attacks**: Malicious npm packages distributed to harvest credentials
- **Social Engineering**: Targeted attacks against HR personnel for payroll manipulation
- **Mobile Malware**: Android spyware masquerading as legitimate applications like WhatsApp and TikTok

## Threat Actor Activities

- **Storm-2603 (CL-CRI-1040)**: Chinese threat group weaponizing Velociraptor tool for LockBit and Babuk ransomware attacks
- **Storm-2657**: Cybercrime group conducting "payroll pirate" attacks targeting university employees since March 2025
- **CL0P-Linked Hackers**: Ransomware group exploiting Oracle EBS zero-day vulnerability affecting dozens of organizations
- **ShinyHunters Group**: Operating BreachForums portal for corporate data leaks and Salesforce extortion activities
- **RondoDox Botnet**: Employing "exploit shotgun" approach targeting consumer edge devices globally
- **Aisuru DDoS Botnet**: Compromising IoT devices on major US ISPs including AT&T, Comcast, and Verizon for record-breaking DDoS attacks