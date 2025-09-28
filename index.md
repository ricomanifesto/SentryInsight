# Exploitation Report

Critical zero-day vulnerabilities are being actively exploited across multiple platforms, with the most severe being a maximum severity flaw in Fortra's GoAnywhere MFT (CVE-2025-10035) that allows remote command injection without authentication. Cisco firewalls are under widespread attack through multiple zero-day vulnerabilities, with threat actors deploying sophisticated malware including RayInitiator and LINE VIPER. Chinese APT groups are conducting extensive campaigns targeting Asian telecommunications infrastructure and edge devices, while multiple malware families including XCSSET, PlugX, and Oyster are being distributed through various attack vectors. Supply chain attacks have impacted major manufacturers, with ransomware groups successfully compromising supplier networks and stealing sensitive employee data.

## Active Exploitation Details

### GoAnywhere MFT Remote Code Execution
- **Description**: Maximum severity vulnerability in Fortra's GoAnywhere Managed File Transfer software allowing attackers to inject commands remotely without authentication
- **Impact**: Complete system compromise, unauthorized access to file transfer systems, potential data exfiltration
- **Status**: Actively exploited as zero-day for approximately one week before public disclosure, patches available
- **CVE ID**: CVE-2025-10035

### Cisco ASA/FTD Zero-Day Vulnerabilities
- **Description**: Multiple security flaws impacting the VPN web server of Cisco Secure Firewall ASA and FTD software, exploited by nation-state actors
- **Impact**: Deployment of RayInitiator and LINE VIPER malware, network device compromise, persistent backdoor access
- **Status**: Actively exploited zero-days, CISA Emergency Mitigation Directive issued, patches available

### XCSSET macOS Malware
- **Description**: Updated variant of Apple macOS malware targeting Xcode developers with enhanced browser targeting capabilities
- **Impact**: Browser manipulation, cryptocurrency wallet hijacking through clipper functionality, persistent system access
- **Status**: Limited active attacks detected, enhanced variant with new persistence mechanisms

### Salesforce ForcedLeak AI Vulnerability
- **Description**: Critical flaw in Salesforce Agentforce platform allowing indirect prompt injection attacks against AI agents
- **Impact**: Exposure of sensitive CRM data, unauthorized data exfiltration through AI agent manipulation
- **Status**: Patched after disclosure, proof-of-concept demonstrations conducted

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: Managed file transfer software vulnerable to remote command injection
- **Cisco ASA/FTD Firewalls**: Secure Firewall devices with VPN web server vulnerabilities
- **Apple macOS**: Systems running Xcode development environment targeted by XCSSET
- **Salesforce Agentforce**: AI agent platform vulnerable to prompt injection attacks
- **Microsoft Teams**: Legitimate software impersonated in malvertising campaigns
- **Network Edge Devices**: Appliances targeted by Brickstorm backdoor deployments
- **npm Packages**: Malicious packages mimicking legitimate Postmark MCP library

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Nation-state actors exploiting unpatched vulnerabilities in network infrastructure
- **Malvertising Campaigns**: SEO poisoning and search advertisements promoting fake software installers
- **Supply Chain Attacks**: Ransomware groups targeting third-party suppliers to access primary victims
- **Phishing Campaigns**: Ukrainian government impersonation to distribute CountLoader and stealer malware
- **Package Repository Poisoning**: Malicious npm packages designed to steal email communications
- **Code-Signing Certificate Abuse**: Iranian threat actors using legitimate SSL.com certificates to sign malware
- **ClickFix-Style Attacks**: Social engineering techniques to trick users into executing malicious code
- **Browser Extension Sideloading**: Malicious extensions installed outside official browser stores

## Threat Actor Activities

- **COLDRIVER (Russian APT)**: Conducting ClickFix-style attacks deploying BO Team and Bearlyfy malware families
- **UNC5221 (Chinese APT)**: Compromising edge devices with Brickstorm backdoors, targeting network appliances without EDR capabilities
- **China-Linked Groups**: Targeting Asian telecommunications and ASEAN networks with PlugX and Bookworm malware variants
- **Charming Kitten/Subtle Snail (Iranian)**: Using legitimate code-signing certificates from SSL.com to deploy signed malware
- **Vane Viper**: Operating global malware and ad fraud network generating over 1 trillion DNS queries
- **Scattered Spider**: Responsible for $107 million loss at UK Co-operative Group through cyberattack
- **Dutch Teenagers**: Arrested for attempting to spy on Europol using hacking devices for Russian intelligence