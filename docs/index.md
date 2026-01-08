# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms with several high-severity vulnerabilities actively being exploited in the wild. CISA has flagged maximum-severity flaws in HPE OneView and Microsoft Office as actively exploited, while attackers are leveraging zero-day vulnerabilities in end-of-life D-Link routers. Additional critical vulnerabilities have been disclosed in n8n workflow automation platform and Coolify self-hosting platform, with some having public proof-of-concept exploits available. Threat actors are also conducting sophisticated campaigns including WhatsApp-based malware distribution, supply chain attacks through malicious npm packages, and SEO poisoning campaigns targeting software downloads.

## Active Exploitation Details

### HPE OneView Maximum Severity Vulnerability
- **Description**: A maximum-severity vulnerability in HPE OneView infrastructure management platform
- **Impact**: Allows attackers to gain unauthorized access and control over infrastructure management systems
- **Status**: Actively exploited in attacks according to CISA's Known Exploited Vulnerabilities catalog

### Microsoft Office Security Flaw
- **Description**: A security vulnerability affecting Microsoft Office applications
- **Impact**: Enables attackers to compromise Office installations and potentially gain system access
- **Status**: Actively exploited in the wild and added to CISA's KEV catalog

### D-Link DSL Router Zero-Day
- **Description**: A critical zero-day vulnerability in end-of-life D-Link DSL routers
- **Impact**: Allows hackers to execute arbitrary commands on affected router systems
- **Status**: Currently being exploited with no patches available for end-of-life devices

### N8N Workflow Automation Critical Vulnerability
- **Description**: A maximum-severity vulnerability dubbed "Ni8mare" in the n8n workflow automation platform
- **Impact**: Enables remote, unauthenticated attackers to take full control of locally deployed n8n instances
- **Status**: CVSS 10.0 severity with potential for complete system compromise

### Cisco Identity Services Engine Vulnerability
- **Description**: A medium-severity security flaw in Cisco ISE and ISE Passive Identity Connector
- **Impact**: Allows attackers with admin privileges to exploit the vulnerability
- **Status**: Patched by Cisco, but public proof-of-concept exploit code is available

### jsPDF Critical Vulnerability
- **Description**: A critical vulnerability in the jsPDF JavaScript library for PDF generation
- **Impact**: Allows attackers to steal sensitive data from the local filesystem through generated PDFs
- **Status**: Critical severity with potential for data exfiltration

## Affected Systems and Products

- **HPE OneView**: Infrastructure management platform with maximum severity vulnerability
- **Microsoft Office**: Various Office applications affected by exploited vulnerability
- **D-Link DSL Routers**: End-of-life router models vulnerable to zero-day exploitation
- **N8N Platform**: Workflow automation platform instances with CVSS 10.0 vulnerability
- **Cisco ISE**: Identity Services Engine and Passive Identity Connector systems
- **Coolify Platform**: Self-hosting platform with 11 critical vulnerabilities enabling server compromise
- **jsPDF Library**: JavaScript PDF generation library used in web applications
- **NPM Packages**: Bitcoin-themed packages containing NodeCordRAT malware
- **WhatsApp Platform**: Used as distribution vector for Astaroth banking trojan

## Attack Vectors and Techniques

- **WhatsApp Auto-Messaging**: Worm spreads Astaroth banking trojan through contact auto-messaging in Brazil
- **Supply Chain Attacks**: Malicious npm packages disguised as Bitcoin-themed utilities deliver NodeCordRAT
- **SEO Poisoning**: Black Cat cybercrime gang uses fraudulent sites advertising popular software
- **Zero-Day Exploitation**: Attackers targeting unpatched end-of-life D-Link routers
- **Credential Theft**: GoBruteforcer botnet targeting cryptocurrency and blockchain project databases
- **Social Engineering**: Office 365 phishing attacks exploiting weak tenant configurations
- **PDF-Based Attacks**: Local file inclusion through malicious PDF generation
- **Infrastructure Compromise**: Direct server takeover through authentication bypass

## Threat Actor Activities

- **Black Cat Cybercrime Gang**: Conducting SEO poisoning campaigns targeting popular software searches with fraudulent download sites
- **UAT-7290 (China-linked)**: Espionage-focused intrusions against South Asia and Southeastern Europe telecommunications using Linux malware and ORB nodes
- **NoName057(16) (Pro-Russian)**: Using DDoSia custom denial-of-service tool to mobilize volunteers for attacks against Ukrainian and Western government, media, and institutional sites
- **Zestix Threat Actor**: Emerging actor conducting vast cloud credential theft using various infostealers to breach file-sharing instances of approximately 50 enterprises
- **Brazilian Campaign Operators**: WhatsApp-based malware distribution targeting Brazilian users with Astaroth banking trojan
- **Cryptocurrency-Focused Attackers**: GoBruteforcer botnet campaigns targeting exposed database servers of crypto and blockchain projects