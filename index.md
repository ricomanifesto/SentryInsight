# Exploitation Report

Critical zero-day exploitation activity has emerged across multiple enterprise platforms, with attackers targeting high-value infrastructure components. The most severe threat involves active exploitation of CVE-2025-10035, a maximum severity vulnerability in Fortra's GoAnywhere MFT platform that allows remote command injection without authentication. Cisco firewall systems are under active attack through multiple zero-day vulnerabilities, prompting emergency directives from CISA. Additional concerns include sophisticated supply chain attacks affecting vehicle manufacturers, malware campaigns targeting macOS developers, and AI-based prompt injection vulnerabilities in enterprise platforms.

## Active Exploitation Details

### GoAnywhere MFT Zero-Day Vulnerability
- **Description**: Maximum severity vulnerability in Fortra's GoAnywhere MFT platform allowing remote command injection without authentication
- **Impact**: Attackers can execute arbitrary commands on affected systems without requiring valid credentials
- **Status**: Currently being actively exploited as a zero-day, exploitation confirmed one week before public disclosure
- **CVE ID**: CVE-2025-10035

### Cisco ASA Firewall Zero-Day Vulnerabilities
- **Description**: Multiple security flaws affecting the VPN web server of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software
- **Impact**: Threat actors are deploying RayInitiator and LINE VIPER malware through exploitation of these vulnerabilities
- **Status**: Actively exploited zero-days affecting millions of devices, CISA has issued emergency mitigation directive

### Salesforce AI Agent Vulnerability
- **Description**: Critical flaw in Salesforce Agentforce AI platform allowing prompt injection attacks to exfiltrate sensitive CRM data
- **Impact**: Attackers can force AI agents to leak sensitive customer and business data through indirect prompt injection
- **Status**: Patched by Salesforce following responsible disclosure

### XCSSET macOS Malware
- **Description**: Updated variant of XCSSET malware targeting macOS systems, particularly Xcode developers
- **Impact**: Enhanced browser targeting, clipboard manipulation, and persistence mechanisms affecting Firefox users
- **Status**: Active in limited attacks with new features for cryptocurrency theft and data exfiltration

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: All versions prior to latest security update
- **Cisco Secure Firewall ASA Software**: VPN web server components
- **Cisco Secure Firewall Threat Defense (FTD)**: Multiple versions affected
- **Salesforce Agentforce**: AI agent platform before security patches
- **macOS Systems**: Particularly targeting Xcode development environments
- **Firefox Browser**: Targeted by XCSSET malware variant
- **Volvo Group Systems**: Affected through supplier ransomware attack
- **npm Package Registry**: Malicious postmark-mcp package compromising email communications

## Attack Vectors and Techniques

- **Remote Command Injection**: Unauthenticated exploitation of GoAnywhere MFT systems
- **VPN Web Server Exploitation**: Targeting Cisco firewall VPN components
- **Supply Chain Attacks**: Compromising vehicle manufacturers through third-party suppliers
- **Prompt Injection**: Manipulating AI agents to exfiltrate sensitive data
- **Malicious Package Distribution**: Trojanized npm packages stealing email communications
- **ClickFix-Style Attacks**: COLDRIVER group using deceptive user interface elements
- **Browser Extension Sideloading**: Malicious extensions bypassing security controls
- **DNS Infrastructure Abuse**: Vane Viper generating trillion DNS queries for malware distribution

## Threat Actor Activities

- **COLDRIVER (Russian APT)**: Conducting fresh ClickFix-style attacks with new lightweight malware families
- **UNC5221 (Chinese APT)**: Deploying Brickstorm backdoors on network edge devices that cannot run traditional EDR agents
- **Iranian State Groups**: Using SSL.com certificates to sign malware, including Charming Kitten APT offshoot Subtle Snail
- **Scattered Spider**: Responsible for Co-operative Group attack resulting in $107 million losses
- **Nation-State Actors**: Exploiting Cisco zero-days including groups behind "ArcaneDoor" campaign
- **Vane Viper**: Operating global malware and ad fraud network through shell companies and DNS infrastructure abuse
- **Supply Chain Attackers**: Targeting automotive industry through third-party vendor compromises