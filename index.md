# Exploitation Report

Critical zero-day vulnerabilities are currently being actively exploited by cybercriminals targeting enterprise and educational institutions. Oracle PeopleSoft systems are under attack via CVE-2026-35273, allowing unauthenticated remote code execution that has enabled the ShinyHunters group to breach multiple universities and steal sensitive data. Additionally, over 400 packages in the Arch Linux User Repository have been compromised to distribute rootkit and credential-stealing malware. A decade-old authentication bypass vulnerability in phpBB forum software has been discovered and patched, while Chinese threat actors have maintained persistent access to authentication systems for nearly ten years. The Splunk Enterprise platform also faces a critical flaw enabling unauthenticated file operations and remote code execution.

## Active Exploitation Details

### Oracle PeopleSoft Zero-Day Vulnerability
- **Description**: Critical vulnerability in Oracle PeopleSoft Suite allowing unauthenticated remote code execution
- **Impact**: Attackers can execute arbitrary code on vulnerable systems without authentication, leading to data theft and system compromise
- **Status**: Actively exploited by ShinyHunters group; Oracle has issued mitigations
- **CVE ID**: CVE-2026-35273

### Splunk Enterprise Critical Flaw
- **Description**: Critical security vulnerability in Splunk Enterprise enabling unauthenticated file operations
- **Impact**: Attackers can perform unauthorized file operations and achieve remote code execution without authentication
- **Status**: Security updates released by Splunk

### phpBB Authentication Bypass
- **Description**: 10-year-old authentication bypass vulnerability in phpBB forum software
- **Impact**: Allows attackers to log in as any user, including administrators
- **Status**: Patched by phpBB

### Ivanti Sentry Vulnerability
- **Description**: Actively exploited vulnerability in Ivanti Sentry systems
- **Impact**: System compromise and potential lateral movement within federal networks
- **Status**: CISA has mandated federal agencies patch within three days

### Linux Login System Backdoor
- **Description**: Chinese-linked hackers backdoored Linux login software to maintain persistent access
- **Impact**: Nearly decade-long hidden access to authentication systems with administrative visibility
- **Status**: Discovered and reported by Sygnia

### Arch Linux Package Compromise
- **Description**: Mass compromise of over 400 packages in the Arch User Repository (AUR)
- **Impact**: Distribution of Linux rootkit and credential-stealing malware targeting access tokens
- **Status**: Packages identified and being remediated

## Affected Systems and Products

- **Oracle PeopleSoft Suite**: Enterprise resource planning software, particularly affecting universities and educational institutions
- **Splunk Enterprise**: Data analytics and monitoring platform used across enterprise environments
- **phpBB Forum Software**: Open-source forum platform with 10-year vulnerability exposure
- **Ivanti Sentry**: Federal government systems requiring immediate patching
- **Linux Authentication Systems**: Enterprise Linux environments with compromised login mechanisms
- **Arch Linux AUR**: Over 400 packages in the Arch User Repository compromised with malware
- **French Government Tchap**: Encrypted messaging platform affecting 73,000+ government employees

## Attack Vectors and Techniques

- **Unauthenticated Remote Code Execution**: Exploitation of Oracle PeopleSoft and Splunk Enterprise vulnerabilities without authentication requirements
- **Supply Chain Compromise**: Hijacking of legitimate software packages in Arch Linux repository to distribute malware
- **Authentication Stack Manipulation**: Chinese actors maintaining persistent access by compromising core authentication mechanisms
- **Phishing-as-a-Service**: Use of platforms like Sniper Dz for large-scale phishing operations
- **AI-Enhanced Phishing**: Exploitation of Google's Gemini AI for generating sophisticated phishing content
- **Agentjacking Attacks**: Novel technique targeting AI coding agents to execute malicious code on developer systems

## Threat Actor Activities

- **ShinyHunters**: Actively exploiting Oracle PeopleSoft zero-day (CVE-2026-35273) to breach universities and steal data for extortion
- **Chinese APT Groups**: Maintaining decade-long persistence in authentication systems and isolated networks with full administrative visibility
- **Ukrainian Conti Operator**: Guilty plea in connection with major ransomware operation targeting critical infrastructure
- **Arch Linux Package Attackers**: Compromised hundreds of packages to distribute eBPF rootkit and credential-stealing malware
- **Chinese Smishing Network**: Using Google's Gemini AI to generate phishing text messages targeting American users
- **AudiA6 Crypto Laundering Service**: Disrupted by Europol, was used by multiple ransomware gangs for cryptocurrency laundering
- **Sniper Dz PhaaS Operators**: Decade-long phishing-as-a-service platform disrupted by INTERPOL Operation Ramz