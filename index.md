# Exploitation Report

A significant surge in sophisticated cyberattacks has emerged, featuring North Korean threat actors conducting high-profile supply chain compromises and financial theft operations. The most critical activities include the UNC1069 group's social engineering attack on the Axios npm package maintainer, resulting in a successful supply chain compromise, and a devastating $280-285 million cryptocurrency theft from the Drift Protocol platform. Additionally, the CVE-2025-55182 React2Shell vulnerability is being actively exploited to breach Next.js hosts for credential harvesting, while device code phishing attacks have surged 37 times this year. European government organizations face targeted campaigns from China-linked TA416 actors, and the TeamPCP threat group has successfully breached the European Commission's cloud infrastructure.

## Active Exploitation Details

### React2Shell Vulnerability in Next.js
- **Description**: A critical vulnerability in Next.js framework that allows attackers to execute remote code and gain initial access to web applications
- **Impact**: Enables credential harvesting, database access theft, SSH private key extraction, and AWS credentials compromise
- **Status**: Actively exploited in large-scale credential harvesting operations affecting 766 Next.js hosts
- **CVE ID**: CVE-2025-55182

### OAuth 2.0 Device Authorization Grant Flow Abuse
- **Description**: Exploitation of the OAuth device code flow to hijack user accounts through phishing campaigns
- **Impact**: Account takeover and unauthorized access to cloud services and applications
- **Status**: Active exploitation with attacks surging 37 times this year as new phishing kits spread online

### DarkSword iOS Exploit
- **Description**: A severe mobile operating system exploitation tool targeting iOS devices
- **Impact**: Complete compromise of iOS devices with capabilities to crack mobile OS protections
- **Status**: Previously unpatched but Apple has now released fixes for iOS 18

### PHP Web Shell Vulnerabilities on Linux Servers
- **Description**: Cookie-controlled PHP web shells that persist on Linux servers through cron jobs
- **Impact**: Remote code execution and persistent backdoor access to compromised systems
- **Status**: Actively observed by Microsoft Defender teams with ongoing exploitation

## Affected Systems and Products

- **Axios npm Package**: Popular HTTP client library compromised through social engineering of maintainer
- **Next.js Framework**: 766 hosts breached through React2Shell vulnerability exploitation
- **Drift Protocol**: Solana-based decentralized exchange platform losing $280-285 million
- **iOS Devices**: All versions prior to iOS 18 vulnerable to DarkSword exploitation tool
- **Linux Servers**: Systems running PHP applications vulnerable to cookie-controlled web shells
- **OAuth-enabled Applications**: Services using OAuth 2.0 Device Authorization Grant flow
- **European Commission Cloud**: Cloud infrastructure of EU entities compromised
- **Zendesk Platform**: Third-party customer service platform affecting Hims & Hers data
- **Chrome Browser Extensions**: Over 6,000 extensions being scanned by LinkedIn's hidden scripts

## Attack Vectors and Techniques

- **Social Engineering**: Sophisticated campaigns targeting software maintainers with fake Microsoft Teams error fixes
- **Supply Chain Compromise**: Injection of malicious code into legitimate npm packages and repositories
- **Device Code Phishing**: Abuse of OAuth device flow to trick users into authorizing malicious applications
- **Web Shell Deployment**: Cookie-controlled PHP backdoors with cron job persistence mechanisms
- **Credential Harvesting**: Large-scale operations to steal database credentials, SSH keys, and cloud access tokens
- **GitHub Repository Abuse**: Use of fake repositories to distribute Vidar infostealer malware
- **Browser Extension Scanning**: Hidden JavaScript scripts collecting device data and extension information

## Threat Actor Activities

- **UNC1069 (North Korean)**: Conducted sophisticated social engineering campaign against Axios maintainer leading to npm supply chain compromise
- **DPRK-linked Actors**: Executed $280-285 million cryptocurrency theft from Drift Protocol using Security Council power seizure
- **TA416 (China-linked)**: Targeting European government and diplomatic organizations with PlugX malware and OAuth-based phishing since mid-2025
- **TeamPCP**: Successfully breached European Commission cloud infrastructure affecting 30 EU entities, with connections to ShinyHunters and Lapsus$ groups
- **Qilin Ransomware**: Claimed responsibility for attack against Die Linke German political party with data theft threats
- **SparkCat Operators**: Deployed new malware variants on Apple App Store and Google Play Store targeting cryptocurrency wallet recovery phrases