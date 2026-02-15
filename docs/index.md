# Exploitation Report

The current threat landscape is dominated by critical vulnerabilities under active exploitation across enterprise systems and infrastructure. Most concerning are the Ivanti Endpoint Manager Mobile (EPMM) remote code execution vulnerabilities, where a single threat actor is responsible for 83% of recent attacks. Additionally, Microsoft Configuration Manager systems are being actively exploited through a critical flaw, prompting CISA to mandate federal agency patching. BeyondTrust Remote Support and Privileged Remote Access products face active exploitation of a critical pre-authentication remote code execution vulnerability with a CVSS score of 9.9. Beyond traditional vulnerabilities, sophisticated social engineering campaigns are evolving, including DNS-based ClickFix attacks and the abuse of AI platforms like Claude artifacts to deliver malware.

## Active Exploitation Details

### Ivanti Endpoint Manager Mobile (EPMM) RCE Vulnerabilities
- **Description**: Two critical remote code execution vulnerabilities in Ivanti EPMM are being actively exploited
- **Impact**: Complete system compromise and unauthorized remote access to enterprise mobile management infrastructure
- **Status**: Under active exploitation with one threat actor responsible for 83% of attacks

### Microsoft Configuration Manager (SCCM) RCE Vulnerability
- **Description**: Critical remote code execution flaw in Microsoft System Center Configuration Manager
- **Impact**: Attackers can achieve remote code execution on enterprise configuration management systems
- **Status**: Patched in October 2024 but now exploited in the wild, flagged by CISA for federal agency remediation

### BeyondTrust Remote Support and Privileged Remote Access RCE
- **Description**: Critical pre-authentication remote code execution vulnerability with CVSS 9.9 score
- **Impact**: Complete system compromise without authentication requirements
- **Status**: Actively exploited following public proof-of-concept release

### Windows LNK Shortcut Spoofing Vulnerabilities
- **Description**: Multiple vulnerabilities in Windows LNK shortcut files allowing malicious payload deployment
- **Impact**: Attackers can deploy malicious payloads through spoofed shortcut files
- **Status**: Disclosed at Wild West Hackin' Fest, Microsoft does not consider these as vulnerabilities

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Enterprise mobile device management platforms experiencing widespread exploitation
- **Microsoft Configuration Manager**: Enterprise system configuration and management infrastructure
- **BeyondTrust Remote Support and Privileged Remote Access**: Remote access and privileged access management appliances
- **Google Chrome Extensions**: Browser extensions targeting Meta Business Suite and Facebook Business Manager data
- **Windows LNK Files**: Windows shortcut files vulnerable to spoofing attacks
- **Cryptocurrency Hardware Wallets**: Trezor and Ledger users targeted through physical mail campaigns

## Attack Vectors and Techniques

- **DNS-Based ClickFix Attacks**: Microsoft disclosed new variant using nslookup commands for malware staging through DNS queries
- **Claude AI Artifact Abuse**: Threat actors exploiting Claude LLM artifacts combined with Google Ads to deliver macOS infostealers
- **Physical Mail Campaigns**: Traditional mail targeting cryptocurrency wallet users to steal recovery phrases
- **Fake Recruitment Campaigns**: North Korean threat actors embedding malware in coding challenges for JavaScript and Python developers
- **Malicious Browser Extensions**: Chrome extensions stealing business data, emails, and browsing history from Meta platforms
- **BYOVD Attacks**: Bring Your Own Vulnerable Driver attacks exploiting security gaps to weaponize Windows drivers
- **Social Engineering**: ClickFix tactics tricking users into running malicious commands

## Threat Actor Activities

- **Single Ivanti Threat Actor**: One actor responsible for 83% of recent Ivanti EPMM exploitation attempts
- **UAT-9921**: Previously unknown threat actor deploying VoidLink malware framework against technology and financial sectors
- **Suspected Russian Actor**: Google attributed CANFAIL malware attacks targeting Ukrainian organizations
- **North Korean Groups**: Conducting fake recruiter campaigns with cryptocurrency-themed coding challenges
- **Nation-State Coalitions**: China, Iran, Russia, and North Korea coordinating defense industrial base cyber operations with over two dozen zero-day exploits in edge devices
- **Qilin Ransomware Gang**: Successfully breached Romania's oil pipeline operator Conpet S.A. and confirmed data theft