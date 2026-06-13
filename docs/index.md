# Exploitation Report

Critical exploitation activity is dominated by multiple zero-day vulnerabilities being actively exploited in the wild, most notably an Oracle PeopleSoft zero-day (CVE-2026-35273) used by the ShinyHunters extortion crew to breach numerous universities and enterprise systems. Additional active exploitations include a maximum severity Ivanti Sentry vulnerability that was exploited within 24 hours of disclosure, prompting emergency patching orders from CISA. The threat landscape also features supply chain attacks targeting over 400 Arch Linux packages with rootkits and infostealers, sophisticated AI agent manipulation attacks, and a decade-long authentication bypass vulnerability in phpBB forum software. China-linked threat actors have maintained persistent access to Linux systems for nearly a decade through backdoored login software.

## Active Exploitation Details

### Oracle PeopleSoft Zero-Day Vulnerability
- **Description**: Critical unpatched vulnerability in Oracle PeopleSoft Suite allowing unauthenticated remote code execution
- **Impact**: Enables attackers to break into enterprise systems, steal sensitive data, and conduct extortion campaigns
- **Status**: Actively exploited by ShinyHunters crew, Oracle has issued mitigation guidance
- **CVE ID**: CVE-2026-35273

### Ivanti Sentry Maximum Severity Vulnerability
- **Description**: Critical vulnerability in Ivanti Sentry with maximum severity rating
- **Impact**: Allows unauthorized access and compromise of affected systems
- **Status**: Exploited within 24 hours of public disclosure, CISA ordered federal agencies to patch within 3 days
- **CVE ID**: Not specified in articles

### phpBB Authentication Bypass Vulnerability
- **Description**: 10-year-old authentication bypass vulnerability in phpBB forum software
- **Impact**: Allows attackers to log in as any user, including administrators
- **Status**: Recently patched after lurking undetected for a decade
- **CVE ID**: Not specified in articles

### LangGraph Remote Code Execution Chain
- **Description**: Critical vulnerability chain in LangGraph affecting self-hosted AI agents
- **Impact**: Enables remote code execution on systems running LangGraph agents
- **Status**: Three security flaws have been patched
- **CVE ID**: Not specified in articles

## Affected Systems and Products

- **Oracle PeopleSoft Suite**: Enterprise resource planning software, particularly affecting universities and higher education institutions
- **Ivanti Sentry**: Security and access management platform used by government agencies and enterprises
- **phpBB Forum Software**: Web forum platform with 10-year-old vulnerability affecting all versions
- **Arch Linux AUR**: Over 400 packages compromised in the Arch User Repository
- **LangGraph**: AI agent framework for building language model applications
- **OpenClaw AI Agent**: Self-hosted AI agent platform vulnerable to code execution attacks
- **Windows BitLocker**: Encryption system bypassed via GreatXML exploit targeting recovery partition XML files
- **Linux Systems**: Login software backdoored by China-linked actors for nearly a decade

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: ShinyHunters leveraged Oracle PeopleSoft zero-day for enterprise breaches and data theft
- **Supply Chain Compromise**: Mass hijacking of 400+ Arch Linux AUR packages to deploy rootkits and credential stealers
- **AI Agent Manipulation**: "Agentjacking" attacks tricking AI coding agents into executing malicious code
- **Authentication Bypass**: Exploitation of decade-old phpBB vulnerability for administrative access
- **BitLocker Bypass**: GreatXML exploit manipulating recovery partition XML files to circumvent Windows encryption
- **Backdoor Persistence**: China-linked actors maintained nearly decade-long presence in Linux login systems
- **Rapid Exploitation**: Attackers exploited Ivanti vulnerability within 24 hours of public disclosure

## Threat Actor Activities

- **ShinyHunters**: Actively exploiting Oracle PeopleSoft zero-day targeting universities and enterprises for data theft and extortion
- **China-Linked Group (Venom Spider)**: Maintained persistent backdoor access to Linux login systems for nearly a decade, tracked by Sygnia
- **AUR Package Hijackers**: Compromised over 400 Arch Linux packages to distribute eBPF rootkits and credential-stealing malware
- **Chinese Smishing Network**: Using Google's Gemini AI to enhance phishing text message campaigns targeting Americans
- **Ivanti Exploit Actors**: Rapidly weaponized maximum severity Ivanti vulnerability within 24 hours of disclosure
- **Conti Ransomware Operation**: Ukrainian national pleaded guilty to conspiracy charges related to the notorious ransomware group