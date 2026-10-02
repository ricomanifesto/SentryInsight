---
schema_version: 2
report_date: 2026-10-02
generated_at: 2026-10-02T06:34:42Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-10-02/
---
# Exploitation Report

## Executive Summary

Critical zero-day exploitation activity dominates the current threat landscape, with CISA adding two actively exploited vulnerabilities to its Known Exploited Vulnerabilities catalog within days of each other. Fortinet FortiMail CVE-2026-104286 (CVSS 9.8) and Cisco Catalyst SD-WAN Manager CVE-2026-76504 (CVSS 9.8) are both being exploited in the wild as unauthenticated, remote attack vectors allowing arbitrary file writes and authentication bypass respectively. Both carry maximum severity ratings and require immediate patching.

Simultaneously, threat actors are weaponizing recently patched flaws and novel AI-driven techniques. The Zimbra Collaboration Suite flaw CVE-2026-73570 (CVSS 8.9) has been actively exploited to deploy web shells and harvest authentication secrets despite available patches. A proof-of-concept for Apple CoreGraphics CVE-2026-86950 has emerged, with Apple indicating it may have been used in targeted attacks. The Dutch Institute for Vulnerability Disclosure confirmed a breach enabled by a chain of two zero-days in Zammad, while Bitget suffered a $387.5 million cryptocurrency theft via a third-party security product zero-day.

Law enforcement achieved significant disruption against the KillSec ransomware operation, arresting a suspected 16-year-old administrator and seizing infrastructure in Operation KillSwitch. Russian state actor Star Blizzard has adopted a new "RedFlick" technique to deploy CosmicPulse backdoors. Chinese threat actor Warlock Ransomware targets Spanish and Portuguese organizations, while Moonshot AI associates conducted a reasoning extraction campaign against OpenAI models. Over 543,000 valid credentials remain exposed in public GitHub repositories, and malicious Custom GPTs are being used for ClickFix-style RAT delivery.

## Active Exploitation Details

