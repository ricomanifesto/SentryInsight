---
schema_version: 2
report_date: 2026-09-21
generated_at: 2026-09-21T12:35:10Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-21/
---
# Exploitation Report

## Executive Summary

Critical exploitation activity spans multiple high-impact vulnerabilities across enterprise infrastructure, AI platforms, and supply chains. CISA has added three Linux kernel flaws to its Known Exploited Vulnerabilities catalog, confirming active exploitation of CVE-2025-39682 (CVSS 9.8) and two additional kernel vulnerabilities. A critical pre-authentication RCE in Orkes Conductor (CVE-2026-58138, CVSS 9.8) is being actively exploited in the wild, while a maximum-severity authentication bypass in Cisco Identity Services Engine (CVE-2026-76460, CVSS 10.0) represents a zero-day threat to network access control systems.

Simultaneously, threat actors are advancing supply chain and AI-enabled attack techniques. North Korean groups Jade Sleet and WaterPlum continue prolific campaigns—Jade Sleet deploying FLATROOF and ROOFDECK backdoors against IT service providers, while WaterPlum has compromised over 30,000 devices globally and exfiltrated $10.7 million in cryptocurrency. The ShinyHunters extortion gang breached the Clop ransomware leak site, and Transparent Tribe (APT36) deployed novel Rust-based backdoors targeting government entities in India and Afghanistan. Malicious npm packages are evading runtime defenses, and researchers demonstrated AI-assisted vulnerability chaining using Claude Opus 5 to compromise OpenAI staff accounts.

Microsoft and SolarWinds have released patches for critical flaws: Azure AI Foundry privilege escalation (CVE-2026-85889, CVSS 10.0) requires no customer action, while SolarWinds Access Rights Manager (CVE-2026-28326, CVSS 8.8) demands immediate updating. Public exploit code for four additional Linux kernel local-root vulnerabilities increases urgency for kernel patching. The ClickFix social engineering technique continues to deliver the ChainScript RAT, and the BragJack "Prompt Forcing" attack hijacks AI browser agents via malicious extensions. Gyazo confirmed a server flaw exploited to steal 23.6 million user records.

## Active Exploitation Details

