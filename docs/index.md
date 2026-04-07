# Exploitation Report

Critical exploitation activity is currently targeting multiple high-severity vulnerabilities across enterprise systems and development platforms. Most concerning is the active exploitation of a maximum-severity CVSS 10.0 remote code execution vulnerability in Flowise AI platform, with over 12,000 instances exposed globally. Fortinet systems face widespread attacks through an authentication bypass flaw in FortiClient Enterprise Management Server, prompting CISA to issue emergency patching orders for federal agencies. Additionally, threat actors are exploiting React2Shell vulnerabilities in Next.js applications for automated credential harvesting, while a leaked Windows privilege escalation zero-day exploit called "BlueHammer" poses immediate risks to Windows environments.

## Active Exploitation Details

### Flowise AI Platform RCE Vulnerability
- **Description**: A maximum-severity security flaw in Flowise, an open-source artificial intelligence platform that allows remote code execution
- **Impact**: Complete system compromise with CVSS 10.0 rating, affecting over 12,000 exposed instances globally
- **Status**: Currently under active exploitation by threat actors

### FortiClient EMS Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in FortiClient Enterprise Management Server
- **Impact**: Unauthorized access to enterprise management systems, allowing attackers to bypass authentication mechanisms
- **Status**: Actively exploited in attacks, emergency patch released by Fortinet
- **CVE ID**: CVE-2026-35616

### React2Shell Next.js Vulnerability
- **Description**: Vulnerability in Next.js applications that enables automated exploitation of web-exposed applications
- **Impact**: Credential harvesting, secrets exfiltration, and system data theft through automated tools
- **Status**: Under active exploitation in large-scale automated campaigns
- **CVE ID**: CVE-2025-55182

### BlueHammer Windows Zero-Day
- **Description**: Unpatched Windows privilege escalation vulnerability with publicly released exploit code
- **Impact**: Allows attackers to gain SYSTEM or elevated administrator permissions on Windows systems
- **Status**: Exploit code publicly leaked, vulnerability remains unpatched by Microsoft

## Affected Systems and Products

- **Flowise AI Platform**: Open-source AI platform with 12,000+ exposed instances globally
- **FortiClient Enterprise Management Server**: Enterprise management systems across federal agencies and organizations
- **Next.js Applications**: Web-exposed applications using the Next.js framework
- **Windows Operating Systems**: All versions affected by the BlueHammer privilege escalation flaw
- **GPU Systems**: Graphics processing units with GDDR6 memory vulnerable to GPUBreach rowhammer attacks
- **npm Registry**: 36 malicious packages targeting Redis and PostgreSQL databases
- **GitHub Repositories**: Supply chain attacks targeting maintainers and repository configurations

## Attack Vectors and Techniques

- **Remote Code Execution**: Direct exploitation of Flowise AI platform for complete system compromise
- **Authentication Bypass**: Circumventing FortiClient EMS security controls to gain unauthorized access
- **Automated Credential Harvesting**: Large-scale automated tools exploiting React2Shell for credential theft
- **Privilege Escalation**: BlueHammer exploit enabling elevation to SYSTEM privileges on Windows
- **GPU Rowhammer**: GPUBreach technique using bit-flips on GPU memory to escalate privileges
- **Supply Chain Compromise**: Malicious npm packages disguised as legitimate Strapi CMS plugins
- **Social Engineering**: Sophisticated multi-month operations targeting cryptocurrency platforms
- **Bring Your Own Vulnerable Driver (BYOVD)**: Ransomware operators using vulnerable drivers to disable EDR tools

## Threat Actor Activities

- **Storm-1175**: China-based cybercriminal group deploying Medusa ransomware with n-day and zero-day exploits
- **UAT-10608**: Emerging threat cluster conducting automated credential harvesting campaigns using React2Shell
- **Iran-Nexus Actors**: Password-spraying campaigns targeting 300+ Israeli Microsoft 365 organizations
- **DPRK-Linked Groups**: Using GitHub as command-and-control infrastructure in multi-stage attacks targeting South Korea
- **Qilin Ransomware**: Employing BYOVD techniques to disable over 300 EDR security tools
- **Warlock Ransomware**: Utilizing vulnerable drivers to silence security tools on compromised hosts
- **REvil/GandCrab Operations**: German authorities identified Russian nationals leading major ransomware campaigns between 2019-2021
- **Cryptocurrency Threat Actors**: Six-month social engineering operation resulting in $285 million Drift Protocol theft