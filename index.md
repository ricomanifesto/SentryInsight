# Exploitation Report

Critical zero-day vulnerabilities are actively being exploited across multiple high-profile platforms, with threat actors targeting Cisco firewall infrastructure, Fortra's GoAnywhere MFT systems, and leveraging sophisticated malware campaigns. The most severe threats include CVE-2025-10035 (CVSS 10.0) in GoAnywhere MFT being exploited as a zero-day, and multiple Cisco ASA firewall vulnerabilities that prompted CISA to issue an Emergency Directive. Nation-state actors, particularly China-linked groups, are deploying advanced backdoors and conducting supply chain attacks while using legitimate code-signing certificates to evade detection.

## Active Exploitation Details

### GoAnywhere MFT Zero-Day Vulnerability
- **Description**: Maximum severity vulnerability in Fortra's GoAnywhere Managed File Transfer software that allows remote command injection without authentication
- **Impact**: Attackers can execute arbitrary commands remotely on affected systems without any authentication requirements
- **Status**: Actively exploited as zero-day approximately one week before public disclosure; patches now available
- **CVE ID**: CVE-2025-10035

### Cisco ASA Firewall Zero-Day Vulnerabilities
- **Description**: Multiple security flaws impacting the VPN web server of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software
- **Impact**: Nation-state actors deploying RayInitiator and LINE VIPER malware through these vulnerabilities
- **Status**: Actively exploited by threat actors; CISA issued Emergency Directive for immediate patching

### XCSSET macOS Malware Variant
- **Description**: Updated version of known Apple macOS malware targeting Xcode developers with enhanced browser targeting capabilities
- **Impact**: Cryptocurrency clipboard manipulation, enhanced persistence mechanisms, and expanded browser targeting including Firefox
- **Status**: Actively deployed in limited attacks with new clipper and persistence modules

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: All versions prior to latest security update
- **Cisco ASA and FTD Firewalls**: Millions of devices affected by VPN web server vulnerabilities
- **Apple macOS Systems**: Xcode development environments targeted by XCSSET variant
- **Microsoft Teams**: Windows systems targeted through fake installer campaigns
- **Salesforce Agentforce**: AI agent platform vulnerable to prompt injection attacks
- **Network Edge Devices**: Various appliances targeted by Brickstorm backdoor deployments
- **Ukrainian Government Systems**: Targeted by CountLoader and PureRAT phishing campaigns

## Attack Vectors and Techniques

- **Malvertising Campaigns**: SEO poisoning and search engine advertisements promoting fake Microsoft Teams installers distributing Oyster backdoor
- **Supply Chain Attacks**: Compromised npm packages like unofficial 'postmark-mcp' silently exfiltrating email communications
- **Phishing Operations**: Ukrainian government impersonation campaigns delivering CountLoader, Amatera Stealer, and PureMiner
- **Code-Signing Certificate Abuse**: Iranian threat groups using legitimate SSL.com certificates to sign malware and evade detection
- **ClickFix-Style Attacks**: COLDRIVER APT group deploying BO Team and Bearlyfy malware families
- **AI Prompt Injection**: ForcedLeak attacks against Salesforce AI agents to extract sensitive CRM data
- **DNS Infrastructure Abuse**: Vane Viper generating 1 trillion DNS queries for global malware and ad fraud operations

## Threat Actor Activities

- **China-linked APT Groups**: PlugX and Bookworm malware campaigns targeting Asian telecom and ASEAN networks; UNC5221 deploying Brickstorm backdoors on network appliances
- **COLDRIVER (Russian APT)**: Fresh ClickFix-style attacks delivering lightweight malware families for espionage operations
- **Iranian State Hackers**: Charming Kitten APT offshoot Subtle Snail using legitimate code-signing certificates for malware distribution
- **Vane Viper**: Operating massive DNS-based infrastructure supporting global malware distribution and ad fraud networks through shell companies
- **Nation-State Actors**: Exploiting Cisco firewall vulnerabilities to deploy RayInitiator and LINE VIPER malware for persistent access
- **Dutch Teenagers**: Arrested for attempting to spy on Europol using hacking devices in coordination with Russian interests