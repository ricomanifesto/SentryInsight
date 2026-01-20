# Exploitation Report

Current cybersecurity landscapes show significant exploitation activity across multiple attack vectors, with particular focus on browser-based attacks, malicious extensions, AI system vulnerabilities, and critical infrastructure targeting. Notable developments include the active exploitation of FortiSIEM vulnerabilities by threat actors, sophisticated malware campaigns using novel evasion techniques, and targeted attacks against government entities. Russian-aligned hacktivist groups continue aggressive campaigns against UK critical infrastructure, while ransomware operations deploy new malware strains against Fortune 100 companies.

## Active Exploitation Details

### FortiSIEM Command Injection Vulnerability
- **Description**: Critical command injection vulnerability in Fortinet's FortiSIEM platform that allows attackers to execute arbitrary commands
- **Impact**: Complete system compromise and potential lateral movement within network infrastructure
- **Status**: Actively exploited in the wild by multiple threat actors from various IP addresses
- **CVE ID**: CVE-2025-64155

### Google Gemini Prompt Injection Vulnerability
- **Description**: Security flaw allowing indirect prompt injection targeting Google Gemini to bypass authorization guardrails and access Google Calendar data
- **Impact**: Unauthorized access to private calendar information through malicious calendar invites
- **Status**: Disclosed vulnerability with potential for ongoing exploitation through social engineering attacks

### AMD StackWarp Hardware Vulnerability
- **Description**: Hardware flaw affecting AMD Secure Encrypted Virtualization with Secure Nested Paging (SEV-SNP) protections across Zen 1-5 CPU architectures
- **Impact**: Breaks fundamental security protections in virtualized environments, potentially allowing guest-to-host escapes
- **Status**: Newly disclosed vulnerability affecting wide range of AMD processors

## Affected Systems and Products

- **Fortinet FortiSIEM**: Security information and event management platform under active attack
- **Google Gemini AI**: Prompt injection vulnerabilities affecting calendar integration
- **AMD Zen Processors**: Hardware vulnerability affecting Zen 1 through Zen 5 CPU architectures with SEV-SNP features
- **Chrome/Edge Browsers**: Multiple malicious extension campaigns targeting browser security
- **Windows Systems**: Fortune 100 companies affected by PDFSider malware deployment
- **U.S. Government Systems**: Supreme Court filing systems, AmeriCorps, and Department of Veterans Affairs breached
- **Canadian Investment Systems**: CIRO platform breach affecting 750,000 investors
- **Ingram Micro Infrastructure**: Ransomware attack affecting over 42,000 individuals

## Attack Vectors and Techniques

- **Malicious Browser Extensions**: Fake ad blockers (NexShield, CrashFix) designed to crash browsers and deliver ClickFix attacks
- **ClickFix Attack Chain**: Browser crashes followed by social engineering to trick users into executing malicious code
- **Spear Phishing Campaigns**: Venezuela-themed lures targeting U.S. policy entities to deliver LOTUSLITE backdoor
- **ZIP Archive Concatenation**: GootLoader malware using 500-1,000 concatenated ZIP archives to evade detection
- **Prompt Injection**: Indirect attacks against AI systems to bypass security guardrails
- **Social Engineering**: Malicious calendar invites used to trigger prompt injection attacks
- **Extension Impersonation**: Chrome extensions masquerading as legitimate HR and ERP platforms like Workday and NetSuite

## Threat Actor Activities

- **Russian Hacktivist Groups**: Ongoing campaigns against UK critical infrastructure and local government organizations
- **Black Basta Ransomware**: Leadership identified with members added to EU Most Wanted and INTERPOL Red Notice lists
- **Access Brokers**: Jordanian operator sold access to over 50 corporate networks before pleading guilty
- **Supreme Court Hacker**: Tennessee individual breached multiple federal systems including Supreme Court filing system
- **KongTuke Campaign**: Sophisticated operation using malicious Chrome extensions to deliver ModeloRAT through browser crash lures
- **Fortune 100 Attackers**: Ransomware groups targeting major financial sector companies with PDFSider malware
- **StealC Operators**: Information stealer campaigns with compromised control panels exposing threat actor operations