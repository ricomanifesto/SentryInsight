# Exploitation Report

A critical wave of active exploitation activities has been identified across multiple platforms, with attackers leveraging zero-day vulnerabilities, supply chain compromises, and sophisticated social engineering techniques. The most concerning developments include active exploitation of a critical Fortinet FortiClient EMS vulnerability (CVE-2026-35616) and widespread exploitation of a Next.js vulnerability (CVE-2025-55182) affecting hundreds of hosts. Additionally, North Korean threat actors have successfully executed high-impact supply chain attacks against npm packages and cryptocurrency platforms, while ransomware groups continue to target political organizations and major corporations.

## Active Exploitation Details

### Fortinet FortiClient EMS Critical Vulnerability
- **Description**: Critical security flaw in Fortinet's FortiClient EMS (Enterprise Management Server) that has been actively exploited in the wild
- **Impact**: Allows attackers to gain unauthorized access to enterprise management systems
- **Status**: Fortinet has released out-of-band patches to address the vulnerability
- **CVE ID**: CVE-2026-35616

### React2Shell Next.js Vulnerability
- **Description**: Vulnerability in Next.js framework that enables remote code execution and credential harvesting
- **Impact**: Large-scale credential theft operation affecting 766 Next.js hosts, allowing attackers to steal database credentials, SSH private keys, and AWS credentials
- **Status**: Actively exploited in widespread campaigns
- **CVE ID**: CVE-2025-55182

### Apple iOS DarkSword Vulnerability
- **Description**: Severe mobile OS-cracking tool vulnerability affecting iOS systems
- **Impact**: Allows attackers to crack iOS security mechanisms and gain unauthorized access
- **Status**: Apple has broken precedent by patching this vulnerability for iOS 18, protecting users unable to adopt iOS 26

## Affected Systems and Products

- **Fortinet FortiClient EMS**: Enterprise Management Server systems across organizations using Fortinet security infrastructure
- **Next.js Applications**: 766 confirmed compromised hosts running Next.js framework applications
- **npm Registry**: 36 malicious packages disguised as Strapi CMS plugins targeting Redis and PostgreSQL databases
- **Axios npm Package**: Popular HTTP client library compromised through social engineering attack
- **Apple iOS**: Mobile devices running iOS systems vulnerable to DarkSword exploitation tool
- **Linux Servers**: PHP-based web applications on Linux systems targeted by cookie-controlled web shells
- **Solana Drift Platform**: Decentralized exchange platform compromised resulting in $285 million loss
- **European Commission Cloud**: Cloud infrastructure affecting 30 EU entities
- **German Political Party (Die Linke)**: IT systems compromised by ransomware attack

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Malicious npm packages disguised as legitimate Strapi CMS plugins to deploy persistent implants
- **Social Engineering**: Sophisticated campaigns using fake Microsoft Teams error messages to hijack maintainer accounts
- **OAuth 2.0 Device Authorization Grant Abuse**: Device code phishing attacks surging 37 times, abusing legitimate authentication flows
- **Cookie-Controlled Web Shells**: PHP-based web shells using HTTP cookies as control channels for remote code execution
- **Durable Nonce Social Engineering**: Advanced technique used in cryptocurrency platform attacks
- **Ransomware Multi-Extortion**: Combined data encryption and exfiltration tactics for increased pressure on victims

## Threat Actor Activities

- **UNC1069 (North Korean APT)**: Orchestrated sophisticated social engineering campaign targeting Axios npm maintainer, leading to supply chain compromise
- **TA416 (China-aligned)**: Targeting European government and diplomatic organizations since mid-2025 using PlugX malware and OAuth-based phishing
- **TeamPCP**: Conducting supply chain attacks with expanding blast radius, complicated by involvement of ShinyHunters and Lapsus$ groups
- **Qilin Ransomware Group**: Successfully attacked German political party Die Linke, causing IT system outages and threatening data leaks
- **DPRK-linked Actors**: Responsible for $285 million Drift platform compromise using advanced social engineering techniques
- **SparkCat Operators**: Deploying new malware variants on iOS and Android app stores to steal cryptocurrency wallet recovery phrases