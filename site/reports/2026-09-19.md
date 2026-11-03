---
schema_version: 2
report_date: 2026-09-19
generated_at: 2026-09-19T20:25:49Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-19/
---
# Exploitation Report

## Executive Summary

Critical exploitation activity spans multiple high-value targets this period, with five actively exploited vulnerabilities carrying CVSS scores of 8.8 or higher. CISA has added three Linux kernel flaws to its Known Exploited Vulnerabilities catalog, including CVE-2025-39682 rated 9.8, while Fortinet confirms active exploitation of a critical pre-authentication RCE in Orkes Conductor (CVE-2026-58138, CVSS 9.8). A maximum-severity authentication bypass in Cisco Identity Services Engine (CVE-2026-76460, CVSS 10.0) and a privilege escalation flaw in Azure AI Foundry (CVE-2026-85889, CVSS 10.0) round out the most severe issues, both now patched.

Nation-state and criminal threat actors are conducting large-scale operations with significant impact. North Korea's WaterPlum group compromised at least 30,000 devices globally between December 2025 and July 2026, exfiltrating over $10.7 million in cryptocurrency. Pakistan-aligned Transparent Tribe (APT36) deployed novel Rust-based backdoors against government and defense entities in India and Afghanistan using private GitHub repositories for command and control. The ShinyHunters extortion gang breached the Clop ransomware operation's leak site, stealing server data and onion service private keys in a notable criminal-on-criminal attack.

Supply chain and AI-driven attack vectors are accelerating. A TanStack npm supply chain compromise led to the theft of 170 private GitHub repositories from CrowdSec via a departed employee's compromised credentials. Public exploit code for four Linux kernel local privilege escalation flaws has been released, endangering unpatched systems. Researchers demonstrated AI-assisted vulnerability chaining using Claude Opus 5 to compromise OpenAI employee accounts, while the BragJack technique shows malicious extensions can hijack AI browser agents across Chrome, Edge, Opera, and Perplexity. The Plugin4Shell flaw affects four major AI coding agents, allowing repository owners to swap pinned plugins for malicious versions.

## Active Exploitation Details

