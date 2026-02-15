# Exploitation Report

Critical vulnerabilities in enterprise infrastructure are being actively exploited in targeted attacks. Multiple threat actors are focusing on Ivanti Endpoint Manager Mobile systems, with a single threat actor responsible for 83% of recent remote code execution attacks. Additionally, attackers are leveraging sophisticated social engineering tactics including ClickFix attacks distributed through various platforms, DNS-based staging methods, and malware campaigns targeting both enterprise systems and cryptocurrency users. Nation-state actors have intensified their focus on defense contractors, exploiting numerous zero-day vulnerabilities in edge devices to establish persistent access to critical infrastructure networks.

## Active Exploitation Details

### Ivanti Endpoint Manager Mobile (EPMM) Vulnerabilities
- **Description**: Two critical remote code execution vulnerabilities in Ivanti EPMM are being actively exploited by threat actors
- **Impact**: Attackers can gain unauthorized remote access and execute arbitrary code on vulnerable systems
- **Status**: Under active exploitation with one threat actor responsible for 83% of observed attacks

### Microsoft Configuration Manager (SCCM) Vulnerability
- **Description**: Critical remote code execution flaw in Microsoft System Center Configuration Manager (SCCM)
- **Impact**: Allows attackers to execute arbitrary code and gain elevated privileges on managed systems
- **Status**: CISA has flagged this vulnerability as actively exploited and ordered federal agencies to patch immediately

### BeyondTrust Remote Support Critical Vulnerability
- **Description**: Pre-authentication remote code execution vulnerability with CVSS score of 9.9 affecting BeyondTrust Remote Support (RS) and Privileged Remote Access (PRA) products
- **Impact**: Allows attackers to execute arbitrary code without authentication on affected appliances
- **Status**: Actively exploited in the wild after proof-of-concept code publication

### Defense Sector Zero-Day Vulnerabilities
- **Description**: At least two dozen zero-day vulnerabilities in edge devices specifically targeting defense contractors
- **Impact**: Enable nation-state espionage groups to establish persistent access to sensitive defense networks
- **Status**: Actively burned by Chinese, Russian, and other nation-state actors in coordinated campaigns

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile**: EPMM systems with unpatched critical vulnerabilities
- **Microsoft Configuration Manager**: SCCM installations requiring immediate patching per CISA directive
- **BeyondTrust Products**: Remote Support (RS) and Privileged Remote Access (PRA) appliances
- **Defense Industrial Base**: Edge devices and network infrastructure at defense contractors
- **Chrome Extensions**: Malicious extensions targeting Meta Business Suite and Facebook Business Manager
- **Cryptocurrency Platforms**: Hardware wallets including Trezor and Ledger users
- **macOS Systems**: Targets of infostealer malware via ClickFix campaigns

## Attack Vectors and Techniques

- **DNS-Based ClickFix Attacks**: Attackers use nslookup commands to stage malware through Domain Name System queries
- **Social Engineering via Physical Mail**: Physical letters impersonating Trezor and Ledger to steal cryptocurrency recovery phrases
- **Malicious Chrome Extensions**: Data theft targeting business accounts and browsing history
- **Fake Recruitment Campaigns**: North Korean threat actors targeting developers with malicious coding challenges
- **Google Groups Abuse**: Over 4,000 malicious Google Groups distributing Lumma Stealer and trojanized browsers
- **Pastebin Comment Exploitation**: ClickFix attacks distributed through Pastebin comments to hijack cryptocurrency transactions
- **Claude LLM Artifact Abuse**: Leveraging AI platform artifacts combined with Google Ads for macOS infostealer distribution
- **BYOVD Attacks**: Bring Your Own Vulnerable Driver attacks exploiting Windows driver security gaps

## Threat Actor Activities

- **Single Ivanti Attacker**: One threat actor responsible for 83% of recent Ivanti EPMM exploitation attempts
- **UAT-9921**: Previously unknown threat actor deploying VoidLink malware framework against technology and financial sectors
- **Russian-Attributed Actor**: Google linked suspected Russian group to CANFAIL malware attacks on Ukrainian organizations
- **North Korean Groups**: Conducting sophisticated fake recruiter campaigns targeting JavaScript and Python developers
- **Nation-State Coalitions**: Coordinated campaigns by Chinese, Iranian, Russian, and North Korean actors against defense contractors
- **Cryptocurrency Threat Actors**: Multi-vector campaigns targeting crypto users through physical mail, browser attacks, and social engineering