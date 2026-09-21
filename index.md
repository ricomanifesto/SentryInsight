---
schema_version: 2
report_date: 2026-09-21
generated_at: 2026-09-21T20:00:17Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-21/
---
# Exploitation Report

## Executive Summary

Critical exploitation activity this period centers on three actively exploited vulnerabilities now listed in CISA's Known Exploited Vulnerabilities catalog: a critical pre-authentication RCE in Orkes Conductor (CVE-2026-58138), a high-severity unauthenticated RCE in SolarWinds Access Rights Manager (CVE-2026-28326), and three Linux kernel flaws including CVE-2025-39682. These vulnerabilities enable remote code execution without authentication and have confirmed exploitation in the wild, demanding immediate patching.

Simultaneously, North Korean threat actors continue large-scale campaigns. The Contagious Interview operation—attributed to the WaterPlum group—has compromised at least 30,000 devices across more than 100 countries and stolen over $10.7 million in cryptocurrency. A separate Jade Sleet intrusion targeted an Indian IT services provider using FLATROOF and ROOFDECK backdoors, highlighting persistent developer-focused supply chain targeting. New malware delivery techniques include ClickFix social engineering lures deploying the previously undocumented ChainScript RAT, a PowerShell backdoor dubbed TASK#STOMP with extensive data harvesting capabilities, and malicious npm packages that evade runtime defenses.

Emerging attack surfaces involve AI systems and browser-integrated assistants. Researchers demonstrated sandbox escapes from OpenAI's Codex, chainable flaws in OpenAI's authentication systems, and the BragJack technique that hijacks AI browser agents across Chrome, Edge, Opera, and Perplexity via a single malicious extension. A fake LastPass Authenticator installer abused a Microsoft-signed kernel driver to disable antivirus and EDR solutions, while the WordPress Click2Shell CSRF vulnerability gained a public proof-of-concept exploit enabling PHP execution on affected servers.

## Active Exploitation Details

