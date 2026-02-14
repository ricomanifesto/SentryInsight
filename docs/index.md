# Exploitation Report

Critical exploitation activity is currently targeting enterprise infrastructure and consumer applications through multiple active attack campaigns. Nation-state actors from China, Iran, Russia, and North Korea are conducting coordinated operations against defense industrial base organizations, leveraging dozens of zero-day vulnerabilities in edge devices. Simultaneously, critical vulnerabilities in Microsoft Configuration Manager and BeyondTrust remote access products are being actively exploited in the wild, while threat actors abuse legitimate platforms like Claude AI artifacts and malicious browser extensions to deploy infostealers targeting both Windows and macOS users.

## Active Exploitation Details

### Microsoft Configuration Manager Remote Code Execution Vulnerability
- **Description**: A critical vulnerability in Microsoft System Center Configuration Manager (SCCM) that allows remote code execution
- **Impact**: Attackers can execute arbitrary code remotely on vulnerable SCCM systems, potentially gaining full control over enterprise configuration management infrastructure
- **Status**: Patched in October 2024, now actively exploited in attacks with CISA ordering federal agencies to secure their systems

### BeyondTrust Remote Support Critical RCE Vulnerability
- **Description**: A critical pre-authentication remote code execution vulnerability affecting BeyondTrust Remote Support (RS) and Privileged Remote Access (PRA) appliances with CVSS score of 9.9
- **Impact**: Allows attackers to execute arbitrary code without authentication on remote access management systems
- **Status**: Currently being exploited in the wild following public proof-of-concept publication

### Zero-Day Vulnerabilities in Edge Devices
- **Description**: At least two dozen zero-day vulnerabilities targeting edge devices used by defense contractors
- **Impact**: Enable nation-state actors to infiltrate defense industrial base networks for espionage operations
- **Status**: Actively exploited by espionage groups from China, Russia, and other nations

### Ivanti EPMM Zero-Day Vulnerabilities
- **Description**: Multiple zero-day vulnerabilities affecting Ivanti Endpoint Manager Mobile (EPMM) products
- **Impact**: Allows attackers to compromise mobile device management infrastructure
- **Status**: Currently experiencing active exploitation following vulnerability disclosure

### WordPress WPvivid Backup Plugin RCE Vulnerability
- **Description**: Critical remote code execution vulnerability in WPvivid Backup & Migration plugin installed on over 900,000 WordPress sites
- **Impact**: Enables arbitrary file upload leading to remote code execution on WordPress websites
- **Status**: Vulnerability disclosed, patch status unclear

## Affected Systems and Products

- **Microsoft Configuration Manager**: Enterprise configuration management systems patched in October 2024
- **BeyondTrust Remote Support/PRA**: Remote access management appliances with CVSS 9.9 vulnerability
- **Defense Industrial Base Edge Devices**: Various edge computing and network devices used by defense contractors
- **Ivanti EPMM Products**: Mobile device management systems experiencing zero-day exploitation
- **WordPress WPvivid Plugin**: Backup and migration plugin with 900,000+ installations
- **Google Chrome Extensions**: Malicious extensions targeting Meta Business Suite and Facebook Business Manager data
- **macOS Systems**: Targeted by AMOS infostealer through AI application abuse
- **Claude AI Artifacts**: Abused to deliver infostealers in ClickFix campaigns
- **npm and PyPI Repositories**: Compromised with malicious packages linked to Lazarus group

## Attack Vectors and Techniques

- **ClickFix Campaigns**: Abuse of Claude AI artifacts and Google Ads to deliver infostealers to macOS users
- **Malicious Browser Extensions**: Chrome extensions designed to steal business data, emails, and browsing history
- **Supply Chain Attacks**: Malicious packages planted in npm and PyPI ecosystems by Lazarus group
- **Fake Recruitment Campaigns**: Social engineering tactics using job opportunities to distribute malware
- **AI Platform Abuse**: Exploitation of legitimate AI applications and extension marketplaces
- **BYOVD Attacks**: Bring Your Own Vulnerable Driver attacks targeting Windows systems
- **Pre-authentication Exploitation**: Remote code execution without requiring user credentials
- **Zero-Day Edge Device Exploitation**: Targeting network infrastructure and edge computing devices

## Threat Actor Activities

- **Nation-State Espionage Groups**: China, Iran, Russia, and North Korea conducting coordinated operations against defense industrial base
- **UNC2970 (North Korea)**: Using Google Gemini AI for reconnaissance and attack support activities
- **Lazarus Group**: Planting malicious packages in software repositories through fake recruitment campaigns
- **Russian State Actor**: Attributed to CANFAIL malware attacks targeting Ukrainian organizations
- **UAT-9921**: Deploying VoidLink malware framework against technology and financial sectors
- **Qilin Ransomware Gang**: Confirmed data theft from Romania's oil pipeline operator Conpet S.A.
- **Various Cybercriminals**: Exploiting newly disclosed vulnerabilities in enterprise software and conducting infostealer campaigns