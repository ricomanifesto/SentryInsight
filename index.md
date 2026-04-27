# Exploitation Report

Critical exploitation activity is currently dominated by several significant security incidents including an unpatched Windows privilege escalation flaw, active exploitation of TrueConf video conferencing vulnerabilities by pro-Ukrainian hacktivists, persistent malware on Cisco firewall devices, and widespread supply chain attacks targeting popular development platforms. The PhantomRPC vulnerability in Windows presents a particularly concerning threat as it remains unpatched and provides multiple exploit paths for privilege escalation. Additionally, threat actors are leveraging compromised PyPI packages, VS Code extensions, and Microsoft Teams to deploy sophisticated malware campaigns, while the Firestarter malware demonstrates advanced persistence capabilities by surviving security patches on Cisco firewall devices.

## Active Exploitation Details

### PhantomRPC Vulnerability
- **Description**: An architectural weakness in Windows' Remote Procedure Call (RPC) mechanism that handles connections to unavailable services
- **Impact**: Enables privilege escalation through five different exploit paths
- **Status**: Currently unpatched and actively exploitable

### TrueConf Video Conferencing Vulnerabilities
- **Description**: Multiple vulnerabilities in TrueConf video conferencing software servers
- **Impact**: Complete server compromise and network breach capabilities
- **Status**: Actively exploited by PhantomCore group since September 2025

### Cisco Firewall Device Compromise
- **Description**: Custom malware infection targeting Cisco Firepower and Secure Firewall devices running Adaptive Security Appliance (ASA)
- **Impact**: Persistent backdoor access that survives security updates and patches
- **Status**: Active infections confirmed at federal civilian agency

### PyPI Package Compromise
- **Description**: Malicious version of elementary-data package with 1.1 million monthly downloads
- **Impact**: Theft of sensitive developer data and cryptocurrency wallets
- **Status**: Malicious package successfully deployed to steal credentials

## Affected Systems and Products

- **Windows Systems**: All versions affected by PhantomRPC RPC mechanism vulnerability
- **TrueConf Video Conferencing**: Servers running TrueConf software in Russian networks
- **Cisco Firepower Devices**: Firepower and Secure Firewall devices running ASA software
- **PyPI Package Repository**: elementary-data package and dependent applications
- **Microsoft Teams**: Used as attack vector for Snow malware deployment
- **Visual Studio Code**: 73 malicious extensions on Open VSX repository delivering GlassWorm v2
- **SimpleHelp, Samsung MagicINFO 9 Server, D-Link DIR-823X**: Recently added to CISA KEV catalog
- **ADT Systems**: Home security infrastructure compromised affecting 5.5 million customers
- **Medtronic Networks**: Medical device company systems breached with 9 million records stolen
- **Checkmarx GitHub**: Repository data exposed following March 23 attack

## Attack Vectors and Techniques

- **RPC Exploitation**: Multiple privilege escalation paths through Windows RPC mechanism flaws
- **Supply Chain Attacks**: Compromised packages in PyPI and VS Code extension repositories
- **Social Engineering**: Microsoft Teams used to deploy Snow malware suite including browser extensions and backdoors
- **Persistent Backdoors**: Firestarter malware designed to survive firmware updates and security patches
- **Fake CAPTCHA Schemes**: International Revenue Share Fraud (IRSF) campaigns using fake verification prompts
- **Vishing Campaigns**: Voice-based social engineering attacks by BlackFile extortion group
- **Deepfake Voice Attacks**: Three-second audio samples used to clone voices for fraud

## Threat Actor Activities

- **PhantomCore**: Pro-Ukrainian hacktivist group actively targeting Russian TrueConf servers since September 2025
- **UNC6692**: Deploying Snow malware suite through Microsoft Teams social engineering campaigns
- **ShinyHunters**: Extortion group responsible for ADT breach affecting 5.5 million individuals and threatening data publication
- **GlassWorm Campaign**: Operators distributing 73 malicious VS Code extensions for information theft
- **BlackFile Group**: New extortion group conducting vishing attacks against retail and hospitality organizations since February 2026
- **Federal Agency Attackers**: Unknown threat actors deploying Firestarter backdoor on government Cisco devices
- **Elementary-data Attackers**: Compromised popular Python package to steal developer credentials and cryptocurrency wallets