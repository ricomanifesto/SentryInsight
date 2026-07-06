# Exploitation Report

## Executive Summary

Critical exploitation activity spans multiple vectors this period, from kernel-level privilege escalation to AI-automated ransomware and supply chain poisoning. The most immediately dangerous vulnerability is **CVE-2026-46242 (Bad Epoll)**, a Linux kernel flaw that allows unprivileged local users to gain root access on desktops, servers, and Android devices. Simultaneously, ransomware operators are actively exploiting **CVE-2025-5777 (Citrix Bleed 2)** for initial access, while FortiBleed actors have added a Nextcloud zero-day to their arsenal and are now collaborating with Inc and Lynx ransomware gangs to monetize thousands of compromised Fortinet firewalls.

Nation-state activity remains intense. North Korean operators linked to the Contagious Interview campaign have published 108 malicious packages and browser extensions across npm, Packagist, Go, and Chrome Web Store in the PolinRider campaign, while a separate cluster mimics Rollup polyfills to steal developer secrets. A newly identified actor, Armored Likho, is targeting government agencies and the electric power sector across Russia, Brazil, and Kazakhstan with the BusySnake stealer. The Kairos extortion group successfully extracted a $1 million payment from a U.S. government entity, and Pegasus spyware was deployed against a European Parliament member investigating surveillance abuses.

Emerging techniques signal a shift in the threat landscape. Researchers demonstrated **TrojPix**, a method to exfiltrate data from air-gapped systems via video cable emissions. The **JadePuffer** operation represents the first documented case of a ransomware attack fully automated by an LLM agent. **ConsentFix and ClickFix** attacks are hijacking Microsoft 365 accounts in seconds through OAuth flow abuse, while **SkillCloak** demonstrates packing techniques that evade static analysis of AI agent skills. A joint Google-FBI operation disrupted the NetNut residential proxy network, cutting off two million compromised Android devices, smart TVs, and streaming boxes.

## Active Exploitation Details

### Bad Epoll (CVE-2026-46242)
- **Description**: A Linux kernel flaw in the epoll subsystem that allows an unprivileged local user to escalate privileges to root. The vulnerability affects the core event notification mechanism used for I/O multiplexing.
- **Impact**: Full system compromise with root privileges. Attackers can bypass all access controls, install persistent rootkits, access all data, and pivot across the network. The flaw impacts Linux desktops, servers, and Android devices.
- **Status**: Actively exploitable. Public disclosure has occurred; patch status varies by distribution and Android OEM. No evidence of in-the-wild exploitation cited in source, but trivial local exploitability makes immediate patching critical.
- **CVE ID**: CVE-2026-46242

### Citrix Bleed 2 (CVE-2025-5777)
- **Description**: A vulnerability in Citrix NetScaler ADC and Gateway appliances that enables unauthenticated remote attackers to obtain active session tokens and bypass authentication.
- **Impact**: Full administrative access to the appliance, allowing attackers to pivot into internal networks, harvest credentials, and deploy ransomware. Anubis ransomware operators are actively leveraging this for initial access.
- **Status**: Actively exploited by Anubis ransomware group. Patches available from Citrix; urgent application required for all exposed instances.
- **CVE ID**: CVE-2025-5777

### Nextcloud Zero-Day
- **Description**: An undisclosed zero-day vulnerability in Nextcloud, an open-source file sync and share platform. Specific technical details were not released in the source reporting.
- **Impact**: FortiBleed threat actors are exploiting this vulnerability alongside their existing Fortinet firewall compromises to expand access and facilitate ransomware deployment by partner groups.
- **Status**: Actively exploited in the wild by FortiBleed actors. No patch information available in source articles; Nextcloud administrators should monitor for emergency releases.
- **CVE ID**: Not assigned in source reporting

### FatFs Filesystem Vulnerabilities (Seven Flaws)
- **Description**: Seven vulnerabilities disclosed in FatFs, a lightweight FAT/exFAT filesystem library embedded in millions of IoT, industrial, automotive, and consumer devices. Flaws include buffer overflows, integer overflows, and path traversal issues triggered by malformed filesystem images on USB drives or SD cards.
- **Impact**: Remote code execution or denial of service when a malicious storage medium is inserted. Given the library's ubiquity in embedded systems with no patching mechanism, the attack surface is vast and largely unpatchable.
- **Status**: Unpatched as of disclosure by runZero. Vendors of affected devices must incorporate fixes and push firmware updates; many devices will never receive patches.
- **CVE ID**: Not assigned in source reporting

### Opera GX Mod Auto-Install Flaw
- **Description**: A flaw in Opera GX's "Mods" feature that allows a malicious website to silently install a browser extension/mod without user consent, which can then read and exfiltrate data from any page the user visits.
- **Impact**: Complete compromise of browser session data across all origins, including authentication tokens, personal information, and corporate data accessed through the browser.
- **Status**: Disclosed by researchers; patch status not specified in source. Opera GX users should update immediately and audit installed mods.
- **CVE ID**: Not assigned in source reporting

