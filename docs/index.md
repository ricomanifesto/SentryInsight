# Exploitation Report

Critical security vulnerabilities are being actively exploited across multiple platforms and industries, with threat actors leveraging zero-day vulnerabilities, recently patched flaws, and sophisticated social engineering tactics. The most severe exploitation activity includes a critical Microsoft Configuration Manager vulnerability now being exploited in the wild, a BeyondTrust remote code execution flaw with active exploitation following proof-of-concept publication, and new zero-day vulnerabilities in Ivanti Endpoint Manager Mobile (EPMM) products. Nation-state actors from China, Russia, North Korea, and Iran are conducting coordinated campaigns against defense industrial base organizations, while various threat groups are deploying malware through fake recruitment campaigns, malicious browser extensions, and supply chain attacks.

## Active Exploitation Details

### Microsoft Configuration Manager Critical Vulnerability
- **Description**: Critical vulnerability in Microsoft System Center Configuration Manager (SCCM) that was patched in October 2024
- **Impact**: Enables remote code execution and system compromise
- **Status**: Now being actively exploited in attacks according to CISA advisory requiring federal agencies to patch immediately

### BeyondTrust Remote Code Execution Vulnerability
- **Description**: Critical pre-authentication remote code execution vulnerability affecting BeyondTrust Remote Support (RS) and Privileged Remote Access (PRA) appliances
- **Impact**: Allows attackers to execute arbitrary code without authentication with CVSS score of 9.9
- **Status**: Active exploitation observed following publication of proof-of-concept exploit code

### Ivanti EPMM Zero-Day Vulnerabilities
- **Description**: Multiple zero-day vulnerabilities discovered in Ivanti Endpoint Manager Mobile products
- **Impact**: Enables remote exploitation and system compromise
- **Status**: Active exploitation campaigns targeting these zero-day flaws

### WPvivid Backup WordPress Plugin RCE
- **Description**: Critical remote code execution vulnerability in WPvivid Backup & Migration plugin for WordPress
- **Impact**: Allows arbitrary file upload leading to remote code execution on websites
- **Status**: Vulnerability disclosed, affects over 900,000 installations

## Affected Systems and Products

- **Microsoft Configuration Manager**: System Center Configuration Manager (SCCM) installations patched in October 2024
- **BeyondTrust Products**: Remote Support (RS) and Privileged Remote Access (PRA) appliances
- **Ivanti EPMM**: Endpoint Manager Mobile products experiencing zero-day exploitation
- **WordPress Sites**: Over 900,000 websites using WPvivid Backup & Migration plugin
- **Chrome Browser**: Malicious extensions targeting Meta Business Suite and Facebook Business Manager data
- **macOS Systems**: Users targeted through Claude AI artifacts and Google Ads in ClickFix campaigns
- **Defense Industrial Base**: Organizations targeted by coordinated nation-state campaigns
- **npm and PyPI**: Package repositories compromised with malicious packages from Lazarus group

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Nation-state actors burning dozens of zero-days in edge devices to infiltrate defense contractors
- **Social Engineering**: Fake recruitment campaigns targeting JavaScript and Python developers with cryptocurrency-related coding challenges
- **Supply Chain Attacks**: Malicious packages planted in npm and PyPI repositories by North Korean Lazarus group
- **ClickFix Campaigns**: Abuse of Claude AI artifacts and Google Ads to deliver macOS infostealers
- **BYOVD Attacks**: Bring Your Own Vulnerable Driver attacks exploiting Windows driver security gaps
- **Malicious Browser Extensions**: Chrome extensions designed to steal business data and browsing history
- **AI-Assisted Reconnaissance**: State-backed hackers using Google's Gemini AI for target reconnaissance and attack support

## Threat Actor Activities

- **North Korean Groups**: UNC2970 and Lazarus conducting fake recruitment campaigns and using AI tools for reconnaissance and attack support
- **Russian Actors**: Previously undocumented threat actor deploying CANFAIL malware against Ukrainian organizations
- **UAT-9921**: New threat actor targeting technology and financial sectors with VoidLink modular framework
- **Chinese State Groups**: Coordinated campaigns against defense industrial base alongside other nation-state actors
- **Multiple Nation-States**: China, Iran, Russia, and North Korea conducting coordinated cyber operations against defense sector
- **Qilin Ransomware**: Successful attack against Romania's national oil pipeline operator Conpet S.A. with confirmed data theft