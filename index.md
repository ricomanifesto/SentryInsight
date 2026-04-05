# Exploitation Report

Critical exploitation activity is currently underway across multiple platforms and systems. The most significant threats include the active exploitation of React2Shell vulnerability in Next.js applications for automated credential theft, the in-the-wild exploitation of a critical Fortinet FortiClient EMS vulnerability, and sophisticated supply chain attacks targeting popular npm packages. North Korean threat actors are conducting extensive social engineering campaigns targeting major open-source projects, while Chinese state-sponsored groups are launching targeted attacks against European government entities. Additionally, malicious actors are distributing crypto-stealing malware through legitimate app stores and exploiting legitimate OAuth flows for phishing attacks.

## Active Exploitation Details

### React2Shell Vulnerability in Next.js Applications
- **Description**: A vulnerability in Next.js applications that allows attackers to execute automated credential theft campaigns
- **Impact**: Attackers can steal user credentials through automated exploitation of vulnerable web applications
- **Status**: Currently being actively exploited in large-scale campaigns
- **CVE ID**: CVE-2025-55182

### Fortinet FortiClient EMS Critical Vulnerability
- **Description**: A critical security flaw in Fortinet's FortiClient EMS (Endpoint Management Server) that has been exploited in the wild
- **Impact**: Allows unauthorized access and potential compromise of enterprise endpoint management infrastructure
- **Status**: Actively exploited; out-of-band patches have been released by Fortinet
- **CVE ID**: CVE-2026-35616

### Apple iOS DarkSword Vulnerability
- **Description**: A severe mobile OS-cracking vulnerability that affects iOS systems
- **Impact**: Allows attackers to compromise iOS devices using specialized mobile exploitation tools
- **Status**: Apple has broken precedent by patching this vulnerability in iOS 18

### Malicious npm Packages Exploiting Database Systems
- **Description**: 36 malicious packages disguised as Strapi CMS plugins that exploit Redis and PostgreSQL databases
- **Impact**: Deploy persistent implants and compromise database infrastructure
- **Status**: Packages discovered in npm registry, targeting Redis and PostgreSQL systems

## Affected Systems and Products

- **Next.js Applications**: Web applications built with Next.js framework vulnerable to React2Shell exploitation
- **Fortinet FortiClient EMS**: Enterprise endpoint management servers requiring immediate patching
- **iOS 18 Devices**: Mobile devices affected by DarkSword exploitation tool
- **npm Registry**: JavaScript package ecosystem containing malicious Strapi CMS plugin packages
- **Redis Databases**: NoSQL databases targeted by malicious npm packages for persistent implant deployment
- **PostgreSQL Databases**: SQL databases exploited by disguised npm packages
- **Axios npm Package**: Popular HTTP client library compromised through social engineering
- **Linux Servers**: Systems running PHP applications vulnerable to cookie-controlled web shells
- **Chrome Extensions**: Browser extensions being scanned by LinkedIn for data collection
- **OAuth 2.0 Implementations**: Authentication systems vulnerable to device code phishing attacks

## Attack Vectors and Techniques

- **Social Engineering**: North Korean threat actors using fake Microsoft Teams error fixes to compromise npm maintainer accounts
- **Supply Chain Attacks**: Targeting popular open-source packages like Axios through maintainer account compromise
- **Device Code Phishing**: Exploiting OAuth 2.0 Device Authorization Grant flow with 37x surge in attacks
- **Cookie-Controlled Web Shells**: Using HTTP cookies as control channels for PHP-based web shells on Linux servers
- **Malicious App Distribution**: Distributing SparkCat malware variants through Apple App Store and Google Play Store
- **OAuth-Based Phishing**: Chinese TA416 group using OAuth mechanisms for credential harvesting
- **Durable Nonce Attacks**: Social engineering attacks targeting cryptocurrency platforms
- **Browser Extension Scanning**: Hidden JavaScript scripts scanning for installed Chrome extensions

## Threat Actor Activities

- **North Korean UNC1069**: Conducting sophisticated social engineering campaigns against npm maintainers, successfully compromising Axios package maintainer accounts through fake Teams support scenarios
- **Chinese TA416 Group**: Targeting European government and diplomatic organizations since mid-2025, using PlugX malware and OAuth-based phishing techniques after a two-year hiatus from regional targeting
- **TeamPCP Threat Group**: Responsible for European Commission cloud infrastructure hack, exposing data from at least 30 EU entities, with involvement from ShinyHunters and Lapsus$ groups creating complex attribution challenges
- **Qilin Ransomware Group**: Successfully attacking Die Linke German political party, forcing IT systems outage and threatening sensitive data disclosure
- **DPRK-Linked Actors**: Executing $285 million cryptocurrency theft from Drift platform using durable nonce social engineering techniques