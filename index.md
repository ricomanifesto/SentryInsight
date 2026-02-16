# Exploitation Report

The current threat landscape reveals multiple critical zero-day vulnerabilities under active exploitation, with Google Chrome facing its first zero-day attack of the year, BeyondTrust products experiencing widespread exploitation of a critical CVSS 9.9 vulnerability, and Microsoft Configuration Manager (SCCM) vulnerabilities being actively exploited in the wild. Additionally, Ivanti Endpoint Manager Mobile continues to face significant exploitation pressure, with a single threat actor responsible for 83% of recent attacks. Mobile spyware platforms like ZeroDayRAT are enabling sophisticated surveillance operations, while innovative attack techniques such as DNS-based ClickFix campaigns and malicious Chrome extensions are expanding the threat surface.

## Active Exploitation Details

### Chrome Zero-Day Vulnerability
- **Description**: A high-severity security flaw in Google Chrome browser that has been actively exploited in the wild
- **Impact**: Allows attackers to exploit users through zero-day attacks targeting the Chrome browser
- **Status**: Patched by Google with emergency security updates released
- **CVE ID**: CVE-2026-2441

### BeyondTrust Critical Vulnerability
- **Description**: A critical security flaw affecting BeyondTrust Remote Support (RS) and Privileged Remote Access (PRA) products with a maximum CVSS score
- **Impact**: Enables threat actors to compromise remote access and privileged access management systems
- **Status**: Actively exploited in the wild with observed in-the-wild exploitation
- **CVSS Score**: 9.9 (Critical)

### Microsoft Configuration Manager (SCCM) Vulnerability
- **Description**: A critical remote code execution vulnerability in Microsoft Configuration Manager patched in October 2024
- **Impact**: Allows attackers to achieve remote code execution on affected systems
- **Status**: CISA has flagged this as actively exploited and ordered federal agencies to secure systems

### Ivanti EPMM Zero-Day Vulnerabilities
- **Description**: Multiple critical vulnerabilities in Ivanti Endpoint Manager Mobile (EPMM) systems
- **Impact**: Remote code execution and system compromise capabilities
- **Status**: Under active exploitation with one threat actor responsible for 83% of recent attacks

## Affected Systems and Products

- **Google Chrome**: All versions prior to the emergency security update
- **BeyondTrust Remote Support (RS)**: Privileged remote access management systems
- **BeyondTrust Privileged Remote Access (PRA)**: Remote support platforms
- **Microsoft Configuration Manager (SCCM)**: Enterprise system management platforms
- **Ivanti Endpoint Manager Mobile (EPMM)**: Mobile device management solutions
- **Android Mobile Devices**: Targeted by ZeroDayRAT spyware platform
- **Windows Systems**: Affected by BYOVD (Bring Your Own Vulnerable Driver) attacks
- **Meta Business Suite**: Targeted by malicious Chrome extensions
- **Facebook Business Manager**: Compromised through malicious browser extensions

## Attack Vectors and Techniques

- **Zero-Day Browser Exploitation**: Chrome vulnerability exploited through web-based attacks
- **DNS-Based ClickFix Attacks**: Novel technique using nslookup commands and DNS queries to retrieve PowerShell payloads
- **Malicious Chrome Extensions**: Extensions designed to steal business data, emails, and browsing history
- **ClickFix Social Engineering**: JavaScript-based attacks distributed through Pastebin comments and Claude LLM artifacts
- **Mobile Spyware Deployment**: ZeroDayRAT platform enabling real-time surveillance and data theft
- **BYOVD Attacks**: Bring Your Own Vulnerable Driver techniques to terminate security processes
- **Supply Chain Attacks**: Targeting of defense industrial base through edge device compromises
- **Social Engineering via Physical Mail**: Letters impersonating Trezor and Ledger to steal cryptocurrency recovery phrases
- **Fake Recruiter Campaigns**: North Korean actors using coding challenges to deliver malware to developers

## Threat Actor Activities

- **Single Ivanti Attacker**: One threat actor responsible for 83% of recent Ivanti EPMM remote code execution attacks
- **UAT-9921**: Previously unknown threat actor deploying VoidLink malware framework against technology and financial sectors
- **Russian-Linked Actor**: Suspected Russian threat actor using CANFAIL malware to target Ukrainian organizations
- **ShinyHunters**: Data extortion group claiming theft of 600,000+ Canada Goose customer records
- **Chinese State-Sponsored Groups**: Multiple nation-state actors targeting defense industrial base with zero-day exploits
- **North Korean Actors**: Conducting fake recruiter campaigns targeting JavaScript and Python developers
- **Multi-Nation Coordination**: China, Iran, Russia, and North Korea coordinating cyber operations against defense sectors
- **Criminal Groups**: Various criminal entities leveraging Lumma Stealer and infostealer campaigns through Google Groups abuse