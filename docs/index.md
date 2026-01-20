# Exploitation Report

Current threat landscape analysis reveals several critical security incidents involving sophisticated malware campaigns, browser-based attacks, and infrastructure vulnerabilities. Key exploitation activities include a critical FortiSIEM command injection vulnerability being actively exploited, malicious Chrome extensions targeting enterprise platforms, advanced malware loaders using evasion techniques, and hardware vulnerabilities affecting AMD processors. Notable ransomware operations continue targeting Fortune 100 companies while Russian hacktivist groups maintain pressure on UK infrastructure.

## Active Exploitation Details

### Critical FortiSIEM Command Injection Vulnerability
- **Description**: Command injection vulnerability in Fortinet's FortiSIEM platform that allows attackers to execute arbitrary commands
- **Impact**: Unauthorized command execution on affected FortiSIEM systems, potential for complete system compromise
- **Status**: Currently under active exploitation from multiple IP addresses, patch available
- **CVE ID**: CVE-2025-64155

### Google Gemini Prompt Injection Vulnerability
- **Description**: Security flaw leveraging indirect prompt injection targeting Google Gemini to bypass authorization guardrails
- **Impact**: Unauthorized access to private Google Calendar data through malicious calendar invites
- **Status**: Disclosed vulnerability affecting Google's AI platform, allowing data exposure

### AMD StackWarp Hardware Vulnerability
- **Description**: Hardware flaw affecting AMD processors that breaks SEV-SNP (Secure Encrypted Virtualization) protections
- **Impact**: Compromise of secure virtualization environments and confidential computing protections
- **Status**: Newly disclosed vulnerability affecting Zen 1-5 CPU architectures

### StealC Malware Panel Cross-Site Scripting Vulnerability
- **Description**: XSS vulnerability in the web-based control panel used by StealC information stealer operators
- **Impact**: Allowed security researchers to spy on threat actor operations and gather intelligence
- **Status**: Vulnerability in criminal infrastructure exposed operator activities

## Affected Systems and Products

- **FortiSIEM**: Security information and event management platform with critical command injection vulnerability
- **Google Gemini**: AI platform vulnerable to prompt injection attacks affecting calendar data access
- **AMD Zen CPUs**: Zen 1-5 architecture processors affected by StackWarp hardware vulnerability compromising SEV-SNP
- **Google Chrome**: Browser targeted by multiple malicious extensions and fake ad blockers
- **Enterprise HR/ERP Platforms**: Workday and NetSuite targeted by credential-stealing Chrome extensions
- **Windows Systems**: Affected by PDFSider malware and requiring emergency out-of-band updates
- **Supreme Court Electronic Filing System**: Breached and data leaked on social media platforms
- **Ingram Micro Systems**: IT giant affected by ransomware attack impacting 42,000 individuals

## Attack Vectors and Techniques

- **Browser Extension Hijacking**: Malicious Chrome extensions masquerading as legitimate productivity tools targeting HR and ERP platforms
- **ClickFix Browser Attacks**: Fake ad-blocker extensions deliberately crashing browsers to prepare for ClickFix-style social engineering attacks
- **Malware Evasion**: GootLoader using 500-1,000 concatenated ZIP archives to evade security detection systems
- **Prompt Injection**: Indirect prompt injection attacks against AI systems to bypass security controls
- **Hardware-Level Attacks**: Exploitation of CPU-level vulnerabilities to break virtualization security boundaries
- **Social Engineering**: Browser crash scenarios designed to trick users into executing malicious code
- **Access Brokerage**: Criminal networks selling access to compromised corporate networks

## Threat Actor Activities

- **KongTuke Campaign**: Ongoing operation deploying malicious Chrome extensions and ModeloRAT malware through fake ad blockers
- **Russian Hacktivist Groups**: Continued targeting of UK critical infrastructure and local government organizations
- **Black Basta Ransomware**: Leadership identified and added to EU Most Wanted and INTERPOL Red Notice lists
- **PDFSider Operators**: Ransomware attackers targeting Fortune 100 finance sector companies with new malware strains
- **Access Brokers**: Jordanian national operating network providing access to 50+ corporate networks
- **StealC Operators**: Information stealer campaign operators exposed through panel vulnerability
- **Supreme Court Attacker**: Tennessee individual conducting multi-agency breaches including AmeriCorps and VA systems