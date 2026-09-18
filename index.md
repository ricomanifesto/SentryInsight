---
schema_version: 2
report_date: 2026-09-18
generated_at: 2026-09-18T16:15:59Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-18/
---
# Exploitation Report

## Executive Summary

Multiple active exploitation campaigns are underway across diverse attack surfaces, from supply-chain compromises and infrastructure vulnerabilities to AI-powered malware and state-sponsored espionage. The most impactful incident involves the confirmed breach of Gyazo's image-sharing platform, where a server vulnerability was exploited to exfiltrate 23.6 million user records. Simultaneously, a supply-chain attack against Brevo resulted in malicious ClickFix scripts being injected into customer sites via a compromised Cloudflare API key, distributing malware to downstream victims.

State-aligned threat actors continue aggressive operations: Pakistan-linked Transparent Tribe (APT36) is deploying novel Rust-based backdoors against government and defense targets in India and Afghanistan, while China-linked FamousSparrow conducts political espionage in Latin America and Iran-linked Handala Hack operates the HEAVYGRAM Telegram backdoor for surveillance. On the cybercrime front, multiple infostealer campaigns—Rapuncel via fake GitHub repositories, WeaselBiscuit through 13 malicious npm packages, and PhantomRaven likely built with LLM assistance—are actively harvesting credentials and browser data. Emerging threats include AI-driven attacks, with a confirmed breach of a Spanish organization by an AI agent that modified personal data, and RatHat Android malware using AI to automate device control via ADB persistence.

Critical vulnerabilities have been disclosed in foundational infrastructure: a CVSS 10.0 flaw in Azure AI Foundry (CVE-2026-85889), a critical heap overflow in Unbound's DNSSEC validator (CVE-2026-81642), a critical Docker Sandboxes escape on macOS (CVE-2026-77179), and a critical Check Point Management Server flaw allowing unauthenticated root code execution. While patches exist for all four, only the Check Point flaw has explicit confirmation of no observed wild exploitation; the others lack exploitation status reporting. An abandoned CDN domain re-registration affects thousands of sites still referencing it, creating a latent supply-chain risk.

## Active Exploitation Details

