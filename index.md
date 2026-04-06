# Exploitation Report

Critical exploitation activity is currently dominated by several high-impact vulnerabilities being actively exploited in the wild. Most notably, Fortinet's FortiClient Enterprise Management Server is facing active exploitation of CVE-2026-35616, prompting an emergency security update. Simultaneously, React2Shell vulnerabilities (CVE-2025-55182) in Next.js applications are being leveraged in large-scale automated credential theft campaigns. The threat landscape is further complicated by sophisticated supply chain attacks, including North Korean-linked social engineering operations targeting npm maintainers and the deployment of malicious packages disguised as legitimate CMS plugins. Additionally, mobile platforms are experiencing renewed threats with SparkCat malware variants infiltrating official app stores to steal cryptocurrency wallet recovery phrases.

## Active Exploitation Details

### FortiClient EMS Critical Vulnerability
- **Description**: A critical security flaw in Fortinet's FortiClient Enterprise Management Server that allows attackers to compromise enterprise network management infrastructure
- **Impact**: Potential complete compromise of enterprise network management, unauthorized access to managed endpoints, and lateral movement across corporate networks
- **Status**: Actively exploited in the wild; emergency out-of-band patches released by Fortinet
- **CVE ID**: CVE-2026-35616

### React2Shell Next.js Vulnerability
- **Description**: A vulnerability in Next.js applications that enables remote code execution through React component exploitation
- **Impact**: Automated credential theft, unauthorized access to web applications, and potential server compromise
- **Status**: Actively exploited in large-scale automated campaigns targeting vulnerable Next.js deployments
- **CVE ID**: CVE-2025-55182

### iOS DarkSword Mobile Exploitation Tool
- **Description**: A sophisticated mobile operating system exploitation tool targeting iOS devices
- **Impact**: Complete device compromise, data exfiltration, and persistent access to mobile devices
- **Status**: Apple has broken precedent by patching this vulnerability in iOS 18, indicating severity of the threat

## Affected Systems and Products

- **FortiClient Enterprise Management Server**: All versions prior to emergency patch release, affecting enterprise network management infrastructure
- **Next.js Applications**: Web applications using vulnerable React components, particularly those with improper input validation
- **iOS Devices**: iOS versions prior to the emergency iOS 18 security update addressing DarkSword exploitation
- **npm Package Ecosystem**: 36 malicious packages disguised as Strapi CMS plugins targeting Redis and PostgreSQL databases
- **Axios HTTP Client**: Popular JavaScript library compromised through maintainer account takeover
- **Chrome Browser Extensions**: Over 6,000 extensions being scanned and monitored by LinkedIn's hidden tracking scripts

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Malicious npm packages masquerading as legitimate Strapi plugins to deploy persistent database implants
- **Social Engineering**: Six-month targeted operations against cryptocurrency platforms and npm maintainers using fake Microsoft Teams error scenarios
- **OAuth Device Code Phishing**: 37x increase in attacks abusing OAuth 2.0 Device Authorization Grant flow for account hijacking
- **QR Code Phishing**: Traffic violation scams utilizing QR codes to bypass traditional email security filters
- **Cookie-Controlled Web Shells**: PHP-based web shells on Linux servers using HTTP cookies for command and control persistence
- **Mobile App Store Infiltration**: SparkCat malware variants distributed through official Apple App Store and Google Play Store

## Threat Actor Activities

- **North Korean APT Groups (UNC1069/DPRK)**: Conducting sophisticated social engineering campaigns targeting cryptocurrency platforms and software supply chains, resulting in $285 million theft from Drift exchange
- **China-Linked TA416**: Targeting European government and diplomatic organizations with PlugX malware and OAuth-based phishing since mid-2025
- **REvil/GandCrab Operations**: German authorities identifying Russian national Daniil Maksimov ("UNKN") as leader of major ransomware operations
- **Qilin Ransomware Group**: Successfully compromising German political party Die Linke and threatening sensitive data disclosure
- **TeamPCP Supply Chain Attackers**: Expanding operations with involvement from ShinyHunters and Lapsus$ groups creating complex attribution challenges
- **Unknown Threat Actors**: Deploying 36 malicious npm packages with Redis and PostgreSQL exploitation capabilities for persistent infrastructure compromise