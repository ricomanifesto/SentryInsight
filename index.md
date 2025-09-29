# Exploitation Report

Multiple critical zero-day vulnerabilities are currently being exploited in active campaigns targeting enterprise infrastructure, with particularly severe attacks on Cisco network devices and Fortra's GoAnywhere MFT platform. The most significant threats include maximum severity vulnerabilities in widely deployed systems, with CVE-2025-10035 representing an unauthenticated remote command injection flaw that has achieved widespread exploitation. Nation-state actors, including Chinese APT groups and Iranian state-sponsored attackers, are leveraging these vulnerabilities alongside sophisticated malware campaigns to compromise telecommunications infrastructure, government networks, and enterprise systems globally.

## Active Exploitation Details

### GoAnywhere MFT Command Injection Vulnerability
- **Description**: Maximum severity vulnerability allowing remote command injection without authentication in Fortra's GoAnywhere Managed File Transfer software
- **Impact**: Attackers can execute arbitrary commands on affected systems with full system privileges
- **Status**: Actively exploited as zero-day approximately one week before public disclosure, patches available
- **CVE ID**: CVE-2025-10035

### Cisco ASA Firewall Zero-Day Vulnerabilities
- **Description**: Multiple security flaws impacting the VPN web server component of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software
- **Impact**: Nation-state actors deploying RayInitiator and LINE VIPER malware through compromised firewall devices
- **Status**: Actively exploited zero-days with CISA Emergency Mitigation Directive issued, patches available

### SonicWall SSL VPN Authentication Bypass
- **Description**: Vulnerability allowing Akira ransomware operators to bypass multi-factor authentication on SonicWall VPN devices
- **Impact**: Successful login to MFA-protected accounts, leading to network compromise and ransomware deployment
- **Status**: Ongoing active exploitation by Akira ransomware group

### Salesforce Agentforce AI Prompt Injection
- **Description**: Critical flaw dubbed "ForcedLeak" affecting Salesforce Agentforce AI agent platform through indirect prompt injection
- **Impact**: Attackers can force AI agents to leak sensitive CRM data and customer information
- **Status**: Recently patched by Salesforce after researcher disclosure

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: All versions prior to latest security update, affecting managed file transfer operations
- **Cisco ASA/FTD Firewalls**: Millions of deployed devices running vulnerable VPN web server components
- **SonicWall SSL VPN**: Devices with MFA-enabled accounts targeted by ransomware operators
- **Salesforce Agentforce**: AI agent platform vulnerable to prompt injection attacks
- **Network Edge Devices**: Various appliances targeted by Chinese APT groups for backdoor deployment
- **macOS Systems**: Firefox browsers targeted by updated XCSSET malware variants

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Nation-state actors leveraging undisclosed vulnerabilities in network infrastructure
- **MFA Bypass**: Advanced techniques to circumvent multi-factor authentication on VPN systems
- **Malvertising Campaigns**: SEO poisoning and search engine advertisements distributing fake Microsoft Teams installers
- **Supply Chain Attacks**: Targeting third-party suppliers to compromise major manufacturers like Volvo
- **Phishing Operations**: Ukrainian government impersonation campaigns delivering CountLoader and PureRAT malware
- **DNS Infrastructure Abuse**: Vane Viper generating over 1 trillion DNS queries for malware distribution and ad fraud
- **Code Signing Certificate Abuse**: Iranian state hackers using legitimate SSL.com certificates to sign malware

## Threat Actor Activities

- **Chinese APT Groups**: UNC5221 deploying "Brickstorm" backdoors on network edge devices, PlugX and Bookworm malware targeting Asian telecommunications and ASEAN networks
- **Akira Ransomware**: Sophisticated attacks on MFA-protected SonicWall VPN infrastructure with evolving bypass techniques
- **Iranian State Actors**: Charming Kitten APT offshoot "Subtle Snail" using legitimate code-signing certificates for malware distribution
- **COLDRIVER (Russian APT)**: Fresh ClickFix-style campaigns deploying "BO Team" and "Bearlyfy" lightweight malware families
- **Vane Viper**: Massive DNS-based infrastructure supporting global malware distribution and ad fraud operations
- **Dutch Teenage Hackers**: Russian-sponsored espionage attempts targeting Europol using specialized hacking devices