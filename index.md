# Exploitation Report

Current exploitation activity reveals critical security threats across multiple platforms and attack vectors. Google has addressed two high-severity Chrome zero-day vulnerabilities affecting Skia and V8 components that are being actively exploited in the wild. Linux systems face significant risks from nine newly disclosed AppArmor vulnerabilities dubbed "CrackArmor" that enable root privilege escalation and container isolation bypass. Supply chain attacks continue to proliferate through multiple campaigns including MacSync malware distribution via fake AI tool installers, AppsFlyer Web SDK hijacking for cryptocurrency theft, and the escalated GlassWorm campaign targeting developers through 72 compromised Open VSX extensions. Microsoft has issued an out-of-band patch for a critical Windows 11 RRAS remote code execution vulnerability, while sophisticated threat actors are deploying advanced techniques including the DRILLAPP backdoor targeting Ukraine and Storm-2561's credential theft operations using fake enterprise VPN clients.

## Active Exploitation Details

### Google Chrome Zero-Day Vulnerabilities
- **Description**: Two high-severity vulnerabilities affecting Chrome's Skia graphics library and V8 JavaScript engine
- **Impact**: Active exploitation in the wild enabling potential code execution and security bypass
- **Status**: Patched by Google in latest Chrome security update

### Linux AppArmor CrackArmor Vulnerabilities
- **Description**: Nine security flaws within the Linux kernel's AppArmor security module
- **Impact**: Unprivileged users can circumvent kernel protections, escalate to root privileges, and bypass container isolation
- **Status**: Disclosed vulnerabilities requiring immediate patching

### Windows 11 RRAS Remote Code Execution Flaw
- **Description**: Critical vulnerability in Windows 11 Routing and Remote Access Service (RRAS)
- **Impact**: Remote code execution capability on affected Windows 11 Enterprise systems
- **Status**: Microsoft released out-of-band hotpatch update

### AppsFlyer Web SDK Supply Chain Attack
- **Description**: Temporary hijacking of AppsFlyer Web SDK with malicious cryptocurrency-stealing code
- **Impact**: JavaScript code injection enabling cryptocurrency theft from affected websites
- **Status**: Supply chain compromise temporarily active before mitigation

## Affected Systems and Products

- **Google Chrome**: All versions prior to latest security update, affecting Skia and V8 components
- **Linux Systems**: All distributions using AppArmor security module in kernel
- **Windows 11 Enterprise**: Systems receiving hotpatch updates, specifically RRAS component
- **macOS Systems**: Targeted by MacSync infostealer via fake AI tool installers
- **Open VSX Registry**: 72 compromised extensions in GlassWorm campaign targeting developers
- **Steam Gaming Platform**: Eight malicious games used for malware distribution
- **Web Applications**: Sites using AppsFlyer Web SDK affected by supply chain attack
- **Samsung Laptops**: Specific models experiencing C: drive access issues after February 2026 updates
- **Enterprise VPN Users**: Targets of fake Ivanti, Cisco, and Fortinet VPN client distributions

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of Chrome vulnerabilities in Skia and V8 components
- **Supply Chain Attacks**: Multiple campaigns including AppsFlyer SDK hijacking and GlassWorm extension compromise
- **Social Engineering**: ClickFix campaigns using fake AI tool installers and captcha-style prompts
- **SEO Poisoning**: Storm-2561 using search engine optimization manipulation to distribute fake VPN clients
- **Container Escape**: CrackArmor vulnerabilities enabling bypass of Linux container isolation
- **Microsoft Edge Debugging Abuse**: DRILLAPP backdoor leveraging Edge debugging features for stealth
- **Gaming Platform Abuse**: Malicious games uploaded to Steam for malware distribution
- **Fake Software Distribution**: Trojan VPN clients masquerading as legitimate enterprise solutions

## Threat Actor Activities

- **Storm-2561**: Credential theft campaign using fake enterprise VPN clients from Ivanti, Cisco, and Fortinet distributed through SEO poisoning
- **Russian-linked Actors**: DRILLAPP backdoor campaign targeting Ukrainian entities using Microsoft Edge debugging for stealth espionage
- **Chinese Cyber Espionage Groups**: AppleChris and MemFun malware deployment against Southeast Asian military organizations in campaigns dating back to 2020
- **GlassWorm Campaign Operators**: Significant escalation with 72 compromised Open VSX extensions targeting developers
- **MacSync Distributors**: Three separate ClickFix campaigns delivering macOS infostealer via fake AI tool installers
- **Banking Trojan Operations**: Real-time attacks targeting Brazil's Pix payment system users with human-operated malware
- **Cybercrime Infrastructure**: INTERPOL operation dismantled 45,000 malicious IP addresses used for phishing, malware, and ransomware campaigns