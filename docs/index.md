# Exploitation Report

Current threat landscape shows critical exploitation activity across multiple platforms, with Chinese threat actors conducting decade-long persistence campaigns and the ShinyHunters group actively exploiting a zero-day vulnerability in Oracle PeopleSoft systems. Major incidents include over 400 compromised Arch Linux packages deploying rootkits and infostealers, a critical Splunk Enterprise vulnerability enabling unauthenticated remote code execution, and sophisticated authentication bypass attacks targeting enterprise infrastructure. The most concerning activity involves CVE-2026-35273, a PeopleSoft zero-day being actively exploited to breach university systems and steal sensitive data.

## Active Exploitation Details

### Oracle PeopleSoft Zero-Day Vulnerability
- **Description**: Critical vulnerability in Oracle PeopleSoft Suite allowing unauthenticated remote code execution
- **Impact**: Complete system compromise, data theft, and unauthorized access to enterprise systems
- **Status**: Actively exploited by ShinyHunters group, Oracle has released mitigations
- **CVE ID**: CVE-2026-35273

### Splunk Enterprise Critical Vulnerability
- **Description**: Critical security flaw enabling unauthenticated file operations and remote code execution
- **Impact**: Full system compromise without authentication requirements
- **Status**: Security updates released by Splunk

### phpBB Authentication Bypass
- **Description**: 10-year-old authentication bypass vulnerability in phpBB forum software
- **Impact**: Allows attackers to log in as any user, including administrators
- **Status**: Recently patched after decade-long exposure

### Ivanti Sentry Vulnerability
- **Description**: Actively exploited vulnerability in Ivanti Sentry systems
- **Impact**: System compromise and unauthorized access
- **Status**: CISA has mandated federal agencies patch within three days

### Arch Linux Package Compromise
- **Description**: Mass compromise of over 400 packages in Arch User Repository (AUR)
- **Impact**: Installation of credential stealers and eBPF rootkits on victim systems
- **Status**: Ongoing investigation and cleanup efforts

### LangGraph Vulnerability Chain
- **Description**: Critical vulnerability chain in LangGraph affecting self-hosted AI agents
- **Impact**: Remote code execution on AI agent systems
- **Status**: Three vulnerabilities patched

## Affected Systems and Products

- **Oracle PeopleSoft Suite**: Enterprise resource planning systems, particularly affecting American universities
- **Splunk Enterprise**: Log analysis and security information management platforms
- **phpBB Forum Software**: Web forum applications with 10+ year installations
- **Ivanti Sentry**: Enterprise security and management solutions
- **Arch Linux AUR**: Over 400 packages in user repository compromised
- **LangGraph**: Self-hosted AI agent frameworks
- **Linux Authentication Systems**: PAM and login subsystems targeted by Chinese actors
- **Tchap Messenger**: French government encrypted messaging platform affecting 73,000+ accounts

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active use of unpatched vulnerabilities for initial access
- **Supply Chain Attacks**: Package repository compromise to distribute malware
- **Authentication Stack Hijacking**: Long-term persistence through authentication system backdoors
- **Credential Harvesting**: Deployment of infostealers targeting access tokens and passwords
- **AI Agent Manipulation**: Agentjacking attacks tricking AI coding agents into executing malicious code
- **Phishing-as-a-Service**: Professional phishing platforms providing turnkey attack capabilities
- **eBPF Rootkit Deployment**: Advanced kernel-level persistence mechanisms

## Threat Actor Activities

- **ShinyHunters Group**: Actively exploiting CVE-2026-35273 in Oracle PeopleSoft to breach university systems and conduct data theft extortion campaigns
- **Chinese APT Groups**: Conducting decade-long persistence campaigns through authentication system backdoors and Linux login software manipulation
- **Conti Ransomware Operation**: Continued legal proceedings against Ukrainian national involved in ransomware operations
- **Chinese Smishing Networks**: Using AI tools like Google Gemini to enhance phishing campaigns targeting American consumers
- **AudiA6 Cryptocurrency Laundering Service**: Disrupted by Europol after facilitating ransomware gang money laundering operations
- **Sniper Dz PhaaS Platform**: Decade-long phishing-as-a-service operation disrupted by INTERPOL Operation Ramz