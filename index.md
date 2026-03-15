# Exploitation Report

The current threat landscape reveals intense exploitation activity across multiple attack vectors, with several critical zero-day vulnerabilities being actively exploited in the wild. Google has released emergency patches for two high-severity Chrome zero-day vulnerabilities affecting the Skia graphics library and V8 JavaScript engine, which are currently being exploited by threat actors. Supply chain attacks continue to pose significant risks, with the AppsFlyer Web SDK being hijacked to distribute cryptocurrency-stealing JavaScript code and the GlassWorm campaign escalating its abuse of Open VSX extensions to target developers. Microsoft has issued an out-of-band hotpatch for a remote code execution vulnerability in Windows 11's RRAS component, while Linux systems face new privilege escalation threats through nine CrackArmor vulnerabilities in the AppArmor security module. Threat actors are also leveraging sophisticated social engineering techniques, including fake VPN clients distributed through SEO poisoning and malicious Steam games containing malware.

## Active Exploitation Details

### Google Chrome Zero-Day Vulnerabilities
- **Description**: Two high-severity vulnerabilities in Chrome's Skia graphics library and V8 JavaScript engine that allow attackers to compromise web browsers
- **Impact**: Attackers can achieve remote code execution and potentially gain full control over victim systems through browser exploitation
- **Status**: Currently being exploited in active zero-day attacks; emergency security updates released by Google

### Windows 11 RRAS Remote Code Execution
- **Description**: A critical vulnerability in Windows 11's Routing and Remote Access Service (RRAS) that allows remote code execution
- **Impact**: Attackers can execute arbitrary code remotely on Windows 11 Enterprise systems
- **Status**: Microsoft has released an out-of-band hotpatch to address the vulnerability

### AppsFlyer Web SDK Supply Chain Attack
- **Description**: The AppsFlyer Web SDK was temporarily compromised with malicious JavaScript code designed to steal cryptocurrency
- **Impact**: Websites using the compromised SDK could unknowingly serve malicious code to visitors, enabling cryptocurrency theft
- **Status**: Supply chain attack has been contained but demonstrates ongoing risks to JavaScript libraries

### Linux AppArmor Privilege Escalation Vulnerabilities
- **Description**: Nine security vulnerabilities in Linux kernel's AppArmor module that allow unprivileged users to bypass kernel protections
- **Impact**: Attackers can escalate privileges to root level and bypass container isolation mechanisms
- **Status**: Vulnerabilities disclosed as "CrackArmor" flaws affecting Linux systems with AppArmor enabled

### Veeam Backup & Replication Critical Flaws
- **Description**: Seven critical vulnerabilities in Veeam's Backup & Replication software allowing remote code execution
- **Impact**: Attackers can execute arbitrary code on backup infrastructure, potentially compromising entire backup systems
- **Status**: Security updates released by Veeam to address the vulnerabilities

## Affected Systems and Products

- **Google Chrome**: All versions prior to the latest security update containing Skia and V8 component fixes
- **Windows 11 Enterprise**: Systems using RRAS functionality, particularly those receiving hotpatch updates
- **AppsFlyer Web SDK**: Websites and applications integrating the compromised SDK version
- **Linux Systems**: Distributions running AppArmor security module with kernel vulnerabilities
- **Veeam Backup & Replication**: Enterprise backup solutions vulnerable to remote code execution
- **Steam Gaming Platform**: Eight malicious games distributed through the platform
- **Open VSX Registry**: 72 malicious extensions targeting Visual Studio Code developers
- **Samsung Laptops**: Windows 11 systems experiencing C: drive access issues after February 2026 updates

## Attack Vectors and Techniques

- **Zero-Day Browser Exploitation**: Attackers leveraging unpatched Chrome vulnerabilities for remote code execution
- **Supply Chain Attacks**: Compromise of third-party libraries and development tools to distribute malware
- **SEO Poisoning**: Fake VPN client distribution through manipulated search engine results
- **Social Engineering**: Malicious Steam games and fake enterprise software to trick users
- **Credential Theft Campaigns**: Trojan VPN clients designed to steal corporate authentication credentials
- **Container Escape Techniques**: Exploitation of AppArmor vulnerabilities to break out of containerized environments
- **Proxy Botnet Operations**: SocksEscort botnet enslaving residential routers across 163 countries

## Threat Actor Activities

- **Storm-2561**: Conducting credential theft campaigns using fake enterprise VPN clients from major vendors like Ivanti, Cisco, and Fortinet distributed through SEO poisoning
- **GlassWorm Campaign**: Escalated supply chain attacks targeting developers through 72 malicious Open VSX extensions for Visual Studio Code
- **Chinese State-Sponsored Groups**: Targeting Southeast Asian military organizations using AppleChris and MemFun malware in campaigns dating back to 2020
- **Cryptocurrency Thieves**: Exploiting compromised web SDKs and developing specialized banking trojans targeting Brazil's Pix payment system users
- **SocksEscort Operators**: Running proxy botnet operations across 369,000 compromised IP addresses in 163 countries before law enforcement disruption