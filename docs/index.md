# Exploitation Report

The current threat landscape is marked by significant zero-day exploitation activity and large-scale malicious campaigns targeting major platforms. Two critical zero-day vulnerabilities in Microsoft Windows have been actively exploited in the wild, with Microsoft addressing them in the April 2026 Patch Tuesday alongside 165 other flaws. Adobe has also issued emergency patches for an actively exploited zero-day in Acrobat Reader that has been under attack for at least four months. Meanwhile, cybercriminals are leveraging legitimate platforms for widespread distribution of malicious software, with over 100 malicious Chrome extensions targeting user credentials and cryptocurrency wallets, a fake Ledger Live app stealing $9.5 million in cryptocurrency, and sophisticated campaigns using AI-generated content and social media manipulation.

## Active Exploitation Details

### Microsoft Windows Zero-Day Vulnerabilities
- **Description**: Two zero-day vulnerabilities in Windows operating systems that were being actively exploited in the wild
- **Impact**: Attackers could potentially gain unauthorized access to systems and compromise user data
- **Status**: Patched in Microsoft's April 2026 Patch Tuesday update (KB5082200)

### Adobe Acrobat and Reader Zero-Day
- **Description**: Critical vulnerability in Adobe Acrobat and Reader that enables exploitation through maliciously crafted PDF files
- **Impact**: Attackers can execute arbitrary code and compromise systems when users open malicious PDF documents
- **Status**: Emergency patch released after months of active exploitation
- **CVE ID**: CVE-2026-34621

### ShowDoc Remote Code Execution Vulnerability
- **Description**: Critical security flaw in ShowDoc document management service enabling remote code execution
- **Impact**: Attackers can execute arbitrary commands on vulnerable servers
- **Status**: Actively exploited on unpatched servers
- **CVE ID**: CVE-2025-0520

### PHP Composer Vulnerabilities
- **Description**: Two high-severity security vulnerabilities in Composer package manager for PHP
- **Impact**: Successful exploitation could result in arbitrary command execution
- **Status**: Patches have been released

## Affected Systems and Products

- **Microsoft Windows 10**: Affected by zero-day vulnerabilities, extended security updates available via KB5082200
- **Microsoft Windows 11**: Security updates released via KB5083769 and KB5082052 for multiple versions
- **Adobe Acrobat and Reader**: All versions affected by zero-day vulnerability CVE-2026-34621
- **ShowDoc**: Document management service with actively exploited RCE vulnerability
- **PHP Composer**: Package manager with high-severity command execution flaws
- **Google Chrome**: Over 100 malicious extensions targeting OAuth2 tokens and user data
- **Apple App Store**: Hosting fake Ledger Live application for cryptocurrency theft
- **Salesforce**: Configuration vulnerabilities exploited in McGraw-Hill breach
- **wolfSSL Library**: Critical vulnerability affecting certificate verification
- **Fortinet, Microsoft, and Adobe Software**: Six vulnerabilities added to CISA's Known Exploited Vulnerabilities catalog

## Attack Vectors and Techniques

- **Malicious Browser Extensions**: Chrome extensions stealing Google OAuth2 Bearer tokens and deploying backdoors
- **Supply Chain Attacks**: Malicious Axios package targeting GitHub Actions workflows and code-signing certificates
- **PDF-based Attacks**: Crafted PDF files exploiting Adobe zero-day vulnerability
- **App Store Impersonation**: Fake Ledger Live app mimicking legitimate cryptocurrency wallet software
- **BYOVD (Bring Your Own Vulnerable Driver)**: EDR-killer techniques using vulnerable drivers to bypass security
- **Social Engineering**: W3LL phishing platform providing comprehensive phishing-as-a-service capabilities
- **AI-Generated Content**: Pushpaganda scams using artificial intelligence to create deceptive content and manipulate search results
- **Mobile Malware**: Mirax Android RAT converting devices into SOCKS5 proxies via Meta advertising platforms

## Threat Actor Activities

- **Chrome Extension Campaign**: Cluster of 108 malicious extensions coordinated through shared command-and-control infrastructure, affecting over 20,000 users
- **ShinyHunters**: Extortion gang responsible for leaking Rockstar Games analytics data following Anodot security incident
- **Mirax RAT Operators**: Targeting Spanish-speaking countries with Android malware, reaching 220,000 accounts across Facebook, Instagram, and Messenger
- **JanelaRAT Campaign**: Banking malware targeting Latin American financial institutions with 14,739 attacks in Brazil during 2025
- **W3LL Platform Developers**: Global phishing service operators arrested by FBI and Indonesian authorities
- **Cryptocurrency Thieves**: Sophisticated actors deploying fake Ledger Live app and stealing $9.5 million from 50 victims in days
- **McGraw-Hill Attackers**: Threat actors exploiting Salesforce misconfigurations for data access and extortion
- **Basic-Fit Breach**: Hackers compromising fitness giant's systems and accessing one million customer records