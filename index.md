# Exploitation Report

Critical zero-day vulnerabilities are currently under active exploitation across multiple platforms, with Adobe Acrobat/Reader CVE-2026-34621 representing the most significant threat after being exploited for at least four months before detection. Concurrent exploitation campaigns target document management systems like ShowDoc (CVE-2025-0520) and data analytics platforms like Marimo, while sophisticated malware operations leverage Android RATs, Chrome extension abuse, and supply chain compromises to establish persistent access across millions of devices. The emergence of advanced AI-powered vulnerability discovery tools has heightened concerns about accelerated exploit development capabilities.

## Active Exploitation Details

### Adobe Acrobat/Reader Zero-Day Vulnerability
- **Description**: Critical security flaw in Adobe Acrobat and Reader applications that has been exploited through maliciously crafted PDF files
- **Impact**: Attackers can achieve code execution and compromise systems by distributing weaponized PDF documents
- **Status**: Emergency patch released by Adobe after months of active exploitation in the wild
- **CVE ID**: CVE-2026-34621

### ShowDoc Remote Code Execution Flaw
- **Description**: Critical vulnerability in ShowDoc document management and collaboration service, particularly popular in China
- **Impact**: Remote code execution capabilities allowing full system compromise
- **Status**: Actively exploited against unpatched servers
- **CVE ID**: CVE-2025-0520

### Marimo Pre-Authentication RCE Vulnerability
- **Description**: Critical pre-authentication remote code execution vulnerability in the Marimo platform
- **Impact**: Credential theft and system compromise without authentication requirements
- **Status**: Currently under active exploitation for credential harvesting attacks

### CISA Known Exploited Vulnerabilities
- **Description**: Six security flaws in Fortinet, Microsoft, and Adobe software products
- **Impact**: Various system compromise scenarios depending on the specific vulnerability
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog due to evidence of active exploitation

### wolfSSL Certificate Verification Bypass
- **Description**: Critical vulnerability in the wolfSSL SSL/TLS library affecting Elliptic Curve Digital Signature Algorithm (ECDSA) verification
- **Impact**: Enables use of forged certificates, potentially allowing man-in-the-middle attacks and authentication bypass
- **Status**: Recently disclosed with high severity rating

## Affected Systems and Products

- **Adobe Acrobat and Reader**: All versions prior to emergency patch release
- **ShowDoc Servers**: Unpatched installations of the document management platform
- **Marimo Platform**: Pre-authentication access points vulnerable to RCE
- **Google Chrome Browser**: 108 malicious extensions affecting approximately 20,000 users
- **Android Devices**: 220,000+ accounts targeted by Mirax RAT via Meta advertising platforms
- **Fortinet Products**: Specific products mentioned in CISA KEV catalog
- **Microsoft Software**: Various applications included in CISA's exploitation list
- **wolfSSL Library**: SSL/TLS implementations using vulnerable ECDSA verification
- **CPUID Website**: Hardware monitoring tools (CPU-Z, HWMonitor) served with malicious payloads
- **Basic-Fit Systems**: Fitness chain infrastructure affecting 1 million member accounts
- **Booking.com Platform**: Reservation and user data systems compromised

## Attack Vectors and Techniques

- **Malicious PDF Distribution**: Weaponized documents exploiting Adobe Reader zero-day vulnerability
- **Chrome Extension Abuse**: 108 malicious browser extensions communicating with shared C2 infrastructure
- **Android RAT Deployment**: Mirax trojan turning devices into SOCKS5 proxies via social media advertising
- **Supply Chain Compromise**: CPUID website breach distributing STX RAT through legitimate software downloads
- **Social Engineering Campaigns**: Facebook-based approaches delivering RokRAT malware
- **Certificate Forgery**: Exploitation of wolfSSL ECDSA verification weaknesses
- **Session Hijacking**: Storm infostealer bypassing MFA through server-side decryption techniques
- **Typosquatting**: APT41 using domain mimicry to obscure command and control communications
- **Phishing-as-a-Service**: W3LL platform facilitating large-scale credential theft operations

## Threat Actor Activities

- **APT41**: China-backed group deploying zero-detection backdoors to harvest cloud credentials from AWS, Google, Azure, and Alibaba environments
- **APT37 (ScarCruft)**: North Korean group conducting Facebook social engineering campaigns to deliver RokRAT malware
- **Mirax Operators**: Spanish-speaking region targeting through Android RAT campaigns reaching 220,000+ Meta platform accounts
- **ShinyHunters**: Extortion gang leaking Rockstar Games analytics data following Anodot security incident
- **W3LL Network**: Dismantled global phishing operation responsible for $20 million in fraud attempts
- **Chrome Extension Threat Actors**: Coordinated campaign operators managing 108 malicious browser extensions
- **JanelaRAT Operators**: Latin American banking sector targeting with 14,739 attacks recorded in Brazil during 2025
- **Storm Infostealer Developers**: Advanced credential theft operation using server-side decryption techniques
- **CPUID Attackers**: Supply chain compromise operators distributing STX RAT through legitimate software channels