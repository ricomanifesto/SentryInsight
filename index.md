# Exploitation Report

The current threat landscape reveals intensified exploitation activity targeting critical enterprise infrastructure and supply chains. A single threat actor is responsible for 83% of recent attacks exploiting critical Ivanti Endpoint Manager Mobile vulnerabilities, while nation-state actors from China, Russia, Iran, and North Korea are coordinating sophisticated campaigns against defense contractors using dozens of zero-day exploits. Critical remote code execution flaws in Microsoft Configuration Manager and BeyondTrust products are being actively exploited following public proof-of-concept releases, highlighting the urgent need for organizations to prioritize patching and implement defense-in-depth strategies.

## Active Exploitation Details

### Ivanti Endpoint Manager Mobile (EPMM) Vulnerabilities
- **Description**: Two critical remote code execution vulnerabilities in Ivanti EPMM are being actively exploited
- **Impact**: Attackers can achieve remote code execution on vulnerable systems
- **Status**: Under active exploitation with one threat actor responsible for 83% of attacks

### Microsoft Configuration Manager (SCCM) Vulnerability
- **Description**: Critical remote code execution flaw in Microsoft Configuration Manager
- **Impact**: Remote code execution capabilities for attackers
- **Status**: CISA has flagged this as exploited in attacks, patched in October 2024

### BeyondTrust Remote Support and Privileged Remote Access Vulnerability
- **Description**: Critical pre-authentication remote code execution vulnerability with CVSS 9.9 rating
- **Impact**: Pre-authentication remote code execution allowing full system compromise
- **Status**: Now being exploited in the wild following public proof-of-concept release

### Windows LNK Spoofing Vulnerabilities
- **Description**: Multiple vulnerabilities in Windows LNK shortcut files allowing payload deployment
- **Impact**: Attackers can deploy malicious payloads through spoofed shortcut files
- **Status**: Recently disclosed at Wild West Hackin' Fest, Microsoft disputes classification as vulnerabilities

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile**: Enterprise mobile device management platform
- **Microsoft Configuration Manager**: Enterprise system management platform
- **BeyondTrust Remote Support/PRA**: Remote access and privileged access management solutions
- **Windows LNK Files**: Windows shortcut file system components
- **Google Chrome Extensions**: Browser extension ecosystem targeting business data
- **Meta Business Suite/Facebook Business Manager**: Social media business management platforms
- **Cryptocurrency Hardware Wallets**: Trezor and Ledger devices targeted through social engineering

## Attack Vectors and Techniques

- **Remote Code Execution**: Exploitation of unpatched RCE vulnerabilities in enterprise software
- **Supply Chain Attacks**: Malicious npm packages and Chrome extensions targeting developers
- **Social Engineering**: Physical mail campaigns targeting cryptocurrency wallet users
- **Bring Your Own Vulnerable Driver (BYOVD)**: Weaponizing Windows drivers to terminate security processes
- **ClickFix Campaigns**: Abusing Claude LLM artifacts and Google Ads to deliver macOS infostealers
- **Fake Recruitment**: North Korean actors using cryptocurrency-related coding challenges as malware vectors

## Threat Actor Activities

- **Single Ivanti Attacker**: One threat actor responsible for 83% of Ivanti EPMM exploitation
- **Nation-State Coordination**: China, Russia, Iran, and North Korea coordinating defense sector attacks with 24+ zero-days
- **UAT-9921**: Previously unknown actor deploying VoidLink malware framework against technology and financial sectors
- **North Korean Groups**: Targeting JavaScript and Python developers through fake recruitment campaigns
- **Russian Actor**: Suspected of CANFAIL malware attacks targeting Ukrainian organizations
- **Qilin Ransomware**: Confirmed data theft from Romania's national oil pipeline operator Conpet
- **Cryptocurrency Scammers**: Physical mail campaigns targeting Trezor and Ledger users for wallet phrase theft