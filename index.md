# Exploitation Report

Microsoft's April 2026 Patch Tuesday addresses a massive security update with 167-169 vulnerabilities, including two zero-day vulnerabilities that have been actively exploited in the wild. The most critical exploitation activity involves a SharePoint Server zero-day that has been under active attack, alongside a publicly disclosed vulnerability. Additional active exploitation includes CVE-2025-0520 in ShowDoc servers and six vulnerabilities recently added to CISA's Known Exploited Vulnerabilities catalog affecting Fortinet, Microsoft, and Adobe products. The threat landscape also shows significant malicious activity through Chrome extensions, Android malware campaigns, and sophisticated phishing operations targeting cryptocurrency users.

## Active Exploitation Details

### SharePoint Server Zero-Day Vulnerability
- **Description**: A critical zero-day vulnerability affecting Microsoft SharePoint Server that allows unauthorized access and potential system compromise
- **Impact**: Attackers can gain unauthorized access to SharePoint environments, potentially leading to data theft, system compromise, and lateral movement within corporate networks
- **Status**: Actively exploited in the wild; patches released in Microsoft's April 2026 Patch Tuesday update

### ShowDoc Remote Code Execution Vulnerability
- **Description**: A critical security vulnerability in ShowDoc, a document management and collaboration service popular in China, allowing remote code execution
- **Impact**: Attackers can execute arbitrary code on unpatched ShowDoc servers, leading to complete system compromise
- **Status**: Under active exploitation on unpatched servers
- **CVE ID**: CVE-2025-0520

### Adobe Zero-Day Vulnerability
- **Description**: A zero-day vulnerability in Adobe Acrobat and Reader exploited through maliciously crafted PDF files
- **Impact**: Allows attackers to compromise systems when users open malicious PDF documents
- **Status**: Actively exploited for at least four months before patching; patches now available

### Microsoft Publicly Disclosed Vulnerability
- **Description**: A publicly disclosed vulnerability included in Microsoft's April 2026 security updates
- **Impact**: Potential system compromise and unauthorized access
- **Status**: Publicly disclosed and patched in April 2026 Patch Tuesday

### PHP Composer Security Vulnerabilities
- **Description**: Two high-severity security vulnerabilities in Composer, a package manager for PHP
- **Impact**: Successful exploitation could result in arbitrary command execution on affected systems
- **Status**: Patches have been released

## Affected Systems and Products

- **Microsoft SharePoint Server**: Critical zero-day vulnerability requiring immediate patching
- **Microsoft Windows**: 167-169 total vulnerabilities patched, including elevation-of-privilege bugs comprising over half of the vulnerabilities
- **ShowDoc Servers**: Document management platform vulnerable to remote code execution attacks
- **Adobe Acrobat and Reader**: Zero-day vulnerability exploited through malicious PDF files
- **PHP Composer**: Package manager affected by command execution vulnerabilities
- **Google Chrome Web Store**: Over 100 malicious extensions targeting user accounts and data
- **Android Devices**: Mirax RAT targeting Spanish-speaking countries through Meta advertising platforms
- **Apple App Store**: Fake Ledger Live app stealing cryptocurrency from macOS users

## Attack Vectors and Techniques

- **Malicious PDF Exploitation**: Crafted PDF files used to exploit Adobe zero-day vulnerability for system compromise
- **Chrome Extension Abuse**: 108 malicious Chrome extensions stealing Google OAuth2 Bearer tokens and deploying backdoors
- **Social Media Advertising**: Meta ads used to distribute Mirax Android RAT to over 220,000 accounts
- **App Store Impersonation**: Fake Ledger Live application on Apple's App Store stealing $9.5 million in cryptocurrency
- **Remote Desktop File Abuse**: Phishing attacks leveraging malicious .rdp files for system access
- **Salesforce Misconfiguration**: Exploitation of cloud service misconfigurations for data access
- **SEO Poisoning**: AI-generated content used in search engine optimization attacks for ad fraud
- **BYOVD Attacks**: Bring-Your-Own-Vulnerable-Driver techniques used by EDR-killer malware

## Threat Actor Activities

- **ShinyHunters Gang**: Extortion activities targeting multiple organizations including Rockstar Games and Kraken cryptocurrency exchange
- **Chrome Extension Operators**: Coordinated campaign using 108 extensions with shared command-and-control infrastructure
- **Mirax RAT Operators**: Android malware campaign targeting Spanish-speaking users through social media platforms
- **Cryptocurrency Scammers**: Sophisticated operation deploying fake applications on official app stores to steal digital assets
- **Pushpaganda Campaign**: AI-driven scam exploiting Google Discover for scareware distribution and ad fraud