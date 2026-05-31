# Exploitation Report

Critical exploitation activity is currently targeting multiple enterprise infrastructure components, with attackers leveraging authentication bypass vulnerabilities and privilege escalation flaws to compromise corporate networks. The most severe ongoing exploitation involves Palo Alto Networks GlobalProtect VPN systems through CVE-2026-0257, which allows attackers to bypass authentication mechanisms and gain unauthorized network access. Additionally, threat actors are exploiting FortiClient Enterprise Management Server vulnerabilities (CVE-2026-35616) to deploy credential-stealing malware, while a newly discovered Linux kernel privilege escalation vulnerability dubbed 'CIFSwitch' poses significant risks across multiple distributions. State-sponsored groups, including the newly identified Russian-linked GREYVIBE cluster, are incorporating AI-powered tools into their attack campaigns, demonstrating the evolving sophistication of modern cyber operations.

## Active Exploitation Details

### Palo Alto GlobalProtect Authentication Bypass
- **Description**: Authentication bypass vulnerability in PAN-OS GlobalProtect and Prisma Access that allows attackers to circumvent authentication mechanisms
- **Impact**: Unauthorized access to corporate VPN infrastructure and potential lateral movement within enterprise networks
- **Status**: Under active exploitation in the wild, patches available from Palo Alto Networks
- **CVE ID**: CVE-2026-0257

### FortiClient EMS Authentication Bypass
- **Description**: Authentication bypass flaw in FortiClient Enterprise Management Server that enables unauthorized access to management functions
- **Impact**: Deployment of credential-stealing malware and compromise of endpoint management infrastructure
- **Status**: Actively exploited to deliver EKZ infostealer malware
- **CVE ID**: CVE-2026-35616

### CIFSwitch Linux Privilege Escalation
- **Description**: Local privilege escalation vulnerability in the Linux kernel that allows attackers to forge CIFS authentication key descriptions and abuse kernel key request mechanisms
- **Impact**: Root-level access on multiple Linux distributions, complete system compromise
- **Status**: Newly discovered vulnerability affecting multiple Linux distributions

### Marimo Application Vulnerability
- **Description**: Security flaw in publicly-accessible Marimo applications that allows initial access compromise
- **Impact**: Initial foothold for attackers to conduct post-exploitation activities using AI agents
- **Status**: Exploited by unknown threat actors for post-compromise operations
- **CVE ID**: CVE-2026-39987

## Affected Systems and Products

- **Palo Alto Networks PAN-OS**: GlobalProtect VPN and Prisma Access implementations
- **FortiClient Enterprise Management Server**: Endpoint management infrastructure
- **Linux Kernel**: Multiple distributions affected by CIFSwitch vulnerability
- **Marimo Applications**: Publicly-accessible instances vulnerable to exploitation
- **ChatGPT Shared Links**: Abused for hosting fake outage pages and malware distribution
- **NuGet Packages**: Malicious packages targeting Brazilian financial systems
- **NPM Packages**: Malicious packages targeting cloud secrets and credentials

## Attack Vectors and Techniques

- **VPN Authentication Bypass**: Exploitation of GlobalProtect authentication mechanisms to gain network access
- **Management Server Compromise**: Targeting enterprise management servers to deploy malware
- **Privilege Escalation**: Using kernel vulnerabilities to gain root access on Linux systems
- **AI-Powered Social Engineering**: Using ChatGPT and Gemini to generate convincing phishing lures
- **Package Repository Poisoning**: Deploying malicious packages in NuGet and NPM repositories
- **Shared Link Abuse**: Leveraging ChatGPT content-sharing features for malware distribution
- **Post-Exploitation AI Agents**: Using large language models for automated post-compromise activities

## Threat Actor Activities

- **GREYVIBE**: Russian-linked threat cluster targeting Ukrainian entities using AI-generated lures and custom malware tools, operating since August 2025
- **Kimsuky (Velvet Chollima)**: North Korean state-sponsored group deploying HTTPSpy, HelloDoor, and VS Code Tunnels against South Korean military and corporate targets
- **ShinyHunters**: Extortion gang responsible for Charter Communications breach affecting 4.9 million accounts
- **Unknown LLM-Using Actors**: Threat actors leveraging large language model agents for post-exploitation activities following Marimo application compromises
- **Brazilian Banking Malware Operators**: Cybercriminals deploying malicious Sicoob NuGet packages to steal banking credentials
- **The Com Criminal Gang**: Neo-Nazi-affiliated cybercriminal organization supporting violence and exploitation through cyber operations