# Exploitation Report

## Executive Summary

A significant escalation in AI-driven offensive operations has emerged with the documentation of JadePuffer, the first ransomware campaign believed to be executed entirely by an autonomous LLM agent. This development signals a fundamental shift in threat actor capabilities, lowering the barrier for sophisticated attack chain automation. Simultaneously, North Korean threat actors have intensified supply chain operations, publishing 108 malicious packages across npm, Packagist, Go, and Chrome Web Store under the PolinRider campaign while deploying additional npm packages masquerading as Rollup polyfills to compromise developer environments.

Critical vulnerability exploitation continues across multiple fronts. The "Bad Epoll" Linux kernel flaw (CVE-2026-46242) provides unprivileged local users with a reliable path to root on Linux desktops, servers, and Android devices. Anubis ransomware operators are actively leveraging Citrix Bleed 2 (CVE-2025-5777) for initial access, while Cisco has confirmed active exploitation of a Unified Communications Manager vulnerability patched in early June. Seven unpatched vulnerabilities in the FatFs filesystem library threaten millions of embedded devices, and FortiBleed actors are monetizing Fortinet firewall access while exploiting a Nextcloud zero-day. The Kairos extortion group successfully extracted $1 million from a U.S. government entity, and Pegasus spyware continues to target high-profile political figures.

## Active Exploitation Details

### Bad Epoll Linux Kernel Privilege Escalation
- **Description**: A newly disclosed Linux kernel vulnerability in the epoll subsystem allows an unprivileged local user to escalate privileges to root. The flaw affects the core event notification facility used throughout the kernel.
- **Impact**: Attackers with any local user access can achieve full root control over the system, compromising confidentiality, integrity, and availability. The vulnerability impacts Linux desktops, servers, and Android devices broadly.
- **Status**: Actively exploitable; patch availability depends on distribution and Android vendor update cycles.
- **CVE ID**: CVE-2026-46242

### Citrix Bleed 2 Exploitation by Anubis Ransomware
- **Description**: The Citrix Bleed Bleed 2 vulnerability in Citrix NetScaler ADC and Gateway allows unauthenticated attackers to obtain active session tokens and bypass authentication mechanisms.
- **Impact**: Provides initial access to internal networks without credentials. Anubis ransomware operators are leveraging this for deployment, leading to data encryption, exfiltration, and extortion.
- **Status**: Actively exploited in the wild by Anubis ransomware affiliates; patches available from Citrix.
- **CVE ID**: CVE-2025-5777

### Cisco Unified Communications Manager Exploitation
- **Description**: Cisco has confirmed that threat actors are actively exploiting a vulnerability in Unified Communications Manager (Unified CM). The flaw was patched in early June but exploitation has commenced post-patch release.
- **Impact**: Compromise of enterprise voice and video infrastructure, potential lateral movement, call interception, and persistence in critical communication systems.
- **Status**: Active exploitation confirmed by vendor; patches released in early June 2026.

### FatFs Filesystem Vulnerabilities in Embedded Devices
- **Description**: Security firm runZero disclosed seven vulnerabilities in FatFs, a lightweight FAT/exFAT filesystem library embedded in millions of IoT, industrial, automotive, and consumer devices. The flaws include buffer overflows, integer overflows, and out-of-bounds reads/writes triggered by malformed filesystem images.
- **Impact**: Remote code execution or denial of service via malicious USB drives, SD cards, or firmware images. Devices rarely receive updates, creating a long-tail exposure.
- **Status**: Unpatched as of disclosure; vendor notification initiated but remediation timeline uncertain for deployed device base.

### Nextcloud Zero-Day Exploitation by FortiBleed Actors
- **Description**: Threat actors associated with the FortiBleed campaign are exploiting a zero-day vulnerability in Nextcloud, an on-premises file sharing and collaboration platform, as part of post-exploitation activity following Fortinet firewall compromise.
- **Impact**: Unauthorized access to sensitive documents, credentials, and collaboration data stored in Nextcloud instances; facilitates lateral movement and data exfiltration.
- **Status**: Zero-day actively exploited; no patch available at time of reporting.

