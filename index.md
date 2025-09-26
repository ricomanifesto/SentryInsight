# Exploitation Report

The current threat landscape reveals several critical zero-day exploitations across major infrastructure components. Most notably, Cisco firewall systems are under active attack through two zero-day vulnerabilities that have prompted an emergency directive from CISA. Additionally, Fortra's GoAnywhere MFT platform faces maximum severity exploitation through a command injection flaw that was exploited as a zero-day before public disclosure. Russian APT groups continue sophisticated campaigns using new malware variants, while supply chain attacks target developers through malicious packages in popular repositories. These activities demonstrate coordinated efforts by nation-state actors and cybercriminals to compromise critical infrastructure and development environments.

## Active Exploitation Details

### Cisco ASA Firewall Zero-Day Vulnerabilities
- **Description**: Two security flaws impacting the VPN web server of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software
- **Impact**: Attackers can deploy RayInitiator and LINE VIPER malware, with exploitation attributed to nation-state actors behind the "ArcaneDoor" campaign
- **Status**: Actively exploited in zero-day attacks, patches available, CISA emergency directive issued for federal agencies

### GoAnywhere MFT Command Injection Flaw
- **Description**: Maximum severity vulnerability allowing remote command injection without authentication
- **Impact**: Complete system compromise and unauthorized access to managed file transfer systems
- **Status**: Exploited as zero-day approximately one week before public disclosure, patches now available
- **CVE ID**: CVE-2025-10035

### Salesforce Agentforce AI Prompt Injection
- **Description**: Critical flaw in Salesforce Agentforce platform allowing indirect prompt injection against autonomous AI agents
- **Impact**: Potential exfiltration of sensitive CRM data through forced AI agent responses
- **Status**: Recently patched by Salesforce after researcher disclosure

## Affected Systems and Products

- **Cisco ASA/FTD Firewalls**: VPN web server components across millions of deployed devices
- **Fortra GoAnywhere MFT**: Managed file transfer software installations
- **Salesforce Agentforce**: AI agent platform for CRM automation
- **macOS Systems**: Targeted by new XCSSET malware variant affecting Xcode developers
- **NPM Ecosystem**: Unofficial postmark-mcp package stealing email communications
- **Rust Crates.io**: Two malicious packages with nearly 8,500 downloads targeting crypto wallet keys
- **Firefox Browser**: Targeted by updated XCSSET malware with clipper and persistence modules

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Cisco firewall vulnerabilities exploited by nation-state actors before patches were available
- **Supply Chain Attacks**: Malicious packages in NPM and Rust repositories targeting developers
- **Phishing Campaigns**: SVG-based attacks impersonating Ukrainian government agencies delivering CountLoader
- **ClickFix-Style Attacks**: COLDRIVER APT group using social engineering to deploy lightweight malware
- **Prompt Injection**: AI-targeted attacks against Salesforce autonomous agents
- **Backdoor Deployment**: Chinese APT group UNC5221 deploying Brickstorm backdoors on edge devices
- **Cryptocurrency Theft**: AkdoorTea backdoor used by North Korean hackers in fake interview campaigns

## Threat Actor Activities

- **COLDRIVER (Russian APT)**: Conducting ClickFix-style attacks with new lightweight malware families including BO Team and Bearlyfy
- **UNC5221 (Chinese APT)**: Compromising network appliances to deploy new versions of Brickstorm backdoor
- **Nation-State Actors**: Exploiting Cisco zero-days as part of ArcaneDoor campaign targeting critical infrastructure
- **North Korean Groups**: Using AkdoorTea backdoor in Contagious Interview campaigns targeting crypto developers globally
- **Scattered Spider**: Responsible for $107 million loss at Co-operative Group through sophisticated cyberattack
- **Vane Viper**: Operating global malware and ad fraud network generating 1 trillion DNS queries
- **Ukrainian Impersonators**: Phishing campaign targeting Ukraine and Vietnam using government agency impersonation
- **Cryptocurrency Thieves**: Multiple campaigns targeting developers through malicious packages and fake interview processes