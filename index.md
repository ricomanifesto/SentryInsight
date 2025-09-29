# Exploitation Report

The cybersecurity landscape is experiencing a surge of critical zero-day exploitations, with threat actors actively targeting network infrastructure and enterprise systems. Most notably, Cisco firewalls are under widespread attack through multiple zero-day vulnerabilities, prompting an emergency directive from CISA. Simultaneously, Fortra's GoAnywhere MFT platform faces maximum severity exploitation through CVE-2025-10035, while ransomware groups continue to breach MFA-protected VPN systems. Nation-state actors, particularly China-linked APT groups, are deploying sophisticated backdoors on network edge devices and telecommunications infrastructure, demonstrating persistent and evolving threats to critical systems worldwide.

## Active Exploitation Details

### Cisco ASA Firewall Zero-Day Vulnerabilities
- **Description**: Multiple security flaws impacting the VPN web server of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software
- **Impact**: Deployment of RayInitiator and LINE VIPER malware, complete system compromise, and persistent backdoor installation
- **Status**: Actively exploited as zero-days, CISA has issued an Emergency Mitigation Directive requiring immediate patching

### GoAnywhere MFT Command Injection Vulnerability
- **Description**: Maximum severity vulnerability in Fortra's GoAnywhere Managed File Transfer software allowing remote command injection without authentication
- **Impact**: Complete system compromise with ability to execute arbitrary commands remotely
- **Status**: Actively exploited as zero-day for approximately one week before public disclosure
- **CVE ID**: CVE-2025-10035

### Brickstorm Backdoor Deployment on Edge Devices
- **Description**: Chinese APT group UNC5221 compromising network appliances that cannot run traditional EDR agents
- **Impact**: Persistent backdoor access to critical network infrastructure, data exfiltration capabilities
- **Status**: Ongoing campaign targeting edge devices globally

### SonicWall VPN MFA Bypass
- **Description**: Akira ransomware group successfully bypassing multi-factor authentication on SonicWall SSL VPN devices
- **Impact**: Complete network compromise despite MFA protections, ransomware deployment
- **Status**: Ongoing attacks with evolving bypass techniques

## Affected Systems and Products

- **Cisco Secure Firewall ASA Software**: VPN web server components affected by zero-day exploits
- **Cisco Secure Firewall Threat Defense (FTD)**: Multiple versions vulnerable to active exploitation
- **Fortra GoAnywhere MFT**: All versions prior to latest security patches vulnerable to command injection
- **SonicWall SSL VPN Devices**: MFA-protected accounts being successfully compromised
- **Network Edge Devices**: Various appliances targeted by Brickstorm backdoor deployment
- **Telecommunications Infrastructure**: Central and South Asian telecom sectors under active attack
- **Salesforce Agentforce Platform**: AI agents vulnerable to prompt injection attacks exposing CRM data

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Coordinated attacks on Cisco firewall infrastructure using previously unknown vulnerabilities
- **Command Injection**: Remote code execution on GoAnywhere MFT systems without authentication requirements
- **MFA Bypass**: Advanced techniques to circumvent one-time password protections on VPN systems
- **Backdoor Deployment**: Installation of persistent access tools on network appliances
- **PlugX and Bookworm Malware**: Distribution through telecommunications and manufacturing sector targeting
- **SEO Poisoning**: Fake Microsoft Teams installers distributed through search engine manipulation
- **ClickFix-Style Attacks**: Social engineering techniques to deliver lightweight malware families
- **Prompt Injection**: AI agent manipulation to extract sensitive CRM data through crafted inputs

## Threat Actor Activities

- **UNC5221 (Chinese APT)**: Deploying Brickstorm backdoors on edge devices globally, focusing on network appliances without EDR capabilities
- **Akira Ransomware Group**: Evolving techniques to breach MFA-protected VPN accounts, targeting SonicWall infrastructure specifically
- **COLDRIVER (Russian APT)**: Launching ClickFix-style attacks with new lightweight malware families BO Team and Bearlyfy
- **Charming Kitten/Subtle Snail (Iranian)**: Using legitimate SSL.com certificates to sign malware, enhancing evasion capabilities
- **China-Linked Groups**: Targeting Asian telecommunications and ASEAN networks with PlugX and Bookworm malware variants
- **Vane Viper**: Operating massive DNS-based malware and ad fraud network generating over 1 trillion DNS queries
- **Nation-State Actors**: Exploiting Cisco zero-days as part of the previously identified "ArcaneDoor" campaign infrastructure