### Apple Email Flaw
- **Description**: A vulnerability in Apple's email infrastructure or client referenced in the ThreatsDay roundup. Specific technical details were not provided in the source article.
- **Impact**: Potential email compromise, data leakage, or account takeover depending on the exact nature of the flaw.
- **Status**: Mentioned as a current weak spot in the ThreatsDay summary; no patch or exploitation status details available in source.
- **CVE ID**: Not assigned in source reporting

## Affected Systems and Products

- **Linux Kernel (Desktop, Server, Android)**: All versions with the vulnerable epoll implementation; CVE-2026-46242 allows local root escalation.
- **Citrix NetScaler ADC and Gateway**: Unpatched appliances exposed to the internet; actively targeted by Anubis ransomware via CVE-2025-5777.
- **Nextcloud Instances**: Self-hosted and managed deployments; targeted by FortiBleed actors via an undisclosed zero-day.
- **Devices Using FatFs Library**: Millions of embedded devices across IoT, industrial control, automotive, medical, and consumer electronics that read FAT/exFAT media; seven unpatched vulnerabilities with no vendor fix timeline.
- **Opera GX Browser**: Gaming-focused browser versions with the Mods feature enabled; silent extension installation and cross-origin data theft.
- **Microsoft 365 Tenants**: All organizations using Microsoft 365; targeted by ConsentFix and ClickFix OAuth token theft attacks that bypass MFA.
- **Android Devices**: Broad range of versions affected by Bad Epoll (CVE-2026-46242) and previously compromised by NetNut/Popa botnet (2 million devices).
- **Windows, Linux, macOS**: All platforms targeted by QuimaRAT MaaS, a cross-platform Java-based remote access trojan.
- **npm, Packagist, Go Module Proxy, Chrome Web Store**: Supply chain repositories poisoned with 108 malicious packages/extensions by North Korean actors (PolinRider campaign) and additional typosquat packages mimicking Rollup polyfills.
- **macOS Systems**: Targeted by PamStealer info-stealer distributed via fake Maccy clipboard manager sites; leverages PAM authentication prompts to capture login passwords.
- **Fortinet FortiGate Firewalls**: Thousands compromised by FortiBleed actors; access now being monetized through collaboration with Inc and Lynx ransomware gangs.
- **AI Coding Agents (VS Code, Cursor, etc.)**: Extension/skill ecosystems vulnerable to SkillCloak packing technique that evades static malware scanners.
- **Air-Gapped Systems with Video Output**: Systems using VGA, DVI, or HDMI cables; vulnerable to TrojPix electromagnetic emanation data exfiltration.

## Attack Vectors and Techniques

- **Local Privilege Escalation via Kernel Epoll Abuse**: Exploitation of CVE-2026-46242 (Bad Epoll) to escalate from unprivileged user to root on Linux/Android without requiring additional vulnerabilities.
- **Unauthenticated Session Hijacking on Citrix NetScaler**: Exploitation of CVE-2025-5777 (Citrix Bleed 2) to harvest valid session tokens and assume administrative identities without credentials.
- **Supply Chain Poisoning via Malicious Packages**: North Korean actors publishing 108 packages across npm, Packagist, Go, and Chrome Web Store (PolinRider); separate campaign typosquatting Rollup polyfill packages to steal developer credentials and enable remote access.
- **OAuth Token Theft via ConsentFix/ClickFix**: Attackers lure victims to malicious sites that trigger legitimate Microsoft OAuth consent prompts; once approved, attackers receive valid access/refresh tokens, bypassing MFA and compromising M365 accounts in seconds.
- **Phishing-as-a-Service (ARToken/EvilTokens)**: Turnkey phishing kits targeting Microsoft 365 credentials with adversary-in-the-middle capabilities, session hijacking, and automated MFA bypass.
- **Multi-Stage Phishing Delivering Modular Malware (Avalon)**: Phishing chains that deliver the Avalon framework, which includes CrownX ransomware, credential harvesters, and lateral movement tools; bypasses traditional email security.
- **BYOVD (Bring Your Own Vulnerable Driver)**: Ransomware groups loading signed but vulnerable kernel drivers to disable EDR/AV and escalate privileges; observed alongside Citrix Bleed 2 exploitation.
- **Residential Proxy Botnet (NetNut/Popa)**: Two million compromised Android devices, smart TVs, and streaming boxes enrolled as exit nodes for anonymizing malicious traffic; disrupted by Google/FBI joint operation.
- **AI-Automated Ransomware Operations (JadePuffer)**: First documented case of an LLM agent autonomously executing the full ransomware kill chain: reconnaissance, exploitation, lateral movement, encryption, and extortion.
- **Air-Gapped Data Exfiltration via Video Emanations (TrojPix)**: Modulating pixel values to encode data in electromagnetic emissions from video cables; receivable at a distance with software-defined radio equipment.
- **macOS Credential Theft via Fake App Spoofing and PAM Abuse (PamStealer)**: Typosquat domains mimicking the Maccy clipboard manager deliver a stealer that triggers legitimate PAM authentication dialogs to phish user passwords.
- **AI Skill/Extension Obfuscation (SkillCloak)**: Self-extracting packing technique that hides malicious payloads in AI agent skills/extensions, evading static analysis while preserving runtime functionality.
- **Spyware Deployment Against High-Value Targets (Pegasus)**: Zero-click or one-click exploits targeting iOS/Android; used against a European Parliament member investigating spyware abuse.
- **Social Engineering via Authority Impersonation**: Ransomware campaigns masquerading as Interpol communications to trick small businesses into executing payloads.
- **Web Browser Extension Silent Install (Opera GX Flaw)**: Abuse of the Mods installation flow to deploy extensions without user interaction, granting immediate access to all DOM content across origins.

