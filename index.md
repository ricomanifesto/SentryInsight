# Exploitation Report

Critical exploitation activity is currently dominated by several significant vulnerabilities across enterprise systems and open-source platforms. Most notably, Oracle PeopleSoft systems are under active attack through a zero-day vulnerability that the ShinyHunters extortion group has weaponized to breach university systems and steal sensitive data. Additionally, over 400 packages in the Arch Linux User Repository have been compromised to distribute malware, while a decade-old authentication bypass vulnerability in phpBB forum software has been discovered and patched. Chinese threat actors continue their sophisticated long-term operations, with one group maintaining persistence in authentication systems for nearly 10 years, and another exploiting Oracle zero-day vulnerabilities to target higher education institutions.

## Active Exploitation Details

### Oracle PeopleSoft Zero-Day Vulnerability
- **Description**: Critical vulnerability in Oracle PeopleSoft Suite allowing unauthenticated remote code execution
- **Impact**: Attackers can execute arbitrary code without authentication, leading to complete system compromise and data theft
- **Status**: Actively exploited by ShinyHunters group; Oracle has released mitigation measures
- **CVE ID**: CVE-2026-35273

### Ivanti Sentry Vulnerability
- **Description**: Critical security flaw in Ivanti Sentry platform under active exploitation
- **Impact**: Allows attackers to compromise affected systems and gain unauthorized access
- **Status**: Actively exploited in the wild; CISA has mandated federal agencies patch within three days

### phpBB Authentication Bypass
- **Description**: 10-year-old authentication bypass vulnerability in phpBB forum software
- **Impact**: Allows attackers to log in as any user, including administrators
- **Status**: Recently discovered and patched after lurking undetected for a decade

### Splunk Enterprise Critical Flaw
- **Description**: Critical security vulnerability in Splunk Enterprise enabling unauthenticated file operations
- **Impact**: Allows remote code execution and unauthorized file manipulation without authentication
- **Status**: Security updates released by Splunk

### LangGraph Vulnerability Chain
- **Description**: Three security flaws in LangGraph including a critical vulnerability chain
- **Impact**: Could result in remote code execution on self-hosted AI agents
- **Status**: All three vulnerabilities have been patched

## Affected Systems and Products

- **Oracle PeopleSoft Suite**: Enterprise resource planning software used extensively by universities and organizations
- **Ivanti Sentry**: Enterprise security platform used by federal agencies and organizations
- **phpBB Forum Software**: Open-source forum platform with widespread deployment
- **Splunk Enterprise**: Enterprise data analytics and monitoring platform
- **Arch Linux AUR**: Over 400 packages in the Arch User Repository compromised
- **LangGraph**: AI agent framework for self-hosted deployments
- **Linux Authentication Systems**: PAM modules and login systems targeted by Chinese actors

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: ShinyHunters leveraging unpatched Oracle PeopleSoft vulnerability for data theft campaigns
- **Supply Chain Compromise**: Mass hijacking of Arch Linux AUR packages to distribute rootkits and infostealers
- **Authentication Bypass**: Exploitation of decade-old phpBB vulnerability to gain administrative access
- **Long-Term Persistence**: Chinese actors maintaining access to authentication systems for nearly a decade
- **Unauthenticated Remote Code Execution**: Multiple vulnerabilities allowing code execution without credentials
- **Package Repository Poisoning**: Rewriting build scripts in compromised AUR packages to install malware
- **AI Agent Manipulation**: Agentjacking attacks tricking AI coding agents into executing malicious code

## Threat Actor Activities

- **ShinyHunters**: Actively exploiting Oracle PeopleSoft zero-day (CVE-2026-35273) to breach university systems and conduct data theft extortion campaigns targeting higher education sector
- **Chinese State-Sponsored Groups**: Conducting sophisticated long-term operations including decade-long persistence in authentication systems and backdooring Linux login software for extended covert access
- **AUR Package Hijackers**: Compromised over 400 Arch Linux packages to distribute credential stealers and eBPF rootkits, targeting developer machines
- **Conti Ransomware Operation**: Ukrainian national pleaded guilty to conspiracy charges related to the Conti ransomware group's activities
- **Chinese Smishing Network**: Using Google's Gemini AI to enhance phishing text message campaigns targeting American users
- **Sniper Dz PhaaS Operators**: Decade-long phishing-as-a-service platform disrupted by INTERPOL Operation Ramz with administrator arrested