### Pegasus Spyware Deployment Against Political Target
- **Description**: Citizen Lab confirmed that former European Parliament member Stelios Kouloglou was repeatedly infected with NSO Group's Pegasus spyware while investigating spyware abuse. The infections employed zero-click exploits requiring no user interaction.
- **Impact**: Complete compromise of mobile device communications, location tracking, microphone/camera access, and message interception.
- **Status**: Ongoing threat to high-risk individuals; mitigations include Lockdown Mode and timely OS updates.

## Affected Systems and Products

- **Linux Kernel (all versions prior to patched releases)**: Core epoll subsystem vulnerability affecting desktops, servers, containers, and Android devices — **Platform**: Linux, Android
- **Citrix NetScaler ADC and Gateway**: Citrix Bleed 2 authentication bypass — **Platform**: On-premises and cloud-deployed Citrix ADC/Gateway appliances
- **Cisco Unified Communications Manager**: Actively exploited post-patch vulnerability — **Platform**: Enterprise VoIP and video conferencing infrastructure
- **FatFs Filesystem Library (all current versions)**: Seven vulnerabilities in FAT/exFAT implementation — **Platform**: Embedded devices (IoT, industrial control, automotive, consumer electronics, medical devices)
- **Nextcloud (unpatched versions)**: Zero-day exploited by FortiBleed actors — **Platform**: On-premises file sync and collaboration servers
- **Apple iOS / Android**: Pegasus spyware zero-click exploit chains — **Platform**: Mobile devices of high-value targets
- **npm, Packagist, Go module proxy, Chrome Web Store**: 108+ malicious packages in PolinRider campaign — **Platform**: Developer build environments, CI/CD pipelines, browser extensions
- **npm (additional packages)**: North Korea-linked packages mimicking Rollup polyfills — **Platform**: JavaScript/TypeScript developer workstations and build systems
- **NetNut residential proxy network**: 2 million compromised Android devices (smart TVs, streaming boxes, phones) — **Platform**: Consumer Android/IoT devices enrolled in botnet
- **Microsoft 365 / Google Workspace**: OAuth abuse via ConsentFix, ClickFix, ARToken/EvilTokens PhaaS, and Umbrij malware — **Platform**: Cloud identity and productivity suites

## Attack Vectors and Techniques

- **AI Agent-Automated Ransomware Operations**: JadePuffer demonstrates end-to-end attack execution (reconnaissance, initial access, lateral movement, encryption, exfiltration, negotiation) orchestrated by an LLM agent without human intervention — **Vector**: Autonomous tool use via API-enabled LLM with access to offensive tooling
- **Software Supply Chain Compromise**: Publication of 108 malicious packages across four ecosystems (npm, Packagist, Go, Chrome Web Store) under legitimate-sounding names; additional npm packages typosquatting Rollup polyfills — **Vector**: Developer dependency installation, CI/CD pipeline poisoning, browser extension installation
- **Phishing-as-a-Service (PhaaS) Platforms**: ARToken and EvilTokens provide turnkey Microsoft 365 phishing toolkits with MFA bypass, token theft, and session hijacking capabilities — **Vector**: Adversary-in-the-middle phishing pages, OAuth consent phishing (ConsentFix/ClickFix)
- **OAuth Token Abuse for Email Access**: Umbrij malware (ToddyCat) and ConsentFix/ClickFix attacks steal OAuth refresh/access tokens to silently access Gmail and Microsoft 365 mailboxes via legitimate APIs — **Vector**: Malicious OAuth applications, consent phishing, token replay
- **Local Privilege Escalation via Kernel Flaw**: Bad Epoll (CVE-2026-46242) enables reliable root escalation from any local user context — **Vector**: Local code execution (via ssh, container escape, compromised service) followed by epoll exploit
- **Bring Your Own Vulnerable Driver (BYOVD)**: Ransomware groups loading signed but vulnerable kernel drivers to disable EDR and escalate privileges — **Vector**: Driver installation via administrator access or exploit chain
- **Authentication Bypass via Session Token Theft**: Citrix Bleed 2 (CVE-2025-5777) leaks valid session tokens allowing unauthenticated administrative access — **Vector**: Unauthenticated HTTP requests to vulnerable NetScaler management interfaces
- **Residential Proxy Botnet Enrollment**: NetNut/Popa botnet compromises Android devices (including smart TVs/streaming boxes) to sell residential IP bandwidth — **Vector**: Malicious apps, firmware supply chain, or exploit of device management interfaces
- **Zero-Click Mobile Exploitation**: Pegasus spyware achieves full device compromise without user interaction — **Vector**: Messaging platform parsing flaws (iMessage, WhatsApp, etc.) triggered by silent delivery
- **Credential Theft via Application Impersonation**: PamStealer distributes trojanized versions of the Maccy clipboard manager; uses PAM authentication prompts to steal macOS login passwords — **Vector**: Typosquatted download sites, GitHub release hijacking, social engineering

