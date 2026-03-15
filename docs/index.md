# Exploitation Report

Current exploitation activity reveals a concerning landscape of active zero-day vulnerabilities and sophisticated attack campaigns targeting critical infrastructure and enterprise systems. Google has patched two high-severity Chrome zero-day vulnerabilities affecting the Skia graphics engine and V8 JavaScript engine that were actively exploited in attacks. Microsoft released emergency out-of-band updates for a Windows 11 RRAS remote code execution vulnerability. Multiple supply-chain attacks are ongoing, including the hijacking of AppsFlyer Web SDK to distribute cryptocurrency-stealing malware and the GlassWorm campaign targeting developers through 72 compromised Open VSX extensions. State-sponsored actors continue targeting military organizations across Southeast Asia with custom malware, while cybercriminals exploit residential networks through massive botnets affecting hundreds of thousands of IPs globally.

## Active Exploitation Details

### Chrome Zero-Day Vulnerabilities
- **Description**: Two high-severity vulnerabilities affecting Chrome's Skia graphics engine and V8 JavaScript engine components
- **Impact**: Remote code execution allowing attackers to compromise user systems through malicious web content
- **Status**: Actively exploited in the wild, emergency patches released by Google

### Windows 11 RRAS Remote Code Execution Flaw
- **Description**: Critical vulnerability in Windows 11 Routing and Remote Access Service (RRAS) component
- **Impact**: Remote code execution on Windows 11 Enterprise systems
- **Status**: Out-of-band hotpatch released by Microsoft for hotpatch-enabled systems

### AppsFlyer Web SDK Supply-Chain Attack
- **Description**: Temporary hijacking of the AppsFlyer Web SDK with malicious JavaScript code
- **Impact**: Cryptocurrency theft from websites using the compromised SDK
- **Status**: Supply-chain attack temporarily active, affecting multiple websites

### Nine AppArmor Vulnerabilities (CrackArmor)
- **Description**: Multiple security flaws in Linux kernel's AppArmor module
- **Impact**: Unprivileged users can escalate to root privileges and bypass container isolation
- **Status**: Vulnerabilities disclosed, patches required for affected Linux systems

## Affected Systems and Products

- **Google Chrome**: All versions prior to latest security update, affecting Skia graphics and V8 JavaScript engines
- **Windows 11 Enterprise**: Devices receiving hotpatch updates, specifically RRAS component
- **AppsFlyer Web SDK**: Websites using the SDK during the compromise window
- **Linux Systems**: Distributions using AppArmor security module
- **Samsung PCs**: Windows 11 systems experiencing C: drive access issues after February 2026 updates
- **Steam Platform**: Eight malicious games containing malware
- **Open VSX Registry**: 72 compromised extensions targeting developers
- **VPN Clients**: Fake Ivanti, Cisco, and Fortinet VPN applications
- **Veeam Backup & Replication**: Seven critical vulnerabilities allowing remote code execution

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched Chrome vulnerabilities through malicious web content
- **Supply-Chain Attacks**: Compromise of legitimate software distribution channels including SDK hijacking and malicious extensions
- **SEO Poisoning**: Fake VPN clients distributed through manipulated search results
- **Malicious Gaming Content**: Distribution of malware through Steam gaming platform
- **Credential Theft**: Trojan VPN clients designed to steal enterprise credentials
- **Botnet Infrastructure**: SocksEscort proxy botnet exploiting 369,000 residential IP addresses across 163 countries
- **Social Engineering**: Click-Fix variants and fake software downloads

## Threat Actor Activities

- **Storm-2561**: Distributing fake enterprise VPN clients from major vendors to steal credentials through SEO poisoning campaigns
- **Chinese State-Sponsored Groups**: Targeting Southeast Asian military organizations with AppleChris and MemFun malware in campaigns dating back to 2020
- **GlassWorm Campaign**: Escalated supply-chain attacks through 72 compromised Open VSX extensions targeting software developers
- **SocksEscort Operators**: Criminal proxy service operators enslaving residential routers across 163 countries before law enforcement disruption
- **Banking Trojan Groups**: Real-time operators targeting Brazil's Pix payment system users with human-operated malware
- **Cryptocurrency Thieves**: Attackers exploiting supply-chain vulnerabilities to inject crypto-stealing code into legitimate web services
- **Ransomware Groups**: Continuing operations using infrastructure disrupted in INTERPOL Operation Synergia III, which resulted in 94 arrests and 45,000 malicious IP addresses being sinkholed