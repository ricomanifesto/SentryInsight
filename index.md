# Exploitation Report

Critical exploitation activity is currently targeting multiple enterprise systems with several zero-day vulnerabilities under active attack. Most concerning are the widespread compromises of SonicWall SSL VPN devices affecting over 100 customer accounts, active exploitation of a zero-day vulnerability in Gladinet file sharing software (CVE-2025-11371), and a zero-day flaw in Oracle's E-Business Suite being exploited by CL0P-linked hackers since August 2025. Additionally, threat actors are weaponizing legitimate security tools like Velociraptor DFIR platform for ransomware deployment, while the Storm-2657 group conducts "payroll pirate" attacks targeting HR systems to redirect employee salaries.

## Active Exploitation Details

### SonicWall SSL VPN Compromise
- **Description**: Widespread compromise of SonicWall SSL VPN devices allowing threat actors to authenticate into multiple customer environments
- **Impact**: Unauthorized access to corporate networks and customer environments across over 100 accounts
- **Status**: Active exploitation detected with widespread impact across multiple organizations

### Gladinet CentreStack and TrioFox Zero-Day
- **Description**: Zero-day vulnerability allowing local attackers to access system files without authentication, escalating from Local File Inclusion (LFI) to Remote Code Execution (RCE)
- **Impact**: Complete system compromise with ability to access sensitive files and execute arbitrary code
- **Status**: Active in-the-wild exploitation detected, currently unpatched
- **CVE ID**: CVE-2025-11371

### Oracle E-Business Suite Zero-Day
- **Description**: Zero-day security flaw in Oracle's E-Business Suite software being exploited by CL0P-linked hackers
- **Impact**: Organizational breaches affecting dozens of companies
- **Status**: Active exploitation since August 9, 2025, targeting multiple organizations

### Fortra GoAnywhere MFT Critical Flaw
- **Description**: Critical security vulnerability in GoAnywhere Managed File Transfer platform
- **Impact**: Potential unauthorized access to managed file transfer systems and sensitive data
- **Status**: Under active exploitation with full investigation timeline revealed
- **CVE ID**: CVE-2025-10035

## Affected Systems and Products

- **SonicWall SSL VPN Devices**: Multiple models and versions experiencing widespread compromise
- **Gladinet CentreStack and TrioFox**: File sharing and collaboration platforms vulnerable to zero-day exploitation
- **Oracle E-Business Suite**: Enterprise resource planning software affected by zero-day attacks
- **Fortra GoAnywhere MFT**: Managed file transfer solutions experiencing critical vulnerabilities
- **Velociraptor DFIR Tool**: Open-source digital forensics platform being weaponized for malicious purposes
- **Consumer Edge Devices**: Various IoT and networking devices targeted by RondoDox botnet
- **npm Registry**: 175 malicious packages with 26,000 downloads targeting developer environments

## Attack Vectors and Techniques

- **VPN Compromise**: Authentication bypass and credential abuse in SonicWall SSL VPN systems
- **Zero-Day Exploitation**: Multiple unpatched vulnerabilities being actively exploited across different platforms
- **Tool Weaponization**: Abuse of legitimate security tools like Velociraptor for persistent access and ransomware deployment
- **Supply Chain Attacks**: Malicious npm packages designed for credential harvesting and data exfiltration
- **Social Engineering**: Malware distribution through fake game and VPN installers using Node.js SEA features
- **Credential Hijacking**: HR system compromises to redirect payroll payments to attacker-controlled accounts

## Threat Actor Activities

- **Storm-2603 (CL-CRI-1040)**: Weaponizing Velociraptor DFIR tool for LockBit and Babuk ransomware deployments with persistent network access
- **Storm-2657**: Conducting "payroll pirate" attacks targeting university HR employees and SaaS accounts to hijack salary payments since March 2025
- **CL0P-Linked Hackers**: Exploiting Oracle E-Business Suite zero-day vulnerability affecting dozens of organizations since August 2025
- **ShinyHunters Group**: Operating BreachForums portal for Salesforce extortion before FBI takedown, with continued extortion activities
- **RondoDox Botnet Operators**: Using "exploit shotgun" approach targeting edge device vulnerabilities globally
- **Aisuru Botnet**: Leveraging compromised IoT devices on major US ISPs (AT&T, Comcast, Verizon) for record-breaking DDoS attacks