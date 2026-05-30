# Exploitation Report

Critical vulnerabilities across multiple platforms are experiencing active exploitation, posing significant risks to enterprise infrastructure and security. The most severe activity involves authentication bypass flaws in Palo Alto Networks' PAN-OS GlobalProtect (CVE-2026-0257), exploitation of FortiClient EMS vulnerabilities (CVE-2026-35616) to deploy credential-stealing malware, and a code execution vulnerability in the Marimo platform (CVE-2026-39987) where attackers are leveraging large language models for post-exploitation activities. Additionally, threat actors are exploiting vulnerabilities in the Gogs Git service and abusing legitimate platforms like ChatGPT for malware distribution and phishing campaigns.

## Active Exploitation Details

### PAN-OS GlobalProtect Authentication Bypass
- **Description**: A medium-severity security flaw affecting PAN-OS and Prisma Access systems that allows attackers to bypass authentication mechanisms
- **Impact**: Unauthorized access to network resources and potential lateral movement within enterprise networks
- **Status**: Under active exploitation in the wild, recently disclosed by Palo Alto Networks
- **CVE ID**: CVE-2026-0257

### FortiClient EMS Authentication Bypass
- **Description**: An authentication bypass vulnerability in FortiClient Enterprise Management Server that allows unauthorized access to the system
- **Impact**: Enables deployment of infostealer malware, specifically the undocumented EKZ credential stealer, compromising user credentials and sensitive data
- **Status**: Actively exploited by threat actors to distribute malware
- **CVE ID**: CVE-2026-35616

### Marimo Platform Exploitation
- **Description**: A vulnerability in publicly-accessible Marimo installations that provides initial access to attackers
- **Impact**: Remote code execution and system compromise, with attackers using LLM agents for sophisticated post-exploitation activities
- **Status**: Exploited in the wild with novel post-compromise techniques involving AI agents
- **CVE ID**: CVE-2026-39987

### Gogs Git Service RCE
- **Description**: A critical remote code execution vulnerability in the open-source self-hosted Git service Gogs
- **Impact**: Allows any authenticated user to execute arbitrary code under certain conditions, leading to complete system compromise
- **Status**: Critical vulnerability affecting popular Git hosting platform

### ChatGPT Platform Abuse
- **Description**: Exploitation of ChatGPT's content-sharing feature and web summary functionality for malicious purposes
- **Impact**: Hosting fake outage pages to deliver malware and creating phishing surfaces through manipulation of AI-generated content
- **Status**: Active abuse of legitimate AI platform features for malicious distribution

## Affected Systems and Products

- **Palo Alto Networks**: PAN-OS and Prisma Access systems vulnerable to authentication bypass
- **Fortinet**: FortiClient Enterprise Management Server affected by authentication bypass flaw
- **Marimo Platform**: Publicly-accessible installations compromised for initial access
- **Gogs Git Service**: Open-source self-hosted Git repositories at risk of remote code execution
- **OpenAI ChatGPT**: Content-sharing and web summary features exploited for malware distribution
- **Charter Communications**: 4.9 million customer accounts compromised by ShinyHunters extortion gang
- **Android Devices**: Targeted by BTMOB remote access trojan through custom phishing payloads

## Attack Vectors and Techniques

- **Authentication Bypass**: Exploitation of authentication flaws in enterprise security and management platforms
- **AI-Powered Post-Exploitation**: Use of large language model agents to conduct sophisticated post-compromise activities
- **Legitimate Platform Abuse**: Leveraging trusted AI platforms like ChatGPT for malware hosting and phishing
- **Supply Chain Attacks**: Malicious NuGet and npm packages targeting developers and cloud environments
- **Custom Malware Distribution**: Development of tailored Android trojans with builder interfaces for generating specific payloads
- **Social Engineering**: AI-generated lures and content for enhanced phishing campaigns

## Threat Actor Activities

- **GREYVIBE**: Russian-linked threat actor conducting persistent attacks against Ukraine using AI-powered tools including ChatGPT and Gemini for cyberattacks since August 2025
- **Kimsuky (Velvet Chollima)**: North Korean state-sponsored group deploying HTTPSpy malware and expanding arsenal with HelloDoor and VS Code Tunnels against South Korean military and corporate entities
- **ShinyHunters**: Extortion gang responsible for Charter Communications breach affecting 4.9 million accounts
- **Unknown LLM-Using Actor**: Threat actor leveraging large language model agents for post-exploitation activities following Marimo platform compromise
- **The Com Criminal Gang**: Neo-Nazi-affiliated cybercriminal organization using cyber proceeds to support violence and exploitation activities
- **BTMOB Operators**: Cybercriminals offering Android RAT as a service with custom payload generation capabilities