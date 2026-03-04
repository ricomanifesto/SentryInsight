# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms and systems across various attack vectors. The most significant threats include active exploitation of a VMware Aria Operations remote code execution vulnerability (CVE-2026-22719) that has been added to CISA's Known Exploited Vulnerabilities catalog, indicating widespread in-the-wild attacks. Additionally, a powerful iOS exploit kit called Coruna has been identified targeting Apple devices with 23 different exploits across five exploitation chains, affecting iOS versions 13.0 through 17.2.1. A Qualcomm zero-day vulnerability (CVE-2026-21385) is also being actively exploited in targeted Android attacks, potentially linked to commercial spyware or nation-state operations. These developments represent a significant escalation in mobile and enterprise infrastructure targeting.

## Active Exploitation Details

### VMware Aria Operations Remote Code Execution Vulnerability
- **Description**: A security flaw in Broadcom VMware Aria Operations that allows remote code execution
- **Impact**: Attackers can execute arbitrary code remotely on affected systems
- **Status**: Actively exploited in the wild, added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2026-22719

### Coruna iOS Exploit Kit
- **Description**: A new and powerful exploit kit targeting Apple iPhone models with 23 exploits across five exploitation chains
- **Impact**: Complete compromise of iOS devices, allowing attackers full system access
- **Status**: Active exploitation targeting iOS versions 13.0 through 17.2.1
- **CVE ID**: Not specified in source articles

### Qualcomm Zero-Day Android Vulnerability
- **Description**: A high-severity memory corruption flaw in Qualcomm components used in targeted Android attacks
- **Impact**: Device compromise potentially enabling surveillance capabilities
- **Status**: Actively exploited, potentially tied to commercial spyware or nation-state threat groups
- **CVE ID**: CVE-2026-21385

## Affected Systems and Products

- **VMware Aria Operations**: Broadcom VMware Aria Operations systems vulnerable to remote code execution
- **Apple iOS Devices**: iPhone models running iOS versions 13.0 through 17.2.1 targeted by Coruna exploit kit
- **Android Devices**: Devices with Qualcomm components affected by memory corruption vulnerability
- **Fortinet FortiGate**: Network security appliances targeted in AI-driven attacks across 55 countries
- **Enterprise OAuth Systems**: Organizations using OAuth authentication mechanisms targeted for credential theft

## Attack Vectors and Techniques

- **RDP Brute Force**: Credential-based attacks targeting Remote Desktop Protocol services leading to ransomware infrastructure exposure
- **OAuth Redirect Abuse**: Legitimate OAuth redirection mechanisms abused to bypass phishing protections in email and browsers
- **AI-Assisted Attacks**: CyberStrikeAI platform deployed in automated attacks against FortiGate appliances
- **Phishing-as-a-Service**: Starkiller phishing suite using adversary-in-the-middle reverse proxy to bypass multi-factor authentication
- **Supply Chain Compromise**: Fake Laravel packages on Packagist deploying cross-platform remote access trojans
- **Fake Tech Support**: Social engineering campaigns deploying customized Havoc C2 framework for data exfiltration

## Threat Actor Activities

- **Silver Dragon (APT41-linked)**: Targeting government entities in Europe and Southeast Asia using Cobalt Strike and Google Drive for command and control
- **Sloppy Lemming**: India-nexus threat actors targeting defense and critical infrastructure with custom Rust-coded tools and cloud-based C2
- **Pro-Iranian Actors**: Launching cyberattacks in retaliation for US-Israeli military action, aimed at economic and physical disruption
- **Commercial Spyware Operations**: Exploitation of Qualcomm zero-day potentially linked to commercial surveillance tools
- **Cybercrime Syndicates**: African cybercrime ring disrupted by law enforcement with 574 arrests and $3 million recovered
- **Underground Markets**: Mass distribution of compromised cPanel credentials for phishing and scam infrastructure deployment