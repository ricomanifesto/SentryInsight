# Exploitation Report

The current threat landscape reveals significant active exploitation activity across multiple platforms and technologies. Microsoft addressed two zero-day vulnerabilities in its April 2026 Patch Tuesday update affecting 167 security flaws, while attackers continue exploiting a critical ShowDoc remote code execution vulnerability and Adobe zero-day vulnerability that has been under active attack for months. Additionally, threat actors are leveraging browser extension ecosystems, mobile platforms, and supply chain attacks to compromise user data and systems. Notable incidents include sophisticated attacks against cryptocurrency platforms, educational institutions, and fitness companies, demonstrating the broad scope of current exploitation campaigns.

## Active Exploitation Details

### Microsoft Zero-Day Vulnerabilities
- **Description**: Two zero-day vulnerabilities patched in Microsoft's April 2026 Patch Tuesday update affecting Windows and related software
- **Impact**: Attackers can exploit these vulnerabilities for privilege escalation and system compromise
- **Status**: Patches available as of April 2026 Patch Tuesday, actively exploited in the wild

### ShowDoc Remote Code Execution Vulnerability
- **Description**: Critical security vulnerability in ShowDoc document management and collaboration service popular in China
- **Impact**: Remote code execution capabilities allowing complete system compromise
- **Status**: Under active exploitation on unpatched servers
- **CVE ID**: CVE-2025-0520

### Adobe Acrobat and Reader Zero-Day
- **Description**: Zero-day vulnerability in Adobe Acrobat and Reader exploited through maliciously crafted PDF files
- **Impact**: System compromise through document-based attacks
- **Status**: Actively exploited for at least four months before patching

### SharePoint Server Zero-Day
- **Description**: Zero-day vulnerability affecting Microsoft SharePoint Server
- **Impact**: Server compromise and potential data access
- **Status**: Publicly disclosed and patched in April 2026 update

### PHP Composer Security Vulnerabilities
- **Description**: Two high-severity vulnerabilities in Composer package manager for PHP
- **Impact**: Arbitrary command execution on affected systems
- **Status**: Patches released, potential for exploitation if unpatched

## Affected Systems and Products

- **Microsoft Windows**: All versions affected by 167 vulnerabilities including 2 zero-days in April 2026 patch cycle
- **Adobe Acrobat and Reader**: Vulnerable to zero-day exploitation through malicious PDFs
- **ShowDoc Servers**: Chinese document management platform under active RCE exploitation
- **Google Chrome Extensions**: Over 100 malicious extensions targeting OAuth2 tokens and user data
- **Android Devices**: Mirax RAT affecting Spanish-speaking users through Meta advertising campaigns
- **wolfSSL Library**: Critical certificate verification vulnerability affecting applications using this SSL/TLS library
- **Salesforce Platforms**: Misconfiguration exploitation affecting McGraw-Hill data security

## Attack Vectors and Techniques

- **Malicious Browser Extensions**: 108 Chrome extensions stealing Google OAuth2 Bearer tokens and Telegram data affecting 20,000+ users
- **PDF-Based Exploitation**: Zero-day attacks through crafted PDF documents targeting Adobe products
- **Remote Desktop Protocol Abuse**: Phishing attacks using malicious .rdp files to compromise systems
- **Supply Chain Attacks**: Fake applications distributed through official app stores (Apple App Store Ledger Live impersonation)
- **BYOVD Attacks**: Bring-Your-Own-Vulnerable-Driver techniques to disable EDR solutions
- **Social Engineering**: Meta advertising campaigns distributing Mirax Android RAT to Spanish-speaking targets
- **Configuration Exploitation**: Salesforce misconfigurations leading to unauthorized data access

## Threat Actor Activities

- **Cryptocurrency-Focused Groups**: Targeting Kraken exchange through insider threats and Apple App Store supply chain attacks resulting in $9.5M theft
- **ShinyHunters Extortion Gang**: Conducting data theft and extortion campaigns against major gaming companies including Rockstar Games
- **Chinese APT Groups**: Exploiting ShowDoc vulnerabilities on servers in China for persistent access
- **Chrome Extension Operators**: Coordinated campaign using 108 malicious extensions communicating with shared C2 infrastructure
- **Mirax RAT Operators**: Large-scale Android malware distribution targeting 220,000+ accounts across Meta platforms
- **PDF Exploitation Groups**: Sustained zero-day exploitation campaign against Adobe products lasting multiple months