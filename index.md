# Exploitation Report

Critical cybersecurity threats are actively exploiting vulnerabilities across multiple platforms, with several high-severity flaws being weaponized in the wild. CISA has added four new vulnerabilities to its Known Exploited Vulnerabilities catalog affecting SimpleHelp, Samsung MagicINFO 9 Server, and D-Link DIR-823X series routers. A concerning trend shows attackers rapidly exploiting newly disclosed vulnerabilities, with the LMDeploy flaw being weaponized within 13 hours of public disclosure. Additional active exploitation campaigns target Cisco firewall devices, Zimbra servers, and WordPress plugins, while sophisticated threat actors are deploying custom malware suites and compromising trusted software packages.

## Active Exploitation Details

### LMDeploy Security Flaw
- **Description**: High-severity vulnerability in LMDeploy, an open-source toolkit for compressing, deploying, and serving Large Language Models
- **Impact**: Allows attackers to compromise systems running LMDeploy infrastructure
- **Status**: Under active exploitation within 13 hours of public disclosure
- **CVE ID**: CVE-2026-33626

### Zimbra Cross-Site Scripting Vulnerability
- **Description**: Cross-site scripting (XSS) security flaw affecting Zimbra Collaboration Suite instances
- **Impact**: Enables malicious code execution in victim browsers and potential account compromise
- **Status**: Ongoing attacks against over 10,000 vulnerable servers exposed online

### Breeze Cache WordPress Plugin File Upload Vulnerability
- **Description**: Critical vulnerability in the Breeze Cache plugin for WordPress allowing arbitrary file uploads
- **Impact**: Allows attackers to upload malicious files without authentication, potentially leading to full website compromise
- **Status**: Currently being actively exploited by hackers

### CISA KEV Catalog Additions
- **Description**: Four vulnerabilities affecting SimpleHelp, Samsung MagicINFO 9 Server, and D-Link DIR-823X series routers
- **Impact**: Various security impacts depending on the specific vulnerability
- **Status**: Added to Known Exploited Vulnerabilities catalog with May 2026 federal deadline for patching

### Pack2TheRoot Linux Vulnerability
- **Description**: Vulnerability in the PackageKit daemon affecting Linux systems
- **Impact**: Allows local users to install or remove system packages and gain root permissions
- **Status**: Newly discovered vulnerability with potential for privilege escalation attacks

### Firestarter Malware on Cisco Devices
- **Description**: Custom malware persisting on Cisco Firepower and Secure Firewall devices running Adaptive Security Appliance (ASA)
- **Impact**: Maintains persistence through security updates and patches, providing ongoing network access
- **Status**: Active infections reported on federal civilian agency devices

## Affected Systems and Products

- **Cisco Firepower and Secure Firewall Devices**: Running Adaptive Security Appliance (ASA) or Firepower Threat Defense software
- **Zimbra Collaboration Suite**: Over 10,000 instances exposed online vulnerable to XSS attacks
- **WordPress Sites**: Running the Breeze Cache plugin with file upload vulnerabilities
- **LMDeploy Infrastructure**: Open-source toolkit deployments for Large Language Model services
- **Linux Systems**: PackageKit daemon implementations across various distributions
- **SimpleHelp**: Remote support software instances
- **Samsung MagicINFO 9 Server**: Digital signage management platforms
- **D-Link DIR-823X Series**: Consumer router models
- **Apple App Store**: 26 malicious cryptocurrency wallet applications
- **npm Package Registry**: Compromised @bitwarden/cli package
- **Microsoft Teams**: Platforms used for malware delivery via social engineering

## Attack Vectors and Techniques

- **Social Engineering via Microsoft Teams**: UNC6692 threat group impersonating IT help desk personnel to deploy SNOW malware suite
- **Supply Chain Attacks**: Compromise of trusted software packages including Bitwarden CLI npm package
- **Trojanized Software**: Distribution of malicious SumatraPDF readers and fake cryptocurrency wallet apps
- **Phishing Campaigns**: Chinese threat actors targeting NASA employees and defense software users
- **File Upload Exploitation**: Direct exploitation of WordPress plugin vulnerabilities for web shell deployment
- **Persistence Mechanisms**: Malware surviving security updates and patches on network infrastructure
- **Cross-Site Scripting**: Web-based attacks targeting Zimbra email server users
- **Privilege Escalation**: Local exploitation of Linux PackageKit vulnerabilities for root access
- **ClickFix Techniques**: Lazarus group targeting macOS users through deceptive user interface elements

## Threat Actor Activities

- **UNC6692**: Deploying custom SNOW malware suite including browser extensions, tunnelers, and backdoors via Microsoft Teams social engineering
- **Tropic Trooper**: Chinese APT group using trojanized SumatraPDF and GitHub for AdaptixC2 deployment, expanding operations to target home routers and Japanese organizations
- **Lazarus Group**: North Korean threat actors leveraging ClickFix techniques against macOS users and high-value organizational leaders
- **Chinese State-Sponsored Groups**: Multiple campaigns including spear-phishing against NASA employees and industrial-scale botnet operations for low-cost, deniable attacks
- **ShinyHunters**: Extortion group threatening ADT with data leaks unless ransom demands are met
- **BlackFile Extortion Group**: New financially motivated group targeting retail and hospitality organizations with data theft and extortion since February 2026
- **Trigona Ransomware Operators**: Using custom command-line exfiltration tools for faster and more efficient data theft from compromised environments
- **Myanmar-based Fraud Ring**: 29 individuals charged in financial fraud targeting US citizens through fake investment sites