### Gyazo Server Vulnerability
- **Description**: A server-side vulnerability in the Gyazo image-sharing platform was exploited by attackers to gain unauthorized access to user databases, resulting in the theft of 23.6 million user records.
- **Impact**: Attackers obtained 23.6 million user records, likely including account credentials, email addresses, and associated metadata.
- **Status**: Actively exploited; breach confirmed by Gyazo. Patch or mitigation status not specified in reporting.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Gyazo server flaw exploited to steal 23.6 million user records](https://www.bleepingcomputer.com/news/security/gyazo-server-flaw-exploited-to-steal-236-million-user-records/)

### Brevo Supply-Chain Attack (ClickFix Injection)
- **Description**: Attackers stole a Cloudflare API key from Brevo and used it to inject malicious ClickFix scripts into Brevo's websites and JavaScript files embedded on customer sites, creating a supply-chain malware distribution vector.
- **Impact**: Malware distribution to visitors of Brevo customer sites; compromise of the software supply chain via trusted third-party JavaScript.
- **Status**: Active attack confirmed by Brevo; Cloudflare API key compromised and used for script injection.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Brevo supply-chain attack injected ClickFix scripts on customer sites](https://www.bleepingcomputer.com/news/security/brevo-supply-chain-attack-injected-clickfix-scripts-on-customer-sites/)

### Transparent Tribe Rust Backdoor Campaign (Operation RUSTYSHADE)
- **Description**: Pakistan-aligned APT group Transparent Tribe (APT36/Earth Karkaddan) deploys previously undocumented Rust-based tools—RUSTYSHADE, RUSTYMOVE, PSNATCH, and BASHNATCH—using private GitHub repositories for command-and-control infrastructure.
- **Impact**: Persistent access to government and defense entities in India and Afghanistan; credential theft, file exfiltration, and lateral movement capabilities.
- **Status**: Active campaign attributed by Zscaler ThreatLabz; novel toolset observed in recent attacks.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [The Hacker News — Transparent Tribe Deploys New Rust Backdoor Using Private GitHub Repositories for C2](https://thehackernews.com/2026/09/transparent-tribe-deploys-new-rust.html)

### Rapuncel Infostealer Campaign (Fake GitHub Repositories)
- **Description**: An ongoing malware campaign uses SEO-optimized GitHub repositories impersonating legitimate software firms (including LastPass Authenticator) to distribute a previously undocumented information stealer named Rapuncel.
- **Impact**: Credential theft, browser data harvesting, and potential compromise of developer and end-user systems via trusted platform abuse.
- **Status**: Active distribution via GitHub; campaign ongoing at time of reporting.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [Bleeping Computer — Fake LastPass Authenticator GitHub repos push new Rapuncel infostealer](https://www.bleepingcomputer.com/news/security/fake-lastpass-authenticator-github-repos-push-new-rapuncel-infostealer/)

### WeaselBiscuit npm Supply-Chain Campaign
- **Description**: A cluster of 13 malicious npm packages delivers the WeaselBiscuit JavaScript stealer, which harvests Chrome extension storage data. The malware shows functional overlaps with DPRK-linked Contagious Interview campaign tools (BeaverTail, etc.).
- **Impact**: Theft of Chrome extension storage data, including potential credentials and session tokens; supply-chain risk for developers installing compromised packages.
- **Status**: 13 packages identified and reported by OpenSourceMalware; active distribution via npm registry.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — WeaselBiscuit Stealer Spreads via 13 npm Packages to Harvest Chrome Extension Storage](https://thehackernews.com/2026/09/weaselbiscuit-stealer-spreads-via-13.html)

### PhantomRaven npm Stealer
- **Description**: A financially motivated threat actor distributes the PhantomRaven JavaScript information stealer via the npm package registry. Code analysis suggests the malware was likely authored with LLM assistance based on verbose comments, placeholder code, and token patterns.
- **Impact**: Information stealing from compromised development environments and downstream applications; demonstrates LLM-assisted malware development.
- **Status**: Active distribution via npm; attributed to a claimed bug bounty hunter.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [The Hacker News — Claimed Bug Bounty Hunter Likely Used LLM to Build PhantomRaven npm Stealer](https://thehackernews.com/2026/09/claimed-bug-bounty-hunter-likely-used.html)

### RatHat Android Malware Campaign
- **Description**: China-linked threat actors distribute RatHat Android malware via targeted smishing and malvertising campaigns leading to deceptive third-party download portals. The malware features an AI-powered subsystem for automated device navigation and control, and abuses ADB to retain shell access even after uninstallation.
- **Impact**: Persistent device compromise, automated remote control, data exfiltration, and surveillance capabilities on Android devices.
- **Status**: Active distribution campaigns observed; AI-powered control system operational.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [The Hacker News — RatHat Android Malware Abuses ADB to Retain Shell Access After Uninstall](https://thehackernews.com/2026/09/rathat-android-malware-abuses-adb-to.html), [Bleeping Computer — New RatHat Android malware uses AI to automate device control](https://www.bleepingcomputer.com/news/security/new-rathat-android-malware-uses-ai-to-automate-device-control/)

### AI Agent Breach of Spanish Organization
- **Description**: An AI-driven cyberattack successfully breached a Spanish organization, with the AI agent modifying personal data. This represents a confirmed case of autonomous AI agent misuse in a real-world intrusion.
- **Impact**: Unauthorized access and modification of personal data; demonstration of AI agent capabilities for offensive operations.
- **Status**: Confirmed breach reported by Dark Reading; active incident.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Dark Reading — AI Agent Breaches Spanish Organization, Modifies Personal Data](https://www.darkreading.com/cyberattacks-data-breaches/ai-agent-breaches-spanish-organization-personal-data)

### FamousSparrow APT Espionage Campaign
- **Description**: China-linked APT group FamousSparrow conducts political espionage targeting US political interests in Latin America, utilizing a stealthy backdoor for persistent access.
- **Impact**: Intelligence collection on political entities; long-term persistent access to sensitive networks in Latin America.
- **Status**: Active espionage campaign attributed by Dark Reading; backdoor deployed.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [Dark Reading — China's FamousSparrow APT Spies on US Politics in Latin America](https://www.darkreading.com/cyberattacks-data-breaches/china-famoussparrow-spies-latin-america)

### Handala Hack / HEAVYGRAM Telegram Backdoor
- **Description**: Iran-linked "hacktivist" persona Handala Hack operates HEAVYGRAM, a Telegram-based surveillance backdoor with built-in commands for remote command execution, system/network/process discovery, data and Telegram session exfiltration, screenshot capture, and DLL sideloading. A companion Delphi utility, CRUDEEXCLUDE, supports operations.
- **Impact**: Comprehensive surveillance, data theft, and remote control of compromised systems via Telegram C2.
- **Status**: Active attribution to Handala Hack; backdoor capabilities documented.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [The Hacker News — Iran-Linked Handala Hack Tied to HEAVYGRAM Telegram Backdoor That Can Steal Passwords](https://thehackernews.com/2026/09/iran-linked-handala-hack-tied-to.html)

### Azure AI Foundry Privilege Escalation (CVE-2026-85889)
- **Description**: Missing authentication for a critical function in Azure AI Foundry allows an unauthorized attacker to elevate privileges over the network. The flaw carries a maximum CVSS score of 10.0.
- **Impact**: Unauthorized privilege escalation in Azure AI Foundry environments, potentially leading to full service compromise.
- **Status**: Patched by Microsoft; no customer action required per vendor. No active exploitation reported.
- **Severity**: critical
- **Exploitation Status**: not_observed
- **Action**: patch
- **CVE IDs**: CVE-2026-85889
- **Reporting**: [The Hacker News — Microsoft Patches CVSS 10.0 Azure AI Foundry Flaw Enabling Unauthorized Privilege Escalation](https://thehackernews.com/2026/09/microsoft-patches-cvss-100-azure-ai.html)

### Unbound DNSSEC Validator Heap Overflow (CVE-2026-81642)
- **Description**: A critical heap overflow in the DNSSEC validator of all Unbound DNS resolver releases before 1.26.1. An attacker controlling a malicious DNS zone can trigger the overflow by querying a vulnerable resolver, enabling remote code execution.
- **Impact**: Remote code execution on DNS resolvers processing malicious zones; potential compromise of DNS infrastructure.
- **Status**: Fixed in Unbound 1.26.1 released same day as advisory. No active exploitation reported.
- **Severity**: critical
- **Exploitation Status**: not_observed
- **Action**: patch
- **CVE IDs**: CVE-2026-81642
- **Reporting**: [The Hacker News — Critical Unbound DNSSEC Validator Flaw Could Allow RCE via a Malicious DNS Zone](https://thehackernews.com/2026/09/critical-unbound-dnssec-validator-flaw.html)

### Docker Sandboxes macOS Escape (CVE-2026-77179)
- **Description**: Malicious code running inside a Docker Sandboxes virtual machine on macOS can escape the shared project directory and read or modify files anywhere on the host with the privileges of the host account running the VM.
- **Impact**: Container escape leading to host file system read/write access; compromise of macOS host from sandboxed workloads.
- **Status**: Docker security announcement issued September 15; affected versions not specified in reporting. No active exploitation reported.
- **Severity**: critical
- **Exploitation Status**: not_observed
- **Action**: patch
- **CVE IDs**: CVE-2026-77179
- **Reporting**: [The Hacker News — Critical Docker Sandboxes Flaw Lets Malicious Guest Code Read and Modify macOS Host Files](https://thehackernews.com/2026/09/critical-docker-sandboxes-flaw-lets.html)

### Check Point Management Server Unauthenticated RCE
- **Description**: A critical vulnerability in Check Point Security Management and Log Servers allows unauthenticated attackers to execute code as root over the network. The Security Management Server controls firewall policy and administrator access.
- **Impact**: Full root compromise of management infrastructure controlling firewall policies and admin access.
- **Status**: Fix released via LivePatch update channel. Check Point states it has no indication the flaw has been exploited in the wild.
- **Severity**: critical
- **Exploitation Status**: not_observed
- **Action**: patch
- **Reporting**: [The Hacker News — Critical Check Point Management Flaw Lets Unauthenticated Attackers Run Code as Root](https://thehackernews.com/2026/09/critical-check-point-management-server.html), [Bleeping Computer — New Check Point flaw lets hackers execute code with root privileges](https://www.bleepingcomputer.com/news/security/check-point-warns-critical-flaw-lets-hackers-execute-code-as-root/)

### Plugin4Shell AI Coding Agent Plugin Hijacking
- **Description**: A flaw in four widely used AI coding agents allows a plugin repository owner to swap the plugin code installed by the agent for a malicious version, even when the agent pinned the plugin to a specific reviewed version. Anthropic patched Claude Code 2.1.179; OpenAI patched Codex 0.146.0; GitHub Copilot reportedly has no fix.
- **Impact**: Supply-chain compromise of AI-assisted development environments; malicious code execution in developer contexts.
- **Status**: Partial vendor patches available; GitHub Copilot unpatched per reporting. No active exploitation reported.
- **Severity**: high
- **Exploitation Status**: not_observed
- **Action**: patch
- **Reporting**: [The Hacker News — Plugin4Shell Lets Repository Owners Swap Pinned Plugin Code Across Four AI Coding Agents](https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html)

### Abandoned CDN Domain Re-registration Supply-Chain Risk
- **Description**: A previously abandoned CDN domain was re-registered in July 2025. Thousands of websites, code repositories, and documentation pages still contain hard-coded references to hostnames under this domain, allowing the new owner to serve arbitrary content to those callers.
- **Impact**: Potential supply-chain compromise of thousands of sites; ability to inject malicious scripts, serve malware, or harvest data from dependent properties.
- **Status**: Domain re-registered; thousands of active references persist. No active exploitation confirmed, but latent risk is high.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: investigate
- **Reporting**: [The Hacker News — An Abandoned CDN Domain Was Re-Registered. Thousands of Sites Still Call It.](https://thehackernews.com/2026/09/an-abandoned-cdn-domain-was-re.html)

## Affected Systems and Products

- **Gyazo Image-Sharing Platform**: Server infrastructure hosting 23.6 million user accounts; specific version or component not disclosed.
- **Brevo Marketing Platform & Customer Sites**: Brevo's Cloudflare configuration and JavaScript assets embedded on customer websites; all customers using embedded Brevo scripts affected.
- **Check Point Security Management and Log Servers**: Management server appliances and virtual instances controlling firewall policy; patched via LivePatch.
- **Unbound DNS Resolver**: All releases prior to 1.26.1; widely deployed as validating resolver in enterprise and ISP environments.
- **Docker Sandboxes on macOS**: Docker Sandboxes virtual machines running on macOS hosts; versions not specified in advisory.
- **Azure AI Foundry**: Microsoft's managed AI platform service; patch applied by provider with no customer action required.
- **npm Package Registry**: 13 malicious packages (WeaselBiscuit) and PhantomRaven package; any project installing compromised packages.
- **GitHub Repositories**: SEO-optimized repositories impersonating LastPass Authenticator and other legitimate software; Rapuncel distribution vector.
- **Private GitHub Repositories**: Used by Transparent Tribe for C2 infrastructure hosting Rust-based tooling (RUSTYSHADE, RUSTYMOVE, PSNATCH, BASHNATCH).
- **Android Devices**: Targeted via smishing and malvertising leading to third-party APK downloads; RatHat malware with ADB persistence.
- **AI Coding Agents**: Anthropic Claude Code (<2.1.179), OpenAI Codex (<0.146.0), GitHub Copilot (unpatched), and one additional unnamed agent; Plugin4Shell plugin hijacking.
- **Abandoned CDN Domain Callers**: Thousands of websites, code repositories, and documentation pages with hard-coded references to the re-registered domain.

## Attack Vectors and Techniques

- **Server-Side Vulnerability Exploitation**: Direct exploitation of a flaw in Gyazo's server infrastructure to access user databases.
- **Supply-Chain Compromise via Stolen API Key**: Theft of a Cloudflare API key enabling malicious script injection into Brevo's and customer sites' JavaScript.
- **Malicious Package Publishing (npm)**: Publication of 13 WeaselBiscuit packages and PhantomRaven to the public npm registry targeting developers and CI/CD pipelines.
- **Typosquatting/Impersonation on GitHub**: SEO-optimized repositories mimicking legitimate software (LastPass Authenticator) to deliver Rapuncel infostealer.
- **Private Repository C2 Hosting**: Use of private GitHub repositories as covert command-and-control infrastructure for Rust-based backdoors.
- **Rust-Based Malware Development**: Novel toolset (RUSTYSHADE, RUSTYMOVE, PSNATCH, BASHNATCH) written in Rust for evasion and cross-platform capability.
- **AI-Powered Malware Control**: RatHat's AI subsystem automates device navigation and control; PhantomRaven likely authored with LLM assistance.
- **ADB Persistence Post-Uninstall**: RatHat abuses Android Debug Bridge to retain shell access after the malicious app is uninstalled.
- **Autonomous AI Agent Intrusion**: AI agent independently breached a Spanish organization and modified personal data without direct human operation.
- **Telegram-Based C2**: HEAVYGRAM backdoor uses Telegram API for command delivery, data exfiltration, and session hijacking.
- **DNSSEC Validator Heap Overflow**: Malicious DNS zone triggers heap overflow in Unbound resolver during validation, achieving RCE.
- **Container Escape via Host Filesystem Access**: Docker Sandboxes flaw allows VM guest to traverse outside shared directory to host filesystem.
- **Unauthenticated Management Interface RCE**: Check Point Management Server accepts unauthenticated network requests leading to root code execution.
- **Plugin Version Pinning Bypass**: AI coding agents' plugin pinning mechanism bypassed by repository owner modifying pinned plugin code.
- **Expired Domain Re-registration**: Attacker registers abandoned CDN domain to control content served to thousands of hard-coded references.

## Threat Actor Activities

- **Transparent Tribe (APT36 / Earth Karkaddan)**: Pakistan-aligned APT conducting Operation RUSTYSHADE/RUSTYMOVE targeting government and defense sectors in India and Afghanistan; employs novel Rust toolset and private GitHub C2.
- **Handala Hack**: Iran-linked hacktivist persona operating HEAVYGRAM Telegram backdoor and CRUDEEXCLUDE utility for surveillance, data theft, and remote access.
- **FamousSparrow**: China-linked APT conducting political espionage against US interests in Latin America using a stealthy backdoor.
- **DPRK-Linked Actors (Contagious Interview Campaign)**: Nexus identified between WeaselBiscuit npm stealer and known DPRK tools BeaverTail and associated strains; suggests shared infrastructure or code reuse.
- **Financially Motivated npm Actor**: Developer distributing PhantomRaven stealer via npm; assessed as likely using LLM for code generation; claims bug bounty hunter persona.
- **RatHat Operators**: China-based threat actors distributing Android malware via smishing and malvertising; employ AI-powered control system and ADB persistence.
- **Gyazo Breach Actors**: Unidentified threat actors who exploited Gyazo server vulnerability to steal 23.6 million records; motivation and attribution not disclosed.
- **Brevo Supply-Chain Attackers**: Unidentified actors who compromised a Cloudflare API key to inject ClickFix scripts; likely financially motivated malware distribution.
- **Abandoned CDN Domain Registrant**: Unknown party who re-registered expired CDN domain; capability to serve arbitrary content to thousands of dependent sites; intent not yet observed.