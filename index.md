# Exploitation Report

Critical zero-day vulnerabilities are actively being exploited across multiple major platforms, with particularly severe activity targeting Cisco network infrastructure and managed file transfer systems. The most concerning developments include maximum severity exploits against Fortra's GoAnywhere MFT platform (CVE-2025-10035) and a coordinated campaign exploiting Cisco ASA firewall vulnerabilities that prompted an emergency CISA directive. Nation-state actors, particularly China-linked groups, are leveraging these vulnerabilities alongside sophisticated malware campaigns to compromise telecommunications networks, edge devices, and enterprise infrastructure.

## Active Exploitation Details

### GoAnywhere MFT Remote Code Injection Vulnerability
- **Description**: A maximum severity vulnerability in Fortra's GoAnywhere Managed File Transfer software that allows remote command injection without authentication
- **Impact**: Attackers can execute arbitrary commands remotely without any authentication, leading to complete system compromise
- **Status**: Zero-day exploitation detected approximately one week before public disclosure; patches now available
- **CVE ID**: CVE-2025-10035

### Cisco ASA Firewall Zero-Day Vulnerabilities
- **Description**: Two critical security flaws affecting the VPN web server of Cisco Secure Firewall ASA Software and Cisco Secure Firewall Threat Defense Software
- **Impact**: Threat actors deploy RayInitiator and LINE VIPER malware on compromised systems, enabling persistent access and data exfiltration
- **Status**: Actively exploited in zero-day attacks; CISA issued Emergency Mitigation Directive

### XCSSET macOS Malware Evolution
- **Description**: Updated variant of known macOS malware targeting Xcode developers with enhanced browser targeting capabilities
- **Impact**: Cryptocurrency wallet address manipulation through clipper functionality and enhanced persistence mechanisms
- **Status**: Active in limited attacks with new features targeting Firefox browsers

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: All versions prior to latest security update vulnerable to remote code injection
- **Cisco ASA Firewalls**: Secure Firewall ASA Software and Threat Defense Software VPN web servers
- **Cisco IOS Devices**: Multiple network devices affected by nation-state targeting campaign
- **macOS Systems**: Xcode development environments targeted by XCSSET malware
- **Microsoft Teams**: Fake installers distributing Oyster backdoor malware
- **Network Edge Devices**: Appliances targeted by Chinese APT group UNC5221 with Brickstorm backdoors
- **Salesforce Agentforce**: AI agent platform vulnerable to prompt injection attacks

## Attack Vectors and Techniques

- **SEO Poisoning and Malvertising**: Fake Microsoft Teams installers promoted through search engine manipulation and malicious advertisements
- **ClickFix-Style Attacks**: COLDRIVER APT group utilizing deceptive user interaction techniques to deliver lightweight malware families
- **Supply Chain Compromise**: Ransomware attacks targeting automotive suppliers affecting major manufacturers like Volvo
- **Phishing Campaigns**: Ukrainian government impersonation to deliver CountLoader, Amatera Stealer, and PureMiner malware
- **Code-Signing Certificate Abuse**: Iranian threat groups using legitimate SSL.com certificates to sign and distribute malware
- **DNS Infrastructure Manipulation**: Vane Viper generating over 1 trillion DNS queries to support global malware and ad fraud networks
- **Prompt Injection Attacks**: ForcedLeak technique targeting Salesforce AI agents to exfiltrate sensitive CRM data

## Threat Actor Activities

- **China-linked APT Groups**: Deploying PlugX and Bookworm malware variants targeting Asian telecommunications and ASEAN networks
- **UNC5221 (Chinese APT)**: Compromising network edge devices with Brickstorm backdoor variants that evade traditional EDR detection
- **COLDRIVER (Russian APT)**: Conducting ClickFix campaigns delivering BO Team and Bearlyfy malware families
- **Charming Kitten/Subtle Snail (Iranian)**: Utilizing legitimate code-signing certificates from SSL.com to distribute malware
- **Scattered Spider**: Responsible for Co-operative Group attack resulting in £80 million ($107 million) operational losses
- **Vane Viper**: Operating extensive malware and ad fraud network leveraging shell companies and complex ownership structures
- **Nation-state Actor**: Previously associated with ArcaneDoor campaign, now actively exploiting Cisco zero-day vulnerabilities