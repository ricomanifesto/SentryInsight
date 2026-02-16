# Exploitation Report

The current threat landscape shows intense exploitation activity across multiple critical vulnerabilities, with particular focus on enterprise infrastructure and supply chain attacks. Threat actors are actively exploiting critical vulnerabilities in Ivanti Endpoint Manager Mobile, Microsoft Configuration Manager, and BeyondTrust remote access products. Meanwhile, sophisticated social engineering campaigns utilizing ClickFix techniques are evolving to abuse DNS queries and legitimate platforms like Google Groups and Claude AI artifacts to deliver malware. Nation-state actors from China, Iran, Russia, and North Korea are coordinating extensive campaigns against defense industrial base organizations, burning dozens of zero-day vulnerabilities in edge devices to infiltrate contractor networks.

## Active Exploitation Details

### Ivanti Endpoint Manager Mobile Critical RCE Vulnerabilities
- **Description**: Two critical remote code execution vulnerabilities in Ivanti EPMM are being actively exploited in widespread attacks
- **Impact**: Attackers can achieve remote code execution on vulnerable Ivanti EPMM systems, potentially leading to complete system compromise
- **Status**: Active exploitation observed with one threat actor responsible for 83% of recent attacks

### Microsoft Configuration Manager Critical Vulnerability
- **Description**: Critical vulnerability in Microsoft SCCM (System Center Configuration Manager) that allows remote code execution
- **Impact**: Complete compromise of configuration management infrastructure, potential for lateral movement across enterprise networks
- **Status**: CISA has flagged this vulnerability as actively exploited and ordered federal agencies to secure their systems
- **CVE ID**: Patched in October 2024

### BeyondTrust Remote Support Critical Vulnerability
- **Description**: Critical security flaw in BeyondTrust Remote Support (RS) and Privileged Remote Access (PRA) products
- **Impact**: Remote code execution and potential complete system compromise of privileged access management systems
- **Status**: In-the-wild exploitation observed by security researchers with CVSS score of 9.9

### Defense Industrial Base Zero-Day Exploitation
- **Description**: Multiple zero-day vulnerabilities in edge devices being exploited by nation-state actors
- **Impact**: Network infiltration of defense contractors and sensitive military-related organizations
- **Status**: At least two dozen zero-days burned in coordinated campaigns targeting the defense sector

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile**: Enterprise mobile device management platforms vulnerable to RCE attacks
- **Microsoft Configuration Manager (SCCM)**: Enterprise system configuration and deployment infrastructure
- **BeyondTrust Remote Support/PRA**: Privileged remote access and support management systems
- **Google Chrome Extensions**: Malicious extensions targeting Meta Business Suite and Facebook Business Manager
- **Edge Network Devices**: Various edge infrastructure devices targeted with zero-day exploits
- **Windows Commercial Systems**: Boot failure issues following security updates affecting Windows 11 systems
- **Cryptocurrency Hardware Wallets**: Trezor and Ledger users targeted through physical mail phishing campaigns

## Attack Vectors and Techniques

- **ClickFix DNS-Based Attacks**: New technique abusing nslookup commands to retrieve PowerShell payloads via DNS queries
- **Google Groups Abuse**: Over 4,000 malicious Google Groups and 3,500+ Google-hosted URLs distributing Lumma Stealer malware
- **Claude AI Artifacts Exploitation**: Threat actors abusing Claude LLM artifacts and Google Ads to deliver macOS infostealers
- **Pastebin Comment Manipulation**: Cryptocurrency-focused ClickFix attacks distributed through Pastebin comments to hijack crypto transactions
- **Physical Mail Social Engineering**: Traditional mail campaigns targeting cryptocurrency wallet users with fake security warnings
- **Fake Recruitment Campaigns**: North Korean actors using coding challenges with cryptocurrency-related tasks to target developers
- **Supply Chain Attacks**: Malicious Chrome extensions stealing business data and browsing history
- **BYOVD (Bring Your Own Vulnerable Driver)**: Attackers exploiting Windows driver vulnerabilities to terminate security processes

## Threat Actor Activities

- **ShinyHunters**: Data extortion group claimed theft of over 600,000 Canada Goose customer records containing personal and payment data
- **UAT-9921**: Previously unknown threat actor deploying VoidLink malware framework targeting technology and financial sectors
- **Russian State Actor**: Google attributed CANFAIL malware attacks against Ukrainian organizations to suspected Russian threat actor
- **North Korean Groups**: Conducting fake recruiter campaigns targeting JavaScript and Python developers with malware-laden coding challenges
- **Multi-National Coordination**: China, Iran, Russia, and North Korea coordinating extensive cyber operations against defense industrial base sector
- **Lumma Stealer Operators**: Large-scale campaign distributing infostealer malware through Google Groups and trojanized browser applications
- **Cryptocurrency Threat Actors**: Multiple groups targeting crypto users through physical mail, browser hijacking, and wallet-focused social engineering