# Exploitation Report

Critical exploitation activity is currently targeting network infrastructure and enterprise systems through multiple zero-day vulnerabilities and sophisticated attack campaigns. The most severe threats include active exploitation of Cisco ASA firewalls through zero-day vulnerabilities, a maximum severity flaw in Fortra's GoAnywhere MFT platform (CVE-2025-10035) being exploited in the wild, and ongoing Akira ransomware attacks successfully bypassing MFA-protected SonicWall VPN accounts. Nation-state actors, including Chinese APT groups and Iranian state hackers, are deploying advanced malware campaigns while leveraging legitimate code-signing certificates to evade detection.

## Active Exploitation Details

### Fortra GoAnywhere MFT Critical Vulnerability
- **Description**: Maximum severity vulnerability allowing remote command injection without authentication
- **Impact**: Attackers can execute arbitrary commands remotely on affected systems without requiring credentials
- **Status**: Actively exploited as zero-day approximately one week before public disclosure
- **CVE ID**: CVE-2025-10035

### Cisco ASA Firewall Zero-Day Vulnerabilities
- **Description**: Security flaws impacting the VPN web server of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software
- **Impact**: Deployment of RayInitiator and LINE VIPER malware, complete system compromise
- **Status**: Actively exploited by nation-state actors, CISA Emergency Mitigation Directive issued

### SonicWall SSL VPN MFA Bypass
- **Description**: Akira ransomware actors successfully bypassing OTP MFA protection on SonicWall SSL VPN accounts
- **Impact**: Unauthorized access to corporate networks despite multi-factor authentication
- **Status**: Ongoing active exploitation in ransomware campaigns

### Salesforce Agentforce AI Prompt Injection
- **Description**: Critical flaw in Salesforce Agentforce platform allowing data exfiltration through AI prompt injection attacks
- **Impact**: Exposure of sensitive CRM data and customer information
- **Status**: Patched by Salesforce following security researcher disclosure

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: Managed File Transfer software with maximum severity vulnerability
- **Cisco ASA Firewalls**: Adaptive Security Appliance software and Threat Defense systems
- **SonicWall SSL VPN**: VPN devices with MFA-enabled accounts being compromised
- **Salesforce Agentforce**: AI agent platform susceptible to prompt injection attacks
- **Microsoft Teams**: Fake installers distributing Oyster backdoor malware
- **macOS Systems**: XCSSET malware variant targeting Firefox browsers and Xcode developers
- **Asian Telecommunications**: Central and South Asian telecom and manufacturing sectors
- **Network Edge Devices**: Appliances targeted with Brickstorm backdoor deployments

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple zero-day vulnerabilities in network infrastructure devices
- **MFA Bypass**: Sophisticated techniques to circumvent multi-factor authentication on VPN systems
- **SEO Poisoning**: Search engine optimization manipulation and malicious advertisements
- **Supply Chain Attacks**: Targeting suppliers to compromise downstream organizations
- **Prompt Injection**: AI system manipulation to extract sensitive data
- **Code-Signing Abuse**: Legitimate SSL.com certificates used to sign malicious software
- **ClickFix Social Engineering**: Deceptive user interaction techniques for malware delivery
- **DNS Infrastructure Abuse**: Massive DNS query generation for malware and ad fraud networks

## Threat Actor Activities

- **Akira Ransomware Group**: Actively breaching MFA-protected VPN accounts and expanding attack capabilities
- **Chinese APT Groups**: Deploying PlugX and Bookworm malware variants targeting Asian telecommunications
- **UNC5221 (Chinese APT)**: Compromising edge devices with Brickstorm backdoor variants
- **Iranian State Actors**: Charming Kitten APT offshoot Subtle Snail using legitimate code-signing certificates
- **COLDRIVER (Russian APT)**: Conducting ClickFix-style attacks with new lightweight malware families
- **Vane Viper**: Operating global malware and ad fraud networks generating trillion DNS queries
- **Ukrainian Government Impersonators**: Phishing campaigns distributing CountLoader and PureRAT malware
- **Nation-State ArcaneDoor Operators**: Exploiting Cisco infrastructure with sophisticated malware deployment