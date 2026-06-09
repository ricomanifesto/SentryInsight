# Exploitation Report

A significant wave of zero-day vulnerabilities and active exploitation campaigns has emerged across multiple critical systems and platforms. Check Point VPN systems are under active attack through a critical zero-day vulnerability affecting IKEv1 configurations, with the Qilin ransomware group confirmed as one of the threat actors. Linux kernel systems face immediate risk from CVE-2026-0985, a one-character flaw enabling local privilege escalation with public exploits now available. The Gogs Git service has been compromised through a critical zero-day allowing remote code execution, while WordPress sites are being actively exploited through CVE-2026-3300 in the Everest Forms Pro plugin. Supply chain attacks continue to escalate with the Shai-Hulud campaign compromising 19 PyPI packages and Meta's AI support system being exploited to hijack over 20,000 Instagram accounts.

## Active Exploitation Details

### Check Point VPN Zero-Day
- **Description**: Critical vulnerability affecting Remote Access VPN and Mobile Access deployments configured with deprecated IKEv1 key exchange protocol
- **Impact**: Attackers can bypass password authentication and gain unauthorized VPN access
- **Status**: Under active exploitation since early May 2025; patches available

### Linux Kernel Use-After-Free Vulnerability
- **Description**: A single character flaw in the Linux kernel creating a use-after-free condition
- **Impact**: Unprivileged local users can escalate to root privileges and break out of containers
- **Status**: Public exploits available; actively exploited
- **CVE ID**: CVE-2026-0985

### Gogs Git Service Zero-Day
- **Description**: Critical security flaw in Gogs Git service allowing remote code execution
- **Impact**: Attackers can compromise Internet-facing instances and access any repositories including private ones
- **Status**: Zero-day vulnerability recently patched after active exploitation

### Everest Forms Pro WordPress Plugin Vulnerability
- **Description**: Critical vulnerability in the Everest Forms Pro WordPress plugin
- **Impact**: Complete takeover of WordPress websites
- **Status**: Under active exploitation
- **CVE ID**: CVE-2026-3300

### Meta AI Support System Exploitation
- **Description**: Attackers exploited Meta's AI-powered support system to reset passwords
- **Impact**: 20,225 Instagram accounts hijacked through automated password resets
- **Status**: Incident contained; accounts affected

## Affected Systems and Products

- **Check Point Remote Access VPN**: Systems configured with IKEv1 key exchange protocol
- **Linux Kernel**: Multiple distributions affected by use-after-free vulnerability
- **Gogs Git Service**: Internet-facing instances vulnerable to remote code execution
- **WordPress Sites**: Sites using Everest Forms Pro plugin vulnerable to complete takeover
- **Instagram Accounts**: Over 20,000 accounts compromised through AI support system exploitation
- **PyPI Packages**: 19 science-focused packages compromised in supply chain attack
- **DD-WRT Routers**: Firmware vulnerable to C0XMO botnet exploitation
- **UniFi OS Servers**: Ubiquiti systems vulnerable to root access through vulnerability chaining

## Attack Vectors and Techniques

- **VPN Authentication Bypass**: Exploitation of IKEv1 protocol weaknesses to bypass password requirements
- **Local Privilege Escalation**: Use-after-free exploitation in Linux kernel for root access
- **Remote Code Execution**: Direct exploitation of Gogs service vulnerabilities
- **AI System Manipulation**: Abuse of automated support systems for credential theft
- **Supply Chain Poisoning**: Trojanizing legitimate software packages with malicious code
- **Social Engineering**: Vishing attacks combined with physical intrusions
- **Phishing Campaigns**: NSO Group spear-phishing through WhatsApp
- **Botnet Propagation**: Router firmware exploitation for botnet expansion

## Threat Actor Activities

- **Qilin Ransomware Group**: Actively exploiting Check Point VPN zero-day for initial access
- **Silent Ransom Group (UNC3753)**: Targeting US law firms through vishing, IT impersonation, and physical intrusions
- **NSO Group**: Conducting spear-phishing campaigns through WhatsApp despite legal restrictions
- **VerdantBamboo (China-nexus)**: Deploying BSD variants of BRICKSTORM backdoor on Linux appliances
- **C0XMO Botnet Operators**: Spreading malware through DD-WRT router vulnerabilities while eliminating competing malware
- **Shai-Hulud Campaign Actors**: Compromising PyPI packages to steal developer secrets through supply chain attacks