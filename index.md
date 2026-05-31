# Exploitation Report

Critical vulnerability exploitation activity is currently affecting enterprise networks across multiple platforms. Palo Alto Networks GlobalProtect VPN systems are under active attack through CVE-2026-0257, an authentication bypass flaw that allows attackers to breach corporate networks. Simultaneously, FortiClient Enterprise Management Server deployments face exploitation of CVE-2026-35616, being leveraged to distribute credential stealing malware. Additionally, a newly discovered Linux kernel privilege escalation vulnerability dubbed 'CIFSwitch' threatens multiple distributions, while threat actors are exploiting Marimo framework vulnerabilities (CVE-2026-39987) and employing AI-powered post-exploitation techniques.

## Active Exploitation Details

### PAN-OS GlobalProtect Authentication Bypass
- **Description**: A medium-severity authentication bypass vulnerability in Palo Alto Networks PAN-OS and Prisma Access that allows attackers to circumvent authentication mechanisms
- **Impact**: Enables unauthorized access to corporate networks through compromised VPN endpoints
- **Status**: Under active exploitation in the wild; patches available from Palo Alto Networks
- **CVE ID**: CVE-2026-0257

### FortiClient EMS Authentication Bypass
- **Description**: Authentication bypass vulnerability in FortiClient Enterprise Management Server allowing attackers to gain unauthorized access to the management interface
- **Impact**: Attackers can deploy credential stealing malware and compromise managed endpoints
- **Status**: Actively exploited to deliver EKZ infostealer malware
- **CVE ID**: CVE-2026-35616

### CIFSwitch Linux Kernel Privilege Escalation
- **Description**: Local privilege escalation vulnerability in the Linux kernel that allows attackers to forge CIFS authentication key descriptions and abuse the kernel's key request mechanism
- **Impact**: Attackers can escalate privileges to root access on affected Linux distributions
- **Status**: Newly discovered vulnerability affecting multiple Linux distributions

### Marimo Framework Exploitation
- **Description**: Vulnerability in the publicly-accessible Marimo framework being exploited for initial access
- **Impact**: Provides entry point for sophisticated post-compromise activities using AI agents
- **Status**: Under active exploitation with AI-powered post-exploitation techniques
- **CVE ID**: CVE-2026-39987

## Affected Systems and Products

- **Palo Alto PAN-OS**: GlobalProtect VPN implementations and Prisma Access services
- **FortiClient EMS**: Enterprise Management Server deployments across corporate networks
- **Linux Distributions**: Multiple distributions affected by CIFSwitch kernel vulnerability
- **Marimo Framework**: Publicly accessible instances of the data science framework
- **ChatGPT Platform**: Web summary and content sharing features vulnerable to phishing abuse
- **NuGet Packages**: Malicious packages targeting Brazilian banking systems (Sicoob)
- **npm Packages**: Compromised packages targeting cloud secrets and credentials

## Attack Vectors and Techniques

- **VPN Authentication Bypass**: Exploitation of GlobalProtect authentication mechanisms to gain network access
- **Management Server Compromise**: Leveraging FortiClient EMS vulnerabilities to deploy malware across managed endpoints
- **AI-Powered Post-Exploitation**: Use of large language model agents for automated post-compromise activities
- **Supply Chain Attacks**: Malicious packages distributed through NuGet and npm repositories
- **Social Engineering**: ChatGPT content sharing features abused to create convincing phishing pages
- **Privilege Escalation**: Kernel-level exploitation for root access on Linux systems

## Threat Actor Activities

- **GreyVibe**: Russian-linked threat group targeting Ukrainian entities using AI-generated lures and custom malware tools, leveraging ChatGPT and Google Gemini for attack operations
- **Kimsuky (Velvet Chollima)**: North Korean state-sponsored group deploying HTTPSpy backdoor and expanding arsenal with HelloDoor and VS Code tunnels to target South Korean military and corporate entities
- **The Com Criminal Gang**: Neo-Nazi-affiliated cybercriminal organization using cyber profits to support violent activities and sexploitation
- **ShinyHunters**: Extortion gang responsible for breaching Charter Communications and stealing data from 4.9 million customer accounts
- **BTMOB Operators**: Android malware service providers offering custom phishing payload generation for cybercriminals