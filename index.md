# Exploitation Report

Critical exploitation activity is currently affecting multiple platforms with several zero-day vulnerabilities being actively exploited in the wild. The most significant threats include two Chrome zero-day vulnerabilities in the Skia graphics library and V8 JavaScript engine, nine Linux AppArmor vulnerabilities enabling privilege escalation, and a Windows 11 RRAS remote code execution flaw requiring emergency patching. Additionally, widespread supply chain attacks are targeting developers through compromised SDK packages and malicious browser extensions, while threat actors continue exploiting vulnerabilities in enterprise systems and cloud environments.

## Active Exploitation Details

### Chrome Zero-Day Vulnerabilities in Skia and V8
- **Description**: Two high-severity vulnerabilities affecting Google Chrome's Skia graphics library and V8 JavaScript engine
- **Impact**: Remote code execution and potential system compromise through browser exploitation
- **Status**: Actively exploited in the wild, security updates released by Google

### Windows 11 RRAS Remote Code Execution Vulnerability
- **Description**: Critical security vulnerability affecting Windows 11 Enterprise devices' Routing and Remote Access Service (RRAS)
- **Impact**: Remote code execution allowing attackers to gain system control
- **Status**: Out-of-band hotpatch released by Microsoft for Enterprise systems

### Linux AppArmor CrackArmor Vulnerabilities
- **Description**: Nine security flaws within the Linux kernel's AppArmor security module
- **Impact**: Unprivileged users can circumvent kernel protections, escalate privileges to root, and bypass container isolation
- **Status**: Multiple vulnerabilities identified and disclosed, patches required

### Veeam Backup & Replication Critical Flaws
- **Description**: Seven critical vulnerabilities in Veeam's Backup & Replication software
- **Impact**: Remote code execution capabilities allowing complete system compromise
- **Status**: Security updates released by Veeam

## Affected Systems and Products

- **Google Chrome**: Skia graphics library and V8 JavaScript engine components affected
- **Windows 11 Enterprise**: Routing and Remote Access Service (RRAS) functionality
- **Linux Systems**: AppArmor security module in Linux kernel
- **Veeam Backup & Replication**: Enterprise backup software installations
- **AppsFlyer Web SDK**: JavaScript SDK used in web applications
- **Open VSX Extensions**: 72 malicious extensions in the Visual Studio Code marketplace
- **Steam Gaming Platform**: Eight malicious games containing malware
- **Samsung Windows 11 PCs**: C: drive access issues after February 2026 security updates
- **Southeast Asian Military Organizations**: Targeted by state-sponsored campaigns

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Compromising legitimate software packages and SDKs to distribute malware
- **Browser Exploitation**: Zero-day vulnerabilities in Chrome components for remote code execution
- **SEO Poisoning**: Fake VPN client distribution through manipulated search engine results
- **Malicious Extensions**: Trojanized VS Code extensions in Open VSX registry
- **Container Escape**: Linux AppArmor bypass techniques for privilege escalation
- **Credential Harvesting**: Fake enterprise VPN clients stealing authentication credentials
- **Cryptocurrency Theft**: JavaScript injection for wallet draining attacks
- **Phishing Campaigns**: Advanced social engineering targeting enterprise users

## Threat Actor Activities

- **Storm-2561**: Distributing fake enterprise VPN clients from Ivanti, Cisco, and Fortinet to steal credentials through SEO poisoning techniques
- **GlassWorm Campaign**: Escalated supply chain attacks through 72 compromised Open VSX extensions targeting developers
- **Chinese State-Sponsored Groups**: Targeting Southeast Asian military organizations with AppleChris and MemFun malware since 2020
- **SocksEscort Operators**: Running proxy botnet exploiting 369,000 IP addresses across 163 countries before law enforcement disruption
- **Banking Trojan Operators**: Real-time attacks targeting Brazil's Pix payment system users with human-operated malware
- **Steam Game Publishers**: Eight malicious games uploaded to Steam platform for malware distribution