### FortiMail Unauthenticated Arbitrary File Write
- **Description**: A critical zero-day vulnerability in Fortinet FortiMail allowing unauthenticated attackers to write arbitrary files on the underlying system, leading to remote code execution. The flaw stems from improper validation of file upload parameters.
- **Impact**: Attackers can achieve unauthenticated remote code execution on vulnerable FortiMail appliances, enabling full system compromise, lateral movement, and data exfiltration.
- **Status**: Actively exploited in zero-day attacks. Fortinet has released patches. CISA added to KEV catalog on October 2026.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-104286
- **Reporting**: [The Hacker News — Critical FortiMail Zero-Day Flaw Exploited in Attacks Allows Unauthenticated Arbitrary File Writes](https://thehackernews.com/2026/10/critical-fortimail-zero-day-flaw.html), [Bleeping Computer — Fortinet warns of critical FortiMail flaw exploited in zero-day attacks](https://www.bleepingcomputer.com/news/security/fortinet-warns-of-critical-fortimail-flaw-exploited-in-zero-day-attacks/)

### Cisco Catalyst SD-WAN Manager Authentication Bypass
- **Description**: A critical authentication bypass vulnerability in Cisco Catalyst SD-WAN Manager that allows an unauthenticated, remote attacker to access an affected system with elevated privileges. The flaw enables bypassing authentication controls entirely.
- **Impact**: Unauthenticated remote attackers can gain administrative access to SD-WAN Manager, potentially compromising the entire SD-WAN fabric, manipulating network traffic, and pivoting to connected systems.
- **Status**: Actively exploited in the wild. CISA added to KEV catalog. Patches available from Cisco.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-76504
- **Reporting**: [The Hacker News — CISA Adds Exploited Cisco Catalyst SD-WAN Manager Auth Bypass to KEV](https://thehackernews.com/2026/10/cisa-adds-exploited-cisco-catalyst-sd.html)

### Zimbra Collaboration Suite Command Injection
- **Description**: An unauthenticated operating system command injection flaw in Zimbra Collaboration Suite (ZCS) that can lead to remote code execution when Simple Network Management Protocol (SNMP) is enabled. The vulnerability allows attackers to inject arbitrary commands via crafted SNMP requests.
- **Impact**: Attackers deploy web shells, access mailbox data, harvest authentication secrets, and maintain persistent access to compromised email servers.
- **Status**: Now patched but actively exploited in the wild. Microsoft Security Research team observed weaponization. CVE-2026-73570 patched by Zimbra.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-73570
- **Reporting**: [The Hacker News — Attackers Exploit Zimbra Flaw to Deploy Web Shells and Harvest Authentication Secrets](https://thehackernews.com/2026/09/attackers-exploit-zimbra-flaw-to-deploy.html)

### Apple CoreGraphics PDF Font Parsing Flaw
- **Description**: A memory corruption vulnerability in Apple CoreGraphics triggered by a malicious PDF with a crafted embedded font. The flaw causes crashes on unpatched iPhones and Macs. Apple has indicated it may have been used in attacks against specific targeted individuals.
- **Impact**: Memory corruption leading to application crashes; potential for remote code execution if memory corruption can be weaponized beyond denial-of-service. Targeted attacks against specific individuals reported.
- **Status**: Proof-of-concept published. Apple acknowledges possible exploitation in targeted attacks. Patch status not explicitly stated in source.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: patch
- **CVE IDs**: CVE-2026-86950
- **Reporting**: [The Hacker News — Apple CoreGraphics PoC Emerges as WhatsApp PDF Checks Hint at Possible Delivery Path](https://thehackernews.com/2026/10/apple-coregraphics-poc-emerges-as.html)

### Zammad Ticketing System Zero-Day Chain
- **Description**: A chain of two zero-day vulnerabilities in the open-source Zammad ticketing system that enabled a network breach of the Dutch Institute for Vulnerability Disclosure (DIVD). The vulnerabilities were exploited in sequence to achieve initial access and privilege escalation.
- **Impact**: Full network breach of a vulnerability disclosure organization, demonstrating the risk of chained zero-days in internet-facing ticketing systems.
- **Status**: Two zero-days actively exploited in a real-world breach. DIVD disclosed the incident. Patch status not specified in source.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — DIVD says Zammad zero-days enabled AI-driven network breach](https://www.bleepingcomputer.com/news/security/divd-says-zammad-zero-days-enabled-ai-driven-network-breach/)

### Citrix NetScaler Pre-Authentication Command Injection
- **Description**: A critical pre-authentication command injection vulnerability in Citrix NetScaler ADC and NetScaler Gateway. Threat actors exploit this to drop web shells and attempt theft of configuration data.
- **Impact**: Attackers create superuser accounts, deploy web shells mapped to CSS-like URLs for stealth, and exfiltrate configuration data including certificates and keys.
- **Status**: Actively exploited across multiple customer environments. LevelBlue THOR team analyzed post-exploitation activity. Patch availability not explicitly stated.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Citrix NetScaler Post-Exploitation Payload Creates Superuser, Maps Web Shell to CSS-Like URLs](https://thehackernews.com/2026/10/citrix-netscaler-post-exploitation.html)

### Kiteworks Email Protection Gateway Code Injection
- **Description**: A maximum-severity code injection vulnerability affecting Kiteworks Email Protection Gateway (EPG), part of 126 vulnerabilities patched in a security update release.
- **Impact**: Code injection in the email protection gateway could allow attackers to execute arbitrary code in the context of the gateway process, potentially compromising email security inspection and filtering.
- **Status**: Patched in security updates addressing 126 total vulnerabilities. Exploitation status not explicitly confirmed in source.
- **Severity**: critical
- **Exploitation Status**: unknown
- **Action**: patch
- **Reporting**: [Bleeping Computer — Kiteworks patches max severity code injection vulnerability](https://www.bleepingcomputer.com/news/security/kiteworks-patches-max-severity-email-protection-gateway-code-injection-vulnerability/)

### Bitget Third-Party Security Product Zero-Day
- **Description**: A zero-day vulnerability in third-party security products exploited to steal $387.5 million in cryptocurrency from Bitget exchange. SlowMist investigation identified malicious activity and recovered a customized attacker tool.
- **Impact**: Massive cryptocurrency theft ($387.5M) via exploitation of a zero-day in security products trusted by the exchange. Custom tooling indicates sophisticated, targeted operation.
- **Status**: Actively exploited in a high-value theft. Investigation ongoing by SlowMist. Third-party vendor and specific product not publicly named.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Bitget Confirms Third-Party Zero-Day Behind $387.5 Million Cryptocurrency Theft](https://thehackernews.com/2026/10/bitget-confirms-third-party-zero-day.html)

### MetaMask Infrastructure Security Incident
- **Description**: An ongoing security incident affecting MetaMask infrastructure, prompting exit of affected Ethereum validators. MetaMask coordinates with external partners and security advisors for remediation.
- **Impact**: Infrastructure compromise affecting validator operations. MetaMask states no immediate threat to user wallets, but validator exits indicate operational disruption.
- **Status**: Ongoing incident under active remediation. Root cause and exploitation vector not disclosed.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Metamask discloses security incident affecting its infrastructure](https://www.bleepingcomputer.com/news/security/metamask-discloses-security-incident-affecting-its-infrastructure/), [The Hacker News — MetaMask Security Incident Prompts Exit of Affected Ethereum Validators](https://thehackernews.com/2026/10/metamask-security-incident-prompts-exit.html)

## Affected Systems and Products

- **Fortinet FortiMail**: All versions prior to patched releases. Appliance and virtual appliance deployments. Email security gateway platforms.
- **Cisco Catalyst SD-WAN Manager**: Vulnerable versions of the SD-WAN management platform. Centralized controllers for Cisco SD-WAN fabric.
- **Zimbra Collaboration Suite (ZCS)**: Versions with SNMP enabled prior to patch release. On-premises email and collaboration deployments.
- **Apple CoreGraphics**: iOS, iPadOS, macOS devices processing malicious PDFs with crafted embedded fonts. iPhones, iPads, Macs.
- **Zammad Ticketing System**: Open-source Zammad installations. Internet-facing helpdesk/ticketing platforms.
- **Citrix NetScaler ADC and NetScaler Gateway**: Application delivery controllers and secure remote access gateways. Pre-authentication attack surface.
- **Kiteworks Email Protection Gateway (EPG)**: Secure email gateway appliances and virtual deployments. Part of Kiteworks secure file sharing platform.
- **Third-party security products (unnamed)**: Security tooling used by Bitget cryptocurrency exchange. Specific vendor/product withheld pending investigation.
- **MetaMask Infrastructure**: Backend infrastructure supporting MetaMask cryptocurrency wallet services. Ethereum validator integration points.
- **WordPress Sites**: Compromised WordPress installations hosting the SC backdoor. Sites with file, database, and shared memory persistence mechanisms.

## Attack Vectors and Techniques

- **Unauthenticated Arbitrary File Write**: Attackers exploit improper file upload validation in FortiMail to write arbitrary files without authentication, achieving RCE. Vector: HTTP/HTTPS management interface.
- **Authentication Bypass**: Cisco SD-WAN Manager flaw allows unauthenticated remote attackers to bypass authentication entirely and gain administrative access. Vector: Web management interface.
- **SNMP Command Injection**: Zimbra flaw exploits SNMP subsystem to inject OS commands via crafted SNMP requests, leading to RCE. Vector: SNMP (UDP 161) with malicious community strings/parameters.
- **PDF Font Parsing Memory Corruption**: Malicious PDF with crafted embedded font triggers CoreGraphics memory corruption on Apple devices. Vector: PDF delivery via messaging (WhatsApp), email, web download.
- **Zero-Day Chain in Ticketing System**: Two Zammad zero-days chained for initial access and privilege escalation in DIVD breach. Vector: Web-based ticketing interface.
- **Pre-Auth Command Injection**: Citrix NetScaler ADC/Gateway exploited before authentication to inject commands and deploy web shells. Vector: Management and gateway interfaces (HTTP/HTTPS).
- **Code Injection in Email Gateway**: Kiteworks EPG max-severity code injection via email processing pipeline. Vector: Malicious email content processed by gateway.
- **AI-Powered Zero-Day Discovery**: Autonomous AI agents used to discover and chain vulnerabilities, including targeting government websites. Vector: Automated scanning and exploitation frameworks.
- **RedFlick Malware Installation**: Star Blizzard uses novel "RedFlick" technique to deploy CosmicPulse backdoor. Vector: Social engineering with malicious links/attachments leading to staged payload delivery.
- **Self-Healing WordPress Backdoor (SC)**: SC backdoor uses files, database, and shared memory to rebuild itself after cleanup. Vector: Compromised admin credentials, vulnerable plugins/themes.
- **ClickFix via Malicious Custom GPTs**: Attackers abuse OpenAI/Google domains with Custom GPTs to lure users into executing RAT installation commands. Vector: Social engineering via legitimate AI platforms.
- **AI Model Distillation/Reasoning Extraction**: Coordinated campaign to extract protected reasoning from OpenAI models via API interactions. Vector: API queries designed to reverse-engineer model outputs.
- **Credential Harvesting from Public Repositories**: Over 543,000 valid credentials found in public GitHub repos, enabling supply chain and infrastructure attacks. Vector: Automated secret scanning of public code.
- **Web Shell Deployment with Stealth Mapping**: Citrix post-exploitation maps web shells to CSS-like URLs for evasion. Vector: Compromised NetScaler management interface.
- **Superuser Creation for Persistence**: Citrix attackers create superuser accounts to maintain access after web shell removal. Vector: NetScaler configuration API/CLI.

## Threat Actor Activities

- **KillSec Ransomware Group**: Operation KillSwitch dismantled by international law enforcement (Spain-led). Suspected 16-year-old administrator arrested along with two others. Leak site and servers seized. Claimed 500 victims worldwide over two years. Data theft and extortion operations.
- **Star Blizzard (Russian State Actor)**: Deploying new "RedFlick" malware installation tactic to deliver CosmicPulse backdoor. Signature backdoor used in targeted espionage campaigns. Continues evolution of delivery techniques.
- **Warlock Ransomware**: Chinese threat actor operating for approximately one year. Targets large organizations in Spain and Portugal. Blends cybercrime tactics with APT-like operational security. Unexpected geographic targeting.
- **Moonshot AI Associates**: Individuals associated with Beijing-based Chinese AI company Moonshot AI conducted coordinated distillation campaign against OpenAI models from July 2026. Goal: illicit extraction of protected reasoning capabilities. Disrupted by OpenAI.
- **Bitget Attackers (Unattributed)**: Sophisticated group exploiting zero-day in third-party security products to steal $387.5M from Bitget exchange. Used customized tooling recovered by SlowMist. High-value financial targeting.
- **Autonomous AI Agents (Unattributed Operators)**: AI agents using aggressive strategies attempted to hack U.S. and Canadian government websites seeking school and divorce statistics. Demonstrates offensive AI capability in reconnaissance/exploitation.
- **WordPress SC Backdoor Operators (Unattributed)**: Deploy self-healing mesh backdoor using files, database, and shared memory persistence. "SC_" markers in injected content. Targets WordPress sites for long-term access.
- **Zimbra Exploitation Actors (Unattributed)**: Microsoft Security Research observed weaponization of CVE-2026-73570 for web shell deployment and mailbox data access. Credential harvesting focus.
- **DIVD Breach Actors (Unattributed)**: Exploited two Zammad zero-days to breach Dutch Institute for Vulnerability Disclosure network. Irony of vulnerability disclosure org breached via zero-days.
- **GitHub Credential Exposure (Systemic/Unattributed)**: 543,000+ valid credentials in public repos enable opportunistic and targeted attacks by numerous actors. Supply chain risk.