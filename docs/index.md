# Exploitation Report

Several critical vulnerabilities are currently under active exploitation, with threat actors leveraging zero-day flaws, enterprise infrastructure weaknesses, and sophisticated attack techniques to compromise systems worldwide. The most significant activity involves CVE-2026-21385, a high-severity Qualcomm zero-day being exploited in targeted Android attacks potentially linked to commercial spyware or nation-state groups. Additionally, CVE-2026-22719, a VMware Aria Operations RCE vulnerability, has been flagged by CISA as actively exploited. Threat actors are also deploying AI-powered attack tools, abusing OAuth mechanisms, and conducting large-scale phishing campaigns targeting government entities and critical infrastructure across multiple countries.

## Active Exploitation Details

### Qualcomm Android Component Zero-Day
- **Description**: High-severity memory corruption vulnerability affecting an open-source Qualcomm component used in Android devices
- **Impact**: Enables targeted exploitation of Android devices, potentially allowing attackers to gain unauthorized access and execute malicious code
- **Status**: Actively exploited in the wild, patches released by Google in Android security updates
- **CVE ID**: CVE-2026-21385

### VMware Aria Operations RCE Vulnerability
- **Description**: Remote code execution vulnerability in VMware Aria Operations platform
- **Impact**: Allows attackers to execute arbitrary code remotely on affected systems
- **Status**: Actively exploited in attacks, added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2026-22719

### AI-Powered FortiGate Attacks
- **Description**: Campaign leveraging CyberStrikeAI platform to conduct AI-assisted attacks against Fortinet FortiGate appliances
- **Impact**: Compromise of network security infrastructure across 55 countries
- **Status**: Ongoing campaign using open-source AI security testing tools for malicious purposes

## Affected Systems and Products

- **Android Devices**: Devices containing Qualcomm components vulnerable to memory corruption attacks
- **VMware Aria Operations**: Enterprise virtualization management platform subject to RCE exploitation
- **Fortinet FortiGate**: Network security appliances targeted by AI-powered attack campaigns across 55 countries
- **Government Systems**: Pakistan and Bangladesh government entities and critical infrastructure targeted by SloppyLemming
- **Enterprise OAuth Systems**: Organizations using OAuth authentication mechanisms vulnerable to redirect abuse
- **Tire Pressure Monitoring Systems**: Vehicle sensors enabling silent tracking capabilities

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Memory corruption vulnerabilities in mobile device components
- **OAuth Redirect Abuse**: Manipulation of legitimate OAuth redirection mechanisms to bypass email and browser phishing protections
- **AI-Assisted Attacks**: Use of CyberStrikeAI platform for automated vulnerability discovery and exploitation
- **Phishing-as-a-Service**: Starkiller suite employing adversary-in-the-middle (AitM) reverse proxy techniques to bypass multi-factor authentication
- **Progressive Web App (PWA) Phishing**: Fake Google Security sites deploying PWA applications to steal credentials and MFA codes
- **Fake Tech Support**: Campaigns masquerading as IT support to deploy Havoc command-and-control frameworks
- **Compromised Site Management**: Bulk sale of cPanel credentials in underground markets for phishing infrastructure

## Threat Actor Activities

- **SloppyLemming**: Targeting government entities and critical infrastructure in Pakistan and Bangladesh using dual malware chains
- **Commercial Spyware/Nation-State Groups**: Suspected exploitation of Qualcomm Android zero-day for targeted surveillance operations
- **Cybercriminal Syndicates**: African cybercrime operations disrupted by law enforcement, resulting in 574 arrests and recovery of over $3 million
- **The Com Collective**: Global law enforcement operation Project Compass resulted in arrest of 30 alleged members of this notorious cybercriminal group
- **Pro-Iranian Actors**: Launching coordinated cyberattacks as retaliation for US-Israeli military actions, targeting economic and physical infrastructure