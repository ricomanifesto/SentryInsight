# Exploitation Report

Critical exploitation activity is currently impacting multiple enterprise environments through zero-day vulnerabilities and sophisticated attack campaigns. Active exploitation has been observed targeting SonicWall SSL VPN devices with widespread compromise affecting over 100 accounts, while threat actors are exploiting a zero-day vulnerability in Gladinet CentreStack and TrioFox file sharing software to gain unauthorized system access. Additionally, attackers are weaponizing legitimate security tools, including the abuse of Velociraptor DFIR tool in ransomware campaigns by Storm-2603 threat actors. CL0P-linked hackers have successfully breached dozens of organizations through Oracle E-Business Suite vulnerabilities, and the RondoDox botnet continues to target consumer edge devices with a shotgun approach to exploit various vulnerabilities.

## Active Exploitation Details

### Gladinet CentreStack and TrioFox Zero-Day Vulnerability
- **Description**: A local file inclusion (LFI) to remote code execution (RCE) vulnerability allowing local attackers to access system files without authentication
- **Impact**: Attackers can gain unauthorized system access and potentially achieve remote code execution capabilities
- **Status**: Currently being exploited in the wild as a zero-day vulnerability
- **CVE ID**: CVE-2025-11371

### Oracle E-Business Suite Zero-Day Vulnerability
- **Description**: Security flaw in Oracle's E-Business Suite (EBS) software that has been exploited since August 9, 2025
- **Impact**: Dozens of organizations have been breached with potential for significant data compromise
- **Status**: Active exploitation by CL0P-linked threat actors

### SonicWall SSL VPN Compromise
- **Description**: Widespread authentication compromise affecting SonicWall SSL VPN devices
- **Impact**: Threat actors are successfully authenticating into multiple customer environments
- **Status**: Active exploitation with over 100 accounts compromised

### Fortra GoAnywhere Managed File Transfer Vulnerability
- **Description**: Critical security flaw in GoAnywhere Managed File Transfer (MFT) system
- **Impact**: Complete compromise of file transfer operations and potential data exfiltration
- **Status**: Active exploitation confirmed
- **CVE ID**: CVE-2025-10035

## Affected Systems and Products

- **SonicWall SSL VPN Devices**: Multiple customer environments compromised with authentication bypass
- **Gladinet CentreStack and TrioFox**: File sharing software vulnerable to authentication bypass and system file access
- **Oracle E-Business Suite**: Enterprise resource planning software affected by zero-day exploitation
- **Velociraptor DFIR Tool**: Legitimate security tool weaponized for persistence in victim networks
- **Fortra GoAnywhere MFT**: Managed file transfer systems vulnerable to critical exploitation
- **Node.js Applications**: Single Executable Application (SEA) feature abused for malware distribution
- **npm Registry**: 175 malicious packages with 26,000 downloads used for credential harvesting
- **Consumer Edge Devices**: Various IoT and networking equipment targeted by RondoDox botnet
- **Android Devices**: ClayRat spyware targeting devices through fake popular applications

## Attack Vectors and Techniques

- **VPN Authentication Bypass**: Direct authentication compromise of SonicWall SSL VPN systems
- **Zero-Day Exploitation**: Coordinated campaigns targeting unpatched vulnerabilities in enterprise software
- **Tool Weaponization**: Abuse of legitimate security tools like Velociraptor for malicious persistence
- **Supply Chain Attacks**: Malicious npm packages distributed through official repositories
- **Social Engineering**: Malware distribution through fake game and VPN installers
- **Mobile Application Impersonation**: ClayRat spyware masquerading as WhatsApp, TikTok, and YouTube
- **Payroll System Hijacking**: Targeted attacks on HR systems to redirect salary payments
- **DDoS Amplification**: IoT device compromise for large-scale distributed denial of service attacks

## Threat Actor Activities

- **Storm-2603 (CL-CRI-1040)**: Chinese threat group deploying LockBit and Babuk ransomware using weaponized Velociraptor DFIR tool for network persistence
- **CL0P-linked Hackers**: Ransomware operators exploiting Oracle E-Business Suite zero-day vulnerability to breach dozens of organizations since August 2025
- **Storm-2657**: Cybercrime gang conducting "payroll pirate" attacks targeting university HR employees to hijack salary payments since March 2025
- **ShinyHunters Group**: Cybercriminal organization operating BreachForums for data extortion, recently disrupted by FBI takedown
- **RondoDox Botnet Operators**: Threat actors using hit-and-run tactics to exploit vulnerabilities in consumer edge devices globally
- **Stealit Campaign Operators**: Malware distributors leveraging Node.js Single Executable Application feature through game and VPN installers
- **Aisuru Botnet Controllers**: Operating the world's largest disruptive botnet primarily using compromised IoT devices from major US ISPs