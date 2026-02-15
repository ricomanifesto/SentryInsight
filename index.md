# Exploitation Report

Critical exploitation activity is currently targeting multiple enterprise platforms, with threat actors actively exploiting vulnerabilities in Ivanti Endpoint Manager Mobile (EPMM), Microsoft Configuration Manager (SCCM), and BeyondTrust remote access products. A single threat actor is responsible for 83% of recent Ivanti RCE attacks, while CISA has flagged active exploitation of a critical Microsoft SCCM vulnerability. Nation-state actors from China, Iran, Russia, and North Korea have coordinated efforts targeting the defense industrial base, utilizing over two dozen zero-day vulnerabilities in edge devices. Additionally, the BeyondTrust RCE vulnerability with a CVSS score of 9.9 is now being actively exploited following the publication of proof-of-concept code.

## Active Exploitation Details

### Ivanti Endpoint Manager Mobile (EPMM) RCE Vulnerabilities
- **Description**: Two critical remote code execution vulnerabilities in Ivanti EPMM are being actively exploited by threat actors
- **Impact**: Attackers can achieve remote code execution on vulnerable systems, potentially gaining full system control
- **Status**: Under active exploitation with a single threat actor responsible for 83% of attacks

### Microsoft Configuration Manager (SCCM) Critical Flaw
- **Description**: Critical vulnerability in Microsoft Configuration Manager that allows remote code execution
- **Impact**: Remote attackers can execute arbitrary code on vulnerable SCCM systems
- **Status**: CISA has flagged this vulnerability as exploited in attacks, ordering federal agencies to secure systems
- **CVE ID**: Patched in October 2024, now confirmed as actively exploited

### BeyondTrust Remote Support and Privileged Remote Access RCE
- **Description**: Critical pre-authentication remote code execution vulnerability in BeyondTrust Remote Support (RS) and Privileged Remote Access (PRA) products
- **Impact**: Pre-authentication remote code execution allowing complete system compromise
- **Status**: Active exploitation confirmed following publication of proof-of-concept code
- **CVSS Score**: 9.9 (Critical)

### Defense Industrial Base Zero-Day Vulnerabilities
- **Description**: Over two dozen zero-day vulnerabilities in edge devices targeting defense contractors
- **Impact**: Nation-state espionage and network infiltration of defense sector organizations
- **Status**: Actively exploited by espionage groups from multiple countries

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Enterprise mobile device management platform experiencing widespread exploitation
- **Microsoft Configuration Manager (SCCM)**: System Center Configuration Manager installations, particularly in federal agencies
- **BeyondTrust Remote Support and Privileged Remote Access**: RS and PRA appliances vulnerable to pre-authentication attacks
- **Edge Devices**: Various edge computing and network infrastructure devices in defense contractor environments
- **Defense Industrial Base Infrastructure**: Networks and systems across defense contractors and related organizations

## Attack Vectors and Techniques

- **Remote Code Execution**: Primary attack vector targeting Ivanti EPMM, Microsoft SCCM, and BeyondTrust products
- **Pre-Authentication Exploitation**: BeyondTrust vulnerability allows attacks without authentication requirements
- **Zero-Day Edge Device Exploitation**: Nation-state actors targeting edge infrastructure to gain network footholds
- **Social Engineering via Physical Mail**: Cryptocurrency hardware wallet users targeted with physical letters mimicking legitimate vendors
- **Malicious Chrome Extensions**: Data theft campaigns targeting business users through browser extensions
- **ClickFix Campaigns**: Abuse of Claude LLM artifacts and Google Ads to deliver macOS infostealer malware
- **Fake Recruitment Campaigns**: North Korean threat actors targeting developers with malicious coding challenges
- **BYOVD (Bring Your Own Vulnerable Driver)**: Exploitation of security gaps to weaponize Windows drivers

## Threat Actor Activities

- **Single Ivanti Threat Actor**: Responsible for 83% of recent Ivanti EPMM RCE attacks, demonstrating concentrated exploitation efforts
- **China, Iran, Russia, North Korea State Actors**: Coordinated cyber operations targeting defense industrial base with zero-day vulnerabilities
- **UAT-9921**: Previously unknown threat actor deploying VoidLink malware framework against technology and financial sectors
- **Russian CANFAIL Actor**: Google attributes suspected Russian threat actor to CANFAIL malware attacks on Ukrainian organizations
- **North Korean Developer Targeting Groups**: Fake recruitment campaigns targeting JavaScript and Python developers with cryptocurrency-themed malicious tasks
- **Cryptocurrency Hardware Wallet Scammers**: Physical mail campaigns targeting Trezor and Ledger users to steal recovery phrases
- **Chrome Extension Threat Actors**: Malicious extensions targeting Meta Business Suite and Facebook Business Manager data
- **Qilin Ransomware Gang**: Confirmed data theft from Romania's national oil pipeline operator Conpet S.A.