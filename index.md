# Exploitation Report

The current threat landscape reveals multiple critical exploitation activities targeting enterprise infrastructure and cloud environments. CISA has issued emergency directives for federal agencies to patch actively exploited vulnerabilities in n8n workflow automation platforms, while threat actors continue to leverage supply chain attacks through compromised NPM packages and malicious code repositories. Healthcare systems across Oceania face ongoing ransomware campaigns, and Iranian-linked groups have deployed wiper malware against major medical technology companies. Meanwhile, sophisticated attackers are exploiting enterprise software vulnerabilities, including SQL injection flaws in WordPress plugins affecting hundreds of thousands of installations, and leveraging compromised GitHub Actions for sustained command and control operations.

## Active Exploitation Details

### n8n Workflow Automation Platform Vulnerabilities
- **Description**: Critical remote code execution and credential exposure vulnerabilities in the n8n workflow automation platform
- **Impact**: Attackers can achieve arbitrary command execution and access stored credentials on affected systems
- **Status**: Actively exploited in the wild; CISA has mandated federal agencies to patch immediately

### Elementor Ally WordPress Plugin SQL Injection
- **Description**: SQL injection vulnerability in the Ally WordPress plugin for web accessibility and usability
- **Impact**: Exploitation allows attackers to steal sensitive data without authentication
- **Status**: Affects over 250,000 WordPress installations; patch status unclear

### xygeni-action GitHub Repository Compromise
- **Description**: Tag poisoning attack compromising AppSec vendor Xygeni's GitHub Action
- **Impact**: Attackers operated an active command and control implant for up to one week
- **Status**: Attackers maintained persistent access to the compromised repository

### Microsoft Zero-Day Vulnerabilities
- **Description**: Two publicly disclosed zero-day vulnerabilities patched in March 2026 Patch Tuesday
- **Impact**: Exploitation details vary by vulnerability; impact assessment ongoing
- **Status**: Publicly known vulnerabilities now patched as part of 79-84 total security fixes

### HPE AOS-CX Authentication Bypass
- **Description**: Critical authentication vulnerability in Hewlett Packard Enterprise's Aruba Networking AOS-CX operating system
- **Impact**: Allows unauthorized administrative password resets and potential system compromise
- **Status**: Multiple authentication and code execution vulnerabilities patched

## Affected Systems and Products

- **n8n Workflow Automation Platform**: Critical RCE and credential exposure vulnerabilities
- **WordPress Sites**: Over 250,000 installations using Elementor Ally plugin vulnerable to SQL injection
- **Microsoft Windows Systems**: 79-84 vulnerabilities across Windows operating systems and software components
- **GitHub Repositories**: xygeni/xygeni-action compromised via tag poisoning attack
- **HPE Aruba Networking**: AOS-CX operating system affected by authentication bypass vulnerabilities
- **Healthcare Systems**: Government agencies, emergency clinics in Australia, New Zealand, and Tonga targeted by ransomware
- **Medical Technology**: Stryker medical technology company hit by wiper malware attack
- **NPM Package Registry**: 88+ malicious packages in PhantomRaven campaign targeting JavaScript developers
- **Rust Package Registry**: Five malicious crates targeting CI/CD pipelines to steal developer secrets
- **Android Devices**: BeatBanker malware targeting users through fake Starlink applications

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Compromised NPM packages, malicious Rust crates, and poisoned GitHub Actions
- **Ransomware Deployment**: INC ransomware group targeting healthcare infrastructure across Oceania
- **Wiper Malware**: Iranian-linked Handala group deploying destructive malware against medical companies
- **SQL Injection**: Web application attacks targeting WordPress plugin vulnerabilities
- **Tag Poisoning**: GitHub repository compromise through malicious tag manipulation
- **EDR Evasion**: BlackSanta malware specifically designed to disable endpoint detection and response systems
- **Mobile Malware**: BeatBanker Android malware masquerading as legitimate Starlink applications
- **Social Engineering**: Fake app stores and malicious packages targeting developer environments
- **Cloud Environment Compromise**: UNC6426 achieving AWS admin access within 72 hours via NPM supply chain attack
- **Zombie ZIP Technique**: New evasion method to conceal payloads in compressed files

## Threat Actor Activities

- **INC Ransomware Group**: Actively targeting healthcare systems across Australia, New Zealand, and Tonga with ransomware attacks
- **Handala (Iranian-linked)**: Pro-Palestinian hacktivist group claiming responsibility for wiper malware attack against Stryker medical technology company
- **PhantomRaven Campaign**: Ongoing supply chain attacks through 88+ malicious NPM packages targeting JavaScript developers
- **UNC6426**: Sophisticated threat actor leveraging stolen NPM package credentials to achieve complete AWS cloud environment compromise
- **Russian-speaking Actor**: Deploying BlackSanta EDR killer malware targeting HR departments for over a year
- **Sednit (Russian APT)**: Resurfacing with sophisticated new malware toolkit after period of using simple implants
- **Chinese Nexus Actors**: Shifting operational focus to Qatari entities in response to Iranian conflict developments
- **BeatBanker Operators**: Distributing Android malware through fake Starlink applications and counterfeit app stores