# Exploitation Report

The current threat landscape reveals multiple critical exploitation activities targeting enterprise infrastructure and popular software platforms. The most severe active threat involves a critical FortiClient EMS vulnerability (CVE-2026-35616) being exploited in the wild, prompting emergency patches from Fortinet. Concurrently, attackers are leveraging React2Shell vulnerabilities in Next.js applications for large-scale automated credential theft campaigns. The threat environment is further complicated by sophisticated social engineering operations, including North Korean threat actors conducting months-long campaigns that successfully compromised major platforms like Drift ($285 million theft) and the Axios npm package. Supply chain attacks continue to escalate with malicious npm packages exploiting database systems and mobile malware variants stealing cryptocurrency wallet recovery phrases from iOS and Android applications.

## Active Exploitation Details

### FortiClient EMS Critical Vulnerability
- **Description**: Critical security flaw in FortiClient Enterprise Management Server allowing attackers to compromise enterprise management infrastructure
- **Impact**: Complete compromise of FortiClient EMS systems, potentially affecting entire enterprise network management and security posture
- **Status**: Actively exploited in the wild; emergency out-of-band patches released by Fortinet
- **CVE ID**: CVE-2026-35616

### React2Shell Vulnerability in Next.js Applications
- **Description**: Security flaw in Next.js applications enabling automated exploitation for credential theft
- **Impact**: Large-scale automated credential harvesting from vulnerable web applications
- **Status**: Currently being exploited in widespread credential theft campaigns
- **CVE ID**: CVE-2025-55182

### Malicious npm Package Supply Chain Attacks
- **Description**: 36 malicious packages disguised as Strapi CMS plugins targeting Redis and PostgreSQL databases
- **Impact**: Deployment of persistent implants in database systems, potential data exfiltration and system compromise
- **Status**: Active threat in npm registry targeting database infrastructure

## Affected Systems and Products

- **FortiClient Enterprise Management Server**: All versions prior to emergency patch release affected by critical vulnerability
- **Next.js Applications**: Web applications using Next.js framework vulnerable to React2Shell exploitation
- **npm Package Registry**: Strapi CMS plugin ecosystem compromised with 36 malicious packages
- **Redis Database Systems**: Targeted by malicious npm packages for persistent implant deployment
- **PostgreSQL Database Systems**: Exploited through compromised npm packages for system persistence
- **iOS and Android Applications**: Mobile apps containing SparkCat malware variants targeting cryptocurrency wallets
- **Axios HTTP Client**: Popular npm package compromised through social engineering of maintainer
- **European Commission Cloud Infrastructure**: Breached exposing data from 30 EU entities
- **Drift Decentralized Exchange**: Solana-based platform compromised for $285 million theft

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Targeting npm package maintainers through sophisticated social engineering campaigns
- **Social Engineering**: Six-month targeted operations using fake Microsoft Teams error messages to compromise developer accounts
- **Database Exploitation**: Malicious packages targeting Redis and PostgreSQL for persistent access
- **OAuth Device Code Phishing**: 37x surge in attacks abusing OAuth 2.0 Device Authorization Grant flow
- **QR Code Phishing**: Traffic violation scams using QR codes in text messages for credential theft
- **Cookie-Controlled Web Shells**: PHP-based web shells using HTTP cookies as control channels on Linux servers
- **Mobile Malware Distribution**: SparkCat variants distributed through official app stores targeting cryptocurrency wallets
- **Durable Nonce Attacks**: Advanced cryptocurrency theft techniques targeting decentralized exchanges

## Threat Actor Activities

- **UNC1069 (North Korean)**: Conducted sophisticated social engineering campaign against Axios maintainer leading to npm supply chain attack
- **DPRK-linked Groups**: Six-month operation targeting Drift platform resulting in $285 million cryptocurrency theft
- **TA416 (China-linked)**: Targeting European government and diplomatic organizations with PlugX malware and OAuth-based phishing
- **TeamPCP**: Supply chain attacks expanding blast radius with involvement from ShinyHunters and Lapsus$ groups, responsible for European Commission hack
- **Qilin Ransomware Group**: Attacked Die Linke German political party, stealing sensitive data and disrupting IT systems
- **Unknown Threat Actors**: Large-scale credential theft campaigns exploiting React2Shell vulnerabilities in automated fashion