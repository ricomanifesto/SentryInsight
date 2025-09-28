# Exploitation Report

Multiple critical zero-day vulnerabilities are currently under active exploitation, with the most severe being CVE-2025-10035 in Fortra's GoAnywhere MFT platform, which has a maximum CVSS score of 10. Threat actors are leveraging this flaw for remote command injection without authentication. Additionally, Cisco firewall systems are being targeted through zero-day exploits affecting ASA and FTD software, with nation-state actors deploying specialized malware including RayInitiator and LINE VIPER. The threat landscape also features ongoing malware campaigns utilizing fake software installers, supply chain attacks, and advanced persistent threat operations targeting telecommunications and manufacturing sectors across Asia.

## Active Exploitation Details

### GoAnywhere MFT Zero-Day Vulnerability
- **Description**: A maximum severity vulnerability in Fortra's GoAnywhere MFT allowing remote command injection without authentication
- **Impact**: Complete system compromise through unauthenticated remote command execution
- **Status**: Actively exploited as zero-day with credible evidence of exploitation occurring approximately one week before public disclosure
- **CVE ID**: CVE-2025-10035

### Cisco ASA/FTD Zero-Day Vulnerabilities
- **Description**: Multiple security flaws affecting the VPN web server component of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software
- **Impact**: Nation-state actors deploying RayInitiator and LINE VIPER malware through exploitation
- **Status**: Actively exploited zero-days with CISA issuing Emergency Mitigation Directive
- **CVE ID**: Not specified in articles

### Brickstorm Backdoor Deployment
- **Description**: Chinese APT group UNC5221 compromising network appliances and edge devices that cannot run traditional EDR agents
- **Impact**: Persistent backdoor access to critical network infrastructure
- **Status**: Active campaign targeting edge devices with new Brickstorm backdoor variants

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: Managed File Transfer software with maximum severity vulnerability
- **Cisco ASA/FTD Firewalls**: Millions of devices affected by zero-day exploits
- **Microsoft Teams**: Fake installers distributing Oyster malware via malvertising
- **macOS Xcode Development Environment**: Targeted by new XCSSET malware variant
- **Network Edge Devices**: Compromised by Chinese APT for Brickstorm backdoor deployment
- **npm Packages**: Unofficial postmark-mcp package exfiltrating email communications
- **Salesforce Agentforce**: AI agent platform vulnerable to ForcedLeak attacks
- **Asian Telecommunications Infrastructure**: Targeted by PlugX and Bookworm malware campaigns

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched critical vulnerabilities in GoAnywhere MFT and Cisco firewalls
- **Malvertising and SEO Poisoning**: Fake Microsoft Teams installers promoted through search engine advertisements
- **Supply Chain Attacks**: Compromising software suppliers to target downstream organizations
- **ClickFix-Style Attacks**: COLDRIVER APT using deceptive user interaction to deploy lightweight malware
- **AI Prompt Injection**: ForcedLeak technique targeting Salesforce AI agents to exfiltrate CRM data
- **Phishing Campaigns**: Ukrainian government impersonation to deliver CountLoader and PureRAT
- **Code Signing Certificate Abuse**: Iranian threat actors using legitimate SSL.com certificates to sign malware

## Threat Actor Activities

- **UNC5221 (Chinese APT)**: Deploying Brickstorm backdoors on network edge devices and appliances
- **COLDRIVER (Russian APT)**: Conducting ClickFix-style attacks with BO Team and Bearlyfy malware families
- **Charming Kitten/Subtle Snail (Iranian)**: Using legitimate code-signing certificates to deploy malware
- **China-linked Groups**: Targeting Asian telecommunications and ASEAN networks with PlugX and Bookworm malware
- **Scattered Spider**: Responsible for $107 million loss at UK Co-operative Group
- **Vane Viper**: Operating global malware and ad fraud network generating 1 trillion DNS queries
- **Nation-State Actors**: Exploiting Cisco zero-days to deploy RayInitiator and LINE VIPER malware
- **Dutch Teenage Hackers**: Arrested for attempting to spy on Europol for Russian intelligence