### SolarWinds Access Rights Manager Hard-Coded Key RCE
- **Description**: A hard-coded cryptographic key in SolarWinds Access Rights Manager (ARM) allows unauthenticated remote code execution. The flaw exists in all versions 2026.2 and prior.
- **Impact**: Unauthenticated attackers can achieve remote code execution on affected ARM installations, potentially leading to full system compromise and lateral movement within identity management infrastructure.
- **Status**: Patched by SolarWinds; security updates released addressing the vulnerability.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: patch
- **CVE IDs**: CVE-2026-28326
- **Reporting**: [The Hacker News — SolarWinds Patches ARM Hard-Coded Key Flaw Enabling Unauthenticated RCE](https://thehackernews.com/2026/09/solarwinds-patches-arm-hard-coded-key.html)

### Orkes Conductor Pre-Authentication RCE
- **Description**: An unauthenticated remote code execution vulnerability in Orkes Conductor workflow platform versions 3.21.21 before 3.30.2. The flaw allows remote attackers to execute arbitrary code without authentication.
- **Impact**: Full remote code execution on Orkes Conductor servers, enabling attackers to compromise workflow orchestration infrastructure, access sensitive data, and pivot to connected systems.
- **Status**: Actively exploited in the wild per Fortinet; patched in version 3.30.2.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-58138
- **Reporting**: [The Hacker News — Critical Pre-Auth RCE in Orkes Conductor Workflow Platform Exploited in the Wild](https://thehackernews.com/2026/09/critical-pre-auth-rce-in-orkes.html)

### Linux Kernel TLS Receive Path Vulnerability
- **Description**: An improper check for unusual or exceptional conditions in the TLS receive path of the Linux kernel. This is one of three kernel vulnerabilities added to CISA's KEV catalog with evidence of active exploitation.
- **Impact**: Kernel-level exploitation potentially leading to privilege escalation, container escape, or system compromise on affected Linux systems.
- **Status**: Added to CISA KEV catalog indicating active exploitation; kernel maintainers have released fixes.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2025-39682
- **Reporting**: [The Hacker News — CISA Flags Three Linux Kernel Vulnerabilities Exploited in the Wild](https://thehackernews.com/2026/09/cisa-flags-three-linux-kernel.html)

### Cisco Identity Services Engine Authentication Bypass
- **Description**: An authentication bypass flaw in Cisco Identity Services Engine (ISE) API endpoints, rated maximum severity. The zero-day allows unauthenticated attackers to bypass authentication controls.
- **Impact**: Complete bypass of authentication on Cisco ISE, potentially allowing unauthorized network access control changes, policy manipulation, and network compromise.
- **Status**: Zero-day vulnerability disclosed; CVSS 10.0 indicates maximum severity.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: patch
- **CVE IDs**: CVE-2026-76460
- **Reporting**: [Dark Reading — Cisco Zero-Day Highlights API Endpoint Authentication Issues](https://www.darkreading.com/vulnerabilities-threats/cisco-zero-day-api-endpoint-authentication-issues)

### Azure AI Foundry Privilege Escalation
- **Description**: Missing authentication for a critical function in Azure AI Foundry allows unauthorized privilege escalation over the network. Microsoft has deployed fixes with no customer action required.
- **Impact**: Unauthorized attackers could elevate privileges within Azure AI Foundry environments, potentially accessing sensitive AI models, training data, and connected resources.
- **Status**: Patched by Microsoft; no customer action required per advisory.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: monitor
- **CVE IDs**: CVE-2026-85889
- **Reporting**: [The Hacker News — Microsoft Patches CVSS 10.0 Azure AI Foundry Flaw Enabling Unauthorized Privilege Escalation](https://thehackernews.com/2026/09/microsoft-patches-cvss-100-azure-ai.html)

### ClickFix Social Engineering Delivering ChainScript RAT
- **Description**: Threat actors use ClickFix-like lures (fake software updates, CAPTCHA pages) to deliver ChainScript, a previously undocumented remote access trojan. The malware rotates C2 infrastructure using the Polygon blockchain.
- **Impact**: Full remote access to victim systems, data exfiltration, credential theft, and persistent foothold via blockchain-resilient C2.
- **Status**: Active campaign observed by Blackpoint APG; ChainScript appears under multiple build names masquerading as legitimate software (Spotify, Zoom, Teams).
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — ClickFix Lures Deploy ChainScript RAT Using Polygon to Rotate C2 Infrastructure](https://thehackernews.com/2026/09/clickfix-lures-deploy-chainscript-rat.html)

### Jade Sleet FLATROOF and ROOFDECK Backdoor Campaign
- **Description**: North Korean threat actor Jade Sleet compromised an India-based IT services provider using Apple Developer ID-signed malware (FLATROOF and ROOFDECK backdoors) targeting developers to breach downstream networks.
- **Impact**: Supply chain compromise via trusted IT provider, developer system infiltration, and potential access to customer networks through trusted relationships.
- **Status**: Active campaign disclosed by SentinelOne; infrastructure and tooling documented.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Jade Sleet Linked to Indian IT Provider Breach With FLATROOF and ROOFDECK Backdoors](https://thehackernews.com/2026/09/jade-sleet-linked-to-indian-it-provider.html)

### WaterPlum Global Device Compromise
- **Description**: North Korean WaterPlum hackers compromised at least 30,000 devices worldwide from December 2025 through July 2026, transferring over $10.7 million in stolen cryptocurrency to North Korea.
- **Impact**: Massive-scale device compromise, cryptocurrency theft, and financial funding of North Korean regime operations.
- **Status**: Joint law enforcement advisory confirms active exploitation at scale; campaign spanned 8+ months.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — North Korean WaterPlum hackers infected 30,000 devices worldwide](https://www.bleepingcomputer.com/news/security/north-korean-waterplum-hackers-infected-30-000-devices-worldwide/)

### Malicious npm Package Runtime Evasion
- **Description**: The 'indexed-btree' npm package hides malicious code in normal runtime behavior rather than installation scripts, evading supply chain defenses that only scan install-time scripts.
- **Impact**: Supply chain compromise of Node.js projects; runtime data exfiltration, credential theft, and potential deployment of additional payloads.
- **Status**: Ongoing campaign; demonstrates fundamental gap in current npm security tooling.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Malicious npm packages evade install-script defenses at runtime](https://www.bleepingcomputer.com/news/security/malicious-npm-packages-evade-install-script-defenses-at-runtime/)

### TanStack npm Supply Chain Attack
- **Description**: Malicious versions of TanStack npm packages stole credentials from developer machines, leading to compromise of a CrowdSec employee's GitHub account and exfiltration of 170 private repositories.
- **Impact**: Credential theft, source code exfiltration, supply chain contamination, and potential downstream attacks via compromised packages.
- **Status**: Confirmed breach in May 2026; CrowdSec disclosed in September 2026.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — CrowdSec Says TanStack npm Attack Led to Copy of 170 Private GitHub Repositories](https://thehackernews.com/2026/09/crowdsec-says-tanstack-npm-attack-led.html)

### BragJack Prompt Forcing via Malicious Extensions
- **Description**: Proof-of-concept attack hijacking AI browser agents (Chrome, Edge, Opera Neon, Perplexity Comet, Claude in Chrome) through a single malicious extension using "Prompt Forcing" technique.
- **Impact**: Complete control over AI assistant interactions, potential data exfiltration, action injection, and bypass of AI safety controls across multiple browser platforms.
- **Status**: Proof-of-concept demonstrated; earned $20,000+ in bug bounties and two CVE assignments (CVE IDs not publicly disclosed in source).
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: monitor
- **Reporting**: [Bleeping Computer — BragJack attacks hijack AI browser agents through malicious extensions](https://www.bleepingcomputer.com/news/security/bragjack-attacks-hijack-ai-browser-agents-through-malicious-extensions/)

### Gyazo Server Flaw Data Breach
- **Description**: Hackers exploited a server vulnerability in the Gyazo image-sharing platform to steal 23.6 million user records.
- **Impact**: Massive data breach exposing user records; platform confirmed the exploitation.
- **Status**: Breach confirmed by Gyazo; vulnerability exploited in the wild.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Gyazo server flaw exploited to steal 23.6 million user records](https://www.bleepingcomputer.com/news/security/gyazo-server-flaw-exploited-to-steal-236-million-user-records/)

### Transparent Tribe Rust Backdoor Deployment
- **Description**: Pakistan-aligned APT36 (Transparent Tribe) deployed novel Rust-based backdoors (RUSTYSHADE, RUSTYMOVE, PSNATCH, BASHNATCH) using private GitHub repositories for C2, targeting government and defense entities in India and Afghanistan.
- **Impact**: Persistent access to sensitive government networks, data exfiltration, and espionage via modern Rust tooling evading traditional detection.
- **Status**: Active campaign attributed by Zscaler ThreatLabz; codenamed Operation (name truncated in source).
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Transparent Tribe Deploys New Rust Backdoor Using Private GitHub Repositories for C2](https://thehackernews.com/2026/09/transparent-tribe-deploys-new-rust.html)

### WordPress Click2Shell Theme Installation Chain
- **Description**: WordPress core vulnerability allowing a crafted link opened by a logged-in administrator to install a theme from WordPress.org without user interaction, chainable to code execution.
- **Impact**: Unauthorized theme installation leading to potential remote code execution via malicious themes; requires admin interaction but no explicit install click.
- **Status**: Patched by WordPress; reported by pwn.ai researchers.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — New WordPress Click2Shell Flaw Forces Theme Installs, Can Chain to Code Execution](https://thehackernews.com/2026/09/new-wordpress-click2shell-flaw-forces.html)

### OpenAI Codex Sandbox Escape
- **Description**: Researchers escaped OpenAI's Codex sandbox in two ways, including running commands on a developer's machine from the most locked-down mode.
- **Impact**: Sandbox escape allowing host command execution from AI coding agent; potential supply chain risk for developers using Codex.
- **Status**: Both vulnerabilities patched by OpenAI after responsible disclosure.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: monitor
- **Reporting**: [Bleeping Computer — Researchers escape OpenAI Codex sandbox to run commands on host](https://www.bleepingcomputer.com/news/security/researchers-escape-openai-codex-sandbox-to-run-commands-on-host/)

### AI-Assisted Vulnerability Chaining Against OpenAI
- **Description**: Researchers used Anthropic's Claude Opus 5 to chain two flaws—a bug in OpenAI's public help forum software and a weakness in OpenAI's login system—to take over ChatGPT/Codex accounts of OpenAI employees and access an internal code repository.
- **Impact**: Demonstration of AI-accelerated vulnerability discovery and chaining; compromise of internal systems via chained web application flaws.
- **Status**: Security research exercise; vulnerabilities disclosed and presumably patched.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — Claude Opus 5 Helped Researchers Take Over OpenAI Staff Accounts via Chained Flaws](https://thehackernews.com/2026/09/claude-opus-5-helped-researchers-take.html)

### Rapuncel Infostealer via Fake GitHub Repositories
- **Description**: SEO-optimized fake GitHub repositories impersonating legitimate software firms (including LastPass Authenticator) deliver the previously undocumented Rapuncel information stealer.
- **Impact**: Credential theft, browser data exfiltration, cryptocurrency wallet compromise, and persistent malware installation via social engineering and supply chain deception.
- **Status**: Ongoing malware campaign; repositories optimized for search visibility.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Fake LastPass Authenticator GitHub repos push new Rapuncel infostealer](https://www.bleepingcomputer.com/news/security/fake-lastpass-authenticator-github-repos-push-new-rapuncel-infostealer/)

### ShinyHunters Compromise of Clop Leak Site
- **Description**: ShinyHunters extortion gang breached the Clop ransomware operation's Tor-based data leak site, defacing it and allegedly stealing server data and onion service private keys.
- **Impact**: Disruption of ransomware operations, potential exposure of victim data held by Clop, and escalation of inter-gang conflict in cybercrime ecosystem.
- **Status**: Active breach confirmed; Tor site defaced and infrastructure compromised.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: monitor
- **Reporting**: [Bleeping Computer — ShinyHunters hacks Clop leak site, threatens to extort ransomware gang](https://www.bleepingcomputer.com/news/security/shinyhunters-hacks-clop-leak-site-threatens-to-extort-ransomware-gang/)

### Linux Kernel Local-Root Exploits (Public)
- **Description**: Security researcher released working exploit code for four Linux kernel flaws each allowing local users to gain root privileges. All four have been fixed in recent kernel updates.
- **Impact**: Local privilege escalation to root on unpatched systems; public exploit availability increases risk for outdated kernels.
- **Status**: Exploits public; patches available in upstream kernels.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — Public Exploits Released for Four Linux Kernel Flaws That Enable Local Root](https://thehackernews.com/2026/09/public-exploits-released-for-four-linux.html)

## Affected Systems and Products

- **SolarWinds Access Rights Manager**: All versions 2026.2 and prior; Windows/Linux platforms running ARM
- **Orkes Conductor**: Versions 3.21.21 through 3.30.1; workflow orchestration platforms
- **Linux Kernel**: Multiple versions affected by CVE-2025-39682 and three additional KEV-listed flaws; four additional local-root flaws with public exploits; all major distributions
- **Cisco Identity Services Engine (ISE)**: Versions affected by CVE-2026-76460; network access control appliances
- **Microsoft Azure AI Foundry**: Cloud-hosted AI development platform; server-side patch deployed
- **WordPress Core**: Versions prior to September 2026 security release; all installations with admin users
- **Gyazo Platform**: Server infrastructure; image-sharing service backend
- **npm Ecosystem**: 'indexed-btree' package and malicious TanStack package versions; Node.js development environments
- **OpenAI Codex**: Sandbox environment; developer machines using Codex agent
- **Browser AI Extensions**: Chrome, Edge, Opera Neon, Perplexity Comet, Claude in Chrome; extension-enabled browsers
- **Apple Developer Ecosystem**: Developer IDs abused for code signing of FLATROOF/ROOFDECK malware
- **GitHub**: Private repositories accessed via compromised employee credentials; repository hosting platform

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: Fake browser updates, CAPTCHA challenges, and error pages trick users into executing malicious PowerShell commands that deploy ChainScript RAT; leverages Polygon blockchain for C2 rotation resilience
- **Supply Chain Compromise via npm**: Malicious packages evade install-script scanning by hiding payloads in runtime behavior (indexed-btree); typo-squatted or compromised legitimate packages (TanStack) steal developer credentials and GitHub tokens
- **AI-Assisted Vulnerability Discovery**: Researchers used Claude Opus 5 to identify and chain web application flaws (forum software bug + login system weakness) for account takeover and internal repository access
- **Prompt Forcing / BragJack**: Single malicious browser extension hijacks AI assistants across multiple browsers by injecting prompts that override AI safety controls and exfiltrate data
- **Sandbox Escape**: Codex sandbox breakout via two distinct methods achieving host command execution from locked-down AI coding agent mode
- **Unauthenticated RCE via Hard-Coded Keys**: SolarWinds ARM flaw exploits static cryptographic material to bypass authentication and achieve remote code execution
- **Pre-Auth RCE in Workflow Platform**: Orkes Conductor vulnerability allows unauthenticated code execution on workflow orchestration servers
- **Kernel-Level Exploitation**: Linux kernel TLS receive path flaw (CVE-2025-39682) and three additional KEV-listed vulnerabilities exploited for privilege escalation/container escape; four local-root exploits publicly released
- **Authentication Bypass in NAC**: Cisco ISE API endpoint flaw (CVE-2026-76460) allows complete authentication bypass on network access control system
- **Privilege Escalation in AI Platform**: Azure AI Foundry missing authentication for critical function (CVE-2026-85889) enables unauthorized privilege elevation
- **Click2Shell Chain**: WordPress vulnerability forces theme installation via crafted admin link, chainable to RCE through malicious theme deployment
- **Server-Side Vulnerability Exploitation**: Gyazo server flaw exploited for mass data exfiltration (23.6M records)
- **Rust-Based Malware Tooling**: Transparent Tribe deploys RUSTYSHADE, RUSTYMOVE, PSNATCH, BASHNATCH backdoors using private GitHub repositories for C2, targeting government/defense sectors
- **SEO-Optimized Fake Repositories**: Rapuncel infostealer distributed via GitHub repositories impersonating legitimate software (LastPass Authenticator) with search optimization
- **Ransomware Gang Infrastructure Compromise**: ShinyHunters breached Clop's Tor leak site, stole onion keys and server data, defacing the extortion platform
- **OAuth Consent Abuse**: Attackers exploit OAuth consent flows to bypass MFA and gain persistent application access without credential theft

## Threat Actor Activities

- **Jade Sleet (North Korea)**: Attributed to compromise of India-based IT services provider using Apple Developer ID-signed FLATROOF and ROOFDECK backdoors; targets developers for supply chain access to downstream networks; disclosed by SentinelOne
- **WaterPlum (North Korea)**: Compromised 30,000+ devices globally (Dec 2025–Jul 2026), exfiltrated $10.7M+ in cryptocurrency to North Korea; joint law enforcement advisory issued
- **Transparent Tribe / APT36 / Earth Karkaddan (Pakistan-aligned)**: Deploying novel Rust-based backdoors (RUSTYSHADE, RUSTYMOVE, PSNATCH, BASHNATCH) via private GitHub C2; targeting government and defense entities in India and Afghanistan; Zscaler ThreatLabz attribution
- **ShinyHunters (Extortion Gang)**: Breached Clop ransomware leak site on Tor, defaced platform, allegedly stole server data and onion service private keys; escalating cybercrime gang conflict
- **Clop / Cl0p (Ransomware Operation)**: Victim of ShinyHunters breach; leak site infrastructure compromised
- **ClickFix Operators (Unattributed)**: Delivering ChainScript RAT via ClickFix social engineering lures masquerading as Spotify, Zoom, Teams software; using Polygon blockchain for C2 rotation; tracked by Blackpoint APG
- **TanStack npm Attackers (Unattributed)**: Injected malicious code into TanStack npm packages to steal developer credentials; led to CrowdSec GitHub compromise and 170 private repository exfiltration
- **Rapuncel Operators (Unattributed)**: Distributing novel infostealer via SEO-optimized fake GitHub repositories impersonating LastPass Authenticator and other legitimate software
- **Researchers (Hacktron, Forever Security, OpenAI/Codex researchers)**: Demonstrated AI-assisted vulnerability chaining (Claude Opus 5), Codex sandbox escapes, and BragJack Prompt Forcing; responsible disclosure to affected vendors
- **Fortinet Threat Researchers**: Identified active exploitation of Orkes Conductor CVE-2026-58138 in the wild
- **CISA**: Added three Linux kernel vulnerabilities to KEV catalog based on active exploitation evidence