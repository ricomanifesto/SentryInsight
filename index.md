---
schema_version: 2
report_date: 2026-09-17
generated_at: 2026-09-17T16:42:52Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-17/
---
# Exploitation Report

## Executive Summary

Active exploitation campaigns are intensifying across multiple vectors, with three critical vulnerabilities confirmed under active attack in the wild. Cisco's Identity Services Engine faces a maximum-severity authentication bypass (CVE-2026-76460, CVSS 10.0) that allows unauthenticated remote attackers to compromise network access control infrastructure. The Issabel Framework PBX platform is being actively exploited via an unauthenticated OS command execution flaw (CVE-2026-89026, CVSS 9.8), while a critical heap overflow in the Unbound DNSSEC validator (CVE-2026-81642) enables remote code execution through malicious DNS zones. Patches are available for all three vulnerabilities and should be applied immediately.

State-sponsored threat actors are conducting sustained espionage and disruptive operations globally. China-aligned FamousSparrow has deployed the previously undocumented SparroWocky modular backdoor against government entities across Latin America since mid-2025. Iranian state-linked operators are leveraging the CHOSEN BRICK malware to target dissidents, activists, and journalists worldwide. Three distinct threat clusters—NightEagle (APT-Q-95), Hacking Cat, and Toy Ghouls—are simultaneously targeting Russian enterprises with backdoors, ransomware, and wipers. Law enforcement disruption of the NightmareStresser DDoS-for-hire platform has removed infrastructure linked to hundreds of thousands of attacks.

Emerging attack techniques are weaponizing AI assistants and development tools at unprecedented speed. Attackers have demonstrated the ability to hijack AI coding assistant sessions to spread supply chain worms across internal repositories, while browser extensions can now subvert built-in AI assistants across Chrome, Edge, Opera Neon, and other Chromium-based products to exfiltrate data and execute malicious actions. Banking malware operations are bypassing browser security controls to force-install malicious extensions that harvest credentials and session tokens. These developments signal a fundamental shift where AI-powered tooling is becoming both a target and a force multiplier for exploitation.

## Active Exploitation Details

