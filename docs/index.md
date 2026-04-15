# Exploitation Report

The cybersecurity landscape is experiencing intense exploitation activity with multiple zero-day vulnerabilities under active attack. Microsoft's April 2026 Patch Tuesday addressed 167 security flaws including two actively exploited zero-days, while CISA has added six new vulnerabilities to its Known Exploited Vulnerabilities catalog affecting Fortinet, Microsoft, and Adobe products. Critical remote code execution flaws are being exploited in ShowDoc servers (CVE-2025-0520), Adobe Acrobat/Reader products, and PHP Composer package manager. Additionally, sophisticated supply chain attacks are targeting users through malicious Chrome extensions, fake cryptocurrency applications, and Android remote access trojans distributed via social media platforms.

## Active Exploitation Details

### Microsoft Zero-Day Vulnerabilities
- **Description**: Two zero-day vulnerabilities in Microsoft products are being actively exploited in the wild
- **Impact**: Attackers can achieve privilege escalation and compromise Windows systems
- **Status**: Patched in April 2026 Patch Tuesday update (KB5082200, KB5083769, KB5082052)

### ShowDoc Remote Code Execution Vulnerability
- **Description**: Critical security vulnerability in ShowDoc document management and collaboration service
- **Impact**: Remote code execution on unpatched servers
- **Status**: Actively exploited in the wild against unpatched installations
- **CVE ID**: CVE-2025-0520

### Adobe Acrobat/Reader Zero-Day
- **Description**: Zero-day vulnerability in Adobe Acrobat and Reader products exploited through maliciously crafted PDF files
- **Impact**: Code execution through PDF file exploitation
- **Status**: Actively exploited for at least four months before patching

### PHP Composer Vulnerabilities
- **Description**: Two high-severity security vulnerabilities in Composer package manager for PHP
- **Impact**: Arbitrary command execution if successfully exploited
- **Status**: Patches released

### wolfSSL Certificate Verification Flaw
- **Description**: Critical vulnerability in wolfSSL SSL/TLS library affecting certificate verification
- **Impact**: Weakened security through improper verification of hash algorithms in ECDSA signature checking
- **Status**: Enables use of forged certificates

## Affected Systems and Products

- **Microsoft Windows**: All versions affected by 167 vulnerabilities, including Windows 10 and Windows 11
- **SharePoint Server**: Affected by zero-day vulnerability
- **Adobe Acrobat and Reader**: Vulnerable to zero-day PDF exploitation
- **PHP Composer**: Package manager affected by command execution flaws
- **ShowDoc**: Document management platform with RCE vulnerability
- **wolfSSL Library**: SSL/TLS library with certificate verification issues
- **Chrome Web Store**: Over 100 malicious extensions targeting user credentials
- **Android Devices**: Affected by Mirax RAT distributed through Meta advertising platforms
- **Apple App Store**: Compromised by fake Ledger Live application

## Attack Vectors and Techniques

- **Malicious PDF Files**: Exploiting Adobe zero-day through crafted PDF documents
- **Supply Chain Attacks**: Malicious Chrome extensions stealing OAuth2 tokens and deploying backdoors
- **Social Engineering**: Fake cryptocurrency applications distributed through official app stores
- **Remote Desktop Protocol Abuse**: Phishing attacks using malicious .rdp files
- **Bring Your Own Vulnerable Driver (BYOVD)**: EDR-killer techniques for security bypass
- **Search Engine Poisoning**: AI-generated content used for scareware distribution
- **Meta Advertising Platforms**: Mirax Android RAT distribution reaching 220,000 accounts
- **Salesforce Misconfiguration**: Data breach vector affecting McGraw-Hill systems

## Threat Actor Activities

- **ShinyHunters**: Extortion gang leaking stolen Rockstar Games analytics data following Anodot security incident
- **Chrome Extension Operators**: Coordinated campaign using 108 malicious extensions with shared C2 infrastructure affecting 20,000 users
- **Kraken Exchange Attackers**: Cybercrime group conducting extortion following insider breach with threats to release client data videos
- **Mirax RAT Operators**: Targeting Spanish-speaking countries, converting Android devices into SOCKS5 proxies
- **Fake Ledger Attackers**: Operators who stole $9.5 million in cryptocurrency from 50 victims using malicious macOS application
- **Basic-Fit Breach Actors**: Hackers who compromised fitness giant's systems affecting 1 million members