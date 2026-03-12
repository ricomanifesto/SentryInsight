# Exploitation Report

The current threat landscape reveals significant active exploitation across multiple critical vulnerabilities, with CISA recently adding an n8n remote code execution flaw to its Known Exploited Vulnerabilities catalog amid evidence of widespread attacks. Apple has responded to active exploitation by backporting security fixes for the Coruna exploit kit targeting WebKit vulnerabilities in older iOS devices. Supply chain attacks continue to proliferate with sophisticated campaigns targeting npm and Rust package repositories, while threat actors demonstrate rapid adaptation to geopolitical events and increasingly leverage AI-powered tools for automated exploitation.

## Active Exploitation Details

### n8n Remote Code Execution Vulnerability
- **Description**: Critical security flaw in the n8n workflow automation platform that allows attackers to execute arbitrary commands remotely
- **Impact**: Complete system compromise and potential access to stored credentials and sensitive workflow data
- **Status**: Actively exploited in the wild with CISA ordering federal agencies to patch immediately; approximately 24,700 instances remain exposed globally

### Coruna WebKit Exploit Kit
- **Description**: Set of vulnerabilities in WebKit targeting older Apple devices used in cyberespionage and cryptocurrency theft campaigns
- **Impact**: Complete device compromise allowing data theft and unauthorized access to cryptocurrency wallets
- **Status**: Actively exploited against older iPhones and iPads; Apple has backported security fixes to older iOS, iPadOS, and macOS Sonoma versions

### nx npm Supply Chain Compromise
- **Description**: Supply chain attack targeting the nx npm package that resulted in credential theft and cloud environment compromise
- **Impact**: Complete AWS environment takeover within 72 hours using stolen authentication keys
- **Status**: Previously exploited by UNC6426 threat group with ongoing implications for affected organizations

### Microsoft Zero-Day Vulnerabilities
- **Description**: Two publicly known zero-day vulnerabilities patched in Microsoft's March Patch Tuesday update
- **Impact**: Various levels of system compromise depending on specific vulnerability
- **Status**: Publicly disclosed but exploitation status unclear; patches available as of March 2026

## Affected Systems and Products

- **n8n Workflow Automation Platform**: Over 24,700 exposed instances globally with active exploitation targeting unpatched systems
- **Apple iOS/iPadOS Devices**: Older iPhone and iPad models targeted by Coruna exploit kit in cyberespionage campaigns
- **WordPress Sites**: Over 250,000 sites using vulnerable Elementor Ally plugin exposed to SQL injection attacks
- **npm Package Ecosystem**: Developers using compromised packages including nx and 88 malicious PhantomRaven packages
- **Rust Package Registry**: Five malicious crates targeting CI/CD pipelines to steal developer secrets
- **Microsoft Windows Systems**: 84 vulnerabilities patched including two public zero-days affecting various Windows components
- **SAP Enterprise Software**: Critical vulnerabilities allowing arbitrary code execution on affected systems
- **Android Devices**: Six new malware families targeting Pix payments, banking apps, and cryptocurrency wallets

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Malicious packages distributed through npm, Rust crates, and GitHub Actions to compromise developer environments
- **WebKit Browser Exploitation**: Coruna exploit kit leveraging browser vulnerabilities for device compromise and data theft
- **SQL Injection**: Elementor Ally plugin vulnerability allowing database access and sensitive data extraction
- **Remote Code Execution**: n8n platform exploitation enabling complete system takeover and credential theft
- **Wiper Malware**: Iranian-linked Handala group deploying destructive malware against healthcare and technology companies
- **AI-Powered Phishing**: Sophisticated campaigns designed to exhaust SOC analysts while maintaining persistence
- **Tag Poisoning**: GitHub Action compromise through malicious version tagging affecting CI/CD pipelines

## Threat Actor Activities

- **UNC6426**: Leveraged nx npm compromise to achieve complete AWS environment takeover within 72 hours using stolen credentials
- **PhantomRaven Campaign**: Ongoing supply chain attacks targeting JavaScript developers through 88 malicious npm packages
- **Handala Group**: Iranian-linked hacktivist group conducting wiper attacks against medical technology companies including Stryker
- **INC Ransomware**: Targeting healthcare organizations across Oceania including government agencies and emergency clinics
- **Chinese Nexus Actors**: Pivoting focus to Qatari entities in response to Middle East geopolitical developments
- **BlackCat/ALPHV Affiliates**: Continued ransomware operations with insider collaboration through cryptocurrency exchange partnerships
- **Android Banking Trojans**: Six new malware families targeting financial applications and cryptocurrency wallets in coordinated campaigns