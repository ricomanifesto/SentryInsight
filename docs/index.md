# Exploitation Report

Current threat activity is dominated by sophisticated social engineering campaigns, supply chain attacks, and the exploitation of web application vulnerabilities. North Korean threat actors are conducting high-impact operations including a $285 million cryptocurrency theft from Drift Protocol and supply chain compromises targeting npm packages. The React2Shell vulnerability (CVE-2025-55182) is being actively exploited to compromise Next.js hosts for credential harvesting, while device code phishing attacks have surged dramatically with a 37-fold increase. Chinese APT group TA416 has resumed targeting European governments with PlugX malware and OAuth-based phishing campaigns, and ransomware groups continue multi-extortion operations against high-profile targets including political organizations and major corporations.

## Active Exploitation Details

### React2Shell Vulnerability in Next.js
- **Description**: A vulnerability in Next.js frameworks that allows attackers to gain unauthorized access to web applications
- **Impact**: Large-scale credential harvesting operation targeting database credentials, SSH private keys, and Amazon Web Services credentials across 766 compromised hosts
- **Status**: Actively being exploited in widespread attacks
- **CVE ID**: CVE-2025-55182

### DarkSword iOS Exploitation Tool
- **Description**: A severe mobile operating system cracking tool targeting iOS devices
- **Impact**: Provides attackers with advanced capabilities to compromise iOS devices and extract sensitive data
- **Status**: Recently patched by Apple in iOS 18, breaking precedent for emergency security updates
- **CVE ID**: Not specified

### Device Code OAuth 2.0 Phishing
- **Description**: Abuse of the OAuth 2.0 Device Authorization Grant flow to hijack user accounts through phishing
- **Impact**: Account takeover leading to unauthorized access to cloud services and corporate resources
- **Status**: Actively exploited with attacks surging 37 times this year due to proliferation of attack kits

### PHP Web Shell Cookie-Control Technique
- **Description**: HTTP cookies used as a control channel for PHP-based web shells on Linux servers
- **Impact**: Remote code execution and persistent access to compromised Linux servers through cron job persistence
- **Status**: Actively used by threat actors for maintaining long-term access to compromised systems

## Affected Systems and Products

- **Next.js Applications**: 766 confirmed compromised hosts running vulnerable Next.js frameworks
- **iOS Devices**: iOS versions prior to iOS 18 vulnerable to DarkSword exploitation tool
- **OAuth 2.0 Implementations**: Applications and services using Device Authorization Grant flow
- **Linux Servers**: Systems running PHP applications vulnerable to cookie-controlled web shell attacks
- **Axios npm Package**: JavaScript library compromised in supply chain attack
- **European Government Systems**: Diplomatic and government organizations targeted by TA416
- **Drift Protocol**: Solana-based decentralized exchange platform
- **Zendesk Platform**: Customer service platform used by Hims & Hers
- **Die Linke IT Systems**: German political party infrastructure
- **Hasbro Corporate Systems**: Toy manufacturer's business systems
- **European Commission Cloud**: EU cloud infrastructure exposing 30 entities

## Attack Vectors and Techniques

- **Social Engineering**: Highly-targeted campaigns against software maintainers and administrators
- **Supply Chain Compromise**: Malicious code injection into trusted software packages and repositories
- **OAuth Phishing**: Device code flow abuse for account takeover
- **Web Shell Deployment**: Cookie-controlled PHP shells with cron persistence
- **Ransomware Multi-Extortion**: Data theft combined with encryption for increased pressure
- **Repository Poisoning**: Fake GitHub repositories distributing malware disguised as legitimate tools
- **Browser Extension Scanning**: JavaScript-based fingerprinting of installed browser extensions
- **Administrative Privilege Escalation**: Exploitation of security council powers in DeFi platforms

## Threat Actor Activities

- **UNC1069 (North Korean)**: Conducted sophisticated social engineering campaign against Axios maintainer leading to npm supply chain compromise
- **DPRK-linked Groups**: Executed $285 million theft from Drift Protocol using durable nonce social engineering attack
- **TA416 (Chinese APT)**: Resumed targeting of European government and diplomatic organizations after two-year hiatus, using PlugX malware and OAuth-based phishing
- **Qilin Ransomware Group**: Attacked Die Linke German political party, stealing sensitive data and disrupting IT systems
- **TeamPCP**: Supply chain attacks expanding with involvement from ShinyHunters and Lapsus$ groups creating attribution confusion
- **SparkCat Operators**: Deployed new malware variant on iOS and Android app stores targeting cryptocurrency wallet recovery phrases
- **Vidar Malware Distributors**: Exploiting Claude Code leak to distribute information-stealing malware through fake GitHub repositories