# Exploitation Report

Critical exploitation activity is currently focused on several high-impact vulnerabilities being actively targeted by threat actors. A China-linked group known as Storm-1175 is weaponizing zero-day vulnerabilities to deploy Medusa ransomware in high-velocity attacks. Meanwhile, multiple AI platforms are under siege, with Flowise AI Agent Builder facing active exploitation through a maximum-severity remote code execution flaw, and over 1,000 ComfyUI instances being targeted for cryptocurrency mining operations. Additionally, Fortinet products are experiencing continued exploitation pressure with a newly disclosed FortiClient authentication bypass vulnerability, and threat actors are leveraging sophisticated social engineering and AI-assisted techniques to target GitHub and other supply chain components.

## Active Exploitation Details

### Flowise AI Agent Builder Remote Code Execution
- **Description**: A maximum-severity security flaw in Flowise, an open-source artificial intelligence platform, is being actively exploited by threat actors
- **Impact**: Remote code execution allowing complete system compromise
- **Status**: Under active exploitation with over 12,000 instances exposed globally
- **CVE ID**: CVSS 10.0 severity rating confirmed

### ComfyUI Cryptomining Botnet Campaign
- **Description**: Internet-exposed instances of ComfyUI, a popular stable diffusion platform, are being targeted for enrollment into a cryptocurrency mining and proxy botnet
- **Impact**: Unauthorized resource consumption and potential data exfiltration through proxy operations
- **Status**: Active campaign with over 1,000 instances compromised

### FortiClient Authentication Bypass
- **Description**: An authentication bypass vulnerability in Fortinet's FortiClient Enterprise Management Server
- **Impact**: Unauthorized access to enterprise management systems
- **Status**: Actively exploited in the wild, emergency patch issued by Fortinet
- **CVE ID**: CVE-2026-35616

### BlueHammer Windows Privilege Escalation
- **Description**: An unpatched Windows privilege escalation vulnerability with public exploit code
- **Impact**: Allows attackers to gain SYSTEM or elevated administrator permissions
- **Status**: Zero-day with exploit code publicly released by disgruntled researcher

### React2Shell Vulnerability in Next.js Applications
- **Description**: A vulnerability affecting web-exposed Next.js applications being exploited for automated credential harvesting
- **Impact**: Theft of credentials, secrets, and system data through automated tools
- **Status**: Active exploitation by threat cluster UAT-10608

### GPUBreach Attack Vector
- **Description**: A new attack method exploiting RowHammer bit-flips on GPU GDDR6 memories
- **Impact**: Privilege escalation and potential full system compromise through GPU memory manipulation
- **Status**: Proof-of-concept demonstrated, enables CPU privilege escalation via graphics cards

## Affected Systems and Products

- **Flowise AI Platform**: Open-source artificial intelligence agent builder with 12,000+ exposed instances
- **ComfyUI**: Stable diffusion platform with over 1,000 compromised instances
- **Fortinet FortiClient EMS**: Enterprise management server systems requiring immediate patching
- **Windows Systems**: All versions affected by BlueHammer privilege escalation vulnerability
- **Next.js Applications**: Web applications using React framework exposed to credential harvesting
- **GPU Systems**: High-performance graphics processing units with GDDR6 memory vulnerable to RowHammer attacks
- **Microsoft 365**: Over 300 Israeli organizations targeted in password spraying campaigns
- **GitHub Repositories**: Supply chain targets for AI-assisted attacks and social engineering

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Combination of zero-day and N-day vulnerabilities used for rapid deployment
- **Cryptomining Botnet**: Automated enrollment of compromised systems into mining operations
- **Authentication Bypass**: Direct circumvention of security controls in enterprise management systems
- **Privilege Escalation**: Local elevation of privileges through memory manipulation techniques
- **Automated Credential Harvesting**: Systematic extraction of authentication materials from web applications
- **RowHammer Attacks**: Memory corruption techniques targeting GPU hardware
- **Password Spraying**: Large-scale credential guessing attacks against cloud environments
- **Social Engineering**: Sophisticated manipulation targeting software maintainers and developers
- **AI-Assisted Targeting**: Automated identification and exploitation of GitHub misconfigurations
- **Supply Chain Attacks**: Targeting of package maintainers and development infrastructure

## Threat Actor Activities

- **Storm-1175**: China-based financially motivated group deploying Medusa ransomware through zero-day exploitation in high-velocity attacks
- **UAT-10608**: Emerging threat cluster conducting automated credential harvesting campaigns against Next.js applications
- **Iran-Nexus Actor**: Password spraying campaign targeting over 300 Israeli Microsoft 365 organizations amid Middle East conflict
- **DPRK-Linked Groups**: North Korean threat actors using GitHub as command-and-control infrastructure in multi-stage attacks targeting South Korean organizations
- **REvil/GandCrab Operations**: German authorities have identified Russian nationals as leaders of major ransomware operations between 2019-2021
- **Axios Package Attackers**: Sophisticated social engineering campaign targeting NPM package maintainers demonstrating industrialized approach to supply chain compromise