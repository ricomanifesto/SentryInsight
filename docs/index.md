# Exploitation Report

Critical zero-day and actively exploited vulnerabilities are dominating the current threat landscape, with attackers demonstrating rapid exploitation capabilities and sophisticated supply chain targeting. The most significant activity includes the ShinyHunters group exploiting CVE-2026-35273, a zero-day in Oracle PeopleSoft that has devastated higher education institutions, and CVE-2025-26015, a maximum severity Ivanti Sentry vulnerability exploited within 24 hours of public disclosure. Supply chain attacks have escalated dramatically with over 400 Arch Linux AUR packages compromised to distribute rootkits and infostealers. Additionally, a decade-old authentication bypass vulnerability in phpBB forum software and sophisticated backdoors in Linux login systems highlight the persistence and evolution of modern cyber threats.

## Active Exploitation Details

### Oracle PeopleSoft Zero-Day Vulnerability
- **Description**: Critical vulnerability in Oracle PeopleSoft Suite allowing unauthenticated remote code execution
- **Impact**: Complete system compromise, data theft, and extortion campaigns targeting enterprise systems
- **Status**: Actively exploited by ShinyHunters group in data theft attacks; Oracle has issued mitigations
- **CVE ID**: CVE-2026-35273

### Ivanti Sentry Maximum Severity Flaw
- **Description**: Critical vulnerability in Ivanti Sentry systems enabling remote exploitation
- **Impact**: Full system compromise allowing attackers to gain unauthorized access and control
- **Status**: Actively exploited within 24 hours of disclosure; CISA has ordered federal agencies to patch within 3 days
- **CVE ID**: CVE-2025-26015

### phpBB Authentication Bypass Vulnerability
- **Description**: A decade-old authentication bypass vulnerability in phpBB forum software
- **Impact**: Allows attackers to log in as any user, including administrators, compromising forum security completely
- **Status**: Recently patched after lurking undetected for 10 years

### Linux Login System Backdoors
- **Description**: Sophisticated backdoors implanted in Linux login systems by China-linked threat actors
- **Impact**: Near-decade-long persistence allowing covert access to Linux servers and systems
- **Status**: Discovered after operating undetected for almost 10 years

### LangGraph Remote Code Execution Chain
- **Description**: Critical vulnerability chain in LangGraph affecting self-hosted AI agents
- **Impact**: Remote code execution on systems running AI agent infrastructure
- **Status**: Three security flaws have been patched, including critical RCE chain

## Affected Systems and Products

- **Oracle PeopleSoft Suite**: Enterprise resource planning software with critical zero-day vulnerability
- **Ivanti Sentry**: Security management systems with maximum severity exploitation
- **Arch Linux AUR Packages**: Over 400 compromised packages distributing malware to Linux users
- **phpBB Forum Software**: Popular forum platform affected by 10-year-old authentication bypass
- **Linux Login Systems**: Core authentication mechanisms compromised by persistent backdoors
- **LangGraph AI Framework**: Self-hosted AI agent platform vulnerable to remote code execution
- **Windows BitLocker**: Encryption system bypassed by GreatXML exploit via recovery partition manipulation
- **OpenClaw AI Agent**: Popular self-hosted AI agent vulnerable to code execution and data exfiltration

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Rapid weaponization of newly disclosed vulnerabilities within hours
- **Supply Chain Compromise**: Mass hijacking of software repositories to distribute malware
- **Package Repository Poisoning**: Rewriting build scripts in 400+ Arch Linux packages to install credential stealers
- **Authentication Bypass**: Exploiting decade-old vulnerabilities to gain administrative access
- **Persistent Backdoors**: Long-term compromise of core system components for sustained access
- **Recovery Partition Manipulation**: GreatXML technique bypassing BitLocker encryption through XML file exploitation
- **AI Agent Manipulation**: Agentjacking attacks tricking AI coding agents into executing malicious code
- **Phishing-as-a-Service**: Sophisticated platforms like Sniper Dz providing turnkey phishing operations

## Threat Actor Activities

- **ShinyHunters**: Exploiting Oracle PeopleSoft zero-day to breach universities and conduct data extortion campaigns
- **China-Linked Groups**: Operating sophisticated backdoors in Linux login systems for nearly a decade
- **Supply Chain Attackers**: Compromising 400+ Arch Linux packages to deploy eBPF rootkits and credential stealers
- **Chinese Smishing Network**: Using Google's Gemini AI to enhance phishing text message campaigns
- **Conti Ransomware Operation**: Continued legal proceedings against Ukrainian national involved in major ransomware campaigns
- **AudiA6 Cryptocurrency Laundering Service**: Disrupted by Europol after serving ransomware gangs and cybercriminal networks
- **Sniper Dz PhaaS Operators**: Decade-long phishing platform disrupted by INTERPOL Operation Ramz