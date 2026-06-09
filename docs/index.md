# Exploitation Report

Critical zero-day vulnerabilities are under active exploitation across multiple platforms, with attackers targeting enterprise infrastructure, supply chain components, and consumer applications. The most severe incidents involve a Check Point VPN zero-day being exploited by the Qilin ransomware group, a one-character Linux kernel flaw enabling local root access with public exploits available, and a critical Gogs zero-day allowing remote code execution. Additionally, widespread supply chain attacks are targeting Python package repositories, while sophisticated social engineering campaigns are compromising thousands of Instagram accounts and targeting law firms with multi-vector attacks.

## Active Exploitation Details

### Check Point VPN Zero-Day
- **Description**: Critical vulnerability in Remote Access VPN and Mobile Access deployments configured with deprecated IKEv1 key exchange protocol that allows authentication bypass
- **Impact**: Attackers can bypass password authentication and gain unauthorized access to VPN infrastructure
- **Status**: Under active exploitation since early May 2026, patches have been released
- **CVE ID**: CVE information not provided in source articles

### Linux Kernel Use-After-Free Vulnerability
- **Description**: One-character flaw in the Linux kernel that creates a use-after-free condition
- **Impact**: Unprivileged local users can escalate to root privileges and break out of containers
- **Status**: Working exploits have been published publicly, making this vulnerability extremely dangerous
- **CVE ID**: CVE-202 (article appears truncated)

### Gogs Remote Code Execution Zero-Day
- **Description**: Critical security flaw in Gogs Git service that enables remote code execution
- **Impact**: Attackers can compromise Internet-facing instances and access any repositories including private ones
- **Status**: Zero-day that has been patched, but exploitation status unclear

### Everest Forms Pro WordPress Vulnerability
- **Description**: Critical flaw in Everest Forms Pro WordPress plugin
- **Impact**: Complete takeover of WordPress websites
- **Status**: Actively being exploited in the wild
- **CVE ID**: CVE-2026-3300

### UniFi OS Authentication Bypass Chain
- **Description**: Chain of three previously fixed vulnerabilities in Ubiquiti UniFi OS server
- **Impact**: Remote code execution with root privileges without authentication
- **Status**: Vulnerabilities are already fixed but can be chained for exploitation

## Affected Systems and Products

- **Check Point VPN**: Remote Access VPN and Mobile Access deployments using IKEv1 protocol
- **Linux Kernel**: Systems running affected kernel versions with local user access
- **Gogs**: Internet-facing Git service instances
- **WordPress Sites**: Sites using Everest Forms Pro plugin
- **Ubiquiti UniFi OS**: UniFi OS server installations
- **PyPI Packages**: 19 science-focused packages and 37 additional wheels compromised
- **Instagram**: Over 20,000 user accounts compromised through Meta AI support system
- **Android Devices**: Targeted by NFCShare malware via fake banking app updates
- **DD-WRT Routers**: Targeted by C0XMO botnet variant

## Attack Vectors and Techniques

- **VPN Authentication Bypass**: Exploitation of IKEv1 protocol weaknesses to bypass authentication
- **Container Escape**: Local privilege escalation combined with container breakout techniques
- **Supply Chain Poisoning**: Compromising legitimate Python packages to deliver malware
- **Social Engineering**: Multi-vector attacks combining vishing, IT impersonation, and physical intrusions
- **Malicious Package Distribution**: Using GitHub to host fake banking app updates containing malware
- **AI-Assisted Phishing**: Leveraging AI systems to conduct spear-phishing attacks
- **Botnet Propagation**: Exploiting router firmware flaws to spread malware and eliminate competing infections

## Threat Actor Activities

- **Qilin Ransomware Group**: Exploiting Check Point VPN zero-day for initial access to corporate networks
- **NSO Group**: Conducting sophisticated spear-phishing campaigns targeting WhatsApp users despite legal restrictions
- **Silent Ransom Group (UNC3753)**: Targeting US law firms and professional services with vishing attacks, IT impersonation, and physical office intrusions for data theft and extortion
- **VerdantBamboo**: China-nexus group deploying BSD variants of BRICKSTORM backdoor along with PLENET and AGENTPSD malware on Linux appliances
- **Shai-Hulud Operators**: Conducting "Hades" campaign against PyPI, compromising multiple Python packages to steal developer secrets
- **C0XMO Botnet**: Targeting DD-WRT routers and expanding to multiple CPU architectures while eliminating rival malware