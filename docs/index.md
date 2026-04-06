# Exploitation Report

Critical exploitation activity is currently centered around several high-impact vulnerabilities and sophisticated attack campaigns. Most notably, Fortinet's FortiClient Enterprise Management Server is under active attack through CVE-2026-35616, prompting emergency patches. Simultaneously, threat actors are exploiting React2Shell vulnerabilities (CVE-2025-55182) in Next.js applications for automated credential theft campaigns. Advanced persistent threat groups, including North Korean actors, are conducting elaborate social engineering operations targeting major software supply chains, while ransomware operators are leveraging vulnerable drivers to disable hundreds of endpoint detection and response tools. These attacks demonstrate increasingly sophisticated techniques combining zero-day exploitation, supply chain compromise, and advanced evasion methods.

## Active Exploitation Details

### FortiClient EMS Critical Vulnerability
- **Description**: A critical security flaw in Fortinet's FortiClient Enterprise Management Server that allows attackers to compromise enterprise security management infrastructure
- **Impact**: Complete compromise of enterprise endpoint management capabilities, potentially affecting entire organizational security postures
- **Status**: Actively exploited in the wild; emergency out-of-band patches released by Fortinet
- **CVE ID**: CVE-2026-35616

### React2Shell Next.js Vulnerability
- **Description**: A vulnerability in Next.js applications that enables attackers to execute shell commands and steal credentials through automated exploitation
- **Impact**: Automated credential theft campaigns targeting vulnerable web applications at scale
- **Status**: Currently being exploited in large-scale automated campaigns
- **CVE ID**: CVE-2025-55182

### Bring Your Own Vulnerable Driver (BYOVD) Attacks
- **Description**: Ransomware operators are exploiting vulnerable legitimate drivers to disable endpoint detection and response (EDR) tools
- **Impact**: Complete neutralization of security tools, enabling undetected ransomware deployment and data exfiltration
- **Status**: Actively used by Qilin and Warlock ransomware groups to disable over 300 EDR tools

## Affected Systems and Products

- **Fortinet FortiClient EMS**: Enterprise management servers vulnerable to critical exploitation
- **Next.js Applications**: Web applications using React frameworks susceptible to React2Shell attacks
- **Windows Systems**: Targeted by vulnerable driver exploitation to disable EDR protection
- **npm Package Ecosystem**: Supply chain compromised through social engineering of maintainers
- **Redis and PostgreSQL Databases**: Exploited through malicious npm packages disguised as Strapi CMS plugins
- **iOS and Android Devices**: Targeted by SparkCat malware variants stealing cryptocurrency wallet recovery phrases
- **Linux Servers**: Compromised through cookie-controlled PHP web shells with cron persistence

## Attack Vectors and Techniques

- **Social Engineering**: Sophisticated months-long campaigns targeting software maintainers with fake Microsoft Teams error scenarios
- **Supply Chain Compromise**: Infiltration of popular npm packages including Axios through maintainer account hijacking
- **Device Code Phishing**: 37-fold increase in OAuth 2.0 Device Authorization Grant flow abuse for account takeovers
- **Malicious Package Distribution**: Deployment of 36 malicious npm packages disguised as legitimate Strapi CMS plugins
- **Cookie-Controlled Web Shells**: HTTP cookies used as control channels for PHP-based backdoors on Linux systems
- **QR Code Phishing**: Traffic violation scams using QR codes to redirect victims to credential harvesting sites

## Threat Actor Activities

- **North Korean Groups (UNC1069/DPRK)**: Conducted six-month social engineering operation resulting in $285 million Drift platform theft and Axios npm package compromise
- **Qilin Ransomware**: Attacking German political organizations and using vulnerable drivers to disable security tools
- **Warlock Ransomware**: Employing BYOVD techniques alongside Qilin to neutralize endpoint protection
- **China-Linked TA416**: Targeting European government and diplomatic organizations with PlugX malware and OAuth-based phishing since mid-2025
- **REvil/GandCrab Leadership**: German authorities identified key figures including "UNKN" (Daniil Maksimov) behind major ransomware operations
- **TeamPCP**: Supply chain attacks expanding with involvement from ShinyHunters and Lapsus$ groups creating complex attribution challenges