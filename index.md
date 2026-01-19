# Exploitation Report

Critical exploitation activity is currently targeting enterprise infrastructure through multiple attack vectors. China-linked threat actors have been actively exploiting zero-day vulnerabilities in Cisco Secure Email Gateways and Sitecore systems to gain initial access to North American critical infrastructure. Additionally, a new hardware vulnerability called StackWarp has been discovered affecting AMD processors, while malicious browser extensions continue to proliferate across Chrome, Firefox, and Edge stores, targeting enterprise HR platforms and accumulating hundreds of thousands of installations. Fortinet systems face ongoing exploitation of a critical command injection vulnerability in FortiSIEM products.

## Active Exploitation Details

### Cisco AsyncOS Zero-Day Vulnerability
- **Description**: A maximum-severity remote code execution vulnerability in Cisco AsyncOS Software for Cisco Secure Email Gateway and Cisco Secure Email and Web Manager
- **Impact**: Allows attackers to achieve complete system compromise and remote code execution
- **Status**: Recently patched by Cisco after being actively exploited by China-linked APT groups
- **CVE ID**: CVE-2025-64155

### Sitecore Zero-Day Vulnerability
- **Description**: An unknown zero-day vulnerability in Sitecore content management systems
- **Impact**: Provides initial access for threat actors to infiltrate critical infrastructure networks
- **Status**: Actively exploited by China-linked threat actor UAT-8837 targeting North American critical infrastructure

### FortiSIEM Command Injection Vulnerability
- **Description**: A critical command injection vulnerability in Fortinet FortiSIEM products
- **Impact**: Enables attackers to execute arbitrary commands on affected systems
- **Status**: Currently under active exploitation from various IP addresses following recent disclosure
- **CVE ID**: CVE-2025-64155

### StackWarp Hardware Vulnerability
- **Description**: A hardware flaw affecting AMD processors that breaks SEV-SNP (Secure Encrypted Virtualization-Secure Nested Paging) security protections
- **Impact**: Compromises confidential computing protections and allows attackers to bypass hardware-level security features
- **Status**: Newly disclosed vulnerability affecting AMD Zen 1-5 CPUs

## Affected Systems and Products

- **Cisco Secure Email Gateway**: AsyncOS Software vulnerable to remote code execution
- **Cisco Secure Email and Web Manager**: AsyncOS Software affected by critical vulnerability
- **Fortinet FortiSIEM**: Command injection vulnerability enabling system compromise
- **AMD Processors**: Zen 1, 2, 3, 4, and 5 architectures affected by StackWarp hardware flaw
- **Sitecore CMS**: Zero-day vulnerability exploited for initial access
- **Chrome Web Store**: Multiple malicious extensions targeting HR platforms like Workday and NetSuite
- **Firefox and Edge Stores**: GhostPoster campaign extensions with 840,000 total installations
- **StealC Malware Panels**: Cross-site scripting vulnerability in control panels

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: China-linked APTs leveraging unknown vulnerabilities in Sitecore and Cisco systems for initial access
- **Malicious Browser Extensions**: Credential-stealing extensions masquerading as productivity tools for enterprise platforms
- **Hardware-Level Attacks**: StackWarp vulnerability exploiting AMD processor architecture to bypass security protections
- **Command Injection**: FortiSIEM exploitation enabling arbitrary command execution
- **Social Engineering**: KongTuke campaign using fake Chrome extensions with browser crash lures to deliver ModeloRAT
- **Evasion Techniques**: GootLoader malware using 500-1,000 concatenated ZIP archives to avoid detection
- **Spear Phishing**: LOTUSLITE backdoor campaigns using Venezuela-themed lures targeting U.S. policy entities

## Threat Actor Activities

- **UAT-8837 (China-linked)**: Focusing on North American critical infrastructure, exploiting both known and zero-day vulnerabilities in Sitecore systems
- **China-linked APT Groups**: Actively exploiting Cisco Secure Email Gateway zero-days for enterprise infiltration
- **KongTuke Campaign Operators**: Distributing ModeloRAT through malicious Chrome extensions using ClickFix-style browser crash social engineering
- **GhostPoster Campaign**: Deploying 17 malicious extensions across Chrome, Firefox, and Edge with 840,000 combined installations
- **Black Basta Ransomware**: Leadership identified by Ukrainian and German law enforcement, with leader added to EU Most Wanted and INTERPOL Red Notice lists
- **StealC Malware Operators**: Running information-stealing operations with vulnerable web-based control panels
- **LOTUSLITE Campaign**: Targeting U.S. government and policy entities using politically themed spear phishing emails