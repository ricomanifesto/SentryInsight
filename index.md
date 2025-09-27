# Exploitation Report

The current threat landscape is dominated by several critical zero-day vulnerabilities being actively exploited in the wild. Most notably, Cisco firewall devices are under active attack through zero-day exploits targeting ASA and FTD software, prompting an emergency directive from CISA. Additionally, Fortra's GoAnywhere MFT platform has been compromised through a maximum severity vulnerability that was exploited as a zero-day before public disclosure. The threat landscape also includes sophisticated malware campaigns from state-sponsored groups, with Iranian actors using legitimate code-signing certificates and Chinese APTs deploying new backdoor variants on network appliances.

## Active Exploitation Details

### Cisco ASA and FTD Zero-Day Vulnerabilities
- **Description**: Two security flaws affecting the VPN web server of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software
- **Impact**: Allows threat actors to deploy malware including RayInitiator and LINE VIPER backdoors on compromised network devices
- **Status**: Actively exploited as zero-days; CISA has issued an emergency directive requiring federal agencies to patch these vulnerabilities
- **CVE ID**: Not specified in the articles

### Fortra GoAnywhere MFT Critical Vulnerability
- **Description**: Maximum severity vulnerability in Fortra's GoAnywhere Managed File Transfer software allowing remote command injection without authentication
- **Impact**: Enables attackers to execute arbitrary commands remotely without authentication
- **Status**: Actively exploited as zero-day approximately one week before public disclosure; patches now available
- **CVE ID**: CVE-2025-10035

### Salesforce Agentforce ForcedLeak Vulnerability
- **Description**: Critical flaw in Salesforce Agentforce platform allowing indirect prompt injection attacks against AI agents
- **Impact**: Enables attackers to exfiltrate sensitive CRM data through AI prompt injection techniques
- **Status**: Recently patched by Salesforce after security research disclosure

## Affected Systems and Products

- **Cisco ASA Software**: Secure Firewall Adaptive Security Appliance devices with VPN web server functionality
- **Cisco FTD Software**: Secure Firewall Threat Defense devices with VPN web server functionality
- **Fortra GoAnywhere MFT**: Managed File Transfer software platforms allowing unauthenticated remote access
- **Salesforce Agentforce**: AI agent platform vulnerable to prompt injection attacks
- **macOS Systems**: Targeted by new XCSSET malware variant affecting Xcode developers and Firefox browsers
- **npm Package Ecosystem**: postmark-mcp package users affected by malicious code injection

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple threat actors exploiting unpatched vulnerabilities in network infrastructure devices
- **Supply Chain Attacks**: Compromise of third-party suppliers affecting major manufacturers like Volvo
- **Malicious Code Signing**: Iranian threat actors using legitimate SSL.com certificates to sign malware
- **AI Prompt Injection**: ForcedLeak technique targeting AI agents to extract sensitive data
- **Phishing Campaigns**: SVG-based phishing attacks delivering CountLoader, Amatera Stealer, and PureMiner
- **Package Poisoning**: Malicious npm packages exfiltrating email communications from users

## Threat Actor Activities

- **Iranian State Actors (Charming Kitten/Subtle Snail)**: Deploying malware signed with legitimate SSL.com certificates to evade detection
- **Chinese APT Group (UNC5221)**: Compromising network appliances to deploy new Brickstorm backdoor variants on edge devices
- **Russian APT (COLDRIVER)**: Conducting ClickFix-style attacks delivering new lightweight malware families (BO Team and Bearlyfy)
- **Nation-State Actor (ArcaneDoor)**: Previously linked to exploitation of Cisco devices, now associated with current zero-day attacks
- **Scattered Spider**: Responsible for $107 million in losses to The Co-operative Group through sophisticated attack campaign
- **Vane Viper**: Operating global malware and ad fraud network generating over 1 trillion DNS queries through shell companies