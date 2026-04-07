# Exploitation Report

Critical vulnerability exploitation activity is dominated by several zero-day and recently disclosed flaws being actively exploited in the wild. The most severe threats include a newly discovered FortiClient EMS authentication bypass vulnerability (CVE-2026-35616) that prompted emergency patching, a leaked Windows privilege escalation zero-day known as "BlueHammer," and widespread exploitation of the React2Shell vulnerability (CVE-2025-55182) in automated credential harvesting campaigns. Nation-state actors are leveraging sophisticated social engineering operations, including a six-month DPRK campaign that resulted in a $285 million cryptocurrency theft, while ransomware groups are using vulnerable drivers to disable over 300 endpoint detection and response tools.

## Active Exploitation Details

### FortiClient EMS Authentication Bypass Vulnerability
- **Description**: Critical authentication bypass flaw in FortiClient Enterprise Management Server that allows attackers to circumvent security controls
- **Impact**: Complete system compromise and unauthorized access to enterprise management infrastructure
- **Status**: Actively exploited in the wild; emergency patch released by Fortinet
- **CVE ID**: CVE-2026-35616

### BlueHammer Windows Zero-Day
- **Description**: Unpatched Windows privilege escalation vulnerability that was privately reported to Microsoft but remains unfixed
- **Impact**: Allows attackers to gain SYSTEM or elevated administrator permissions on Windows systems
- **Status**: Exploit code has been publicly leaked by a disgruntled researcher; no patch currently available

### React2Shell Vulnerability
- **Description**: Vulnerability in Next.js applications that enables automated credential and data exfiltration
- **Impact**: Large-scale credential theft, secret extraction, and system data compromise
- **Status**: Actively exploited in automated campaigns by threat cluster UAT-10608
- **CVE ID**: CVE-2025-55182

### Chrome Zero-Day Vulnerability
- **Description**: Unspecified zero-day vulnerability affecting Google Chrome browser
- **Impact**: Browser-based attacks and potential system compromise
- **Status**: Recently disclosed and being actively exploited

## Affected Systems and Products

- **FortiClient Enterprise Management Server**: Critical authentication bypass affecting enterprise security infrastructure
- **Windows Operating Systems**: Privilege escalation vulnerability affecting all Windows versions
- **Next.js Applications**: Web applications vulnerable to automated credential harvesting attacks
- **Google Chrome Browser**: Zero-day vulnerability affecting browser security
- **Microsoft 365 Environments**: Targeted by Iran-linked password spraying campaigns affecting 300+ Israeli organizations
- **Redis and PostgreSQL Databases**: Exploited by malicious npm packages for persistent implant deployment
- **npm Package Registry**: 36 malicious packages disguised as Strapi CMS plugins targeting developers

## Attack Vectors and Techniques

- **Authentication Bypass**: Exploiting critical flaws in FortiClient EMS to gain unauthorized access
- **Privilege Escalation**: Using BlueHammer zero-day to elevate permissions on Windows systems
- **Automated Credential Harvesting**: Large-scale exploitation of React2Shell for systematic credential theft
- **Password Spraying**: Iran-linked actors targeting Microsoft 365 environments with credential attacks
- **Social Engineering**: Sophisticated six-month DPRK operation targeting cryptocurrency platforms
- **Supply Chain Attacks**: Malicious npm packages and compromised maintainer accounts (Axios incident)
- **BYOVD (Bring Your Own Vulnerable Driver)**: Ransomware groups using vulnerable drivers to disable EDR tools
- **Device Code Phishing**: OAuth 2.0 abuse with 37x increase in attacks using device authorization flows
- **QR Code Phishing**: Traffic violation scams incorporating QR codes to bypass traditional security measures

## Threat Actor Activities

- **Storm-1175 (China-based)**: Medusa ransomware affiliate deploying zero-day and n-day exploits in high-velocity attacks
- **UAT-10608**: Emerging threat cluster exploiting React2Shell in automated credential harvesting campaigns
- **Iran-linked Actors**: Conducting password spraying campaigns against 300+ Israeli Microsoft 365 organizations amid Middle East conflict
- **DPRK-linked Groups**: Using GitHub as C2 infrastructure in multi-stage attacks targeting South Korean organizations; executed sophisticated six-month social engineering operation resulting in $285 million Drift Protocol theft
- **Qilin Ransomware**: Using vulnerable drivers to disable 300+ EDR tools on compromised hosts
- **Warlock Ransomware**: Employing BYOVD techniques to silence security tools during ransomware deployment
- **REvil/Sodinokibi Leaders**: Key figures identified by German authorities behind 130 German ransomware attacks, including "UNKN" (Daniil Maksimov)