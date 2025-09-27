# Exploitation Report

A critical wave of zero-day exploitations has emerged targeting infrastructure systems, with the most severe being CVE-2025-10035 in Fortra's GoAnywhere MFT and multiple Cisco firewall vulnerabilities. These exploitations represent active threats to enterprise networks, with threat actors deploying sophisticated malware campaigns including RayInitiator, LINE VIPER, and various nation-state backed operations. The exploitation activity spans from maximum severity command injection flaws to supply chain attacks affecting major corporations, highlighting the urgent need for immediate patching and enhanced security measures across affected platforms.

## Active Exploitation Details

### Fortra GoAnywhere MFT Command Injection
- **Description**: A maximum severity vulnerability allowing remote command injection without authentication in Fortra's GoAnywhere Managed File Transfer software
- **Impact**: Attackers can execute arbitrary commands remotely on affected systems without authentication
- **Status**: Actively exploited as zero-day approximately one week before public disclosure
- **CVE ID**: CVE-2025-10035

### Cisco ASA Firewall Zero-Day Vulnerabilities
- **Description**: Critical security flaws in Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software affecting VPN web servers
- **Impact**: Exploitation allows deployment of malware including RayInitiator and LINE VIPER backdoors, enabling persistent network access and espionage capabilities
- **Status**: Actively exploited in zero-day attacks, CISA has issued emergency directive for federal agencies to patch immediately
- **CVE ID**: Not explicitly provided in source articles

### Salesforce ForcedLeak AI Prompt Injection
- **Description**: Critical vulnerability in Salesforce Agentforce platform allowing indirect prompt injection attacks against AI agents
- **Impact**: Attackers can force AI agents to leak sensitive CRM data and customer information through malicious prompt manipulation
- **Status**: Recently patched by Salesforce after researcher disclosure

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: Managed File Transfer software with maximum severity remote command injection vulnerability
- **Cisco ASA/FTD Firewalls**: VPN web server components vulnerable to zero-day exploitation
- **Salesforce Agentforce**: AI agent platform susceptible to prompt injection attacks
- **macOS Systems**: XCSSET malware variant targeting Xcode developers and Firefox browsers
- **npm Package Ecosystem**: Malicious postmark-mcp package exfiltrating email communications
- **Network Edge Devices**: Various appliances targeted by Chinese APT group UNC5221 with Brickstorm backdoors
- **Supply Chain Targets**: Volvo and other automotive manufacturers affected through supplier compromises

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple critical vulnerabilities exploited before patches were available
- **Supply Chain Attacks**: Targeting third-party suppliers to compromise major corporations like Volvo
- **Malicious NPM Packages**: Package typosquatting and malicious updates to steal email communications
- **AI Prompt Injection**: Manipulating AI agents to leak sensitive data through crafted prompts
- **Browser Extension Sideloading**: Malicious extensions bypassing security controls in web browsers
- **Phishing Campaigns**: SVG-based attacks and ClickFix-style social engineering targeting Ukraine and Vietnam
- **Code Signing Certificate Abuse**: Iranian threat actors using legitimate SSL.com certificates to sign malware

## Threat Actor Activities

- **COLDRIVER (Russian APT)**: Deploying lightweight malware families through ClickFix-style attacks
- **Charming Kitten/Subtle Snail (Iranian)**: Using legitimate code-signing certificates to distribute malware
- **UNC5221 (Chinese APT)**: Compromising network edge devices with Brickstorm backdoor variants
- **Scattered Spider**: Responsible for $107 million in losses to Co-operative Group through sophisticated attack
- **Nation-State Actors**: Exploiting Cisco zero-days as part of broader ArcaneDoor campaign
- **Vane Viper**: Operating massive DNS-based malware and ad fraud network generating over 1 trillion queries
- **Supply Chain Attackers**: Targeting automotive industry through third-party supplier compromises