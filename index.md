# Exploitation Report

Critical zero-day vulnerabilities are currently under active exploitation across multiple attack surfaces, with Adobe Acrobat Reader being targeted through malicious PDF files for several months. Security researchers have identified active campaigns exploiting vulnerabilities in ShowDoc document management systems, a critical pre-authentication RCE flaw in Marimo, and malicious Chrome extensions targeting user data. CISA has added six new vulnerabilities to its Known Exploited Vulnerabilities catalog, affecting major software vendors including Fortinet, Microsoft, and Adobe. The threat landscape is further complicated by sophisticated supply chain attacks, including the compromise of CPUID's website and a malicious Axios package affecting OpenAI's code-signing workflow.

## Active Exploitation Details

### Adobe Acrobat Reader Zero-Day
- **Description**: A critical vulnerability in Adobe Acrobat and Reader that has been exploited through maliciously crafted PDF files
- **Impact**: Attackers can execute arbitrary code on victim systems when malicious PDF files are opened
- **Status**: Emergency patch released by Adobe after months of active exploitation in the wild
- **CVE ID**: CVE-2026-34621

### ShowDoc Remote Code Execution
- **Description**: A critical security vulnerability affecting ShowDoc document management and collaboration service
- **Impact**: Enables remote code execution on unpatched servers
- **Status**: Under active exploitation in the wild, particularly targeting deployments in China
- **CVE ID**: CVE-2025-0520

### Marimo Pre-Authentication RCE
- **Description**: A critical pre-authentication remote code execution vulnerability in Marimo
- **Impact**: Allows attackers to execute arbitrary code without authentication and perform credential theft
- **Status**: Now under active exploitation following public disclosure

### CISA Known Exploited Vulnerabilities
- **Description**: Six security flaws in Fortinet, Microsoft, and Adobe software products
- **Impact**: Various impacts including remote code execution and privilege escalation
- **Status**: Added to CISA KEV catalog due to evidence of active exploitation in the wild

## Affected Systems and Products

- **Adobe Acrobat and Reader**: All versions prior to emergency security update
- **ShowDoc**: Document management and collaboration service, particularly popular in China
- **Marimo**: Interactive computing environment and applications
- **Google Chrome**: 108 malicious extensions affecting approximately 20,000 users
- **CPUID Tools**: CPU-Z, HWMonitor, HWMonitor Pro, and PerfMonitor downloads compromised
- **Fortinet Products**: Multiple products affected by newly cataloged vulnerabilities
- **Microsoft Software**: Various Microsoft products with exploited vulnerabilities
- **wolfSSL Library**: SSL/TLS library with critical certificate verification flaw

## Attack Vectors and Techniques

- **Malicious PDF Files**: Exploitation of Adobe Reader zero-day through weaponized documents
- **Pre-Authentication Attacks**: Direct exploitation of Marimo services without authentication requirements
- **Browser Extension Abuse**: Malicious Chrome extensions communicating with command-and-control infrastructure
- **Supply Chain Compromise**: Trojanized downloads from legitimate software distribution sites
- **Social Engineering**: Facebook-based campaigns by North Korean APT37 delivering RokRAT malware
- **Session Hijacking**: New "Storm" infostealer bypassing passwords and MFA through server-side decryption
- **Typosquatting**: APT41 using domain name variations to obscure command-and-control communications

## Threat Actor Activities

- **APT41**: Deploying zero-detection backdoors to harvest cloud credentials from AWS, Google, Azure, and Alibaba environments
- **APT37 (ScarCruft)**: North Korean group conducting multi-stage social engineering campaigns via Facebook to deliver RokRAT malware
- **Unknown Threat Actors**: Compromising CPUID website to distribute STX RAT through trojanized hardware monitoring tools
- **Chrome Extension Operators**: Coordinated campaign using 108 malicious extensions to steal Google and Telegram data
- **JanelaRAT Operators**: Targeting Latin American banks with 14,739 attacks recorded in Brazil during 2025
- **ShinyHunters**: Extortion gang leaking stolen Rockstar Games analytics data following Anodot security incident