# Exploitation Report

Critical vulnerabilities are actively being exploited across multiple attack vectors, with notable zero-day exploitation and sophisticated social engineering campaigns. The most severe activity includes active exploitation of CVE-2026-35616 in Fortinet's FortiClient EMS requiring emergency patching, widespread credential theft campaigns targeting CVE-2025-55182 (React2Shell) vulnerabilities in Next.js applications, and sophisticated supply chain attacks targeting npm maintainers. Ransomware groups continue leveraging vulnerable drivers through BYOVD techniques to disable EDR tools, while North Korean threat actors have orchestrated complex multi-month social engineering operations resulting in significant financial losses and supply chain compromises.

## Active Exploitation Details

### FortiClient EMS Critical Vulnerability
- **Description**: Critical security flaw in FortiClient Enterprise Management Server actively exploited in the wild
- **Impact**: Allows attackers to compromise enterprise endpoint management infrastructure
- **Status**: Emergency patches released by Fortinet, active exploitation confirmed
- **CVE ID**: CVE-2026-35616

### React2Shell Vulnerability
- **Description**: Vulnerability in Next.js applications being exploited in large-scale automated campaigns
- **Impact**: Enables credential theft through automated exploitation methods
- **Status**: Active exploitation in widespread credential harvesting operations
- **CVE ID**: CVE-2025-55182

### Vulnerable Driver Exploitation (BYOVD)
- **Description**: Bring Your Own Vulnerable Driver technique used to disable endpoint detection and response tools
- **Impact**: Complete neutralization of security monitoring across 300+ EDR products
- **Status**: Actively used by multiple ransomware groups including Qilin and Warlock

## Affected Systems and Products

- **FortiClient EMS**: Enterprise Management Server infrastructure requiring immediate patching
- **Next.js Applications**: Web applications vulnerable to React2Shell exploitation
- **Windows Endpoints**: Targeted by BYOVD attacks disabling EDR protection
- **npm Registry**: Supply chain targeting through malicious packages and social engineering
- **Redis and PostgreSQL**: Database systems exploited through malicious npm packages
- **iOS and Android Devices**: Targeted by SparkCat malware variants for cryptocurrency theft
- **Linux Servers**: Compromised through cookie-controlled PHP web shells

## Attack Vectors and Techniques

- **BYOVD (Bring Your Own Vulnerable Driver)**: Ransomware groups loading vulnerable drivers to disable security tools
- **Social Engineering**: Multi-month targeted campaigns against software maintainers and developers
- **Supply Chain Compromise**: Malicious npm packages disguised as legitimate plugins
- **Automated Credential Harvesting**: Large-scale exploitation of React2Shell vulnerabilities
- **Cookie-Controlled Web Shells**: PHP-based remote code execution using HTTP cookies as control channels
- **Device Code Phishing**: OAuth 2.0 Device Authorization Grant flow abuse showing 37x increase
- **QR Code Phishing**: Traffic violation scams incorporating QR codes for mobile targeting

## Threat Actor Activities

- **UNC1069 (North Korean)**: Six-month social engineering operation against Axios maintainer resulting in npm supply chain attack
- **Qilin Ransomware**: Using BYOVD techniques and targeting German political organizations
- **Warlock Ransomware**: Employing vulnerable drivers to disable EDR systems
- **TA416 (China-linked)**: Targeting European government and diplomatic organizations with PlugX malware and OAuth-based phishing
- **DPRK Actors**: $285 million cryptocurrency theft through sophisticated social engineering
- **ShinyHunters and Lapsus$**: Involvement in TeamPCP supply chain attacks amid hacker infighting
- **SparkCat Operators**: Deploying mobile malware variants on official app stores for cryptocurrency wallet theft