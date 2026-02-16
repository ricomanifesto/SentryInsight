# Exploitation Report

Current threat landscape shows significant exploitation activity across multiple attack vectors, with a critical Chrome zero-day vulnerability **CVE-2026-2441** being actively exploited in the wild. The Chrome vulnerability represents a high-severity security flaw that has prompted emergency updates from Google. Additionally, threat actors are targeting Ivanti Endpoint Manager Mobile systems with two critical remote code execution vulnerabilities, with one actor responsible for 83% of observed attacks. A critical Microsoft Configuration Manager vulnerability has been flagged by CISA as actively exploited, while a BeyondTrust vulnerability with a CVSS score of 9.9 is also seeing active exploitation. The threat landscape is further complicated by sophisticated social engineering campaigns using ClickFix attacks that abuse DNS queries and various platforms to deliver malware payloads.

## Active Exploitation Details

### Chrome Zero-Day Vulnerability
- **Description**: A high-severity vulnerability in Google Chrome browser that has been exploited in zero-day attacks
- **Impact**: Allows attackers to compromise Chrome browsers and potentially execute malicious code
- **Status**: Emergency patches have been released by Google to address the active exploitation
- **CVE ID**: CVE-2026-2441

### Ivanti EPMM Remote Code Execution Vulnerabilities
- **Description**: Two critical vulnerabilities in Ivanti Endpoint Manager Mobile (EPMM) allowing remote code execution
- **Impact**: Attackers can achieve remote code execution on affected Ivanti EPMM systems
- **Status**: Under active exploitation with one threat actor responsible for 83% of observed attacks
- **CVE ID**: Not specified in the articles

### Microsoft Configuration Manager Critical Flaw
- **Description**: A critical vulnerability in Microsoft System Center Configuration Manager (SCCM)
- **Impact**: Enables attackers to compromise Configuration Manager systems
- **Status**: CISA has flagged this vulnerability as exploited in attacks; patch was released in October 2024
- **CVE ID**: Not specified in the articles

### BeyondTrust Critical Vulnerability
- **Description**: A critical security flaw affecting BeyondTrust Remote Support (RS) and Privileged Remote Access (PRA) products
- **Impact**: High-impact vulnerability with CVSS score of 9.9 allowing significant system compromise
- **Status**: Recently disclosed and now being exploited in the wild according to watchTowr research
- **CVE ID**: Not specified in the articles

## Affected Systems and Products

- **Google Chrome**: All versions prior to the emergency security update containing the patch for CVE-2026-2441
- **Ivanti Endpoint Manager Mobile (EPMM)**: Systems vulnerable to two critical RCE flaws under active exploitation
- **Microsoft System Center Configuration Manager (SCCM)**: Systems not updated since the October 2024 security patch
- **BeyondTrust Remote Support and Privileged Remote Access**: Products affected by the CVSS 9.9 vulnerability
- **Windows 11 Commercial Systems**: Experiencing boot failures related to recent security updates

## Attack Vectors and Techniques

- **Browser-Based Exploitation**: Chrome zero-day being leveraged for browser compromise and potential code execution
- **ClickFix Social Engineering**: Advanced social engineering attacks using DNS queries via nslookup to retrieve PowerShell payloads
- **DNS-Based Malware Delivery**: First known use of DNS as a channel in ClickFix campaigns to deliver malicious payloads
- **Pastebin Comment Abuse**: Attackers using Pastebin comments to distribute ClickFix-style attacks targeting cryptocurrency users
- **Claude AI Artifacts Abuse**: Threat actors leveraging Claude LLM artifacts and Google Ads in ClickFix campaigns targeting macOS users
- **Google Groups Platform Abuse**: Over 4,000 malicious Google Groups and 3,500+ Google-hosted URLs used to distribute Lumma Stealer malware
- **Malicious Chrome Extensions**: Extensions designed to steal Meta Business Suite and Facebook Business Manager data
- **Physical Social Engineering**: Physical letters impersonating Trezor and Ledger to steal cryptocurrency wallet recovery phrases
- **Fake Recruitment Campaigns**: North Korean threat actors targeting developers with malicious coding challenges

## Threat Actor Activities

- **Dominant Ivanti Attacker**: Single threat actor responsible for 83% of recent Ivanti EPMM RCE exploitation attempts
- **ShinyHunters Group**: Data extortion group claiming theft of over 600,000 Canada Goose customer records containing personal and payment data
- **UAT-9921**: Previously unknown threat actor deploying VoidLink malware framework targeting technology and financial services sectors
- **Russian-Attributed Actor**: Google has tied a suspected Russian actor to CANFAIL malware attacks specifically targeting Ukrainian organizations
- **Nation-State Consortium**: Multiple state-sponsored actors from China, Iran, Russia, and North Korea coordinating attacks against defense industrial base sector
- **North Korean Developers Campaign**: Continued fake recruiter operations targeting JavaScript and Python developers with cryptocurrency-related malicious tasks
- **Multi-Platform ClickFix Operators**: Threat actors expanding ClickFix attacks across DNS, Pastebin, Claude AI, and other platforms for broader malware distribution