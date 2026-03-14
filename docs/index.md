# Exploitation Report

Critical exploitation activity is currently dominated by two actively exploited Google Chrome zero-day vulnerabilities affecting the Skia graphics library and V8 JavaScript engine, alongside multiple supply-chain attacks targeting developers and organizations. The Chrome vulnerabilities represent immediate threats to millions of users, while sophisticated campaigns like GlassWorm are compromising development environments through malicious VSX extensions. Additionally, threat actors are leveraging fake VPN clients and SEO poisoning techniques to steal enterprise credentials, and multiple critical vulnerabilities have been discovered in Veeam Backup & Replication software and Linux AppArmor that could enable remote code execution and privilege escalation.

## Active Exploitation Details

### Google Chrome Zero-Day Vulnerabilities
- **Description**: Two high-severity vulnerabilities in Google Chrome's Skia graphics library and V8 JavaScript engine that are being actively exploited in the wild
- **Impact**: Attackers can potentially achieve remote code execution and compromise user systems through malicious websites
- **Status**: Google has released emergency security updates to patch these vulnerabilities
- **CVE ID**: CVE-2026-20023 (Skia), CVE-2026-20024 (V8)

### AppsFlyer Web SDK Supply-Chain Attack
- **Description**: The AppsFlyer Web SDK was temporarily hijacked with malicious JavaScript code designed to steal cryptocurrency
- **Impact**: Websites using the compromised SDK could have their visitors' cryptocurrency wallets targeted and funds stolen
- **Status**: The attack has been identified and mitigated, but affected websites may have been compromised during the attack window

### GlassWorm VSX Extension Campaign
- **Description**: A significant escalation of the GlassWorm campaign targeting developers through 72 malicious Open VSX extensions
- **Impact**: Compromise of developer environments and potential injection of malicious code into software projects
- **Status**: Active campaign targeting the development community through infected Visual Studio Code extensions

## Affected Systems and Products

- **Google Chrome**: All versions prior to the latest security update containing patches for Skia and V8 vulnerabilities
- **AppsFlyer Web SDK**: Websites and applications using the compromised SDK during the attack window
- **Open VSX Registry**: Developer environments using affected extensions from the compromised registry
- **Veeam Backup & Replication**: Multiple versions containing seven critical vulnerabilities enabling remote code execution
- **Linux AppArmor**: Systems running affected versions of the Linux kernel's AppArmor security module
- **Samsung Windows 11 PCs**: Specific Samsung laptop models experiencing C: drive access issues after February 2026 security updates
- **Steam Gaming Platform**: Eight malicious games identified as containing malware
- **Enterprise VPN Systems**: Fake clients impersonating Ivanti, Cisco, and Fortinet VPN solutions

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched Chrome vulnerabilities through malicious websites
- **Supply-Chain Compromise**: Hijacking of legitimate SDKs and development tools to distribute malicious code
- **SEO Poisoning**: Using search engine optimization techniques to promote fake VPN download sites
- **Social Engineering**: Distributing trojan VPN clients disguised as legitimate enterprise security tools
- **Malicious Extensions**: Compromising developer environments through infected VSX registry extensions
- **Gaming Platform Abuse**: Using Steam as a distribution mechanism for malware through fake games

## Threat Actor Activities

- **Storm-2561**: Microsoft-tracked group distributing fake enterprise VPN clients through SEO poisoning to steal corporate credentials
- **Chinese APT Groups**: Targeting Southeast Asian military organizations with AppleChris and MemFun malware in campaigns dating back to 2020
- **GlassWorm Operators**: Escalating supply-chain attacks through compromised developer tools and extensions
- **Banking Trojan Operators**: Targeting Brazil's Pix payment system users with real-time operator-assisted attacks
- **SocksEscort Botnet**: International criminal operation that enslaved 369,000 residential router IPs across 163 countries before law enforcement disruption