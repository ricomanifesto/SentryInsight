# Exploitation Report

Critical exploitation activity has intensified across multiple attack vectors, with threat actors leveraging both supply chain compromises and actively exploited vulnerabilities to target organizations worldwide. The most significant incidents include a critical FortiClient EMS vulnerability being exploited in the wild, large-scale supply chain attacks targeting npm packages and the Axios library through sophisticated social engineering campaigns, and a massive credential harvesting operation exploiting Next.js hosts. North Korean threat actors, particularly UNC1069, have been prominently involved in these campaigns, demonstrating advanced social engineering techniques and targeting high-value software supply chains.

## Active Exploitation Details

### FortiClient EMS Critical Vulnerability
- **Description**: Critical security flaw in Fortinet's FortiClient Enterprise Management Server that has been actively exploited in the wild
- **Impact**: Allows attackers to achieve unauthorized access and compromise enterprise management infrastructure
- **Status**: Fortinet has released out-of-band patches to address the actively exploited vulnerability
- **CVE ID**: CVE-2026-35616

### React2Shell Next.js Vulnerability
- **Description**: Vulnerability in Next.js framework enabling large-scale credential harvesting operations
- **Impact**: Attackers can steal database credentials, SSH private keys, and Amazon Web Services credentials from compromised hosts
- **Status**: Actively exploited with 766 Next.js hosts confirmed compromised
- **CVE ID**: CVE-2025-55182

### DarkSword iOS Mobile Exploitation Tool
- **Description**: Severe mobile operating system cracking tool targeting iOS devices
- **Impact**: Capable of compromising iOS security mechanisms and gaining unauthorized access to mobile devices
- **Status**: Apple has broken precedent by patching the vulnerability in iOS 18, protecting organizations with users unable to upgrade to iOS 26

## Affected Systems and Products

- **FortiClient EMS**: Enterprise management servers running vulnerable versions prior to the out-of-band patch release
- **Next.js Framework**: Web applications and hosts running vulnerable Next.js implementations, with 766 confirmed compromised systems
- **npm Registry Packages**: 36 malicious packages disguised as Strapi CMS plugins targeting Redis and PostgreSQL databases
- **Axios HTTP Client**: Popular JavaScript library compromised through maintainer account takeover
- **iOS Devices**: Mobile devices running iOS versions prior to the DarkSword patch in iOS 18
- **Linux Servers**: Systems running PHP applications vulnerable to cookie-controlled web shell deployment
- **Chrome Browsers**: Users with specific extensions being scanned and monitored by LinkedIn's hidden JavaScript

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Malicious npm packages disguised as legitimate Strapi CMS plugins to target database systems
- **Social Engineering**: Sophisticated campaigns targeting software maintainers with fake Microsoft Teams error messages
- **OAuth 2.0 Device Code Phishing**: Abuse of Device Authorization Grant flow with 37x surge in attacks using proliferating attack kits
- **Cookie-Controlled Web Shells**: PHP-based backdoors using HTTP cookies as control channels on Linux servers with cron persistence
- **Durable Nonce Social Engineering**: Advanced technique targeting cryptocurrency platforms, resulting in $285 million theft from Drift exchange
- **Browser Extension Scanning**: Hidden JavaScript deployment to enumerate and collect data about installed Chrome extensions

## Threat Actor Activities

- **UNC1069 (North Korean)**: Orchestrated sophisticated social engineering campaign against Axios maintainer, leading to npm supply chain compromise through fake Teams support scenarios
- **TA416 (China-linked)**: Renewed targeting of European government and diplomatic organizations since mid-2025 using PlugX malware and OAuth-based phishing campaigns
- **TeamPCP**: Supply chain attacks expanding blast radius with involvement from ShinyHunters and Lapsus$ groups, compromising European Commission and exposing data from 30 EU entities
- **DPRK-linked Groups**: Connected to $285 million Drift cryptocurrency exchange theft using durable nonce social engineering techniques
- **Qilin Ransomware**: Confirmed attack against German political party Die Linke, stealing sensitive data and disrupting IT systems
- **SparkCat Operators**: Deploying new malware variants on both Apple App Store and Google Play Store targeting cryptocurrency wallet recovery phrases