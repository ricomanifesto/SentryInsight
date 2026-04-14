# Exploitation Report

Critical zero-day exploitation activity is currently targeting widely-used software platforms, with Adobe Acrobat and Reader experiencing active attacks through maliciously crafted PDF files for at least four months. CVE-2026-34621 represents a significant threat as attackers have successfully weaponized this vulnerability before patches were available. Additionally, a critical pre-authentication remote code execution flaw in Marimo is now under active exploitation for credential theft, while threat actors have compromised the CPUID website to distribute trojaned versions of popular hardware monitoring tools. These incidents highlight the persistent challenge of zero-day vulnerabilities and supply chain attacks targeting both enterprise and consumer software platforms.

## Active Exploitation Details

### Adobe Acrobat and Reader Zero-Day Vulnerability
- **Description**: A critical vulnerability in Adobe Acrobat and Reader that allows attackers to exploit the software through maliciously crafted PDF files
- **Impact**: Successful exploitation enables attackers to execute arbitrary code on victim systems, potentially leading to full system compromise
- **Status**: Adobe has released an emergency security update to patch this actively exploited vulnerability
- **CVE ID**: CVE-2026-34621

### Marimo Pre-Authentication Remote Code Execution Flaw
- **Description**: A critical pre-authentication remote code execution vulnerability that allows attackers to execute code without prior authentication
- **Impact**: Attackers can gain unauthorized access to systems and steal credentials without needing valid login information
- **Status**: Currently under active exploitation with attacks focused on credential theft

### wolfSSL Library Certificate Verification Flaw
- **Description**: A critical vulnerability in the wolfSSL SSL/TLS library affecting improper verification of hash algorithms or their size when checking Elliptic Curve Digital Signature Algorithm (ECDSA)
- **Impact**: Enables the use of forged certificates, potentially allowing man-in-the-middle attacks and bypassing SSL/TLS security protections
- **Status**: Vulnerability disclosed with security implications for applications using the affected library

## Affected Systems and Products

- **Adobe Acrobat and Reader**: All versions vulnerable to CVE-2026-34621 prior to emergency patch release
- **Marimo Platform**: Systems running vulnerable versions susceptible to pre-authentication RCE attacks
- **wolfSSL Library**: Applications and systems utilizing the affected wolfSSL library for SSL/TLS operations
- **CPUID Tools**: CPU-Z, HWMonitor, HWMonitor Pro, and PerfMonitor downloaded during compromise window
- **macOS Applications**: OpenAI applications affected by malicious Axios supply chain incident

## Attack Vectors and Techniques

- **Malicious PDF Files**: Weaponized PDF documents exploiting Adobe zero-day vulnerability for code execution
- **Pre-Authentication Exploitation**: Direct attacks against Marimo systems without requiring valid credentials
- **Supply Chain Compromise**: CPUID website breach resulting in distribution of trojaned hardware monitoring tools
- **Certificate Forgery**: Exploitation of wolfSSL library flaws to use forged certificates in SSL/TLS communications
- **Social Engineering**: Facebook-based campaigns delivering RokRAT malware through multi-stage attacks
- **Session Hijacking**: Storm infostealer bypassing passwords and MFA through server-side decryption techniques

## Threat Actor Activities

- **APT37 (ScarCruft)**: North Korean group conducting Facebook social engineering campaigns to deliver RokRAT malware through multi-stage attacks
- **APT41**: China-backed threat group deploying zero-detection backdoors targeting AWS, Google, Azure, and Alibaba cloud environments using typosquatting for C2 communication
- **ShinyHunters**: Extortion gang leaking stolen Rockstar Games analytics data following Anodot security incident
- **Unknown Actors**: Compromised CPUID website for less than 24 hours to distribute STX RAT through trojaned versions of popular hardware tools
- **Criminal Organizations**: JanelaRAT malware campaigns targeting Latin American banks with 14,739 attacks recorded in Brazil during 2025
- **W3LL Phishing Network**: Global phishing operation dismantled by FBI and Indonesian authorities, responsible for $20 million in fraud attempts