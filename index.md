# Exploitation Report

The current threat landscape shows significant active exploitation across multiple critical vulnerabilities, with several zero-day attacks targeting enterprise infrastructure and consumer software. The most concerning activities include a Chrome zero-day marking the fifth such vulnerability exploited this year, a critical Check Point VPN flaw linked to Qilin ransomware operations, and a BerriAI LiteLLM vulnerability enabling unauthenticated remote code execution that has been added to CISA's Known Exploited Vulnerabilities catalog. Additional zero-day exploits have been identified in Gogs git service and various Android platforms, while sophisticated threat actors are employing novel attack vectors including supply chain poisoning of PyPI packages and advanced social engineering campaigns.

## Active Exploitation Details

### Chrome Zero-Day Vulnerability
- **Description**: Fifth Chrome zero-day vulnerability exploited in attacks this year, requiring emergency security updates from Google
- **Impact**: Enables attackers to compromise user systems through web browser exploitation
- **Status**: Patched with emergency Chrome updates, actively exploited in the wild

### BerriAI LiteLLM Authentication Bypass
- **Description**: High-severity vulnerability in BerriAI LiteLLM that chains to enable unauthenticated remote code execution
- **Impact**: Allows attackers to execute arbitrary code without authentication
- **Status**: Added to CISA KEV catalog due to evidence of active exploitation
- **CVE ID**: CVE-2026-42271

### Check Point VPN Zero-Day
- **Description**: Critical vulnerability affecting Remote Access VPN and Mobile Access deployments configured with deprecated IKEv1 key exchange protocol
- **Impact**: Enables password bypass and unauthorized VPN access
- **Status**: Actively exploited since early May, now patched

### Gogs Git Service Zero-Day
- **Description**: Critical security flaw in Gogs git service allowing compromise of Internet-facing instances
- **Impact**: Provides attackers access to any repositories including private ones, enables remote code execution
- **Status**: Recently patched after active exploitation

### Linux Kernel Use-After-Free Vulnerability
- **Description**: One-character flaw in Linux kernel that enables local privilege escalation
- **Impact**: Allows unprivileged local users to escalate to root and break out of containers
- **Status**: Working exploits now publicly available
- **CVE ID**: CVE-202[truncated in source]

## Affected Systems and Products

- **Google Chrome**: All versions prior to latest emergency update
- **BerriAI LiteLLM**: Unspecified versions vulnerable to authentication bypass
- **Check Point Remote Access VPN**: Deployments using IKEv1 protocol configuration
- **Check Point Mobile Access**: IKEv1 configured systems
- **Gogs Git Service**: Internet-facing instances running vulnerable versions
- **Linux Kernel**: Systems running affected kernel versions
- **Android Devices**: Multiple variants affected by NFCShare malware and zero-day exploits
- **Ubiquiti UniFi OS**: Server deployments vulnerable to chained exploitation
- **DD-WRT Router Firmware**: Devices targeted by C0XMO botnet
- **PyPI Packages**: 19 science-focused packages compromised in Shai-Hulud attack, 37 additional packages in Hades campaign

## Attack Vectors and Techniques

- **Zero-Day Web Browser Exploitation**: Targeting Chrome users through malicious web content
- **VPN Protocol Exploitation**: Bypassing authentication in IKEv1 configurations
- **Supply Chain Poisoning**: Trojanizing legitimate PyPI packages with malware
- **Social Engineering**: Vishing campaigns and fake IT support calls targeting law firms
- **Physical Intrusion**: In-person office access combined with digital attacks
- **Malware Distribution**: Fake banking app updates hosted on GitHub repositories
- **Container Escape**: Kernel exploitation enabling escape from containerized environments
- **Botnet Propagation**: Router firmware exploitation for botnet expansion
- **Spear-Phishing**: NSO Group campaigns targeting WhatsApp users
- **AI-Powered Support System Abuse**: Exploiting Meta's AI support for Instagram account takeover

## Threat Actor Activities

- **Qilin Ransomware Gang**: Actively exploiting Check Point VPN zero-day vulnerabilities for initial access
- **NSO Group**: Conducting spear-phishing campaigns against WhatsApp users despite legal restrictions
- **Silent Ransom Group/UNC3753**: Targeting U.S. law firms and professional services with vishing, IT impersonation, and physical intrusion tactics
- **VerdantBamboo (China-nexus)**: Deploying BSD variant of BRICKSTORM backdoor on Linux appliances along with PLENET and AGENTPSD malware
- **Shai-Hulud/Hades Campaign Operators**: Compromising Python package repositories to distribute malware targeting developers
- **NFCShare Malware Distributors**: Using fake banking app updates on GitHub to spread Android malware
- **C0XMO Botnet Operators**: Exploiting DD-WRT router vulnerabilities while eliminating competing malware
- **Instagram Account Hijackers**: Abusing Meta AI support systems to compromise over 20,000 accounts