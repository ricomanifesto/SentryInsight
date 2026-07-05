# Exploitation Report

## Executive Summary

A significant escalation in AI-driven offensive operations has emerged with the first documented case of a fully autonomous ransomware attack. Researchers identified JadePuffer, a ransomware operation conducted entirely by a large language model agent, marking a paradigm shift in threat automation. Simultaneously, North Korean threat actors continue expanding their software supply chain campaigns, publishing 108 malicious packages across npm, Packagist, Go, and Chrome Web Store under the PolinRider campaign, while a separate cluster mimics Rollup polyfills to steal developer secrets.

Critical infrastructure exploitation is accelerating across multiple fronts. The Bad Epoll vulnerability (CVE-2026-46242) in the Linux kernel enables unprivileged users to gain root access on Linux desktops, servers, and Android devices. Ransomware groups including Anubis are actively exploiting Citrix Bleed 2 (CVE-2025-5777) for initial access, while FortiBleed actors have monetized access to thousands of compromised Fortinet firewalls and begun leveraging a Nextcloud zero-day. A joint FBI-Google operation dismantled the NetNut residential proxy network, cutting off two million compromised Android devices including smart TVs and streaming boxes.

## Active Exploitation Details

### Bad Epoll Linux Kernel Privilege Escalation
- **Description**: A newly disclosed Linux kernel flaw in the epoll subsystem allows an ordinary user with no special access to take full control of a machine as root. The vulnerability affects the core event notification mechanism used throughout the kernel.
- **Impact**: Complete system compromise with root privileges on affected Linux desktops, servers, and Android devices. Attackers can bypass all access controls, install persistent malware, and access all data.
- **Status**: Actively exploitable; patch availability varies by distribution and Android vendor. Android impact is particularly significant due to fragmented patching.
- **CVE ID**: CVE-2026-46242

### Citrix Bleed 2 Exploitation by Ransomware Groups
- **Description**: Threat actors associated with the Anubis ransomware operation are exploiting a vulnerability in Citrix NetScaler ADC and Gateway appliances to obtain initial access to target networks.
- **Impact**: Unauthenticated remote attackers can gain a foothold in organizational networks, enabling lateral movement, data exfiltration, and ransomware deployment.
- **Status**: Actively exploited in the wild. Patches available from Citrix; organizations running vulnerable versions remain at high risk.
- **CVE ID**: CVE-2025-5777

### Cisco Unified Communications Manager Exploitation
- **Description**: Attackers are exploiting a vulnerability in Cisco Unified Communications Manager (Unified CM) that was patched in early June 2026. Cisco has confirmed active exploitation in the wild.
- **Impact**: Compromise of enterprise voice and video communication infrastructure, potential eavesdropping, call manipulation, and lateral movement into connected systems.
- **Status**: Actively exploited post-patch. Organizations that have not applied the June 2026 security updates are vulnerable.

### FatFs Filesystem Library Vulnerabilities
- **Description**: Security firm runZero disclosed seven vulnerabilities in FatFs, a lightweight filesystem library supporting FAT and exFAT formats used on USB drives and SD cards. The library is bundled into millions of embedded devices.
- **Impact**: Potential code execution, denial of service, or filesystem corruption on affected embedded devices including IoT, industrial control systems, automotive, and consumer electronics.
- **Status**: Unpatched as of disclosure. Vendors must integrate fixes into their firmware; widespread deployment in embedded systems complicates remediation.

### Nextcloud Zero-Day Exploitation
- **Description**: FortiBleed actors have begun exploiting a zero-day vulnerability in Nextcloud, an open-source file sharing and collaboration platform, as part of their monetization strategy after compromising Fortinet firewalls.
- **Impact**: Unauthorized access to sensitive files, collaboration data, and potential further compromise of connected systems.
- **Status**: Zero-day actively exploited; patch status unclear from available reporting.

### JadePuffer AI-Automated Ransomware
- **Description**: The first documented case of a ransomware operation conducted entirely by a large language model (LLM) agent. The JadePuffer operation demonstrates end-to-end automation from initial access through encryption and extortion.
- **Impact**: Drastically reduced time-to-exploit and operational costs for attackers; potential for massive scaling of ransomware campaigns without human operators.
- **Status**: Active operation observed; represents aidentified by researchers; demonstrates proof-of-concept for fully autonomous cybercrime.

## Affected Systems and Products

- **Linux Kernel (epoll subsystem)**: All Linux distributions and Android devices running vulnerable kernel versions; impacts desktops, servers, mobile devices, and embedded Linux systems
- **Citrix NetScaler ADC and Gateway**: Versions vulnerable to CVE-2025-5777 (Citrix Bleed 2); widely deployed for remote access and application delivery
- **Cisco Unified Communications Manager**: Enterprise deployments running versions prior to June 2026 security patches
- **FatFs Filesystem Library**: Millions of embedded devices across IoT, industrial control systems, automotive, medical devices, and consumer electronics using FAT/exFAT on removable media
- **Nextcloud**: Self-hosted and managed deployments; version(s) affected by the zero-day not publicly specified
- **Android Devices (NetNut/Popa Botnet)**: Two million compromised home devices including smartphones, smart TVs, streaming boxes, and other IoT devices enrolled in residential proxy network
- **npm, Packagist, Go Module Proxy, Chrome Web Store**: Developer ecosystems targeted by 108 malicious packages in the PolinRider supply chain campaign
- **Microsoft 365 / Entra ID**: Organizations targeted by ConsentFix, ClickFix, and ARToken/EvilTokens phishing-as-a-service operations
- **Google Workspace / Gmail**: Accounts targeted by ToddyCat's Umbrij malware abusing OAuth flows
- **macOS Systems**: Users targeted by PamStealer via fake Maccy clipboard manager sites and PAM authentication prompts

