# Exploitation Report

The current threat landscape is dominated by several critical zero-day exploitations and active malware campaigns. Most notably, Cisco firewall systems are under widespread attack through two zero-day vulnerabilities in ASA and FTD software, prompting CISA to issue an emergency directive. Simultaneously, Fortra's GoAnywhere MFT platform faces active exploitation of CVE-2025-10035, a maximum severity vulnerability allowing remote command injection without authentication. Additional threats include updated XCSSET macOS malware variants targeting developers, Iranian state actors using legitimate SSL certificates for malware signing, and sophisticated phishing campaigns delivering CountLoader and associated stealers. The threat landscape also features supply chain compromises affecting major automotive manufacturers and malicious npm packages stealing email communications.

## Active Exploitation Details

### Cisco ASA/FTD Zero-Day Vulnerabilities
- **Description**: Two zero-day vulnerabilities affecting the VPN web server of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software
- **Impact**: Attackers can deploy RayInitiator and LINE VIPER malware, enabling persistent access and data exfiltration from network infrastructure
- **Status**: Actively exploited in the wild, patches available, CISA emergency directive issued requiring federal agencies to patch immediately

### GoAnywhere MFT Critical Vulnerability
- **Description**: Maximum severity vulnerability in Fortra's GoAnywhere Managed File Transfer software allowing remote command injection
- **Impact**: Unauthenticated remote code execution enabling complete system compromise
- **Status**: Actively exploited as zero-day approximately one week before public disclosure
- **CVE ID**: CVE-2025-10035

### XCSSET macOS Malware Variant
- **Description**: Updated version of known macOS malware targeting Xcode developers with enhanced capabilities
- **Impact**: Browser targeting, clipboard manipulation (clipper functionality), and improved persistence mechanisms
- **Status**: Limited active attacks observed, targeting Firefox browsers specifically

### Salesforce ForcedLeak Vulnerability
- **Description**: Critical flaw in Salesforce Agentforce platform enabling AI prompt injection attacks
- **Impact**: Unauthorized access to sensitive CRM data through indirect prompt injection against autonomous agents
- **Status**: Patched by Salesforce following researcher disclosure

## Affected Systems and Products

- **Cisco Secure Firewall ASA Software**: VPN web server components vulnerable to zero-day exploitation
- **Cisco Secure Firewall Threat Defense (FTD) Software**: Network security appliances targeted by nation-state actors
- **Fortra GoAnywhere MFT**: File transfer software with maximum severity vulnerability
- **Apple macOS Systems**: Targeted by XCSSET malware variants, specifically Xcode development environments
- **Firefox Browsers on macOS**: Specifically targeted by new XCSSET variant
- **Salesforce Agentforce Platform**: AI agent platform vulnerable to prompt injection attacks
- **npm Package Ecosystem**: Malicious postmark-mcp package stealing email communications
- **Network Edge Devices**: Various appliances targeted by Chinese APT groups for Brickstorm backdoor deployment

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in Cisco firewalls and GoAnywhere MFT
- **Supply Chain Compromise**: Malicious npm packages mimicking legitimate projects to steal sensitive data
- **Phishing Campaigns**: SVG-based phishing emails impersonating Ukrainian government agencies to deliver CountLoader
- **Code Signing Abuse**: Iranian threat actors using legitimate SSL.com certificates to sign malware
- **AI Prompt Injection**: Indirect prompt injection attacks against Salesforce AI agents to extract CRM data
- **Malware Sideloading**: Browser extension sideloading techniques bypassing security controls
- **ClickFix-Style Attacks**: Social engineering attacks disguised as software fixes to deliver malware

## Threat Actor Activities

- **Nation-State Actors**: Exploitation of Cisco zero-days attributed to previously identified nation-state group behind "ArcaneDoor" campaign
- **COLDRIVER (Russian APT)**: Deploying BO Team and Bearlyfy malware families through ClickFix-style social engineering attacks
- **Iranian Charming Kitten/Subtle Snail**: Using legitimate SSL certificates from SSL.com to sign and distribute malware
- **UNC5221 (Chinese APT)**: Deploying Brickstorm backdoors on network edge devices that cannot run traditional EDR agents
- **Scattered Spider**: Responsible for Co-operative Group attack resulting in $107 million financial losses
- **Vane Viper**: Operating global malware and ad fraud network generating over 1 trillion DNS queries
- **Ukrainian Government Impersonators**: Conducting phishing campaigns to deliver CountLoader, Amatera Stealer, and PureMiner
- **Supply Chain Attackers**: Targeting automotive manufacturers including Volvo through ransomware attacks on suppliers