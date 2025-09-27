# Exploitation Report

The cybersecurity landscape is currently experiencing a surge of critical zero-day exploitations, with Cisco firewall infrastructure being the primary target of active attacks. Multiple maximum severity vulnerabilities are being exploited in the wild, including CVE-2025-10035 in Fortra's GoAnywhere MFT platform and two zero-day flaws in Cisco ASA firewalls that prompted an emergency directive from CISA. Nation-state actors, particularly Iranian and Chinese APT groups, are deploying sophisticated malware campaigns using legitimate code-signing certificates and targeting critical network infrastructure. The exploitation activity spans multiple attack vectors, from supply chain compromises affecting major vehicle manufacturers to AI-based prompt injection attacks against enterprise platforms.

## Active Exploitation Details

### Fortra GoAnywhere MFT Command Injection Vulnerability
- **Description**: A maximum severity vulnerability allowing remote command injection without authentication in Fortra's GoAnywhere Managed File Transfer software
- **Impact**: Attackers can execute arbitrary commands remotely on affected systems without requiring authentication credentials
- **Status**: Actively exploited as zero-day with credible evidence of exploitation occurring one week before public disclosure
- **CVE ID**: CVE-2025-10035

### Cisco ASA Firewall Zero-Day Vulnerabilities
- **Description**: Two critical security flaws affecting the VPN web server component of Cisco Secure Firewall ASA and FTD software
- **Impact**: Nation-state actors are deploying RayInitiator and LINE VIPER malware through these vulnerabilities
- **Status**: Actively exploited in zero-day attacks, prompting CISA Emergency Directive requiring federal agencies to patch immediately

### Salesforce Agentforce AI Prompt Injection Flaw
- **Description**: Critical vulnerability dubbed "ForcedLeak" allowing indirect prompt injection against AI agents in Salesforce's Agentforce platform
- **Impact**: Attackers can force AI agents to leak sensitive CRM data and customer information through malicious prompts
- **Status**: Patched by Salesforce after researcher disclosure

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: Managed File Transfer software experiencing maximum severity command injection attacks
- **Cisco ASA Firewalls**: Secure Firewall Adaptive Security Appliance and Threat Defense software with VPN web server vulnerabilities
- **Cisco IOS Devices**: Multiple network devices affected by recently disclosed zero-day vulnerabilities
- **Salesforce Agentforce**: AI agent platform vulnerable to prompt injection attacks exposing CRM data
- **macOS Systems**: XCSSET malware variant targeting Xcode developers and Firefox browser users
- **Vehicle Manufacturers**: Volvo and other international manufacturers affected by supply chain ransomware attacks

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Nation-state actors exploiting undisclosed vulnerabilities in Cisco firewall infrastructure before patches become available
- **Supply Chain Attacks**: Ransomware groups targeting third-party suppliers to compromise major manufacturers like Volvo
- **Phishing Campaigns**: Ukrainian government impersonation attacks delivering CountLoader malware to drop Amatera Stealer and PureMiner
- **Code-Signing Certificate Abuse**: Iranian threat actors using legitimate SSL.com certificates to sign and deploy malware
- **AI Prompt Injection**: Sophisticated attacks against autonomous AI agents to extract sensitive enterprise data
- **DNS Infrastructure Abuse**: Vane Viper generating over 1 trillion DNS queries to power global malware and ad fraud networks

## Threat Actor Activities

- **Iranian State Hackers (Charming Kitten/Subtle Snail)**: Deploying malware signed with legitimate SSL.com certificates for enhanced evasion
- **Chinese APT UNC5221**: Compromising network edge devices to deploy "Brickstorm" backdoor variants on appliances that cannot run traditional EDR agents
- **COLDRIVER (Russian APT)**: Conducting ClickFix-style attacks delivering lightweight malware families in Russia-focused cyberattacks
- **Scattered Spider**: Conducted major attack against The Co-operative Group resulting in £80 million ($107 million) in losses
- **Vane Viper**: Operating massive DNS-based malware and ad fraud network through shell companies and opaque ownership structures
- **Nation-State Actors**: Exploiting Cisco zero-days as part of "ArcaneDoor" campaign targeting critical network infrastructure