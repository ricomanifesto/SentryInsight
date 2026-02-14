# Exploitation Report

Critical vulnerabilities across multiple enterprise systems are currently under active exploitation, with several high-severity flaws being leveraged in targeted attacks. Most notably, a critical Microsoft Configuration Manager vulnerability and a severe BeyondTrust Remote Support flaw are being actively exploited in the wild, prompting urgent patching directives from CISA. Additionally, threat actors continue to target defense industrial base organizations through coordinated campaigns exploiting edge device vulnerabilities, while North Korean actors have expanded their social engineering tactics to target developers through malicious recruitment campaigns. The exploitation landscape also includes ongoing attacks against WordPress installations and emerging threats targeting mobile device management platforms.

## Active Exploitation Details

### Microsoft Configuration Manager Vulnerability
- **Description**: Critical remote code execution vulnerability in Microsoft System Center Configuration Manager (SCCM) that was patched in October 2024
- **Impact**: Allows attackers to execute arbitrary code remotely on vulnerable systems
- **Status**: Currently being exploited in attacks; CISA has ordered federal agencies to patch immediately

### BeyondTrust Remote Support Critical Flaw
- **Description**: Critical pre-authentication remote code execution vulnerability in BeyondTrust Remote Support and Privileged Remote Access appliances
- **Impact**: Enables attackers to achieve remote code execution without authentication on affected systems
- **Status**: Active exploitation observed after proof-of-concept was published online; CVSS score of 9.9

### WPvivid Backup & Migration Plugin Vulnerability
- **Description**: Critical remote code execution vulnerability in WordPress plugin with over 900,000 installations
- **Impact**: Allows attackers to upload arbitrary files and achieve remote code execution on WordPress sites
- **Status**: Vulnerability disclosed but exploitation status unclear

### Ivanti EPMM Zero-Day Vulnerabilities
- **Description**: Multiple zero-day vulnerabilities discovered in Ivanti Endpoint Manager Mobile (EPMM)
- **Impact**: Exploitation allows attackers to compromise mobile device management systems
- **Status**: Active exploitation reported; patches available

### Defense Industrial Base Edge Device Exploits
- **Description**: At least two dozen zero-day vulnerabilities in edge devices targeted by nation-state actors
- **Impact**: Used to infiltrate defense contractor networks for espionage purposes
- **Status**: Active campaigns by Chinese, Russian, and other nation-state groups

## Affected Systems and Products

- **Microsoft Configuration Manager**: Enterprise system management platform used across federal agencies and organizations
- **BeyondTrust Remote Support/PRA**: Remote access and privileged access management appliances
- **WordPress WPvivid Plugin**: Backup and migration plugin installed on over 900,000 websites
- **Ivanti EPMM**: Enterprise mobile device management platform
- **Edge Network Devices**: Various edge devices used by defense contractors and organizations
- **Google Chrome**: Browser targeted through malicious extensions stealing business data
- **Claude AI Platform**: Anthropic's LLM platform abused to distribute macOS infostealers
- **Facebook Business Manager**: Targeted through malicious Chrome extensions

## Attack Vectors and Techniques

- **Social Engineering Campaigns**: North Korean actors using fake recruitment campaigns targeting JavaScript and Python developers with cryptocurrency-related coding challenges
- **ClickFix Campaigns**: Abuse of Claude LLM artifacts and Google Ads to deliver infostealer malware to macOS users
- **Malicious Browser Extensions**: Chrome extensions designed to steal Meta Business Suite and Facebook Business Manager data
- **BYOVD Attacks**: Bring Your Own Vulnerable Driver attacks exploiting Windows driver security gaps to terminate security processes
- **Supply Chain Attacks**: Targeting npm package ecosystem and development environments
- **Pre-authentication Exploitation**: Direct exploitation of network-accessible services without authentication requirements

## Threat Actor Activities

- **North Korean Groups (UNC2970)**: Conducting fake recruitment campaigns targeting developers and using Google's Gemini AI for reconnaissance and attack support
- **UAT-9921**: Previously unknown threat actor deploying VoidLink malware framework against technology and financial sectors
- **Russian Actors**: Deploying CANFAIL malware against Ukrainian organizations
- **Chinese, Iranian, Russian, North Korean State Groups**: Coordinated campaigns targeting defense industrial base with focus on edge device exploitation
- **Qilin Ransomware Gang**: Successfully breached Romania's national oil pipeline operator Conpet S.A.
- **Multiple Nation-State Groups**: Collaborative efforts targeting defense contractors through zero-day exploits in network edge devices