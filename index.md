# Exploitation Report

Multiple critical vulnerabilities across enterprise software platforms are currently under active exploitation, posing significant risks to organizations worldwide. The most severe activity involves exploitation of Ivanti Endpoint Manager Mobile (EPMM) vulnerabilities, where a single threat actor is responsible for 83% of recent attacks, and BeyondTrust Remote Support products experiencing in-the-wild exploitation of a critical remote code execution flaw with a CVSS score of 9.9. Additionally, Microsoft Configuration Manager vulnerabilities are being actively exploited, prompting CISA to order federal agencies to implement immediate security measures. The threat landscape is further complicated by sophisticated ClickFix social engineering campaigns that now leverage DNS queries and various platforms to deliver malware payloads.

## Active Exploitation Details

### Ivanti Endpoint Manager Mobile (EPMM) Vulnerabilities
- **Description**: Critical remote code execution vulnerabilities in Ivanti EPMM affecting enterprise mobile device management systems
- **Impact**: Complete system compromise allowing attackers to gain unauthorized access to corporate mobile device infrastructure
- **Status**: Under active exploitation with a single threat actor responsible for 83% of recent attacks

### BeyondTrust Remote Support RCE Vulnerability
- **Description**: Critical pre-authentication remote code execution vulnerability in BeyondTrust Remote Support (RS) and Privileged Remote Access (PRA) products
- **Impact**: Complete system compromise without authentication requirements, allowing attackers to execute arbitrary code
- **Status**: Now being exploited in the wild after proof-of-concept publication

### Microsoft Configuration Manager Vulnerability
- **Description**: Critical Microsoft System Center Configuration Manager (SCCM) vulnerability allowing remote code execution
- **Impact**: Complete compromise of enterprise system management infrastructure
- **Status**: Actively exploited in attacks, patched in October 2024, CISA KEV listing issued

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Enterprise mobile device management platforms
- **BeyondTrust Remote Support**: Remote access and privileged access management appliances
- **Microsoft Configuration Manager**: Enterprise system management and deployment infrastructure
- **Google Chrome**: Browser extensions targeting Meta Business Suite and Facebook Business Manager data
- **macOS Systems**: Targeted by infostealer malware through Claude LLM artifacts and ClickFix campaigns
- **Windows Systems**: Affected by Family Safety bugs blocking browser launches and boot failure issues

## Attack Vectors and Techniques

- **DNS-Based ClickFix Attacks**: Malicious actors abuse nslookup commands to retrieve PowerShell payloads through DNS queries
- **Social Engineering via Pastebin**: Attackers use Pastebin comments to distribute ClickFix-style attacks targeting cryptocurrency users
- **Google Groups Abuse**: Over 4,000 malicious Google Groups and 3,500 Google-hosted URLs spreading Lumma Stealer malware
- **Malicious Chrome Extensions**: Extensions designed to steal Meta Business Suite and Facebook Business Manager data
- **Physical Mail Campaigns**: Traditional mail targeting Trezor and Ledger cryptocurrency wallet users
- **Fake Recruitment Campaigns**: North Korean actors targeting developers with malicious coding challenges
- **Supply Chain Attacks**: Exploitation of npm ecosystem vulnerabilities and package management weaknesses

## Threat Actor Activities

- **Single Ivanti Attacker**: One threat actor responsible for 83% of recent Ivanti EPMM exploitation attempts
- **UAT-9921**: Previously unknown threat actor deploying VoidLink malware framework against technology and financial sectors
- **Russian State Actor**: Google attributes CANFAIL malware attacks against Ukrainian organizations to suspected Russian threat group
- **North Korean Groups**: Conducting fake recruiter campaigns targeting JavaScript and Python developers with cryptocurrency-related malicious tasks
- **Multi-Nation Coordination**: Google reports coordinated operations by China, Iran, Russia, and North Korea targeting defense industrial base sector
- **Defense Sector Targeting**: Nation-state hackers utilizing at least two dozen zero-day exploits in edge devices to infiltrate defense contractors