# Exploitation Report

The cybersecurity landscape is experiencing intense exploitation activity across multiple attack vectors, with several critical vulnerabilities under active attack. Most concerning is the zero-day exploitation of Gladinet CentreStack and TrioFox products, where attackers are escalating from Local File Inclusion (LFI) to Remote Code Execution (RCE). The CL0P ransomware group has leveraged a zero-day flaw in Oracle E-Business Suite to breach dozens of organizations since August 2025. Additionally, threat actors are weaponizing legitimate tools like Node.js Single Executable Applications and the Velociraptor DFIR platform for malicious purposes, while large-scale campaigns targeting npm packages and Android platforms continue to proliferate.

## Active Exploitation Details

### Gladinet CentreStack and TrioFox Zero-Day Vulnerability
- **Description**: An unpatched security flaw allowing attackers to escalate from Local File Inclusion (LFI) to Remote Code Execution (RCE)
- **Impact**: Complete system compromise through remote code execution capabilities
- **Status**: Zero-day vulnerability with active in-the-wild exploitation detected by Huntress

### Oracle E-Business Suite Zero-Day Flaw
- **Description**: Critical security vulnerability in Oracle's E-Business Suite (EBS) software
- **Impact**: System compromise leading to data breaches across multiple organizations
- **Status**: Zero-day exploitation ongoing since August 9, 2025, with dozens of organizations impacted

### Fortra GoAnywhere MFT Critical Vulnerability
- **Description**: Critical security flaw in GoAnywhere Managed File Transfer platform
- **Impact**: Unauthorized access to file transfer systems and potential data exfiltration
- **Status**: Active exploitation detected and investigated by Fortra
- **CVE ID**: CVE-2025-10035

### RondoDox Botnet N-Day Exploitation
- **Description**: Large-scale botnet targeting 56 known vulnerabilities across more than 30 distinct device types
- **Impact**: Botnet recruitment and potential data theft or system compromise
- **Status**: Active worldwide attacks exploiting previously disclosed vulnerabilities, including Pwn2Own competition findings

## Affected Systems and Products

- **Gladinet CentreStack**: File sharing and collaboration platform vulnerable to LFI-to-RCE exploitation
- **TrioFox**: Cloud file server platform affected by the same zero-day vulnerability
- **Oracle E-Business Suite**: Enterprise resource planning software compromised in CL0P attacks
- **Fortra GoAnywhere MFT**: Managed file transfer solution with critical vulnerability
- **npm Registry**: 175 malicious packages with 26,000 downloads used for credential harvesting
- **Android Devices**: Targeted by ClayRat spyware and other malicious applications
- **SonicWall Cloud Backup Service**: All customer firewall configuration backups potentially compromised
- **Node.js Applications**: Single Executable Application feature abused for malware distribution
- **University HR Systems**: Targeted in "payroll pirate" attacks by Storm-2657
- **Multiple IoT and Network Devices**: Over 30 device types targeted by RondoDox botnet

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active use of unpatched vulnerabilities in Gladinet, TrioFox, and Oracle EBS
- **Supply Chain Attacks**: Malicious npm packages used to harvest credentials from developers
- **Social Engineering**: Storm-2657 targeting HR employees to redirect payroll payments
- **Mobile Malware Distribution**: ClayRat spyware distributed through fake popular app installers
- **Legitimate Tool Abuse**: Velociraptor DFIR tool repurposed for ransomware deployment
- **Node.js SEA Exploitation**: Stealit malware campaign leveraging Single Executable Application feature
- **Multi-Vector Botnet Operations**: RondoDox targeting 56 vulnerabilities across diverse platforms
- **Cloud Service Compromise**: SonicWall backup service breach affecting all customers
- **AI-Powered Attacks**: CamoLeak technique targeting GitHub Copilot for data exfiltration

## Threat Actor Activities

- **CL0P Ransomware Group**: Actively exploiting Oracle E-Business Suite zero-day since August 2025, targeting dozens of organizations
- **Storm-2657**: Conducting "payroll pirate" attacks against university HR employees to hijack salary payments since March 2025
- **UTA0388**: China-aligned threat actor using spear-phishing campaigns to deliver GOVERSHELL malware across North America, Asia, and Europe
- **Stealit Campaign Operators**: Distributing malware through game and VPN installers using Node.js SEA feature
- **ClayRat Operators**: Targeting Android users in Russia through Telegram channels and phishing websites
- **RondoDox Botnet Controllers**: Operating large-scale botnet infrastructure targeting 56 vulnerabilities globally
- **ShinyHunters Group**: Operating BreachForums portal for corporate data leaks before FBI takedown
- **npm Package Attackers**: Deploying 175 malicious packages for credential harvesting operations