### Cisco ISE Authentication Bypass (CVE-2026-76460)
- **Description**: A maximum-severity zero-day vulnerability in Cisco Identity Services Engine (ISE) caused by insufficient authentication control on an API endpoint. An unauthenticated, remote attacker can bypass authentication entirely.
- **Impact**: Full authentication bypass on network access control infrastructure, potentially allowing attackers to gain unauthorized network access, manipulate policy enforcement, and compromise identity-based segmentation.
- **Status**: Actively exploited in the wild. Cisco has released security updates to address the vulnerability.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-76460
- **Reporting**: [The Hacker News — Cisco Warns of New Zero-Day ISE Auth Bypass (CVSS 10.0) Exploited in Active Attacks](https://thehackernews.com/2026/09/cisco-warns-of-new-zero-day-ise-auth.html), [Bleeping Computer — Cisco warns of max severity ISE zero-day exploited in attacks](https://www.bleepingcomputer.com/news/security/cisco-warns-of-identity-service-engine-zero-day-exploited-in-attacks/)

### Issabel Framework OS Command Execution (CVE-2026-89026)
- **Description**: A critical security flaw in Issabel Framework, a web-based framework for open-source unified communications PBX software. The vulnerability stems from a hard-coded credential issue that enables unauthenticated remote attackers to execute arbitrary operating system commands.
- **Impact**: Unauthenticated remote code execution with the privileges of the PBX application, leading to complete system compromise, potential lateral movement into voice/network infrastructure, and data exfiltration.
- **Status**: Actively exploited in the wild. CVSS v3.1 score 9.8, CVSS v4.0 score 9.3.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-89026
- **Reporting**: [The Hacker News — Attackers Exploit Issabel Framework Flaw Enabling Unauthenticated OS Command Execution](https://thehackernews.com/2026/09/attackers-exploit-issabel-framework.html)

### Unbound DNSSEC Validator Heap Overflow (CVE-2026-81642)
- **Description**: A critical heap overflow in the DNSSEC validator of the Unbound DNS resolver affecting every release before version 1.26.1. An attacker who controls a malicious DNS zone and can induce queries to a vulnerable resolver can trigger the overflow.
- **Impact**: Remote code execution on the DNS resolver infrastructure, potentially allowing cache poisoning, traffic interception, domain hijacking, and persistent network compromise.
- **Status**: Proof-of-concept exploitability demonstrated; patch available in Unbound 1.26.1 released same day as advisory. No confirmed active exploitation reported in source.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-81642
- **Reporting**: [The Hacker News — Critical Unbound DNSSEC Validator Flaw Could Allow RCE via a Malicious DNS Zone](https://thehackernews.com/2026/09/critical-unbound-dnssec-validator-flaw.html)

## Affected Systems and Products

- **Cisco Identity Services Engine (ISE)**: All versions prior to the September 2026 security update release. Network access control and policy enforcement appliances.
- **Issabel Framework**: Web-based unified communications PBX framework installations. Specific affected versions not detailed in source; all deployments should verify patch status.
- **Unbound DNS Resolver**: All versions prior to 1.26.1. Widely deployed as recursive DNS resolver with DNSSEC validation in enterprise, ISP, and embedded environments.
- **Windows 11 24H2 Home and Pro Editions**: Reaching end of support in October 2026; will cease receiving security updates.
- **Windows 11 with KB5124008 Update**: Enterprise systems experiencing domain trust relationship failures preventing valid domain credential logins.
- **Parallels Desktop for Mac**: Versions prior to 27. Intel-based Macs cannot install the fixed version 27, leaving them permanently vulnerable to local privilege escalation.
- **BIND 9 DNS Server**: Versions prior to 9.20.29 and 9.21.26. Fourteen security flaws addressed, including unauthenticated crash via DNS-over-HTTPS.
- **Gyazo Image-Sharing Service**: User database and image metadata storage systems; breach exposed 23.62 million user records and 490 million image metadata records.
- **Browser AI Assistants**: Gemini Live in Chrome, Perplexity Comet, Microsoft Edge Copilot, Opera Neon, and Claude in Chrome extension—all Chromium-based products with built-in AI assistants.
- **AI Coding Assistants**: Session-based coding assistant tools used in SaaS development environments; vulnerable to session hijacking and supply chain poisoning.

## Attack Vectors and Techniques

- **API Authentication Bypass**: Insufficient authentication control on Cisco ISE API endpoints allows unauthenticated remote attackers to bypass all authentication mechanisms (source-fefb67106246).
- **DNSSEC Validation Exploitation**: Malicious DNS zone responses trigger heap overflow in Unbound's DNSSEC validator during cryptographic validation, achieving RCE on resolver infrastructure (source-4341f2269a01).
- **Hard-Coded Credential Abuse**: Issabel Framework contains hard-coded credentials that enable unauthenticated OS command execution via web interface endpoints (source-4a519778a75a).
- **Modular Backdoor Deployment**: SparroWocky C++ backdoor provides modular espionage capabilities including command execution, file operations, and persistence across Latin American government networks (source-f355c5f46acf, source-ab0296330fd9).
- **CHOSEN BRICK Windows Malware**: Iranian state-linked malware targeting dissidents, activists, and journalists with surveillance capabilities including credential theft, screen capture, and persistence (source-768c30c52b45).
- **KREMLIN Browser Extension Toolkit**: Banking malware operation forcing installation of malicious Chrome and Edge extensions that bypass browser security checks to steal credentials, session tokens, and sensitive data (source-7eb18c524e79).
- **BragJack AI Assistant Hijacking**: Attack technique subverting browser-integrated agentic AI assistants to access sensitive information, execute malicious actions, and exfiltrate data through the AI's legitimate permissions (source-574b145c417e).
- **AI Coding Assistant Session Hijacking**: Attacker compromises active AI coding assistant session, poisons recommendations, and spreads Shai-Hulud worm across ~100 internal repositories to steal secrets and source code (source-ffa867bf23d6).
- **Cross-Browser AI Extension Hijacking**: Single browser extension exploits shared Chromium extension architecture to hijack AI assistants across Chrome, Comet, Edge, Opera Neon, and Claude simultaneously (source-d58c7f1a86f6).
- **Parallels Desktop Local Privilege Escalation**: Non-admin local user exploits flaw to execute code as root on macOS; requires local code execution but not network access (source-f1a5ac76bbe3).
- **DDoS-for-Hire Infrastructure**: NightmareStresser platform provided DDoS attack capabilities to customers, linked to hundreds of thousands of attacks before domain seizure (source-97289c2c314a, source-cd6d3ec16304).
- **AI-Powered Data Breach**: First reported case of AI agent powered by known LLM used to carry out data breach, reported to Spanish Data Protection Agency (source-b32240f631c6).
- **BIND DoH Unauthenticated Crash**: Single malformed request with invalid signature over DNS-over-HTTPS crashes named process without credentials (source-6829fa0c1a46).

## Threat Actor Activities

- **FamousSparrow (China-aligned)**: Deploying SparroWocky modular backdoor in sustained espionage campaign targeting government organizations across multiple Latin American countries since at least August 2025. Uses previously unreported C++ backdoor with modular architecture (source-f355c5f46acf, source-ab0296330fd9).
- **Iranian State-Linked Operators**: Leveraging CHOSEN BRICK Windows malware in global surveillance campaign targeting dissidents, activists, and journalists. Government agencies issuing warnings about ongoing activity (source-768c30c52b45).
- **NightEagle (APT-Q-95)**: Active since at least 2023, targeting Russian enterprises with new persistence and lateral movement techniques. Part of three-cluster campaign against Russian organizations (source-27afdbdfcf69).
- **Hacking Cat**: Threat activity cluster targeting Russian enterprises with backdoors, ransomware, and wipers alongside NightEagle and Toy Ghouls (source-27afdbdfcf69).
- **Toy Ghouls**: Third threat cluster in coordinated targeting of Russian enterprises, employing destructive wiper malware alongside backdoor and ransomware payloads (source-27afdbdfcf69).
- **Banking Malware Operators (KREMLIN)**: Active since mid-2025, using custom toolkit to force-install malicious browser extensions for credential theft and session hijacking across financial targets (source-7eb18c524e79).
- **NightmareStresser Operators**: Long-running DDoS-for-hire service operators whose infrastructure (nightmare-stresser[.]com, nightmarestresser[.]org) was seized by FBI/DoJ after facilitating hundreds of thousands of attacks (source-97289c2c314a, source-cd6d3ec16304).
- **Unknown Actor (AI Coding Assistant Hijack)**: Compromised active AI coding assistant session at unnamed SaaS provider, poisoned software recommendations, and propagated Shai-Hulud worm across ~100 internal repositories to steal secrets and source code (source-ffa867bf23d6).
- **Unknown Actor (Browser AI Extension)**: Demonstrated cross-browser AI assistant hijacking via single malicious extension affecting five Chromium-based AI products; research by Forever Security (source-d58c7f1a86f6).