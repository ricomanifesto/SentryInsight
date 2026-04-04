# Exploitation Report

Current exploitation activity reveals a landscape dominated by supply chain attacks, advanced social engineering campaigns, and targeted breaches affecting major organizations. North Korean threat actors are leading sophisticated operations, including the massive $280-285 million theft from Drift Protocol and a targeted npm supply chain compromise affecting the popular Axios package. The TeamPCP threat group has expanded its operations with attacks on the European Commission exposing data from 30 EU entities. Active exploitation includes CVE-2025-55182 being used to breach hundreds of Next.js hosts for credential theft, while threat actors exploit iOS vulnerabilities through the DarkSword tool and distribute SparkCat malware through official app stores.

## Active Exploitation Details

### React2Shell Vulnerability in Next.js
- **Description**: A vulnerability in Next.js framework allowing unauthorized access to web applications and server environments
- **Impact**: Mass credential harvesting operation targeting database credentials, SSH private keys, and Amazon Web Services credentials across 766 compromised hosts
- **Status**: Currently being actively exploited in large-scale attacks
- **CVE ID**: CVE-2025-55182

### DarkSword iOS Exploitation Tool
- **Description**: A severe mobile operating system cracking tool targeting iOS devices
- **Impact**: Complete compromise of iOS devices, allowing attackers to bypass security controls and access sensitive data
- **Status**: Apple has broken precedent to patch this vulnerability in iOS 18, indicating severity
- **Platform**: iOS 18 and earlier versions

### SparkCat Mobile Malware
- **Description**: Trojan malware distributed through official iOS and Android app stores targeting cryptocurrency wallets
- **Impact**: Theft of cryptocurrency wallet recovery phrase images, potentially leading to complete wallet compromise
- **Status**: New variant discovered on both Apple App Store and Google Play Store after previous detection

### Cookie-Controlled PHP Web Shells
- **Description**: Advanced web shell techniques using HTTP cookies as control channels on compromised Linux servers
- **Impact**: Remote code execution and persistent access to compromised servers through cron job persistence
- **Status**: Actively deployed by threat actors targeting Linux server environments

## Affected Systems and Products

- **Next.js Framework**: 766 hosts compromised in credential harvesting campaign
- **iOS Devices**: Targeted by DarkSword exploitation tool, patched in iOS 18
- **Android and iOS Mobile Apps**: SparkCat malware distributed through official app stores
- **Linux Servers**: Targeted by PHP web shell attacks using cookie-based control mechanisms
- **Axios npm Package**: Supply chain compromise affecting popular JavaScript library
- **European Commission Cloud Infrastructure**: Compromised by TeamPCP affecting 30 EU entities
- **Drift Protocol**: Solana-based decentralized exchange losing $280-285 million
- **Die Linke Political Party**: German political organization hit by Qilin ransomware
- **Hims & Hers Health**: Telehealth platform affected through Zendesk breach
- **Hasbro**: Toy manufacturer experiencing ongoing attack requiring weeks of remediation

## Attack Vectors and Techniques

- **Social Engineering**: Highly targeted campaigns against open source maintainers, particularly North Korean operations against npm package maintainers
- **Supply Chain Attacks**: Compromise of trusted software packages and third-party services to reach downstream targets
- **OAuth-Based Phishing**: Advanced phishing techniques leveraging OAuth authentication mechanisms
- **Administrative Privilege Escalation**: Attackers gaining Security Council powers in decentralized finance protocols
- **Multi-Extortion Ransomware**: Combined data encryption and data theft for enhanced pressure tactics
- **Residential Proxy Networks**: Malicious traffic routing through legitimate residential IP addresses to evade detection
- **Browser Extension Scanning**: Hidden JavaScript used to fingerprint users based on installed browser extensions
- **Fake Repository Distribution**: Exploitation of source code leaks to distribute malware through fake GitHub repositories

## Threat Actor Activities

- **UNC1069 (North Korean APT)**: Social engineering campaign targeting Axios npm package maintainer, leading to supply chain compromise
- **DPRK-Linked Groups**: $285 million theft from Drift Protocol using sophisticated durable nonce attack techniques
- **TA416 (China-Aligned)**: Renewed targeting of European government and diplomatic organizations after two-year hiatus, using PlugX malware and OAuth-based phishing
- **TeamPCP**: Supply chain attacks expanding to affect European Commission and 30 EU entities, with involvement from ShinyHunters and Lapsus$ groups
- **Qilin Ransomware Group**: Attack on German political party Die Linke with threats of sensitive data leak
- **SparkCat Operators**: Distribution of cryptocurrency theft malware through official mobile app stores targeting wallet recovery phrases