# Exploitation Report

Critical exploitation activity continues across multiple platforms with several zero-day vulnerabilities under active attack. Microsoft addressed two zero-day vulnerabilities in their April 2026 Patch Tuesday, while Adobe patched CVE-2026-34621, a zero-day in Acrobat Reader that has been exploited since at least December. Additionally, CVE-2025-0520 affecting ShowDoc servers is seeing widespread exploitation, and CISA has added six new vulnerabilities to their Known Exploited Vulnerabilities catalog affecting Fortinet, Microsoft, and Adobe products.

## Active Exploitation Details

### Microsoft Zero-Day Vulnerabilities
- **Description**: Two zero-day vulnerabilities addressed in Microsoft's April 2026 Patch Tuesday affecting Windows systems
- **Impact**: Critical security compromises allowing attackers to exploit unpatched Windows systems
- **Status**: Patches available through Windows 10 KB5082200 extended security update and Windows 11 cumulative updates KB5083769 & KB5082052

### Adobe Acrobat Reader Zero-Day
- **Description**: Critical vulnerability in Adobe Acrobat and Reader exploited through maliciously crafted PDF files
- **Impact**: Attackers can execute arbitrary code through compromised PDF documents
- **Status**: Emergency security update released after months of active exploitation
- **CVE ID**: CVE-2026-34621

### ShowDoc Remote Code Execution
- **Description**: Critical remote code execution vulnerability in ShowDoc document management service popular in China
- **Impact**: Complete system compromise allowing arbitrary command execution on unpatched servers
- **Status**: Under active exploitation in the wild with widespread targeting of vulnerable instances
- **CVE ID**: CVE-2025-0520

### PHP Composer Vulnerabilities
- **Description**: Two high-severity security vulnerabilities in Composer package manager for PHP
- **Impact**: Arbitrary command execution capabilities for attackers
- **Status**: Patches released to address exploitation vectors

## Affected Systems and Products

- **Microsoft Windows**: Windows 10 and Windows 11 systems affected by two zero-day vulnerabilities
- **Adobe Acrobat Reader**: All versions vulnerable to PDF-based exploitation until emergency patch
- **ShowDoc Servers**: Document management platforms running vulnerable versions under active attack
- **PHP Composer**: Package manager installations vulnerable to command execution
- **Fortinet Products**: Multiple products added to CISA KEV catalog for active exploitation
- **Android Devices**: Mirax RAT targeting devices in Spanish-speaking countries through social media campaigns
- **Chrome Extensions**: 108 malicious extensions affecting 20,000 users with data theft capabilities
- **wolfSSL Library**: SSL/TLS implementations vulnerable to certificate forgery attacks

## Attack Vectors and Techniques

- **Malicious PDF Exploitation**: Crafted PDF files targeting Adobe Reader zero-day for code execution
- **Social Media Campaigns**: Meta platform advertisements distributing Mirax Android RAT to 220,000+ accounts
- **Browser Extension Abuse**: Malicious Chrome extensions stealing Google and Telegram data through coordinated C2 infrastructure
- **Fake Mobile Applications**: Fraudulent Ledger Live app on Apple App Store stealing $9.5 million in cryptocurrency
- **Supply Chain Attacks**: Malicious Axios package targeting OpenAI's GitHub Actions workflow
- **Configuration Exploitation**: Salesforce misconfigurations leading to data breaches at McGraw-Hill
- **Session Hijacking**: New "Storm" infostealer bypassing MFA through server-side decryption techniques
- **AI-Generated Content**: Pushpaganda schemes using AI to create deceptive content for ad fraud

## Threat Actor Activities

- **APT41**: Deploying zero-detection backdoors to harvest cloud credentials from AWS, Google, Azure, and Alibaba environments
- **ShinyHunters**: Extortion gang leaking stolen Rockstar Games analytics data following Anodot breach
- **JanelaRAT Operators**: Targeting Latin American banks with 14,739 attacks recorded in Brazil during 2025
- **W3LL Phishing Network**: Dismantled global operation responsible for $20 million in fraud attempts before FBI takedown
- **Chrome Extension Threat Actors**: Coordinated campaign managing 108 malicious browser extensions with shared C2 infrastructure
- **Mirax RAT Distributors**: Spanish-speaking threat actors leveraging Meta advertising platforms for large-scale mobile device compromise