## Threat Actor Activities

- **North Korean Actors (Contagious Interview / PolinRider Campaign)**: Published 108 malicious packages and browser extensions across npm, Packagist, Go module proxy, and Chrome Web Store. Separate cluster mimics Rollup polyfill packages to steal developer secrets and establish persistent access. Attribution to DPRK based on infrastructure, TTPs, and prior campaign overlaps.
- **Armored Likho**: Newly identified threat actor targeting government agencies and the electric power sector in Russia, Brazil, and Kazakhstan. Deploys BusySnake stealer for credential harvesting and reconnaissance. Motivations appear to be espionage and potential disruptive capability positioning.
- **Kairos Extortion Group**: Conducted data-theft extortion against a U.S. government entity, securing a $1 million payment to prevent data leakage. Negotiation chat leaked, revealing operational details. Pure extortion model without ransomware encryption.
- **FortiBleed Actors**: Compromised thousands of Fortinet FortiGate firewalls via FortiOS vulnerabilities. Now collaborating with Inc Ransomware and Lynx Ransomware gangs to monetize access. Added exploitation of a Nextcloud zero-day to expand footholds in victim environments.
- **Anubis Ransomware**: Actively exploiting Citrix Bleed 2 (CVE-2025-5777) for initial access. Combines with BYOVD techniques for defense evasion and uses supply chain credentials for lateral movement.
- **Inc Ransomware**: Partnering with FortiBleed actors to deploy ransomware on networks accessed via compromised FortiGate firewalls.
- **Lynx Ransomware**: Collaborating with FortiBleed and Inc groups; part of the emerging consortium monetizing firewall-level access.
- **JadePuffer Operators**: Deployed the first fully AI-automated ransomware attack, using an LLM agent to execute all phases from initial access to extortion without human intervention.
- **EvilTokens / ARToken Operators**: Running a mature Phishing-as-a-Service ecosystem targeting Microsoft 365. ARToken operates as an affiliate, exposing the broader toolkit including AiTM proxies, session token replay, and automated MFA bypass.
- **Pegasus Operators (NSO Group Customers)**: Deployed Pegasus spyware against former European Parliament member Stelios Kouloglou repeatedly while he served on a spyware investigation committee. Attribution to government clients of NSO Group.
- **NetNut / Popa Botnet Operators**: Operated a residential proxy service backed by two million compromised Android/IoT devices. Infrastructure seized by FBI with Google and Lumen assistance; domains taken down.
- **QuimaRAT Developers / MaaS Affiliates**: Distributing a cross-platform Java RAT via Malware-as-a-Service model; capabilities include remote shell, file management, keylogging, and persistence on Windows, Linux, and macOS.
- **Avalon Framework Operators**: Distributing a modular malware framework (including CrownX ransomware) through sophisticated multi-stage phishing chains that bypass traditional email security controls.

## Source Attribution

- **New TrojPix Attack Leaks Data From Air-Gapped Systems via Video Cable Emissions**: The Hacker News - https://thehackernews.com/2026/07/new-trojpix-attack-leaks-data-from-air.html
- **New Java-Based QuimaRAT MaaS Built to Run on Windows, Linux, and macOS**: The Hacker News - https://thehackernews.com/2026/07/new-java-based-quimarat-maas-built-to.html
- **Opera GX Flaw Let Malicious Sites Auto-Install Mods to Steal Data From Visited Pages**: The Hacker News - https://thehackernews.com/2026/07/opera-gx-flaw-let-malicious-sites-auto.html
- **SkillCloak Lets Malicious AI Agent Skills Evade Static Scanners with Self-Extracting Packing**: The Hacker News - https://thehackernews.com/2026/07/new-skillcloak-technique-lets-malicious.html
- **Flipper Zero firmware development continues with community help**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/flipper-zero-firmware-development-continues-with-community-help/
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
