# Exploitation Report

Multiple zero-day vulnerabilities are currently under active exploitation, with the most critical activity targeting enterprise infrastructure. Cisco firewalls are experiencing widespread zero-day exploitation by nation-state actors deploying custom malware including RayInitiator and LINE VIPER backdoors. Fortra's GoAnywhere MFT platform is being actively exploited through CVE-2025-10035, a maximum severity vulnerability allowing remote command injection without authentication. Chinese APT groups are conducting sophisticated campaigns targeting telecommunications and ASEAN networks using PlugX and Bookworm malware, while also deploying Brickstorm backdoors on edge devices. Additional threats include malvertising campaigns distributing Oyster backdoor malware through fake Microsoft Teams installers, and the emergence of new XCSSET macOS malware variants targeting Firefox browsers.

## Active Exploitation Details

### Cisco ASA Firewall Zero-Day Vulnerabilities
- **Description**: Two critical zero-day vulnerabilities affecting Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software VPN web servers
- **Impact**: Nation-state actors are exploiting these flaws to deploy RayInitiator and LINE VIPER malware for persistent access and data exfiltration
- **Status**: Actively exploited by threat actors; patches available from Cisco; CISA issued Emergency Mitigation Directive

### GoAnywhere MFT Critical Vulnerability
- **Description**: Maximum severity vulnerability in Fortra's GoAnywhere Managed File Transfer software allowing remote command injection
- **Impact**: Attackers can execute arbitrary commands remotely without authentication
- **Status**: Zero-day exploitation detected approximately one week before public disclosure; patches now available
- **CVE ID**: CVE-2025-10035

### XCSSET macOS Malware
- **Description**: Updated variant of known Apple macOS malware with enhanced capabilities targeting Firefox browsers
- **Impact**: Cryptocurrency clipping attacks, enhanced persistence mechanisms, and browser data theft
- **Status**: Limited active attacks observed against macOS users and Xcode developers

### PlugX and Bookworm Malware Campaign
- **Description**: China-linked campaign distributing new variants of PlugX malware targeting telecommunications and manufacturing sectors
- **Impact**: Network infiltration, data exfiltration, and persistent access to critical infrastructure
- **Status**: Ongoing campaign targeting Central and South Asian countries

## Affected Systems and Products

- **Cisco Secure Firewall ASA Software**: VPN web server components vulnerable to zero-day exploitation
- **Cisco Secure Firewall Threat Defense (FTD) Software**: VPN web server functionality affected
- **Fortra GoAnywhere MFT**: All versions prior to patched release vulnerable to remote command injection
- **Apple macOS Systems**: Firefox browsers and Xcode development environments targeted by XCSSET
- **Telecommunications Infrastructure**: Central and South Asian telecom providers targeted by PlugX campaigns
- **Manufacturing Systems**: Industrial control systems and manufacturing networks in Asian markets
- **Windows Systems**: Microsoft Teams users targeted through malvertising campaigns
- **Network Edge Devices**: Appliances that cannot run traditional EDR agents targeted for Brickstorm backdoor deployment

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Nation-state actors exploiting unpatched Cisco firewall vulnerabilities for initial access
- **Malvertising Campaigns**: SEO poisoning and search engine advertisements promoting fake Microsoft Teams installers
- **Supply Chain Attacks**: Targeting third-party suppliers to gain access to major organizations like Volvo
- **Phishing Operations**: Ukrainian government impersonation campaigns delivering CountLoader and PureRAT malware
- **Code-Signing Certificate Abuse**: Iranian threat actors using legitimate SSL.com certificates to sign malicious software
- **DNS Infrastructure Manipulation**: Vane Viper generating over 1 trillion DNS queries to support malware and ad fraud networks
- **ClickFix-Style Attacks**: COLDRIVER APT group using deceptive user interface elements to deliver lightweight malware families
- **Prompt Injection**: ForcedLeak attacks against Salesforce AI agents to exfiltrate sensitive CRM data

## Threat Actor Activities

- **Chinese APT Groups**: Conducting sophisticated campaigns against ASEAN networks and telecommunications infrastructure using PlugX and Bookworm malware
- **UNC5221**: China-linked cyber-espionage group deploying Brickstorm backdoors on network edge devices that cannot run traditional security agents
- **Nation-State Actors**: Exploiting Cisco zero-day vulnerabilities identified as part of the "ArcaneDoor" campaign to deploy custom malware
- **COLDRIVER APT**: Russian advanced persistent threat group conducting ClickFix-style attacks with new lightweight malware families
- **Charming Kitten/Subtle Snail**: Iranian state-sponsored groups using legitimate code-signing certificates to deploy signed malware
- **Scattered Spider**: Conducted cyberattack against Co-operative Group resulting in $107 million in losses
- **Vane Viper**: Operating global malware and ad fraud network through complex shell company structures and DNS manipulation
- **Dutch Teenagers**: Two 17-year-old suspects arrested for attempting to spy on Europol for Russian intelligence services