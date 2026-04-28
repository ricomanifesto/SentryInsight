# Exploitation Report

The current threat landscape reveals a surge in sophisticated attack campaigns targeting critical infrastructure and enterprise systems. Threat actors are exploiting unpatched vulnerabilities in Windows RPC mechanisms, Cisco firewall devices, and third-party software platforms while simultaneously deploying advanced malware frameworks and conducting large-scale supply chain compromises. Notable activities include the discovery of a 20-year-old malware framework that predates Stuxnet, persistent malware surviving security updates on federal systems, and coordinated campaigns leveraging social engineering through legitimate cloud platforms.

## Active Exploitation Details

### PhantomRPC Windows Vulnerability
- **Description**: An architectural weakness in Windows Remote Procedure Call (RPC) mechanism that handles connections to unavailable services
- **Impact**: Enables privilege escalation with five different exploit paths discovered
- **Status**: Currently unpatched and actively exploitable

### TrueConf Video Conferencing Vulnerabilities
- **Description**: Multiple security flaws in TrueConf video conferencing software
- **Impact**: Complete server compromise and network breach capabilities
- **Status**: Actively exploited by PhantomCore hacktivist group since September 2025

### FIRESTARTER Persistent Backdoor
- **Description**: Custom malware targeting Cisco Firepower and Secure Firewall devices running Adaptive Security Appliance (ASA) software
- **Impact**: Persistent access to network infrastructure, survives security patches and updates
- **Status**: Confirmed infection of federal civilian agency device, remains active post-patching

### Four CISA KEV Vulnerabilities
- **Description**: Four vulnerabilities affecting SimpleHelp, Samsung MagicINFO 9 Server, and D-Link DIR-823X series routers
- **Impact**: Various compromise scenarios depending on affected system
- **Status**: Added to CISA Known Exploited Vulnerabilities catalog with May 2026 federal remediation deadline

## Affected Systems and Products

- **Windows Systems**: All versions affected by PhantomRPC RPC mechanism vulnerability
- **TrueConf Video Conferencing**: Servers running TrueConf software in Russian networks
- **Cisco Firepower/Secure Firewall**: Devices running Adaptive Security Appliance (ASA) software
- **SimpleHelp**: Remote support software platform
- **Samsung MagicINFO 9 Server**: Digital signage management platform
- **D-Link DIR-823X**: Series routers with known vulnerabilities
- **PyPI elementary-data Package**: Python package with 1.1 million monthly downloads
- **VS Code Extensions**: 73 malicious extensions on Open VSX repository
- **Microsoft Teams**: Leveraged for malware delivery and social engineering

## Attack Vectors and Techniques

- **Social Engineering via Microsoft Teams**: UNC6692 uses Teams platform to deploy Snow malware suite
- **Supply Chain Compromise**: Malicious PyPI package versions and fake VS Code extensions
- **SMS Blaster Devices**: Physical devices mimicking cellular towers for phishing message distribution
- **Fake CAPTCHA Schemes**: International Revenue Share Fraud (IRSF) campaigns using fake verification
- **Cloud Infrastructure Abuse**: AWS S3 buckets used for command and control operations
- **Deepfake Voice Technology**: Three-second audio samples sufficient for voice cloning attacks
- **Persistent Malware**: FIRESTARTER backdoor survives system updates and security patches

## Threat Actor Activities

- **UNC6692**: Multi-pronged campaign combining Microsoft Teams social engineering, custom Snow malware suite (browser extension, tunneler, backdoor), and AWS cloud infrastructure abuse
- **PhantomCore**: Pro-Ukrainian hacktivist group actively targeting Russian TrueConf servers since September 2025
- **ShinyHunters**: Extortion group responsible for ADT data breach affecting 5.5 million individuals and threatening data publication
- **GlassWorm Campaign**: Persistent information-stealing operation distributing malware through 73 fake VS Code extensions
- **Silk Typhoon**: Chinese state-sponsored group with member extradited to US for cyberespionage operations
- **fast16 Operators**: Historical threat actors operating Lua-based malware framework targeting engineering software five years before Stuxnet
- **Myanmar Fraud Ring**: 29-person operation including Cambodian senator targeting US citizens through fake investment sites