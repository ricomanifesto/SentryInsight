---
schema_version: 2
report_date: 2026-09-20
generated_at: 2026-09-20T15:57:29Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-20/
---
# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse technology stacks, ranging from network infrastructure and workflow platforms to AI-driven development tools and software supply chains. CISA has confirmed active exploitation of three Linux kernel flaws, while Fortinet reports a critical pre-authentication RCE in Orkes Conductor being exploited in the wild. A maximum-severity zero-day in Cisco Identity Services Engine (CVSS 10.0) highlights systemic API authentication weaknesses. Simultaneously, nation-state actors—most notably North Korea's WaterPlum group—have compromised over 30,000 devices globally in a sustained cryptocurrency theft campaign, and Pakistan-aligned Transparent Tribe continues targeting government and defense entities in South Asia with novel Rust-based tooling.

The software supply chain remains a primary battleground. The TanStack npm attack facilitated credential theft and the exfiltration of 170 private GitHub repositories from CrowdSec, while an ongoing malicious npm campaign ('indexed-btree') demonstrates evolution in evasion techniques by embedding payloads in runtime behavior rather than installation scripts. Researchers have also demonstrated practical sandbox escapes against OpenAI Codex and chained authentication flaws to compromise OpenAI employee accounts, underscoring emergent risks in AI-assisted development workflows. Proof-of-concept exploits for four additional Linux kernel local privilege escalation flaws are now public, and a Gyazo server breach exposed 23.6 million user records.

## Active Exploitation Details

