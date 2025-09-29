# Exploitation Report

The current threat landscape reveals several critical zero-day vulnerabilities under active exploitation, with particular concern around network infrastructure devices. Most notably, a maximum severity vulnerability in Fortra's GoAnywhere MFT (CVE-2025-10035) is being actively exploited to allow unauthenticated remote command injection. Additionally, Cisco network devices are experiencing a wave of zero-day attacks, with threat actors exploiting vulnerabilities in ASA firewalls and FTD software to deploy sophisticated malware. The Akira ransomware group continues to evolve their tactics, successfully bypassing MFA protections on SonicWall VPN devices. These incidents highlight the persistent targeting of critical network infrastructure and the rapid weaponization of newly disclosed vulnerabilities.

## Active Exploitation Details

### GoAnywhere MFT Command Injection Vulnerability
- **Description**: A maximum severity vulnerability in Fortra's GoAnywhere Managed File Transfer software that allows remote command injection without authentication
- **Impact**: Attackers can execute arbitrary commands on affected systems remotely without requiring any authentication credentials
- **Status**: Actively exploited as a zero-day approximately one week before public disclosure; patches are now available
- **CVE ID**: CVE-2025-10035

### Cisco ASA Firewall Zero-Day Vulnerabilities
- **Description**: Multiple security flaws affecting the VPN web server component of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software
- **Impact**: Threat actors can deploy malware including RayInitiator and LINE VIPER on compromised firewall devices, enabling persistent network access and espionage capabilities
- **Status**: Actively exploited by nation-state actors; CISA has issued an Emergency Mitigation Directive requiring immediate patching

### SonicWall VPN MFA Bypass
- **Description**: Vulnerability allowing Akira ransomware operators to authenticate to SonicWall SSL VPN devices despite multi-factor authentication being enabled
- **Impact**: Complete bypass of MFA security controls, enabling unauthorized VPN access for ransomware deployment
- **Status**: Ongoing exploitation by Akira ransomware group with evolving attack techniques

### Salesforce Agentforce AI Prompt Injection
- **Description**: Critical vulnerability in Salesforce Agentforce AI platform allowing indirect prompt injection attacks to exfiltrate sensitive CRM data
- **Impact**: Unauthorized access to customer relationship management data through maliciously crafted prompts that manipulate AI agent behavior
- **Status**: Recently patched by Salesforce after responsible disclosure

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: All versions prior to latest security update containing CVE-2025-10035 patch
- **Cisco ASA Firewalls**: Cisco Secure Firewall Adaptive Security Appliance Software and Threat Defense Software with VPN web server functionality
- **SonicWall SSL VPN**: Devices with multi-factor authentication enabled, specifically targeted by Akira ransomware
- **Salesforce Agentforce**: AI agent platform vulnerable to prompt injection attacks before recent patches
- **Network Edge Devices**: Various network appliances targeted by Chinese APT groups for Brickstorm backdoor deployment

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Immediate weaponization of undisclosed vulnerabilities, particularly in network infrastructure devices
- **MFA Bypass**: Advanced techniques to circumvent multi-factor authentication on VPN devices
- **Supply Chain Attacks**: Targeting of third-party suppliers to compromise major manufacturers like Volvo
- **AI Prompt Injection**: Manipulation of artificial intelligence agents through crafted prompts to extract sensitive data
- **Malvertising Campaigns**: Use of fake Microsoft Teams installers distributed through search engine advertisements and SEO poisoning
- **Phishing with Malware Delivery**: Campaigns impersonating Ukrainian government agencies to distribute CountLoader, Amatera Stealer, and PureMiner

## Threat Actor Activities

- **Akira Ransomware Group**: Evolved tactics now include successful bypass of MFA-protected VPN accounts on SonicWall devices, demonstrating advanced persistence capabilities
- **UNC5221 (Chinese APT)**: Actively compromising network edge devices that cannot run traditional EDR agents, deploying new variants of the Brickstorm backdoor for persistent access
- **COLDRIVER (Russian APT)**: Conducting fresh ClickFix-style attacks to deliver lightweight malware families BO Team and Bearlyfy, targeting Russian-focused operations
- **Charming Kitten/Subtle Snail (Iranian APT)**: Using legitimate SSL.com certificates to digitally sign malware, lending false credibility to malicious payloads
- **Nation-State Actors**: Multiple groups targeting Cisco infrastructure devices as part of the broader ArcaneDoor campaign, focusing on critical network infrastructure
- **PlugX Operators**: China-linked campaigns targeting telecommunications and manufacturing sectors across Central and South Asian countries, particularly ASEAN networks
- **Vane Viper**: Operating massive malware and ad fraud network generating over 1 trillion DNS queries through complex shell company structures