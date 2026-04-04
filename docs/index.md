# Exploitation Report

A significant wave of exploitation activity has emerged across multiple attack vectors, with threat actors leveraging both supply chain compromises and vulnerability exploits to achieve widespread impact. The most critical developments include North Korean threat groups conducting sophisticated social engineering campaigns targeting npm maintainers, the exploitation of CVE-2025-55182 affecting 766 Next.js hosts for credential harvesting, and the TeamPCP group's supply chain attacks compromising multiple European organizations. Additionally, advanced persistent threat actors are deploying novel techniques including cookie-controlled PHP web shells and OAuth-based phishing campaigns targeting government entities.

## Active Exploitation Details

### React2Shell Vulnerability in Next.js
- **Description**: A vulnerability in Next.js framework being actively exploited for large-scale credential harvesting operations
- **Impact**: Attackers can steal database credentials, SSH private keys, and Amazon Web Services credentials from compromised hosts
- **Status**: Active exploitation observed with 766 Next.js hosts breached in ongoing campaign
- **CVE ID**: CVE-2025-55182

### DarkSword iOS Mobile Exploitation Tool
- **Description**: A severe mobile OS-cracking tool targeting iOS devices that prompted Apple to break precedent in patching procedures
- **Impact**: Allows attackers to crack iOS security protections and gain unauthorized access to mobile devices
- **Status**: Apple has released patches for iOS 18, breaking from normal update practices to address the threat

### Cookie-Controlled PHP Web Shells
- **Description**: Sophisticated web shells using HTTP cookies as control channels for remote code execution on Linux servers
- **Impact**: Enables persistent access to compromised servers with cron-based persistence mechanisms
- **Status**: Active deployment observed by Microsoft Defender teams

## Affected Systems and Products

- **Next.js Framework**: 766 hosts confirmed compromised through React2Shell vulnerability exploitation
- **iOS Devices**: All iOS 18 systems vulnerable to DarkSword exploitation tool
- **Linux Servers**: PHP-based web applications susceptible to cookie-controlled web shell attacks
- **npm Package Ecosystem**: Axios package compromised through social engineering of maintainers
- **European Government Systems**: Multiple EU entities affected by TeamPCP supply chain attacks
- **Zendesk Platform**: Support ticket systems breached affecting Hims & Hers customer data
- **Chrome Browser**: 6,000+ extensions being scanned by LinkedIn for data collection
- **Drift Protocol**: Solana-based decentralized exchange platform losing $285 million
- **Windows Devices**: 254 servers locked in internal extortion plot

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Social engineering of open source maintainers to inject malicious code into widely-used packages
- **OAuth-Based Phishing**: Advanced phishing campaigns targeting authentication systems of government organizations
- **Cookie-Based Command and Control**: Novel technique using HTTP cookies to control PHP web shells and maintain persistence
- **Social Engineering**: Highly-targeted campaigns against cryptocurrency platforms and development teams
- **Multi-Extortion Ransomware**: Advanced ransomware operations combining encryption with data theft for increased pressure
- **Residential Proxy Abuse**: Using legitimate residential IP addresses to evade detection systems in 78% of malicious sessions
- **GitHub Repository Spoofing**: Creating fake repositories exploiting recent source code leaks to distribute malware

## Threat Actor Activities

- **TA416 (China-linked)**: Targeting European government and diplomatic organizations with PlugX malware and OAuth phishing since mid-2025
- **UNC1069 (North Korean)**: Conducting sophisticated social engineering campaigns against npm package maintainers for supply chain attacks
- **TeamPCP**: Executing widespread supply chain attacks affecting European Commission and 30+ EU entities
- **Qilin Ransomware Group**: Claiming responsibility for attacks against German political party Die Linke with sensitive data theft
- **DPRK-linked Groups**: Orchestrating $285 million cryptocurrency theft from Drift Protocol through social engineering
- **ShinyHunters and Lapsus$**: Taking credit for various breaches tied to TeamPCP supply chain attacks, creating confusion about attribution
- **SparkCat Operators**: Distributing new malware variants through official app stores targeting cryptocurrency wallet recovery phrases