### Orkes Conductor Unauthenticated RCE
- **Description**: A critical unauthenticated remote code execution vulnerability in Orkes Conductor workflow platform, caused by improper input validation allowing attackers to execute arbitrary code without authentication.
- **Impact**: Full remote code execution on affected Orkes Conductor instances, enabling complete system compromise, data theft, and lateral movement.
- **Status**: Actively exploited in the wild per Fortinet; patched in version 3.30.2.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-58138
- **Reporting**: [The Hacker News — Critical Pre-Auth RCE in Orkes Conductor Workflow Platform Exploited in the Wild](https://thehackernews.com/2026/09/critical-pre-auth-rce-in-orkes.html)

### Cisco Identity Services Engine Authentication Bypass Zero-Day
- **Description**: An authentication bypass flaw in Cisco Identity Services Engine (ISE) API endpoints that allows unauthenticated attackers to bypass authentication mechanisms entirely.
- **Impact**: Complete authentication bypass on Cisco ISE, potentially enabling unauthorized administrative access, policy manipulation, and network compromise.
- **Status**: Zero-day vulnerability with maximum CVSS score; exploitation confirmed in the wild.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-76460
- **Reporting**: [Dark Reading — Cisco Zero-Day Highlights API Endpoint Authentication Issues](https://www.darkreading.com/vulnerabilities-threats/cisco-zero-day-api-endpoint-authentication-issues)

### Linux Kernel TLS Receive Path Vulnerability
- **Description**: An improper check for unusual or exceptional conditions vulnerability in the TLS receive path of the Linux kernel that can be triggered remotely.
- **Impact**: Remote code execution or denial of service on affected Linux systems; CVSS score of 9.8 indicates near-maximum severity.
- **Status**: Added to CISA Known Exploited Vulnerabilities catalog with evidence of active exploitation.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2025-39682
- **Reporting**: [The Hacker News — CISA Flags Three Linux Kernel Vulnerabilities Exploited in the Wild](https://thehackernews.com/2026/09/cisa-flags-three-linux-kernel.html)

### Two Additional Linux Kernel Vulnerabilities (CISA KEV)
- **Description**: Two additional Linux kernel security flaws added to CISA's Known Exploited Vulnerabilities catalog alongside CVE-2025-39682, citing evidence of active exploitation in the wild.
- **Impact**: Kernel-level compromise enabling privilege escalation, container escape, or system takeover depending on the specific flaw.
- **Status**: Actively exploited per CISA; patches available in recent kernel releases.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — CISA Flags Three Linux Kernel Vulnerabilities Exploited in the Wild](https://thehackernews.com/2026/09/cisa-flags-three-linux-kernel.html)

### SolarWinds Access Rights Manager Hard-Coded Key RCE
- **Description**: A hard-coded cryptographic key flaw in SolarWinds Access Rights Manager (ARM) that enables unauthenticated remote code execution.
- **Impact**: Unauthenticated RCE on all ARM versions 2026.2 and prior, allowing full system compromise.
- **Status**: Security updates released by SolarWinds; exploitation status in wild not explicitly confirmed but high-risk given unauthenticated RCE nature.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-28326
- **Reporting**: [The Hacker News — SolarWinds Patches ARM Hard-Coded Key Flaw Enabling Unauthenticated RCE](https://thehackernews.com/2026/09/solarwinds-patches-arm-hard-coded-key.html)

### Azure AI Foundry Privilege Escalation
- **Description**: Missing authentication for critical function in Azure AI Foundry allowing unauthorized attackers to elevate privileges over the network.
- **Impact**: Unauthorized privilege escalation within Azure AI Foundry environment, potentially leading to cross-tenant access or resource manipulation.
- **Status**: Microsoft released fixes; no customer action required per Microsoft; no indication of exploitation in the wild.
- **Severity**: critical
- **Exploitation Status**: not_observed
- **Action**: none
- **CVE IDs**: CVE-2026-85889
- **Reporting**: [The Hacker News — Microsoft Patches CVSS 10.0 Azure AI Foundry Flaw Enabling Unauthorized Privilege Escalation](https://thehackernews.com/2026/09/microsoft-patches-cvss-100-azure-ai.html)

### WaterPlum North Korean Campaign
- **Description**: Sustained campaign by North Korean hacking group WaterPlum compromising devices globally to steal cryptocurrency, operating from December 2025 through July 2026.
- **Impact**: At least 30,000 devices compromised worldwide; over $10.7 million in cryptocurrency stolen and transferred to North Korea.
- **Status**: Active campaign documented in joint law enforcement advisory; specific vulnerabilities exploited not publicly disclosed.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — North Korean WaterPlum hackers infected 30,000 devices worldwide](https://www.bleepingcomputer.com/news/security/north-korean-waterplum-hackers-infected-30-000-devices-worldwide/)

### TanStack npm Supply Chain Attack
- **Description**: Malicious versions of TanStack npm packages published in a supply chain attack that stole credentials from developer environments, leading to downstream compromise of GitHub accounts.
- **Impact**: Credential theft from developer machines; used to access and copy 170 private GitHub repositories from CrowdSec via a compromised former employee's account.
- **Status**: Attack occurred in May 2026; malicious packages identified and removed; CrowdSec confirmed breach on September 18, 2026.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — CrowdSec Says TanStack npm Attack Led to Copy of 170 Private GitHub Repositories](https://thehackernews.com/2026/09/crowdsec-says-tanstack-npm-attack-led.html)

### Malicious npm Package 'indexed-btree' Runtime Evasion Campaign
- **Description**: Ongoing npm malware campaign where the 'indexed-btree' package hides malicious code in normal runtime behavior rather than installation scripts, evading traditional supply chain defenses that scan install hooks.
- **Impact**: Arbitrary code execution during normal package usage; bypasses install-script scanning defenses; persistent access to development and build environments.
- **Status**: Ongoing campaign as of reporting; no patch available for the evasion technique itself—requires behavioral detection.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [Bleeping Computer — Malicious npm packages evade install-script defenses at runtime](https://www.bleepingcomputer.com/news/security/malicious-npm-packages-evade-install-script-defenses-at-runtime/)

### Gyazo Server Vulnerability Data Breach
- **Description**: A server vulnerability in the Gyazo image-sharing platform that was exploited to access and exfiltrate user databases.
- **Impact**: Theft of 23.6 million user records including account credentials and associated data.
- **Status**: Breach confirmed by Gyazo; vulnerability exploited in the wild; specific flaw not disclosed.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Gyazo server flaw exploited to steal 23.6 million user records](https://www.bleepingcomputer.com/news/security/gyazo-server-flaw-exploited-to-steal-236-million-user-records/)

### Transparent Tribe Rust Backdoor Campaign
- **Description**: Pakistan-aligned APT36 (Transparent Tribe/Earth Karkaddan) deploying previously undocumented Rust-based backdoors (RUSTYSHADE, RUSTYMOVE, PSNATCH, BASHNATCH) using private GitHub repositories for command-and-control infrastructure.
- **Impact**: Persistent access to government and defense entities in India and Afghanistan; novel tooling evades traditional detection; GitHub-based C2 blends with legitimate traffic.
- **Status**: Active campaign attributed by Zscaler ThreatLabz; operation codenamed (name not fully captured in source).
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Transparent Tribe Deploys New Rust Backdoor Using Private GitHub Repositories for C2](https://thehackernews.com/2026/09/transparent-tribe-deploys-new-rust.html)

### Four Linux Kernel Local Privilege Escalation Flaws (Public Exploits)
- **Description**: Working exploit code released for four Linux kernel vulnerabilities that each allow a local user to gain root privileges.
- **Impact**: Local root privilege escalation on any unpatched system; exploit code is publicly available.
- **Status**: Kernel maintainers have fixed all four flaws in recent weeks; public exploits increase urgency for patching.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — Public Exploits Released for Four Linux Kernel Flaws That Enable Local Root](https://thehackernews.com/2026/09/public-exploits-released-for-four-linux.html)

### WordPress Click2Shell Theme Installation Flaw
- **Description**: A vulnerability in WordPress core allowing a crafted web link, when opened by a logged-in administrator, to install a theme from the official WordPress.org directory without user interaction. Can be chained to achieve code execution.
- **Impact**: Unauthorized theme installation leading to potential remote code execution via malicious themes; requires admin interaction with malicious link.
- **Status**: WordPress released patches; exploitation in wild not confirmed.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — New WordPress Click2Shell Flaw Forces Theme Installs, Can Chain to Code Execution](https://thehackernews.com/2026/09/new-wordpress-click2shell-flaw-forces.html)

### OpenAI Codex Sandbox Escape
- **Description**: Researchers demonstrated two methods to escape the OpenAI Codex sandbox, one allowing command execution on the developer's host machine from the most locked-down mode.
- **Impact**: Container/sandbox escape leading to host compromise; affects developers using Codex in restricted modes.
- **Status**: OpenAI has patched both escape vectors; demonstrated as research, not observed in malicious exploitation.
- **Severity**: high
- **Exploitation Status**: not_observed
- **Action**: patch
- **Reporting**: [Bleeping Computer — Researchers escape OpenAI Codex sandbox to run commands on host](https://www.bleepingcomputer.com/news/security/researchers-escape-openai-codex-sandbox-to-run-commands-on-host/)

### Chained OpenAI Account Takeover via Help Forum and Login Flaws
- **Description**: Researchers chained a bug in OpenAI's public help forum software with a weakness in OpenAI's login system to take over ChatGPT and Codex accounts of OpenAI employees, then accessed an internal code repository.
- **Impact**: Full account takeover of high-value targets; access to internal proprietary code repositories.
- **Status**: Demonstrated by security researchers (Hacktron) using AI assistance (Claude Opus 5); flaws reported; not observed in malicious wild exploitation.
- **Severity**: high
- **Exploitation Status**: not_observed
- **Action**: investigate
- **Reporting**: [The Hacker News — Claude Opus 5 Helped Researchers Take Over OpenAI Staff Accounts via Chained Flaws](https://thehackernews.com/2026/09/claude-opus-5-helped-researchers-take.html)

### BragJack AI Browser Agent Hijacking
- **Description**: Proof-of-concept attack (BragJack) using a single malicious browser extension to hijack AI assistants in Chrome, Edge, Opera Neon, Perplexity Comet, and Claude in Chrome via a "Prompt Forcing" technique.
- **Impact**: Complete control over AI browser agents; data exfiltration, action injection, and persistent access across multiple AI platforms simultaneously.
- **Status**: Proof-of-concept only; earned $20,000+ in bug bounties and two CVEs (not specified in source); not observed in wild exploitation.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: monitor
- **Reporting**: [Bleeping Computer — BragJack attacks hijack AI browser agents through malicious extensions](https://www.bleepingcomputer.com/news/security/bragjack-attacks-hijack-ai-browser-agents-through-malicious-extensions/)

### Plugin4Shell AI Coding Agent Plugin Swap
- **Description**: Flaw in four widely used AI coding agents allowing repository owners to swap pinned plugin code for malicious versions even when agents locked plugins to specific reviewed versions.
- **Impact**: Supply chain compromise of AI coding assistants; malicious plugin execution in developer environments with high privileges.
- **Status**: Anthropic patched in Claude Code 2.1.179; OpenAI patched in Codex 0.146.0; GitHub Copilot reportedly has no fix; demonstrated by Air Security researchers.
- **Severity**: high
- **Exploitation Status**: not_observed
- **Action**: patch
- **Reporting**: [The Hacker News — Plugin4Shell Lets Repository Owners Swap Pinned Plugin Code Across Four AI Coding Agents](https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html)

### Abandoned CDN Domain Re-registration Supply Chain Risk
- **Description**: An abandoned CDN domain re-registered in July 2025; thousands of websites, code repositories, and documentation pages still contain hard-coded references to the domain, enabling potential supply chain attacks.
- **Impact**: Potential code injection, malware delivery, or data interception for any site still referencing the domain; broad ecosystem impact.
- **Status**: Domain under new ownership since July 2025; thousands of callers remain; no confirmed exploitation reported.
- **Severity**: medium
- **Exploitation Status**: potential
- **Action**: investigate
- **Reporting**: [The Hacker News — An Abandoned CDN Domain Was Re-Registered. Thousands of Sites Still Call It.](https://thehackernews.com/2026/09/an-abandoned-cdn-domain-was-re.html)

### Fake LastPass Authenticator GitHub Repos Distributing Rapuncel Infostealer
- **Description**: Malware campaign using SEO-optimized GitHub repositories impersonating legitimate software firms to distribute a previously undocumented information stealer named Rapuncel.
- **Impact**: Credential theft, session hijacking, cryptocurrency wallet compromise, and system information exfiltration from victims who download the fake authenticator.
- **Status**: Ongoing campaign; GitHub repositories actively used for distribution; no CVE associated (malware distribution, not vulnerability exploitation).
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [Bleeping Computer — Fake LastPass Authenticator GitHub repos push new Rapuncel infostealer](https://www.bleepingcomputer.com/news/security/fake-lastpass-authenticator-github-repos-push-new-rapuncel-infostealer/)

### ShinyHunters Breach of Clop Ransomware Leak Site
- **Description**: The ShinyHunters extortion gang breached the Clop (Cl0p) ransomware operation's data leak site on Tor, defacing the site and allegedly stealing server data and onion service private keys.
- **Impact**: Compromise of ransomware gang infrastructure; potential exposure of victim data held by Clop; disruption of ransomware operations.
- **Status**: Active incident; ShinyHunters threatening to extort Clop; no vulnerability exploitation details disclosed.
- **Severity**: medium
- **Exploitation Status**: observed
- **Action**: monitor
- **Reporting**: [Bleeping Computer — ShinyHunters hacks Clop leak site, threatens to extort ransomware gang](https://www.bleepingcomputer.com/news/security/shinyhunters-hacks-clop-leak-site-threatens-to-extort-ransomware-gang/)

### Google Gemini Security Test Domain Mix-Up
- **Description**: During a security evaluation by Israeli company Irregular in May 2026, Google's Gemini model accessed the internet and interacted with real company systems due to a test domain configuration error.
- **Impact**: Unauthorized access to third-party systems by an AI model during authorized testing; highlights risks of AI agency in security evaluations.
- **Status**: Incident occurred during controlled evaluation; configuration issue remediated; not a vulnerability in Gemini itself.
- **Severity**: medium
- **Exploitation Status**: not_observed
- **Action**: investigate
- **Reporting**: [The Hacker News — Google Gemini Broke Into Real Company Systems After Security Test Domain Mix-Up](https://thehackernews.com/2026/09/google-gemini-broke-into-real-company.html)

## Affected Systems and Products

- **Orkes Conductor**: Versions 3.21.21 through 3.30.1; workflow orchestration platform
- **Cisco Identity Services Engine (ISE)**: All versions vulnerable to CVE-2026-76460; network access control and policy management platform
- **Linux Kernel**: Multiple versions affected by CVE-2025-39682 and three additional KEV-listed flaws; plus four additional local privilege escalation flaws with public exploits (patched in recent kernel releases)
- **SolarWinds Access Rights Manager (ARM)**: All versions 2026.2 and prior; Windows-based identity and access governance
- **Azure AI Foundry**: Cloud-based AI development platform; server-side patch deployed by Microsoft
- **TanStack npm Packages**: Malicious versions published to npm registry in May 2026; React query and table libraries
- **npm Package 'indexed-btree'**: Malicious package on npm registry; ongoing campaign
- **Gyazo Platform**: Server infrastructure for image-sharing service; specific component not disclosed
- **WordPress Core**: Versions prior to September 2026 security release; Click2Shell vulnerability chain
- **OpenAI Codex**: Sandbox environment; patched in recent releases
- **OpenAI Help Forum & Login Systems**: Internal OpenAI infrastructure; chained flaws patched
- **AI Coding Agents**: Anthropic Claude Code (< 2.1.179), OpenAI Codex (< 0.146.0), GitHub Copilot (unpatched), and one unnamed agent; Plugin4Shell vulnerability
- **Browser Extensions / AI Assistants**: Chrome, Edge, Opera Neon, Perplexity Comet, Claude in Chrome; BragJack PoC targets extension ecosystem
- **Abandoned CDN Domain**: Thousands of websites, repositories, and documentation pages with hard-coded references
- **GitHub Repositories**: Private repositories compromised via stolen credentials (CrowdSec: 170 repos); also used as C2 by Transparent Tribe

## Attack Vectors and Techniques

- **Unauthenticated Remote Code Execution**: Orkes Conductor (CVE-2026-58138), SolarWinds ARM (CVE-2026-28326), Linux kernel TLS flaw (CVE-2025-39682) — direct network exploitation without credentials
- **Authentication Bypass / Zero-Day**: Cisco ISE (CVE-2026-76460) — API endpoint authentication failure allowing full bypass
- **Supply Chain Compromise (npm)**: TanStack packages (credential-stealing malicious versions), 'indexed-btree' (runtime-behavior evasion) — developer machine compromise via package installation/usage
- **Credential Theft & Reuse**: TanStack attack → GitHub account compromise → private repository exfiltration (CrowdSec); WaterPlum campaign (cryptocurrency theft)
- **Sandbox/Container Escape**: OpenAI Codex (two distinct escape vectors) — host command execution from restricted environment
- **Chained Vulnerability Exploitation**: OpenAI help forum bug + login system weakness → account takeover → internal repo access
- **Prompt Forcing / AI Agent Hijacking**: BragJack — single malicious extension manipulates multiple AI browser agents simultaneously via prompt injection
- **Plugin Swap / Pinned Version Bypass**: Plugin4Shell — repository owner replaces reviewed plugin code after pinning, affecting four AI coding agents
- **Hard-Coded Cryptographic Key**: SolarWinds ARM — static key enables unauthenticated RCE
- **Local Privilege Escalation**: Four Linux kernel flaws with public exploits — local user to root
- **Theme Installation CSRF/Clickjacking Chain**: WordPress Click2Shell — admin interaction with crafted link → unauthorized theme install → RCE chain
- **Rust-Based Malware Tooling**: Transparent Tribe (RUSTYSHADE, RUSTYMOVE, PSNATCH, BASHNATCH) — novel backdoors with GitHub-based C2
- **SEO-Optimized Fake Repositories**: Rapuncel infostealer distribution via GitHub search poisoning
- **Abandoned Infrastructure Takeover**: Expired CDN domain re-registration — passive supply chain risk to thousands of dependents
- **Ransomware Gang Infrastructure Attack**: ShinyHunters breaching Clop leak site — Tor service compromise, onion key theft
- **AI Model Agency Misuse**: Gemini accessing real systems during security test — configuration error enabling unintended external access

## Threat Actor Activities

- **WaterPlum (North Korea)**: Sustained global campaign (Dec 2025 – Jul 2026) compromising 30,000+ devices, stealing $10.7M+ in cryptocurrency; joint law enforcement advisory issued; financially motivated state-sponsored activity
- **Transparent Tribe / APT36 / Earth Karkaddan (Pakistan-aligned)**: Active espionage campaign targeting government and defense entities in India and Afghanistan; novel Rust-based toolset (RUSTYSHADE, RUSTYMOVE, PSNATCH, BASHNATCH); private GitHub repositories used for C2; attributed by Zscaler ThreatLabz
- **ShinyHunters**: Extortion gang; breached Clop ransomware leak site on Tor; defaced site, stole server data and onion private keys; threatening to extort Clop; opportunistic targeting of criminal infrastructure
- **Clop / Cl0p (Ransomware Gang)**: Victim of ShinyHunters breach; leak site compromised; operational disruption
- **Hacktron Researchers**: Security research team; used Claude Opus 5 to chain OpenAI help forum and login flaws; took over OpenAI employee accounts; accessed internal code repository; responsible disclosure implied
- **Forever Security / Gal Weizman**: BragJack PoC developer; Prompt Forcing technique; $20,000+ in bug bounties; two CVEs awarded; defensive research
- **Air Security**: Plugin4Shell researchers; disclosed to Anthropic, OpenAI, GitHub; Claude Code and Codex patched
- **pwn.ai**: WordPress Click2Shell researchers; reported to WordPress; patches released
- **Fortinet**: Reported active exploitation of Orkes Conductor CVE-2026-58138 in the wild
- **CISA**: Added three Linux kernel vulnerabilities to KEV catalog based on active exploitation evidence
- **Irregular (Israeli Security Company)**: Conducted security evaluation where Gemini accessed real systems; domain configuration error
- **Rapuncel Campaign Operators (Unknown)**: SEO-poisoned GitHub repos impersonating legitimate firms; distributing novel infostealer; ongoing
- **Malicious npm Publishers (Unknown)**: 'indexed-btree' runtime evasion campaign; TanStack supply chain attack; ongoing/active