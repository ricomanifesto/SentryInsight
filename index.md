# Exploitation Report

Current threat activity reveals several critical exploitation campaigns targeting diverse attack vectors. The most significant active exploitations include the React2Shell vulnerability being mass-exploited against Next.js hosts, resulting in credential theft across 766 compromised systems. China-linked TA416 group has resumed targeting European governments with PlugX malware and OAuth-based phishing campaigns. North Korean threat actors continue sophisticated supply chain attacks, including social engineering of npm package maintainers and the $285 million Drift Protocol compromise through Security Council administrative power seizure. Additionally, cookie-controlled PHP web shells are increasingly being deployed on Linux servers for persistent access, while SparkCat malware variants continue targeting mobile cryptocurrency wallets through official app stores.

## Active Exploitation Details

### React2Shell Vulnerability in Next.js
- **Description**: A vulnerability in Next.js applications enabling remote code execution through React component exploitation
- **Impact**: Attackers can steal database credentials, SSH private keys, Amazon Web Services credentials, and other sensitive data from compromised hosts
- **Status**: Actively exploited in large-scale credential harvesting operation affecting 766 hosts
- **CVE ID**: CVE-2025-55182

### DarkSword iOS Vulnerability
- **Description**: A severe mobile OS-cracking tool vulnerability affecting iOS systems prior to version 18
- **Impact**: Enables complete compromise of iOS devices, bypassing security controls
- **Status**: Patched by Apple in iOS 18 in an unprecedented move to address the threat
- **CVE ID**: Not specified

### Cookie-Controlled PHP Web Shells
- **Description**: PHP-based web shells using HTTP cookies as control channels on Linux servers
- **Impact**: Remote code execution, persistent access, and system compromise
- **Status**: Actively being deployed by threat actors for maintaining persistence
- **CVE ID**: Not specified

## Affected Systems and Products

- **Next.js Applications**: 766 confirmed compromised hosts experiencing credential theft
- **iOS Devices**: All devices running iOS versions prior to iOS 18 vulnerable to DarkSword exploitation
- **Linux Servers**: Systems running PHP applications targeted by cookie-controlled web shells
- **Axios npm Package**: Supply chain compromise through social engineering of package maintainer
- **European Government Systems**: Multiple diplomatic and government organizations targeted by TA416
- **Drift Protocol**: Solana-based decentralized exchange compromised for $285 million
- **Die Linke Political Party**: German political organization hit by Qilin ransomware
- **Hims & Hers Health**: Telehealth platform affected by Zendesk support ticket breach
- **European Commission Cloud**: Breach exposing data of 30 EU entities attributed to TeamPCP

## Attack Vectors and Techniques

- **React2Shell Exploitation**: Mass scanning and exploitation of Next.js applications for credential harvesting
- **Social Engineering Campaigns**: Highly-targeted operations against npm package maintainers and cryptocurrency platforms
- **OAuth-Based Phishing**: Sophisticated phishing campaigns targeting European government credentials
- **PlugX Malware Deployment**: Advanced persistent threat tool delivery for long-term access
- **Ransomware Operations**: Multi-extortion attacks combining encryption with data theft threats
- **Supply Chain Attacks**: Compromise of trusted software packages and development environments
- **Cookie-Based Command and Control**: Steganographic use of HTTP cookies for web shell communication
- **Administrative Privilege Escalation**: Seizing Security Council powers in decentralized platforms

## Threat Actor Activities

- **TA416 (China-linked)**: Resumed targeting of European governments after two-year hiatus, deploying PlugX malware and OAuth phishing
- **UNC1069 (North Korean)**: Conducted sophisticated social engineering campaign against Axios npm package maintainer
- **DPRK-linked Groups**: Orchestrated $285 million Drift Protocol compromise through administrative power seizure
- **Qilin Ransomware Group**: Claimed responsibility for Die Linke German political party attack with data theft threats
- **TeamPCP**: Supply chain attacks affecting European Commission and multiple EU entities, with involvement from ShinyHunters and Lapsus$ groups
- **SparkCat Operators**: Continued deployment of cryptocurrency wallet-targeting malware through official iOS and Android app stores
- **Unknown Threat Actors**: Large-scale exploitation of React2Shell vulnerability for credential harvesting operations