## Threat Actor Activities

- **JadePuffer Operator**: First documented fully AI-agent-driven ransomware operation; represents paradigm shift toward autonomous offensive cyber operations — **Campaign**: Automated end-to-end ransomware deployment
- **Kairos Extortion Group**: Conducted data-theft extortion against a U.S. government entity, securing $1 million payment confirmed via leaked negotiation chat — **Campaign**: Targeted intrusion, data exfiltration, extortion negotiation
- **North Korean Actors (Contagious Interview / PolinRider)**: Published 108 malicious packages across npm, Packagist, Go, and Chrome Web Store; additional campaign deploying Rollup polyfill typosquats on npm — **Campaign**: PolinRider supply chain campaign; ongoing developer-targeted credential theft
- **Armored Likho**: Previously undocumented threat actor targeting government agencies and electric power sector in Russia, Brazil, and Kazakhstan using BusySnake stealer — **Campaign**: Critical infrastructure intelligence collection and credential theft
- **ToddyCat (APT)**: Deployed new Umbrij malware abusing OAuth to access Gmail via Google API; consistent with long-term espionage focus — **Campaign**: Email surveillance of strategic targets
- **Anubis Ransomware Affiliates**: Actively exploiting Citrix Bleed 2 (CVE-2025-5777) for initial access; employing BYOVD techniques and supply chain credential abuse — **Campaign**: Ransomware deployment via NetScaler compromise
- **FortiBleed Actors**: Leveraging compromised Fortinet firewalls (thousands of devices) for initial access; now collaborating with Inc Ransomware and Lynx Ransomware gangs; exploiting Nextcloud zero-day post-compromise — **Campaign**: Access monetization via ransomware partnerships
- **EvilTokens / ARToken Operators**: Running Phishing-as-a-Service platforms providing Microsoft 365 credential harvesting, MFA bypass, and session token theft toolkits — **Campaign**: PhaaS affiliate operations targeting enterprises
- **NetNut / Popa Botnet Operators**: Managed residential proxy network of 2 million compromised Android/IoT devices; disrupted by joint Google/FBI/Lumen operation — **Campaign**: Bandwidth resale for credential stuffing, ad fraud, scraping
- **NSO Group (Pegasus Operator)**: Deployed zero-click exploits against European Parliament member investigating spyware; demonstrates continued targeting of democratic institutions — **Campaign**: Political surveillance

## Source Attribution

