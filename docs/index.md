# Exploitation Report

Critical zero-day vulnerabilities are currently under active exploitation across multiple platforms and industries. The most severe incident involves an Adobe Acrobat Reader zero-day vulnerability (CVE-2026-34621) that has been exploited through malicious PDF files for at least four months before receiving an emergency patch. Additionally, a critical pre-authentication remote code execution flaw in Marimo is experiencing active exploitation for credential theft. Supply chain attacks have escalated with multiple incidents including the compromise of CPUID's website to distribute trojanized hardware monitoring tools, and OpenAI's code-signing workflow being targeted through a malicious Axios package. Advanced persistent threats are leveraging sophisticated backdoors and social engineering campaigns, while financial institutions face targeted malware campaigns and widespread phishing operations.

## Active Exploitation Details

### Adobe Acrobat Reader Zero-Day Vulnerability
- **Description**: Critical vulnerability in Adobe Acrobat and Reader applications that allows attackers to exploit the software through maliciously crafted PDF files
- **Impact**: Successful exploitation enables attackers to execute arbitrary code on target systems through weaponized PDF documents
- **Status**: Actively exploited for at least four months before Adobe released emergency security updates
- **CVE ID**: CVE-2026-34621

### Marimo Pre-Authentication Remote Code Execution
- **Description**: Critical pre-authentication remote code execution vulnerability affecting Marimo applications
- **Impact**: Attackers can execute arbitrary code without authentication and steal user credentials
- **Status**: Currently under active exploitation in the wild

### CPUID Website Compromise
- **Description**: Supply chain attack targeting CPUID's official website hosting popular hardware monitoring tools
- **Impact**: Trojanized versions of CPU-Z, HWMonitor, HWMonitor Pro, and PerfMonitor distributed with STX RAT malware
- **Status**: Compromise lasted less than 24 hours but affected legitimate software downloads

### OpenAI Code-Signing Workflow Compromise
- **Description**: GitHub Actions workflow used for macOS app signing was compromised through a malicious Axios package
- **Impact**: Potential exposure of code-signing certificates and compromise of software integrity
- **Status**: OpenAI rotated potentially exposed macOS certificates as a precautionary measure

## Affected Systems and Products

- **Adobe Acrobat and Reader**: All versions affected by the zero-day vulnerability requiring emergency patching
- **Marimo Applications**: Systems running Marimo applications vulnerable to pre-authentication RCE attacks
- **CPUID Hardware Tools**: CPU-Z, HWMonitor, HWMonitor Pro, and PerfMonitor downloads compromised with malware
- **OpenAI macOS Applications**: Code-signing workflow potentially compromised affecting macOS app integrity
- **wolfSSL Library**: Critical vulnerability in SSL/TLS library affecting ECDSA certificate verification
- **Cloud Environments**: AWS, Google Cloud, Microsoft Azure, and Alibaba Cloud platforms targeted by APT41
- **Banking Systems**: Latin American financial institutions targeted by JanelaRAT malware
- **Industrial Control Systems**: Nearly 4,000 US programmable logic controllers exposed to potential attacks
- **Developer IDEs**: Multiple integrated development environments targeted by GlassWorm campaign

## Attack Vectors and Techniques

- **Malicious PDF Files**: Weaponized PDF documents exploiting Adobe Reader zero-day vulnerability
- **Supply Chain Compromise**: Targeting legitimate software distribution channels to insert malware
- **Social Engineering**: Facebook-based approaches used by APT37 to deliver RokRAT malware
- **Phishing-as-a-Service**: W3LL platform facilitating large-scale phishing operations
- **Session Hijacking**: Storm infostealer bypassing passwords and multi-factor authentication
- **Typosquatting**: APT41 using domain spoofing to obscure command and control communications
- **Zero-Detection Backdoors**: Advanced backdoors designed to evade security detection systems
- **Server-Side Decryption**: Novel approach by Storm malware to decrypt browser data remotely

## Threat Actor Activities

- **APT41**: China-backed group targeting cloud environments with zero-detection backdoors for credential harvesting
- **APT37 (ScarCruft)**: North Korean group using Facebook social engineering to deliver RokRAT malware
- **ShinyHunters**: Extortion gang leaking stolen Rockstar Games analytics data
- **Unknown Actors**: Exploiting Adobe zero-day through PDF-based attacks for extended periods
- **JanelaRAT Operators**: Targeting Latin American banks with 14,739 attacks recorded in Brazil
- **W3LL Platform Users**: Global phishing operation attempting over $20 million in fraud before FBI takedown
- **GlassWorm Campaign**: Using Zig droppers to infect developer environments across multiple IDEs
- **Iranian-Linked Groups**: Targeting US critical infrastructure through exposed industrial control systems