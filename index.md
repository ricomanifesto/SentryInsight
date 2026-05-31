# Exploitation Report

Critical exploitation activity is currently targeting enterprise infrastructure through multiple vectors. The most severe ongoing threats include active exploitation of a Palo Alto Networks GlobalProtect authentication bypass vulnerability (CVE-2026-0257) allowing unauthorized network access, a local privilege escalation flaw dubbed "CIFSwitch" in the Linux kernel enabling root access across multiple distributions, and exploitation of FortiClient Enterprise Management Server authentication bypass (CVE-2026-35616) to deploy infostealer malware. Additionally, threat actors are leveraging AI-powered tools and exploiting a Marimo vulnerability (CVE-2026-39987) for post-exploitation activities, while abusing legitimate platforms like ChatGPT for malicious purposes.

## Active Exploitation Details

### PAN-OS GlobalProtect Authentication Bypass
- **Description**: A medium-severity authentication bypass vulnerability in Palo Alto Networks PAN-OS and Prisma Access that allows attackers to circumvent authentication mechanisms
- **Impact**: Unauthorized access to corporate networks through VPN infrastructure, enabling potential lateral movement and data exfiltration
- **Status**: Under active exploitation in the wild with patches available from vendor
- **CVE ID**: CVE-2026-0257

### CIFSwitch Linux Kernel Privilege Escalation
- **Description**: A newly discovered local privilege escalation vulnerability in the Linux kernel that allows attackers to forge CIFS authentication key descriptions and abuse the kernel's key request mechanism
- **Impact**: Attackers can escalate privileges to root access on multiple Linux distributions
- **Status**: Actively exploitable across multiple Linux distributions

### FortiClient EMS Authentication Bypass
- **Description**: Authentication bypass vulnerability in FortiClient Enterprise Management Server allowing unauthorized access to management functions
- **Impact**: Deployment of infostealer malware (EKZ) through compromised enterprise management infrastructure
- **Status**: Under active exploitation with undocumented malware deployment
- **CVE ID**: CVE-2026-35616

### Marimo Post-Exploitation Vulnerability
- **Description**: A publicly-accessible vulnerability being exploited for initial access followed by LLM-powered post-compromise activities
- **Impact**: Initial system compromise with AI-enhanced post-exploitation capabilities for persistence and lateral movement
- **Status**: Actively exploited with threat actors using large language model agents for automated post-compromise actions
- **CVE ID**: CVE-2026-39987

## Affected Systems and Products

- **Palo Alto Networks PAN-OS**: GlobalProtect VPN infrastructure and Prisma Access cloud security services
- **Linux Distributions**: Multiple distributions affected by CIFSwitch kernel vulnerability enabling root access
- **FortiClient EMS**: Enterprise Management Server installations vulnerable to authentication bypass attacks
- **Marimo Platforms**: Publicly-accessible instances being exploited for initial access
- **ChatGPT Platform**: Content-sharing features being abused to host fake outage pages and phishing content
- **OpenAI ChatGPT**: Web summary functionality vulnerable to markdown-based phishing attacks (ChatGPhish)

## Attack Vectors and Techniques

- **VPN Authentication Bypass**: Exploitation of GlobalProtect authentication mechanisms to gain unauthorized network access
- **Local Privilege Escalation**: CIFSwitch vulnerability abuse through CIFS authentication key manipulation
- **AI-Powered Social Engineering**: Use of ChatGPT and Google Gemini by GreyVibe threat actors to generate convincing phishing lures
- **LLM Agent Automation**: Deployment of large language model agents for automated post-exploitation activities
- **Platform Abuse**: Leveraging legitimate ChatGPT sharing features to host malicious content and phishing pages
- **Enterprise Management Compromise**: Exploitation of FortiClient EMS to deploy custom infostealer malware
- **Markdown Injection**: ChatGPhish technique using AI assistant's trust in markdown links for phishing attacks

## Threat Actor Activities

- **GreyVibe (Russia-linked)**: Conducting persistent AI-powered attacks against Ukraine and Ukrainian entities since August 2025, utilizing ChatGPT and Google Gemini for generating phishing content and deploying custom malware tools
- **Unknown LLM-Using Actors**: Exploiting Marimo vulnerabilities (CVE-2026-39987) and employing large language model agents for sophisticated post-compromise operations including automated reconnaissance and persistence
- **Enterprise-Targeting Groups**: Actively exploiting FortiClient EMS vulnerabilities to deploy EKZ infostealer malware through compromised enterprise management infrastructure
- **VPN-Focused Attackers**: Exploiting PAN-OS GlobalProtect authentication bypass to gain unauthorized access to corporate networks worldwide