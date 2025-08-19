# Exploitation Report

Current threat activity reveals several critical exploitation campaigns targeting diverse sectors. A sophisticated malware campaign is deploying GodRAT trojan against trading and brokerage firms using advanced steganography techniques and code derived from the Gh0st RAT family. Meanwhile, attackers are exploiting a two-year-old Apache ActiveMQ vulnerability through the DripDropper malware, which uniquely patches the exploited vulnerability after successful compromise to prevent other attackers from using the same entry point. Additional threats include XenoRAT campaigns targeting South Korean embassies through malicious GitHub repositories, and public exploits for chained SAP NetWeaver vulnerabilities enabling remote code execution. The threat landscape also includes the Noodlophile stealer using copyright complaint phishing lures and multiple significant data breaches affecting major organizations.

## Active Exploitation Details

### Apache ActiveMQ Vulnerability Exploitation
- **Description**: A widely abused vulnerability in Apache ActiveMQ that is approximately two years old is being actively exploited by the DripDropper malware campaign
- **Impact**: Attackers gain initial access to Linux systems and install malware, then patch the vulnerability to prevent other threat actors from exploiting the same flaw
- **Status**: Actively exploited in the wild; attackers are patching the vulnerability after exploitation

### SAP NetWeaver Chained Vulnerabilities
- **Description**: Two critical, now-patched security flaws in SAP NetWeaver are being exploited in combination through a publicly available exploit
- **Impact**: Remote code execution capabilities allowing system compromise and data theft
- **Status**: Public exploit available; vulnerabilities are patched but unpatched systems remain at risk

### GitHub Repository Abuse for XenoRAT Deployment
- **Description**: Malicious GitHub repositories are being used to host and distribute XenoRAT malware in targeted campaigns
- **Impact**: Remote access trojan deployment enabling persistent access and data exfiltration
- **Status**: Active campaign targeting diplomatic entities

## Affected Systems and Products

- **Apache ActiveMQ**: Linux systems running vulnerable versions of the message broker software
- **SAP NetWeaver**: Unpatched enterprise systems vulnerable to chained exploitation
- **Trading and Brokerage Firms**: Financial institutions targeted by GodRAT campaigns
- **Foreign Embassies in South Korea**: Diplomatic missions targeted by XenoRAT campaigns
- **Windows Systems**: Recovery and reset operations broken by August 2025 security updates
- **Allianz Life**: 1.1 million individuals affected by Salesforce data theft
- **Business Council of New York State**: 47,000 individuals impacted by network breach
- **Inotiv Pharmaceutical**: Systems encrypted in ransomware attack

## Attack Vectors and Techniques

- **Steganography**: GodRAT uses advanced steganographic techniques to hide malicious payloads
- **GitHub Repository Abuse**: Threat actors hosting malware on legitimate code repositories to evade detection
- **Copyright Complaint Phishing**: Noodlophile stealer using bogus copyright claims as spear-phishing lures
- **Vulnerability Patching Post-Exploitation**: DripDropper malware patches exploited vulnerabilities to maintain exclusive access
- **Chained Vulnerability Exploitation**: Combining multiple SAP NetWeaver flaws for enhanced attack capabilities
- **Ransomware Deployment**: Traditional encryption-based attacks affecting pharmaceutical operations

## Threat Actor Activities

- **State-Sponsored Groups**: Conducting espionage campaigns against South Korean embassies using XenoRAT malware
- **Financial Sector Attackers**: Targeting trading firms and brokerage companies with sophisticated GodRAT trojan campaigns
- **DripDropper Operators**: Exploiting Apache ActiveMQ vulnerabilities while implementing unique post-exploitation patching techniques
- **Enterprise-Focused Groups**: Leveraging public SAP NetWeaver exploits for system compromise and data theft
- **Ransomware Groups**: Continuing attacks against pharmaceutical and healthcare sectors
- **Data Theft Specialists**: Conducting large-scale breaches affecting insurance companies and business organizations