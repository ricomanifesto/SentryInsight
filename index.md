# Exploitation Report

Current exploitation activity reveals several critical zero-day vulnerabilities being actively exploited in the wild, with threat actors targeting network infrastructure, enterprise applications, and VPN systems. The most severe incidents involve maximum severity vulnerabilities in Fortra GoAnywhere MFT (CVE-2025-10035) and multiple zero-day exploits targeting Cisco ASA firewalls. These attacks demonstrate sophisticated nation-state capabilities, with Chinese APT groups deploying advanced backdoors on network edge devices and Iranian state hackers leveraging code-signing certificates to deploy malware. The Akira ransomware group continues to evolve their tactics, successfully bypassing multi-factor authentication on SonicWall VPN systems, while various malware campaigns target both Windows and macOS systems through phishing and malvertising techniques.

## Active Exploitation Details

### Fortra GoAnywhere MFT Remote Code Execution
- **Description**: Maximum severity vulnerability allowing remote command injection without authentication
- **Impact**: Attackers can execute arbitrary commands remotely on affected systems without any authentication
- **Status**: Actively exploited as zero-day approximately one week before public disclosure
- **CVE ID**: CVE-2025-10035

### Cisco ASA Firewall Zero-Day Vulnerabilities
- **Description**: Security flaws impacting the VPN web server of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software
- **Impact**: Deployment of RayInitiator and LINE VIPER malware, potential complete system compromise
- **Status**: Actively exploited by threat actors, CISA issued Emergency Mitigation Directive

### SonicWall SSL VPN MFA Bypass
- **Description**: Akira ransomware attackers successfully logging into MFA-protected SonicWall VPN accounts despite OTP MFA being enabled
- **Impact**: Complete network compromise and ransomware deployment bypassing multi-factor authentication
- **Status**: Ongoing active exploitation with evolving attack techniques

### Salesforce Agentforce AI Prompt Injection
- **Description**: Critical flaw allowing indirect prompt injection attacks against AI agents
- **Impact**: Potential exfiltration of sensitive CRM data through AI agent manipulation
- **Status**: Recently patched after disclosure of "ForcedLeak" vulnerability

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: All versions affected by remote command injection vulnerability
- **Cisco ASA Firewalls**: VPN web servers in Cisco Secure Firewall ASA and FTD Software
- **SonicWall SSL VPN**: Devices with MFA-enabled accounts targeted by Akira ransomware
- **Salesforce Agentforce**: AI agent platform vulnerable to prompt injection attacks
- **Network Edge Devices**: Appliances that cannot run traditional EDR agents targeted with Brickstorm backdoors
- **Windows Systems**: Targeted by fake Microsoft Teams installers delivering Oyster backdoor
- **macOS Systems**: New XCSSET variant targeting Firefox browsers with clipper and persistence modules

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple critical vulnerabilities exploited before patches were available
- **MFA Bypass**: Advanced techniques to circumvent multi-factor authentication on VPN systems
- **Malvertising Campaigns**: SEO poisoning and search engine advertisements promoting fake software installers
- **Phishing Operations**: Impersonation of Ukrainian government agencies to deliver CountLoader and PureRAT
- **Supply Chain Attacks**: Targeting third-party suppliers to compromise major manufacturers like Volvo
- **Code Signing Certificate Abuse**: Iranian threat actors using legitimate SSL.com certificates to sign malware
- **AI Prompt Injection**: Indirect prompt injection to manipulate AI agents and exfiltrate data
- **Backdoor Deployment**: Installation of persistent backdoors on network infrastructure devices

## Threat Actor Activities

- **Chinese APT Groups**: Deploying PlugX and Bookworm malware targeting Asian telecommunications and ASEAN networks; UNC5221 compromising edge devices with Brickstorm backdoors
- **Akira Ransomware Group**: Continuously evolving attack methods to bypass MFA protection on SonicWall VPN systems
- **Iranian State Hackers**: Charming Kitten APT offshoot Subtle Snail using legitimate code-signing certificates from SSL.com to deploy malware
- **COLDRIVER (Russian APT)**: Attributed to ClickFix-style attacks delivering new lightweight malware families BO Team and Bearlyfy
- **Vane Viper**: Operating global malware and ad fraud network generating over 1 trillion DNS queries through shell companies
- **Dutch Teenagers**: Arrested for attempting to spy on Europol for Russia using hacking devices