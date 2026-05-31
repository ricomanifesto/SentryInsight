# Exploitation Report

Multiple critical vulnerabilities are currently under active exploitation, presenting significant risks to enterprise networks and global infrastructure. The most concerning activity involves authentication bypass flaws in enterprise VPN solutions, privilege escalation vulnerabilities in Linux systems, and sophisticated AI-powered attack campaigns. Threat actors are exploiting enterprise management platforms to deploy information stealing malware, while state-sponsored groups are leveraging artificial intelligence to enhance their attack capabilities against geopolitical targets.

## Active Exploitation Details

### Palo Alto GlobalProtect Authentication Bypass
- **Description**: A medium-severity authentication bypass vulnerability in PAN-OS GlobalProtect and Prisma Access systems that allows unauthorized network access
- **Impact**: Attackers can bypass authentication mechanisms to breach corporate networks and gain unauthorized access to enterprise VPN infrastructure
- **Status**: Currently under active exploitation in the wild with patches available
- **CVE ID**: CVE-2026-0257

### CIFSwitch Linux Privilege Escalation
- **Description**: A local privilege escalation vulnerability in the Linux kernel affecting multiple distributions, allowing attackers to forge CIFS authentication key descriptions and abuse the kernel's key request mechanism
- **Impact**: Attackers can escalate privileges to root access on compromised Linux systems across multiple distributions
- **Status**: Newly discovered vulnerability with exploitation capabilities demonstrated

### Marimo Post-Exploitation Framework
- **Description**: A vulnerability being exploited by threat actors who subsequently deploy large language model (LLM) agents for post-compromise activities
- **Impact**: Enables sophisticated post-exploitation operations using AI-powered automation for lateral movement and data exfiltration
- **Status**: Under active exploitation with novel LLM-based post-compromise techniques observed
- **CVE ID**: CVE-2026-39987

### FortiClient EMS Authentication Bypass
- **Description**: An authentication bypass vulnerability in FortiClient Enterprise Management Server affecting enterprise security management infrastructure
- **Impact**: Attackers can deploy undocumented credential stealer malware called EKZ to harvest authentication credentials from enterprise environments
- **Status**: Currently being exploited to distribute information stealing malware
- **CVE ID**: CVE-2026-35616

## Affected Systems and Products

- **Palo Alto Networks PAN-OS**: GlobalProtect VPN and Prisma Access platforms affected by authentication bypass
- **Linux Kernel**: Multiple distributions vulnerable to CIFSwitch privilege escalation via CIFS authentication mechanisms
- **Marimo Framework**: Publicly-accessible instances being targeted for initial access and LLM-powered post-exploitation
- **FortiClient EMS**: Enterprise Management Server platforms targeted for credential theft operations
- **OpenAI ChatGPT**: Web summary features exploited via ChatGPhish vulnerability for phishing attacks
- **Android Devices**: BTMOB malware targeting mobile platforms through custom phishing payloads

## Attack Vectors and Techniques

- **VPN Authentication Bypass**: Exploitation of authentication mechanisms in enterprise VPN solutions to gain network access
- **Kernel Privilege Escalation**: Local exploitation of Linux kernel vulnerabilities to achieve root-level system compromise
- **AI-Enhanced Social Engineering**: Use of ChatGPT and Google Gemini to generate convincing phishing lures and attack content
- **Package Repository Poisoning**: Malicious NuGet packages targeting Brazilian banking credentials and npm packages stealing cloud secrets
- **Enterprise Management Exploitation**: Targeting of centralized management platforms to deploy information stealing malware
- **Phishing-as-a-Service**: Custom Android malware builders generating tailored phishing payloads for cybercriminal operations

## Threat Actor Activities

- **GreyVibe (Russia-linked)**: Conducting AI-powered cyberattacks against Ukrainian entities using ChatGPT and Google Gemini for content generation since August 2025
- **Kimsuky (North Korean APT)**: Deploying HTTPSpy malware and expanding arsenal with HelloDoor backdoors and VS Code tunnels targeting South Korean military and corporate entities
- **The Com Criminal Gang**: Neo-Nazi-affiliated group using cyber proceeds to fund violent activities and sexual exploitation operations
- **ShinyHunters**: Extortion gang responsible for Charter Communications breach affecting 4.9 million customer accounts
- **Unknown LLM-Powered Actor**: Novel threat group utilizing large language model agents for post-exploitation activities following Marimo framework compromise
- **Brazilian Banking Fraudsters**: Targeting Sicoob financial cooperative customers through malicious SDK packages designed to steal banking credentials