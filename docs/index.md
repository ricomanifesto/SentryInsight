# Exploitation Report

The cybersecurity landscape is currently experiencing heightened exploitation activity across multiple attack vectors, with threat actors leveraging both zero-day vulnerabilities and recently patched flaws to conduct sophisticated campaigns. Critical exploitation activity includes a maximum-severity CVSS 10.0 remote code execution vulnerability in Flowise AI Agent Builder with over 12,000 exposed instances, multiple FortiClient vulnerabilities being actively exploited including CVE-2026-35616, and a Windows privilege escalation zero-day exploit dubbed "BlueHammer" that has been publicly leaked. China-linked threat actor Storm-1175 is conducting high-velocity ransomware attacks using a combination of zero-day and N-day exploits, while threat actors are exploiting React2Shell vulnerability CVE-2025-55182 in automated credential harvesting campaigns against Next.js applications.

## Active Exploitation Details

### Flowise AI Agent Builder Remote Code Execution
- **Description**: A maximum-severity security flaw in the open-source Flowise AI platform that enables remote code execution
- **Impact**: Complete system compromise with potential for lateral movement across AI infrastructure
- **Status**: Under active exploitation with over 12,000 instances exposed globally
- **CVE ID**: CVSS 10.0 severity rating

### FortiClient Enterprise Management Server Authentication Bypass
- **Description**: An authentication bypass vulnerability in FortiClient EMS that allows unauthorized access to management systems
- **Impact**: Unauthorized access to enterprise management systems and potential network compromise
- **Status**: Actively exploited in the wild, emergency patch released
- **CVE ID**: CVE-2026-35616

### Windows BlueHammer Privilege Escalation
- **Description**: An unpatched Windows privilege escalation vulnerability that has been publicly disclosed by a disgruntled researcher
- **Impact**: Attackers can gain SYSTEM or elevated administrator permissions on Windows systems
- **Status**: Zero-day status with public exploit code available, no patch currently available

### React2Shell Next.js Vulnerability
- **Description**: A vulnerability in Next.js applications that enables unauthorized access and data exfiltration
- **Impact**: Credential harvesting, secrets extraction, and system data compromise
- **Status**: Being exploited in large-scale automated campaigns
- **CVE ID**: CVE-2025-55182

## Affected Systems and Products

- **Flowise AI Agent Builder**: Open-source AI platform with over 12,000 exposed instances globally
- **FortiClient Enterprise Management Server**: Enterprise management systems requiring immediate patching
- **Windows Systems**: All versions affected by the BlueHammer privilege escalation vulnerability
- **Next.js Applications**: Web applications using vulnerable Next.js framework versions
- **Microsoft 365 Environments**: Over 300 Israeli organizations targeted in password-spraying campaigns
- **GPU Systems**: GDDR6 memory systems vulnerable to GPUBreach rowhammer attacks
- **GitHub Repositories**: Multiple supply chain attack vectors targeting open-source projects

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Storm-1175 and other threat actors weaponizing unpatched vulnerabilities for rapid deployment
- **High-Velocity Attacks**: Combination of zero-day and N-day exploits for accelerated compromise timelines
- **Automated Credential Harvesting**: Large-scale automated tools exploiting React2Shell for systematic data exfiltration
- **Password Spraying**: Mass credential attacks against Microsoft 365 environments using distributed infrastructure
- **Supply Chain Attacks**: AI-assisted targeting of GitHub repositories and package maintainers
- **BYOVD Techniques**: Bring Your Own Vulnerable Driver methods to disable over 300 EDR security tools
- **GPU Rowhammer**: Novel GPUBreach attack inducing bit-flips in GPU memory for privilege escalation
- **Social Engineering**: Sophisticated six-month operations targeting cryptocurrency platforms

## Threat Actor Activities

- **Storm-1175 (China-linked)**: Deploying Medusa ransomware through zero-day and N-day exploit combinations in high-velocity attack campaigns
- **UAT-10608**: Emerging threat cluster conducting automated credential harvesting campaigns against vulnerable Next.js applications
- **Iran-nexus Actors**: Conducting large-scale password-spraying campaigns targeting over 300 Israeli Microsoft 365 organizations amid regional conflicts
- **DPRK-linked Groups**: Using GitHub as command-and-control infrastructure in multi-stage attacks against South Korean organizations and conducting sophisticated social engineering operations against cryptocurrency platforms
- **Qilin Ransomware**: Employing BYOVD techniques to disable security tools and deploy ransomware payloads
- **Warlock Ransomware**: Utilizing vulnerable drivers to circumvent endpoint detection and response systems
- **REvil/GandCrab Operations**: Historical ransomware operations with leadership identities revealed by German authorities, responsible for over 130 attacks in Germany alone