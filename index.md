# Exploitation Report

Critical exploitation activity is currently dominated by vulnerabilities in enterprise infrastructure systems, with threat actors heavily targeting Ivanti Endpoint Manager Mobile, BeyondTrust Remote Access products, and Microsoft Configuration Manager. A single threat actor is responsible for 83% of recent Ivanti attacks, while BeyondTrust vulnerabilities rated at CVSS 9.9 are now being exploited in the wild following proof-of-concept publication. Simultaneously, sophisticated social engineering campaigns are proliferating through ClickFix attacks that abuse legitimate platforms like Pastebin, Google Groups, and Claude artifacts to deliver cryptocurrency theft malware and infostealers. Nation-state actors from China, Iran, Russia, and North Korea are coordinating extensive campaigns against defense industrial base organizations, burning dozens of zero-day vulnerabilities in edge devices to infiltrate contractor networks.

## Active Exploitation Details

### Ivanti Endpoint Manager Mobile Remote Code Execution Vulnerabilities
- **Description**: Two critical vulnerabilities in Ivanti EPMM allowing remote code execution without authentication
- **Impact**: Complete system compromise and lateral movement within enterprise networks
- **Status**: Actively exploited with a single threat actor responsible for 83% of observed attacks

### BeyondTrust Remote Support and Privileged Remote Access Vulnerability
- **Description**: Critical pre-authentication remote code execution flaw with CVSS 9.9 rating
- **Impact**: Complete compromise of privileged access management systems
- **Status**: Now being exploited in the wild following public proof-of-concept release

### Microsoft Configuration Manager Vulnerability
- **Description**: Critical remote code execution flaw in Microsoft SCCM
- **Impact**: Enterprise-wide system compromise and administrative control
- **Status**: Exploited in attacks, CISA has ordered federal agencies to patch immediately

### Defense Industrial Base Zero-Day Vulnerabilities
- **Description**: Multiple zero-day vulnerabilities in edge devices targeting defense contractors
- **Impact**: Network infiltration and espionage operations
- **Status**: At least two dozen zero-days burned by nation-state actors in active campaigns

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Enterprise mobile device management systems vulnerable to RCE attacks
- **BeyondTrust Remote Support and Privileged Remote Access**: Critical infrastructure for remote access management
- **Microsoft Configuration Manager (SCCM)**: Enterprise system management and deployment platforms
- **Edge Network Devices**: Various edge computing and networking equipment in defense sector
- **Google Chrome Extensions**: Malicious extensions targeting Meta Business Suite and Facebook Business Manager
- **Cryptocurrency Platforms**: Hardware wallets (Trezor, Ledger) and swap interfaces targeted through social engineering

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: Malicious JavaScript execution disguised as system fixes, distributed through Pastebin comments and Claude artifacts
- **DNS-Based ClickFix**: Nslookup command exploitation for malware staging and delivery
- **Google Groups Abuse**: Over 4,000 malicious Google Groups and 3,500 Google-hosted URLs spreading Lumma Stealer malware
- **Physical Mail Campaigns**: Traditional letters impersonating hardware wallet manufacturers to steal recovery phrases
- **Fake Recruitment Operations**: North Korean threat actors using cryptocurrency-related coding challenges to target JavaScript and Python developers
- **Bring Your Own Vulnerable Driver (BYOVD)**: Weaponization of Windows drivers to terminate security processes
- **Chrome Extension Hijacking**: Malicious browser extensions stealing business data and browsing history

## Threat Actor Activities

- **Single Ivanti Threat Actor**: Dominating exploitation landscape with 83% of recent EPMM attacks
- **UAT-9921**: Previously unknown threat actor deploying VoidLink malware framework against technology and financial sectors
- **Russian Actor with CANFAIL**: Google-attributed threat group targeting Ukrainian organizations with CANFAIL malware
- **North Korean Groups**: Conducting fake recruitment campaigns targeting software developers with cryptocurrency-themed attacks
- **Multi-Nation State Coalition**: China, Iran, Russia, and North Korea coordinating attacks against defense industrial base
- **Cryptocurrency Threat Actors**: Sophisticated campaigns combining digital and physical attack vectors against crypto users
- **Chrome Extension Operators**: Deploying "CL S" and other malicious extensions to steal Meta Business Suite data