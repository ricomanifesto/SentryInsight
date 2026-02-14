# Exploitation Report

Critical exploitation activity is currently targeting enterprise infrastructure and software supply chains. Nation-state actors from Russia, China, North Korea, and Iran are actively exploiting zero-day vulnerabilities in edge devices and enterprise management systems. Particularly concerning is the active exploitation of a critical Microsoft Configuration Manager vulnerability and a BeyondTrust remote access flaw with CVSS 9.9 rating. North Korean threat actors are conducting sophisticated supply chain attacks through malicious npm and PyPI packages, while leveraging AI tools for reconnaissance. The defense industrial base has become a primary target, with over two dozen zero-day vulnerabilities exploited in coordinated campaigns against defense contractors.

## Active Exploitation Details

### Microsoft Configuration Manager RCE Vulnerability
- **Description**: Critical vulnerability in Microsoft System Center Configuration Manager (SCCM) that allows remote code execution
- **Impact**: Attackers can achieve complete system compromise and lateral movement across enterprise networks
- **Status**: Patched in October 2024, now actively exploited in the wild with CISA ordering federal agencies to secure systems

### BeyondTrust Remote Support Critical RCE Flaw  
- **Description**: Pre-authentication remote code execution vulnerability in BeyondTrust Remote Support (RS) and Privileged Remote Access (PRA) products
- **Impact**: Complete system compromise without authentication requirements
- **Status**: Currently being exploited in attacks following public PoC release, CVSS score 9.9

### Ivanti EPMM Zero-Day Vulnerabilities
- **Description**: Multiple zero-day vulnerabilities in Ivanti Endpoint Manager Mobile (EPMM) products
- **Impact**: Complete device compromise and enterprise network infiltration
- **Status**: Active exploitation ongoing with exploit frenzy observed

### WPvivid WordPress Plugin RCE Vulnerability
- **Description**: Critical remote code execution vulnerability in WPvivid Backup & Migration plugin
- **Impact**: Arbitrary file upload leading to complete website compromise
- **Status**: Affects over 900,000 WordPress installations, patch status unclear

## Affected Systems and Products

- **Microsoft Configuration Manager (SCCM)**: Enterprise system management and deployment platform
- **BeyondTrust Remote Support/PRA**: Remote access and privileged account management appliances  
- **Ivanti EPMM**: Mobile device management and endpoint security solutions
- **WPvivid WordPress Plugin**: Backup and migration plugin with 900,000+ installations
- **Edge Devices**: Network infrastructure components targeted by nation-state actors
- **npm/PyPI Repositories**: Software package repositories contaminated with malicious packages
- **Chrome Browser Extensions**: Malicious extensions targeting Meta Business Suite data

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Malicious packages planted in npm and PyPI ecosystems by Lazarus Group
- **Fake Recruitment Campaigns**: North Korean actors using cryptocurrency-related coding challenges to deliver malware
- **ClickFix Attacks**: Abuse of Claude LLM artifacts and Google Ads to distribute macOS infostealers
- **BYOVD Attacks**: Bring Your Own Vulnerable Driver attacks exploiting Windows driver security gaps
- **AI-Assisted Reconnaissance**: State-backed hackers using Google Gemini AI for target reconnaissance
- **Chrome Extension Abuse**: Malicious extensions stealing business data and browsing history
- **Zero-Day Exploitation**: Coordinated use of over 24 zero-days against defense sector targets

## Threat Actor Activities

- **Lazarus Group (North Korea)**: Conducting supply chain attacks through malicious npm/PyPI packages and fake recruitment campaigns targeting developers
- **UNC2970 (North Korea)**: Using Google Gemini AI for reconnaissance and attack planning
- **UAT-9921**: Deploying VoidLink malware framework against technology and financial sectors
- **Russian State Actors**: Attributed to CANFAIL malware attacks targeting Ukrainian organizations
- **Multi-Nation Coordination**: China, Iran, Russia, and North Korea conducting coordinated operations against defense industrial base
- **Qilin Ransomware Group**: Confirmed data theft from Romania's national oil pipeline operator Conpet S.A.