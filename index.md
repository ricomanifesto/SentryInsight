# Exploitation Report

The cybersecurity landscape is currently experiencing significant exploitation activity across multiple fronts, with threat actors leveraging zero-day vulnerabilities and sophisticated attack vectors to compromise critical systems. Most notably, the ShinyHunters extortion crew has been exploiting a critical Oracle PeopleSoft zero-day vulnerability to breach university systems and steal sensitive data. Additionally, Chinese-linked threat actors have demonstrated remarkable persistence by maintaining unauthorized access to authentication systems for nearly a decade, while supply chain attacks have compromised over 400 Arch Linux packages. Critical vulnerabilities in enterprise software like Splunk Enterprise and phpBB forum software have also emerged, with some flaws having existed undetected for extended periods.

## Active Exploitation Details

### Oracle PeopleSoft Zero-Day Vulnerability
- **Description**: A critical vulnerability in Oracle PeopleSoft Suite that allows unauthenticated remote code execution
- **Impact**: Attackers can break into enterprise systems, steal sensitive data, and conduct extortion campaigns. The vulnerability has disproportionately affected American universities
- **Status**: Actively exploited by ShinyHunters extortion crew. Oracle has issued mitigations for the vulnerability
- **CVE ID**: CVE-2026-35273

### Splunk Enterprise Critical Vulnerability
- **Description**: A critical security flaw in Splunk Enterprise that enables unauthenticated file operations and remote code execution
- **Impact**: Attackers can execute arbitrary code on affected systems without requiring authentication credentials
- **Status**: Splunk has released security updates to address the vulnerability

### phpBB Authentication Bypass Vulnerability
- **Description**: A 10-year-old authentication bypass vulnerability in phpBB forum software that allows attackers to log in as any user
- **Impact**: Complete compromise of forum systems, including administrative access and potential data theft
- **Status**: Recently discovered and patched after lurking undetected for a decade

### Ivanti Sentry Vulnerability
- **Description**: A security flaw in Ivanti Sentry that is being actively exploited in attacks
- **Impact**: Successful exploitation can lead to system compromise and unauthorized access
- **Status**: CISA has ordered federal agencies to patch within three days due to active exploitation

## Affected Systems and Products

- **Oracle PeopleSoft Suite**: ERP software widely used in enterprise environments, particularly vulnerable in university settings
- **Splunk Enterprise**: Data analytics and monitoring platform used across various industries
- **phpBB Forum Software**: Open-source forum platform with authentication systems compromised
- **Arch Linux AUR Packages**: Over 400 packages in the Arch User Repository containing malicious code
- **Ivanti Sentry**: Enterprise security management platform
- **LangGraph**: AI agent framework with self-hosted deployments vulnerable to remote code execution
- **Linux Login Systems**: Authentication mechanisms backdoored by Chinese-linked actors

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: ShinyHunters leveraging unpatched Oracle vulnerabilities for data theft and extortion
- **Supply Chain Compromise**: Mass hijacking of over 400 Arch Linux packages to deploy infostealers and rootkits
- **Authentication Stack Hijacking**: Chinese actors maintaining persistent access through compromised login systems
- **eBPF Rootkit Deployment**: Advanced Linux rootkits using eBPF technology for stealth persistence
- **Agentjacking Attacks**: Novel attack method targeting AI coding agents to execute malicious code
- **Phishing-as-a-Service**: Sniper Dz platform providing phishing infrastructure for cybercriminals

## Threat Actor Activities

- **ShinyHunters**: Actively exploiting Oracle PeopleSoft zero-day to breach universities and conduct data theft extortion campaigns
- **Chinese-Linked APT Groups**: Maintained decade-long persistence in authentication systems, demonstrating advanced operational security and long-term strategic objectives
- **Conti Ransomware Operation**: Continued legal proceedings with Ukrainian national pleading guilty to conspiracy charges
- **Chinese Cybercrime Network**: Google pursuing legal action against network using Gemini AI for sophisticated phishing campaigns targeting American users
- **AudiA6 Operators**: Cryptocurrency laundering service disrupted by Europol, previously used by ransomware gangs and cybercriminal networks