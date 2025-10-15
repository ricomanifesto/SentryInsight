# Exploitation Report

Microsoft's October 2025 Patch Tuesday represents a critical security milestone, addressing 172 vulnerabilities including six zero-day exploits that are currently being actively exploited in the wild. This massive security update coincides with Windows 10 reaching end-of-support, leaving unpatched systems exposed to ongoing attacks. Simultaneously, threat actors continue to leverage novel attack vectors including the Pixnapping side-channel attack on Android devices, malicious VSCode extensions targeting developers' cryptocurrency wallets, and sophisticated supply chain attacks through compromised package repositories. State-sponsored groups, particularly Chinese APT actors, have demonstrated advanced persistence techniques by weaponizing legitimate infrastructure tools like ArcGIS servers for long-term access.

## Active Exploitation Details

### Microsoft Windows Zero-Day Vulnerabilities
- **Description**: Six zero-day vulnerabilities in Microsoft Windows systems are being actively exploited by threat actors
- **Impact**: Attackers can achieve various levels of system compromise, privilege escalation, and unauthorized access
- **Status**: Patches released in October 2025 Patch Tuesday update addressing all six zero-days

### Oracle E-Business Suite Vulnerability
- **Description**: Critical vulnerability in Oracle E-Business Suite that was actively exploited to breach servers
- **Impact**: Server compromise and unauthorized access to sensitive business data
- **Status**: Oracle has silently patched the vulnerability after public exploit disclosure
- **CVE ID**: CVE-2025-61884

### RMPocalypse AMD SEV-SNP Vulnerability
- **Description**: Security flaw that can be exploited through a single 8-byte write to undermine confidential computing guarantees
- **Impact**: Complete breakdown of AMD's Secure Encrypted Virtualization with Secure Nested Paging (SEV-SNP) protections
- **Status**: AMD has released fixes to address the vulnerability

### Pixnapping Android Side-Channel Attack
- **Description**: Novel side-channel attack targeting Android devices that steals sensitive data pixel-by-pixel without requiring permissions
- **Impact**: Theft of two-factor authentication codes, Google Maps timelines, and other sensitive information from apps including Gmail, Google Accounts, Google Authenticator, Signal, and Venmo
- **Status**: Affects Google and Samsung Android devices, proof-of-concept exploit available

### Framework Laptop Secure Boot Bypass
- **Description**: Vulnerability in signed UEFI shell components on Framework laptops running Linux
- **Impact**: Bypass of Secure Boot protections, potentially allowing malicious code execution during boot process
- **Status**: Affects approximately 200,000 Linux Framework systems

## Affected Systems and Products

- **Microsoft Windows**: All Windows operating systems affected by 172 vulnerabilities including six actively exploited zero-days
- **Microsoft Windows 10**: End-of-support reached, no longer receiving security patches for new vulnerabilities
- **Microsoft Windows 11**: Security updates available through KB5066835 and KB5066793 cumulative updates
- **Microsoft Exchange Server**: Exchange 2016 and 2019 have reached end-of-support status
- **Oracle E-Business Suite**: Systems compromised through actively exploited vulnerability
- **AMD Processors**: SEV-SNP confidential computing features affected by RMPocalypse vulnerability
- **Android Devices**: Google and Samsung devices vulnerable to Pixnapping attack
- **Framework Laptops**: Nearly 200,000 Linux-based systems with Secure Boot bypass risk
- **ArcGIS Server**: Geospatial mapping software compromised and weaponized as backdoor
- **VSCode Extensions**: Malicious extensions on Microsoft VSCode marketplace and OpenVSX registry
- **Package Repositories**: npm, PyPI, and RubyGems ecosystems hosting malicious packages

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in Microsoft Windows systems
- **Supply Chain Attacks**: Malicious packages distributed through legitimate software repositories targeting developers
- **Side-Channel Attacks**: Pixnapping technique extracting sensitive data through pixel analysis without permissions
- **Web Shell Deployment**: Conversion of legitimate ArcGIS server components into persistent backdoors
- **Social Engineering**: Phishing campaigns delivering MonsterV2 malware and other threats
- **Cryptocurrency Theft**: Targeted attacks on developer environments to steal cryptocurrency wallets
- **Command and Control**: Use of Discord channels for data exfiltration and remote control
- **Privilege Escalation**: Exploitation of high-severity bugs for elevated system access

## Threat Actor Activities

- **Chinese APT Groups (Flax Typhoon)**: Compromised ArcGIS servers for over a year, maintaining persistent access through modified geospatial mapping software
- **TigerJack**: Continuously targeting developers through malicious VSCode extensions designed to steal cryptocurrency
- **TA585**: Delivering MonsterV2 malware through sophisticated phishing campaigns
- **ShinyHunters**: Publicly leaked proof-of-concept exploit for Oracle E-Business Suite vulnerability
- **RondoDox Botnet Operators**: Weaponizing over 50 vulnerabilities across 30+ vendors in expanded targeting campaigns
- **Prince Group**: Criminal organization conducting "pig butchering" cryptocurrency fraud schemes resulting in $15 billion in seized assets
- **State-Sponsored Actors**: Targeting critical infrastructure through unmonitored "back-office clutter" data exploitation