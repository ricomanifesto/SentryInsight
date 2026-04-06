# Exploitation Report

Critical exploitation activity is currently dominated by several high-impact vulnerabilities being actively exploited in the wild. Most notably, Fortinet's FortiClient Enterprise Management Server is under active attack through CVE-2026-35616, prompting an emergency patch release. Simultaneously, threat actors are exploiting CVE-2025-55182 (React2Shell) in Next.js applications for automated credential theft campaigns. The exploitation landscape is further complicated by sophisticated social engineering campaigns, including a six-month North Korean operation that resulted in a $285 million cryptocurrency theft from Drift, and supply chain attacks targeting popular npm packages like Axios through social engineering tactics.

## Active Exploitation Details

### FortiClient EMS Critical Vulnerability
- **Description**: A critical security flaw in Fortinet's FortiClient Enterprise Management Server that allows attackers to compromise enterprise management infrastructure
- **Impact**: Unauthorized access to enterprise management systems, potential for lateral movement and credential theft
- **Status**: Actively exploited in the wild; emergency patch released by Fortinet
- **CVE ID**: CVE-2026-35616

### React2Shell Vulnerability in Next.js Applications
- **Description**: A vulnerability in Next.js applications that enables remote code execution and credential theft
- **Impact**: Automated credential harvesting, potential system compromise, and data exfiltration
- **Status**: Being exploited in large-scale automated campaigns
- **CVE ID**: CVE-2025-55182

### DarkSword iOS Exploit
- **Description**: A severe mobile operating system exploitation tool targeting iOS devices
- **Impact**: Complete device compromise and jailbreaking capabilities
- **Status**: Patched by Apple in iOS 18, breaking precedent for older iOS versions

## Affected Systems and Products

- **Fortinet FortiClient EMS**: Enterprise management servers vulnerable to critical exploitation
- **Next.js Applications**: Web applications using the React framework susceptible to React2Shell attacks
- **iOS Devices**: Mobile devices running iOS versions prior to the emergency patch
- **npm Package Ecosystem**: JavaScript packages including Axios and 36 malicious Strapi CMS plugins
- **Redis and PostgreSQL Databases**: Database systems targeted through malicious npm packages
- **Chrome Browser Extensions**: Over 6,000 extensions being fingerprinted by LinkedIn's data collection

## Attack Vectors and Techniques

- **Social Engineering**: Six-month targeted campaigns against cryptocurrency platforms and npm maintainers
- **Supply Chain Compromise**: Malicious npm packages disguised as legitimate Strapi CMS plugins
- **Device Code Phishing**: OAuth 2.0 Device Authorization Grant flow abuse with 37x surge in attacks
- **QR Code Phishing**: Traffic violation scams using QR codes to redirect to phishing sites
- **PHP Web Shells**: Cookie-controlled web shells persisting via cron jobs on Linux servers
- **Fake Teams Error Messages**: Social engineering technique used to hijack maintainer accounts

## Threat Actor Activities

- **UNC1069 (North Korean)**: Conducted sophisticated social engineering campaign against Axios maintainer, leading to npm supply chain attack
- **DPRK-Linked Groups**: Six-month social engineering operation targeting Drift cryptocurrency exchange, resulting in $285 million theft
- **REvil Ransomware Leaders**: German authorities identified Daniil Maksimov ("UNKN") as leader of REvil and GandCrab operations, responsible for 130 German attacks
- **TA416 (China-Linked)**: Targeting European government and diplomatic organizations with PlugX malware and OAuth-based phishing since mid-2025
- **Qilin Ransomware Group**: Attacked German political party Die Linke, stealing sensitive data and threatening public release
- **TeamPCP**: Supply chain attacks expanding with involvement from ShinyHunters and Lapsus$ groups creating confusion for enterprise victims