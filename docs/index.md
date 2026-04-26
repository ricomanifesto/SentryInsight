# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms and services with several high-impact vulnerabilities under active attack. The most severe include rapid exploitation of the LMDeploy CVE-2026-33626 vulnerability within 13 hours of disclosure, persistent malware on Cisco firewall devices surviving security patches, active attacks against over 10,000 vulnerable Zimbra servers, and widespread exploitation of WordPress plugin vulnerabilities. Threat actors are leveraging sophisticated social engineering campaigns through Microsoft Teams, compromising npm packages, and deploying custom malware suites while Chinese state-sponsored groups are expanding their targeting scope across multiple regions.

## Active Exploitation Details

### LMDeploy High-Severity Vulnerability
- **Description**: A high-severity security flaw in LMDeploy, an open-source toolkit for compressing, deploying, and serving Large Language Models (LLMs)
- **Impact**: Allows unauthorized access to LLM deployment infrastructure and potential data compromise
- **Status**: Under active exploitation in the wild less than 13 hours after public disclosure
- **CVE ID**: CVE-2026-33626

### Zimbra Collaboration Suite Cross-Site Scripting
- **Description**: Cross-site scripting (XSS) security flaw affecting Zimbra Collaboration Suite instances
- **Impact**: Enables attackers to execute malicious scripts in user browsers and potentially steal credentials
- **Status**: Currently being exploited in ongoing attacks against over 10,000 exposed servers

### Breeze Cache WordPress Plugin File Upload Vulnerability
- **Description**: Critical vulnerability in the Breeze Cache plugin for WordPress allowing arbitrary file uploads
- **Impact**: Permits uploading malicious files on the server without authentication, leading to full server compromise
- **Status**: Currently under active exploitation by hackers

### Pack2TheRoot Linux Privilege Escalation
- **Description**: Vulnerability in the PackageKit daemon that allows local Linux users to gain elevated permissions
- **Impact**: Enables local users to install or remove system packages and achieve root access
- **Status**: Recently disclosed vulnerability with potential for exploitation

### Cisco Firepower Persistent Malware
- **Description**: Firestarter malware persisting on Cisco Firepower and Secure Firewall devices running Adaptive Security Appliance (ASA) software
- **Impact**: Maintains persistent access to critical network infrastructure even after security updates
- **Status**: Confirmed compromise of federal civilian agency device, survives security patches and updates

## Affected Systems and Products

- **LMDeploy**: Open-source toolkit for LLM deployment and serving
- **Zimbra Collaboration Suite**: Over 10,000 exposed instances vulnerable to XSS attacks
- **WordPress Breeze Cache Plugin**: WordPress caching plugin with critical file upload vulnerability
- **Linux PackageKit**: Package management system affected by privilege escalation flaw
- **Cisco Firepower/ASA**: Network security appliances compromised by persistent Firestarter malware
- **Microsoft Teams**: Platform abused for social engineering attacks deploying SNOW malware
- **Bitwarden CLI npm Package**: Temporarily compromised developer tool package
- **Apple App Store**: 26 malicious FakeWallet applications targeting cryptocurrency users
- **SumatraPDF**: Trojanized version used to deploy AdaptixC2 malware

## Attack Vectors and Techniques

- **Social Engineering via Microsoft Teams**: UNC6692 impersonates IT help desk personnel to deploy custom malware
- **Supply Chain Compromise**: Malicious packages uploaded to npm repository targeting developer credentials
- **Trojanized Software**: Legitimate applications modified to deliver backdoors and command-and-control tools
- **Persistent Malware**: Advanced techniques allowing malware to survive system updates and patches
- **File Upload Exploitation**: Direct server compromise through unrestricted file upload vulnerabilities
- **Mobile App Store Abuse**: Fake cryptocurrency wallet applications distributed through official channels
- **Phishing Campaigns**: AI-enhanced and personalized phishing attacks increasing in sophistication
- **ClickFix Techniques**: North Korean groups using deceptive user interface tricks for initial access

## Threat Actor Activities

- **UNC6692**: Deploying custom SNOW malware suite through Microsoft Teams social engineering, targeting organizations with browser extensions, tunnelers, and backdoors
- **Tropic Trooper**: Chinese-speaking threat group using trojanized SumatraPDF and GitHub infrastructure to deploy AdaptixC2 Beacon, expanding targeting to home routers and Japanese organizations
- **Chinese State-Sponsored APTs**: Multiple groups conducting espionage operations against Mongolia using cloud services like Microsoft Outlook, Slack, and Discord for command and control
- **Lazarus Group**: North Korean APT targeting macOS users through ClickFix techniques, focusing on Mac-centric organizations and high-value leaders
- **BlackFile Extortion Group**: New financially motivated group conducting data theft and extortion attacks against retail and hospitality sectors since February 2026
- **ShinyHunters**: Extortion group threatening to leak stolen ADT customer data unless ransom demands are met
- **Trigona Ransomware Operators**: Using custom command-line tools for faster and more efficient data exfiltration from compromised environments