# Exploitation Report

The current threat landscape reveals critical zero-day vulnerabilities actively exploited in the wild, alongside sophisticated supply-chain attacks targeting developers and enterprise infrastructure. Most notably, Google has patched two high-severity Chrome zero-day vulnerabilities affecting the Skia and V8 engines that were being actively exploited by threat actors. Simultaneously, multiple supply-chain attacks have emerged, including the hijacking of the AppsFlyer Web SDK for cryptocurrency theft, the GlassWorm campaign targeting 72 Open VSX extensions used by developers, and Storm-2561's distribution of malicious VPN clients through SEO poisoning. These incidents demonstrate an escalation in both the sophistication and scope of active exploitation campaigns.

## Active Exploitation Details

### Chrome Zero-Day Vulnerabilities
- **Description**: Two high-severity vulnerabilities in Google Chrome affecting the Skia graphics library and V8 JavaScript engine
- **Impact**: Attackers can achieve arbitrary code execution within the browser context, potentially leading to full system compromise
- **Status**: Actively exploited in the wild; patches released by Google in emergency security updates

### AppsFlyer Web SDK Supply-Chain Attack
- **Description**: The AppsFlyer Web SDK was temporarily hijacked with malicious JavaScript code designed to steal cryptocurrency
- **Impact**: Websites using the compromised SDK exposed visitors to cryptocurrency theft malware
- **Status**: Supply-chain attack successfully executed; SDK has been cleaned

### GlassWorm Campaign VSX Extensions
- **Description**: Malicious campaign compromising 72 extensions in the Open VSX registry targeting developers
- **Impact**: Code execution within developer environments, potential access to source code and development infrastructure
- **Status**: Represents significant escalation in propagation through Open VSX registry

### Windows 11 RRAS Remote Code Execution Flaw
- **Description**: Critical vulnerability in Windows 11 Routing and Remote Access Service (RRAS)
- **Impact**: Remote code execution on affected Windows 11 Enterprise systems
- **Status**: Out-of-band hotpatch released by Microsoft for hotpatch-enabled systems

### Linux AppArmor CrackArmor Vulnerabilities
- **Description**: Nine security vulnerabilities in Linux kernel's AppArmor module
- **Impact**: Unprivileged users can escalate to root privileges and bypass container isolation
- **Status**: Multiple critical flaws enabling privilege escalation and container escape

### Veeam Backup & Replication Critical Flaws
- **Description**: Seven critical vulnerabilities in Veeam's Backup & Replication software
- **Impact**: Remote code execution on backup infrastructure systems
- **Status**: Security updates released to address remote code execution risks

## Affected Systems and Products

- **Google Chrome**: All versions prior to the latest security update affecting Skia and V8 engines
- **Windows 11 Enterprise**: Systems using Routing and Remote Access Service, particularly hotpatch-enabled deployments
- **AppsFlyer Web SDK**: Websites and applications integrating the temporarily compromised SDK
- **Open VSX Registry**: 72 compromised extensions affecting Visual Studio Code and compatible editors
- **Linux Systems**: AppArmor-enabled distributions vulnerable to privilege escalation
- **Veeam Backup & Replication**: Enterprise backup infrastructure running vulnerable versions
- **Enterprise VPN Solutions**: Fake clients impersonating Ivanti, Cisco, and Fortinet products
- **Steam Gaming Platform**: Eight malicious games distributed through the platform
- **Samsung Laptops**: Windows 11 systems experiencing C: drive access issues after February 2026 updates

## Attack Vectors and Techniques

- **Zero-Day Browser Exploitation**: Active exploitation of Chrome vulnerabilities through malicious websites
- **Supply-Chain Compromise**: Hijacking of legitimate development tools and SDKs to distribute malware
- **SEO Poisoning**: Storm-2561 uses search engine manipulation to distribute fake VPN clients
- **Container Escape**: AppArmor vulnerabilities enable breaking out of containerized environments
- **Gaming Platform Abuse**: Distribution of malware through legitimate game distribution platforms
- **Extension Registry Manipulation**: Compromising developer tool extensions for widespread impact
- **Credential Harvesting**: Fake enterprise VPN clients designed to steal corporate authentication data

## Threat Actor Activities

- **Storm-2561**: Conducting credential theft campaigns using fake VPN clients distributed via SEO poisoning, targeting enterprise users with spoofed Ivanti, Cisco, and Fortinet VPN applications
- **GlassWorm Operators**: Escalating supply-chain attacks through Open VSX registry compromise, representing significant evolution in targeting developer ecosystems
- **Chinese APT Groups**: Targeting Southeast Asian military organizations with AppleChris and MemFun malware in ongoing state-sponsored espionage campaigns dating back to 2020
- **Cryptocurrency Thieves**: Hijacking legitimate web SDKs to inject cryptocurrency-stealing JavaScript code into websites
- **SocksEscort Botnet**: Operating proxy service that enslaved 369,000 IP addresses across 163 countries before law enforcement disruption
- **Brazil Banking Trojan Operators**: Deploying real-time human-operated banking Trojans specifically targeting Brazil's Pix payment system users