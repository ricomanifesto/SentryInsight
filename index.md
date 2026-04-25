# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms and systems, with attackers demonstrating sophisticated persistence techniques and rapid vulnerability exploitation. The Firestarter malware has shown remarkable persistence on Cisco Firepower and Secure Firewall devices, surviving both software updates and security patches. Threat actors are exploiting vulnerabilities within hours of public disclosure, as demonstrated by the LMDeploy toolkit exploitation occurring just 13 hours after vulnerability disclosure. Active campaigns include the deployment of sophisticated backdoors on federal infrastructure, supply chain compromises targeting developer tools, and extensive exploitation of WordPress plugin vulnerabilities.

## Active Exploitation Details

### Firestarter Malware on Cisco Firewalls
- **Description**: Custom malware persisting on Cisco Firepower and Secure Firewall devices running Adaptive Security Appliance (ASA) software
- **Impact**: Maintains persistent access to federal civilian agency infrastructure, survives security patches and updates
- **Status**: Active exploitation confirmed on federal devices with malware demonstrating advanced persistence capabilities

### LMDeploy Toolkit Vulnerability
- **Description**: High-severity security flaw in LMDeploy open-source toolkit for compressing, deploying, and serving LLMs
- **Impact**: Allows attackers to exploit LLM deployment infrastructure
- **Status**: Actively exploited within 13 hours of public disclosure
- **CVE ID**: CVE-2026-33626

### Zimbra Cross-Site Scripting Vulnerability
- **Description**: XSS security flaw affecting Zimbra Collaboration Suite (ZCS) instances
- **Impact**: Enables cross-site scripting attacks against email and collaboration systems
- **Status**: Ongoing attacks confirmed with over 10,000 vulnerable servers exposed online

### Pack2TheRoot Linux Privilege Escalation
- **Description**: Vulnerability in PackageKit daemon allowing local privilege escalation
- **Impact**: Enables local Linux users to install/remove system packages and gain root permissions
- **Status**: Newly discovered vulnerability with potential for widespread exploitation

### Breeze Cache WordPress Plugin File Upload
- **Description**: Critical vulnerability allowing arbitrary file uploads without authentication
- **Impact**: Complete server compromise through unauthenticated file upload
- **Status**: Active exploitation confirmed by threat actors

## Affected Systems and Products

- **Cisco Firepower and Secure Firewall**: Devices running Adaptive Security Appliance (ASA) software affected by persistent Firestarter malware
- **LMDeploy Toolkit**: Open-source LLM deployment infrastructure vulnerable to rapid exploitation
- **Zimbra Collaboration Suite**: Over 10,000 instances exposed to XSS attacks
- **Linux Systems**: PackageKit daemon vulnerability affects multiple Linux distributions
- **WordPress Sites**: Breeze Cache plugin installations vulnerable to file upload attacks
- **Bitwarden CLI**: npm package temporarily compromised with credential-stealing payload
- **Checkmarx KICS**: Docker images, VSCode and Open VSX extensions compromised in supply chain attack
- **Apple App Store**: 26 malicious FakeWallet apps targeting cryptocurrency users

## Attack Vectors and Techniques

- **Persistent Backdoor Deployment**: Firestarter malware survives system updates and patches through advanced persistence mechanisms
- **Rapid Exploitation**: Attackers exploiting vulnerabilities within hours of public disclosure
- **Supply Chain Compromise**: Targeting developer tools and package repositories to spread malicious code
- **Social Engineering via Microsoft Teams**: UNC6692 threat group impersonating IT help desk to deploy SNOW malware
- **Trojanized Software Distribution**: Tropic Trooper using compromised SumatraPDF to deploy AdaptixC2 Beacon
- **Mobile App Store Infiltration**: FakeWallet apps bypassing Apple App Store security to steal cryptocurrency credentials
- **Vishing Campaigns**: BlackFile extortion group using voice phishing against retail and hospitality organizations
- **Cloud Platform Abuse**: Chinese APT groups leveraging Microsoft Outlook, Slack, Discord, and file.io for command and control

## Threat Actor Activities

- **Firestarter Operators**: Targeting federal civilian agency infrastructure with persistent malware capable of surviving security updates
- **ShinyHunters**: Conducting extortion campaigns against major corporations like ADT with data leak threats
- **BlackFile Group**: New financially motivated group conducting data theft and extortion attacks against retail and hospitality sectors since February 2026
- **UNC6692**: Deploying SNOW malware through Microsoft Teams social engineering campaigns impersonating IT help desk personnel
- **Tropic Trooper**: Chinese APT group expanding operations to target home routers and Japanese organizations using trojanized software
- **Lazarus Group**: North Korean APT leveraging ClickFix techniques to target macOS users and Mac-centric organizations
- **Chinese APT Groups**: Multiple groups using industrialized botnet operations and cloud service abuse for espionage operations against Mongolia
- **Trigona Ransomware**: Deploying custom exfiltration tools for more efficient data theft operations