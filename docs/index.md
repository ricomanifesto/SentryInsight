# Exploitation Report

Critical zero-day exploitation activity is dominating the threat landscape, with the ShinyHunters extortion crew actively exploiting CVE-2026-35273, an Oracle PeopleSoft vulnerability allowing unauthenticated remote code execution. This campaign has disproportionately affected American universities, enabling widespread data theft operations. Simultaneously, sophisticated nation-state actors have demonstrated unprecedented persistence, with Chinese hackers maintaining decade-long access to authentication systems and backdooring Linux login software. The threat environment is further complicated by supply chain compromises affecting over 400 Arch Linux packages, critical Splunk Enterprise vulnerabilities enabling unauthenticated remote code execution, and a 10-year-old phpBB authentication bypass vulnerability. These incidents collectively represent a significant escalation in both attack sophistication and the scale of vulnerable systems being actively exploited.

## Active Exploitation Details

### Oracle PeopleSoft Zero-Day Vulnerability
- **Description**: Critical vulnerability in Oracle PeopleSoft Suite allowing unauthenticated remote code execution
- **Impact**: Enables attackers to break into enterprise systems, steal sensitive data, and conduct extortion operations
- **Status**: Actively exploited by ShinyHunters crew; Oracle has issued mitigations
- **CVE ID**: CVE-2026-35273

### Splunk Enterprise Critical Flaw
- **Description**: Critical security vulnerability in Splunk Enterprise enabling unauthenticated file operations and remote code execution
- **Impact**: Allows attackers to execute arbitrary code without authentication, potentially compromising entire Splunk deployments
- **Status**: Security updates released by Splunk to address the vulnerability

### phpBB Authentication Bypass
- **Description**: 10-year-old authentication bypass vulnerability in phpBB forum software
- **Impact**: Allows attackers to log in as any user, including administrators, potentially compromising forum operations and user data
- **Status**: Patched by phpBB developers after decade-long exposure

### Ivanti Sentry Vulnerability
- **Description**: Actively exploited vulnerability in Ivanti Sentry systems
- **Impact**: Enables unauthorized access to Ivanti Sentry deployments, potentially compromising security infrastructure
- **Status**: Under active exploitation; CISA mandated federal agencies patch within three days

### Arch Linux AUR Package Compromise
- **Description**: Over 400 packages in Arch User Repository hijacked with malicious build scripts
- **Impact**: Installs credential stealer and eBPF rootkit on systems that build compromised packages
- **Status**: Active supply chain attack affecting Linux environments

### LangGraph Security Flaws
- **Description**: Critical vulnerability chain in LangGraph affecting self-hosted AI agents
- **Impact**: Could result in remote code execution on AI agent systems
- **Status**: Three vulnerabilities patched after disclosure

## Affected Systems and Products

- **Oracle PeopleSoft Suite**: Enterprise resource planning systems, particularly at American universities
- **Splunk Enterprise**: Data analytics and security information management platforms
- **phpBB Forum Software**: Web-based forum platforms running vulnerable versions for up to 10 years
- **Ivanti Sentry**: Identity and access management systems in federal government environments
- **Arch Linux AUR**: Over 400 compromised packages affecting Linux users and developers
- **LangGraph**: Self-hosted artificial intelligence agents and development frameworks
- **Linux Authentication Systems**: Login software backdoored by sophisticated threat actors
- **Tchap Messaging Platform**: French government encrypted messaging system affecting 73,000+ accounts

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: ShinyHunters leveraging unpatched Oracle PeopleSoft vulnerability for data theft
- **Supply Chain Poisoning**: Malicious code injection into legitimate software repositories affecting hundreds of packages
- **Authentication System Backdoors**: Long-term persistence through modification of core authentication components
- **Unauthenticated Remote Code Execution**: Direct system compromise without credential requirements
- **AI Agent Manipulation**: "Agentjacking" attacks tricking AI coding agents into executing malicious code
- **Phishing-as-a-Service**: Sophisticated platforms like Sniper Dz enabling widespread credential harvesting
- **Authentication Flow Hijacking**: Taking control of organizational authentication stacks for persistent access

## Threat Actor Activities

- **ShinyHunters**: Actively exploiting Oracle PeopleSoft zero-day (CVE-2026-35273) in targeted data theft campaigns against universities; conducting extortion operations demanding payment to keep stolen data private
- **Chinese Nation-State Groups**: Maintaining decade-long persistence in target networks through authentication system hijacking; backdooring Linux login software for nearly 10 years of covert access
- **Arch Linux Package Attackers**: Compromised over 400 AUR packages to deploy credential stealers and eBPF rootkits targeting Linux developers and users
- **Chinese Smishing Network**: Using Google's Gemini AI to enhance phishing text message campaigns targeting American users
- **Sniper Dz Operators**: Decade-long phishing-as-a-service platform disrupted by INTERPOL Operation Ramz
- **Conti Ransomware Affiliates**: Ukrainian national pleading guilty to conspiracy charges related to ransomware operations