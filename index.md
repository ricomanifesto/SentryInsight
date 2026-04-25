# Exploitation Report

Multiple critical vulnerabilities are currently being actively exploited across various platforms and applications. The most significant threats include the Firestarter malware persisting on Cisco Firepower devices despite security patches, a rapid exploitation of the LMDeploy CVE-2026-33626 vulnerability within 13 hours of disclosure, and widespread attacks targeting over 10,000 vulnerable Zimbra servers. Additionally, attackers are exploiting the Pack2TheRoot vulnerability in Linux systems, WordPress plugin vulnerabilities, and conducting sophisticated supply chain attacks through compromised development tools. These exploits demonstrate attackers' ability to rapidly weaponize newly disclosed vulnerabilities and maintain persistence even after patching attempts.

## Active Exploitation Details

### Firestarter Malware on Cisco Devices
- **Description**: A custom malware called Firestarter that persists on Cisco Firepower and Secure Firewall devices running Adaptive Security Appliance (ASA) software
- **Impact**: Provides backdoor access to network infrastructure devices and survives security patches and updates
- **Status**: Active exploitation confirmed by CISA on federal civilian agency devices; malware persists despite patching efforts

### LMDeploy Vulnerability
- **Description**: High-severity security flaw in LMDeploy, an open-source toolkit for compressing, deploying, and serving Large Language Models
- **Impact**: Allows attackers to exploit machine learning deployment infrastructure
- **Status**: Actively exploited in the wild within 13 hours of public disclosure
- **CVE ID**: CVE-2026-33626

### Pack2TheRoot Linux Vulnerability
- **Description**: Vulnerability in the PackageKit daemon that allows local Linux users to escalate privileges
- **Impact**: Enables local users to install or remove system packages and gain root permissions
- **Status**: Newly disclosed vulnerability with potential for exploitation

### Zimbra Cross-Site Scripting Vulnerability
- **Description**: Cross-site scripting (XSS) security flaw in Zimbra Collaboration Suite (ZCS)
- **Impact**: Allows attackers to execute malicious scripts in user browsers and potentially steal credentials
- **Status**: Over 10,000 Zimbra servers currently vulnerable and under active attack

### Breeze Cache WordPress Plugin Vulnerability
- **Description**: Critical file upload vulnerability in the Breeze Cache plugin for WordPress
- **Impact**: Allows uploading arbitrary files on the server without authentication, potentially leading to full website compromise
- **Status**: Actively being exploited by attackers

## Affected Systems and Products

- **Cisco Firepower and Secure Firewall**: Devices running Adaptive Security Appliance (ASA) software affected by persistent Firestarter malware
- **LMDeploy**: Open-source toolkit for machine learning model deployment
- **Linux Systems**: PackageKit daemon vulnerability affects various Linux distributions
- **Zimbra Collaboration Suite**: Over 10,000 instances exposed online and vulnerable to XSS attacks
- **WordPress**: Websites using the Breeze Cache plugin vulnerable to file upload attacks
- **Bitwarden CLI**: Command-line interface compromised in supply chain attack
- **Checkmarx KICS**: Docker images, VSCode and Open VSX extensions compromised
- **Apple App Store**: 26 malicious cryptocurrency wallet applications targeting iOS users

## Attack Vectors and Techniques

- **Persistent Malware**: Firestarter malware survives security patches and system updates on network infrastructure
- **Rapid Exploitation**: Attackers weaponized LMDeploy vulnerability within hours of public disclosure
- **Privilege Escalation**: Pack2TheRoot exploits PackageKit daemon for local privilege escalation to root
- **Cross-Site Scripting**: Mass exploitation of Zimbra XSS vulnerability across thousands of servers
- **Unauthenticated File Upload**: Breeze Cache plugin exploited for arbitrary file uploads without authentication
- **Supply Chain Compromise**: Multiple development tools and packages compromised to steal developer credentials
- **Social Engineering**: Teams-based attacks impersonating IT help desk to deploy malware
- **Trojanized Software**: Legitimate applications like SumatraPDF weaponized for malware delivery

## Threat Actor Activities

- **CISA Alert**: Federal agencies warned about Firestarter malware persistence on critical infrastructure
- **BlackFile Group**: New financially motivated group conducting data theft and extortion attacks against retail and hospitality organizations since February 2026
- **Tropic Trooper**: Chinese APT group targeting home routers, Japanese organizations, and Chinese-speaking individuals using trojanized PDF readers
- **Lazarus Group**: North Korean APT leveraging ClickFix techniques to target macOS users and high-value leaders
- **UNC6692**: Previously undocumented threat group using Microsoft Teams social engineering to deploy SNOW malware
- **Chinese APT Groups**: Multiple groups conducting espionage operations against Mongolia using cloud services and industrializing botnet operations
- **Myanmar Criminal Ring**: 29 individuals charged for financial fraud targeting US citizens through fake investment sites