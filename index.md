# Exploitation Report

Current exploitation activity is dominated by several critical zero-day vulnerabilities and active malware campaigns. The most severe threat involves a maximum severity zero-day vulnerability in Fortra's GoAnywhere MFT (CVE-2025-10035) that allows remote command injection without authentication and has been actively exploited for over a week. Cisco network infrastructure faces significant threats with multiple zero-day vulnerabilities in ASA firewalls and IOS systems being exploited by nation-state actors to deploy advanced backdoors. Malware distribution campaigns are leveraging sophisticated techniques including fake software installers, supply chain attacks, and AI-powered phishing to compromise organizations worldwide. China-linked APT groups continue targeting telecommunications and manufacturing sectors across Asia with advanced persistent access tools.

## Active Exploitation Details

### GoAnywhere MFT Zero-Day Vulnerability
- **Description**: Maximum severity authentication bypass vulnerability allowing remote command injection in Fortra's GoAnywhere Managed File Transfer software
- **Impact**: Complete system compromise without authentication, remote code execution with full system privileges
- **Status**: Actively exploited as zero-day for over a week before public disclosure, patches now available
- **CVE ID**: CVE-2025-10035

### Cisco ASA Firewall Zero-Day Vulnerabilities
- **Description**: Multiple security flaws impacting VPN web server functionality in Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Firewall Threat Defense (FTD) Software
- **Impact**: Remote code execution, deployment of RayInitiator and LINE VIPER malware, persistent backdoor access
- **Status**: Actively exploited by nation-state actors, CISA Emergency Directive issued, patches available

### Salesforce Agentforce AI Vulnerability
- **Description**: Critical flaw enabling indirect prompt injection attacks against AI agents lacking sufficient security controls
- **Impact**: Exfiltration of sensitive CRM data through manipulated AI agent responses
- **Status**: Patched by Salesforce following responsible disclosure

### XCSSET macOS Malware
- **Description**: Updated variant of known Apple macOS malware with enhanced capabilities targeting Xcode developers
- **Impact**: Browser hijacking, cryptocurrency clipboard manipulation, persistent system access, data theft
- **Status**: Active in limited attacks with new Firefox targeting and persistence modules

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: All versions prior to latest security patches
- **Cisco ASA Firewalls**: VPN web server components in ASA Software and FTD Software
- **Cisco IOS Systems**: Multiple device types affected by nation-state exploitation
- **Salesforce Agentforce Platform**: AI agent implementations prior to security patches
- **Apple macOS**: Xcode development environments targeted by XCSSET variant
- **Microsoft Teams**: Fake installers distributing Oyster backdoor malware
- **Network Edge Devices**: Appliances unable to run traditional EDR agents targeted with Brickstorm backdoors
- **npm Package Ecosystem**: Malicious postmark-mcp package silently exfiltrating email communications
- **SSL Certificate Infrastructure**: SSL.com certificates abused by Iranian state actors for malware signing

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Pre-disclosure attacks against unpatched critical vulnerabilities in enterprise software
- **Supply Chain Compromise**: Malicious npm packages and fake software installers distributed through legitimate channels
- **SEO Poisoning and Malvertising**: Search engine manipulation to promote fake Microsoft Teams installers
- **ClickFix-Style Attacks**: Social engineering techniques tricking users into executing malicious code
- **Prompt Injection**: AI-specific attacks manipulating agent responses to leak sensitive data
- **Certificate Abuse**: Legitimate SSL certificates used to sign and distribute malware payloads
- **Network Appliance Targeting**: Exploitation of edge devices that cannot deploy traditional security agents
- **Phishing Campaigns**: Government agency impersonation to deliver CountLoader and stealer malware

## Threat Actor Activities

- **China-Linked APT Groups**: Targeting telecommunications and manufacturing sectors in Central and South Asia with PlugX malware and Bookworm campaigns
- **UNC5221**: Chinese cyber-espionage group deploying Brickstorm backdoors on network edge devices
- **COLDRIVER (Russian APT)**: Fresh ClickFix-style attacks delivering BO Team and Bearlyfy lightweight malware families
- **Iranian State Actors**: Charming Kitten APT offshoot Subtle Snail using SSL.com certificates to sign malware
- **Scattered Spider**: Responsible for £80 million ($107 million) losses at Co-operative Group following major cyberattack
- **Vane Viper**: Operating global malware and ad fraud network generating over 1 trillion DNS queries
- **Nation-State Actors**: Exploiting Cisco zero-days as part of broader "ArcaneDoor" campaign targeting network infrastructure
- **Dutch Teenagers**: Arrested for attempting to conduct espionage operations against Europol for Russian intelligence