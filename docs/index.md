# Exploitation Report

Current exploitation activity demonstrates a concerning trend of supply chain attacks, zero-day vulnerabilities being actively exploited, and sophisticated campaigns targeting enterprise infrastructure. Google has patched two critical Chrome zero-day vulnerabilities affecting the Skia graphics library and V8 JavaScript engine that were actively exploited in the wild. Multiple supply chain attacks have emerged, including the hijacking of AppsFlyer Web SDK for cryptocurrency theft and the GlassWorm campaign targeting developers through malicious VSX extensions. Additionally, Linux AppArmor has been found to contain nine critical vulnerabilities enabling privilege escalation, while Veeam Backup & Replication software was discovered to have seven critical remote code execution flaws.

## Active Exploitation Details

### Chrome Zero-Day Vulnerabilities
- **Description**: Two high-severity vulnerabilities in Google Chrome affecting the Skia graphics library and V8 JavaScript engine
- **Impact**: Successful exploitation could allow attackers to execute arbitrary code in the context of the Chrome browser
- **Status**: Actively exploited in the wild; Google has released emergency security updates to patch these vulnerabilities

### AppsFlyer Web SDK Supply Chain Attack
- **Description**: The AppsFlyer Web SDK was temporarily compromised with malicious JavaScript code designed to steal cryptocurrency
- **Impact**: Users of applications integrating the compromised SDK were exposed to cryptocurrency theft
- **Status**: Supply chain attack was detected and remediated; affected SDK versions have been cleaned

### Linux AppArmor Vulnerabilities (CrackArmor)
- **Description**: Nine security vulnerabilities within the Linux kernel's AppArmor module that allow unprivileged users to bypass kernel protections
- **Impact**: Attackers can achieve root privilege escalation and bypass container isolation mechanisms
- **Status**: Vulnerabilities disclosed; patches should be applied immediately

### Veeam Backup & Replication Critical Flaws
- **Description**: Seven critical vulnerabilities in Veeam's Backup & Replication software
- **Impact**: Remote code execution capabilities for attackers who successfully exploit these flaws
- **Status**: Security updates have been released by Veeam to address all critical vulnerabilities

## Affected Systems and Products

- **Google Chrome**: All versions prior to the latest security update containing fixes for Skia and V8 vulnerabilities
- **AppsFlyer Web SDK**: Temporary compromise affecting applications using the malicious SDK version
- **Linux Systems**: All distributions running AppArmor module with CrackArmor vulnerabilities
- **Veeam Backup & Replication**: Multiple versions affected by seven critical remote code execution flaws
- **Windows 11 Enterprise**: RRAS (Routing and Remote Access Service) vulnerability requiring out-of-band hotpatch
- **Samsung Windows 11 PCs**: Specific models experiencing C: drive access issues after February 2026 security updates
- **Steam Gaming Platform**: Eight malicious games identified containing malware
- **Open VSX Registry**: 72 malicious extensions deployed as part of GlassWorm campaign

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Compromise of legitimate software distribution channels including SDK hijacking and malicious browser extensions
- **Zero-Day Exploitation**: Active exploitation of unpatched Chrome vulnerabilities before public disclosure
- **SEO Poisoning**: Distribution of fake VPN clients through manipulated search engine results
- **Privilege Escalation**: Exploitation of Linux AppArmor flaws to gain root access from unprivileged accounts
- **Container Escape**: Use of CrackArmor vulnerabilities to bypass container isolation mechanisms
- **Credential Theft**: Deployment of fake enterprise VPN clients to harvest corporate login credentials
- **Click-Fix Campaigns**: New variants of social engineering attacks to trick users into executing malicious code
- **Malware Distribution**: Use of gaming platforms and legitimate software repositories to spread malicious code

## Threat Actor Activities

- **Storm-2561**: Microsoft-tracked threat group distributing fake VPN clients from major vendors (Ivanti, Cisco, Fortinet) through SEO poisoning to steal enterprise credentials
- **Chinese APT Groups**: Suspected China-based cyber espionage targeting Southeast Asian military organizations with AppleChris and MemFun malware since at least 2020
- **GlassWorm Campaign Operators**: Threat actors behind an escalated supply chain attack targeting developers through 72 malicious Open VSX extensions
- **SocksEscort Botnet**: Criminal proxy service operators who enslaved 369,000 IP addresses across 163 countries for illegal activities before law enforcement disruption
- **Banking Trojan Operators**: Cybercriminals targeting Brazil's Pix payment users with real-time banking malware combining automated tools with human operators
- **Steam Malware Distributors**: Threat actors who uploaded eight malicious games to Steam platform, prompting FBI investigation and victim identification efforts