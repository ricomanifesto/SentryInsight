# Exploitation Report

Critical zero-day exploitation activity is currently targeting multiple high-profile systems, with the most severe threat being the maximum severity CVE-2025-10035 vulnerability in Fortra's GoAnywhere MFT platform that allows remote command injection without authentication. Simultaneously, Cisco firewall infrastructure faces active exploitation through multiple zero-day vulnerabilities affecting ASA and FTD systems, with threat actors deploying sophisticated malware including RayInitiator and LINE VIPER. The threat landscape is further complicated by ongoing Akira ransomware campaigns successfully bypassing MFA-protected SonicWall VPN accounts, Chinese APT groups distributing PlugX malware variants across Asian telecommunications networks, and the emergence of new malware families like the XCSSET variant targeting macOS developers.

## Active Exploitation Details

### Fortra GoAnywhere MFT Zero-Day
- **Description**: Maximum severity vulnerability allowing remote command injection without authentication in Fortra's GoAnywhere Managed File Transfer software
- **Impact**: Complete system compromise with ability to execute arbitrary commands remotely without any authentication requirements
- **Status**: Actively exploited as zero-day approximately one week before public disclosure; patches now available
- **CVE ID**: CVE-2025-10035

### Cisco ASA and FTD Firewall Zero-Days
- **Description**: Multiple security flaws affecting the VPN web server components of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software
- **Impact**: Deployment of sophisticated malware including RayInitiator and LINE VIPER backdoors on compromised firewall systems
- **Status**: Actively exploited by nation-state actors; CISA has issued Emergency Mitigation Directive requiring immediate patching

### SonicWall VPN MFA Bypass
- **Description**: Vulnerability in SonicWall SSL VPN devices allowing attackers to successfully authenticate despite OTP MFA being enabled on accounts
- **Impact**: Complete bypass of multi-factor authentication protections, enabling unauthorized access to corporate networks
- **Status**: Actively exploited by Akira ransomware operators in ongoing campaigns

### Salesforce Agentforce ForcedLeak Vulnerability
- **Description**: Critical flaw in Salesforce Agentforce AI platform susceptible to indirect prompt injection attacks
- **Impact**: Exposure and exfiltration of sensitive CRM data through AI agent manipulation
- **Status**: Patched by Salesforce following security research disclosure

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: Managed File Transfer software installations across enterprise environments
- **Cisco ASA Firewalls**: Adaptive Security Appliance devices running VPN web server components
- **Cisco FTD Systems**: Firewall Threat Defense software implementations
- **SonicWall SSL VPN**: VPN appliances with MFA-enabled accounts under active attack
- **Salesforce Agentforce**: AI agent platform for customer relationship management
- **macOS Systems**: Xcode development environments targeted by XCSSET malware variants
- **Asian Telecommunications**: Networks in Central and South Asian countries targeted by PlugX campaigns
- **Microsoft Teams**: Windows systems targeted through fake installer malvertising campaigns

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple vendors affected by previously unknown vulnerabilities being actively exploited before patches
- **MFA Bypass Techniques**: Advanced methods to circumvent one-time password multi-factor authentication on VPN systems
- **Supply Chain Attacks**: Targeting of third-party suppliers to compromise major manufacturers like Volvo
- **SEO Poisoning**: Manipulation of search engine results to promote malicious Microsoft Teams installers
- **Malvertising Campaigns**: Use of search engine advertisements to distribute Oyster backdoor malware
- **ClickFix-Style Attacks**: Social engineering techniques employed by COLDRIVER APT group
- **Indirect Prompt Injection**: AI-specific attack vector targeting Salesforce Agentforce systems
- **Code-Signing Certificate Abuse**: Iranian threat actors using legitimate SSL.com certificates to sign malware

## Threat Actor Activities

- **Akira Ransomware Group**: Conducting sophisticated campaigns against SonicWall VPN infrastructure with MFA bypass capabilities
- **Chinese APT Groups**: Deploying PlugX and Bookworm malware variants targeting Asian telecommunications and ASEAN networks
- **UNC5221 (Chinese APT)**: Compromising network appliances to deploy Brickstorm backdoor variants on edge devices
- **COLDRIVER (Russian APT)**: Launching ClickFix-style attacks delivering lightweight malware families BO Team and Bearlyfy
- **Iranian State Actors**: Charming Kitten APT offshoot Subtle Snail using legitimate code-signing certificates for malware distribution
- **Vane Viper**: Operating large-scale malware and ad fraud network generating over one trillion DNS queries globally
- **Nation-State Actors**: Targeting Cisco infrastructure through ArcaneDoor campaign and related zero-day exploitation