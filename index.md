# Exploitation Report

Critical zero-day vulnerabilities are currently being exploited in the wild, with the most severe being a maximum severity flaw in Fortra's GoAnywhere MFT platform (CVE-2025-10035) that allows remote command injection without authentication. Additionally, Cisco ASA firewall zero-day vulnerabilities are being actively exploited by threat actors to deploy sophisticated malware including RayInitiator and LINE VIPER. These attacks demonstrate sophisticated adversary capabilities, with evidence showing exploitation occurring approximately one week before public disclosure. The exploitation landscape also includes ongoing supply chain attacks, malvertising campaigns distributing backdoors, and advanced persistent threat groups deploying new malware variants targeting critical infrastructure and development environments.

## Active Exploitation Details

### Fortra GoAnywhere MFT Zero-Day Vulnerability
- **Description**: A maximum severity vulnerability affecting Fortra's GoAnywhere Managed File Transfer software that allows remote command injection without authentication
- **Impact**: Attackers can execute commands remotely on affected systems without requiring authentication credentials
- **Status**: Currently being actively exploited as a zero-day with credible evidence of exploitation occurring one week before public disclosure
- **CVE ID**: CVE-2025-10035

### Cisco ASA Firewall Zero-Day Vulnerabilities
- **Description**: Multiple security flaws impacting the VPN web server of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software
- **Impact**: Threat actors are deploying RayInitiator and LINE VIPER malware through exploitation of these vulnerabilities
- **Status**: Actively exploited zero-day vulnerabilities with CISA issuing an Emergency Mitigation Directive

### Salesforce Agentforce ForcedLeak Vulnerability
- **Description**: Critical flaw affecting Salesforce Agentforce AI agent platform that allows indirect prompt injection attacks
- **Impact**: Attackers can potentially exfiltrate sensitive CRM data through AI prompt manipulation
- **Status**: Recently patched by Salesforce following security research disclosure

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: Managed file transfer software with maximum severity vulnerability allowing unauthenticated remote command injection
- **Cisco ASA/FTD Firewalls**: Cisco Secure Firewall Adaptive Security Appliance and Threat Defense software with multiple zero-day vulnerabilities
- **Salesforce Agentforce**: AI agent platform vulnerable to prompt injection attacks exposing CRM data
- **macOS Systems**: Targeted by new XCSSET malware variant affecting Firefox browsers and Xcode development environments
- **Windows Systems**: Affected by Oyster backdoor malware distributed through fake Microsoft Teams installers
- **Network Edge Devices**: Compromised by Chinese APT groups deploying Brickstorm backdoors on devices that cannot run traditional EDR agents

## Attack Vectors and Techniques

- **Malvertising Campaigns**: SEO poisoning and search engine advertisements promoting fake Microsoft Teams installers delivering Oyster backdoor malware
- **Supply Chain Attacks**: Compromised npm packages like the unofficial postmark-mcp silently exfiltrating users' email communications
- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in critical infrastructure components like firewalls and file transfer systems
- **Phishing Operations**: Ukrainian government agency impersonation campaigns delivering CountLoader, Amatera Stealer, and PureMiner malware
- **ClickFix-Style Attacks**: COLDRIVER APT group deploying lightweight malware families through deceptive user interface elements
- **Code-Signing Certificate Abuse**: Iranian state hackers using SSL.com certificates to sign malware and evade security controls
- **AI Prompt Injection**: Indirect prompt injection attacks against autonomous AI agents lacking sufficient security controls

## Threat Actor Activities

- **COLDRIVER APT Group**: Russian advanced persistent threat group conducting ClickFix-style attacks with new lightweight malware families targeting Russian-focused operations
- **Chinese APT UNC5221**: Deploying new versions of Brickstorm backdoors on network edge devices that cannot run traditional endpoint detection and response agents
- **Charming Kitten/Subtle Snail**: Iranian state-sponsored threat actors using SSL.com code-signing certificates to deploy signed malware in espionage operations
- **Scattered Spider**: Cybercriminal group responsible for major financial impact attacks, including the Co-operative Group attack resulting in $107 million in losses
- **Vane Viper**: Threat actor operating global malware and ad fraud network generating over 1 trillion DNS queries through shell companies and opaque ownership structures
- **Dutch Teen Operatives**: Two 17-year-old individuals arrested for attempting to spy on Europol for Russian intelligence services using hacking devices
- **Chinese-Linked Groups**: Multiple campaigns targeting Asian telecommunications and ASEAN networks with PlugX and Bookworm malware variants