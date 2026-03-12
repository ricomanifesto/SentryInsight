# Exploitation Report

The cybersecurity landscape is currently dominated by several critical exploitation activities affecting enterprise systems, cloud environments, and developer toolchains. Most notably, CISA has ordered federal agencies to patch an actively exploited n8n workflow automation vulnerability that allows remote code execution, while threat actors continue to leverage supply chain compromises through malicious NPM packages and GitHub Action poisoning. Healthcare sectors in Oceania face ongoing ransomware attacks from the INC group, and Iranian-linked actors have launched wiper attacks against major medical technology firms. Additionally, Microsoft's March Patch Tuesday addressed two publicly disclosed zero-day vulnerabilities alongside numerous other critical flaws.

## Active Exploitation Details

### n8n Workflow Automation RCE Vulnerability
- **Description**: Critical remote code execution flaw in the n8n workflow automation platform that allows arbitrary command execution
- **Impact**: Attackers can execute arbitrary commands on affected systems and potentially access stored credentials
- **Status**: Actively exploited in attacks; CISA has ordered federal agencies to patch immediately

### Microsoft Zero-Day Vulnerabilities
- **Description**: Two publicly disclosed zero-day vulnerabilities in Microsoft products addressed in March 2026 Patch Tuesday
- **Impact**: Publicly known vulnerabilities that could be exploited before patches are applied
- **Status**: Recently patched but were publicly disclosed before fixes were available

### Xygeni GitHub Action Tag Poisoning
- **Description**: Supply chain compromise of the xygeni/xygeni-action GitHub Action through tag poisoning attack
- **Impact**: Attackers operated an active command and control implant for up to a week, potentially compromising CI/CD pipelines
- **Status**: AppSec vendor Xygeni's GitHub Action was compromised and used maliciously

## Affected Systems and Products

- **n8n Workflow Automation Platform**: Critical RCE vulnerability affecting workflow automation systems
- **Microsoft Windows**: 79 security flaws addressed in March 2026 Patch Tuesday, including 2 zero-days
- **WordPress Elementor Ally Plugin**: SQL injection vulnerability affecting 250,000+ installations
- **HPE Aruba Networking AOS-CX**: Critical authentication bypass allowing admin password resets
- **SAP Enterprise Software**: Two critical vulnerabilities enabling arbitrary code execution
- **GitHub Actions**: Supply chain compromise through tag poisoning of security vendor tools
- **NPM Registry**: Multiple waves of malicious packages targeting JavaScript developers
- **Rust Crates Registry**: Five malicious crates masquerading as time utilities to steal secrets

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Malicious NPM packages and compromised GitHub Actions targeting developer environments
- **Tag Poisoning**: Manipulation of version control tags to serve malicious code through legitimate repositories
- **SQL Injection**: Database attacks targeting WordPress plugins with over 250,000 installations
- **Remote Code Execution**: Critical vulnerabilities in enterprise automation platforms allowing arbitrary command execution
- **Wiper Malware**: Destructive attacks targeting medical technology infrastructure
- **EDR Evasion**: New "BlackSanta" EDR killer malware targeting HR departments
- **Zombie ZIP Technique**: Payload concealment method designed to bypass security solutions
- **CI/CD Pipeline Exploitation**: Malicious crates and AI bots targeting development environments

## Threat Actor Activities

- **INC Ransomware Group**: Actively targeting healthcare organizations across Australia, New Zealand, and Tonga with ransomware attacks
- **Handala (Iranian-linked)**: Pro-Palestinian hacktivist group claimed responsibility for wiper malware attack against medical technology giant Stryker
- **UNC6426**: Leveraged stolen keys from nx NPM supply chain compromise to achieve AWS admin access within 72 hours
- **PhantomRaven Campaign**: Ongoing supply chain attacks distributing 88 malicious NPM packages to steal developer data
- **Chinese Nexus Actors**: Shifted targeting focus to Qatar entities in response to geopolitical events involving Iranian conflict
- **Russian-speaking Threat Actor**: Operating BlackSanta EDR killer targeting HR departments for over a year
- **Sednit (Russian APT)**: Resurfaced with sophisticated new malware toolkit after years of using simpler implants