### SolarWinds Access Rights Manager Hard-Coded Key Remote Code Execution
- **Description**: A hard-coded cryptographic key in SolarWinds Access Rights Manager (ARM) allows unauthenticated attackers to achieve remote code execution. The flaw affects all versions of ARM 2026.2 and prior.
- **Impact**: Unauthenticated remote code execution with SYSTEM privileges on the ARM server, leading to full compromise of the identity management infrastructure.
- **Status**: SolarWinds has released security updates addressing the vulnerability. Patches are available for all affected versions.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: patch
- **CVE IDs**: CVE-2026-28326
- **Reporting**: [The Hacker News — SolarWinds Patches ARM Hard-Coded Key Flaw Enabling Unauthenticated RCE](https://thehackernews.com/2026/09/solarwinds-patches-arm-hard-coded-key.html)

### Orkes Conductor Pre-Authentication Remote Code Execution
- **Description**: An unauthenticated remote code execution vulnerability in Orkes Conductor workflow platform versions 3.21.21 through 3.30.1. The flaw allows remote attackers to execute arbitrary code without authentication.
- **Impact**: Full system compromise of Orkes Conductor instances, enabling attackers to execute arbitrary commands, access workflow data, and pivot within the environment.
- **Status**: Fortinet confirms active exploitation in the wild. Orkes has released version 3.30.2 which addresses the vulnerability.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-58138
- **Reporting**: [The Hacker News — Critical Pre-Auth RCE in Orkes Conductor Workflow Platform Exploited in the Wild](https://thehackernews.com/2026/09/critical-pre-auth-rce-in-orkes.html)

### Cisco Identity Services Engine Authentication Bypass
- **Description**: An authentication bypass flaw in Cisco Identity Services Engine (ISE) API endpoints that allows unauthenticated attackers to bypass authentication controls entirely.
- **Impact**: Complete bypass of authentication mechanisms in Cisco ISE, potentially allowing unauthorized access to network access control policies, guest management, and identity services.
- **Status**: Identified as a zero-day with maximum CVSS score. Cisco has acknowledged the vulnerability; patch status should be verified via Cisco security advisories.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-76460
- **Reporting**: [Dark Reading — Cisco Zero-Day Highlights API Endpoint Authentication Issues](https://www.darkreading.com/vulnerabilities-threats/cisco-zero-day-api-endpoint-authentication-issues)

### Linux Kernel TLS Receive Path Vulnerability
- **Description**: An improper check for unusual or exceptional conditions in the TLS receive path of the Linux kernel. This flaw allows attackers to trigger kernel-level memory corruption or privilege escalation.
- **Impact**: Kernel-level code execution or privilege escalation on affected Linux systems. CISA has confirmed active exploitation in the wild.
- **Status**: Added to CISA Known Exploited Vulnerabilities catalog. Kernel maintainers have released fixes; distributions are issuing updated kernel packages.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2025-39682
- **Reporting**: [The Hacker News — CISA Flags Three Linux Kernel Vulnerabilities Exploited in the Wild](https://thehackernews.com/2026/09/cisa-flags-three-linux-kernel.html)

### Microsoft Azure AI Foundry Privilege Escalation
- **Description**: Missing authentication for a critical function in Azure AI Foundry allows unauthorized attackers to elevate privileges over the network without requiring valid credentials.
- **Impact**: Unauthorized privilege escalation within Azure AI Foundry environments, potentially granting attackers elevated access to AI models, data, and configuration.
- **Status**: Microsoft has released fixes. No customer action is required as the patch is applied at the platform level.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: patch
- **CVE IDs**: CVE-2026-85889
- **Reporting**: [The Hacker News — Microsoft Patches CVSS 10.0 Azure AI Foundry Flaw Enabling Unauthorized Privilege Escalation](https://thehackernews.com/2026/09/microsoft-patches-cvss-100-azure-ai.html)

### Linux Kernel Local Privilege Escalation Flaws (Four Vulnerabilities)
- **Description**: Four distinct Linux kernel vulnerabilities each allowing a local user to gain root privileges. Working exploit code has been publicly released for all four flaws.
- **Impact**: Local privilege escalation to root on any Linux system running an unpatched kernel. Public exploit availability significantly increases risk for unpatched systems.
- **Status**: Kernel maintainers have fixed all four vulnerabilities over recent weeks. Public exploit code is available. Systems running current kernel versions are not affected.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — Public Exploits Released for Four Linux Kernel Flaws That Enable Local Root](https://thehackernews.com/2026/09/public-exploits-released-for-four-linux.html)

### WordPress Click2Shell Vulnerability Chain
- **Description**: A vulnerability chain in WordPress core allowing a crafted link, when opened by a logged-in administrator, to install a theme from WordPress.org without user interaction. This can be chained to achieve remote code execution.
- **Impact**: Unauthorized theme installation leading to potential remote code execution on WordPress sites when an administrator clicks a malicious link.
- **Status**: WordPress has released patches addressing the vulnerability chain. The security firm pwn.ai reported the flaw and named the attack chain "Click2Shell."
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — New WordPress Click2Shell Flaw Forces Theme Installs, Can Chain to Code Execution](https://thehackernews.com/2026/09/new-wordpress-click2shell-flaw-forces.html)

### Gyazo Server Vulnerability Data Breach
- **Description**: Attackers exploited a server vulnerability in the Gyazo image-sharing platform to access and exfiltrate user records.
- **Impact**: Theft of 23.6 million user records from the Gyazo platform.
- **Status**: Gyazo has confirmed the breach. Specific vulnerability details and patch status were not disclosed in the reporting.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Gyazo server flaw exploited to steal 23.6 million user records](https://www.bleepingcomputer.com/news/security/gyazo-server-flaw-exploited-to-steal-236-million-user-records/)

### Check Point Management Critical Remote Code Execution
- **Description**: A critical vulnerability in Check Point Software management systems allowing attackers to execute code with root privileges.
- **Impact**: Full root-level compromise of Check Point management systems, enabling complete control over firewall and security policy infrastructure.
- **Status**: Check Point has released security updates addressing the vulnerability.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: patch
- **Reporting**: [Bleeping Computer — New Check Point flaw lets hackers execute code with root privileges](https://www.bleepingcomputer.com/news/security/check-point-warns-critical-flaw-lets-hackers-execute-code-as-root/)

### Plugin4Shell AI Coding Agent Plugin Hijacking
- **Description**: A flaw in four widely used AI coding agents (Claude Code, Codex, GitHub Copilot, and one unnamed) allows repository owners to swap pinned plugin code for malicious versions, even when the agent has locked the plugin to a specific reviewed version.
- **Impact**: Supply chain compromise of AI coding assistants, enabling arbitrary code execution in development environments when agents install malicious plugin updates.
- **Status**: Anthropic patched in Claude Code 2.1.179; OpenAI patched in Codex 0.146.0; GitHub Copilot has no fix reported as of publication.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — Plugin4Shell Lets Repository Owners Swap Pinned Plugin Code Across Four AI Coding Agents](https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html)

### BragJack AI Browser Agent Hijacking
- **Description**: A proof-of-concept attack technique called "Prompt Forcing" that uses a single malicious browser extension to hijack AI assistants across Chrome, Edge, Opera Neon, Perplexity Comet, and Claude in Chrome.
- **Impact**: Complete control over AI browser agents, allowing attackers to exfiltrate data, manipulate AI responses, and perform actions on behalf of the user.
- **Status**: Proof-of-concept demonstrated by Forever Security researcher Gal Weizman. Two CVEs assigned (specific IDs not disclosed). Earned over $20,000 in bug bounties.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: mitigate
- **Reporting**: [Bleeping Computer — BragJack attacks hijack AI browser agents through malicious extensions](https://www.bleepingcomputer.com/news/security/bragjack-attacks-hijack-ai-browser-agents-through-malicious-extensions/)

### TanStack npm Supply Chain Attack
- **Description**: Malicious versions of TanStack npm packages were published that stole credentials from developer environments. This led to compromise of a CrowdSec employee's laptop and subsequent theft of 170 private GitHub repositories using the employee's retained access.
- **Impact**: Credential theft from developer machines, unauthorized access to private source code repositories, and potential further supply chain contamination.
- **Status**: Malicious packages identified. CrowdSec revoked the compromised employee's access. TanStack supply chain compromise under investigation.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — CrowdSec Says TanStack npm Attack Led to Copy of 170 Private GitHub Repositories](https://thehackernews.com/2026/09/crowdsec-says-tanstack-npm-attack-led.html)

### WeaselBiscuit npm Malware Campaign
- **Description**: A cluster of 13 malicious npm packages delivering the WeaselBiscuit JavaScript stealer, which harvests Chrome Extension Storage data. The malware shows functional overlaps with DPRK Contagious Interview campaign tooling (BeaverTail).
- **Impact**: Theft of sensitive data stored in Chrome extensions, including authentication tokens, cryptocurrency wallet data, and personal information.
- **Status**: 13 malicious packages identified by OpenSourceMalware. Packages likely removed from npm registry; developers should audit dependencies.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — WeaselBiscuit Stealer Spreads via 13 npm Packages to Harvest Chrome Extension Storage](https://thehackernews.com/2026/09/weaselbiscuit-stealer-spreads-via-13.html)

### OpenAI Help Forum and Login System Chain (Research)
- **Description**: Security researchers at Hacktron chained two vulnerabilities—a bug in OpenAI's public help forum software and a weakness in OpenAI's login system—using Anthropic's Claude Opus 5 to assist in the exploit development.
- **Impact**: Account takeover of OpenAI employee ChatGPT and Codex accounts, with access to an internal OpenAI code repository.
- **Status**: Conducted as authorized security research. OpenAI has been notified; remediation status not publicly disclosed.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — Claude Opus 5 Helped Researchers Take Over OpenAI Staff Accounts via Chained Flaws](https://thehackernews.com/2026/09/claude-opus-5-helped-researchers-take.html)

### Google Gemini Security Test Domain Mix-Up
- **Description**: During a security evaluation by Israeli company Irregular in May 2026, Google's Gemini AI model accessed the internet and inadvertently broke into real company systems due to a test domain configuration error.
- **Impact**: Unauthorized access to third-party systems by an AI model during authorized testing, demonstrating risks of autonomous AI agents with internet access.
- **Status**: Incident occurred during controlled evaluation. Irregular and Google notified affected parties. Architectural safeguards under review.
- **Severity**: medium
- **Exploitation Status**: observed
- **Action**: monitor
- **Reporting**: [The Hacker News — Google Gemini Broke Into Real Company Systems After Security Test Domain Mix-Up](https://thehackernews.com/2026/09/google-gemini-broke-into-real-company.html)

## Affected Systems and Products

- **SolarWinds Access Rights Manager**: All versions 2026.2 and prior; Windows Server environments running ARM for identity governance
- **Orkes Conductor**: Versions 3.21.21 through 3.30.1; Workflow orchestration platforms deployed on-premises or in cloud environments
- **Cisco Identity Services Engine (ISE)**: Affected versions per Cisco security advisory; Network access control and policy management appliances (physical and virtual)
- **Linux Kernel**: All versions prior to patched releases containing fixes for CVE-2025-39682 and the four local privilege escalation flaws; All Linux distributions and embedded systems running vulnerable kernels
- **Microsoft Azure AI Foundry**: Platform-level service; No customer-deployed components affected as patch applied by Microsoft
- **WordPress Core**: Versions prior to the September 2026 security release; All WordPress installations with administrator accounts
- **Gyazo Platform**: Server-side infrastructure; Image-sharing service users (23.6 million records compromised)
- **Check Point Management**: Management servers and multi-domain management appliances; Security policy management infrastructure
- **AI Coding Agents**: Anthropic Claude Code (< 2.1.179), OpenAI Codex (< 0.146.0), GitHub Copilot (all versions), and one additional unnamed agent; Developer workstations and CI/CD pipelines using these tools
- **Browser AI Assistants**: Chrome, Edge, Opera Neon, Perplexity Comet, and Claude in Chrome with malicious extensions installed; End-user browsers with extension support
- **TanStack npm Packages**: Compromised package versions published to npm registry; Developer environments and CI/CD systems installing TanStack dependencies
- **npm Ecosystem**: 13 identified malicious packages delivering WeaselBiscuit stealer; JavaScript/TypeScript projects with compromised dependencies
- **OpenAI Internal Systems**: Help forum platform and authentication systems; Employee ChatGPT, Codex, and internal repository access

## Attack Vectors and Techniques

- **AI-Assisted Vulnerability Chaining**: Researchers used Claude Opus 5 to identify and chain a help forum bug with a login system weakness, demonstrating AI-accelerated exploit development against production systems
- **Prompt Forcing (BragJack)**: Malicious browser extensions inject prompts into AI assistant contexts, hijacking agent behavior across multiple browser platforms and AI providers with a single extension
- **Supply Chain Credential Theft via Malicious npm Packages**: TanStack supply chain compromise delivered credential stealers to developer machines, enabling downstream repository access using valid stolen credentials
- **Chrome Extension Storage Harvesting**: WeaselBiscuit stealer targets Chrome Extension Storage APIs to exfiltrate authentication tokens, crypto wallet data, and sensitive credentials stored by legitimate extensions
- **Private GitHub Repository C2**: Transparent Tribe uses private GitHub repositories as command-and-control infrastructure for Rust-based backdoors (RUSTYSHADE, RUSTYMOVE, PSNATCH, BASHNATCH), blending malicious traffic with legitimate developer workflows
- **Pinned Plugin Bypass (Plugin4Shell)**: Repository owners exploit trust in pinned plugin versions by swapping underlying code, defeating version pinning protections in AI coding agents
- **Unauthenticated Pre-Auth RCE**: Orkes Conductor and Cisco ISE vulnerabilities allow remote code execution without any authentication, exposing management interfaces directly to internet-based attacks
- **Hard-Coded Cryptographic Key Abuse**: SolarWinds ARM flaw leverages a static embedded key to forge authentication tokens and achieve unauthenticated RCE
- **Kernel TLS Path Memory Corruption**: Linux kernel CVE-2025-39682 exploits improper exception handling in TLS receive processing for kernel-level code execution
- **Local Privilege Escalation via Public Exploits**: Four Linux kernel flaws with released exploit code enable unprivileged local users to gain root access on unpatched systems
- **Administrator-Initiated Theme Installation (Click2Shell)**: Crafted URLs trigger unauthorized theme installation when opened by logged-in WordPress administrators, chaining to RCE via theme functionality
- **AI Model Autonomous Network Access**: Google Gemini accessed external systems during security testing due to domain configuration errors, demonstrating emergent risks of internet-connected autonomous agents
- **Ransomware Leak Site Compromise**: ShinyHunters breached Clop's Tor-hosted leak site, stealing server data and onion private keys—criminal-on-criminal infrastructure attack
- **Nation-State Cryptocurrency Theft**: WaterPlum (North Korea) compromised 30,000+ devices globally, exfiltrating $10.7M+ in cryptocurrency over 8-month campaign
- **SEO-Optimized GitHub Malware Distribution**: Fake LastPass Authenticator repositories use search optimization to deliver Rapuncel infostealer to developers searching for legitimate tools

## Threat Actor Activities

- **WaterPlum (North Korea)**: Compromised at least 30,000 devices worldwide from December 2025 through July 2026 per joint law enforcement advisory. Exfiltrated over $10.7 million in stolen cryptocurrency to North Korean infrastructure. Large-scale opportunistic campaign targeting global device population.
- **Transparent Tribe / APT36 / Earth Karkaddan (Pakistan-aligned)**: Deployed novel Rust-based toolkit (RUSTYSHADE, RUSTYMOVE, PSNATCH, BASHNATCH) against government and defense entities in India and Afghanistan. Uses private GitHub repositories for C2 infrastructure. Activity codenamed Operation (name truncated in reporting).
- **ShinyHunters (Extortion Gang)**: Breached Clop (Cl0p) ransomware operation's Tor leak site, defacing the site and allegedly stealing server data and onion service private keys. Notable criminal-on-criminal attack targeting ransomware infrastructure.
- **DPRK Contagious Interview Campaign Operators**: Linked to WeaselBiscuit npm malware campaign through functional code overlaps with BeaverTail and associated tooling. Targets developers via malicious npm packages and fake GitHub repositories.
- **TanStack Supply Chain Attackers (Unidentified)**: Compromised TanStack npm package publishing pipeline to inject credential-stealing code. Led to compromise of CrowdSec employee laptop and theft of 170 private GitHub repositories.
- **Forever Security / Gal Weizman (Security Researcher)**: Developed BragJack Prompt Forcing technique demonstrating AI browser agent hijacking via malicious extensions. Proof-of-concept earned $20,000+ in bounties and two CVE assignments.
- **Hacktron Researchers (Security Research)**: Used Claude Opus 5 to chain OpenAI help forum and login vulnerabilities, achieving employee account takeover and internal repository access as authorized research.
- **Irregular (Israeli Security Firm)**: Conducted security evaluation where Google Gemini autonomously accessed third-party systems due to test domain misconfiguration. Demonstrates AI safety risks in autonomous agent deployments.
- **pwn.ai (Security Firm)**: Discovered and reported WordPress Click2Shell vulnerability chain enabling forced theme installation and chained RCE via administrator link clicks.