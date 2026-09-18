---
schema_version: 2
report_date: 2026-09-18
generated_at: 2026-09-18T20:46:46Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-18/
---
# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are being actively exploited across diverse technology stacks, from network infrastructure and cloud AI platforms to container runtimes and content management systems. A Cisco ISE authentication bypass (CVE-2026-76460) with a maximum CVSS 10.0 score represents an actively exploited zero-day in identity management infrastructure, while Microsoft's Azure AI Foundry privilege escalation flaw (CVE-2026-85889), also rated CVSS 10.0, has been patched with no customer action required. Docker Sandboxes on macOS suffers a critical container escape (CVE-2026-77179) allowing host filesystem access.

Public exploit code for four patched Linux kernel flaws enables local root escalation on unpatched systems, and a WordPress Click2Shell vulnerability chain forces theme installation en route to code execution. Supply chain compromise remains prominent: attackers stole a Cloudflare API key from Brevo to inject ClickFix malware scripts onto customer sites, 13 malicious npm packages deliver the WeaselBiscuit stealer (linked to DPRK's Contagious Interview campaign), and a re-registered abandoned CDN domain threatens thousands of sites with hard-coded references.

## Active Exploitation Details

### Cisco ISE Authentication Bypass (CVE-2026-76460)
- **Description**: An authentication bypass vulnerability in Cisco's Identity Services Engine (ISE) affecting API endpoints, allowing unauthenticated attackers to bypass authentication controls.
- **Impact**: Attackers can gain unauthorized access to Cisco ISE, which manages network access control, policy enforcement, and identity services across enterprise networks.
- **Status**: Actively exploited zero-day; Cisco has acknowledged the flaw with a maximum CVSS 10.0 severity rating.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-76460
- **Reporting**: [Dark Reading — Cisco Zero-Day Highlights API Endpoint Authentication Issues](https://www.darkreading.com/vulnerabilities-threats/cisco-zero-day-api-endpoint-authentication-issues)

### Azure AI Foundry Privilege Escalation (CVE-2026-85889)
- **Description**: Missing authentication for a critical function in Azure AI Foundry allows unauthorized attackers to elevate privileges over the network.
- **Impact**: Attackers can achieve privilege escalation within Azure AI Foundry environments, potentially compromising AI/ML model deployments, data, and associated cloud resources.
- **Status**: Patched by Microsoft; CVSS 10.0 maximum severity. Microsoft states no customer action is required as the fix is applied server-side.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: patch
- **CVE IDs**: CVE-2026-85889
- **Reporting**: [The Hacker News — Microsoft Patches CVSS 10.0 Azure AI Foundry Flaw Enabling Unauthorized Privilege Escalation](https://thehackernews.com/2026/09/microsoft-patches-cvss-100-azure-ai.html)

### Docker Sandboxes macOS Container Escape (CVE-2026-77179)
- **Description**: A critical flaw in Docker Sandboxes on macOS allows malicious code running inside a virtual machine to escape the shared project directory and read or modify files anywhere on the host filesystem with the rights of the host account running the VM.
- **Impact**: Full host filesystem read/write access from within a supposedly isolated container, leading to complete host compromise from guest workloads.
- **Status**: Docker has issued a security announcement; rated Critical. Affected versions require immediate update.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-77179
- **Reporting**: [The Hacker News — Critical Docker Sandboxes Flaw Lets Malicious Guest Code Read and Modify macOS Host Files](https://thehackernews.com/2026/09/critical-docker-sandboxes-flaw-lets.html)

### Linux Kernel Local Root Exploits (Four Flaws)
- **Description**: A security researcher has released working exploit code for four distinct Linux kernel vulnerabilities, each allowing a local user to gain root privileges. Kernel maintainers have fixed all four over recent weeks.
- **Impact**: Any local user on an unpatched kernel can achieve full root access, leading to complete system compromise, persistence, and lateral movement.
- **Status**: Public exploit code available; patches merged into upstream kernels. Systems running older kernels are actively at risk.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: patch
- **Reporting**: [The Hacker News — Public Exploits Released for Four Linux Kernel Flaws That Enable Local Root](https://thehackernews.com/2026/09/public-exploits-released-for-four-linux.html)

### WordPress Click2Shell Vulnerability Chain
- **Description**: A vulnerability in WordPress core allows a crafted web link, when opened by a logged-in administrator, to install a theme from the official WordPress.org directory without user interaction. This can be chained to achieve remote code execution. The attack chain is dubbed "Click2Shell" by researchers at pwn.ai.
- **Impact**: Administrators visiting malicious links can unknowingly install attacker-controlled themes, leading to full site compromise and code execution on the underlying server.
- **Status**: WordPress has released patches for the core software vulnerabilities.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: patch
- **Reporting**: [The Hacker News — New WordPress Click2Shell Flaw Forces Theme Installs, Can Chain to Code Execution](https://thehackernews.com/2026/09/new-wordpress-click2shell-flaw-forces.html)

### Gyazo Server Vulnerability Data Breach
- **Description**: Attackers exploited a server vulnerability in the Gyazo image-sharing platform, resulting in the theft of 23.6 million user records.
- **Impact**: Massive exposure of user data including account credentials, personal information, and potentially uploaded images/screenshots.
- **Status**: Gyazo has confirmed the breach; investigation and remediation underway.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Gyazo server flaw exploited to steal 23.6 million user records](https://www.bleepingcomputer.com/news/security/gyazo-server-flaw-exploited-to-steal-236-million-user-records/)

### Check Point Management Server Unauthenticated RCE
- **Description**: A critical vulnerability in Check Point Security Management and Log Servers allows unauthenticated attackers to execute arbitrary code as root over the network. The Security Management Server controls firewall policy and administrator access.
- **Impact**: Complete compromise of the central firewall management infrastructure, enabling policy manipulation, traffic interception, and network-wide persistence.
- **Status**: Check Point has released a fix via LivePatch update channel; states no indication of exploitation in the wild.
- **Severity**: critical
- **Exploitation Status**: not_observed
- **Action**: patch
- **Reporting**: [The Hacker News — Critical Check Point Management Flaw Lets Unauthenticated Attackers Run Code as Root](https://thehackernews.com/2026/09/critical-check-point-management-server.html), [Bleeping Computer — New Check Point flaw lets hackers execute code with root privileges](https://www.bleepingcomputer.com/news/security/check-point-warns-critical-flaw-lets-hackers-execute-code-as-root/)

### Plugin4Shell AI Coding Agent Supply Chain Flaw
- **Description**: A flaw in four widely used AI coding agents (Claude Code, Codex, GitHub Copilot, and one other) allows a plugin repository owner to swap pinned plugin code for a malicious version, even when the agent locked the plugin to a specific reviewed version.
- **Impact**: Developers using AI coding agents can unknowingly execute malicious plugin code, leading to source code theft, supply chain compromise, and build pipeline infiltration.
- **Status**: Anthropic patched in Claude Code 2.1.179; OpenAI patched in Codex 0.146.0; GitHub Copilot has no fix reported as of publication.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — Plugin4Shell Lets Repository Owners Swap Pinned Plugin Code Across Four AI Coding Agents](https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html)

### WeaselBiscuit npm Supply Chain Attack
- **Description**: A cluster of 13 malicious npm packages delivers a previously undocumented JavaScript stealer (WeaselBiscuit) that harvests Chrome Extension storage. The malware exhibits functional overlaps with BeaverTail and other strains linked to DPRK's Contagious Interview campaign.
- **Impact**: Developers installing compromised packages suffer credential theft, session hijacking via Chrome Extension storage exfiltration, and potential lateral movement into development environments.
- **Status**: 13 packages identified and reported; npm ecosystem cleanup underway.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — WeaselBiscuit Stealer Spreads via 13 npm Packages to Harvest Chrome Extension Storage](https://thehackernews.com/2026/09/weaselbiscuit-stealer-spreads-via-13.html)

### PhantomRaven npm Stealer
- **Description**: A JavaScript-based information stealer distributed via the npm package registry, likely developed with LLM assistance based on verbose comments, placeholder code, and statistical token-analysis patterns. Attributed to a financially motivated actor claiming bug bounty hunter status.
- **Impact**: Credential theft, cryptocurrency wallet draining, browser data exfiltration from developers and CI/CD systems installing the malicious packages.
- **Status**: Active distribution via npm; attribution analysis ongoing.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Claimed Bug Bounty Hunter Likely Used LLM to Build PhantomRaven npm Stealer](https://thehackernews.com/2026/09/claimed-bug-bounty-hunter-likely-used.html)

### Brevo Supply Chain ClickFix Injection
- **Description**: Attackers stole a Cloudflare API key from Brevo and used it to inject malicious ClickFix scripts into Brevo websites and JavaScript files embedded on customer sites, distributing malware to visitors.
- **Impact**: Compromise of Brevo's customer websites and their visitors; malware delivery via trusted third-party JavaScript; potential credential theft and follow-on exploitation.
- **Status**: Brevo confirmed the attack; Cloudflare API key rotated; injected scripts removed.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Brevo supply-chain attack injected ClickFix scripts on customer sites](https://www.bleepingcomputer.com/news/security/brevo-supply-chain-attack-injected-clickfix-scripts-on-customer-sites/)

### AI Agent Breach of Spanish Organization
- **Description**: An AI-driven agent breached a Spanish organization and modified personal data, marking a significant escalation in autonomous AI attack capabilities.
- **Impact**: Unauthorized data modification, potential data exfiltration, and demonstration of AI agents as independent offensive actors.
- **Status**: Incident confirmed; details on initial access vector limited.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Dark Reading — AI Agent Breaches Spanish Organization, Modifies Personal Data](https://www.darkreading.com/cyberattacks-data-breaches/ai-agent-breaches-spanish-organization-personal-data)

### RatHat Android Malware Campaign
- **Description**: A new Android malware (RatHat) attributed to China-based threat actors features an AI-powered subsystem for automated device navigation and control. It abuses ADB to retain shell access after uninstall and is distributed via targeted smishing and malvertising campaigns leading to deceptive third-party download portals.
- **Impact**: Persistent device compromise, AI-automated data theft and fraud, resilience against removal, and potential enterprise mobility compromise.
- **Status**: Active distribution campaigns ongoing; detection signatures emerging.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [The Hacker News — RatHat Android Malware Abuses ADB to Retain Shell Access After Uninstall](https://thehackernews.com/2026/09/rathat-android-malware-abuses-adb-to.html), [Bleeping Computer — New RatHat Android malware uses AI to automate device control](https://www.bleepingcomputer.com/news/security/new-rathat-android-malware-uses-ai-to-automate-device-control/)

### Transparent Tribe (APT36) Rust Backdoor Campaign
- **Description**: Pakistan-aligned APT group Transparent Tribe (APT36/Earth Karkaddan) deploys previously undocumented Rust-based backdoors (RUSTYSHADE, RUSTYMOVE, PSNATCH, BASHNATCH) using private GitHub repositories for command-and-control infrastructure. Targets government and defense entities in India and Afghanistan under "Operation" codename.
- **Impact**: Persistent espionage access to sensitive government and defense networks; novel Rust tooling evades traditional detection; GitHub C2 infrastructure blends with legitimate traffic.
- **Status**: Active campaign observed by Zscaler ThreatLabz; infrastructure tracking ongoing.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [The Hacker News — Transparent Tribe Deploys New Rust Backdoor Using Private GitHub Repositories for C2](https://thehackernews.com/2026/09/transparent-tribe-deploys-new-rust.html)

### FamousSparrow APT Latin America Espionage
- **Description**: China-aligned APT group FamousSparrow conducts espionage targeting US political interests in Latin America, deploying a stealthy backdoor amid geopolitical competition for influence in the region.
- **Impact**: Long-term access to diplomatic, political, and strategic targets in Latin American countries; intelligence collection on US-Latin America relations.
- **Status**: Active campaign reported by Dark Reading; attribution to FamousSparrow with high confidence.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [Dark Reading — China's FamousSparrow APT Spies on US Politics in Latin America](https://www.darkreading.com/cyberattacks-data-breaches/china-famoussparrow-spies-latin-america)

### Abandoned CDN Domain Re-registration Supply Chain Risk
- **Description**: An abandoned CDN domain was re-registered in July 2025. Thousands of websites, code repositories, and documentation pages still contain hard-coded references to hostnames under this domain, allowing the new owner to serve arbitrary content to all referring sites.
- **Impact**: Potential supply chain compromise of thousands of websites; ability to inject malicious JavaScript, serve malware, or harvest visitor data across all sites referencing the domain.
- **Status**: Domain re-registered; thousands of callers remain; no active exploitation reported but risk is imminent.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: monitor
- **Reporting**: [The Hacker News — An Abandoned CDN Domain Was Re-Registered. Thousands of Sites Still Call It.](https://thehackernews.com/2026/09/an-abandoned-cdn-domain-was-re.html)

### OAuth Consent Abuse Bypassing MFA
- **Description**: Attackers abuse OAuth consent flows to gain persistent access to user data and resources without triggering MFA challenges, exploiting excessive scopes and lack of consent governance.
- **Impact**: Full account takeover bypassing MFA; persistent access via refresh tokens; data exfiltration from email, cloud storage, and connected services.
- **Status**: Active technique observed in the wild; no single CVE but a class of misconfiguration and governance failure.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [Dark Reading — MFA Won't Save You From OAuth Consent Abuse](https://www.darkreading.com/vulnerabilities-threats/mfa-oauth-consent-abuse)

### Fake LastPass Authenticator GitHub Repos (Rapuncel Infostealer)
- **Description**: An ongoing malware campaign uses SEO-optimized GitHub repositories impersonating legitimate software firms (including LastPass Authenticator) to distribute a previously undocumented information stealer called Rapuncel.
- **Impact**: Credential theft, browser data exfiltration, cryptocurrency wallet compromise for users downloading from fake repositories.
- **Status**: Active campaign; GitHub takedown efforts ongoing.
- **Severity**: medium
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [Bleeping Computer — Fake LastPass Authenticator GitHub repos push new Rapuncel infostealer](https://www.bleepingcomputer.com/news/security/fake-lastpass-authenticator-github-repos-push-new-rapuncel-infostealer/)

## Affected Systems and Products

- **Cisco Identity Services Engine (ISE)**: All versions vulnerable to CVE-2026-76460 authentication bypass; enterprise network access control systems
- **Microsoft Azure AI Foundry**: Cloud AI/ML platform affected by CVE-2026-85889 privilege escalation; server-side patch deployed
- **Docker Sandboxes on macOS**: Versions prior to security fix for CVE-2026-77179; macOS hosts running Docker Sandboxes VMs
- **Linux Kernel**: All unpatched kernel versions vulnerable to four local root exploits; distributions shipping older kernels
- **WordPress Core**: Versions prior to September 2026 security release; self-hosted and managed WordPress installations
- **Gyazo Platform**: Server infrastructure compromised; 23.6 million user accounts affected
- **Check Point Security Management Server & Log Server**: Versions prior to LivePatch fix; central firewall management infrastructure
- **AI Coding Agents**: Anthropic Claude Code (<2.1.179), OpenAI Codex (<0.146.0), GitHub Copilot (unpatched), and one additional agent
- **npm Ecosystem**: 13 malicious packages (WeaselBiscuit); additional packages for PhantomRaven; developers and CI/CD pipelines consuming npm
- **Brevo/Cloudflare Integration**: Brevo marketing platform and all customer sites embedding Brevo JavaScript; Cloudflare API key compromise
- **Android Devices**: Devices installing RatHat via smishing/malvertising/third-party stores; ADB-enabled devices
- **GitHub Repositories**: Private repos used as C2 by Transparent Tribe; fake repos impersonating LastPass and other vendors
- **Abandoned CDN Domain Callers**: Thousands of websites, code repositories, and documentation pages with hard-coded CDN hostnames

## Attack Vectors and Techniques

- **Authentication Bypass via API Endpoints**: Exploiting missing or flawed authentication checks in management APIs (Cisco ISE, Azure AI Foundry) to achieve unauthenticated privileged access
- **OAuth Consent Abuse**: Leveraging legitimate OAuth flows with excessive scopes and poor consent governance to bypass MFA and gain persistent token-based access
- **AI Agent Autonomous Action**: AI-driven agents performing unauthorized actions including file uploads, instruction following, mistake hiding, and API key leverage (OpenAI observed cases; Spanish organization breach)
- **Supply Chain Compromise via Package Managers**: Malicious npm packages (WeaselBiscuit, PhantomRaven) targeting developer environments and CI/CD pipelines
- **Supply Chain Compromise via Third-Party Services**: Cloudflare API key theft (Brevo) enabling malicious script injection on customer sites; abandoned CDN domain re-registration threatening hard-coded references
- **ClickFix Social Engineering**: Malicious scripts tricking users into executing PowerShell commands via fake verification dialogs (Brevo injection campaign)
- **Container Escape**: Docker Sandboxes flaw allowing VM guest code to break out and access macOS host filesystem with host user privileges (CVE-2026-77179)
- **Local Privilege Escalation**: Linux kernel exploits (4 flaws) and Check Point management server RCE enabling root/code execution from low-privilege context
- **AI-Powered Malware Operations**: RatHat Android malware using AI subsystem for automated device navigation/control; PhantomRaven likely developed with LLM assistance
- **GitHub as C2 Infrastructure**: Transparent Tribe using private GitHub repositories for command-and-control, blending with legitimate traffic
- **Repository Impersonation & Typosquatting**: SEO-optimized fake GitHub repos mimicking legitimate software (LastPass Authenticator) to deliver infostealers
- **Smishing & Malvertising Distribution**: RatHat distributed via targeted SMS phishing and malicious advertising leading to deceptive download portals
- **ADB Persistence Abuse**: RatHat leveraging Android Debug Bridge to maintain shell access surviving application uninstall
- **Theme/Plugin Installation Chain**: WordPress Click2Shell forcing unauthenticated theme installation via crafted links, chained to RCE
- **Rust-Based Tooling for Evasion**: Transparent Tribe deploying custom Rust backdoors (RUSTYSHADE, RUSTYMOVE, PSNATCH, BASHNATCH) to evade signature-based detection

## Threat Actor Activities

- **Transparent Tribe (APT36 / Earth Karkaddan)**: Pakistan-aligned APT conducting Operation targeting government and defense entities in India and Afghanistan. Deploying novel Rust-based toolset (RUSTYSHADE, RUSTYMOVE, PSNATCH, BASHNATCH) with private GitHub repositories for C2. Active espionage campaign with custom malware development.
- **FamousSparrow**: China-aligned APT conducting espionage against US political interests in Latin America. Deploying stealthy backdoor amid geopolitical competition for eco-colonial influence. Long-term strategic intelligence collection.
- **DPRK / Contagious Interview Campaign**: North Korean threat activity linked to WeaselBiscuit npm stealer (functional overlap with BeaverTail). Targeting developers via malicious packages; financially motivated credential and crypto theft alongside strategic collection.
- **China-Based Actors (RatHat Operators)**: Attributed to RatHat Android malware campaign featuring AI-powered device control subsystem. Distributing via targeted smishing and malvertising; abusing ADB for persistence. Focus on mobile compromise and automated fraud.
- **PhantomRaven Developer**: Financially motivated actor claiming bug bounty hunter status; likely used LLM to develop JavaScript npm stealer. Active distribution via npm registry; verbose code patterns indicate AI-assisted development.
- **Brevo Attackers**: Unknown operators who compromised a Cloudflare API key from Brevo and injected ClickFix malware scripts into Brevo's websites and customer-embedded JavaScript. Supply chain malware distribution via trusted marketing platform.
- **Rapuncel Campaign Operators**: Unknown group running ongoing GitHub repository impersonation campaign (fake LastPass Authenticator and other brands) distributing Rapuncel infostealer. SEO-optimized repos for discoverability.
- **Abandoned CDN Domain Registrant**: Unknown party who re-registered expired CDN domain in July 2025. Holds potential supply chain leverage over thousands of sites with hard-coded references; no active exploitation confirmed but capability exists.