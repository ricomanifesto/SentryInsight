# Exploitation Report

Current security intelligence reveals multiple active zero-day exploitations and sophisticated threat actor campaigns targeting enterprise systems globally. Most critically, threat actors are actively exploiting CVE-2025-11371 in Gladinet file sharing software and CVE-2025-10035 in GoAnywhere Managed File Transfer systems. Oracle E-Business Suite has also fallen victim to zero-day exploitation with CL0P-linked hackers breaching dozens of organizations since August 2025. Additionally, widespread compromise of SonicWall SSL VPN devices has impacted over 100 customer environments, while sophisticated malware campaigns abuse legitimate tools like Velociraptor DFIR and Node.js features for persistent access and ransomware deployment.

## Active Exploitation Details

### Gladinet CentreStack and TrioFox Zero-Day
- **Description**: Local file inclusion vulnerability that allows attackers to access system files without authentication, escalating to remote code execution
- **Impact**: Unauthorized system file access, potential complete system compromise through RCE escalation
- **Status**: Actively exploited in the wild, currently unpatched
- **CVE ID**: CVE-2025-11371

### GoAnywhere Managed File Transfer Critical Flaw
- **Description**: Critical security vulnerability in Fortra's GoAnywhere MFT system enabling unauthorized access
- **Impact**: Complete system compromise and potential data exfiltration from managed file transfer systems
- **Status**: Under active exploitation with full timeline disclosed by vendor
- **CVE ID**: CVE-2025-10035

### Oracle E-Business Suite Zero-Day
- **Description**: Authentication bypass vulnerability allowing unauthorized access to sensitive data without login credentials
- **Impact**: Direct access to sensitive enterprise data and business systems
- **Status**: Zero-day exploitation ongoing since August 9, 2025, affecting dozens of organizations

### SonicWall SSL VPN Mass Compromise
- **Description**: Widespread authentication bypass affecting SSL VPN devices across multiple customer environments
- **Impact**: Unauthorized network access and potential lateral movement across compromised environments
- **Status**: Active compromise affecting over 100 customer accounts

## Affected Systems and Products

- **Oracle E-Business Suite**: Enterprise resource planning systems globally compromised through zero-day exploitation
- **Gladinet CentreStack/TrioFox**: File sharing and collaboration platforms vulnerable to unauthenticated access
- **GoAnywhere MFT**: Managed file transfer systems in enterprise environments
- **SonicWall SSL VPN**: Network security appliances providing remote access capabilities
- **Windows 11 23H2**: Home and Pro editions reaching end of support, creating security gaps
- **Consumer IoT Devices**: Compromised devices on major US ISPs including AT&T, Comcast, and Verizon
- **npm Registry**: 175 malicious packages with 26,000+ downloads targeting developers

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in enterprise software
- **Authentication Bypass**: Circumventing login mechanisms to gain unauthorized system access
- **Tool Abuse**: Weaponizing legitimate DFIR tools like Velociraptor for malicious persistence
- **Supply Chain Attacks**: Poisoning npm packages to target software developers and their environments
- **Social Engineering**: Fake government refund schemes targeting New York residents
- **Credential Harvesting**: Hijacking HR SaaS accounts to redirect employee salary payments
- **IoT Botnet Recruitment**: Compromising consumer devices for large-scale DDoS operations
- **Malware Distribution**: Abusing Node.js Single Executable features through game and VPN installers

## Threat Actor Activities

- **CL0P-Linked Groups**: Orchestrating zero-day exploitation campaigns against Oracle E-Business Suite since August 2025
- **Storm-2603**: Abusing Velociraptor DFIR tools in LockBit ransomware operations and persistent network access
- **Storm-2657**: Conducting "Payroll Pirates" operations targeting HR systems to steal employee salaries
- **ShinyHunters**: Operating BreachForums for corporate data leaks and Salesforce extortion before FBI takedown
- **GXC Team**: Brazilian-led cybercrime syndicate dismantled by Spanish authorities
- **RondoDox Operators**: Managing global botnet using "exploit shotgun" approach against edge devices
- **Aisuru Botnet**: Conducting record-breaking DDoS attacks using compromised US ISP infrastructure
- **Stealit Campaign**: Distributing malware through Node.js applications disguised as games and VPN software