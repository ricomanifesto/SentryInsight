# Exploitation Report

Critical exploitation activity is currently targeting enterprise infrastructure with multiple active campaigns. Threat actors are exploiting a zero-day vulnerability in Gladinet file sharing software (CVE-2025-11371) that allows local attackers to access system files without authentication. The RondoDox botnet has escalated its operations, weaponizing over 50 vulnerabilities across more than 30 vendors in what researchers describe as an "exploit shotgun" approach. Additionally, widespread compromise of SonicWall SSL VPN devices has impacted over 100 accounts, while attackers continue exploiting a critical GoAnywhere Managed File Transfer vulnerability (CVE-2025-10035). Microsoft has also responded to credible reports of threat actors abusing Internet Explorer mode in Edge browser as a backdoor mechanism.

## Active Exploitation Details

### Gladinet CentreStack and Triofox Zero-Day
- **Description**: A zero-day vulnerability affecting Gladinet CentreStack and Triofox file sharing products that allows local attackers to access system files
- **Impact**: Unauthorized access to sensitive system files without requiring authentication credentials
- **Status**: Currently being actively exploited in the wild with no patch available
- **CVE ID**: CVE-2025-11371

### GoAnywhere Managed File Transfer Critical Flaw
- **Description**: A critical security vulnerability in Fortra's GoAnywhere Managed File Transfer solution
- **Impact**: Active exploitation allowing unauthorized access to managed file transfer systems
- **Status**: Under active exploitation with detailed timeline of attack progression revealed by vendor
- **CVE ID**: CVE-2025-10035

### SonicWall SSL VPN Mass Compromise
- **Description**: Widespread authentication bypass affecting SonicWall SSL VPN devices
- **Impact**: Threat actors gaining authenticated access to multiple customer environments through compromised VPN infrastructure
- **Status**: Active compromise affecting over 100 accounts across multiple organizations

### Microsoft Edge Internet Explorer Mode Abuse
- **Description**: Legacy Internet Explorer compatibility feature being weaponized as a backdoor mechanism
- **Impact**: Persistent backdoor access through browser compatibility features
- **Status**: Microsoft has implemented security improvements after receiving credible threat reports in August 2025

### RondoDox Botnet Multi-Vendor Exploitation
- **Description**: Malware campaign exploiting vulnerabilities across diverse vendor ecosystems using a shotgun approach
- **Impact**: Mass compromise of edge devices and network infrastructure across multiple vendor platforms
- **Status**: Actively targeting over 50 vulnerabilities across 30+ vendors simultaneously

## Affected Systems and Products

- **Gladinet CentreStack and Triofox**: File sharing and collaboration platforms vulnerable to authentication bypass
- **SonicWall SSL VPN Devices**: Network security appliances experiencing widespread authentication compromise
- **GoAnywhere Managed File Transfer**: Secure file transfer solutions under active exploitation
- **Microsoft Edge Browser**: IE Mode feature being abused for persistent access
- **Consumer Edge Devices**: IoT and network infrastructure targeted by RondoDox botnet campaigns
- **Oracle E-Business Suite**: Enterprise software with newly disclosed unauthorized access vulnerability

## Attack Vectors and Techniques

- **Authentication Bypass**: Direct system file access without credential validation in Gladinet products
- **VPN Infrastructure Compromise**: Mass authentication into SonicWall VPN environments for lateral movement
- **Browser Feature Abuse**: Leveraging legacy compatibility modes as persistent backdoor mechanisms
- **Multi-Vendor Exploitation**: Automated exploitation frameworks targeting diverse vulnerability landscapes
- **Digital Forensics Tool Weaponization**: Abuse of Velociraptor DFIR tool by Storm-2603 for ransomware operations
- **GitHub Infrastructure Abuse**: Astaroth banking trojan using GitHub repositories for command and control resilience

## Threat Actor Activities

- **Storm-2603 (CL-CRI-1040)**: Chinese threat group weaponizing legitimate DFIR tools like Velociraptor in ransomware attacks, specifically targeting LockBit operations
- **Storm-2657**: "Payroll Pirates" campaign hijacking HR SaaS accounts to redirect employee salary payments to attacker-controlled accounts
- **RondoDox Operators**: Conducting mass exploitation campaigns against edge devices using automated vulnerability exploitation across multiple vendor ecosystems
- **Astaroth Banking Trojan Operators**: Maintaining operational resilience through GitHub abuse for command and control infrastructure after takedowns
- **GXC Team Cybercrime Syndicate**: Brazilian-led operation dismantled by Spanish authorities, with leader "GoogleXcoder" arrested
- **Unknown Threat Actors**: Actively exploiting Gladinet zero-day and conducting widespread SonicWall VPN compromises