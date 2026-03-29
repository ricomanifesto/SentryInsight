# Exploitation Report

Critical vulnerabilities across multiple platforms are experiencing active exploitation, highlighting a diverse threat landscape targeting enterprise infrastructure, AI platforms, mobile devices, and supply chain components. CISA has added multiple vulnerabilities to its Known Exploited Vulnerabilities catalog, including F5 BIG-IP APM systems and a newly disclosed Langflow AI platform vulnerability. Meanwhile, nation-state actors are leveraging sophisticated exploit kits including DarkSword for iOS targeting and BPFDoor implants for telecom espionage. Supply chain attacks continue to proliferate through compromised Python packages and VS Code extensions, while targeted campaigns exploit web-based vulnerabilities in mobile devices and enterprise networking equipment.

## Active Exploitation Details

### F5 BIG-IP Access Policy Manager Vulnerability
- **Description**: Critical security flaw affecting F5 BIG-IP Access Policy Manager (APM) systems that allows unauthorized access
- **Impact**: Attackers can gain unauthorized access to APM systems, potentially compromising network security controls
- **Status**: Under active exploitation in the wild, patches available, added to CISA KEV catalog
- **CVE ID**: CVE-2025-53521

### Citrix NetScaler Memory Overread Vulnerability
- **Description**: Critical memory overread bug affecting Citrix NetScaler ADC and NetScaler Gateway with a CVSS score of 9.3
- **Impact**: Memory disclosure that could lead to sensitive information exposure and potential system compromise
- **Status**: Under active reconnaissance activity, recently disclosed with high severity rating
- **CVE ID**: CVE-2026-3055

### Langflow AI Platform Code Injection
- **Description**: Critical vulnerability in the Langflow AI framework allowing code injection attacks
- **Impact**: Attackers can hijack AI workflows and potentially execute arbitrary code within the platform
- **Status**: Actively exploited within hours of disclosure, added to CISA KEV catalog
- **CVE ID**: CVE-2026-33017

### iOS Web-Based Exploits
- **Description**: Multiple web-based vulnerabilities targeting older versions of iOS and iPadOS devices
- **Impact**: Remote code execution and device compromise through malicious websites
- **Status**: Actively exploited, prompting Apple to send lock screen notifications to affected devices

### Open VSX Security Bypass
- **Description**: Bug in Open VSX's pre-publish scanning pipeline that allowed malicious VS Code extensions to bypass security checks
- **Impact**: Deployment of malicious VS Code extensions that could compromise developer environments
- **Status**: Previously exploited, now patched

### LangChain and LangGraph Framework Vulnerabilities
- **Description**: Three security vulnerabilities affecting widely used AI frameworks LangChain and LangGraph
- **Impact**: Exposure of filesystem data, environment secrets, and potential database compromise
- **Status**: Disclosed vulnerabilities with potential for active exploitation

## Affected Systems and Products

- **F5 BIG-IP APM**: Access Policy Manager systems across enterprise networks
- **Citrix NetScaler**: ADC and Gateway appliances in enterprise environments
- **Langflow Framework**: AI workflow management platforms and applications
- **iOS/iPadOS Devices**: Older versions of Apple mobile operating systems
- **macOS Systems**: Targeted by Infinity Stealer malware through ClickFix campaigns
- **Python Development Environment**: PyPI packages including Telnyx, Trivy, KICS, and litellm
- **VS Code Extensions**: Open VSX registry and Microsoft Visual Studio Code environments
- **Telecom Infrastructure**: Network equipment and systems targeted by BPFDoor implants
- **TikTok for Business**: Business account management platforms
- **Ajax Football Club Systems**: IT infrastructure managing fan data and ticketing

## Attack Vectors and Techniques

- **Memory Exploitation**: CVE-2026-3055 leverages memory overread vulnerabilities for information disclosure
- **Supply Chain Poisoning**: Malicious Python packages deployed to PyPI with credential-stealing capabilities hidden in WAV audio files
- **Adversary-in-the-Middle Phishing**: TikTok Business accounts targeted using AitM techniques with Cloudflare Turnstile evasion
- **ClickFix Social Engineering**: Infinity Stealer malware distributed through fake software update prompts on macOS
- **Spear-Phishing with Exploit Kits**: TA446 deploying DarkSword iOS exploit kit through targeted email campaigns
- **Fake Security Alerts**: Malicious campaigns using fake VS Code security alerts on GitHub to distribute malware
- **Steganography**: Malware hidden within WAV audio files to evade detection
- **BPF-based Persistence**: BPFDoor implants using Berkeley Packet Filter for stealthy network-level persistence

## Threat Actor Activities

- **Iran-Linked Groups**: Successfully breached FBI Director's personal email account and deployed wiper attacks against Stryker
- **TA446 (Russian-Linked)**: Conducting targeted spear-phishing campaigns using DarkSword iOS exploit kit against specific victims
- **TeamPCP**: Supply chain attacks targeting Python packages, compromising Telnyx after previous attacks on Trivy, KICS, and litellm
- **Red Menshen (China-Linked)**: Long-term espionage campaign using upgraded BPFDoor malware to spy on telecom networks globally
- **Bearlyfy (Pro-Ukrainian)**: Conducting ransomware attacks against Russian companies using custom GenieLocker ransomware, with over 70 attacks since January 2025
- **Infinity Stealer Operators**: Targeting macOS users through sophisticated ClickFix lures and Python-based payloads