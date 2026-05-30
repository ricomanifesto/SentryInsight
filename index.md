# Exploitation Report

Critical vulnerabilities are being actively exploited across multiple platforms, with threat actors leveraging authentication bypass flaws, privilege escalation vulnerabilities, and AI-powered attack techniques. The most concerning developments include active exploitation of PAN-OS GlobalProtect authentication bypass (CVE-2026-0257), a local privilege escalation flaw dubbed 'CIFSwitch' in Linux kernels, and the weaponization of AI chatbots for sophisticated attack campaigns. Notable threat actors including GREYVIBE and Kimsuky are deploying advanced techniques, while cybercriminals are exploiting authentication bypass vulnerabilities in enterprise management systems to deliver credential-stealing malware.

## Active Exploitation Details

### PAN-OS GlobalProtect Authentication Bypass
- **Description**: A medium-severity authentication bypass vulnerability affecting PAN-OS and Prisma Access systems
- **Impact**: Allows attackers to bypass authentication mechanisms in GlobalProtect VPN solutions
- **Status**: Under active exploitation in the wild, patch available from Palo Alto Networks
- **CVE ID**: CVE-2026-0257

### CIFSwitch Linux Privilege Escalation
- **Description**: A local privilege escalation vulnerability in the Linux kernel that allows attackers to forge CIFS authentication key descriptions and abuse the kernel's key request mechanism
- **Impact**: Enables attackers to gain root privileges on multiple Linux distributions
- **Status**: Recently discovered vulnerability affecting multiple distributions

### FortiClient EMS Authentication Bypass
- **Description**: An authentication bypass vulnerability in FortiClient Enterprise Management Server
- **Impact**: Allows attackers to deliver infostealer malware, specifically the undocumented EKZ credential stealer
- **Status**: Under active exploitation by threat actors
- **CVE ID**: CVE-2026-35616

### Marimo Vulnerability Exploitation
- **Description**: A publicly-accessible vulnerability being exploited for initial access
- **Impact**: Used by threat actors to gain initial compromise before deploying LLM agents for post-exploitation activities
- **Status**: Active exploitation observed with AI-powered post-compromise techniques
- **CVE ID**: CVE-2026-39987

### Gogs Remote Code Execution
- **Description**: A critical vulnerability in the open-source self-hosted Git service Gogs that allows authenticated users to execute arbitrary code
- **Impact**: Any authenticated user can achieve remote code execution under certain conditions
- **Status**: Critical severity vulnerability requiring immediate patching

## Affected Systems and Products

- **Palo Alto Networks PAN-OS**: GlobalProtect VPN solutions and Prisma Access cloud security platforms
- **Linux Distributions**: Multiple distributions affected by CIFSwitch privilege escalation vulnerability
- **FortiClient EMS**: Enterprise Management Server installations vulnerable to authentication bypass
- **Marimo Systems**: Publicly-accessible instances being targeted for initial access
- **Gogs Git Service**: Self-hosted Git service installations with authenticated user access
- **ChatGPT Platform**: Content-sharing features being abused for malware distribution
- **Android Devices**: Targeted by BTMOB malware service generating custom phishing payloads
- **NuGet Package Ecosystem**: Malicious packages targeting Brazilian banking credentials
- **npm Package Ecosystem**: Malicious packages targeting cloud secrets and credentials

## Attack Vectors and Techniques

- **Authentication Bypass**: Exploitation of authentication mechanisms in enterprise VPN and management solutions
- **Privilege Escalation**: Local privilege escalation through kernel vulnerability exploitation
- **AI-Powered Attacks**: Use of ChatGPT and Gemini for generating phishing content and conducting post-exploitation activities
- **Supply Chain Attacks**: Malicious packages in software repositories (NuGet, npm) targeting developers and organizations
- **Content Sharing Abuse**: Leveraging ChatGPT's content-sharing features to host fake outage pages and deliver malware
- **Phishing-as-a-Service**: Automated generation of custom Android malware payloads with phishing capabilities
- **LLM Agent Deployment**: Post-compromise use of large language model agents for advanced persistent threat activities

## Threat Actor Activities

- **GREYVIBE**: Russia-linked threat actor conducting AI-powered cyberattacks against Ukraine and Ukraine-related entities since August 2025, utilizing ChatGPT and Gemini for attack enhancement
- **Kimsuky (Velvet Chollima)**: North Korean state-sponsored group deploying HTTPSpy malware and expanding arsenal with HelloDoor and VS Code tunnels, targeting South Korean military and corporate entities
- **ShinyHunters**: Extortion gang responsible for Charter Communications breach affecting 4.9 million accounts
- **Unknown Threat Actor**: Exploiting Marimo vulnerability and deploying LLM agents for sophisticated post-exploitation activities
- **The Com Criminal Gang**: Neo-Nazi-affiliated cybercriminal organization supporting violence and exploitation through cyberattacks
- **Dutch Botnet Operators**: Massive botnet operation disrupted by authorities, affecting 17 million infected devices across 200+ servers