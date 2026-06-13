# Exploitation Report

Current exploitation activity reveals several critical zero-day vulnerabilities being actively exploited in the wild, with threat actors targeting enterprise systems, Linux distributions, and AI platforms. The most significant concerns include the ShinyHunters group exploiting an Oracle PeopleSoft zero-day (CVE-2026-35273) to breach multiple universities, and a maximum-severity Ivanti Sentry vulnerability (CVE-2026-35273) that was exploited within 24 hours of public disclosure. Additionally, over 400 Arch Linux packages have been compromised to distribute rootkits and infostealers, while new attack techniques targeting AI coding agents and BitLocker encryption present emerging threats to enterprise security.

## Active Exploitation Details

### Oracle PeopleSoft Zero-Day
- **Description**: Critical vulnerability in Oracle PeopleSoft Suite allowing unauthenticated remote code execution
- **Impact**: Enables attackers to break into enterprise systems, steal sensitive data, and conduct extortion campaigns
- **Status**: Zero-day actively exploited by ShinyHunters group; Oracle has released mitigation measures
- **CVE ID**: CVE-2026-35273

### Ivanti Sentry Maximum-Severity Flaw
- **Description**: Critical vulnerability in Ivanti Sentry security platform
- **Impact**: Allows attackers to gain unauthorized access to enterprise security infrastructure
- **Status**: Actively exploited within 24 hours of disclosure; CISA has ordered federal agencies to patch within three days
- **CVE ID**: CVE-2026-35273

### phpBB Authentication Bypass
- **Description**: 10-year-old authentication bypass vulnerability in phpBB forum software
- **Impact**: Allows attackers to log in as any user, including administrators
- **Status**: Recently fixed after a decade of exposure

### Linux Login System Backdoor
- **Description**: China-linked threat actors have maintained persistent backdoors in Linux login systems for nearly a decade
- **Impact**: Enables long-term covert access to Linux servers and systems
- **Status**: Recently discovered and disclosed by security researchers

## Affected Systems and Products

- **Oracle PeopleSoft Suite**: Enterprise resource planning software, particularly affecting American universities
- **Ivanti Sentry**: Security platform used by government agencies and enterprises
- **Arch Linux AUR**: Over 400 packages in the Arch User Repository compromised
- **phpBB Forum Software**: Popular forum platform with 10-year-old vulnerability
- **Linux Login Systems**: Various Linux distributions affected by long-term backdoor campaigns
- **LangGraph AI Framework**: Self-hosted AI agents vulnerable to remote code execution
- **OpenClaw AI Agent**: Popular self-hosted AI platform susceptible to code execution and data leakage
- **Windows BitLocker**: Microsoft's disk encryption system targeted by GreatXML bypass technique

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Attackers rapidly exploiting newly disclosed vulnerabilities within hours
- **Supply Chain Compromise**: Mass compromise of software repositories to distribute malware
- **eBPF Rootkit Deployment**: Advanced rootkits using extended Berkeley Packet Filter technology for persistence
- **AI Agent Manipulation**: "Agentjacking" attacks that trick AI coding agents into executing malicious code
- **BitLocker Recovery Bypass**: GreatXML exploit using XML files in recovery partitions to bypass encryption
- **Phishing-as-a-Service**: Decade-long platforms providing turnkey phishing infrastructure
- **Credential Theft**: Widespread deployment of infostealers targeting authentication tokens and access credentials

## Threat Actor Activities

- **ShinyHunters Group**: Actively exploiting Oracle PeopleSoft zero-day to target universities for data theft and extortion
- **China-Linked Groups**: Operating long-term campaigns with backdoors in Linux login systems, tracked as Velvet Ant by security researchers
- **AUR Package Hijackers**: Compromised over 400 Arch Linux packages to deploy infostealers and eBPF rootkits
- **Sniper Dz Operators**: Decade-long phishing-as-a-service platform disrupted by INTERPOL Operation Ramz
- **Chinese Smishing Network**: Using Google's Gemini AI to enhance phishing text message campaigns
- **Conti Ransomware Associates**: Ukrainian national pleading guilty to conspiracy charges in major ransomware operation
- **AudiA6 Cryptocurrency Launderers**: Service used by ransomware gangs for money laundering, recently disrupted by Europol