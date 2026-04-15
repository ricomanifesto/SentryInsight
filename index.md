# Exploitation Report

The current threat landscape reveals a concerning surge in active exploitation activity, with Microsoft releasing emergency patches for 167 vulnerabilities including two actively exploited zero-day vulnerabilities in April 2026. Critical exploitation activity includes a ShowDoc remote code execution vulnerability being actively targeted on unpatched servers, alongside a months-long zero-day campaign exploiting Adobe Acrobat and Reader through malicious PDF files. CISA has added six new vulnerabilities to its Known Exploited Vulnerabilities catalog, indicating active exploitation of flaws in Fortinet, Microsoft, and Adobe products. The threat environment is further complicated by sophisticated malware campaigns, including over 100 malicious Chrome extensions stealing user credentials and a new Android RAT reaching over 220,000 victims through Meta advertising platforms.

## Active Exploitation Details

### Microsoft Windows Zero-Day Vulnerabilities
- **Description**: Two critical zero-day vulnerabilities patched in Microsoft's April 2026 Patch Tuesday affecting Windows operating systems and SharePoint Server
- **Impact**: Privilege escalation and unauthorized system access, with elevation-of-privilege bugs accounting for more than half of the 165 vulnerabilities patched
- **Status**: Patches released via KB5082200 extended security update for Windows 10 and cumulative updates KB5083769 & KB5082052 for Windows 11

### ShowDoc Remote Code Execution Vulnerability
- **Description**: Critical security vulnerability in ShowDoc document management and collaboration service popular in China
- **Impact**: Remote code execution on unpatched servers, allowing attackers complete system compromise
- **Status**: Actively exploited in the wild on unpatched servers
- **CVE ID**: CVE-2025-0520

### Adobe Acrobat and Reader Zero-Day
- **Description**: Zero-day vulnerability in Adobe Acrobat and Reader exploited through maliciously crafted PDF files
- **Impact**: System compromise through document-based attacks, enabling arbitrary code execution
- **Status**: Actively exploited for at least four months before patch release

### CISA Known Exploited Vulnerabilities
- **Description**: Six security flaws in Fortinet, Microsoft, and Adobe software added to CISA's Known Exploited Vulnerabilities catalog
- **Impact**: Various impacts including unauthorized access, privilege escalation, and system compromise
- **Status**: Confirmed active exploitation in the wild requiring immediate patching

## Affected Systems and Products

- **Microsoft Windows**: Windows 10, Windows 11 (versions 25H2/24H2 and 23H2), SharePoint Server
- **ShowDoc Platform**: Document management and collaboration service, particularly affecting Chinese deployments
- **Adobe Products**: Acrobat and Reader applications across multiple versions
- **Fortinet Products**: Various Fortinet security appliances and software solutions
- **Chrome Browser Extensions**: Over 100 malicious extensions in official Chrome Web Store
- **Android Devices**: Devices targeted by Mirax RAT through Meta advertising platforms
- **PHP Composer**: Package manager for PHP with newly disclosed command execution vulnerabilities
- **wolfSSL Library**: SSL/TLS library with critical certificate verification vulnerability

## Attack Vectors and Techniques

- **Malicious PDF Files**: Zero-day exploitation through weaponized PDF documents targeting Adobe products
- **Remote Desktop Protocol Abuse**: Phishing attacks using malicious RDP files with new Windows protections implemented
- **Browser Extension Malware**: Over 100 Chrome extensions stealing OAuth2 Bearer tokens and deploying backdoors
- **Social Media Manipulation**: Meta advertising platforms used to distribute Mirax Android RAT to 220,000+ victims
- **Bring-Your-Own-Vulnerable-Driver (BYOVD)**: EDR-killer ecosystem expansion using vulnerable driver techniques
- **OAuth2 Token Theft**: Sophisticated credential harvesting through malicious browser extensions
- **Supply Chain Attacks**: Fake applications distributed through official app stores (Apple App Store Ledger Live scam)
- **SEO Poisoning**: AI-driven Pushpaganda scams exploiting Google Discover for scareware distribution

## Threat Actor Activities

- **ShinyHunters Extortion Gang**: Actively leaking stolen Rockstar Games analytics data following Anodot security incident
- **Chrome Extension Threat Actors**: Coordinated campaign managing 108 malicious extensions communicating with shared command-and-control infrastructure
- **Mirax RAT Operators**: Targeting Spanish-speaking countries through Meta advertising platforms, converting devices into SOCKS5 proxies
- **Crypto Scammers**: Operating fake Ledger Live application that stole $9.5 million in cryptocurrency from 50 victims
- **Kraken Exchange Attackers**: Cybercrime group attempting extortion through insider breach, threatening to release client data videos
- **McGraw-Hill Attackers**: Exploiting Salesforce misconfiguration to access internal education company data
- **Basic-Fit Breach Actors**: Compromising European gym chain systems affecting 1 million customer records