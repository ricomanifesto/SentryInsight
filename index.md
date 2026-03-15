# Exploitation Report

The cybersecurity landscape continues to face significant exploitation activity across multiple attack vectors. Most notably, Google has addressed two high-severity Chrome zero-day vulnerabilities affecting the Skia graphics library and V8 JavaScript engine that are being actively exploited in the wild. Supply chain attacks remain a persistent threat, with the AppsFlyer Web SDK being hijacked to distribute cryptocurrency-stealing malware and the GlassWorm campaign escalating its abuse of Open VSX extensions to target developers. Multiple Linux kernel vulnerabilities in the AppArmor security module have been discovered that enable privilege escalation and container isolation bypass. Additionally, threat actors are leveraging sophisticated social engineering techniques, including fake VPN clients distributed through SEO poisoning and malicious Steam games, to steal credentials and spread malware.

## Active Exploitation Details

### Chrome Zero-Day Vulnerabilities
- **Description**: Two high-severity vulnerabilities affecting Google Chrome's Skia graphics library and V8 JavaScript engine
- **Impact**: Remote code execution and potential system compromise through browser exploitation
- **Status**: Actively exploited in the wild; Google has released emergency security updates

### AppsFlyer Web SDK Supply Chain Attack
- **Description**: The AppsFlyer Web SDK was temporarily compromised with malicious JavaScript code designed to steal cryptocurrency
- **Impact**: Cryptocurrency theft from users of websites utilizing the compromised SDK
- **Status**: Supply chain attack was detected and contained; affected SDK versions identified

### Windows 11 RRAS Remote Code Execution Flaw
- **Description**: A remote code execution vulnerability affecting Windows 11 Enterprise devices' Routing and Remote Access Service (RRAS)
- **Impact**: Remote attackers could execute arbitrary code on vulnerable Windows 11 Enterprise systems
- **Status**: Microsoft released an out-of-band hotpatch to address the vulnerability

### Linux AppArmor CrackArmor Vulnerabilities
- **Description**: Nine security vulnerabilities within the Linux kernel's AppArmor security module
- **Impact**: Unprivileged users can escalate privileges to root level and bypass container isolation protections
- **Status**: Multiple critical flaws allowing circumvention of kernel protections

## Affected Systems and Products

- **Google Chrome**: Skia graphics library and V8 JavaScript engine components affected by zero-day exploits
- **Windows 11 Enterprise**: Devices receiving hotpatch updates affected by RRAS remote code execution vulnerability
- **AppsFlyer Web SDK**: Websites utilizing the compromised SDK versions targeted in supply chain attack
- **Linux Systems**: AppArmor-enabled distributions vulnerable to privilege escalation and container bypass
- **Steam Platform**: Eight malicious games identified containing malware targeting gamers
- **Samsung Laptops**: Specific models experiencing C: drive access issues after February 2026 Windows 11 updates
- **Veeam Backup & Replication**: Seven critical vulnerabilities allowing remote code execution
- **Open VSX Registry**: 72 malicious extensions used in GlassWorm campaign targeting developers

## Attack Vectors and Techniques

- **Zero-Day Browser Exploitation**: Active exploitation of Chrome vulnerabilities through web-based attacks targeting Skia and V8 components
- **Supply Chain Compromise**: Hijacking of legitimate SDKs and development tools to distribute malware to downstream users
- **SEO Poisoning**: Manipulation of search engine results to distribute fake VPN clients containing credential-stealing malware
- **Social Engineering**: Distribution of trojanized VPN clients masquerading as legitimate enterprise solutions from vendors like Ivanti, Cisco, and Fortinet
- **Malicious Gaming Content**: Use of Steam platform to distribute eight different malicious games containing malware
- **Development Environment Targeting**: Abuse of Visual Studio Code extension marketplace to target software developers
- **Proxy Botnet Operations**: SocksEscort botnet compromising 369,000 IP addresses across 163 countries using residential routers

## Threat Actor Activities

- **Storm-2561**: Microsoft-tracked threat actor distributing fake enterprise VPN clients through SEO poisoning to steal corporate credentials from Ivanti, Cisco, and Fortinet users
- **GlassWorm Campaign**: Escalated operations targeting developers through 72 malicious Open VSX extensions in the Visual Studio Code marketplace
- **Chinese State-Sponsored Groups**: Suspected China-based cyber espionage targeting Southeast Asian military organizations using AppleChris and MemFun malware since at least 2020
- **SocksEscort Operators**: Criminal proxy service operators who enslaved residential routers worldwide into a botnet spanning 163 countries before law enforcement disruption
- **Banking Trojan Operators**: Brazil-focused campaign combining traditional malware with real-time human operators targeting Pix payment system users
- **Cryptocurrency Thieves**: Supply chain attackers who compromised AppsFlyer SDK to steal digital currencies from unsuspecting users