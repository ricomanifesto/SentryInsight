# Exploitation Report

Current cybersecurity landscape reveals multiple critical zero-day vulnerabilities under active exploitation, including CVE-2025-11371 in Gladinet file sharing software and CVE-2025-10035 in Fortra's GoAnywhere MFT platform. Threat actors are demonstrating sophisticated techniques by weaponizing legitimate tools like Velociraptor DFIR software for ransomware operations, while widespread SonicWall VPN compromises affect over 100 accounts across multiple organizations. Additional campaigns leverage GitHub infrastructure for banking trojan operations and Discord channels for backdoor command and control, highlighting the evolution of attack methodologies targeting enterprise environments.

## Active Exploitation Details

### Gladinet CentreStack and TrioFox Zero-Day Vulnerability
- **Description**: A zero-day vulnerability allowing local attackers to access system files without authentication, escalating from Local File Inclusion (LFI) to Remote Code Execution (RCE)
- **Impact**: Unauthorized access to sensitive system files and potential remote code execution capabilities
- **Status**: Currently unpatched with active in-the-wild exploitation detected
- **CVE ID**: CVE-2025-11371

### Fortra GoAnywhere MFT Critical Vulnerability
- **Description**: Critical security flaw in GoAnywhere Managed File Transfer platform under active exploitation
- **Impact**: Complete compromise of file transfer systems and potential data exfiltration
- **Status**: Active exploitation confirmed, patch timeline investigation completed
- **CVE ID**: CVE-2025-10035

### SonicWall SSL VPN Compromise
- **Description**: Widespread compromise of SonicWall SSL VPN devices allowing unauthorized access to customer environments
- **Impact**: Threat actors authenticating into multiple accounts across over 100 affected organizations
- **Status**: Active compromise affecting multiple customer environments

### RondoDox Botnet Edge Device Exploitation
- **Description**: Botnet taking a "shotgun approach" to exploiting vulnerabilities in consumer edge devices globally
- **Impact**: Large-scale compromise of consumer networking equipment for botnet operations
- **Status**: Active exploitation using hit-and-run tactics

## Affected Systems and Products

- **Gladinet CentreStack and TrioFox**: File sharing and collaboration platforms vulnerable to authentication bypass
- **Fortra GoAnywhere MFT**: Managed file transfer solutions compromised through critical vulnerability
- **SonicWall SSL VPN Devices**: Enterprise VPN infrastructure across multiple organizations
- **Oracle E-Business Suite**: Enterprise resource planning systems vulnerable to unauthorized data access
- **Consumer Edge Devices**: Routers, IoT devices, and networking equipment targeted by RondoDox botnet
- **Internet-of-Things (IoT) Devices**: Compromised devices on major US ISPs including AT&T, Comcast, and Verizon
- **npm Package Registry**: 175 malicious packages with over 26,000 downloads for credential harvesting

## Attack Vectors and Techniques

- **GitHub Infrastructure Abuse**: Astaroth banking trojan using GitHub repositories as operational backbone for resilience
- **Discord C2 Communications**: ChaosBot backdoor leveraging Discord channels for command and control operations
- **Legitimate Tool Weaponization**: Velociraptor DFIR tool abused by Storm-2603 for LockBit ransomware attacks
- **Supply Chain Attacks**: Malicious npm packages disguised as legitimate software for credential phishing
- **Social Engineering**: Fake "Inflation Refund" SMS campaigns targeting New York residents
- **Node.js SEA Exploitation**: Stealit malware abusing Node.js Single Executable Application feature
- **DDoS Infrastructure**: Aisuru botnet conducting record-breaking distributed denial of service attacks
- **Authentication Bypass**: Zero-day vulnerabilities allowing unauthorized system access

## Threat Actor Activities

- **Storm-2603 (CL-CRI-1040)**: Chinese threat group weaponizing Velociraptor DFIR tool for LockBit ransomware operations and persistent network access
- **Storm-2657 "Payroll Pirates"**: Threat actor hijacking HR SaaS accounts to redirect employee salary payments to attacker-controlled accounts
- **GXC Team**: Brazilian-led cybercrime syndicate dismantled by Spanish authorities, with 25-year-old leader "GoogleXcoder" arrested
- **ShinyHunters**: Cybercrime group operating BreachForums portal for Salesforce data extortion before FBI takedown
- **Astaroth Operators**: Banking trojan campaign using GitHub for infrastructure resilience after previous takedowns
- **ChaosBot Developers**: Rust-based backdoor creators using Discord for covert command and control operations
- **Aisuru Botnet Operators**: Large-scale DDoS operation compromising IoT devices across major US internet service providers