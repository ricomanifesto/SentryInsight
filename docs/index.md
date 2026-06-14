# Exploitation Report

Current cybersecurity landscape reveals several critical zero-day vulnerabilities and active exploitation campaigns targeting enterprise systems. The most significant threats include Oracle PeopleSoft zero-day exploitation by ShinyHunters targeting universities, critical Splunk Enterprise vulnerabilities enabling unauthenticated remote code execution, and sophisticated supply chain attacks compromising over 400 Arch Linux packages. Chinese threat actors have demonstrated remarkable persistence through decade-long authentication bypass campaigns, while authentication vulnerabilities in phpBB forum software have remained undetected for 10 years before discovery.

## Active Exploitation Details

### Oracle PeopleSoft Zero-Day Vulnerability
- **Description**: Critical zero-day vulnerability in Oracle PeopleSoft Suite allowing unauthenticated remote code execution
- **Impact**: Complete system compromise, data theft, and extortion demands from threat actors
- **Status**: Actively exploited by ShinyHunters, Oracle has issued mitigation guidance
- **CVE ID**: CVE-2026-35273

### Splunk Enterprise Critical Vulnerability
- **Description**: Critical security flaw in Splunk Enterprise enabling unauthenticated file operations and remote code execution
- **Impact**: Complete system compromise without authentication requirements
- **Status**: Security updates released by Splunk to address the vulnerability

### Ivanti Sentry Actively Exploited Flaw
- **Description**: Security vulnerability in Ivanti Sentry being actively exploited in the wild
- **Impact**: System compromise affecting federal agencies
- **Status**: CISA has mandated federal agencies patch within three days due to active exploitation

### phpBB Authentication Bypass
- **Description**: 10-year-old authentication bypass vulnerability in phpBB forum software
- **Impact**: Allows attackers to log in as any user, including administrators
- **Status**: Recently discovered and patched after lurking undetected for a decade

### LangGraph Remote Code Execution Chain
- **Description**: Critical vulnerability chain in LangGraph affecting self-hosted AI agents
- **Impact**: Remote code execution on systems running AI agents
- **Status**: Three security flaws have been patched

## Affected Systems and Products

- **Oracle PeopleSoft Suite**: Enterprise resource planning systems, particularly affecting American universities
- **Splunk Enterprise**: Data analytics and monitoring platforms across enterprise environments
- **Ivanti Sentry**: Identity and access management systems used by federal agencies
- **phpBB Forum Software**: Web-based bulletin board systems running vulnerable versions for up to 10 years
- **Arch Linux AUR Packages**: Over 400 compromised packages in the Arch User Repository
- **LangGraph AI Agents**: Self-hosted artificial intelligence coding agents
- **Linux Authentication Systems**: Login software backdoored by Chinese threat actors
- **Tchap Messenger**: French government encrypted messaging platform affecting 73,000+ accounts

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Oracle PeopleSoft zero-day used for direct system access and data theft
- **Supply Chain Compromise**: Malicious modification of over 400 Arch Linux packages to deploy rootkits and infostealers
- **Authentication Stack Hijacking**: Chinese hackers maintaining decade-long persistence through authentication system control
- **Unauthenticated Remote Code Execution**: Splunk Enterprise vulnerabilities exploitable without authentication
- **Package Repository Hijacking**: Attackers taking control of legitimate software packages to distribute malware
- **AI Agent Manipulation**: Agentjacking attacks tricking AI coding agents into executing malicious code
- **Phishing-as-a-Service**: Sniper Dz platform providing decade-long phishing services to cybercriminals

## Threat Actor Activities

- **ShinyHunters**: Actively exploiting Oracle PeopleSoft zero-day to breach university systems and steal data for extortion
- **Chinese APT Groups**: Maintaining decade-long persistence in authentication systems and isolated networks with sophisticated backdoors
- **Conti Ransomware Operation**: Ukrainian national pleading guilty to conspiracy charges related to ransomware activities
- **Chinese Cybercrime Network**: Using Google's Gemini AI for enhanced phishing campaigns targeting American users
- **AudiA6 Cryptocurrency Laundering Service**: Disrupted by Europol, was used by ransomware gangs for money laundering operations
- **Sniper Dz PhaaS Platform**: Decade-long phishing-as-a-service operation disrupted by INTERPOL with administrator arrested
- **Linux Package Attackers**: Compromised hundreds of Arch Linux packages to deploy eBPF rootkits and credential stealers