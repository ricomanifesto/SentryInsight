# Exploitation Report

Critical vulnerabilities across multiple platforms are currently under active exploitation, posing significant risks to organizations worldwide. The most concerning developments include a critical Microsoft Configuration Manager vulnerability being exploited in the wild, a BeyondTrust remote code execution flaw with active exploitation after public proof-of-concept release, and new Ivanti EPMM zero-day vulnerabilities sparking widespread exploit activity. Nation-state actors, including North Korean groups, are leveraging sophisticated social engineering campaigns targeting developers and defense contractors, while multiple threat actors are deploying new malware frameworks and exploiting edge device vulnerabilities with zero-days to infiltrate critical infrastructure.

## Active Exploitation Details

### Microsoft Configuration Manager Remote Code Execution Vulnerability
- **Description**: A critical vulnerability in Microsoft System Center Configuration Manager (SCCM) that allows remote code execution
- **Impact**: Attackers can execute arbitrary code on affected systems with elevated privileges
- **Status**: Patched in October 2024, now actively exploited in attacks - CISA has ordered federal agencies to secure systems

### BeyondTrust Remote Support and Privileged Remote Access RCE Vulnerability
- **Description**: A critical pre-authentication remote code execution vulnerability affecting BeyondTrust Remote Support (RS) and Privileged Remote Access (PRA) products with CVSS score of 9.9
- **Impact**: Allows unauthenticated attackers to execute arbitrary code remotely on affected appliances
- **Status**: Currently being exploited in the wild following publication of proof-of-concept exploit code

### Ivanti Endpoint Manager Mobile (EPMM) Zero-Day Vulnerabilities
- **Description**: Multiple zero-day vulnerabilities in Ivanti EPMM that enable exploitation without authentication
- **Impact**: Allows attackers to gain unauthorized access to mobile device management systems
- **Status**: Active exploitation observed, described as sparking an "exploit frenzy"

### WPvivid Backup & Migration WordPress Plugin RCE Vulnerability
- **Description**: Critical remote code execution vulnerability in the WPvivid Backup & Migration plugin through arbitrary file upload
- **Impact**: Attackers can achieve remote code execution on WordPress sites by uploading malicious files
- **Status**: Affects over 900,000 WordPress installations

## Affected Systems and Products

- **Microsoft System Center Configuration Manager**: All versions prior to October 2024 patches
- **BeyondTrust Remote Support and Privileged Remote Access**: Specific versions of RS and PRA appliances
- **Ivanti Endpoint Manager Mobile**: Current versions with unpatched zero-day vulnerabilities
- **WordPress Sites**: Over 900,000 installations using WPvivid Backup & Migration plugin
- **Google Chrome Extensions**: Malicious extensions targeting Meta Business Suite and Facebook Business Manager
- **Edge Network Devices**: Multiple vendors affected by nation-state zero-day exploitation
- **npm and PyPI Repositories**: Malicious packages planted in JavaScript and Python ecosystems

## Attack Vectors and Techniques

- **Fake Recruitment Campaigns**: North Korean threat actors using cryptocurrency-related coding challenges to target JavaScript and Python developers
- **ClickFix Campaigns**: Abuse of Claude LLM artifacts and Google Ads to deliver macOS infostealers
- **BYOVD Attacks**: Bring Your Own Vulnerable Driver attacks exploiting Windows driver security gaps to terminate security processes
- **Supply Chain Attacks**: Malicious packages planted in npm and PyPI repositories as part of fake recruitment campaigns
- **Social Engineering**: Sophisticated campaigns targeting developers through job recruitment facades
- **AI-Assisted Reconnaissance**: State-backed hackers using Google Gemini AI for target reconnaissance and attack support
- **Chrome Extension Abuse**: Malicious browser extensions stealing business data, emails, and browsing history

## Threat Actor Activities

- **North Korean Lazarus Group**: Deploying malicious packages in npm and PyPI ecosystems through fake recruitment campaigns targeting developers
- **UNC2970 (North Korea-linked)**: Using Google Gemini AI for reconnaissance activities and attack support operations
- **UAT-9921**: Previously unknown threat actor deploying VoidLink malware framework targeting technology and financial sectors
- **Russian State-Sponsored Groups**: Attributed to CANFAIL malware attacks targeting Ukrainian organizations
- **Multi-Nation Coordination**: China, Iran, Russia, and North Korea conducting coordinated cyber operations against defense industrial base
- **Edge Device Exploitation Groups**: Nation-state actors from multiple countries burning zero-days in edge devices to infiltrate defense contractor networks
- **Qilin Ransomware Gang**: Confirmed data theft from Romania's national oil pipeline operator Conpet S.A.