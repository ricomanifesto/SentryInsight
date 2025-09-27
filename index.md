# Exploitation Report

Critical zero-day exploitation activity is dominating the threat landscape, with multiple maximum severity vulnerabilities being actively exploited across enterprise infrastructure. The most severe incidents involve Fortra's GoAnywhere MFT platform suffering from a CVSS 10.0 vulnerability (CVE-2025-10035) that enables remote command injection without authentication, and Cisco ASA/FTD firewall systems being targeted through zero-day attacks deploying advanced malware including RayInitiator and LINE VIPER. Nation-state actors, particularly Iranian and Chinese APT groups, are leveraging these vulnerabilities alongside sophisticated supply chain attacks and malware campaigns targeting critical infrastructure and government agencies.

## Active Exploitation Details

### GoAnywhere MFT Remote Command Injection Vulnerability
- **Description**: A maximum severity vulnerability in Fortra's GoAnywhere Managed File Transfer software that allows attackers to inject commands remotely without authentication
- **Impact**: Complete system compromise with the ability to execute arbitrary commands on affected systems
- **Status**: Actively exploited as a zero-day approximately one week before public disclosure; patches now available
- **CVE ID**: CVE-2025-10035

### Cisco ASA/FTD Firewall Zero-Day Vulnerabilities
- **Description**: Multiple zero-day vulnerabilities affecting the VPN web server component of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software
- **Impact**: Deployment of sophisticated malware including RayInitiator and LINE VIPER backdoors, enabling persistent network access and espionage capabilities
- **Status**: Actively exploited in targeted attacks by nation-state actors; CISA has issued emergency directive requiring federal agencies to patch immediately

### Salesforce Agentforce AI Prompt Injection Flaw
- **Description**: Critical vulnerability dubbed "ForcedLeak" that affects Salesforce Agentforce AI agent platform, allowing indirect prompt injection attacks
- **Impact**: Unauthorized access to sensitive CRM data and customer information through AI agent manipulation
- **Status**: Recently patched by Salesforce following security research disclosure

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: All versions vulnerable to remote command injection without authentication
- **Cisco ASA/FTD Firewalls**: VPN web server components across millions of deployed devices
- **Salesforce Agentforce**: AI agent platforms with insufficient security controls for autonomous operations
- **macOS Systems**: Targeted by new XCSSET malware variant affecting Xcode developers and Firefox users
- **Edge Network Devices**: Compromised by Chinese APT group UNC5221 deploying Brickstorm backdoors
- **npm Package Ecosystem**: postmark-mcp package used for email exfiltration attacks

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple campaigns leveraging unpatched vulnerabilities before public disclosure
- **Supply Chain Attacks**: Compromised npm packages and vendor systems affecting downstream customers
- **Phishing Campaigns**: ClickFix-style attacks delivering CountLoader, Amatera Stealer, and PureMiner
- **AI Prompt Injection**: Indirect prompt injection techniques targeting autonomous AI agents
- **Certificate Abuse**: Legitimate SSL.com code-signing certificates used to sign malware
- **DNS Infrastructure Abuse**: Vane Viper generating over 1 trillion DNS queries to support malware and ad fraud networks

## Threat Actor Activities

- **Iranian APT Groups**: Charming Kitten offshoot Subtle Snail deploying malware signed with legitimate certificates from SSL.com
- **COLDRIVER (Russian APT)**: Fresh ClickFix-style attacks delivering BO Team and Bearlyfy malware families
- **UNC5221 (Chinese APT)**: Compromising edge network devices to deploy new Brickstorm backdoor variants
- **Nation-State Actors**: Exploiting Cisco firewall zero-days to deploy RayInitiator and LINE VIPER malware for espionage
- **Scattered Spider**: Continued ransomware operations resulting in significant financial losses, including $107 million impact on UK Co-operative Group
- **Supply Chain Attackers**: Targeting Ukrainian government agencies and Vietnamese entities through phishing campaigns impersonating official communications