# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms with significant focus on zero-day vulnerabilities in Google Chrome, supply-chain attacks against development tools, and sophisticated credential theft campaigns. Two Chrome zero-day vulnerabilities affecting the Skia graphics library and V8 JavaScript engine are being actively exploited in the wild, prompting emergency security updates from Google. Supply-chain attacks have escalated with the hijacking of the AppsFlyer Web SDK to spread cryptocurrency-stealing malware and the GlassWorm campaign abusing 72 Open VSX extensions to target developers. Additionally, a threat actor designated Storm-2561 is conducting widespread credential theft operations using fake VPN clients distributed through search engine optimization poisoning techniques.

## Active Exploitation Details

### Chrome Zero-Day Vulnerabilities in Skia and V8
- **Description**: Two high-severity vulnerabilities affecting Google Chrome's Skia graphics library and V8 JavaScript engine
- **Impact**: Attackers can achieve remote code execution and potentially gain control of affected systems
- **Status**: Actively exploited in the wild; Google has released emergency security updates to address both vulnerabilities

### AppsFlyer Web SDK Supply-Chain Attack
- **Description**: The AppsFlyer Web SDK was temporarily compromised with malicious JavaScript code designed to steal cryptocurrency
- **Impact**: Websites using the compromised SDK exposed users to cryptocurrency theft
- **Status**: Supply-chain attack was detected and remediated; SDK was temporarily hijacked during the attack window

### Windows 11 RRAS Remote Code Execution Vulnerability
- **Description**: A security vulnerability affecting Windows 11 Enterprise devices' Routing and Remote Access Service (RRAS)
- **Impact**: Remote code execution capabilities for attackers
- **Status**: Microsoft has released an out-of-band hotpatch update to address the vulnerability

### Linux AppArmor CrackArmor Vulnerabilities
- **Description**: Nine security vulnerabilities within the Linux kernel's AppArmor module that allow unprivileged users to circumvent kernel protections
- **Impact**: Root privilege escalation and container isolation bypass
- **Status**: Multiple critical flaws enabling unprivileged users to escalate privileges and bypass security controls

### Veeam Backup & Replication Critical Flaws
- **Description**: Seven critical vulnerabilities in Veeam's Backup & Replication software
- **Impact**: Remote code execution capabilities for attackers
- **Status**: Veeam has released security updates to address all identified vulnerabilities

## Affected Systems and Products

- **Google Chrome**: All versions prior to the latest security update affecting Skia graphics library and V8 JavaScript engine
- **Windows 11 Enterprise**: Devices receiving hotpatch updates, specifically affecting RRAS functionality
- **AppsFlyer Web SDK**: Websites and applications integrating the compromised SDK during the attack window
- **Open VSX Registry**: Development environments using compromised extensions from the GlassWorm campaign
- **Linux Systems**: Distributions using AppArmor module with the CrackArmor vulnerabilities
- **Veeam Backup & Replication**: Enterprise backup solutions running vulnerable versions
- **VPN Clients**: Fake clients impersonating Ivanti, Cisco, and Fortinet enterprise VPN solutions
- **Steam Gaming Platform**: Eight malicious games uploaded to distribute malware to users
- **Samsung Laptops**: Specific models experiencing C: drive access issues after Windows 11 February 2026 security updates

## Attack Vectors and Techniques

- **Supply-Chain Poisoning**: Compromising legitimate software distribution channels including SDK repositories and browser extension marketplaces
- **SEO Poisoning**: Manipulating search engine results to promote fake VPN client downloads for credential theft
- **Zero-Day Exploitation**: Leveraging previously unknown vulnerabilities in widely-used software before patches are available
- **Fake Software Distribution**: Creating counterfeit versions of legitimate enterprise security tools to steal credentials
- **Gaming Platform Abuse**: Uploading malicious games to legitimate gaming platforms to reach unsuspecting users
- **Proxy Botnet Operations**: Enslaving residential routers into botnets for criminal proxy services across 163 countries

## Threat Actor Activities

- **Storm-2561**: Conducting widespread credential theft campaigns using fake enterprise VPN clients distributed through SEO poisoning techniques targeting Ivanti, Cisco, and Fortinet users
- **GlassWorm Campaign Operators**: Escalating supply-chain attacks by abusing 72 Open VSX extensions to target software developers and development environments
- **Chinese State-Sponsored Groups**: Targeting Southeast Asian military organizations with AppleChris and MemFun malware in campaigns dating back to at least 2020
- **SocksEscort Operators**: Managing a criminal proxy service that enslaved 369,000 IP addresses across 163 countries before law enforcement disruption
- **Banking Trojan Operators**: Targeting Brazil's Pix payment system users with real-time human-operated malware campaigns
- **Click-Fix Variant Distributors**: Developing new variants of click-fix attack techniques to bypass security measures
- **Steam Malware Distributors**: Uploading eight malicious games to the Steam platform to distribute malware to gaming communities