# Exploitation Report

Critical exploitation activities are currently targeting multiple systems across enterprise, government, and educational sectors. The ShinyHunters group has been actively exploiting a zero-day vulnerability in Oracle PeopleSoft systems, particularly targeting American universities and stealing sensitive data. Concurrently, multiple supply chain attacks have compromised over 400 Arch Linux packages, while state-sponsored Chinese threat actors have maintained persistent access to authentication systems for nearly a decade. Additional active threats include a critical Splunk Enterprise vulnerability allowing unauthenticated remote code execution, and an actively exploited Ivanti Sentry flaw that has prompted emergency patching directives from CISA.

## Active Exploitation Details

### Oracle PeopleSoft Zero-Day Vulnerability
- **Description**: An unpatched flaw in Oracle's PeopleSoft ERP software that allows unauthorized access to enterprise systems
- **Impact**: Attackers can break into enterprise systems, steal sensitive data, and conduct extortion campaigns
- **Status**: Zero-day vulnerability being actively exploited by ShinyHunters group, particularly targeting universities
- **CVE ID**: CVE-2026-35273

### Splunk Enterprise Critical Vulnerability
- **Description**: A critical security flaw in Splunk Enterprise that allows unauthenticated attackers to conduct file operations and execute remote code
- **Impact**: Complete system compromise without authentication requirements, allowing attackers to execute arbitrary code and access sensitive data
- **Status**: Actively exploitable, security updates released by Splunk

### Ivanti Sentry Vulnerability
- **Description**: A security flaw in Ivanti Sentry systems that is being actively exploited in the wild
- **Impact**: System compromise and unauthorized access to protected resources
- **Status**: Under active exploitation, CISA has issued emergency patching directive requiring federal agencies to patch within three days

### phpBB Authentication Bypass
- **Description**: A 10-year-old authentication bypass vulnerability in phpBB forum software that allows attackers to log in as any user
- **Impact**: Complete administrative access to forum systems, ability to impersonate any user including administrators
- **Status**: Recently patched after decade-long exposure

## Affected Systems and Products

- **Oracle PeopleSoft**: ERP software systems, particularly affecting American universities and educational institutions
- **Splunk Enterprise**: Data analytics and monitoring platforms across enterprise environments
- **Arch Linux AUR**: Over 400 packages in the Arch User Repository compromised with malicious build scripts
- **Ivanti Sentry**: Identity and access management systems in federal government agencies
- **phpBB Forum Software**: Web-based forum platforms with 10+ year vulnerability exposure
- **Linux Authentication Systems**: Login software and authentication stacks targeted by Chinese threat actors
- **LangGraph AI Agents**: Self-hosted artificial intelligence agent platforms vulnerable to remote code execution

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched Oracle PeopleSoft vulnerabilities for data theft and extortion
- **Supply Chain Attacks**: Compromise of software repositories to distribute malicious code through legitimate update channels
- **Authentication Stack Manipulation**: Long-term persistence through modification of Linux login systems and authentication flows
- **Package Repository Hijacking**: Takeover of legitimate software packages to deploy rootkits and information stealers
- **Unauthenticated Remote Code Execution**: Direct system compromise without requiring valid credentials
- **AI Agent Manipulation**: "Agentjacking" attacks that trick AI coding agents into executing malicious code on developer systems

## Threat Actor Activities

- **ShinyHunters Group**: Actively exploiting Oracle PeopleSoft zero-day (CVE-2026-35273) in targeted campaigns against universities, conducting data theft and extortion operations
- **Chinese State-Sponsored Actors**: Maintaining nearly decade-long persistence in authentication systems, demonstrating advanced persistent threat capabilities with complete administrative visibility
- **Supply Chain Attackers**: Coordinated compromise of 400+ Arch Linux AUR packages to distribute eBPF rootkits and credential stealers targeting Linux users
- **AI-Powered Phishing Networks**: Chinese cybercrime groups utilizing Google's Gemini AI and other artificial intelligence tools to enhance phishing campaigns and social engineering attacks
- **Conti Ransomware Operation**: Continued legal proceedings against Ukrainian nationals involved in the ransomware-as-a-service operation
- **Outsider Enterprise**: Chinese phishing-as-a-service operation disrupted by FBI, utilizing over one million URLs for large-scale credential harvesting