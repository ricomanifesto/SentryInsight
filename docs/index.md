# Exploitation Report

Current threat activity demonstrates a concerning mix of actively exploited zero-day vulnerabilities and sophisticated supply chain attacks targeting critical infrastructure and development platforms. Most notably, Microsoft has confirmed active exploitation of CVE-2026-32202, a Windows Shell vulnerability that enables privilege escalation attacks. Meanwhile, threat actors are leveraging unpatched flaws in robotics platforms, conducting large-scale malware campaigns through development repositories, and executing complex social engineering operations across cloud platforms. The emergence of AI-powered vulnerability discovery tools is accelerating the threat landscape, creating new challenges for defensive teams attempting to maintain security postures against increasingly automated exploitation techniques.

## Active Exploitation Details

### Windows Shell Vulnerability
- **Description**: High-severity security flaw impacting Windows Shell that has been revised by Microsoft to acknowledge active exploitation
- **Impact**: Enables privilege escalation attacks on Windows systems
- **Status**: Patched by Microsoft, but confirmed to be actively exploited in the wild
- **CVE ID**: CVE-2026-32202

### Hugging Face LeRobot Remote Code Execution
- **Description**: Critical unpatched security flaw in LeRobot, Hugging Face's open-source robotics platform with nearly 24,000 GitHub stars
- **Impact**: Allows unauthenticated remote code execution on affected robotics systems
- **Status**: Currently unpatched and vulnerable to exploitation
- **CVE ID**: CVE-2026-25874

### TrueConf Video Conferencing Vulnerabilities
- **Description**: Multiple vulnerabilities in TrueConf video conferencing software being actively exploited by the PhantomCore hacktivist group
- **Impact**: Enables unauthorized access and compromise of Russian network infrastructure
- **Status**: Under active exploitation since September 2025

### PhantomRPC Windows Privilege Escalation
- **Description**: Architectural weakness in Windows' Remote Procedure Call (RPC) mechanism that handles connections to unavailable services
- **Impact**: Enables privilege escalation through five different discovered exploit paths
- **Status**: Currently unpatched and exploitable

### Microsoft Entra ID Service Principal Takeover
- **Description**: Administrative role flaw within Microsoft Entra ID designed for AI agents that enables identity compromise
- **Impact**: Allows privilege escalation and service principal takeover attacks
- **Status**: Recently patched by Microsoft

## Affected Systems and Products

- **Hugging Face LeRobot**: Open-source robotics platform with critical unpatched RCE vulnerability
- **Windows Shell**: Systems running affected Windows versions vulnerable to privilege escalation
- **TrueConf Video Conferencing**: Servers running TrueConf software, particularly in Russian networks
- **Microsoft Entra ID**: Identity management systems with AI agent administrative roles
- **PyPI elementary-data Package**: Popular Python package with 1.1 million monthly downloads compromised with infostealer
- **OpenVSX Repository**: 73 malicious VS Code extensions delivering GlassWorm v2 malware
- **Robinhood Trading Platform**: Account creation process vulnerable to phishing injection attacks
- **ADT Security Systems**: Home security infrastructure compromised affecting 5.5 million customers
- **Medtronic Medical Devices**: Corporate IT systems breached with 9 million records potentially compromised

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Malicious packages injected into PyPI and OpenVSX repositories targeting developers
- **Fake CAPTCHA Schemes**: IRSF scam operations using fraudulent verification systems to generate SMS fraud
- **Social Engineering via Microsoft Teams**: UNC6692 threat actor combining Teams messaging with AWS S3 bucket abuse
- **SMS Blaster Devices**: Physical cellular tower impersonation devices for mass phishing distribution
- **Deepfake Voice Attacks**: Audio cloning technology requiring only three seconds of voice samples for fraud
- **Sleeper Extensions**: Malicious VS Code extensions that remain dormant until activated through updates
- **Email Injection**: Exploitation of account creation flows to inject phishing content into legitimate communications

## Threat Actor Activities

- **PhantomCore**: Pro-Ukrainian hacktivist group actively targeting Russian TrueConf servers since September 2025
- **Silk Typhoon**: Chinese state-sponsored group member extradited to US for COVID research facility cyberattacks
- **UNC6692**: Newly discovered threat actor combining Microsoft Teams social engineering with cloud infrastructure abuse and custom "Snow" malware
- **ShinyHunters**: Extortion group responsible for ADT breach affecting 5.5 million individuals
- **GlassWorm Campaign Operators**: Threat actors behind 73 malicious VS Code extensions in persistent information-stealing operations
- **Fast16 Framework Operators**: Historical malware framework predating Stuxnet by five years, rewriting cyber sabotage timeline