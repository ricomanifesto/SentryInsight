# Exploitation Report

Microsoft's April 2026 Patch Tuesday addressed a massive security update encompassing 167 vulnerabilities, including two actively exploited zero-day vulnerabilities and a SharePoint Server zero-day that was publicly disclosed. Concurrent with these critical Windows patches, threat actors have been leveraging various attack vectors including malicious Chrome extensions, compromised mobile applications, and sophisticated social engineering campaigns. Notable incidents include the exploitation of CVE-2025-0520 in ShowDoc servers, six vulnerabilities added to CISA's Known Exploited Vulnerabilities catalog, and an Adobe zero-day that remained actively exploited for months before being patched.

## Active Exploitation Details

### Microsoft Windows Zero-Day Vulnerabilities
- **Description**: Two zero-day vulnerabilities in Windows operating systems were actively exploited in the wild before patches were released
- **Impact**: Attackers could achieve privilege escalation and potentially gain full system control
- **Status**: Patched in April 2026 Patch Tuesday update, including Windows 10 KB5082200 and Windows 11 cumulative updates

### SharePoint Server Zero-Day
- **Description**: Zero-day vulnerability in Microsoft SharePoint Server that was publicly disclosed
- **Impact**: Potential unauthorized access to SharePoint systems and data
- **Status**: Included in the April 2026 Patch Tuesday fixes

### ShowDoc Remote Code Execution Vulnerability
- **Description**: Critical security vulnerability in ShowDoc, a document management and collaboration service popular in China
- **Impact**: Attackers can execute arbitrary commands on unpatched servers
- **Status**: Actively exploited in the wild against unpatched servers
- **CVE ID**: CVE-2025-0520

### Adobe Acrobat and Reader Zero-Day
- **Description**: Zero-day vulnerability in Adobe Acrobat and Reader exploited through maliciously crafted PDF files
- **Impact**: Code execution and potential system compromise through PDF document attacks
- **Status**: Actively exploited for at least four months before being patched

### Six CISA-Listed Vulnerabilities
- **Description**: Multiple security flaws in Fortinet, Microsoft, and Adobe software products
- **Impact**: Various attack vectors depending on specific vulnerabilities
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog due to evidence of active exploitation

## Affected Systems and Products

- **Microsoft Windows**: Windows 10 and Windows 11 systems affected by 167 vulnerabilities including zero-days
- **SharePoint Server**: Microsoft SharePoint installations vulnerable to zero-day exploit
- **ShowDoc Servers**: Document management platforms running unpatched ShowDoc software
- **Adobe Acrobat and Reader**: PDF viewing and editing applications across multiple platforms
- **Chrome Browser Extensions**: Over 100 malicious extensions in Chrome Web Store affecting 20,000+ users
- **Android Devices**: Mirax RAT targeting Spanish-speaking countries through Meta advertising campaigns
- **Fortinet Products**: Multiple Fortinet security appliances and software solutions
- **PHP Composer**: Package manager for PHP with command execution vulnerabilities
- **wolfSSL Library**: SSL/TLS library implementations with certificate verification flaws

## Attack Vectors and Techniques

- **Malicious PDF Files**: Crafted PDF documents exploiting Adobe Reader/Acrobat zero-day vulnerability
- **Browser Extension Compromise**: Malicious Chrome extensions stealing Google OAuth2 tokens and Telegram data
- **Social Engineering**: Meta advertising campaigns distributing Mirax Android RAT to 220,000+ accounts
- **Remote Desktop File Abuse**: Phishing attacks leveraging malicious RDP files with new Windows protections implemented
- **Mobile App Store Infiltration**: Fake Ledger Live app on Apple's App Store stealing $9.5 million in cryptocurrency
- **Bring-Your-Own-Vulnerable-Driver (BYOVD)**: EDR-killer techniques using vulnerable drivers to bypass security controls
- **SEO Poisoning**: AI-driven "Pushpaganda" campaigns exploiting Google Discover for scareware distribution
- **Insider Threats**: Internal access exploitation as seen in Kraken cryptocurrency exchange breach

## Threat Actor Activities

- **ShinyHunters Extortion Gang**: Leaked stolen Rockstar Games analytics data following Anodot security incident
- **Cryptocurrency Attackers**: Targeted Kraken exchange with insider breach and extortion attempts
- **Chrome Extension Operators**: Coordinated campaign using 108 malicious extensions with shared command-and-control infrastructure
- **Mobile Malware Distributors**: Mirax RAT operators targeting Spanish-speaking users through sophisticated Meta ad campaigns
- **PDF Exploit Actors**: Long-term exploitation of Adobe zero-day using malicious PDF files over multiple months
- **Corporate Data Thieves**: Multiple incidents including McGraw-Hill Salesforce misconfiguration exploitation and Basic-Fit breach affecting 1 million members