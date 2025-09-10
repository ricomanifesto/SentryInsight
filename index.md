# Exploitation Report

Current security reports reveal several critical exploitation activities targeting enterprise environments and consumer platforms. Microsoft's September 2025 Patch Tuesday addressed 81 vulnerabilities including two actively exploited zero-day vulnerabilities that pose immediate threats to Windows systems. Meanwhile, Adobe has disclosed a critical vulnerability CVE-2025-54236 in its Magento eCommerce platform, dubbed "SessionReaper," which researchers describe as one of the most severe flaws in the platform's history. Additionally, a massive supply chain attack has compromised NPM packages with over 2 billion weekly downloads, while threat actors continue to exploit exposed Docker APIs through sophisticated botnets operating behind Tor networks.

## Active Exploitation Details

### Microsoft Windows Zero-Day Vulnerabilities
- **Description**: Two publicly disclosed zero-day vulnerabilities affecting Windows systems that are being actively exploited in the wild
- **Impact**: These vulnerabilities allow attackers to compromise Windows systems with potential for privilege escalation, remote code execution, or system compromise
- **Status**: Patched in Microsoft's September 2025 Patch Tuesday security updates

### Adobe SessionReaper Vulnerability
- **Description**: Critical vulnerability in Adobe Commerce and Magento Open Source platforms described as one of the most severe flaws in the platform's history
- **Impact**: Exploitation could lead to complete compromise of eCommerce platforms, potentially affecting customer data and business operations
- **Status**: Recently patched by Adobe
- **CVE ID**: CVE-2025-54236

### NPM Supply Chain Attack
- **Description**: Large-scale supply chain attack targeting NPM packages through compromised developer accounts
- **Impact**: Attackers gained access to publish poisoned versions of 18 popular open-source packages accounting for more than 2 billion weekly downloads
- **Status**: Active threat requiring immediate package verification and updates

### Docker API Exploitation
- **Description**: Threat actors targeting exposed Docker APIs with updated malicious tooling and enhanced functionality
- **Impact**: Compromised Docker environments could serve as foundation for complex botnets and infrastructure hijacking
- **Status**: Ongoing exploitation with attackers using Tor networks to hide their activities

## Affected Systems and Products

- **Microsoft Windows**: Windows 10 and Windows 11 systems vulnerable to two zero-day exploits
- **Adobe Commerce/Magento**: eCommerce platforms running vulnerable versions prior to security patches
- **NPM Ecosystem**: JavaScript developers and applications using compromised NPM packages
- **Docker Environments**: Exposed Docker API endpoints accessible from internet
- **Third-Party Platforms**: Qantas customers affected by third-party platform breach

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched Windows vulnerabilities for system compromise
- **Supply Chain Poisoning**: Compromising developer accounts to inject malicious code into trusted packages
- **API Exploitation**: Targeting misconfigured Docker APIs for container and infrastructure compromise
- **Tor Network Obfuscation**: Using Tor networks to hide malicious traffic and command and control communications
- **Third-Party Platform Compromise**: Exploiting vulnerabilities in partner platforms to access customer data

## Threat Actor Activities

- **NPM Package Attackers**: Sophisticated threat actors who phished developer credentials to compromise the Qix NPM account and poison 18 popular packages
- **Docker API Exploiters**: Advanced persistent actors developing botnet infrastructure through exposed Docker APIs while maintaining anonymity via Tor
- **Southeast Asian Scam Networks**: Large-scale cyber scam operations sanctioned by U.S. Treasury for stealing over $10 billion from Americans
- **Ransomware Administrators**: Ukrainian national Volodymyr Viktorovich Tymoshchuk charged for administering LockerGoga, MegaCortex, and Nefilim ransomware operations
- **BlackDB Marketplace Operator**: Kosovo national Liridon Masurica operating cybercrime marketplace BlackDB.cc since 2018