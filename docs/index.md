# Exploitation Report

The current threat landscape reveals significant exploitation activity across multiple attack vectors, with particularly concerning zero-day vulnerabilities in widely-used software. Google has patched two high-severity Chrome zero-days that were actively exploited in the wild, affecting the Skia graphics library and V8 JavaScript engine. Supply chain attacks continue to pose major risks, with the AppsFlyer Web SDK being hijacked to distribute cryptocurrency-stealing malware and the GlassWorm campaign escalating its operations through 72 malicious Open VSX extensions targeting developers. Critical infrastructure remains under attack, as demonstrated by the targeting of Poland's nuclear research center and a comprehensive law enforcement operation that dismantled 45,000 malicious IP addresses linked to cybercriminal operations. Microsoft has also released emergency patches for Windows 11 RRAS vulnerabilities, while Veeam addressed seven critical flaws in its Backup & Replication software that could enable remote code execution.

## Active Exploitation Details

### Chrome Zero-Day Vulnerabilities
- **Description**: Two high-severity vulnerabilities in Google Chrome affecting the Skia graphics library and V8 JavaScript engine components
- **Impact**: Successful exploitation could allow attackers to execute arbitrary code, potentially leading to full system compromise
- **Status**: Actively exploited in the wild; patches released by Google

### Windows 11 RRAS Remote Code Execution Flaw
- **Description**: Security vulnerability in Windows 11 Routing and Remote Access Service (RRAS) that affects Enterprise devices receiving hotpatch updates
- **Impact**: Remote code execution allowing attackers to gain unauthorized system access
- **Status**: Microsoft released out-of-band hotpatch update to address the vulnerability

### AppsFlyer Web SDK Supply Chain Attack
- **Description**: The AppsFlyer Web SDK was compromised and injected with malicious JavaScript code designed to steal cryptocurrency
- **Impact**: Websites using the compromised SDK could unknowingly serve malware to visitors, leading to cryptocurrency theft
- **Status**: Temporary hijacking detected and addressed; supply chain attack vector remains a concern

### Veeam Backup & Replication Critical Vulnerabilities
- **Description**: Seven critical security flaws in Veeam's Backup & Replication software
- **Impact**: Remote code execution capabilities that could allow attackers to compromise backup infrastructure
- **Status**: Security updates released by Veeam to address all critical vulnerabilities

### Linux AppArmor CrackArmor Vulnerabilities
- **Description**: Nine security vulnerabilities within the Linux kernel's AppArmor security module
- **Impact**: Unprivileged users can circumvent kernel protections, escalate to root privileges, and bypass container isolation
- **Status**: Newly disclosed vulnerabilities requiring immediate patching

## Affected Systems and Products

- **Google Chrome**: All versions prior to the latest security update, affecting Skia and V8 components
- **Windows 11 Enterprise**: Devices receiving hotpatch updates vulnerable to RRAS RCE flaw
- **AppsFlyer Web SDK**: Websites and applications utilizing the compromised SDK during the attack window
- **Veeam Backup & Replication**: All versions prior to the latest security patches
- **Linux Systems**: Distributions using AppArmor security module vulnerable to privilege escalation
- **Open VSX Registry**: 72 malicious extensions compromising developer environments
- **Steam Gaming Platform**: Eight malicious games distributed through the platform
- **Samsung PCs**: Specific models experiencing C: drive access issues after Windows 11 February 2026 updates

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched Chrome vulnerabilities in targeted attacks
- **Supply Chain Compromise**: Injection of malicious code into legitimate software distribution channels
- **SEO Poisoning**: Distribution of fake VPN clients through manipulated search engine results
- **Malicious Extensions**: Abuse of developer tool repositories to distribute compromised extensions
- **Proxy Botnet Operations**: Enslaving residential routers for criminal proxy services across 163 countries
- **Social Engineering**: Click-fix variants and fake enterprise software downloads to steal credentials
- **Banking Trojan Campaigns**: Real-time human-operated malware targeting Brazilian Pix payment users

## Threat Actor Activities

- **Storm-2561**: Distributing fake enterprise VPN clients from major vendors (Ivanti, Cisco, Fortinet) to steal corporate credentials through SEO poisoning techniques
- **GlassWorm Campaign**: Escalated operations targeting developers through 72 malicious Open VSX extensions, representing significant supply chain threat evolution
- **Chinese State-Sponsored Groups**: Targeting Southeast Asian military organizations with AppleChris and MemFun malware in campaigns dating back to 2020
- **SocksEscort Operators**: Criminal proxy service operators who enslaved 369,000 IP addresses across 163 countries before law enforcement disruption
- **Banking Trojan Groups**: Sophisticated campaigns targeting Brazilian financial institutions with real-time human operators monitoring victim activities
- **Cybercriminal Networks**: Coordinated operations using 45,000 malicious IP addresses for phishing, malware, and ransomware distribution before international law enforcement takedown