## Attack Vectors and Techniques

- **AI-Agent Autonomous Operations**: Large language model agents conducting end-to-end ransomware operations including reconnaissance, exploitation, lateral movement, encryption, and extortion negotiation without human intervention (JadePuffer)
- **Software Supply Chain Compromise**: Publication of 108 malicious packages across multiple package registries (npm, Packagist, Go) and browser extension store (Chrome Web Store) masquerading as legitimate tooling (PolinRider, Rollup polyfill mimics)
- **Kernel Privilege Escalation via epoll**: Exploitation of race condition or reference counting flaw in Linux epoll interface to escalate from unprivileged user to root (CVE-2026-46242)
- **Citrix NetScaler Unauthenticated RCE**: Exploitation of CVE-2025-5777 for initial access without credentials, enabling ransomware deployment
- **Bring Your Own Vulnerable Driver (BYOVD)**: Ransomware groups loading known vulnerable kernel drivers to disable security tools and escalate privileges
- **Supply Chain Credential Theft**: Compromise of upstream credentials to access downstream targets; used in conjunction with Citrix Bleed 2 and BYOVD
- **OAuth Token Hijacking (ConsentFix/ClickFix)**: Fake OAuth consent prompts and malicious applications stealing Microsoft 365 tokens in seconds, bypassing MFA
- **Phishing-as-a-Service (ARToken/EvilTokens)**: Modular M365 phishing toolkits sold as a service with affiliate programs, including reverse proxy, 2FA capture, and session hijacking
- **OAuth Abuse for Email Access (Umbrij)**: Malware using stolen OAuth tokens to access Gmail via Google API, maintaining persistent email surveillance
- **Residential Proxy Botnet (NetNut/Popa)**: Compromised consumer devices routed through residential IPs for credential stuffing, ad fraud, scraping, and anonymizing malicious traffic
- **Fake Legitimate Software Sites (PamStealer)**: Typosquatting and clone sites mimicking popular open-source tools (Maccy) to deliver macOS info-stealers
- **PAM Authentication Prompt Spoofing**: Abuse of macOS Pluggable Authentication Modules to present fake password prompts capturing login credentials
- **Spyware Deployment (Pegasus)**: Zero-click or one-click exploitation targeting high-value individuals (European Parliament member) for surveillance

## Threat Actor Activities

- **JadePuffer Operator**: First known threat actor (or autonomous agent) to conduct a fully AI-automated ransomware operation; represents emergence of LLM-driven offensive autonomy
- **North Korean Actors (Contagious Interview / PolinRider)**: Published 108 malicious packages across npm, Packagist, Go, and Chrome Web Store; ongoing supply chain campaign targeting developers globally
- **North Korean Actors (Rollup Polyfill Mimics)**: Separate or related cluster publishing npm packages impersonating Rollup polyfill tooling for remote access and data theft; attributed by JFrog
- **Anubis Ransomware Group**: Actively exploiting Citrix Bleed 2 (CVE-2025-5777) for initial access; employing BYOVD and supply chain credential techniques
- **FortiBleed Actors**: Compromised thousands of Fortinet firewalls; now monetizing access through collaboration with Inc Ransomware and Lynx Ransomware gangs; exploiting Nextcloud zero-day
- **Inc Ransomware Gang**: Collaborating with FortiBleed actors to leverage firewall access for ransomware deployment
- **Lynx Ransomware Gang**: Partnering with FortiBleed actors in joint monetization of compromised Fortinet infrastructure
- **Kairos Extortion Group**: Conducted data-theft extortion against a U.S. government entity; received $1 million payment per leaked negotiation chat analyzed by Ransom-ISAC
- **Armored Likho**: Previously undocumented actor targeting government agencies and electric power sector in Russia, Brazil, and Kazakhstan using BusySnake stealer
- **ToddyCat**: Chinese-aligned APT attributed to Umbrij malware; abuses OAuth tokens to access Gmail via Google API for email surveillance
- **EvilTokens / ARToken Operators**: Running mature phishing-as-a-service platform targeting Microsoft 365 with affiliate model (ARToken); toolkit includes MFA bypass, session hijacking, and reverse proxy
- **Popa Botnet / NetNut Operators**: Built and operated residential proxy network spanning two million compromised Android devices; disrupted by FBI-Google-Lumen joint operation
- **Pegasus Operators (NSO Group clients)**: Targeted former European Parliament member Stelios Kouloglou with Pegasus spyware during spyware investigation; attributed by Citizen Lab

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
