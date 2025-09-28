# Exploitation Report

The cybersecurity landscape is currently experiencing intense exploitation activity across multiple fronts, with several critical zero-day vulnerabilities being actively exploited in the wild. The most concerning developments include a maximum severity zero-day flaw in Fortra's GoAnywhere MFT platform (CVE-2025-10035) allowing unauthenticated remote command injection, multiple actively exploited zero-day vulnerabilities in Cisco ASA firewalls and IOS devices, and sophisticated malware campaigns targeting organizations worldwide. Chinese state-sponsored actors are deploying advanced backdoors on edge devices, while Iranian threat groups are leveraging legitimate SSL certificates to sign malware. Additionally, AI-powered attack vectors are emerging, with vulnerabilities discovered in Salesforce's AI agents that could expose sensitive CRM data through prompt injection attacks.

## Active Exploitation Details

### GoAnywhere MFT Command Injection Vulnerability
- **Description**: A maximum severity vulnerability in Fortra's GoAnywhere Managed File Transfer software that allows remote command injection without authentication
- **Impact**: Attackers can execute arbitrary commands remotely on affected systems without requiring valid credentials
- **Status**: Actively exploited as a zero-day for approximately one week before public disclosure; patches have been released
- **CVE ID**: CVE-2025-10035

### Cisco ASA Firewall Zero-Day Vulnerabilities
- **Description**: Multiple zero-day security flaws impacting the VPN web server of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software
- **Impact**: Deployment of RayInitiator and LINE VIPER malware; complete compromise of firewall systems
- **Status**: Actively exploited by nation-state actors; CISA has issued Emergency Mitigation Directive; patches available

### Cisco IOS Zero-Day Exploits
- **Description**: Zero-day vulnerabilities affecting Cisco IOS devices, part of a broader wave of actively exploited Cisco vulnerabilities
- **Impact**: Device compromise and potential network infiltration
- **Status**: Actively exploited; affects millions of devices; patches required immediately

### Salesforce AI Agent Vulnerability (ForcedLeak)
- **Description**: Critical flaw in Salesforce Agentforce platform allowing indirect prompt injection attacks against autonomous AI agents
- **Impact**: Potential exfiltration of sensitive CRM data through manipulated AI agent responses
- **Status**: Recently patched by Salesforce following security research disclosure

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: Managed File Transfer software installations across enterprise environments
- **Cisco ASA Firewalls**: Secure Firewall Adaptive Security Appliance Software and Threat Defense Software
- **Cisco IOS Devices**: Various network infrastructure devices running Cisco IOS
- **Salesforce Agentforce**: AI agent platform and associated CRM systems
- **Microsoft Teams**: Targeted by fake installer campaigns delivering Oyster backdoor malware
- **macOS Systems**: Targeted by updated XCSSET malware variant focusing on Xcode developers
- **Edge Network Devices**: Compromised by Chinese APT groups deploying Brickstorm backdoors
- **Firefox Browsers**: Specifically targeted by macOS XCSSET variant with clipper modules

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in critical infrastructure
- **Supply Chain Attacks**: Compromising software suppliers to target downstream customers, as seen in Volvo ransomware incident
- **Malvertising Campaigns**: SEO poisoning and search engine advertisements promoting fake Microsoft Teams installers
- **Prompt Injection**: Sophisticated AI manipulation techniques targeting autonomous agents in enterprise platforms
- **ClickFix Attacks**: COLDRIVER APT group employing fake software update prompts to deliver malware
- **Certificate Abuse**: Iranian state hackers using legitimate SSL.com certificates to sign malware for trusted execution
- **NPM Package Poisoning**: Malicious packages mimicking legitimate projects to steal email communications
- **DNS Infrastructure Abuse**: Vane Viper generating over 1 trillion DNS queries for malware distribution and ad fraud

## Threat Actor Activities

- **Chinese APT Groups (UNC5221)**: Deploying Brickstorm backdoors on edge devices; targeting telecom and manufacturing sectors with PlugX and Bookworm malware campaigns across Central and South Asia
- **Iranian State Actors (Charming Kitten/Subtle Snail)**: Leveraging legitimate code-signing certificates from SSL.com to deploy signed malware for enhanced trust and evasion
- **COLDRIVER (Russian APT)**: Conducting fresh ClickFix-style attacks delivering BO Team and Bearlyfy lightweight malware families
- **Scattered Spider**: Responsible for major financial impact attack against Co-operative Group, resulting in £80 million ($107 million) in losses
- **Nation-State Actors**: Exploiting Cisco zero-day vulnerabilities as part of the "ArcaneDoor" campaign, demonstrating advanced persistent threat capabilities
- **Ukrainian Government Impersonators**: Conducting phishing campaigns distributing CountLoader, Amatera Stealer, and PureMiner malware
- **Vane Viper**: Operating massive DNS-based malware distribution and ad fraud network with complex shell company structures