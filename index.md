# Exploitation Report

Current threat intelligence reveals significant active exploitation across multiple attack vectors, including critical zero-day vulnerabilities in widely-used software, sophisticated supply chain attacks targeting developer environments, and advanced malware campaigns leveraging novel techniques. Two Chrome zero-day vulnerabilities affecting Skia and V8 components have been confirmed as exploited in the wild, while threat actors continue to abuse legitimate services and APIs for credential theft and data exfiltration. Notable campaigns include the GlassWorm supply chain attack compromising 72 Open VSX extensions, Storm-2561's fake VPN distribution operation, and DRILLAPP backdoor targeting Ukrainian entities through Microsoft Edge debugging abuse.

## Active Exploitation Details

### Chrome Zero-Day Vulnerabilities
- **Description**: Two high-severity vulnerabilities affecting Chrome's Skia graphics library and V8 JavaScript engine components
- **Impact**: Attackers can achieve code execution and potentially compromise user systems through browser exploitation
- **Status**: Google has released security updates to address both vulnerabilities; active exploitation confirmed in the wild

### Windows 11 RRAS Remote Code Execution Flaw
- **Description**: Security vulnerability affecting Windows 11 Enterprise devices that receive hotpatch updates, specifically targeting the Routing and Remote Access Service (RRAS)
- **Impact**: Remote code execution capability allowing attackers to gain unauthorized system access
- **Status**: Microsoft has released an out-of-band hotpatch update to address the vulnerability

### Linux AppArmor CrackArmor Vulnerabilities
- **Description**: Nine security vulnerabilities within the Linux kernel's AppArmor security module
- **Impact**: Unprivileged users can circumvent kernel protections, escalate privileges to root level, and bypass container isolation mechanisms
- **Status**: Multiple flaws identified enabling privilege escalation and container escape scenarios

## Affected Systems and Products

- **Google Chrome**: Skia graphics library and V8 JavaScript engine components affected by zero-day exploits
- **Windows 11 Enterprise**: Systems receiving hotpatch updates vulnerable to RRAS remote code execution
- **Linux Systems**: AppArmor-enabled distributions susceptible to privilege escalation through kernel module flaws
- **macOS Systems**: Targeted by MacSync infostealer through fake AI tool installers
- **Microsoft Edge**: Debugging features abused by DRILLAPP backdoor for stealth operations
- **Open VSX Registry**: 72 extensions compromised in GlassWorm supply chain attack
- **AppsFlyer Web SDK**: Temporarily hijacked to distribute cryptocurrency-stealing malware
- **Steam Gaming Platform**: Eight malicious games uploaded containing malware payloads
- **Samsung Windows 11 PCs**: C: drive access issues following February 2026 security updates

## Attack Vectors and Techniques

- **Browser Exploitation**: Zero-day vulnerabilities in Chrome components enabling code execution
- **Supply Chain Attacks**: Compromised developer extensions and SDK hijacking for malware distribution
- **Social Engineering**: ClickFix campaigns using fake error messages to distribute malware
- **SEO Poisoning**: Malicious websites optimized for search rankings distributing fake VPN clients
- **API Abuse**: Microsoft Edge debugging features exploited for persistent backdoor access
- **Phishing Campaigns**: Fake enterprise VPN download sites stealing corporate credentials
- **Container Escape**: Linux AppArmor flaws enabling privilege escalation and isolation bypass
- **Gaming Platform Abuse**: Malicious games uploaded to Steam for malware distribution

## Threat Actor Activities

- **Storm-2561**: Distributing fake enterprise VPN clients from Ivanti, Cisco, and Fortinet through SEO poisoning to steal corporate credentials
- **Russian-Linked Groups**: Deploying DRILLAPP backdoor against Ukrainian entities using Microsoft Edge debugging for stealth espionage
- **Chinese APT Groups**: Targeting Southeast Asian military organizations with AppleChris and MemFun malware in state-sponsored campaigns dating back to 2020
- **GlassWorm Campaign Operators**: Escalating supply chain attacks through 72 compromised Open VSX extensions targeting developer environments
- **ClickFix Campaign Groups**: Operating three distinct campaigns delivering MacSync infostealer through fake AI tool installers
- **Brazil-Focused Banking Trojans**: Targeting Pix payment system users with real-time human-operated malware campaigns
- **INTERPOL Operation**: Law enforcement dismantled 45,000 malicious IP addresses and arrested 94 individuals in global cybercrime crackdown