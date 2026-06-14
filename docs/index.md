# Exploitation Report

Critical zero-day exploitation is currently underway across multiple enterprise platforms, with the most significant activity involving Oracle PeopleSoft systems being actively exploited by the ShinyHunters threat group using CVE-2026-35273. Additional active exploitation includes a critical Splunk Enterprise vulnerability enabling unauthenticated remote code execution, a decade-old phpBB authentication bypass flaw, and an actively exploited Ivanti Sentry vulnerability prompting emergency federal patching orders. Sophisticated threat actors are also conducting long-term persistence campaigns, with Chinese hackers maintaining decade-long access through compromised authentication systems and Linux login backdoors, while supply chain attacks have compromised over 400 Arch Linux packages to distribute rootkits and infostealers.

## Active Exploitation Details

### Oracle PeopleSoft Zero-Day Vulnerability
- **Description**: Critical zero-day flaw in Oracle PeopleSoft Suite allowing unauthenticated remote code execution
- **Impact**: Complete system compromise, data theft, and unauthorized access to enterprise systems
- **Status**: Actively exploited by ShinyHunters group, Oracle has issued mitigations
- **CVE ID**: CVE-2026-35273

### Splunk Enterprise Critical Vulnerability
- **Description**: Critical security flaw enabling unauthenticated file operations and remote code execution
- **Impact**: Complete system compromise without authentication requirements
- **Status**: Security updates released by Splunk to address the vulnerability

### phpBB Authentication Bypass Vulnerability
- **Description**: 10-year-old authentication bypass vulnerability in phpBB forum software
- **Impact**: Attackers can log in as any user, including administrators
- **Status**: Recently patched after a decade-long presence in the codebase

### Ivanti Sentry Vulnerability
- **Description**: Actively exploited vulnerability in Ivanti Sentry systems
- **Impact**: System compromise requiring immediate patching
- **Status**: Under active exploitation, CISA has mandated federal agencies patch within three days

## Affected Systems and Products

- **Oracle PeopleSoft Suite**: Enterprise resource planning systems, particularly affecting American universities
- **Splunk Enterprise**: Data analytics and monitoring platforms across enterprise environments  
- **phpBB Forum Software**: Web-based bulletin board systems running affected versions
- **Ivanti Sentry**: Identity and access management systems in federal environments
- **Arch Linux AUR**: Over 400 packages in the Arch User Repository compromised with malicious build scripts
- **Linux Authentication Systems**: Login software backdoored by Chinese threat actors for nearly a decade
- **French Government Tchap Messenger**: Encrypted messaging platform affecting 73,000+ public sector accounts

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched Oracle PeopleSoft systems for data theft
- **Authentication Flow Hijacking**: Chinese hackers taking control of authentication stacks for persistent access
- **Supply Chain Poisoning**: Malicious modification of Arch Linux package build scripts to deploy infostealers and rootkits
- **Authentication Bypass**: Exploitation of decade-old phpBB vulnerabilities to gain administrative access
- **Backdoor Installation**: Long-term compromise of Linux login systems for covert persistence
- **Unauthenticated Remote Code Execution**: Direct system compromise through Splunk Enterprise vulnerabilities

## Threat Actor Activities

- **ShinyHunters Group**: Actively exploiting Oracle PeopleSoft zero-day (CVE-2026-35273) to breach university systems and steal data for extortion
- **Chinese APT Group (Voltaic Storm)**: Maintained decade-long persistence through compromised authentication systems and Linux login backdoors
- **Arch Linux Supply Chain Attackers**: Compromised over 400 AUR packages to distribute credential stealers and eBPF rootkits
- **Chinese Cybercrime Network**: Using Google's Gemini AI to enhance phishing campaigns targeting American users
- **Conti Ransomware Operation**: Ukrainian national pleaded guilty to conspiracy charges related to the ransomware group's activities
- **Former Insider Threat**: Ex-school district IT employee conducted prolonged cyberattacks against former employer, resulting in 21-month prison sentence