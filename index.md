# Exploitation Report

Multiple critical zero-day vulnerabilities are currently under active exploitation across enterprise infrastructure, with attackers targeting Cisco firewall systems, Fortra's GoAnywhere MFT platform, and various other critical systems. The most severe activity involves CVE-2025-10035, a maximum severity flaw in GoAnywhere MFT that allows remote command injection without authentication. Cisco has disclosed four actively exploited zero-day vulnerabilities affecting millions of firewall devices, with nation-state actors deploying sophisticated backdoors including RayInitiator and LINE VIPER malware. Supply chain attacks continue to plague organizations, while threat actors are increasingly leveraging AI systems and code-signing certificates to enhance their operations.

## Active Exploitation Details

### Fortra GoAnywhere MFT Zero-Day
- **Description**: Maximum severity vulnerability allowing remote command injection without authentication in Fortra's GoAnywhere Managed File Transfer software
- **Impact**: Attackers can execute arbitrary commands remotely without any authentication, leading to complete system compromise
- **Status**: Actively exploited as zero-day with credible evidence of exploitation occurring approximately one week before public disclosure
- **CVE ID**: CVE-2025-10035

### Cisco ASA Firewall Zero-Days
- **Description**: Multiple zero-day vulnerabilities targeting Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software VPN web servers
- **Impact**: Nation-state actors are deploying RayInitiator and LINE VIPER malware through these exploits, enabling persistent network access and espionage capabilities
- **Status**: Four actively exploited zero-days affecting millions of devices, with CISA issuing Emergency Mitigation Directive for federal agencies

### Cisco IOS Zero-Day Exploits
- **Description**: Additional zero-day vulnerabilities affecting Cisco IOS systems as part of the broader "ArcaneDoor" campaign
- **Impact**: Nation-state actors gain persistent access to critical network infrastructure
- **Status**: Actively exploited by previously identified threat groups behind ArcaneDoor operations

### XCSSET macOS Malware Variant
- **Description**: Updated version of XCSSET malware targeting Apple macOS systems with enhanced browser targeting capabilities
- **Impact**: Cryptocurrency clipper functionality, persistence modules, and enhanced data theft capabilities targeting Firefox browsers and Xcode developers
- **Status**: Limited active deployment with new persistence and clipping modules

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: Managed File Transfer software with maximum severity remote code execution vulnerability
- **Cisco ASA Firewalls**: Millions of Cisco Secure Firewall Adaptive Security Appliance devices worldwide
- **Cisco FTD Systems**: Cisco Secure Firewall Threat Defense Software installations
- **Cisco IOS Devices**: Various Cisco IOS-based network infrastructure components
- **Apple macOS**: Systems running macOS targeted by XCSSET malware variants
- **Firefox Browser**: Specifically targeted by new XCSSET variant with clipper modules
- **Salesforce Agentforce**: AI agent platform affected by ForcedLeak vulnerability
- **npm Ecosystem**: Postmark MCP package users affected by malicious code injection

## Attack Vectors and Techniques

- **Remote Code Execution**: Unauthenticated remote command injection through GoAnywhere MFT web interfaces
- **VPN Web Server Exploitation**: Targeting Cisco firewall VPN web servers for initial access
- **Supply Chain Compromise**: Malicious npm packages and compromised software suppliers
- **AI Prompt Injection**: ForcedLeak attacks against Salesforce AI agents to exfiltrate CRM data
- **Code Signing Abuse**: Iranian threat actors using legitimate SSL.com certificates to sign malware
- **Social Engineering**: Phishing campaigns impersonating Ukrainian government agencies
- **ClickFix Attacks**: COLDRIVER group utilizing fake error messages to deliver malware
- **Browser Extension Sideloading**: Malicious extensions being deployed through sideloading techniques

## Threat Actor Activities

- **Nation-State ArcaneDoor Operators**: Exploiting Cisco zero-days to deploy RayInitiator and LINE VIPER backdoors for espionage operations
- **COLDRIVER (Russian APT)**: Conducting ClickFix-style attacks with new lightweight malware families BO Team and Bearlyfy
- **UNC5221 (Chinese APT)**: Deploying Brickstorm backdoors on network edge devices that cannot run traditional EDR agents
- **Scattered Spider**: Conducted major attack against Co-operative Group resulting in $107 million in losses
- **Iranian Charming Kitten/Subtle Snail**: Using legitimate SSL.com code-signing certificates to sign and distribute malware
- **Vane Viper**: Operating global malware and ad fraud network generating over 1 trillion DNS queries through shell companies
- **Ukrainian Government Impersonators**: Delivering CountLoader, Amatera Stealer, and PureMiner through phishing campaigns
- **Supply Chain Attackers**: Targeting automotive manufacturers including Volvo through supplier ransomware attacks