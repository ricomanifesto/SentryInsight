# Exploitation Report

Current cybersecurity threats demonstrate a concerning escalation in sophisticated attack techniques across multiple vectors. Critical exploitation activity includes active attacks on Fortinet FortiSIEM systems through command injection vulnerabilities, malicious Chrome extension campaigns targeting enterprise platforms, and advanced malware deployment strategies. Notable incidents include hardware-level vulnerabilities affecting AMD processors, AI platform security flaws, and coordinated ransomware operations targeting Fortune 100 companies. Russian-aligned hacktivist groups continue targeting UK critical infrastructure, while threat actors are increasingly leveraging legitimate platforms for malicious activities.

## Active Exploitation Details

### Fortinet FortiSIEM Command Injection Vulnerability
- **Description**: A critical command injection vulnerability in Fortinet's FortiSIEM platform that allows attackers to execute arbitrary commands on affected systems
- **Impact**: Complete system compromise, unauthorized access to security information and event management infrastructure
- **Status**: Currently being actively exploited from various IP addresses following disclosure
- **CVE ID**: CVE-2025-64155

### Google Gemini Prompt Injection Flaw
- **Description**: Security vulnerability that leverages indirect prompt injection to bypass authorization guardrails in Google Gemini and access private Google Calendar data
- **Impact**: Exposure of private calendar information through malicious calendar invites, bypassing security controls
- **Status**: Disclosed vulnerability affecting Google's AI platform integration

### StackWarp Hardware Vulnerability
- **Description**: Hardware-level vulnerability affecting AMD processors that breaks AMD SEV-SNP (Secure Encrypted Virtualization - Secure Nested Paging) security protections
- **Impact**: Compromise of confidential computing environments and virtualization security boundaries
- **Status**: Affects AMD Zen 1-5 CPU architectures, fundamental hardware flaw

### StealC Malware Panel XSS Vulnerability
- **Description**: Cross-site scripting vulnerability in the web-based control panel used by StealC information stealer operators
- **Impact**: Allows researchers and potentially other threat actors to gather intelligence on criminal operations
- **Status**: Actively exploitable vulnerability in cybercriminal infrastructure

## Affected Systems and Products

- **Fortinet FortiSIEM**: Security information and event management platform with critical command injection vulnerability
- **AMD Processors**: Zen 1-5 CPU architectures affected by StackWarp hardware vulnerability
- **Google Chrome Extensions**: Multiple malicious extensions targeting Workday, NetSuite, and other enterprise platforms
- **Google Gemini**: AI platform vulnerable to prompt injection attacks affecting calendar data
- **Windows Systems**: Targeted by PDFSider malware and various malicious Chrome extensions
- **U.S. Supreme Court Systems**: Electronic filing system compromised in previous attack
- **Ingram Micro Infrastructure**: IT systems affected by ransomware attack impacting 42,000 individuals
- **Canadian Investment Regulatory Organization (CIRO)**: Systems breached affecting 750,000 investors

## Attack Vectors and Techniques

- **Malicious Browser Extensions**: Fake ad blockers and enterprise platform impersonators used to crash browsers and deploy malware
- **ClickFix-Style Attacks**: Browser crash techniques followed by social engineering to trick users into running malicious PowerShell commands
- **Spear Phishing**: Venezuela-themed lures targeting U.S. policy entities to deliver LOTUSLITE backdoor
- **ZIP Archive Concatenation**: GootLoader malware uses 500-1,000 concatenated ZIP archives to evade detection
- **Hardware Exploitation**: StackWarp attacks targeting AMD processor security features
- **Prompt Injection**: Indirect prompt injection targeting AI platforms to bypass security controls
- **Ransomware Deployment**: PDFSider malware used by ransomware groups on Fortune 100 networks

## Threat Actor Activities

- **Black Basta Ransomware Group**: Leader added to EU Most Wanted and INTERPOL Red Notice, continues operations with identified Ukrainian operatives
- **Russian Hacktivist Groups**: Ongoing attacks against UK critical infrastructure and local government organizations
- **KongTuke Campaign**: Operators using CrashFix Chrome extension to deliver ModeloRAT malware
- **Access Brokers**: Jordanian national pleaded guilty to selling access to 50+ corporate networks
- **Supreme Court Attacker**: Tennessee man admitted to hacking U.S. Supreme Court filing system and federal agencies
- **GootLoader Operators**: Enhanced evasion techniques using malformed ZIP archives
- **Enterprise Platform Impersonators**: Threat actors creating fake HR and ERP platform extensions for account hijacking