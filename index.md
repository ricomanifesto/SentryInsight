# Exploitation Report

Critical security vulnerabilities are currently under active exploitation, posing significant risks to enterprise systems and customer data. Adobe Commerce platforms face immediate threats through CVE-2025-54236, enabling attackers to compromise customer accounts. Meanwhile, SAP has addressed multiple critical NetWeaver vulnerabilities with CVSS scores reaching 10.0, alongside previously exploited S/4HANA flaws. Microsoft's September 2025 Patch Tuesday addressed 81 vulnerabilities, including two publicly disclosed zero-day vulnerabilities, with nearly half enabling privilege escalation. Additionally, supply chain attacks continue to evolve, with threat actors compromising NPM packages affecting over 2 billion weekly downloads, while Docker API exposures are being exploited for botnet infrastructure development.

## Active Exploitation Details

### Adobe Commerce Account Takeover Vulnerability
- **Description**: Critical security flaw in Adobe Commerce and Magento Open Source platforms allowing unauthorized access to customer accounts
- **Impact**: Complete customer account compromise, unauthorized access to personal and payment information
- **Status**: Active exploitation warnings issued by Adobe, patches available
- **CVE ID**: CVE-2025-54236

### SAP NetWeaver Critical Vulnerabilities
- **Description**: Multiple critical security flaws in SAP NetWeaver with maximum CVSS scores
- **Impact**: Remote code execution and arbitrary file upload capabilities
- **Status**: Security updates released by SAP on Tuesday
- **CVE ID**: CVSS scores up to 10.0 mentioned but specific CVE IDs not provided

### Microsoft Zero-Day Vulnerabilities
- **Description**: Two publicly disclosed zero-day vulnerabilities included in September 2025 Patch Tuesday
- **Impact**: Various attack vectors including privilege escalation
- **Status**: Security updates released, previously under active exploitation

### NPM Supply Chain Attack
- **Description**: Threat actors compromised Qix's NPM account through phishing and published malicious versions of 18 popular open source packages
- **Impact**: Affects over 2 billion weekly downloads, potential widespread compromise of JavaScript applications
- **Status**: Attack discovered and mitigated, packages removed

## Affected Systems and Products

- **Adobe Commerce and Magento Open Source**: All versions vulnerable to account takeover attacks
- **SAP NetWeaver**: Critical vulnerabilities with CVSS 10.0 scores affecting code execution
- **SAP S/4HANA**: Previously exploited flaws now patched
- **Microsoft Windows**: 81 vulnerabilities addressed across Windows operating systems and software
- **NPM JavaScript Ecosystem**: 18 popular packages with over 2 billion weekly downloads compromised
- **Docker APIs**: Exposed Docker APIs being targeted for malicious infrastructure deployment
- **Qantas Customer Platform**: Third-party platform compromised leading to customer data exposure

## Attack Vectors and Techniques

- **Account Takeover**: Direct exploitation of Adobe Commerce authentication mechanisms
- **Remote Code Execution**: SAP NetWeaver vulnerabilities enable complete system compromise
- **Privilege Escalation**: Nearly half of Microsoft's patched vulnerabilities enable EoP attacks
- **Supply Chain Poisoning**: NPM account compromise leading to malicious package distribution
- **API Exploitation**: Exposed Docker APIs targeted for botnet infrastructure development
- **Third-Party Platform Compromise**: Indirect attacks through vendor systems to access customer data
- **Tor Network Obfuscation**: Attackers using Tor to hide activities in Docker API breaches

## Threat Actor Activities

- **Southeast Asian Scam Networks**: Continued operations despite financial sanctions, stealing over $10 billion from Americans in the previous year
- **NPM Supply Chain Attackers**: Sophisticated phishing campaigns targeting developer accounts for widespread package poisoning
- **Docker API Threat Actors**: Enhanced tooling development for complex botnet infrastructure deployment
- **Enterprise-Focused Groups**: Targeting high-value systems including SAP environments and Adobe Commerce platforms
- **Financial Crime Syndicates**: Operating from Burma and Cambodia despite increased sanctions and enforcement actions