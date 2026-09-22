---
schema_version: 2
report_date: 2026-09-22
generated_at: 2026-09-22T04:44:33Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-22/
---
# Exploitation Report

## Executive Summary

CISA has issued an urgent alert confirming active exploitation of three Linux kernel vulnerabilities, one rated critical, demanding immediate patching across affected systems. Simultaneously, North Korean threat actors—tracked as WaterPlum and Jade Sleet—are conducting large-scale campaigns: WaterPlum's Contagious Interview operation has compromised at least 30,000 devices across more than 100 countries, stealing over $10.7 million in cryptocurrency, while Jade Sleet breached an Indian IT provider using FLATROOF and ROOFDECK backdoors.

Multiple additional active campaigns include ClickFix lures deploying the novel ChainScript RAT with blockchain-based C2 rotation, the TASK#STOMP PowerShell backdoor harvesting documents and credentials, malicious npm packages evading runtime defenses, and a fake LastPass installer abusing a Microsoft-signed driver to disable security tools.

## Active Exploitation Details

### Linux Kernel Vulnerabilities (CISA Alert)
- **Description**: Three vulnerabilities in the Linux kernel are being actively exploited in the wild. CISA has added these to the Known Exploited Vulnerabilities catalog, with one flaw rated critical severity.
- **Impact**: Successful exploitation could allow attackers to achieve privilege escalation, container escape, or kernel-level code execution on affected Linux systems.
- **Status**: Actively exploited per CISA; patches available from upstream kernel maintainers and distribution vendors.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — CISA alerts of active exploitation of three Linux kernel flaws](https://www.bleepingcomputer.com/news/security/cisa-alerts-of-active-exploitation-of-three-linux-kernel-flaws/)

### SolarWinds Access Rights Manager Hard-Coded Key (CVE-2026-28326)
- **Description**: A hard-coded cryptographic key in SolarWinds Access Rights Manager (ARM) versions 2026.2 and prior enables unauthenticated remote code execution. The flaw carries a CVSS 8.8 (High) rating.
- **Impact**: Unauthenticated attackers can execute arbitrary code on the ARM server, leading to full system compromise and potential lateral movement.
- **Status**: Security updates released by SolarWinds addressing the vulnerability.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-28326
- **Reporting**: [The Hacker News — SolarWinds Patches ARM Hard-Coded Key Flaw Enabling Unauthenticated RCE](https://thehackernews.com/2026/09/solarwinds-patches-arm-hard-coded-key.html)

### WordPress Click2Shell CSRF Vulnerability
- **Description**: A cross-site request forgery (CSRF) vulnerability in WordPress Core, dubbed "Click2Shell," allows attackers to execute arbitrary PHP code on the server. Technical details and a proof-of-concept exploit have been publicly published.
- **Impact**: Attackers can trick authenticated administrators into triggering malicious requests that result in remote code execution on the WordPress server.
- **Status**: PoC available; no vendor patch mentioned in reporting.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — WordPress Click2Shell flaw lets hackers execute PHP on the server](https://www.bleepingcomputer.com/news/security/wordpress-click2shell-flaw-lets-hackers-execute-php-on-the-server/)

### Fake LastPass Authenticator Installer with Microsoft-Signed Driver
- **Description**: A malicious GitHub-hosted installer masquerading as LastPass Authenticator deploys a Microsoft-signed Windows kernel driver that terminates antivirus and EDR processes before executing a password-stealing payload. The driver had zero detections on VirusTotal at time of analysis.
- **Impact**: Complete bypass of endpoint protection, credential theft, and potential further compromise of victim systems.
- **Status**: Active distribution via GitHub; Microsoft signature validation complicates detection.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Fake LastPass Authenticator Installer Abuses Microsoft-Signed Driver to Kill Antivirus and EDR](https://thehackernews.com/2026/09/fake-lastpass-authenticator-installer.html)

### Contagious Interview / WaterPlum Campaign
- **Description**: North Korean threat actors (WaterPlum) operate the Contagious Interview campaign targeting web designers, engineers, and cryptocurrency specialists through social engineering and malicious applications.
- **Impact**: At least 30,000 devices compromised across 100+ countries; over 7,000 cryptocurrency wallets drained totaling $10.71 million; business documents, Wi-Fi passwords, clipboard data, and screenshots exfiltrated.
- **Status**: Ongoing campaign from December 2025 through July 2026 per joint law enforcement advisory.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Contagious Interview Campaign Compromises 30,000 Devices, Steals $10.71M in Crypto](https://thehackernews.com/2026/09/contagious-interview-campaign.html), [Bleeping Computer — North Korean WaterPlum hackers infected 30,000 devices worldwide](https://www.bleepingcomputer.com/news/security/north-korean-waterplum-hackers-infected-30-000-devices-worldwide/)

### ClickFix / ChainScript RAT Campaign
- **Description**: Threat actors use ClickFix-style social engineering lures to deploy ChainScript, a previously undocumented remote access trojan that rotates command-and-control infrastructure via the Polygon blockchain. ChainScript masquerades as legitimate software (Spotify, Zoom Workplace, Microsoft Teams) under multiple build names.
- **Impact**: Persistent remote access, data theft, and resilient C2 infrastructure resistant to traditional takedowns.
- **Status**: Active campaign observed by Blackpoint Adversary Pursuit Group.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — ClickFix Lures Deploy ChainScript RAT Using Polygon to Rotate C2 Infrastructure](https://thehackernews.com/2026/09/clickfix-lures-deploy-chainscript-rat.html)

### Jade Sleet Supply Chain Breach (FLATROOF / ROOFDECK)
- **Description**: North Korean actor Jade Sleet compromised an India-based IT services provider, deploying FLATROOF and ROOFDECK backdoors to breach downstream target networks through the software supply chain.
- **Impact**: Developer-focused intrusion enabling lateral movement to client environments; highlights persistent targeting of software supply chains by DPRK actors.
- **Status**: Active intrusion disclosed by SentinelOne; attribution to Jade Sleet.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Jade Sleet Linked to Indian IT Provider Breach With FLATROOF and ROOFDECK Backdoors](https://thehackernews.com/2026/09/jade-sleet-linked-to-indian-it-provider.html)

### TASK#STOMP PowerShell Backdoor Campaign
- **Description**: A campaign delivering a sophisticated PowerShell backdoor that automatically harvests business documents, monitors filesystem changes in real time, steals Wi-Fi passwords and clipboard contents, captures screenshots, and accepts arbitrary commands.
- **Impact**: Comprehensive data exfiltration and persistent access to compromised hosts.
- **Status**: Active campaign disclosed by researchers.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — TASK#STOMP PowerShell Backdoor Steals Documents, Wi-Fi Passwords, and Clipboard Data](https://thehackernews.com/2026/09/taskstomp-powershell-backdoor-steals.html)

### Malicious npm Package Campaign (indexed-btree)
- **Description**: An ongoing supply chain attack using the 'indexed-btree' npm package that hides malicious behavior in normal runtime execution rather than installation scripts, evading standard install-script defenses.
- **Impact**: Arbitrary code execution in developer and build environments; supply chain compromise of downstream consumers.
- **Status**: Ongoing campaign observed in the wild.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Malicious npm packages evade install-script defenses at runtime](https://www.bleepingcomputer.com/news/security/malicious-npm-packages-evade-install-script-defenses-at-runtime/)

### ShinyHunters Breach of Clop Ransomware Infrastructure
- **Description**: The ShinyHunters extortion group breached the Clop (Cl0p) ransomware operation's Tor-based leak site, defacing it and allegedly exfiltrating server data and onion service private keys.
- **Impact**: Potential re-extortion of Clop's previous victims; exposure of sensitive victim data and ransomware operational infrastructure.
- **Status**: Active breach with ongoing extortion threats.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [Dark Reading — ShinyHunters Hacked Clop. Now What About Clop's Victims?](https://www.darkreading.com/cyberattacks-data-breaches/shinyhunters-hacked-clop-what-about-clops-victims), [Bleeping Computer — ShinyHunters hacks Clop leak site, threatens to extort ransomware gang](https://www.bleepingcomputer.com/news/security/shinyhunters-hacks-clop-leak-site-threatens-to-extort-ransomware-gang/)

### BragJack AI Browser Agent Hijacking
- **Description**: A proof-of-concept attack technique ("Prompt Forcing") using a single malicious browser extension to hijack AI assistants in Chrome, Edge, Opera Neon, Perplexity Comet, and Claude in Chrome. The research earned over $20,000 in bounties and two CVE assignments.
- **Impact**: Full control over AI browser agents, enabling data exfiltration, unauthorized actions, and prompt injection across multiple AI platforms.
- **Status**: Proof-of-concept demonstrated; two CVEs assigned but not publicly disclosed in reporting.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: monitor
- **Reporting**: [Bleeping Computer — BragJack attacks hijack AI browser agents through malicious extensions](https://www.bleepingcomputer.com/news/security/bragjack-attacks-hijack-ai-browser-agents-through-malicious-extensions/)

## Affected Systems and Products

- **Linux Kernel**: All distributions running vulnerable kernel versions; specific versions not detailed in CISA alert
- **SolarWinds Access Rights Manager**: Versions 2026.2 and prior
- **WordPress Core**: Versions affected by Click2Shell CSRF; specific version range not disclosed in reporting
- **Windows Systems**: Targeted by fake LastPass installer abusing Microsoft-signed kernel driver
- **Developer Workstations**: Targeted by Contagious Interview, Jade Sleet, TASK#STOMP, and malicious npm packages across Windows, macOS, and Linux
- **Cryptocurrency Wallets**: Over 7,000 wallets compromised in Contagious Interview campaign
- **Browser Extensions**: Chrome, Edge, Opera Neon, Perplexity Comet vulnerable to BragJack extension-based hijack
- **AI Assistant Platforms**: Chrome AI, Edge Copilot, Opera Neon, Perplexity Comet, Claude in Chrome affected by BragJack

## Attack Vectors and Techniques

- **Kernel Exploitation**: Active exploitation of Linux kernel flaws for privilege escalation and container escape
- **Hard-Coded Cryptographic Key**: Unauthenticated RCE via static key in SolarWinds ARM authentication mechanism
- **Cross-Site Request Forgery (CSRF)**: Click2Shell exploits WordPress Core CSRF to achieve PHP code execution via admin interaction
- **Signed Driver Abuse**: Microsoft WHQL-signed kernel driver used to disable AV/EDR before payload execution
- **ClickFix Social Engineering**: Deceptive UI lures (fake CAPTCHAs, error messages) trick users into executing PowerShell commands
- **Blockchain-Based C2 Rotation**: ChainScript RAT uses Polygon blockchain transactions to dynamically update C2 endpoints
- **Supply Chain Compromise**: Jade Sleet breaches IT provider to reach downstream targets; npm packages poison runtime behavior
- **Malicious Browser Extensions**: Single extension hijacks multiple AI assistants via prompt injection ("Prompt Forcing")
- **PowerShell Living-off-the-Land**: TASK#STOMP uses native PowerShell for fileless persistence, data collection, and C2
- **Credential Theft & Cryptocurrency Drainage**: Automated harvesting of wallet credentials, private keys, and direct fund transfers
- **Ransomware Gang Infrastructure Compromise**: ShinyHunters breaches Clop leak site, steals onion keys for re-extortion

## Threat Actor Activities

- **WaterPlum (North Korea)**: Operates Contagious Interview campaign; 30,000+ devices compromised globally; $10.7M+ cryptocurrency stolen; targets developers and crypto specialists via social engineering and trojanized applications
- **Jade Sleet (North Korea)**: Attributed to Indian IT provider breach; deploys FLATROOF and ROOFDECK backdoors; focuses on software supply chain infiltration to access downstream customers
- **ShinyHunters**: Extortion group that breached Clop ransomware leak site; defaced Tor infrastructure; threatens re-extortion of Clop's victim database using stolen onion keys
- **Contagious Interview Operators**: North Korean-aligned; uses fake interview processes and coding challenges to deliver malware; employs TASK#STOMP backdoor for persistent data theft
- **ChainScript/ClickFix Actors**: Unknown attribution; leverages ClickFix lures and blockchain (Polygon) for resilient C2; masquerades malware as legitimate software installers
- **npm Campaign Actors**: Unknown; publishes malicious packages (indexed-btree) that evade install-script scanning by hiding payload in runtime behavior
- **Fake LastPass Distributors**: Unknown; hosts malicious installer on GitHub; leverages Microsoft-signed driver for defense evasion; delivers password stealer payload