# Exploitation Report

Critical zero-day vulnerabilities are currently being exploited across multiple platforms and products, with particularly concerning activity targeting Chrome browsers, Ivanti enterprise systems, and BeyondTrust remote access solutions. A Chrome zero-day vulnerability (CVE-2026-2441) is under active attack, prompting emergency patches from Google. Meanwhile, threat actors are heavily exploiting critical vulnerabilities in Ivanti Endpoint Manager Mobile, with one actor responsible for 83% of recent attacks. Additionally, a critical BeyondTrust vulnerability with a CVSS score of 9.9 is being exploited in the wild, and Microsoft Configuration Manager vulnerabilities are being actively targeted, prompting CISA to mandate federal agency remediation.

## Active Exploitation Details

### Chrome Zero-Day Vulnerability
- **Description**: A high-severity vulnerability in Google Chrome browser that allows attackers to exploit systems through the browser
- **Impact**: Enables attackers to compromise systems through web-based attacks and execute unauthorized code
- **Status**: Google has released emergency security updates to address the actively exploited vulnerability
- **CVE ID**: CVE-2026-2441

### Ivanti Endpoint Manager Mobile Critical Vulnerabilities
- **Description**: Critical remote code execution vulnerabilities affecting Ivanti EPMM systems
- **Impact**: Attackers can achieve remote code execution and gain unauthorized access to enterprise mobile management systems
- **Status**: Under active exploitation with one threat actor responsible for 83% of recent attacks

### BeyondTrust Remote Access Critical Vulnerability
- **Description**: Critical security flaw affecting BeyondTrust Remote Support (RS) and Privileged Remote Access (PRA) products
- **Impact**: Enables threat actors to compromise privileged remote access systems and potentially gain administrative control
- **Status**: Active in-the-wild exploitation observed with CVSS score of 9.9

### Microsoft Configuration Manager Vulnerability
- **Description**: Critical vulnerability in Microsoft System Center Configuration Manager (SCCM)
- **Impact**: Allows attackers to compromise enterprise system management infrastructure
- **Status**: CISA has flagged as exploited in attacks and ordered federal agencies to secure systems

## Affected Systems and Products

- **Google Chrome**: All versions prior to the latest security update containing the CVE-2026-2441 patch
- **Ivanti Endpoint Manager Mobile**: EPMM systems vulnerable to remote code execution attacks
- **BeyondTrust Remote Support and Privileged Remote Access**: RS and PRA products affected by critical vulnerability
- **Microsoft Configuration Manager**: SCCM systems requiring October 2024 patches
- **Mobile Platforms**: Android and iOS devices targeted by ZeroDayRAT spyware platform
- **Cryptocurrency Platforms**: Hardware wallets from Trezor and Ledger users targeted through social engineering

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: Advanced campaigns using DNS queries via nslookup to retrieve PowerShell payloads, marking the first known use of DNS as a channel in these attacks
- **Browser-Based Exploitation**: Zero-day Chrome vulnerability being exploited through web-based attack vectors
- **Mobile Spyware Distribution**: ZeroDayRAT platform advertised on Telegram for real-time surveillance and data theft
- **Supply Chain Attacks**: Malicious Chrome extensions stealing business data, emails, and browsing history from Meta Business Suite users
- **Physical Social Engineering**: Physical mail campaigns targeting cryptocurrency hardware wallet users with fake security notices
- **Fake Recruitment Campaigns**: North Korean threat actors targeting JavaScript and Python developers with cryptocurrency-related coding challenges containing malware

## Threat Actor Activities

- **Dominant Ivanti Attacker**: Single threat actor responsible for 83% of recent Ivanti EPMM remote code execution attacks
- **UAT-9921**: Previously unknown threat actor deploying VoidLink malware framework targeting technology and financial services sectors
- **ShinyHunters**: Data extortion group claiming theft of over 600,000 Canada Goose customer records containing personal and payment data
- **North Korean Groups**: Conducting sophisticated fake recruiter campaigns targeting developers with malware-laden coding challenges
- **State-Sponsored Actors**: Multiple nation-state groups from China, Iran, Russia, and North Korea coordinating attacks against defense industrial base sector, burning at least two dozen zero-day vulnerabilities in edge devices
- **Russian-Attributed Actor**: Google has linked suspected Russian threat actor to CANFAIL malware attacks targeting Ukrainian organizations
- **ClickFix Operators**: Various groups evolving ClickFix attacks to abuse DNS queries, Pastebin comments, Claude LLM artifacts, and Google Ads for malware distribution