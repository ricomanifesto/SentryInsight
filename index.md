# Exploitation Report

Current exploitation activity reveals several critical security incidents including zero-day attacks against Chrome browser components, supply chain compromises targeting developers through malicious SDK hijacking and VSCode extensions, and sophisticated credential theft campaigns using fake VPN clients. Notable threats include actively exploited Chrome vulnerabilities affecting the Skia graphics library and V8 JavaScript engine, a successful hijacking of the AppsFlyer Web SDK for cryptocurrency theft, and the GlassWorm campaign's escalation through compromised development tools. Law enforcement operations have successfully disrupted major cybercriminal infrastructure including the SocksEscort proxy botnet and thousands of malicious IP addresses used in global cybercrime operations.

## Active Exploitation Details

### Chrome Zero-Day Vulnerabilities
- **Description**: Two high-severity vulnerabilities affecting Chrome's Skia graphics library and V8 JavaScript engine that have been actively exploited in the wild
- **Impact**: Attackers can achieve code execution and potentially compromise user systems through malicious web content
- **Status**: Patched by Google in emergency security updates, but exploitation was confirmed in active attacks
- **CVE ID**: CVE-2026-0127 (Skia component) and CVE-2026-0128 (V8 JavaScript engine)

### Linux AppArmor CrackArmor Vulnerabilities
- **Description**: Nine security flaws in the Linux kernel's AppArmor security module that allow unprivileged users to bypass kernel protections
- **Impact**: Enables root privilege escalation and container isolation bypass, compromising system security boundaries
- **Status**: Vulnerabilities disclosed but patch status not specified in source material

### Windows 11 RRAS Remote Code Execution
- **Description**: Critical vulnerability affecting Windows 11 Enterprise systems running Routing and Remote Access Service (RRAS)
- **Impact**: Remote code execution capability allowing complete system compromise
- **Status**: Microsoft released out-of-band hotpatch update to address the vulnerability

## Affected Systems and Products

- **Google Chrome**: All versions prior to emergency security updates addressing Skia and V8 components
- **Linux Systems**: Systems running AppArmor security module vulnerable to privilege escalation attacks
- **Windows 11 Enterprise**: Systems with RRAS service enabled, particularly those receiving hotpatch updates
- **AppsFlyer SDK**: Web applications using the compromised SDK during the hijacking period
- **VSCode Ecosystem**: Developers using Open VSX registry extensions targeted by GlassWorm campaign
- **Samsung Laptops**: Windows 11 systems experiencing C: drive access issues after February 2026 updates
- **Steam Gaming Platform**: Eight malicious games identified as malware distribution vectors

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Hijacking of legitimate SDKs and development tools to distribute malicious code
- **SEO Poisoning**: Manipulation of search results to distribute fake VPN clients and malicious software
- **Zero-Day Exploitation**: Active exploitation of unpatched vulnerabilities in widely-used software
- **Malicious Extensions**: Abuse of development environment extensions to target software developers
- **Fake Software Distribution**: Creation of convincing replicas of legitimate enterprise VPN clients
- **Social Engineering**: Click-fix campaigns and fake software downloads to trick users into installing malware
- **Botnet Operations**: Enslaving residential routers and devices for proxy services and cybercrime infrastructure

## Threat Actor Activities

- **Storm-2561**: Distributing fake enterprise VPN clients from major vendors (Ivanti, Cisco, Fortinet) using SEO poisoning to steal corporate credentials
- **GlassWorm Campaign**: Escalated supply chain attacks through 72 compromised Open VSX extensions targeting software developers
- **Chinese APT Groups**: Long-term espionage campaigns against Southeast Asian military organizations using AppleChris and MemFun malware since 2020
- **SocksEscort Operators**: Criminal proxy service operators who enslaved 369,000 IP addresses across 163 countries before law enforcement disruption
- **Banking Trojan Groups**: Brazilian-focused campaigns targeting Pix payment system users with real-time human-operated attacks
- **AppsFlyer Attackers**: Unknown actors who successfully hijacked the AppsFlyer Web SDK to deploy cryptocurrency-stealing JavaScript code
- **Steam Malware Distributors**: Criminals who uploaded eight malicious games to Steam platform for malware distribution, now under FBI investigation