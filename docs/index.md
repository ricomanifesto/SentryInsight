# Exploitation Report

Current threat landscape analysis reveals several critical exploitation campaigns targeting diverse platforms and systems. Active threats include the GlassWorm malware campaign leveraging 73 malicious VS Code extensions, the PhantomCore group exploiting TrueConf vulnerabilities in Russian networks, and the deployment of the FIRESTARTER backdoor on federal Cisco Firepower devices. Additional concerns include the PhantomRPC vulnerability in Windows enabling privilege escalation, supply chain compromises of popular Python packages, and sophisticated social engineering campaigns using Microsoft Teams to deploy custom Snow malware. CISA has added four new vulnerabilities to its Known Exploited Vulnerabilities catalog, emphasizing the ongoing threat from actively exploited flaws in SimpleHelp, Samsung MagicINFO, and D-Link routers.

## Active Exploitation Details

### GlassWorm v2 Malware Campaign
- **Description**: A persistent information-stealing campaign using 73 malicious Microsoft Visual Studio Code extensions on the Open VSX repository that act as "sleeper" extensions, turning malicious after updates
- **Impact**: Information theft from developer environments and compromised development workflows
- **Status**: Active campaign with malicious extensions still being distributed through legitimate channels

### PhantomCore TrueConf Exploitation
- **Description**: Pro-Ukrainian hacktivist group actively targeting TrueConf video conferencing software servers in Russia since September 2025
- **Impact**: Network compromise and breach of Russian infrastructure systems
- **Status**: Ongoing active exploitation campaign

### FIRESTARTER Backdoor
- **Description**: Sophisticated backdoor implanted on federal Cisco Firepower device running Adaptive Security Appliance (ASA) software
- **Impact**: Persistent access to federal network infrastructure that survives security patches
- **Status**: Confirmed compromise of federal civilian agency systems

### PhantomRPC Windows Vulnerability
- **Description**: Unpatched architectural weakness in Windows Remote Procedure Call (RPC) mechanism for handling connections to unavailable services
- **Impact**: Privilege escalation with five different exploit paths identified
- **Status**: Currently unpatched with active exploitation potential

### Snow Malware Deployment
- **Description**: Custom malware suite deployed by UNC6692 threat group using Microsoft Teams for social engineering
- **Impact**: Multi-component compromise including browser extension, tunneler, and backdoor capabilities
- **Status**: Active campaign targeting organizations through social engineering

### Elementary-data Package Compromise
- **Description**: Popular Python package with 1.1 million monthly downloads on PyPI was compromised to push information-stealing malware
- **Impact**: Developer credential theft and cryptocurrency wallet compromise
- **Status**: Malicious version pushed to legitimate package repository

### CISA KEV Additions
- **Description**: Four vulnerabilities added to Known Exploited Vulnerabilities catalog affecting SimpleHelp, Samsung MagicINFO 9 Server, and D-Link DIR-823X series routers
- **Impact**: Various exploitation capabilities across enterprise and network infrastructure
- **Status**: Active exploitation confirmed, federal remediation deadline set for May 2026

## Affected Systems and Products

- **Microsoft Visual Studio Code**: Open VSX marketplace extensions compromised with 73 malicious packages
- **TrueConf Video Conferencing**: Servers in Russian networks targeted by PhantomCore group
- **Cisco Firepower ASA**: Federal devices compromised with FIRESTARTER backdoor
- **Windows Operating System**: RPC mechanism vulnerable to PhantomRPC privilege escalation
- **Microsoft Teams**: Used as attack vector for Snow malware deployment
- **Python PyPI Repository**: Elementary-data package with 1.1M monthly downloads compromised
- **SimpleHelp Remote Access**: Vulnerability added to CISA KEV catalog
- **Samsung MagicINFO 9 Server**: Digital signage platform with exploited vulnerability
- **D-Link DIR-823X Routers**: Network devices with actively exploited flaws
- **Robinhood Trading Platform**: Account creation process exploited for phishing campaigns

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Malicious VS Code extensions and compromised Python packages distributed through legitimate repositories
- **Social Engineering**: Microsoft Teams used for initial access and Snow malware deployment
- **Persistent Backdoor Implantation**: FIRESTARTER backdoor designed to survive security patches on network infrastructure
- **Privilege Escalation**: PhantomRPC exploiting Windows RPC architectural weaknesses
- **Phishing Infrastructure**: Robinhood account creation process abused to inject malicious content into legitimate emails
- **SMS Blaster Attacks**: Physical devices mimicking cellular towers to send phishing messages
- **Fake CAPTCHA Schemes**: International Revenue Share Fraud (IRSF) using deceptive verification processes

## Threat Actor Activities

- **PhantomCore**: Pro-Ukrainian hacktivist group conducting sustained attacks against Russian TrueConf infrastructure since September 2025
- **UNC6692**: Newly discovered threat actor combining social engineering, custom malware, and cloud abuse tactics using Microsoft Teams and AWS S3 buckets
- **GlassWorm Operators**: Persistent campaign targeting developer environments through malicious VS Code extensions with sophisticated update mechanisms
- **ShinyHunters**: Extortion group responsible for ADT data breach affecting 5.5 million individuals
- **Federal Device Attackers**: Advanced persistent threat actors capable of implanting sophisticated backdoors on government network infrastructure
- **Silk Typhoon Member**: Chinese national conducting cyberespionage operations for intelligence services, recently extradited to the US
- **SMS Blaster Gang**: Canadian-based group using physical devices to impersonate cellular infrastructure for fraud campaigns