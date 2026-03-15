# Exploitation Report

Multiple critical zero-day vulnerabilities and active exploitation campaigns have been identified across various platforms and products. The most significant activity includes two Chrome zero-day vulnerabilities actively exploited in the wild affecting the Skia graphics library and V8 JavaScript engine, requiring immediate patching. Additionally, nine critical Linux AppArmor vulnerabilities collectively dubbed "CrackArmor" enable privilege escalation and container isolation bypass. Supply chain attacks have escalated with malicious code injection into the AppsFlyer Web SDK for cryptocurrency theft and the GlassWorm campaign targeting developers through 72 compromised Open VSX extensions. Seven critical remote code execution vulnerabilities in Veeam Backup & Replication software pose significant risks to enterprise backup infrastructure.

## Active Exploitation Details

### Chrome Zero-Day Vulnerabilities
- **Description**: Two high-severity vulnerabilities in Google Chrome affecting the Skia graphics library and V8 JavaScript engine
- **Impact**: Complete system compromise through arbitrary code execution in the browser context
- **Status**: Actively exploited in the wild, security patches released by Google

### Linux AppArmor CrackArmor Vulnerabilities
- **Description**: Nine security flaws within the Linux kernel's AppArmor security module
- **Impact**: Unprivileged users can escalate to root privileges and bypass container isolation protections
- **Status**: Disclosed vulnerabilities requiring immediate kernel updates

### Veeam Backup & Replication Critical Flaws
- **Description**: Seven critical vulnerabilities in Veeam's enterprise backup solution
- **Impact**: Remote code execution allowing complete compromise of backup infrastructure
- **Status**: Security patches released, immediate updates required

### AppsFlyer Web SDK Supply Chain Attack
- **Description**: Malicious code injection into the AppsFlyer Web SDK library
- **Impact**: Cryptocurrency theft through compromised JavaScript code execution on affected websites
- **Status**: Temporary hijacking detected and resolved

## Affected Systems and Products

- **Google Chrome**: All versions prior to the latest security update across Windows, macOS, and Linux platforms
- **Linux Systems**: Any distribution using AppArmor security module for mandatory access control
- **Veeam Backup & Replication**: Enterprise backup infrastructure across all supported versions
- **AppsFlyer Web SDK**: Websites and applications integrating the compromised SDK version
- **Open VSX Registry**: Development environments using affected extensions from the registry
- **Steam Gaming Platform**: Eight malicious games distributed through the official platform
- **Samsung Laptops**: Windows 11 systems experiencing C: drive access issues after February 2026 updates
- **Enterprise VPN Clients**: Fake Ivanti, Cisco, and Fortinet VPN applications

## Attack Vectors and Techniques

- **Browser Exploitation**: Zero-day vulnerabilities targeting Chrome's graphics and JavaScript engines for code execution
- **Supply Chain Compromise**: Injection of malicious code into legitimate software development tools and libraries
- **SEO Poisoning**: Manipulation of search engine results to distribute fake VPN clients and malware
- **Container Escape**: Exploitation of AppArmor vulnerabilities to break out of containerized environments
- **Social Engineering**: Click-fix variants and fake enterprise software to steal credentials
- **Malicious Extensions**: Abuse of developer tools through compromised Visual Studio Code extensions
- **Proxy Botnet Operations**: SocksEscort botnet enslaving residential routers across 163 countries

## Threat Actor Activities

- **Storm-2561**: Distributing trojan VPN clients through SEO poisoning to steal enterprise credentials from Ivanti, Cisco, and Fortinet users
- **GlassWorm Campaign**: Escalated supply chain attacks through 72 compromised Open VSX extensions targeting software developers
- **Chinese APT Groups**: Sustained espionage operations against Southeast Asian military organizations using AppleChris and MemFun malware since 2020
- **Brazilian Banking Trojans**: Real-time attacks against Pix payment system users combining automated malware with human operators
- **SocksEscort Operators**: International cybercriminal network operating proxy botnet across 369,000 compromised IP addresses
- **Steam Malware Distributors**: Threat actors uploading eight malicious games to the Steam platform for malware distribution
- **Iranian MOIS**: Collaboration with cybercriminal groups to enhance cyberattack capabilities and expand operational reach