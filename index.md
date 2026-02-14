# Exploitation Report

Multiple critical vulnerabilities are currently being exploited in the wild, with particular focus on enterprise infrastructure and remote access solutions. A single threat actor is responsible for 83% of recent attacks against Ivanti Endpoint Manager Mobile vulnerabilities, while BeyondTrust remote access products face active exploitation of a critical pre-authentication remote code execution flaw with a CVSS score of 9.9. Additionally, Microsoft Configuration Manager systems are under attack through a critical vulnerability that CISA has added to its Known Exploited Vulnerabilities catalog, and nation-state actors from China, Russia, Iran, and North Korea are coordinating sophisticated attacks against defense contractors using dozens of zero-day exploits in edge devices.

## Active Exploitation Details

### Ivanti Endpoint Manager Mobile Critical Vulnerabilities
- **Description**: Two critical remote code execution vulnerabilities in Ivanti EPMM are being actively exploited, with a dominant threat actor responsible for the vast majority of attacks
- **Impact**: Remote code execution allowing complete system compromise of endpoint management infrastructure
- **Status**: Active exploitation ongoing with concentrated threat actor activity accounting for 83% of attacks

### BeyondTrust Remote Support and Privileged Remote Access RCE
- **Description**: Critical pre-authentication remote code execution vulnerability in BeyondTrust RS and PRA appliances
- **Impact**: Attackers can achieve remote code execution without authentication, potentially compromising privileged access management systems
- **Status**: Active in-the-wild exploitation confirmed after proof-of-concept publication, CVSS score 9.9

### Microsoft Configuration Manager Critical Flaw
- **Description**: Critical remote code execution vulnerability in Microsoft System Center Configuration Manager (SCCM)
- **Impact**: Remote code execution on enterprise configuration management systems
- **Status**: CISA added to Known Exploited Vulnerabilities catalog, active exploitation confirmed, patched in October 2024

### Defense Industrial Base Zero-Day Attacks
- **Description**: Multiple zero-day vulnerabilities in edge devices being exploited by nation-state actors
- **Impact**: Network infiltration and espionage targeting defense contractors
- **Status**: At least 24 zero-days burned by espionage groups from multiple nations

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile**: Enterprise mobile device management platforms experiencing concentrated attack campaigns
- **BeyondTrust Remote Support and Privileged Remote Access**: Remote access and privileged account management appliances facing critical pre-auth RCE exploitation  
- **Microsoft Configuration Manager (SCCM)**: Enterprise system configuration management infrastructure under active attack
- **Defense Contractor Edge Devices**: Network perimeter devices at defense industrial base organizations targeted with zero-day exploits
- **Chrome Browser Extensions**: Malicious extensions targeting Meta Business Suite and Facebook Business Manager data
- **macOS Systems**: ClickFix campaigns delivering infostealer malware through Claude LLM artifacts and Google Ads

## Attack Vectors and Techniques

- **Pre-Authentication Remote Code Execution**: Exploitation of BeyondTrust appliances without requiring valid credentials
- **Remote Code Execution via SCCM**: Leveraging Microsoft Configuration Manager vulnerabilities for system compromise
- **Zero-Day Edge Device Exploitation**: Nation-state actors using previously unknown vulnerabilities in network perimeter devices
- **Social Engineering via Physical Mail**: Threat actors sending physical letters impersonating Trezor and Ledger to steal cryptocurrency recovery phrases
- **Fake Recruitment Campaigns**: North Korean actors using cryptocurrency-related coding challenges to distribute malware to JavaScript and Python developers
- **ClickFix Campaign Abuse**: Malicious use of Claude LLM artifacts combined with Google Ads to deliver infostealer malware
- **Bring Your Own Vulnerable Driver (BYOVD)**: Weaponizing legitimate Windows drivers to terminate security processes and evade detection
- **Malicious Browser Extensions**: Chrome extensions designed to steal business data, emails, and browsing history from Meta platforms

## Threat Actor Activities

- **Dominant Ivanti Threat Actor**: Single actor responsible for 83% of recent Ivanti EPMM exploitation attempts, showing concentrated focus on enterprise mobile management infrastructure
- **Russian CANFAIL Campaign**: Previously undocumented Russian threat actor targeting Ukrainian organizations with CANFAIL malware
- **UAT-9921**: New threat actor deploying VoidLink modular malware framework against technology and financial services sectors
- **North Korean Developer Targeting**: Continued fake recruiter campaigns targeting software developers with cryptocurrency-themed malicious coding challenges
- **Multi-Nation Defense Targeting**: Coordinated espionage operations by state-sponsored actors from China, Iran, Russia, and North Korea against defense industrial base
- **Qilin Ransomware**: Confirmed data theft from Romania's national oil pipeline operator Conpet S.A.
- **ClickFix Operators**: Threat actors abusing legitimate AI platforms and advertising networks to distribute macOS infostealer malware