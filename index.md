# Exploitation Report

Critical vulnerability exploitation activity is currently targeting multiple high-value systems across various sectors. Adobe Acrobat Reader faces active zero-day exploitation through CVE-2026-34621, which has been leveraged for at least four months using maliciously crafted PDF files. ShowDoc servers are under attack via CVE-2025-0520, a remote code execution flaw enabling complete system compromise. Additionally, CISA has identified six new vulnerabilities in Fortinet, Microsoft, and Adobe products that are being actively exploited in the wild. Meanwhile, sophisticated supply chain attacks have compromised CPUID's website to distribute STX RAT malware, and a critical pre-authentication RCE vulnerability in Marimo is being exploited for credential theft operations.

## Active Exploitation Details

### Adobe Acrobat Reader Zero-Day
- **Description**: Critical security vulnerability in Adobe Acrobat and Reader applications allowing remote code execution through maliciously crafted PDF files
- **Impact**: Attackers can achieve complete system compromise when victims open specially crafted PDF documents
- **Status**: Actively exploited since at least December 2025, emergency patch released by Adobe
- **CVE ID**: CVE-2026-34621

### ShowDoc Remote Code Execution
- **Description**: Critical vulnerability in ShowDoc document management and collaboration service enabling remote code execution
- **Impact**: Complete server compromise allowing attackers full control over affected systems
- **Status**: Under active exploitation targeting unpatched servers
- **CVE ID**: CVE-2025-0520

### Marimo Pre-Authentication RCE
- **Description**: Critical pre-authentication remote code execution vulnerability in Marimo platform
- **Impact**: Allows attackers to execute arbitrary code without authentication, primarily used for credential theft
- **Status**: Currently under active exploitation in the wild

### CISA Known Exploited Vulnerabilities
- **Description**: Six security flaws in Fortinet, Microsoft, and Adobe software products identified by CISA
- **Impact**: Various impacts depending on specific vulnerability, including system compromise and data theft
- **Status**: Active exploitation confirmed, added to CISA's Known Exploited Vulnerabilities catalog

### wolfSSL Certificate Verification Bypass
- **Description**: Critical vulnerability in wolfSSL library enabling improper verification of hash algorithms in ECDSA certificate validation
- **Impact**: Allows use of forged certificates, undermining SSL/TLS security protections
- **Status**: Vulnerability disclosed, patch availability status varies by implementation

## Affected Systems and Products

- **Adobe Acrobat and Reader**: All versions vulnerable to CVE-2026-34621 until emergency patch applied
- **ShowDoc Servers**: Document management platforms popular in China, unpatched installations at risk
- **Marimo Platform**: Pre-authentication vulnerability affects all exposed instances
- **Chrome Browser Extensions**: 108 malicious extensions targeting Google and Telegram data, affecting 20,000 users
- **CPUID Hardware Tools**: CPU-Z, HWMonitor, and related utilities compromised via supply chain attack
- **wolfSSL Library**: SSL/TLS implementations using affected versions of the wolfSSL library
- **Fortinet Products**: Specific products identified by CISA as having exploited vulnerabilities
- **Microsoft Software**: Various Microsoft products with vulnerabilities confirmed as exploited
- **Basic-Fit Systems**: European gym chain systems compromised affecting 1 million members
- **Booking.com Infrastructure**: Reservation and user data systems breached requiring PIN resets

## Attack Vectors and Techniques

- **Malicious PDF Distribution**: Attackers distributing specially crafted PDF files to exploit Adobe Reader zero-day
- **Web Application Exploitation**: Direct attacks against vulnerable ShowDoc and Marimo installations
- **Supply Chain Compromise**: CPUID website compromised to serve trojanized versions of legitimate hardware monitoring tools
- **Browser Extension Abuse**: Malicious Chrome extensions communicating with command-and-control infrastructure
- **Social Engineering**: APT37 using Facebook-based social engineering to deliver RokRAT malware
- **Certificate Forgery**: Exploitation of wolfSSL vulnerability to bypass SSL/TLS protections using forged certificates
- **Session Hijacking**: New "Storm" infostealer performing server-side decryption to hijack authenticated sessions
- **Phishing-as-a-Service**: W3LL platform providing comprehensive phishing infrastructure before FBI takedown

## Threat Actor Activities

- **APT37 (ScarCruft)**: North Korean group conducting multi-stage social engineering campaigns via Facebook to deliver RokRAT malware
- **APT41**: China-backed group deploying zero-detection backdoors to harvest cloud credentials from AWS, Google, Azure, and Alibaba environments
- **Unknown CPUID Attackers**: Sophisticated actors compromised CPUID website for less than 24 hours to distribute STX RAT malware
- **JanelaRAT Operators**: Targeting Latin American banks with 14,739 attacks recorded in Brazil during 2025, focusing on financial institutions
- **ShinyHunters**: Extortion gang leaked stolen Rockstar Games analytics data following Anodot security incident
- **W3LL Network Operators**: Global phishing operation responsible for $20 million in fraud attempts before FBI dismantlement
- **Chrome Extension Threat Actors**: Coordinated campaign deploying 108 malicious extensions to steal Google and Telegram credentials