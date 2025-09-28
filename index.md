# Exploitation Report

Critical zero-day vulnerabilities are currently being exploited across multiple enterprise platforms, with threat actors targeting network infrastructure and managed file transfer systems. The most severe activity involves CVE-2025-10035, a maximum severity vulnerability in Fortra's GoAnywhere MFT that allows unauthenticated remote command injection and was exploited for approximately one week before public disclosure. Simultaneously, Cisco ASA firewall zero-day vulnerabilities are being actively exploited by nation-state actors to deploy sophisticated malware including RayInitiator and LINE VIPER. These attacks demonstrate coordinated campaigns targeting critical infrastructure components, with threat actors leveraging multiple sophisticated techniques including malvertising, supply chain compromises, and AI-powered attacks to maintain persistent access to corporate networks.

## Active Exploitation Details

### GoAnywhere MFT Remote Command Injection
- **Description**: Maximum severity vulnerability in Fortra's GoAnywhere Managed File Transfer software allowing remote command injection without authentication
- **Impact**: Complete system compromise, unauthorized file access, and potential lateral movement within enterprise networks
- **Status**: Zero-day exploitation detected one week before public disclosure, patches now available
- **CVE ID**: CVE-2025-10035

### Cisco ASA Firewall Zero-Day Vulnerabilities
- **Description**: Multiple security flaws in Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) VPN web servers
- **Impact**: Deployment of RayInitiator and LINE VIPER malware, persistent network access for espionage activities
- **Status**: Actively exploited by nation-state actors, emergency mitigation directive issued by CISA

### Salesforce Agentforce AI Prompt Injection
- **Description**: Critical vulnerability in Salesforce's AI agent platform allowing data exfiltration through indirect prompt injection attacks
- **Impact**: Unauthorized access to sensitive CRM data and customer information
- **Status**: Patched by Salesforce following responsible disclosure

### XCSSET macOS Malware Variant
- **Description**: Updated variant of macOS malware targeting Xcode developers with enhanced browser targeting capabilities
- **Impact**: Cryptocurrency wallet manipulation through clipper functionality, persistent system access
- **Status**: Limited attacks detected, targeting Firefox browsers specifically

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: All versions prior to latest security update
- **Cisco ASA/FTD Firewalls**: Multiple versions of Cisco Secure Firewall software
- **Salesforce Agentforce**: AI agent platform with CRM integration
- **macOS Systems**: Targeting Xcode development environments and Firefox browsers
- **Microsoft Teams**: Fake installers distributing Oyster backdoor malware
- **Network Appliances**: Edge devices targeted by Chinese APT groups with Brickstorm backdoors
- **npm Packages**: Malicious packages exfiltrating email communications

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Coordinated attacks against unpatched vulnerabilities in enterprise software
- **Malvertising Campaigns**: SEO poisoning and search engine advertisements promoting fake software installers
- **Supply Chain Attacks**: Compromising software distribution channels and npm packages
- **AI Prompt Injection**: Manipulating AI agents to leak sensitive data through crafted prompts
- **Code Signing Abuse**: Using legitimate SSL certificates to sign and distribute malware
- **ClickFix-Style Attacks**: Social engineering techniques to deliver lightweight malware families
- **DNS Infrastructure Abuse**: Generating massive DNS query volumes to support malware and ad fraud networks

## Threat Actor Activities

- **Nation-State Actors**: Exploiting Cisco firewall vulnerabilities to deploy advanced persistent threat malware
- **Chinese APT Groups**: UNC5221 deploying Brickstorm backdoors on network edge devices, PlugX malware campaigns targeting Asian telecommunications
- **Iranian State Hackers**: Charming Kitten APT offshoot Subtle Snail using SSL.com certificates to sign malware
- **COLDRIVER (Russian APT)**: Deploying BO Team and Bearlyfy malware families through ClickFix-style attacks
- **Scattered Spider**: Conducting ransomware attacks resulting in significant financial losses for targeted organizations
- **Vane Viper**: Operating global malware and ad fraud network generating over 1 trillion DNS queries
- **Dutch Teenagers**: Arrested for attempting to spy on Europol for Russian intelligence services