# Exploitation Report

Critical zero-day vulnerabilities are being actively exploited across multiple high-value targets, with Cisco firewall devices and Fortra GoAnywhere MFT systems facing the most severe threats. The exploitation landscape reveals sophisticated nation-state campaigns targeting telecommunications infrastructure, supply chain attacks affecting major manufacturers, and malware campaigns leveraging legitimate code-signing certificates. Most concerning is the active exploitation of CVE-2025-10035, a maximum severity flaw in GoAnywhere MFT, alongside multiple Cisco ASA firewall zero-days that prompted an emergency directive from CISA.

## Active Exploitation Details

### Fortra GoAnywhere MFT Critical Vulnerability
- **Description**: A maximum severity vulnerability allowing remote command injection without authentication
- **Impact**: Complete system compromise through unauthenticated remote command execution
- **Status**: Zero-day exploitation detected approximately one week before public disclosure; patches now available
- **CVE ID**: CVE-2025-10035

### Cisco ASA Firewall Zero-Day Vulnerabilities
- **Description**: Multiple security flaws impacting VPN web server functionality in Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD)
- **Impact**: Deployment of RayInitiator and LINE VIPER malware, complete firewall compromise
- **Status**: Actively exploited by nation-state actors; CISA emergency directive issued requiring immediate patching

### PlugX Malware Campaign Vulnerabilities
- **Description**: Exploitation targeting telecommunications and manufacturing sectors using updated PlugX malware variant
- **Impact**: Long-term persistence in critical infrastructure networks across Central and South Asia
- **Status**: Ongoing campaign attributed to China-linked threat actors

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: All versions prior to security update containing remote command injection vulnerability
- **Cisco ASA Software**: Multiple versions of Secure Firewall Adaptive Security Appliance and Threat Defense software
- **macOS Systems**: Xcode development environments targeted by XCSSET malware variant
- **Telecommunications Infrastructure**: Central and South Asian telecom providers and ASEAN networks
- **Microsoft Outlook**: Organizations experiencing encrypted email handling errors
- **npm Package Ecosystem**: Users of unofficial postmark-mcp package experiencing email exfiltration

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Attackers leveraging previously unknown vulnerabilities in GoAnywhere MFT and Cisco firewalls
- **Supply Chain Compromise**: Ransomware attacks targeting automotive suppliers affecting Volvo and other manufacturers
- **Malicious Code Signing**: Iranian threat actors using legitimate SSL.com certificates to sign malware
- **ClickFix Social Engineering**: COLDRIVER group using fake error messages to deliver malware
- **Package Supply Chain Poisoning**: Malicious npm package silently exfiltrating email communications
- **Phishing Campaigns**: Ukrainian government impersonation distributing CountLoader and PureRAT malware

## Threat Actor Activities

- **China-Linked APT Groups**: Deploying PlugX and Bookworm malware against Asian telecommunications and manufacturing sectors; UNC5221 group deploying Brickstorm backdoors on edge devices
- **Iranian State Actors**: Charming Kitten APT offshoot Subtle Snail using legitimate code-signing certificates for malware distribution
- **COLDRIVER (Russian APT)**: Conducting ClickFix-style attacks delivering BO Team and Bearlyfy lightweight malware families
- **Scattered Spider**: Responsible for $107 million loss at Co-operative Group through sophisticated cyberattack
- **Vane Viper**: Operating global malware and ad fraud network generating over 1 trillion DNS queries through shell companies