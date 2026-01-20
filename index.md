# Exploitation Report

Current cybersecurity landscape reveals significant active exploitation activity across multiple attack vectors. Critical vulnerabilities are being exploited in Fortinet's FortiSIEM platform (CVE-2025-64155), while sophisticated malware campaigns deploy fake browser extensions and novel hardware vulnerabilities target AMD processors. Ransomware operations continue targeting major enterprises, with new malware strains like PDFSider being deployed against Fortune 100 companies. Social engineering attacks have evolved with ClickFix-style campaigns using fake ad blockers, while threat actors exploit AI platform vulnerabilities to bypass security controls and access private data.

## Active Exploitation Details

### FortiSIEM Command Injection Vulnerability
- **Description**: A critical command injection vulnerability in Fortinet's FortiSIEM platform that allows attackers to execute arbitrary commands on the system
- **Impact**: Attackers can gain unauthorized access to security information and event management systems, potentially compromising entire network monitoring infrastructure
- **Status**: Actively exploited by multiple attackers from various IP addresses shortly after disclosure
- **CVE ID**: CVE-2025-64155

### StackWarp AMD Hardware Vulnerability
- **Description**: A hardware vulnerability affecting AMD processors that breaks SEV-SNP (Secure Encrypted Virtualization-Secure Nested Paging) protections
- **Impact**: Allows attackers to bypass hardware-level security protections on virtualized environments, potentially exposing sensitive data in secure enclaves
- **Status**: Affects AMD Zen 1-5 CPU architectures, recently disclosed by academic researchers

### Cloudflare ACME Validation Bypass
- **Description**: A security flaw in Cloudflare's Automatic Certificate Management Environment validation logic that allows bypassing Web Application Firewall controls
- **Impact**: Attackers can access origin servers directly, circumventing WAF protections and potentially reaching vulnerable backend systems
- **Status**: Recently patched by Cloudflare

### Google Gemini Prompt Injection
- **Description**: An indirect prompt injection vulnerability targeting Google Gemini that bypasses authorization guardrails through malicious calendar invites
- **Impact**: Enables unauthorized access to private Google Calendar data by manipulating AI prompts through calendar event descriptions
- **Status**: Allows attackers to extract sensitive calendar information through crafted invitations

## Affected Systems and Products

- **Fortinet FortiSIEM**: Security information and event management platform vulnerable to command injection attacks
- **AMD Zen Processors**: Zen 1-5 CPU architectures affected by StackWarp hardware vulnerability impacting SEV-SNP protections
- **Cloudflare Services**: ACME validation logic allowing WAF bypass to origin servers
- **Google Gemini**: AI assistant vulnerable to prompt injection through calendar integration
- **Chrome/Edge Browsers**: Targeted by malicious extensions including NexShield fake ad blocker and credential-stealing HR platform tools
- **Windows Systems**: Affected by PDFSider malware deployment and various browser-based attacks
- **StealC Malware Panel**: Command and control infrastructure vulnerable to cross-site scripting attacks

## Attack Vectors and Techniques

- **Malicious Browser Extensions**: Fake ad blockers like NexShield that intentionally crash browsers to facilitate ClickFix social engineering attacks
- **ClickFix Campaign Techniques**: Browser crash manipulation followed by social engineering to trick users into executing malicious commands
- **ZIP Archive Concatenation**: GootLoader malware uses 500-1,000 concatenated ZIP archives to evade detection systems
- **Hardware-Level Exploitation**: StackWarp attacks targeting AMD processor security features in virtualized environments
- **Prompt Injection**: Indirect manipulation of AI systems through malicious calendar invites and crafted prompts
- **Command Injection**: Direct exploitation of input validation flaws in enterprise security management platforms
- **Credential Harvesting**: Malicious Chrome extensions masquerading as productivity tools for HR and ERP platforms

## Threat Actor Activities

- **KongTuke Campaign**: Ongoing operation using CrashFix Chrome extension to deliver ModeloRAT malware through fake ad blocker installations
- **Russian Hacktivist Groups**: Continued targeting of UK critical infrastructure and local government organizations in disruptive attacks
- **Black Basta Ransomware**: Leadership identified by Ukrainian and German authorities, with group added to EU Most Wanted and INTERPOL Red Notice
- **Access Brokers**: Jordanian national pleaded guilty to selling network access to at least 50 corporate networks
- **Fortune 100 Targeting**: Ransomware attackers deploying new PDFSider malware strain against major financial sector companies
- **Supreme Court Hacker**: Tennessee individual admitted to breaching U.S. Supreme Court filing system and multiple federal agencies including AmeriCorps and Veterans Affairs
- **Enterprise Data Breaches**: Multiple incidents including Ingram Micro ransomware attack affecting 42,000 individuals and CIRO breach exposing 750,000 Canadian investors