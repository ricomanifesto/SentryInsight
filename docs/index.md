# Exploitation Report

Current cybersecurity landscape reveals multiple active exploitation campaigns targeting diverse platforms and systems. Critical activities include the deployment of sophisticated malware frameworks like GlassWorm v2 through compromised VS Code extensions, exploitation of unpatched Windows privilege escalation vulnerabilities, and targeted attacks against enterprise infrastructure. Supply chain compromises continue to pose significant risks, with attackers infiltrating popular development tools and repositories to distribute malicious payloads. State-sponsored groups and financially motivated threat actors are leveraging social engineering techniques combined with custom malware to breach organizational networks and steal sensitive data.

## Active Exploitation Details

### PhantomRPC Windows Privilege Escalation Vulnerability
- **Description**: An architectural weakness in Windows' Remote Procedure Call (RPC) mechanism that handles connections to unavailable services, enabling five different exploit paths for privilege escalation
- **Impact**: Attackers can escalate privileges on Windows systems to gain elevated access and control
- **Status**: Currently unpatched with active exploitation potential

### TrueConf Video Conferencing Vulnerabilities
- **Description**: Multiple security flaws in TrueConf video conferencing software actively exploited by PhantomCore hacktivist group
- **Impact**: Complete compromise of Russian networks running vulnerable TrueConf servers
- **Status**: Actively exploited since September 2025 in targeted attacks against Russian infrastructure

### SimpleHelp, Samsung MagicINFO, and D-Link Router Vulnerabilities
- **Description**: Four vulnerabilities affecting SimpleHelp remote access software, Samsung MagicINFO 9 Server, and D-Link DIR-823X series routers recently added to CISA's Known Exploited Vulnerabilities catalog
- **Impact**: Remote code execution, unauthorized access, and network compromise
- **Status**: Actively exploited in the wild with federal agencies required to patch by May 2026

### Cisco Firepower ASA Software Backdoor
- **Description**: FIRESTARTER backdoor implanted in federal Cisco Firepower device running Adaptive Security Appliance software, demonstrating persistence through security patches
- **Impact**: Persistent unauthorized access to critical network security infrastructure
- **Status**: Confirmed compromise at unnamed federal civilian agency

## Affected Systems and Products

- **Microsoft Visual Studio Code**: 73 malicious extensions on Open VSX repository delivering GlassWorm v2 malware
- **Python Package Index (PyPI)**: elementary-data package with 1.1M monthly downloads compromised with infostealer malware
- **Windows Operating Systems**: Vulnerable to PhantomRPC privilege escalation attacks across multiple versions
- **TrueConf Video Conferencing**: Russian-deployed servers actively targeted and compromised
- **Robinhood Trading Platform**: Account creation process exploited for phishing email injection
- **Microsoft Teams**: Used as attack vector for deploying Snow malware suite
- **Cisco Firepower Devices**: Federal infrastructure compromised with persistent backdoor
- **SimpleHelp Remote Access**: Actively exploited vulnerabilities in remote support software
- **Samsung MagicINFO 9 Server**: Digital signage platform with exploited security flaws
- **D-Link DIR-823X Routers**: Consumer networking equipment with known exploited vulnerabilities

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Malicious VS Code extensions and PyPI package tampering to distribute malware
- **Social Engineering via Legitimate Platforms**: Microsoft Teams exploitation for malware delivery and Robinhood platform abuse for phishing
- **Privilege Escalation**: Windows RPC mechanism exploitation for elevated system access
- **Persistent Backdoors**: FIRESTARTER malware surviving security patches on network infrastructure
- **Phishing Email Injection**: Abuse of legitimate service account creation processes to send malicious emails
- **Fake CAPTCHA IRSF Scams**: International Revenue Share Fraud campaigns using fraudulent verification prompts
- **SMS Blaster Devices**: Rogue cellular tower equipment for mass phishing text distribution
- **Cloud Infrastructure Abuse**: AWS S3 buckets utilized for command and control operations

## Threat Actor Activities

- **PhantomCore**: Pro-Ukrainian hacktivist group actively targeting Russian TrueConf servers since September 2025, demonstrating sophisticated network breach capabilities
- **UNC6692**: Newly identified threat actor employing multi-vector campaigns combining social engineering, Microsoft Teams abuse, AWS cloud services, and custom Snow malware deployment
- **GlassWorm Operators**: Persistent malware campaign targeting development environments through 73 compromised VS Code extensions in OpenVSX repository
- **ShinyHunters**: Extortion group responsible for ADT data breach affecting 5.5 million individuals, demonstrating continued targeting of consumer service providers
- **Silk Typhoon**: Chinese state-sponsored group with member extradited to US for cyberespionage operations targeting sensitive government and commercial data
- **Myanmar-based Financial Fraud Ring**: Large-scale operation targeting US citizens through fake investment sites, with 29 individuals charged including high-ranking officials