# Exploitation Report

Current threat activity reveals significant exploitation across multiple attack vectors, with Google Chrome zero-day vulnerabilities being actively exploited in the wild, nine critical Linux AppArmor flaws enabling root escalation and container bypass, and seven critical Veeam Backup & Replication vulnerabilities allowing remote code execution. Supply-chain attacks are escalating through hijacked SDKs and malicious browser extensions, while threat actors increasingly target enterprise VPNs through fake clients and SEO poisoning campaigns. State-sponsored groups continue sophisticated operations against military targets, and law enforcement efforts have disrupted major botnets affecting hundreds of thousands of compromised systems worldwide.

## Active Exploitation Details

### Chrome Zero-Day Vulnerabilities in Skia and V8
- **Description**: Two high-severity vulnerabilities in Google Chrome affecting the Skia graphics engine and V8 JavaScript engine
- **Impact**: Active exploitation in the wild allowing attackers to compromise Chrome browsers
- **Status**: Patched by Google with emergency security updates, actively exploited before patches were available

### Linux AppArmor CrackArmor Vulnerabilities
- **Description**: Nine security vulnerabilities within the Linux kernel's AppArmor module that can be exploited by unprivileged users
- **Impact**: Circumvention of kernel protections, privilege escalation to root, and bypassing container isolation
- **Status**: Disclosed vulnerabilities requiring patching across Linux distributions

### Veeam Backup & Replication Critical Flaws
- **Description**: Seven critical vulnerabilities in Veeam's Backup & Replication software
- **Impact**: Remote code execution capabilities for attackers
- **Status**: Security updates released by Veeam to address all seven critical vulnerabilities

### AppsFlyer Web SDK Supply-Chain Attack
- **Description**: Malicious code injection into the AppsFlyer Web SDK used for mobile app analytics
- **Impact**: Cryptocurrency theft through malicious JavaScript code distributed to websites using the SDK
- **Status**: Temporary hijacking resolved, but affected websites needed to update their implementations

## Affected Systems and Products

- **Google Chrome**: All versions prior to the latest security update, affecting Skia graphics engine and V8 JavaScript engine
- **Linux Systems**: AppArmor-enabled distributions vulnerable to nine privilege escalation flaws
- **Veeam Backup & Replication**: Enterprise backup solutions with seven critical remote code execution vulnerabilities
- **AppsFlyer Web SDK**: Mobile analytics SDK temporarily compromised in supply-chain attack
- **Open VSX Registry**: 72 malicious extensions targeting developers through GlassWorm campaign
- **Steam Gaming Platform**: Eight malicious games identified by FBI investigation
- **Enterprise VPN Clients**: Fake Ivanti, Cisco, and Fortinet VPN clients used for credential theft
- **Windows 11 on Samsung PCs**: C: drive access issues after February 2026 security updates

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched Chrome vulnerabilities before disclosure
- **Supply-Chain Attacks**: SDK hijacking and malicious browser extension distribution through legitimate platforms
- **SEO Poisoning**: Search engine optimization techniques to distribute fake VPN clients
- **Credential Harvesting**: Fake enterprise VPN applications designed to steal corporate credentials
- **Container Escape**: Linux AppArmor vulnerabilities enabling escape from containerized environments
- **Privilege Escalation**: Unprivileged users gaining root access through kernel module vulnerabilities
- **Botnet Operations**: SocksEscort proxy botnet enslaving residential routers across 163 countries

## Threat Actor Activities

- **Storm-2561**: Microsoft-tracked threat actor distributing fake enterprise VPN clients through SEO poisoning to steal credentials from Ivanti, Cisco, and Fortinet users
- **Chinese State-Sponsored Groups**: Suspected China-based cyber espionage operation targeting Southeast Asian military organizations since 2020 using AppleChris and MemFun malware
- **GlassWorm Campaign**: Escalated supply-chain attack through 72 malicious Open VSX extensions targeting developers
- **Iranian MOIS**: Ministry of Intelligence collaboration with cybercriminal groups to enhance cyberattack capabilities
- **AiLock Ransomware**: Targeting organizations including England Hockey governing body
- **SocksEscort Operators**: Criminal proxy service operators managing botnet of 369,000 compromised IP addresses across 163 countries before law enforcement disruption