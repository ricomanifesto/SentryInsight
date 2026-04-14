# Exploitation Report

The cybersecurity landscape is experiencing an alarming surge in active exploitation campaigns, with several critical zero-day vulnerabilities and recently discovered threats causing significant impact across diverse platforms. Most notably, CVE-2026-34621, a critical Adobe Acrobat Reader zero-day vulnerability, has been actively exploited for at least four months through maliciously crafted PDF files. Meanwhile, CVE-2025-0520, affecting ShowDoc document management services, is seeing widespread exploitation on unpatched servers. The threat landscape is further complicated by sophisticated malware campaigns including the Mirax Android RAT affecting over 220,000 accounts, malicious Chrome extensions compromising 20,000 users, and advanced persistent threats like APT37 and APT41 conducting targeted operations against financial institutions and cloud environments.

## Active Exploitation Details

### Adobe Acrobat Reader Zero-Day Vulnerability
- **Description**: A critical security flaw in Adobe Acrobat Reader that allows attackers to exploit the application through maliciously crafted PDF files
- **Impact**: Enables arbitrary code execution and complete system compromise when victims open weaponized PDF documents
- **Status**: Emergency security update released by Adobe after months of active exploitation in the wild
- **CVE ID**: CVE-2026-34621

### ShowDoc Remote Code Execution Flaw
- **Description**: A critical remote code execution vulnerability affecting ShowDoc, a document management and collaboration service popular in China
- **Impact**: Allows attackers to achieve complete system compromise and execute arbitrary code on vulnerable servers
- **Status**: Under active exploitation targeting unpatched ShowDoc installations
- **CVE ID**: CVE-2025-0520

### Marimo Pre-Authentication RCE
- **Description**: A critical pre-authentication remote code execution vulnerability in Marimo that doesn't require user authentication
- **Impact**: Enables credential theft and complete system compromise without any user interaction
- **Status**: Currently under active exploitation for credential harvesting operations

### CISA Known Exploited Vulnerabilities
- **Description**: Six security flaws affecting Fortinet, Microsoft, and Adobe software products
- **Impact**: Various impacts including privilege escalation, remote code execution, and system compromise
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog due to evidence of active exploitation

### wolfSSL Certificate Verification Bypass
- **Description**: Critical vulnerability in the wolfSSL SSL/TLS library affecting proper verification of hash algorithms and sizes when checking ECDSA signatures
- **Impact**: Allows attackers to use forged certificates, potentially enabling man-in-the-middle attacks and bypassing security controls
- **Status**: Patch available, actively being assessed for exploitation potential

## Affected Systems and Products

- **Adobe Acrobat Reader**: All versions prior to the emergency update, exploited via malicious PDF files
- **ShowDoc**: Document management and collaboration service installations, particularly popular in China
- **Marimo**: Interactive computing platform vulnerable to pre-authentication attacks
- **Google Chrome**: 108 malicious extensions affecting approximately 20,000 users
- **Android Devices**: Mirax RAT targeting Spanish-speaking countries through Meta advertising platforms
- **Fortinet Products**: Multiple products with actively exploited vulnerabilities
- **Microsoft Software**: Various Microsoft products with confirmed exploitation
- **CPUID Website**: CPU-Z and HWMonitor download compromises distributing STX RAT
- **wolfSSL Library**: SSL/TLS implementation used across multiple applications and systems
- **macOS Applications**: OpenAI and other applications affected by Axios supply chain attack

## Attack Vectors and Techniques

- **Malicious PDF Files**: Weaponized documents exploiting Adobe Reader vulnerabilities for code execution
- **Social Engineering**: APT37 using Facebook messaging to deliver RokRAT malware to targets
- **Meta Advertising Campaigns**: Mirax RAT distribution through Facebook, Instagram, and Messenger ads
- **Chrome Extension Distribution**: 108 malicious extensions stealing Google and Telegram data
- **Supply Chain Attacks**: Compromised Axios package affecting GitHub Actions workflows
- **Website Compromise**: CPUID website breach distributing trojanized software downloads
- **Session Hijacking**: Storm infostealer bypassing passwords and MFA through server-side decryption
- **SOCKS5 Proxy Creation**: Converting compromised Android devices into network proxies
- **Typosquatting**: APT41 using domain typosquatting to obscure command and control communication
- **Phishing-as-a-Service**: W3LL platform enabling large-scale phishing operations

## Threat Actor Activities

- **APT37 (ScarCruft)**: North Korean group conducting multi-stage social engineering campaigns via Facebook to deliver RokRAT malware
- **APT41**: China-backed group deploying zero-detection backdoors to harvest cloud credentials from AWS, Google, Azure, and Alibaba environments
- **Mirax RAT Operators**: Targeting Spanish-speaking countries with Android malware distributed through Meta advertising platforms
- **JanelaRAT Campaign**: Targeting Latin American banks and financial institutions, with 14,739 attacks recorded in Brazil during 2025
- **ShinyHunters**: Extortion gang leaking stolen Rockstar Games analytics data following Anodot security incident
- **Chrome Extension Campaign**: Coordinated operation deploying 108 malicious Chrome extensions with shared command and control infrastructure
- **W3LL Network**: Global phishing operation dismantled by FBI and Indonesian police after facilitating $20 million in fraud attempts
- **Storm Infostealer Operators**: Deploying advanced session hijacking malware with server-side decryption capabilities
- **CPUID Website Attackers**: Unknown threat actors compromising legitimate software distribution site to distribute STX RAT