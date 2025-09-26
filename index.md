# Exploitation Report

Critical zero-day vulnerabilities are currently under active exploitation, with Cisco firewall devices facing the most severe threat. Cisco ASA and FTD firewalls are being targeted by nation-state actors deploying sophisticated malware including RayInitiator and LINE VIPER backdoors. Additionally, a CVSS 10 vulnerability in Fortra GoAnywhere was exploited as a zero-day before public disclosure, while federal agencies have been compromised through a critical GeoServer flaw. The threat landscape also includes new macOS malware variants, supply chain attacks targeting developers, and AI-focused exploitation techniques.

## Active Exploitation Details

### Cisco ASA Firewall Zero-Day Vulnerabilities
- **Description**: Two critical zero-day vulnerabilities affecting the VPN web server of Cisco Secure Firewall ASA Software and Cisco Secure Firewall Threat Defense (FTD) Software
- **Impact**: Complete system compromise allowing deployment of advanced backdoors including RayInitiator and LINE VIPER malware
- **Status**: Actively exploited by nation-state actors; CISA has issued an emergency directive requiring federal agencies to patch immediately

### Fortra GoAnywhere Critical Vulnerability
- **Description**: A maximum severity CVSS 10 flaw in Fortra GoAnywhere Managed File Transfer (MFT) software
- **Impact**: Complete system compromise with credible evidence of active exploitation
- **Status**: Was exploited as a zero-day approximately one week before public disclosure; patches now available

### Cisco SNMP Vulnerability in IOS Software
- **Description**: High-severity security flaw in IOS Software and IOS XE Software affecting SNMP functionality
- **Impact**: Allows remote attackers to execute arbitrary code or trigger denial-of-service conditions
- **Status**: Actively exploited in the wild; patches available

### GeoServer Critical Vulnerability
- **Description**: Critical vulnerability in GeoServer geospatial software
- **Impact**: Led to successful breach of a large federal civilian executive branch (FCEB) agency
- **Status**: Exploited less than two weeks after initial disclosure
- **CVE ID**: CVE-2024-36401

### Salesforce ForcedLeak AI Vulnerability
- **Description**: Critical flaw in Salesforce Agentforce platform allowing indirect prompt injection attacks against AI agents
- **Impact**: Enables attackers to exfiltrate sensitive CRM data through AI prompt manipulation
- **Status**: Recently patched by Salesforce after researcher disclosure

## Affected Systems and Products

- **Cisco Secure Firewall ASA Software**: All versions running VPN web server functionality
- **Cisco Secure Firewall Threat Defense (FTD) Software**: All versions with VPN capabilities
- **Cisco IOS Software and IOS XE Software**: Devices with SNMP functionality enabled
- **Fortra GoAnywhere MFT**: All versions prior to security update
- **GeoServer**: Federal agencies using geospatial software platforms
- **Salesforce Agentforce**: AI agent platforms with insufficient security controls
- **macOS Systems**: Devices targeted by new XCSSET malware variants
- **Supermicro BMC Firmware**: Baseboard Management Controller systems
- **Developer Environments**: Rust Crates.io, npm packages, and Xcode development environments

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Nation-state actors leveraging unknown vulnerabilities before patches are available
- **Supply Chain Attacks**: Malicious packages in Rust Crates.io and npm repositories targeting cryptocurrency wallet keys
- **AI Prompt Injection**: ForcedLeak technique exploiting autonomous AI agents to leak sensitive data
- **Backdoor Deployment**: Persistent malware installation including RayInitiator, LINE VIPER, and Brickstorm backdoors
- **Browser Extension Manipulation**: XCSSET malware targeting Firefox with clipboard manipulation and persistence modules
- **DNS Infrastructure Abuse**: Vane Viper generating 1 trillion DNS queries to power malware and ad fraud networks
- **BMC Firmware Attacks**: Exploitation of Supermicro baseboard management controllers for persistent access

## Threat Actor Activities

- **Nation-State Groups**: Active exploitation of Cisco zero-days linked to previous ArcaneDoor campaign operators
- **UNC5221 (Chinese APT)**: Deploying Brickstorm backdoors on edge devices that cannot run traditional EDR agents
- **North Korean Actors**: Using AkdoorTea backdoor and TsunamiKit in Contagious Interview campaign targeting crypto developers
- **Scattered Spider**: Continued operations despite claimed shutdown, with financial losses exceeding $107 million reported by Co-op
- **Vane Viper**: Operating global malware and ad fraud network through shell companies and opaque ownership structures
- **Teen Hackers**: 17-year-old suspect in Vegas casino cyberattacks released to parents' custody