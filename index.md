# Exploitation Report

Critical vulnerability exploitation activity is currently focused on several high-impact zero-day vulnerabilities and supply chain attacks. A Check Point VPN zero-day vulnerability is being actively exploited by the Qilin ransomware gang to bypass authentication in IKEv1 deployments, while a critical Linux kernel flaw enabling local root access has public exploits available. Additionally, the Gogs Git service patched a critical zero-day that allowed remote code execution, and the Everest Forms Pro WordPress plugin is under active exploitation for complete site takeover. Supply chain attacks continue with the Shai-Hulud campaign compromising PyPI packages and a sophisticated botnet exploiting DD-WRT router vulnerabilities.

## Active Exploitation Details

### Check Point VPN Zero-Day Vulnerability
- **Description**: Critical vulnerability affecting Remote Access VPN and Mobile Access deployments configured with deprecated IKEv1 key exchange protocol that allows authentication bypass
- **Impact**: Attackers can bypass password authentication and gain unauthorized access to VPN networks
- **Status**: Under active exploitation since early May 2026, patches have been released by Check Point

### Linux Kernel Use-After-Free Vulnerability
- **Description**: One-character flaw in the Linux kernel that creates a use-after-free condition
- **Impact**: Unprivileged local users can escalate privileges to root and break out of containers
- **Status**: Detailed working exploits have been published publicly
- **CVE ID**: CVE-202[truncated in source]

### Gogs Zero-Day Remote Code Execution
- **Description**: Critical security flaw in the Gogs Git service that enables remote code execution
- **Impact**: Attackers can compromise Internet-facing instances and access any repositories, including private ones
- **Status**: Zero-day has been patched, but was previously under exploitation

### Everest Forms Pro WordPress Vulnerability
- **Description**: Critical vulnerability in the Everest Forms Pro plugin for WordPress
- **Impact**: Complete takeover of WordPress websites
- **Status**: Currently under active exploitation
- **CVE ID**: CVE-2026-3300

### UniFi OS Vulnerability Chain
- **Description**: Three chained vulnerabilities in Ubiquiti UniFi OS server
- **Impact**: Remote code execution with root privileges without authentication
- **Status**: All three vulnerabilities have been fixed but can be chained together

## Affected Systems and Products

- **Check Point Remote Access VPN**: IKEv1-configured deployments vulnerable to authentication bypass
- **Check Point Mobile Access**: IKEv1-configured systems affected by zero-day exploitation
- **Linux Kernel**: All systems running vulnerable kernel versions susceptible to local privilege escalation
- **Gogs Git Service**: Internet-facing instances vulnerable to remote code execution
- **WordPress Sites**: Sites using Everest Forms Pro plugin at risk of complete compromise
- **Ubiquiti UniFi OS**: Servers vulnerable to authentication bypass and remote code execution
- **DD-WRT Routers**: Firmware vulnerable to C0XMO botnet exploitation
- **PyPI Packages**: 19 science-focused packages compromised in Shai-Hulud supply chain attack
- **Meta AI Support System**: Used to compromise over 20,000 Instagram accounts

## Attack Vectors and Techniques

- **VPN Authentication Bypass**: Exploitation of IKEv1 protocol weaknesses to bypass password requirements
- **Container Escape**: Local privilege escalation from unprivileged user to root with container breakout capabilities
- **Supply Chain Poisoning**: Trojanizing legitimate PyPI packages to steal developer credentials and secrets
- **Social Engineering**: Vishing attacks combined with physical office intrusions for data theft
- **Phishing Campaigns**: NSO Group spear-phishing attempts targeting WhatsApp users
- **Botnet Propagation**: Router firmware exploitation with capability to eliminate competing malware
- **WordPress Plugin Exploitation**: Direct website takeover through vulnerable form processing plugins

## Threat Actor Activities

- **Qilin Ransomware Gang**: Actively exploiting Check Point VPN zero-day vulnerability for network access and ransomware deployment
- **Silent Ransom Group (UNC3753)**: Targeting U.S. law firms and professional services with vishing, IT impersonation, and physical intrusions for data theft and extortion
- **NSO Group**: Conducting spear-phishing campaigns against WhatsApp users despite legal restrictions
- **VerdantBamboo (China-nexus)**: Deploying BSD variants of BRICKSTORM backdoor and other malware on Linux appliances
- **Shai-Hulud Campaign Operators**: Compromising Python package repositories to steal developer credentials in ongoing supply chain attacks
- **C0XMO Botnet Operators**: Exploiting DD-WRT router vulnerabilities and actively removing competing malware from infected systems