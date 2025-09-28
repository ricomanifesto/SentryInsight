# Exploitation Report

Critical zero-day vulnerabilities are actively being exploited across multiple enterprise platforms, with threat actors targeting Cisco firewall infrastructure, Fortra's GoAnywhere MFT systems, and leveraging sophisticated malware campaigns. The most concerning activity involves CVE-2025-10035 in GoAnywhere MFT with maximum CVSS severity, Cisco ASA firewall zero-days being exploited for nation-state operations, and widespread malware distribution campaigns targeting enterprise environments across multiple sectors.

## Active Exploitation Details

### GoAnywhere MFT Command Injection Vulnerability
- **Description**: A maximum severity vulnerability in Fortra's GoAnywhere Managed File Transfer software allowing remote command injection without authentication
- **Impact**: Attackers can execute arbitrary commands on affected systems remotely without requiring authentication credentials
- **Status**: Actively exploited as zero-day approximately one week before public disclosure; patches now available
- **CVE ID**: CVE-2025-10035

### Cisco ASA Firewall Zero-Day Vulnerabilities
- **Description**: Security flaws affecting the VPN web server component of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software
- **Impact**: Nation-state actors deploying RayInitiator and LINE VIPER malware through exploitation of these vulnerabilities
- **Status**: Actively exploited zero-days with CISA Emergency Mitigation Directive issued; patches available

### Salesforce Agentforce AI Prompt Injection
- **Description**: Critical flaw in Salesforce Agentforce AI agent platform allowing data exfiltration through indirect prompt injection attacks
- **Impact**: Attackers can force AI agents to leak sensitive CRM data and customer information
- **Status**: Recently patched by Salesforce after responsible disclosure

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: Managed file transfer software with maximum severity command injection vulnerability
- **Cisco ASA/FTD Firewalls**: VPN web server components vulnerable to nation-state exploitation
- **Salesforce Agentforce**: AI agent platform susceptible to prompt injection attacks
- **macOS Systems**: Targeted by updated XCSSET malware variant affecting Xcode developers
- **Windows Systems**: Targeted by fake Microsoft Teams installers distributing Oyster backdoor
- **Network Appliances**: Edge devices compromised with Brickstorm backdoors by Chinese APT groups
- **npm Package Ecosystem**: Unofficial postmark-mcp package silently exfiltrating email communications

## Attack Vectors and Techniques

- **Malvertising Campaigns**: SEO poisoning and search engine advertisements promoting fake Microsoft Teams installers
- **Supply Chain Attacks**: Compromised npm packages stealing email communications through minimal code additions
- **ClickFix-Style Attacks**: COLDRIVER APT group using deceptive social engineering to deliver lightweight malware families
- **Zero-Day Exploitation**: Nation-state actors leveraging undisclosed vulnerabilities in enterprise infrastructure
- **Prompt Injection**: Sophisticated attacks against AI systems to bypass security controls and extract sensitive data
- **Phishing Operations**: Ukrainian government agency impersonation to deliver CountLoader and associated malware

## Threat Actor Activities

- **COLDRIVER (Russian APT)**: Deploying new lightweight malware families through ClickFix-style social engineering attacks
- **UNC5221 (Chinese APT)**: Compromising network appliances with new Brickstorm backdoor variants targeting edge devices that cannot run traditional EDR agents
- **Charming Kitten/Subtle Snail (Iranian APT)**: Using legitimate SSL.com certificates to sign malware and evade detection
- **Nation-State Actors**: Exploiting Cisco firewall zero-days to deploy RayInitiator and LINE VIPER malware for espionage operations
- **Scattered Spider**: Responsible for $107 million loss at Co-operative Group through sophisticated cyberattack
- **Vane Viper**: Operating global malware and ad fraud network generating over 1 trillion DNS queries through shell company infrastructure