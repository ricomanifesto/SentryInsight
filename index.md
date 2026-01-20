# Exploitation Report

Current exploitation activity reveals a critical landscape dominated by several significant security incidents. A critical command injection vulnerability in Fortinet's FortiSIEM platform is being actively exploited in the wild, while sophisticated malware campaigns are targeting enterprise systems through various attack vectors. The Google Gemini AI assistant has been compromised through prompt injection attacks that bypass authorization controls to access private calendar data. New hardware vulnerabilities affect AMD processors across multiple CPU generations, and multiple malicious browser extension campaigns are stealing credentials from enterprise platforms. Ransomware operations continue to impact major organizations, with new malware strains like PDFSider being deployed against Fortune 100 companies.

## Active Exploitation Details

### Fortinet FortiSIEM Command Injection Vulnerability
- **Description**: Critical command injection vulnerability in Fortinet's FortiSIEM platform that allows remote code execution
- **Impact**: Attackers can execute arbitrary commands on vulnerable systems, potentially leading to complete system compromise
- **Status**: Currently being exploited in the wild from various IP addresses shortly after public disclosure
- **CVE ID**: CVE-2025-64155

### Google Gemini Prompt Injection Vulnerability
- **Description**: Security flaw that leverages indirect prompt injection targeting Google Gemini to bypass authorization guardrails
- **Impact**: Attackers can access private Google Calendar data through malicious calendar invites
- **Status**: Disclosed vulnerability that bypasses AI authorization controls

### AMD StackWarp Hardware Vulnerability
- **Description**: Hardware vulnerability affecting AMD processors that breaks SEV-SNP (Secure Encrypted Virtualization-Secure Nested Paging) protections
- **Impact**: Compromises hardware-level security protections on affected AMD processors
- **Status**: Newly disclosed hardware flaw affecting multiple CPU generations

### StealC Malware Panel XSS Vulnerability
- **Description**: Cross-site scripting vulnerability in the web-based control panel used by StealC information stealer operators
- **Impact**: Allows security researchers to spy on threat actor operations and gather intelligence
- **Status**: Exploited by researchers for threat intelligence gathering

## Affected Systems and Products

- **Fortinet FortiSIEM**: Security information and event management platform vulnerable to command injection attacks
- **Google Gemini AI**: AI assistant vulnerable to prompt injection attacks affecting calendar access
- **AMD Processors**: Zen 1-5 CPU generations affected by StackWarp hardware vulnerability
- **Google Chrome Extensions**: Multiple malicious extensions targeting enterprise HR and ERP platforms
- **Enterprise HR Platforms**: Workday and NetSuite platforms targeted by credential-stealing browser extensions
- **Windows Systems**: Fortune 100 finance company networks compromised with PDFSider malware
- **U.S. Government Systems**: Supreme Court electronic filing system, AmeriCorps, and Department of Veterans Affairs breached

## Attack Vectors and Techniques

- **Command Injection**: Exploitation of FortiSIEM vulnerability to execute arbitrary commands
- **Prompt Injection**: Indirect manipulation of AI systems to bypass security controls
- **Malicious Browser Extensions**: Chrome extensions masquerading as productivity tools to steal credentials
- **Hardware Exploitation**: StackWarp technique targeting AMD processor security features
- **Spear Phishing**: Venezuela-themed lures delivering LOTUSLITE backdoor to policy entities
- **ZIP Archive Concatenation**: GootLoader malware using 500-1,000 concatenated ZIP files for evasion
- **Social Engineering**: CrashFix extension deliberately crashing browsers to trick users into installation

## Threat Actor Activities

- **Black Basta Ransomware Group**: Russia-linked RaaS operation with leadership added to EU Most Wanted and INTERPOL Red Notice lists
- **Russian Hacktivist Groups**: Ongoing attacks against UK critical infrastructure and local government organizations
- **KongTuke Campaign**: Operation using malicious Chrome extensions to deliver ModeloRAT malware
- **GhostPoster Campaign**: 17 malicious browser extensions with 840,000 total installations across Chrome, Firefox, and Edge
- **Access Brokers**: Jordanian individual selling access to at least 50 corporate networks
- **LOTUSLITE Operators**: Targeting U.S. government and policy entities with politically themed spear phishing campaigns
- **Fortune 100 Attackers**: Ransomware group deploying new PDFSider malware strain against major financial institutions