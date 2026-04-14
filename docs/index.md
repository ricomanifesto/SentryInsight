# Exploitation Report

Multiple critical vulnerabilities are currently under active exploitation across various platforms, with threat actors targeting everything from document readers to development tools. The most significant ongoing threats include a zero-day vulnerability in Adobe Acrobat and Reader (CVE-2026-34621) that has been exploited for at least four months, a critical ShowDoc remote code execution flaw (CVE-2025-0520), and a pre-authentication RCE vulnerability in Marimo that is being actively leveraged for credential theft. Additionally, sophisticated malware campaigns are utilizing Android RATs, Chrome extensions, and supply chain attacks to compromise systems and steal sensitive data across multiple sectors.

## Active Exploitation Details

### Adobe Acrobat and Reader Zero-Day Vulnerability
- **Description**: A critical vulnerability in Adobe Acrobat and Reader that enables attackers to exploit the software through maliciously crafted PDF files
- **Impact**: Successful exploitation allows attackers to execute arbitrary code on target systems, potentially leading to full system compromise
- **Status**: Under active exploitation for at least four months before Adobe released an emergency security update
- **CVE ID**: CVE-2026-34621

### ShowDoc Remote Code Execution Flaw
- **Description**: A critical security vulnerability in ShowDoc, a popular document management and collaboration service in China
- **Impact**: Enables remote code execution on unpatched servers, allowing attackers to gain unauthorized access and control
- **Status**: Actively exploited in the wild on unpatched ShowDoc servers
- **CVE ID**: CVE-2025-0520

### Marimo Pre-Authentication RCE Vulnerability
- **Description**: A critical pre-authentication remote code execution vulnerability affecting the Marimo platform
- **Impact**: Allows attackers to execute arbitrary code without authentication and steal credentials from compromised systems
- **Status**: Currently under active exploitation for credential theft operations

### CISA Known Exploited Vulnerabilities
- **Description**: Six additional security flaws in Fortinet, Microsoft, and Adobe software identified as actively exploited
- **Impact**: Various impacts depending on the specific vulnerability, ranging from privilege escalation to remote code execution
- **Status**: Added to CISA's Known Exploited Vulnerabilities (KEV) catalog due to evidence of active exploitation

## Affected Systems and Products

- **Adobe Acrobat and Reader**: Critical zero-day vulnerability affecting document processing capabilities
- **ShowDoc Platform**: Document management and collaboration service popular in China
- **Marimo Platform**: Development environment vulnerable to pre-authentication attacks
- **Google Chrome Extensions**: 108 malicious extensions compromising user data from Google and Telegram
- **Android Devices**: Mirax RAT targeting Spanish-speaking countries through Meta advertising platforms
- **CPUID Tools**: CPU-Z and HWMonitor downloads compromised with STX RAT malware
- **wolfSSL Library**: SSL/TLS library with critical certificate verification flaw
- **Fortinet Software**: Multiple products affected by known exploited vulnerabilities
- **Microsoft Software**: Various Microsoft products with actively exploited flaws

## Attack Vectors and Techniques

- **Malicious PDF Files**: Zero-day exploitation through crafted PDF documents targeting Adobe products
- **Social Engineering**: APT37 using Facebook messaging to deliver RokRAT malware to targets
- **Chrome Extension Abuse**: 108 malicious extensions stealing Google and Telegram data from 20,000 users
- **Supply Chain Attacks**: CPUID website compromise delivering trojanized hardware monitoring tools
- **Android RAT Distribution**: Mirax malware spread through Meta advertising platforms, turning devices into SOCKS5 proxies
- **Meta Advertising Abuse**: Large-scale campaigns reaching over 220,000 accounts on Facebook, Instagram, and Messenger
- **Typosquatting**: APT41 using domain typosquatting to obscure command-and-control communications
- **Session Hijacking**: Storm infostealer bypassing passwords and MFA through server-side session decryption

## Threat Actor Activities

- **APT37 (ScarCruft)**: North Korean group conducting multi-stage social engineering campaigns via Facebook to deliver RokRAT malware
- **APT41**: China-backed threat group targeting AWS, Google, Azure, and Alibaba cloud environments using zero-detection backdoors for credential harvesting
- **Mirax Operators**: Targeting Spanish-speaking countries with Android RAT campaigns, converting devices into proxy networks
- **Chrome Extension Attackers**: Operating 108 malicious extensions with shared command-and-control infrastructure
- **CPUID Attackers**: Unknown threat actors compromising popular hardware monitoring tool distribution for less than 24 hours
- **Storm Infostealer Operators**: Deploying advanced session hijacking techniques with server-side decryption capabilities
- **ShinyHunters**: Extortion gang leaking stolen Rockstar Games analytics data following Anodot security incident