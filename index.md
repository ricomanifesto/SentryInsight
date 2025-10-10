# Exploitation Report

Critical vulnerabilities are under active exploitation across multiple platforms, with threat actors leveraging zero-day flaws and unpatched vulnerabilities to compromise enterprise systems. Notable incidents include active exploitation of Fortra GoAnywhere MFT systems through CVE-2025-10035, zero-day attacks on Gladinet CentreStack and TrioFox products, and large-scale compromise of Oracle E-Business Suite installations. The CL0P ransomware group has exploited Oracle software flaws to breach dozens of organizations, while the RondoDox botnet is actively targeting 56 known vulnerabilities across 30+ device types. Additional threats include malicious npm packages used for credential harvesting, Android spyware campaigns, and authentication bypass vulnerabilities in WordPress themes.

## Active Exploitation Details

### Fortra GoAnywhere MFT Vulnerability
- **Description**: Critical security flaw in GoAnywhere Managed File Transfer software that has been actively exploited in the wild
- **Impact**: Unauthorized access to file transfer systems and potential data exfiltration
- **Status**: Under active investigation by Fortra with timeline of exploitation revealed
- **CVE ID**: CVE-2025-10035

### Gladinet CentreStack and TrioFox Zero-Day
- **Description**: Unpatched security flaw affecting Gladinet CentreStack and TrioFox products, allowing Local File Inclusion (LFI) to Remote Code Execution (RCE) escalation
- **Impact**: Full system compromise and remote code execution capabilities
- **Status**: Zero-day vulnerability under active exploitation with no patch available

### Oracle E-Business Suite Zero-Day
- **Description**: Zero-day security flaw in Oracle's E-Business Suite (EBS) software exploited since August 9, 2025
- **Impact**: Complete system compromise affecting dozens of organizations globally
- **Status**: Active exploitation by CL0P-linked threat actors

### WordPress Service Finder Theme Authentication Bypass
- **Description**: Critical security flaw allowing authentication bypass in WordPress Service Finder theme
- **Impact**: Unauthorized access to any account including administrator privileges
- **Status**: Under active exploitation by threat actors

### RondoDox Botnet Multi-Vulnerability Campaign
- **Description**: Large-scale botnet targeting 56 vulnerabilities across more than 30 distinct device types, including flaws from Pwn2Own competitions
- **Impact**: Device compromise and botnet recruitment for various malicious activities
- **Status**: Active worldwide attacks targeting known vulnerabilities

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: Managed file transfer systems across enterprise environments
- **Gladinet CentreStack**: Cloud storage and file sharing platforms
- **TrioFox**: File access and sharing solutions
- **Oracle E-Business Suite**: Enterprise resource planning software installations
- **WordPress Service Finder Theme**: Website content management systems
- **npm Registry**: JavaScript package management ecosystem with 175 malicious packages
- **Android Devices**: Mobile platforms targeted by ClayRat spyware through fake app distribution
- **SonicWall Firewalls**: All customers using cloud backup services affected by data breach
- **Multiple Device Types**: 30+ distinct devices targeted by RondoDox botnet

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in enterprise software
- **Supply Chain Attacks**: Distribution of 175 malicious npm packages with 26,000+ downloads for credential harvesting
- **Social Engineering**: ClayRat spyware distributed through fake popular apps like WhatsApp, TikTok, and YouTube
- **Authentication Bypass**: Direct circumvention of login mechanisms in WordPress themes
- **Phishing Campaigns**: Spear-phishing operations delivering Go-based implants and espionage malware
- **Botnet Recruitment**: Mass exploitation of known vulnerabilities for device compromise and control
- **Legitimate Tool Abuse**: Usage of Velociraptor DFIR tool in ransomware deployment operations
- **University Targeting**: "Payroll pirate" attacks specifically targeting HR employees in educational institutions

## Threat Actor Activities

- **CL0P Ransomware Group**: Actively exploiting Oracle E-Business Suite zero-day since August 2025, compromising dozens of organizations
- **UTA0388**: China-aligned threat actor conducting spear-phishing campaigns across North America, Asia, and Europe using GOVERSHELL malware
- **Storm-2657**: Cybercrime gang targeting university employees in payroll hijacking attacks since March 2025
- **RondoDox Operators**: Large-scale botnet operation targeting 56 vulnerabilities across global infrastructure
- **ClayRat Campaign**: Android spyware operation targeting Russian users through Telegram channels and phishing websites
- **ShinyHunters/BreachForums**: Data extortion operations until FBI takedown of their portal used for corporate data leaks
- **TwoNet Hacktivists**: Pro-Russian group pivoting from DDoS attacks to critical infrastructure targeting
- **BatShadow Group**: Vietnam-based cybercrime operation behind Vampire Bot malware targeting job seekers