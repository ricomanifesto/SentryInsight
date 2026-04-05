# Exploitation Report

The cybersecurity landscape is experiencing significant exploitation activity across multiple attack vectors, with threat actors leveraging vulnerabilities in enterprise software, supply chain attacks, and sophisticated social engineering campaigns. Critical exploitation includes an actively exploited FortiClient EMS vulnerability (CVE-2026-35616), a widespread Next.js vulnerability (CVE-2025-55182) affecting 766 hosts, and multiple supply chain compromises targeting npm packages and popular libraries. North Korean threat actors, particularly UNC1069, have been highly active in sophisticated social engineering campaigns, while China-linked groups like TA416 continue targeting European government entities. The exploitation landscape demonstrates a shift toward multi-vector attacks combining technical vulnerabilities with human manipulation techniques.

## Active Exploitation Details

### FortiClient EMS Critical Vulnerability
- **Description**: A critical security flaw in Fortinet's FortiClient EMS that has been exploited in the wild, prompting out-of-band patches from Fortinet
- **Impact**: Allows attackers to compromise enterprise endpoint management systems
- **Status**: Actively exploited, patches released by Fortinet
- **CVE ID**: CVE-2026-35616

### Next.js React2Shell Vulnerability
- **Description**: A vulnerability in Next.js hosts that enables credential harvesting operations at scale
- **Impact**: Large-scale theft of database credentials, SSH private keys, and Amazon Web Services credentials
- **Status**: Actively exploited against 766 Next.js hosts in credential harvesting campaign
- **CVE ID**: CVE-2025-55182

### Apple iOS DarkSword Vulnerability
- **Description**: A severe mobile OS-cracking tool affecting iOS 18 systems
- **Impact**: Enables exploitation of iOS devices for unauthorized access and control
- **Status**: Patched by Apple in an unprecedented move for older iOS versions

### Malicious npm Package Campaign
- **Description**: 36 malicious packages disguised as Strapi CMS plugins deployed in npm registry
- **Impact**: Persistent implants deployed to Redis and PostgreSQL databases
- **Status**: Packages identified and removed, ongoing threat assessment

## Affected Systems and Products

- **FortiClient EMS**: Enterprise endpoint management systems vulnerable to critical exploitation
- **Next.js Applications**: 766 hosts compromised in credential harvesting operation
- **iOS 18 Devices**: Previously vulnerable to DarkSword exploitation tool
- **npm Registry**: 36 malicious packages targeting Strapi CMS environments
- **Axios Library**: Popular HTTP client targeted in supply chain compromise
- **Redis and PostgreSQL**: Databases targeted for persistent implant deployment
- **European Government Systems**: Targeted by China-linked TA416 group
- **Drift Platform**: Solana-based decentralized exchange losing $285 million
- **Zendesk Platform**: Third-party breach affecting Hims & Hers customer data

## Attack Vectors and Techniques

- **Social Engineering**: North Korean UNC1069 group using fake Microsoft Teams error messages to compromise maintainer accounts
- **Supply Chain Attacks**: Multiple compromises targeting npm packages and popular libraries like Axios
- **Device Code Phishing**: OAuth 2.0 Device Authorization Grant flow abuse surging 37x with new attack kits
- **Cookie-Controlled Web Shells**: PHP-based web shells using HTTP cookies for control channels on Linux servers
- **Durable Nonce Attack**: Social engineering attack against Solana-based platforms
- **Extension Scanning**: LinkedIn using hidden JavaScript to scan for Chrome extensions and collect device data
- **Multi-Extortion Ransomware**: Advanced ransomware techniques combining encryption with data theft threats

## Threat Actor Activities

- **UNC1069 (North Korean)**: Sophisticated social engineering campaign targeting Axios maintainer using fake Microsoft Teams error scenarios
- **TA416 (China-linked)**: Renewed targeting of European government and diplomatic organizations since mid-2025 using PlugX malware and OAuth-based phishing
- **TeamPCP**: Supply chain attacks expanding with involvement from ShinyHunters and Lapsus$ groups creating complex attribution challenges
- **Qilin Ransomware Group**: Successful attack against German political party Die Linke with data theft and system outages
- **DPRK-linked Actors**: $285 million theft from Drift platform using social engineering techniques
- **SparkCat Operators**: New malware variant targeting iOS and Android apps to steal cryptocurrency wallet recovery phrases