# Exploitation Report

Critical zero-day vulnerabilities are currently under active exploitation across multiple enterprise security platforms, with the most severe activity targeting Cisco ASA firewalls and Fortra GoAnywhere MFT systems. CVE-2025-10035, a maximum severity vulnerability in GoAnywhere MFT, has been exploited as a zero-day allowing remote command injection without authentication. Meanwhile, threat actors have deployed sophisticated malware campaigns including new variants of XCSSET targeting macOS developers and nation-state groups leveraging backdoors on network edge devices. The exploitation landscape is further complicated by supply chain attacks targeting developer ecosystems through malicious npm packages and Rust crates designed to steal sensitive credentials.

## Active Exploitation Details

### Fortra GoAnywhere MFT Zero-Day Vulnerability
- **Description**: A maximum severity vulnerability allowing remote command injection without authentication in Fortra's GoAnywhere Managed File Transfer software
- **Impact**: Attackers can execute arbitrary commands remotely without requiring authentication credentials
- **Status**: Actively exploited as zero-day approximately one week before public disclosure; patch now available
- **CVE ID**: CVE-2025-10035

### Cisco ASA Firewall Zero-Day Vulnerabilities
- **Description**: Two security flaws impacting the VPN web server of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software
- **Impact**: Enables deployment of RayInitiator and LINE VIPER malware on compromised firewall systems
- **Status**: Actively exploited in zero-day attacks; CISA has issued emergency directive for federal agencies to patch immediately

### Salesforce Agentforce AI Prompt Injection Flaw
- **Description**: Critical vulnerability in Salesforce Agentforce AI platform allowing indirect prompt injection attacks dubbed "ForcedLeak"
- **Impact**: Enables attackers to exfiltrate sensitive CRM data through manipulation of AI agent responses
- **Status**: Patched by Salesforce following responsible disclosure

### XCSSET macOS Malware Variant
- **Description**: Updated version of known macOS malware targeting Apple developers, particularly those using Xcode
- **Impact**: Enhanced browser targeting capabilities, clipboard manipulation, and improved persistence mechanisms
- **Status**: Detected in limited attacks with new features including Firefox targeting

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: All versions prior to latest security update vulnerable to remote command injection
- **Cisco ASA Firewalls**: Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Threat Defense (FTD) Software
- **macOS Systems**: Xcode developers and users of Firefox browsers targeted by XCSSET variant
- **Salesforce Agentforce**: AI agent platform vulnerable to prompt injection attacks
- **npm Ecosystem**: Unofficial postmark-mcp package containing malicious code for email exfiltration
- **Rust Crates.io**: Two malicious packages with nearly 8,500 downloads targeting cryptocurrency wallet keys

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Attackers exploiting unpatched vulnerabilities before public disclosure, particularly in enterprise security appliances
- **Supply Chain Poisoning**: Malicious packages distributed through legitimate software repositories to steal developer credentials and sensitive data
- **Prompt Injection**: Manipulation of AI systems through crafted inputs to bypass security controls and extract confidential information
- **ClickFix-Style Attacks**: Social engineering techniques used by COLDRIVER group to deliver lightweight malware families
- **Browser-Based Attacks**: Enhanced targeting of web browsers, particularly Firefox, for credential theft and persistence

## Threat Actor Activities

- **COLDRIVER (Russian APT)**: Conducting ClickFix-style attacks to deliver new lightweight malware families as part of Russia-focused cyber operations
- **UNC5221 (Chinese APT)**: Deploying "Brickstorm" backdoors on network edge devices that cannot run traditional EDR agents
- **Scattered Spider**: Responsible for cyberattack against Co-op Group resulting in £80 million ($107 million) operating profit loss
- **North Korean Actors**: Using new AkdoorTea backdoor along with TsunamiKit in Contagious Interview campaign targeting global cryptocurrency developers
- **Nation-State Actors**: Exploiting Cisco firewall zero-days as part of broader "ArcaneDoor" campaign targeting critical infrastructure
- **Vane Viper**: Operating global malware and ad fraud network generating 1 trillion DNS queries through complex shell company structures