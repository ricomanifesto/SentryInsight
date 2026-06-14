# Exploitation Report

Critical zero-day vulnerabilities and sophisticated attack campaigns are dominating the current threat landscape. The most significant developments include the active exploitation of Oracle PeopleSoft zero-day vulnerability CVE-2026-35273 by the ShinyHunters group targeting universities, a critical Splunk Enterprise flaw enabling unauthenticated remote code execution, and the compromise of over 400 Arch Linux packages to deploy malware. Additionally, a China-linked threat group has maintained persistence in authentication systems for nearly a decade, while a 10-year-old authentication bypass vulnerability in phpBB forum software has been discovered and patched. These incidents highlight the increasing sophistication of attack vectors and the critical need for immediate security updates.

## Active Exploitation Details

### Oracle PeopleSoft Zero-Day Vulnerability
- **Description**: Critical vulnerability in Oracle PeopleSoft Suite allowing unauthenticated remote code execution
- **Impact**: Attackers can gain unauthorized access to enterprise systems, steal sensitive data, and demand ransom payments
- **Status**: Actively exploited by ShinyHunters group, Oracle has issued mitigation guidance
- **CVE ID**: CVE-2026-35273

### Splunk Enterprise Critical Flaw
- **Description**: Critical security vulnerability in Splunk Enterprise enabling unauthenticated file operations and remote code execution
- **Impact**: Attackers can execute arbitrary code without authentication, potentially compromising entire Splunk deployments
- **Status**: Security updates released by Splunk to address the vulnerability

### Ivanti Sentry Vulnerability
- **Description**: Actively exploited vulnerability in Ivanti Sentry systems
- **Impact**: Allows unauthorized access and potential system compromise
- **Status**: Under active exploitation, CISA has mandated federal agencies patch within three days

### phpBB Authentication Bypass
- **Description**: 10-year-old authentication bypass vulnerability in phpBB forum software
- **Impact**: Allows attackers to log in as any user, including administrators
- **Status**: Recently discovered and patched after lurking undetected for a decade

### Linux Authentication System Compromise
- **Description**: China-linked hackers backdoored Linux login software to maintain persistent access
- **Impact**: Complete control over authentication stack with full visibility into administrative activities
- **Status**: Group maintained access for nearly a decade before detection

## Affected Systems and Products

- **Oracle PeopleSoft Suite**: Enterprise resource planning systems, particularly affecting American universities
- **Splunk Enterprise**: Data analytics and monitoring platforms across various organizations
- **Ivanti Sentry**: Identity and access management systems in federal government agencies
- **phpBB Forum Software**: Open-source bulletin board software used by numerous organizations
- **Arch Linux AUR Packages**: Over 400 packages in the Arch User Repository compromised
- **Linux Authentication Systems**: Login software and authentication stacks in enterprise environments
- **Novo Nordisk Clinical Systems**: Patient information from clinical trials at the pharmaceutical giant
- **French Government Tchap Platform**: Encrypted messaging system affecting over 73,000 public sector employees

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: ShinyHunters leveraging unpatched Oracle vulnerability for data theft operations
- **Supply Chain Attacks**: Compromise of Arch Linux packages to distribute rootkits and infostealers
- **Authentication Hijacking**: Long-term persistence through compromised login systems and authentication flows
- **Unauthenticated Remote Code Execution**: Direct exploitation of critical vulnerabilities without credentials
- **Privilege Escalation**: Authentication bypass techniques to gain administrative access
- **AI-Enhanced Phishing**: Use of artificial intelligence tools like Gemini to create sophisticated phishing campaigns
- **Package Repository Hijacking**: Takeover of legitimate software packages to distribute malware
- **Agentjacking Attacks**: Novel technique targeting AI coding agents to execute malicious code

## Threat Actor Activities

- **ShinyHunters Group**: Actively exploiting Oracle PeopleSoft zero-day to target universities for data theft and extortion
- **China-Linked APT Groups**: Maintaining decade-long persistence in authentication systems and isolated networks
- **Conti Ransomware Operation**: Continued legal proceedings with Ukrainian national pleading guilty to conspiracy charges
- **Chinese Cybercrime Networks**: Using AI tools for sophisticated phishing campaigns targeting American users
- **Former Insider Threat**: Ex-school district employee sentenced for prolonged cyberattacks against former employer
- **AudiA6 Cryptocurrency Laundering Service**: Disrupted by Europol after serving ransomware gangs and cybercriminal networks
- **Sniper Dz PhaaS Platform**: Decade-long phishing-as-a-service operation disrupted by INTERPOL-led Operation Ramz