- **JadePuffer ransomware used AI agent to automate entire attack**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/jadepuffer-ransomware-used-ai-agent-to-automate-entire-attack/
- **U.S. Government Entity Paid Kairos $1 Million in Data-Theft Extortion Case**: The Hacker News - https://thehackernews.com/2026/07/us-government-entity-paid-kairos-group.html
- **North Korean Hackers Publish 108 Malicious Packages and Extensions in PolinRider Campaign**: The Hacker News - https://thehackernews.com/2026/07/north-korean-hackers-publish-108.html
- **Unpatched Flaws Disclosed in Filesystem Bundled Into Millions of Embedded Devices**: The Hacker News - https://thehackernews.com/2026/07/unpatched-flaws-disclosed-in-filesystem.html
- **New "Bad Epoll" Linux Kernel Flaw Lets Unprivileged Users Gain Root, Hits Android**: The Hacker News - https://thehackernews.com/2026/07/new-bad-epoll-linux-kernel-flaw-lets.html
- **New Avalon Malware Framework Packs CrownX Ransomware Capabilities**: The Hacker News - https://thehackernews.com/2026/07/new-avalon-malware-framework-packs.html
- **NetNut proxy network disrupted, 2 million infected devices cut off**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/netnut-proxy-network-disrupted-2-million-infected-devices-cut-off/
- **North Korea-Linked npm Packages Mimic Rollup Polyfills to Steal Developer Secrets**: The Hacker News - https://thehackernews.com/2026/07/north-korea-linked-npm-packages-mimic.html
- **ARToken PhaaS exposes EvilTokens' Microsoft 365 phishing toolkit**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/artoken-phaas-exposes-eviltokens-microsoft-365-phishing-toolkit/
- **Armored Likho Targets Government Agencies, Power Sector with BusySnake Stealer**: The Hacker News - https://thehackernews.com/2026/07/armored-likho-targets-government.html
- **Chinese LLMs Broaden the Gap Between Attackers \&amp; Defenders**: Dark Reading - https://www.darkreading.com/cyber-risk/chinese-llms-broaden-gap-between-attackers-and-defenders
- **European Parliament Member Investigating Spyware Was Hacked With Pegasus**: The Hacker News - https://thehackernews.com/2026/07/european-parliament-member.html
- **PamStealer Uses Fake Maccy Sites and PAM Checks to Steal Mac Login Passwords**: The Hacker News - https://thehackernews.com/2026/07/pamstealer-uses-fake-maccy-sites-and.html
- **Claude Fable 5 isn’t permanently leaving subscriptions, Anthropic says**: Bleeping Computer - https://www.bleepingcomputer.com/news/artificial-intelligence/claude-fable-5-isnt-permanently-leaving-subscriptions-anthropic-says/
- **Claude Fable relaunch disappoints users with nerfed performance**: Bleeping Computer - https://www.bleepingcomputer.com/news/artificial-intelligence/claude-fable-relaunch-disappoints-users-with-nerfed-performance/
- **Aussies Face Reduced Cybercrime Risk, as Pressure Shifts to SMBs**: Dark Reading - https://www.darkreading.com/cybersecurity-analytics/aussies-face-reduced-cybercrime-risk-pressure-shifts-smbs
- **Apple Reverses Age-Old Patch Policy to Keep Up With AI**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/apple-patch-policy-ai
- **FBI Seizes NetNut Proxy Platform, Popa Botnet**: Krebs on Security - https://krebsonsecurity.com/2026/07/fbi-seizes-netnut-proxy-platform-popa-botnet/
- **FortiBleed Actors Collaborating With Inc, Lynx Ransomware Gangs**: Dark Reading - https://www.darkreading.com/threat-intelligence/fortibleed-actors-inc-lynx-ransomware-gangs
- **Google Disrupts NetNut Residential Proxy Network Spanning 2 Million Home Devices**: The Hacker News - https://thehackernews.com/2026/07/google-disrupts-netnut-residential.html
- **Ransomware Groups Turn to Citrix Bleed 2, BYOVD, and Supply Chain Credentials**: The Hacker News - https://thehackernews.com/2026/07/ransomware-groups-turn-to-citrix-bleed.html
- **Ransomware Thugs Masquerade as Interpol to Entice Small Biz**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/attackers-use-interpol-lure-target-small-businesses
- **ThreatsDay: AI Compute Hijacking, Apple Email Flaw, BlueHammer Ransomware + 14 Stories**: The Hacker News - https://thehackernews.com/2026/07/threatsday-ai-compute-hijacking-apple.html
- **Google loses final appeal to overturn €4.1 billion EU fine**: Bleeping Computer - https://www.bleepingcomputer.com/news/legal/google-loses-final-appeal-to-overturn-41-billion-eu-fine/
- **ConsentFix and ClickFix: How Microsoft 365 Accounts are Hijacked in 3 Seconds**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/consentfix-and-clickfix-how-microsoft-365-accounts-are-hijacked-in-3-seconds/
- **ToddyCat-Linked Umbrij Malware Abuses OAuth to Access Gmail via Google API**: The Hacker News - https://thehackernews.com/2026/07/toddycat-linked-umbrij-malware-abuses.html
- **Anthropic's AI Finds Bugs. IBM Bets $5B It Can Fix Them.**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/anthropic-s-ai-finds-bugs-ibm-bets-5b-it-can-fix-them-
- **Microsoft fixes bug that removed Copilot buttons in Outlook**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-bug-that-removed-copilot-button-in-outlook/
- **Cisco finally confirms attackers exploiting Unified CM flaw**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisco-finally-confirms-attackers-exploiting-unified-cm-flaw/
- **Identity Lifecycle Management Wasn't Built for AI Agents**: The Hacker News - https://thehackernews.com/2026/07/identity-lifecycle-management.html
