# Exploitation Report

The cybersecurity landscape is currently experiencing significant exploitation activity across multiple platforms and systems. Most critically, CISA has flagged a VMware Aria Operations vulnerability as actively exploited, prompting its addition to the Known Exploited Vulnerabilities catalog. Simultaneously, threat actors are leveraging a Qualcomm zero-day vulnerability in targeted Android attacks, with Google confirming active exploitation of this high-severity memory corruption flaw. Additional attack vectors include the abuse of OAuth redirection mechanisms to bypass security protections and the deployment of AI-powered attack tools against infrastructure across multiple countries.

## Active Exploitation Details

### VMware Aria Operations Remote Code Execution Vulnerability
- **Description**: A remote code execution vulnerability in Broadcom VMware Aria Operations that allows attackers to execute arbitrary code on affected systems
- **Impact**: Attackers can gain unauthorized access to VMware Aria Operations systems and potentially execute malicious code remotely
- **Status**: Actively exploited in the wild and added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2026-22719

### Qualcomm Android Component Memory Corruption Vulnerability
- **Description**: A high-severity memory corruption vulnerability affecting an open-source Qualcomm display component used in Android devices
- **Impact**: Memory corruption exploitation that could lead to system compromise and potential spyware deployment
- **Status**: Actively exploited in targeted attacks, patches released by Google
- **CVE ID**: CVE-2026-21385

## Affected Systems and Products

- **VMware Aria Operations**: Broadcom VMware Aria Operations installations vulnerable to remote code execution
- **Android Devices**: Devices using Qualcomm display components affected by memory corruption vulnerability
- **Fortinet FortiGate**: Appliances targeted in AI-driven attacks across 55 countries
- **OAuth-enabled Applications**: Systems using OAuth authentication mechanisms susceptible to redirection abuse
- **cPanel Systems**: Compromised website management panels being sold in cybercrime markets

## Attack Vectors and Techniques

- **OAuth Redirection Abuse**: Attackers exploit legitimate OAuth redirection mechanisms to bypass phishing protections in email and browsers
- **AI-Powered Attacks**: Deployment of CyberStrikeAI platform for automated security testing and exploitation against FortiGate appliances
- **Phishing with MFA Bypass**: Starkiller phishing suite uses adversary-in-the-middle (AitM) reverse proxy techniques to bypass multi-factor authentication
- **Fake Tech Support Campaigns**: Customized Havoc C2 framework deployment through fraudulent IT support communications
- **Memory Corruption Exploitation**: Targeted exploitation of Qualcomm component vulnerabilities in Android devices

## Threat Actor Activities

- **SloppyLemming**: Conducting attacks against government entities and critical infrastructure in Pakistan and Bangladesh using dual malware chains
- **Commercial Spyware Operators**: Potentially involved in the exploitation of the Qualcomm Android zero-day vulnerability
- **Nation-State Groups**: Suspected involvement in targeted Android device compromise campaigns
- **Pro-Iranian Actors**: Launching coordinated cyberattacks in retaliation for US-Israeli military actions
- **African Cybercrime Syndicate**: International law enforcement operation resulted in 574 arrests and recovery of over $3 million
- **The Com Collective**: 30 alleged members arrested in Project Compass operation, with nearly 180 total members identified