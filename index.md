# Exploitation Report

Critical exploitation activity is currently dominated by several high-impact vulnerabilities and sophisticated attack campaigns. CISA has flagged CVE-2026-22719, a VMware Aria Operations remote code execution flaw, as actively exploited in the wild. Meanwhile, Google has identified the Coruna iOS exploit kit targeting Apple devices with 23 exploits across five chains, affecting iOS versions 13.0 to 17.2.1. Additionally, a Qualcomm zero-day vulnerability CVE-2026-21385 is being exploited in targeted Android attacks, potentially linked to commercial spyware or nation-state operations. Several APT groups are conducting active campaigns, including China's Silver Dragon group targeting government entities and the emergence of India-nexus Sloppy Lemming targeting defense and critical infrastructure.

## Active Exploitation Details

### VMware Aria Operations Remote Code Execution
- **Description**: A critical security flaw in Broadcom VMware Aria Operations that allows remote code execution
- **Impact**: Attackers can execute arbitrary code remotely on affected systems
- **Status**: Actively exploited in the wild, CISA has added to Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2026-22719

### Coruna iOS Exploit Kit
- **Description**: A powerful exploit kit featuring five full exploit chains with 23 individual exploits targeting Apple iPhone devices
- **Impact**: Complete device compromise across multiple iOS versions from 13.0 to 17.2.1
- **Status**: Active exploitation identified by Google researchers, affects a wide range of iOS versions

### Qualcomm Zero-Day Memory Corruption
- **Description**: A high-severity memory corruption flaw in Qualcomm components affecting Android devices
- **Impact**: Targeted attacks potentially linked to commercial spyware or nation-state threat groups
- **Status**: Actively exploited in targeted campaigns
- **CVE ID**: CVE-2026-21385

### AI-Driven FortiGate Attacks
- **Description**: AI-assisted campaign targeting Fortinet FortiGate appliances using CyberStrikeAI platform
- **Impact**: Compromise of network security appliances across 55 countries
- **Status**: Active campaign leveraging open-source AI security testing tools for malicious purposes

## Affected Systems and Products

- **VMware Aria Operations**: Broadcom VMware Aria Operations platforms vulnerable to remote code execution
- **iOS Devices**: Apple iPhone models running iOS versions 13.0 through 17.2.1
- **Android Devices**: Devices with Qualcomm components affected by memory corruption vulnerability
- **FortiGate Appliances**: Fortinet FortiGate network security devices targeted in AI-driven attacks across 55 countries
- **Healthcare Systems**: University of Mississippi Medical Center affected by ransomware attack
- **Laravel Applications**: PHP applications using malicious Packagist packages disguised as Laravel utilities

## Attack Vectors and Techniques

- **Remote Code Execution**: VMware Aria Operations vulnerability allows direct system compromise
- **Mobile Exploit Chains**: Coruna kit uses sophisticated multi-stage exploitation for iOS devices
- **Memory Corruption Exploitation**: Qualcomm zero-day leveraged for targeted Android attacks
- **AI-Assisted Attacks**: CyberStrikeAI platform used to enhance FortiGate exploitation campaigns
- **RDP Brute Force**: Credential attacks leading to ransomware infrastructure discovery
- **OAuth Abuse**: Legitimate OAuth redirection mechanisms bypassed for malware delivery
- **Phishing-as-a-Service**: Tycoon2FA platform disrupted after facilitating millions of phishing messages
- **Supply Chain Attacks**: Malicious packages distributed through Packagist PHP repository
- **Fake Tech Support**: Social engineering campaigns deploying customized Havoc C2 framework

## Threat Actor Activities

- **Silver Dragon (APT41-linked)**: Targeting government entities in Europe and Southeast Asia using Cobalt Strike and Google Drive for command and control
- **Sloppy Lemming (India-nexus)**: Targeting defense and critical infrastructure with custom Rust-coded tools and cloud-based C2
- **Pro-Iranian Groups**: Conducting retaliatory cyberattacks including 149 DDoS attacks against 110 organizations across 16 countries
- **Hacktivist Groups**: Surge in activity following Middle East conflict, conducting widespread DDoS campaigns
- **Ransomware Operators**: Active campaigns against healthcare sector, including University of Mississippi Medical Center
- **Commercial Spyware Groups**: Potentially exploiting Qualcomm zero-day for targeted surveillance operations