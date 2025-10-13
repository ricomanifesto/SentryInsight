# Exploitation Report

Critical zero-day vulnerabilities are currently under active exploitation across multiple enterprise platforms, with the most severe incidents involving Oracle E-Business Suite (CVE-2025-11371) and Gladinet file sharing software (CVE-2025-11371). CL0P-linked threat actors have successfully breached dozens of organizations through Oracle's EBS software since August 2025, while widespread SonicWall VPN compromises have impacted over 100 customer accounts. Advanced persistent threats are also leveraging legitimate DFIR tools like Velociraptor for ransomware deployment, and sophisticated supply chain attacks are targeting npm repositories with 175 malicious packages affecting 26,000+ downloads.

## Active Exploitation Details

### Oracle E-Business Suite Zero-Day Vulnerability
- **Description**: Critical zero-day vulnerability in Oracle's E-Business Suite software allowing unauthorized access to sensitive data without authentication
- **Impact**: Enables threat actors to breach organizations and access sensitive corporate data, with dozens of organizations confirmed impacted
- **Status**: Under active exploitation since August 9, 2025 by CL0P-linked hackers; Oracle has issued security alerts
- **CVE ID**: CVE-2025-11371

### Gladinet CentreStack and TrioFox Zero-Day
- **Description**: Local file inclusion (LFI) vulnerability that can be escalated to remote code execution (RCE) in Gladinet CentreStack and TrioFox file sharing products
- **Impact**: Allows local attackers to access system files without authentication and potentially achieve remote code execution
- **Status**: Currently unpatched with active in-the-wild exploitation detected by Huntress
- **CVE ID**: CVE-2025-11371

### Fortra GoAnywhere MFT Critical Vulnerability
- **Description**: Critical security flaw in GoAnywhere Managed File Transfer platform
- **Impact**: Enables unauthorized access to managed file transfer systems
- **Status**: Under active exploitation with full investigation timeline revealed by Fortra
- **CVE ID**: CVE-2025-10035

### SonicWall SSL VPN Compromise
- **Description**: Widespread compromise affecting SonicWall SSL VPN devices across multiple customer environments
- **Impact**: Threat actors are authenticating into customer accounts and accessing sensitive network resources
- **Status**: Over 100 customer accounts confirmed compromised with ongoing threat actor access

## Affected Systems and Products

- **Oracle E-Business Suite**: Enterprise resource planning software with widespread corporate deployment
- **Gladinet CentreStack and TrioFox**: File sharing and synchronization platforms used by organizations
- **SonicWall SSL VPN Devices**: Network security appliances providing remote access capabilities
- **Fortra GoAnywhere MFT**: Managed file transfer platforms used for secure data exchange
- **npm Registry**: JavaScript package repository with 175 malicious packages affecting 26,000+ downloads
- **Node.js Applications**: Platforms utilizing Single Executable Application (SEA) features targeted by Stealit malware
- **Android Devices**: Mobile platforms targeted by ClayRat spyware disguised as popular applications
- **IoT Devices**: Internet-of-Things systems compromised for DDoS botnet operations

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in Oracle EBS and Gladinet products
- **VPN Compromise**: Authentication bypass or credential theft targeting SonicWall SSL VPN infrastructure
- **Supply Chain Attacks**: Injection of malicious packages into npm registry for credential harvesting
- **Legitimate Tool Abuse**: Weaponization of Velociraptor DFIR tool for persistent access and ransomware deployment
- **Social Engineering**: Distribution of Android spyware through fake applications mimicking popular services
- **Payroll Hijacking**: Compromise of HR SaaS accounts to redirect employee salary payments
- **DDoS Operations**: Utilization of compromised IoT devices for record-breaking distributed denial-of-service attacks

## Threat Actor Activities

- **CL0P-Linked Groups**: Active exploitation of Oracle E-Business Suite zero-day affecting dozens of organizations since August 2025
- **Storm-2603 (CL-CRI-1040)**: Chinese threat group abusing Velociraptor DFIR tool in LockBit ransomware operations
- **Storm-2657**: Specialized group targeting HR systems and payroll infrastructure for financial theft
- **ShinyHunters**: Cybercrime syndicate operating BreachForums for Salesforce extortion activities before FBI takedown
- **GXC Team**: Dismantled cybercrime syndicate led by Brazilian national "GoogleXcoder" arrested by Spanish authorities
- **Stealit Campaign**: Active malware distribution through compromised game and VPN installers using Node.js SEA features
- **Aisuru Botnet**: Massive DDoS operation targeting US ISPs including AT&T, Comcast, and Verizon with record-breaking attacks
- **ClayRat Operators**: Android spyware campaign impersonating WhatsApp, TikTok, YouTube, and Google Photos applications