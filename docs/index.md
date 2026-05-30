# Exploitation Report

Critical exploitation activity is currently targeting enterprise VPN infrastructure and Linux systems with significant security implications. The most severe active exploitation involves Palo Alto Networks' GlobalProtect VPN authentication bypass vulnerability (CVE-2026-0257), which is being actively exploited by threat actors to breach corporate networks. Additionally, a newly discovered local privilege escalation flaw dubbed 'CIFSwitch' in the Linux kernel allows attackers to gain root access across multiple distributions. Threat actors are also exploiting FortiClient EMS authentication bypass vulnerabilities to deploy credential-stealing malware, while leveraging AI-powered tools for sophisticated post-exploitation activities. The emergence of AI-enhanced attack techniques, including the use of ChatGPT and Gemini for malware generation, represents a significant evolution in threat actor capabilities.

## Active Exploitation Details

### PAN-OS GlobalProtect Authentication Bypass
- **Description**: A medium-severity authentication bypass vulnerability in Palo Alto Networks' PAN-OS and Prisma Access GlobalProtect VPN solution that allows unauthorized network access
- **Impact**: Attackers can bypass authentication mechanisms to gain unauthorized access to corporate networks through VPN infrastructure
- **Status**: Under active exploitation in the wild, with Palo Alto Networks issuing warnings about ongoing attacks
- **CVE ID**: CVE-2026-0257

### CIFSwitch Linux Kernel Privilege Escalation
- **Description**: A newly discovered local privilege escalation vulnerability in the Linux kernel that allows attackers to forge CIFS authentication key descriptions and abuse the kernel's key request mechanism
- **Impact**: Enables attackers to escalate privileges to root access on compromised Linux systems across multiple distributions
- **Status**: Newly disclosed vulnerability affecting multiple Linux distributions with high impact potential

### FortiClient EMS Authentication Bypass
- **Description**: An authentication bypass vulnerability in FortiClient Enterprise Management Server that allows unauthorized access to management functions
- **Impact**: Enables deployment of credential-stealing malware and unauthorized access to enterprise management systems
- **Status**: Currently being exploited to deliver EKZ infostealer malware
- **CVE ID**: CVE-2026-35616

### Marimo Post-Exploitation Vulnerability
- **Description**: A vulnerability in publicly-accessible systems that provides initial access vectors for advanced persistent threat activities
- **Impact**: Used as entry point for LLM agent-powered post-compromise operations
- **Status**: Exploited in combination with AI-powered post-exploitation techniques
- **CVE ID**: CVE-2026-39987

## Affected Systems and Products

- **Palo Alto Networks PAN-OS**: GlobalProtect VPN components and Prisma Access services
- **Linux Kernel**: Multiple distributions affected by CIFSwitch vulnerability through CIFS filesystem implementation
- **FortiClient EMS**: Enterprise Management Server authentication systems
- **Marimo Systems**: Publicly-accessible instances vulnerable to initial compromise
- **ChatGPT Platform**: Content-sharing features being abused for malware distribution
- **Android Devices**: Targeted by BTMOB malware-as-a-service platform
- **NuGet Package Ecosystem**: Malicious packages targeting Brazilian banking credentials
- **npm Package Registry**: Packages designed to steal cloud secrets and credentials

## Attack Vectors and Techniques

- **VPN Authentication Bypass**: Direct exploitation of authentication mechanisms in enterprise VPN solutions
- **Kernel Privilege Escalation**: Local exploitation of Linux kernel vulnerabilities to gain root access
- **AI-Powered Social Engineering**: Use of ChatGPT and Gemini to generate convincing phishing lures and malware
- **Package Repository Poisoning**: Deployment of malicious packages in legitimate software repositories
- **LLM Agent Post-Exploitation**: Advanced post-compromise activities using large language model agents for automated operations
- **ChatGPT Content Sharing Abuse**: Leveraging legitimate platform features to host malicious content
- **Supply Chain Attacks**: Targeting software development ecosystems through malicious packages
- **Malware-as-a-Service**: Custom Android malware generation through automated builder interfaces

## Threat Actor Activities

- **GreyVibe (Russia-linked)**: Conducting AI-powered cyberattacks against Ukrainian entities since August 2025, utilizing ChatGPT and Gemini for malware generation and sophisticated lure creation
- **Kimsuky (North Korea)**: Deploying HTTPSpy malware and expanding arsenal with HelloDoor backdoors and VS Code tunnels against South Korean military and corporate targets
- **ShinyHunters**: Conducted major data breach against Charter Communications affecting 4.9 million accounts
- **Unknown Threat Actors**: Exploiting PAN-OS GlobalProtect vulnerabilities for corporate network breaches and utilizing LLM agents for post-exploitation activities following Marimo compromises
- **BTMOB Operators**: Providing malware-as-a-service platform for generating custom Android phishing payloads
- **Package Poisoners**: Targeting Brazilian banking systems through malicious NuGet packages and cloud infrastructure through npm package attacks