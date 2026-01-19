# Exploitation Report

The cybersecurity landscape is facing significant exploitation activity across multiple fronts, with critical vulnerabilities being actively exploited in enterprise systems and AI platforms. Most notably, Fortinet's FortiSIEM platform has come under active attack through a critical command injection vulnerability that was disclosed and immediately exploited. Chinese-linked threat actors are exploiting a zero-day vulnerability in Sitecore to target North American critical infrastructure, while various malicious browser extensions and AI-related security flaws are creating new attack surfaces for threat actors.

## Active Exploitation Details

### FortiSIEM Critical Command Injection Vulnerability
- **Description**: A critical command injection vulnerability affecting Fortinet's FortiSIEM security information and event management platform
- **Impact**: Allows attackers to execute arbitrary commands on vulnerable systems, potentially leading to complete system compromise
- **Status**: Actively exploited by multiple threat actors from various IP addresses following public disclosure
- **CVE ID**: CVE-2025-64155

### Sitecore Zero-Day Vulnerability
- **Description**: A previously unknown vulnerability in Sitecore content management systems being exploited by Chinese-linked advanced persistent threat groups
- **Impact**: Enables unauthorized access to critical infrastructure systems in North America
- **Status**: Active exploitation in the wild targeting critical infrastructure sectors

### Google Gemini Prompt Injection Flaw
- **Description**: A security vulnerability that allows indirect prompt injection attacks to bypass authorization guardrails in Google Gemini
- **Impact**: Attackers can access private Google Calendar data through malicious calendar invites
- **Status**: Disclosed vulnerability affecting Google's AI platform integration with Calendar services

### AMD StackWarp Hardware Vulnerability
- **Description**: A newly disclosed hardware-level vulnerability affecting AMD processors from Zen 1 through Zen 5 architectures
- **Impact**: Breaks AMD SEV-SNP (Secure Encrypted Virtualization-Secure Nested Paging) security protections
- **Status**: Research disclosure affecting multiple generations of AMD CPUs

## Affected Systems and Products

- **FortiSIEM**: Fortinet's security information and event management platform experiencing active exploitation
- **Sitecore CMS**: Content management systems in critical infrastructure environments targeted by APT groups
- **Google Gemini**: AI platform integration with Google Calendar services vulnerable to prompt injection
- **AMD Processors**: Zen 1-5 architecture CPUs affected by hardware-level security bypass
- **Google Chrome**: Browser platform hosting multiple malicious extensions targeting enterprise HR platforms
- **Enterprise HR Platforms**: Workday and NetSuite platforms being impersonated by malicious Chrome extensions
- **StealC Malware Panel**: Information stealer control panels containing cross-site scripting vulnerabilities
- **U.S. Government Systems**: Supreme Court electronic filing system and federal agency networks compromised

## Attack Vectors and Techniques

- **Command Injection**: Critical vulnerability in FortiSIEM allowing arbitrary command execution
- **Prompt Injection**: Indirect manipulation of AI systems to bypass security controls and access sensitive data
- **Malicious Browser Extensions**: Chrome extensions masquerading as productivity tools to steal credentials from enterprise platforms
- **Hardware Exploitation**: Direct targeting of processor-level security features to bypass virtualization protections
- **Social Engineering**: Venezuela-themed spear phishing campaigns targeting U.S. policy entities
- **Malformed Archive Techniques**: GootLoader malware using concatenated ZIP archives (500-1,000 files) to evade detection
- **Cross-Site Scripting**: XSS vulnerabilities in criminal infrastructure allowing security researchers to monitor threat actor operations

## Threat Actor Activities

- **Chinese-Linked APT Groups**: Actively exploiting Sitecore zero-day vulnerabilities to target North American critical infrastructure since at least last year
- **Russian Hacktivist Groups**: Conducting ongoing attacks against UK critical infrastructure and local government organizations as warned by UK authorities
- **Black Basta Ransomware Group**: Leadership identified by Ukrainian and German law enforcement, with key figures added to EU Most Wanted and INTERPOL Red Notice lists
- **KongTuke Campaign**: Operating malicious Chrome extensions that deliberately crash browsers to deliver ModeloRAT malware through fake CrashFix solutions
- **Access Brokers**: Jordanian criminal pleaded guilty to selling access to at least 50 corporate networks
- **GhostPoster Campaign**: Deploying 17 malicious browser extensions across Chrome, Firefox, and Edge with over 840,000 total installations
- **LOTUSLITE Operations**: Targeting U.S. government and policy entities using politically-themed Venezuelan lures to deliver backdoor malware