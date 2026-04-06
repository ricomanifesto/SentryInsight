# Exploitation Report

The current threat landscape shows intense exploitation activity across multiple critical vulnerabilities, with particularly concerning zero-day and n-day attacks targeting enterprise infrastructure. Most notably, China-based threat actors are deploying zero-day exploits in high-velocity attacks while leveraging Medusa ransomware, and a critical FortiClient EMS vulnerability is being actively exploited in the wild. Additionally, large-scale automated credential harvesting campaigns are exploiting React2Shell flaws in Next.js applications, and ransomware groups are using vulnerable drivers to disable hundreds of security tools simultaneously.

## Active Exploitation Details

### FortiClient Enterprise Management Server Critical Vulnerability
- **Description**: A critical security flaw in FortiClient Enterprise Management Server that allows attackers to compromise enterprise security infrastructure
- **Impact**: Complete compromise of FortiClient EMS instances, potentially leading to enterprise-wide security breaches
- **Status**: Actively exploited in the wild; emergency patch released by Fortinet
- **CVE ID**: CVE-2026-35616

### React2Shell Vulnerability in Next.js Applications
- **Description**: A vulnerability in Next.js applications that enables automated credential theft through web-exposed applications
- **Impact**: Large-scale automated credential harvesting, exfiltration of secrets and system data
- **Status**: Actively exploited by threat cluster UAT-10608 in ongoing campaign
- **CVE ID**: CVE-2025-55182

### Storm-1175 Zero-Day Exploits
- **Description**: Multiple zero-day and n-day vulnerabilities being deployed by China-based cybercriminal group Storm-1175
- **Impact**: High-velocity attacks leading to Medusa ransomware deployment and complete system compromise
- **Status**: Active exploitation ongoing with zero-day vulnerabilities being weaponized

### Apple iOS DarkSword Vulnerability
- **Description**: A severe mobile OS vulnerability that allows complete compromise of iOS devices
- **Impact**: Mobile device compromise and potential enterprise network infiltration
- **Status**: Recently patched by Apple for iOS 18, marking a precedent-breaking security update

## Affected Systems and Products

- **FortiClient Enterprise Management Server**: All versions prior to emergency patch release, affecting federal agencies and enterprise environments
- **Next.js Applications**: Web-exposed Next.js apps vulnerable to React2Shell exploitation
- **iOS Devices**: iOS 18 systems previously vulnerable to DarkSword exploitation tool
- **EDR Security Tools**: Over 300 endpoint detection and response tools targeted by BYOVD attacks
- **npm Registry**: 36 malicious packages disguised as Strapi CMS plugins targeting Redis and PostgreSQL
- **Chrome Browser Extensions**: Over 6,000 extensions being scanned and monitored by LinkedIn
- **Axios HTTP Client**: Popular npm package compromised through social engineering

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Storm-1175 deploying fresh zero-day vulnerabilities in high-velocity attacks
- **Bring Your Own Vulnerable Driver (BYOVD)**: Qilin and Warlock ransomware using vulnerable drivers to disable security tools
- **Automated Credential Harvesting**: UAT-10608 using automated tools to exploit React2Shell for large-scale data theft
- **Social Engineering**: Six-month sophisticated social engineering operation targeting Axios maintainers and Drift protocol
- **Device Code Phishing**: OAuth 2.0 Device Authorization Grant flow abuse with 37x surge in attacks
- **Supply Chain Attacks**: Malicious npm packages targeting Redis and PostgreSQL databases
- **GitHub C2 Infrastructure**: DPRK-linked hackers using GitHub repositories for command and control

## Threat Actor Activities

- **Storm-1175**: China-based financially motivated group deploying Medusa ransomware with zero-day exploits in high-velocity campaigns
- **UAT-10608**: Emerging threat cluster conducting automated credential harvesting through React2Shell exploitation
- **Qilin Ransomware Group**: Using BYOVD techniques to disable 300+ EDR tools and attacking German political party Die Linke
- **Warlock Ransomware Group**: Collaborating with Qilin in BYOVD attacks against security infrastructure
- **DPRK-Linked Actors**: Using GitHub as C2 infrastructure in multi-stage attacks targeting South Korean organizations and conducting sophisticated social engineering operations against crypto platforms
- **TA416**: China-aligned threat actor targeting European government and diplomatic organizations with PlugX malware and OAuth-based phishing
- **REvil Leadership**: German authorities identified key figures behind 130 ransomware attacks, including leader "UNKN" (Daniil Maksimov)