### Critical Pre-Auth RCE in Orkes Conductor Workflow Platform
- **Description**: An unauthenticated remote code execution vulnerability in Orkes Conductor workflow orchestration platform. The flaw exists in versions 3.21.21 through 3.30.1 and allows remote attackers to execute arbitrary code without authentication.
- **Impact**: Full server compromise and arbitrary code execution with the privileges of the Orkes Conductor service, enabling lateral movement, data exfiltration, and persistent access.
- **Status**: Actively exploited in the wild per Fortinet; patched in version 3.30.2.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-58138
- **Reporting**: [The Hacker News — Critical Pre-Auth RCE in Orkes Conductor Workflow Platform Exploited in the Wild](https://thehackernews.com/2026/09/critical-pre-auth-rce-in-orkes.html)

### SolarWinds Access Rights Manager Hard-Coded Key Unauthenticated RCE
- **Description**: A hard-coded cryptographic key flaw in SolarWinds Access Rights Manager (ARM) that enables unauthenticated remote code execution. The vulnerability affects all versions of ARM 2026.2 and prior.
- **Impact**: Unauthenticated attackers can achieve remote code execution on the ARM server, leading to complete compromise of the access rights management infrastructure and potential domain escalation.
- **Status**: Security updates released by SolarWinds; patch available.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: patch
- **CVE IDs**: CVE-2026-28326
- **Reporting**: [The Hacker News — SolarWinds Patches ARM Hard-Coded Key Flaw Enabling Unauthenticated RCE](https://thehackernews.com/2026/09/solarwinds-patches-arm-hard-coded-key.html)

### Linux Kernel Vulnerabilities Exploited in the Wild
- **Description**: Three Linux kernel security flaws added to CISA's Known Exploited Vulnerabilities catalog with evidence of active exploitation. CVE-2025-39682 is an improper check for unusual or exceptional conditions in the TLS receive path with a CVSS score of 9.8.
- **Impact**: Kernel-level code execution, privilege escalation, container escape, and potential full system compromise on affected Linux systems.
- **Status**: Actively exploited per CISA; patches available in upstream kernels and distribution updates.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2025-39682
- **Reporting**: [The Hacker News — CISA Flags Three Linux Kernel Vulnerabilities Exploited in the Wild](https://thehackernews.com/2026/09/cisa-flags-three-linux-kernel.html)

### WordPress Click2Shell CSRF to RCE
- **Description**: A cross-site request forgery (CSRF) vulnerability in WordPress Core dubbed "Click2Shell" that allows attackers to execute arbitrary PHP code on the server. Technical details and a proof-of-concept exploit have been published.
- **Impact**: Remote code execution on WordPress sites via crafted requests that trick authenticated administrators into triggering the vulnerability.
- **Status**: Proof-of-concept exploit publicly available; patch status not specified in source.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: investigate
- **Reporting**: [Bleeping Computer — WordPress Click2Shell flaw lets hackers execute PHP on the server](https://www.bleepingcomputer.com/news/security/wordpress-click2shell-flaw-lets-hackers-execute-php-on-the-server/)

### Fake LastPass Authenticator Installer with Microsoft-Signed Driver
- **Description**: A malicious LastPass Authenticator installer distributed via GitHub that installs a Windows kernel driver signed through Microsoft's hardware compatibility program. The driver disables antivirus and EDR solutions before deploying a password stealer.
- **Impact**: Defense evasion via signed driver, disabling of security controls, credential theft, and potential persistence on compromised endpoints.
- **Status**: Active campaign observed; driver scored zero detections on VirusTotal at time of analysis.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Fake LastPass Authenticator Installer Abuses Microsoft-Signed Driver to Kill Antivirus and EDR](https://thehackernews.com/2026/09/fake-lastpass-authenticator-installer.html)

### Contagious Interview / WaterPlum Campaign
- **Description**: North Korean threat actor campaign (WaterPlum group) compromising at least 30,000 devices across 100+ countries from December 2025 through July 2026, stealing over $10.7 million in cryptocurrency from 7,000+ wallets. Targets web designers, engineers, and cryptocurrency specialists.
- **Impact**: Large-scale device compromise, cryptocurrency theft, credential harvesting, and potential supply chain infiltration via developer targeting.
- **Status**: Ongoing per joint law enforcement advisory; active since December 2025.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Contagious Interview Campaign Compromises 30,000 Devices, Steals $10.71M in Crypto](https://thehackernews.com/2026/09/contagious-interview-campaign.html), [Bleeping Computer — North Korean WaterPlum hackers infected 30,000 devices worldwide](https://www.bleepingcomputer.com/news/security/north-korean-waterplum-hackers-infected-30-000-devices-worldwide/)

### TASK#STOMP PowerShell Backdoor Campaign
- **Description**: A campaign delivering a PowerShell backdoor that automatically harvests business documents, monitors filesystem changes in real time, steals Wi-Fi passwords and clipboard contents, captures screenshots, and accepts arbitrary commands.
- **Impact**: Comprehensive data exfiltration, credential theft, persistent access, and real-time surveillance of compromised hosts.
- **Status**: Active campaign disclosed by researchers; no patch applicable (malware detection/response required).
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — TASK#STOMP PowerShell Backdoor Steals Documents, Wi-Fi Passwords, and Clipboard Data](https://thehackernews.com/2026/09/taskstomp-powershell-backdoor-steals.html)

### ClickFix Social Engineering Delivering ChainScript RAT
- **Description**: ClickFix-style social engineering lures deploying a previously undocumented remote access trojan (ChainScript) that uses the Polygon blockchain to rotate command-and-control infrastructure. ChainScript masquerades as Spotify, Zoom Workplace, and Microsoft Teams software under multiple build names.
- **Impact**: Remote access, command execution, blockchain-based resilient C2, and potential lateral movement.
- **Status**: Active threat actor activity observed by Blackpoint Adversary Pursuit Group.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — ClickFix Lures Deploy ChainScript RAT Using Polygon to Rotate C2 Infrastructure](https://thehackernews.com/2026/09/clickfix-lures-deploy-chainscript-rat.html)

### Jade Sleet Supply Chain Intrusion with FLATROOF/ROOFDECK
- **Description**: North Korean actor Jade Sleet compromised an India-based IT services provider using FLATROOF and ROOFDECK backdoors, targeting developers to breach downstream networks.
- **Impact**: Supply chain compromise, persistent backdoor access, developer environment infiltration, and potential downstream customer impact.
- **Status**: Attributed intrusion disclosed by SentinelOne; active targeting of IT service providers.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — Jade Sleet Linked to Indian IT Provider Breach With FLATROOF and ROOFDECK Backdoors](https://thehackernews.com/2026/09/jade-sleet-linked-to-indian-it-provider.html)

### Malicious npm Package 'indexed-btree' Runtime Evasion
- **Description**: An npm supply chain attack where malicious code executes during normal package runtime rather than in installation scripts, evading defenses that only scan install-time behavior.
- **Impact**: Credential theft, environment variable exfiltration, and potential pipeline compromise for developers and CI/CD systems using the package.
- **Status**: Ongoing campaign; runtime-based evasion technique demonstrated.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Malicious npm packages evade install-script defenses at runtime](https://www.bleepingcomputer.com/news/security/malicious-npm-packages-evade-install-script-defenses-at-runtime/)

### OpenAI Codex Sandbox Escape
- **Description**: Researchers escaped OpenAI's Codex sandbox in two ways, including executing commands on a developer's machine from the most locked-down mode. OpenAI has patched both vectors.
- **Impact**: Container/sandbox escape leading to host command execution, potential access to developer environments and source code.
- **Status**: Patched by OpenAI; research disclosure.
- **Severity**: high
- **Exploitation Status**: not_observed
- **Action**: monitor
- **Reporting**: [Bleeping Computer — Researchers escape OpenAI Codex sandbox to run commands on host](https://www.bleepingcomputer.com/news/security/researchers-escape-openai-codex-sandbox-to-run-commands-on-host/)

### Chained Flaws in OpenAI Authentication Systems
- **Description**: Researchers used Claude Opus 5 to chain two flaws—one in OpenAI's public help forum software and another in OpenAI's login system—to take over ChatGPT and Codex accounts of OpenAI employees and access an internal code repository.
- **Impact**: Account takeover, unauthorized access to internal systems and source code, demonstration of AI-assisted vulnerability chaining.
- **Status**: Security research disclosure; flaws reportedly addressed.
- **Severity**: high
- **Exploitation Status**: not_observed
- **Action**: monitor
- **Reporting**: [The Hacker News — Claude Opus 5 Helped Researchers Take Over OpenAI Staff Accounts via Chained Flaws](https://thehackernews.com/2026/09/claude-opus-5-helped-researchers-take.html)

### BragJack AI Browser Agent Hijacking
- **Description**: Proof-of-concept attack (Prompt Forcing technique) that hijacks AI assistants in Chrome, Edge, Opera Neon, Perplexity Comet, and Claude in Chrome via a single malicious browser extension. Earned over $20,000 in bug bounties and two CVE assignments.
- **Impact**: Full control over AI browser agents, potential data exfiltration, prompt injection, and unauthorized actions via AI assistants with browser access.
- **Status**: Proof-of-concept demonstrated; CVEs assigned but not publicly disclosed in source.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: monitor
- **Reporting**: [Bleeping Computer — BragJack attacks hijack AI browser agents through malicious extensions](https://www.bleepingcomputer.com/news/security/bragjack-attacks-hijack-ai-browser-agents-through-malicious-extensions/)

### TanStack npm Supply Chain Attack
- **Description**: Malicious versions of TanStack npm packages stole credentials from developers, leading to compromise of a CrowdSec employee's GitHub account and exfiltration of approximately 170 private repositories.
- **Impact**: Credential theft, private repository exposure, supply chain compromise, and potential downstream contamination.
- **Status**: Attack occurred in May 2026; discovered September 2026.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — CrowdSec Says TanStack npm Attack Led to Copy of 170 Private GitHub Repositories](https://thehackernews.com/2026/09/crowdsec-says-tanstack-npm-attack-led.html)

### Cisco Zero-Day (Referenced in Weekly Recap)
- **Description**: A zero-day vulnerability in Cisco products referenced in weekly threat recap; specific product and CVE not detailed in source.
- **Impact**: Potential remote code execution or unauthorized access on affected Cisco infrastructure.
- **Status**: Referenced as active zero-day in weekly summary; details not provided in source.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [The Hacker News — ⚡ Weekly Recap: Cisco 0-Day, AI Agent RCE, ClickFix Attacks, ClickFix Surge, and Browser Hijacks](https://thehackernews.com/2026/09/weekly-recap-cisco-0-day-ai-agent-rce.html)

### AI Agent RCE (Referenced in Weekly Recap)
- **Description**: Remote code execution vulnerability in an AI agent system referenced in weekly threat recap; specific platform and CVE not detailed in source.
- **Impact**: Remote code execution via AI agent processing, potentially affecting systems integrating vulnerable AI components.
- **Status**: Referenced as active exploitation in weekly summary; details not provided in source.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [The Hacker News — ⚡ Weekly Recap: Cisco 0-Day, AI Agent RCE, ClickFix Attacks, ClickFix Surge, and Browser Hijacks](https://thehackernews.com/2026/09/weekly-recap-cisco-0-day-ai-agent-rce.html)

### Malware in Torrents for Popular Films
- **Description**: Cybercriminals distributing new malware via torrent files for popular films, with victims identified in Africa including Kenya and Uganda.
- **Impact**: Malware installation on victim systems via social engineering and pirated content downloads.
- **Status**: Active distribution campaign observed.
- **Severity**: medium
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [Dark Reading — Cybercriminals Are Hiding New Malware in Torrents for Popular Films](https://www.darkreading.com/cyberattacks-data-breaches/cybercriminals-hiding-new-malware-torrents-popular-films)

### ShinyHunters Breach of Clop Leak Site
- **Description**: Extortion gang ShinyHunters breached the Clop ransomware operation's data leak site, defacing the Tor site and allegedly stealing server data and onion service private keys.
- **Impact**: Disruption of ransomware operations, potential exposure of victim data held by Clop, escalation of inter-gang conflict.
- **Status**: Active incident; breach claimed by ShinyHunters.
- **Severity**: medium
- **Exploitation Status**: observed
- **Action**: monitor
- **Reporting**: [Bleeping Computer — ShinyHunters hacks Clop leak site, threatens to extort ransomware gang](https://www.bleepingcomputer.com/news/security/shinyhunters-hacks-clop-leak-site-threatens-to-extort-ransomware-gang/)

## Affected Systems and Products

- **Orkes Conductor**: Versions 3.21.21 through 3.30.1; workflow orchestration platform
- **SolarWinds Access Rights Manager**: All versions 2026.2 and prior; Windows-based access rights management
- **Linux Kernel**: Versions containing the flawed TLS receive path (CVE-2025-39682) and two additional undisclosed kernel flaws; all major distributions potentially affected
- **WordPress Core**: Core component affected by Click2Shell CSRF vulnerability; version range not specified in source
- **Windows Systems**: Targeted by fake LastPass installer abusing Microsoft-signed kernel driver; all supported Windows versions potentially vulnerable to driver-based defense evasion
- **Developer Workstations**: Targeted by Contagious Interview/WaterPlum campaign, Jade Sleet intrusion, TanStack npm attack, and malicious npm packages; macOS, Linux, and Windows developer environments
- **AI Development Environments**: OpenAI Codex sandbox (patched), OpenAI authentication systems (help forum and login), AI browser agents in Chrome, Edge, Opera Neon, Perplexity Comet, and Claude in Chrome
- **Cisco Infrastructure**: Unspecified products referenced in zero-day exploitation; networking and security appliances
- **AI Agent Platforms**: Unspecified AI agent system with RCE vulnerability; AI-integrated applications and services
- **BitTorrent Clients**: Users downloading film torrents in Africa (Kenya, Uganda) and potentially other regions
- **Clop Ransomware Infrastructure**: Tor-based data leak site and onion service keys compromised by ShinyHunters

## Attack Vectors and Techniques

- **Unauthenticated Remote Code Execution**: Exploitation of CVE-2026-58138 (Orkes Conductor), CVE-2026-28326 (SolarWinds ARM), and Linux kernel flaws (CVE-2025-39682) for initial access without credentials
- **Cross-Site Request Forgery to RCE**: WordPress Click2Shell flaw chaining CSRF with PHP execution for authenticated administrator compromise
- **Signed Driver Abuse**: Microsoft hardware compatibility program-signed kernel driver used to disable antivirus/EDR before payload deployment
- **ClickFix Social Engineering**: Fake browser/software update prompts tricking users into executing malicious PowerShell commands
- **Blockchain-Based C2 Rotation**: ChainScript RAT using Polygon blockchain transactions to dynamically update command-and-control infrastructure
- **PowerShell Backdoor with Real-Time Monitoring**: TASK#STOMP harvesting documents, Wi-Fi passwords, clipboard, screenshots, and filesystem events
- **Developer-Targeted Supply Chain**: Malicious npm packages (indexed-btree, TanStack) stealing credentials during runtime and build processes
- **AI-Assisted Vulnerability Chaining**: Claude Opus 5 used to identify and chain authentication flaws for account takeover
- **Prompt Forcing / AI Agent Hijacking**: Single malicious browser extension hijacking multiple AI assistants across browsers via prompt injection
- **Sandbox Escape**: Container breakout from OpenAI Codex to host command execution
- **Inter-Gang Compromise**: ShinyHunters breaching Clop ransomware leak site infrastructure via Tor service exploitation
- **Pirated Content Distribution**: Malware bundled in film torrents targeting users seeking copyrighted content
- **North Korean Developer Targeting**: Social engineering via fake interview campaigns (Contagious Interview) and IT service provider compromise (Jade Sleet) to reach downstream networks

## Threat Actor Activities

- **WaterPlum (North Korea)**: Contagious Interview campaign compromising 30,000+ devices across 100+ countries, stealing $10.7M+ in cryptocurrency from 7,000+ wallets; targets web designers, engineers, crypto specialists; active December 2025–July 2026
- **Jade Sleet (North Korea)**: Compromise of Indian IT services provider using FLATROOF and ROOFDECK backdoors; developer-focused supply chain targeting; attributed by SentinelOne
- **ChainScript Operators**: Deploying novel RAT via ClickFix lures with Polygon blockchain C2 rotation; masquerading as legitimate software (Spotify, Zoom, Teams); tracked by Blackpoint APG
- **TASK#STOMP Operators**: PowerShell backdoor campaign with extensive data harvesting capabilities; real-time filesystem monitoring and credential theft
- **ShinyHunters**: Breach and defacement of Clop ransomware leak site; theft of server data and onion service private keys; extortion gang targeting ransomware operators
- **TanStack Supply Chain Attackers**: Compromised npm packages stealing developer credentials; led to CrowdSec GitHub compromise and 170 private repository exfiltration
- **Fake LastPass Distributors**: GitHub-hosted malicious installer with Microsoft-signed driver for defense evasion; password stealer deployment
- **Torrent Malware Distributors**: Campaign targeting African users (Kenya, Uganda) via film torrents; unspecified malware payload
- **Cisco Zero-Day Exploiters**: Unidentified actors exploiting undisclosed Cisco vulnerability; referenced in weekly threat intelligence
- **AI Agent RCE Exploiters**: Unidentified actors exploiting RCE in unspecified AI agent platform; referenced in weekly threat intelligence
- **OpenAI Security Researchers (Hacktron)**: Authorized security research demonstrating Codex sandbox escape and chained authentication flaws; coordinated disclosure
- **BragJack Researcher (Gal Weizman / Forever Security)**: Proof-of-concept development for AI browser agent hijacking via Prompt Forcing; bug bounty awards and CVE assignments