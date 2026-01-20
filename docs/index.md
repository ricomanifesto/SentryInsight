# Exploitation Report

The current cybersecurity landscape reveals several critical exploitation campaigns actively targeting organizations worldwide. Most concerning is the exploitation of a critical command injection vulnerability in Fortinet's FortiSIEM platform, which has come under immediate attack from multiple IP addresses following its disclosure. Additionally, sophisticated malware campaigns are leveraging browser extensions and social engineering techniques, with threat actors deploying advanced evasion methods including the use of concatenated ZIP archives and fake browser crash scenarios to deliver malicious payloads. Hardware vulnerabilities affecting AMD processors and prompt injection attacks targeting AI systems further highlight the diverse attack surface being exploited by cybercriminals.

## Active Exploitation Details

### Critical FortiSIEM Command Injection Vulnerability
- **Description**: A command injection vulnerability in Fortinet's FortiSIEM security information and event management platform
- **Impact**: Allows attackers to execute arbitrary commands on affected systems, potentially leading to full system compromise
- **Status**: Currently being actively exploited by attackers from various IP addresses following recent disclosure
- **CVE ID**: CVE-2025-64155

### StackWarp Hardware Vulnerability
- **Description**: A newly disclosed hardware flaw affecting AMD processors that breaks SEV-SNP (Secure Encrypted Virtualization-Secure Nested Paging) security protections
- **Impact**: Bypasses critical security features designed to protect confidential computing environments and virtualized workloads
- **Status**: Affects AMD Zen 1-5 CPU architectures, exploitation details publicly disclosed

### Google Gemini Prompt Injection Flaw
- **Description**: An indirect prompt injection vulnerability targeting Google Gemini AI that bypasses authorization guardrails through malicious calendar invites
- **Impact**: Unauthorized access to private Google Calendar data and potential exposure of sensitive scheduling information
- **Status**: Security flaw disclosed with exploitation techniques demonstrated

## Affected Systems and Products

- **Fortinet FortiSIEM**: Security information and event management platform affected by critical command injection vulnerability
- **AMD Processors**: Zen 1-5 CPU architectures vulnerable to StackWarp hardware attack
- **Google Chrome Browser**: Targeted by multiple malicious extension campaigns and fake ad-blocker attacks
- **Google Gemini AI**: Susceptible to prompt injection attacks via calendar invitations
- **Microsoft Windows**: Systems affected by shutdown and Cloud PC bugs requiring emergency patches
- **Enterprise HR Platforms**: Workday and NetSuite platforms targeted by credential-stealing browser extensions
- **StealC Malware Panel**: Command and control infrastructure vulnerable to cross-site scripting attacks

## Attack Vectors and Techniques

- **Malicious Browser Extensions**: Fake ad-blockers and productivity tools designed to crash browsers and steal credentials from enterprise platforms
- **ClickFix-Style Attacks**: Browser crash scenarios used as social engineering lures to trick users into executing malicious commands
- **Concatenated ZIP Archives**: GootLoader malware using 500-1,000 concatenated ZIP files to evade security detection systems
- **Hardware-Level Exploits**: Direct attacks against CPU security features in AMD processors
- **Prompt Injection**: Indirect manipulation of AI systems through malicious calendar invitations
- **Ransomware Deployment**: Advanced malware strains like PDFSider being used to deliver ransomware payloads in Fortune 100 companies

## Threat Actor Activities

- **Russian-Aligned Hacktivist Groups**: Conducting ongoing attacks against UK critical infrastructure and local government organizations as warned by UK authorities
- **Black Basta Ransomware Group**: Russia-linked ransomware-as-a-service operation with leadership now on EU Most Wanted and INTERPOL Red Notice lists
- **KongTuke Campaign**: Ongoing operation using CrashFix Chrome extension to deliver ModeloRAT malware through browser crash lures
- **Access Brokers**: Criminal operators selling unauthorized access to corporate networks, with recent cases involving access to over 50 company networks
- **Enterprise Infiltration**: Sophisticated threat actors targeting Fortune 100 financial sector companies with custom malware strains like PDFSider