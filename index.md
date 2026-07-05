# Exploitation Report

## Executive Summary

A newly disclosed Linux kernel vulnerability tracked as CVE-2026-46242, dubbed "Bad Epoll," enables unprivileged users to achieve full root compromise across Linux desktops, servers, and Android devices. This privilege escalation flaw represents a critical risk given the ubiquity of affected systems and the reliability of the exploit primitive. Simultaneously, ransomware operators are actively exploiting Citrix Bleed 2 (CVE-2025-5777) for initial access, with the Anubis ransomware group confirmed leveraging this vulnerability in ongoing campaigns.

Multiple threat actors are diversifying initial access vectors beyond traditional vulnerability exploitation. North Korean operators linked to the Contagious Interview campaign have published 108 malicious packages across npm, Packagist, Go, and Chrome Web Store in the PolinRider supply chain operation, while a separate cluster mimics Rollup polyfill tooling to steal developer credentials. The Kairos extortion group extracted a $1 million payment from a U.S. government entity following data theft, and the ToddyCat APT deployed the novel Umbrij malware to abuse OAuth flows for persistent Gmail access via Google APIs.

## Active Exploitation Details

### Bad Epoll Linux Kernel Privilege Escalation
- **Description**: A Linux kernel flaw in the epoll subsystem allows an unprivileged local user to escalate privileges to root. The vulnerability affects the core event notification mechanism used throughout the kernel.
- **Impact**: Attackers gain full root control over affected Linux desktops, servers, and Android devices, enabling complete system compromise, persistence, and lateral movement.
- **Status**: Actively exploitable; affects current Linux kernel versions and Android. Patch availability varies by distribution and Android OEM.
- **CVE ID**: CVE-2026-46242

### Citrix Bleed 2 Exploitation by Ransomware Actors
- **Description**: A vulnerability in Citrix NetScaler ADC and Gateway appliances that allows unauthenticated attackers to bypass authentication and access sensitive system resources.
- **Impact**: Provides initial access to corporate networks for ransomware deployment. Confused exploited by Anubis ransomware operation for network foothold.
- **Status**: Actively exploited in the wild by Anubis ransomware group; patches available from Citrix.
- **CVE ID**: CVE-2025-5777

### Cisco Unified Communications Manager Exploitation
- **Description**: A vulnerability in Cisco Unified Communications Manager (Unified CM) that Cisco has confirmed is being actively exploited by attackers.
- **Impact**: Compromise of enterprise voice and video communication infrastructure, potential for eavesdropping, call manipulation, and lateral movement.
- **Status**: Actively exploited; patches released in early June 2026.

### FatFs Filesystem Library Vulnerabilities
- **Description**: Seven vulnerabilities disclosed in FatFs, a lightweight filesystem library for FAT/exFAT support embedded in millions of IoT, industrial, and consumer devices.
- **Impact**: Potential for code execution, denial of service, and filesystem corruption on affected embedded devices when processing malicious storage media.
- **Status**: Unpatched as of disclosure; affects vast deployed base with limited update mechanisms.

### Nextcloud Zero-Day Exploitation
- **Description**: A previously unknown vulnerability in Nextcloud collaboration platform being exploited by FortiBleed threat actors.
- **Impact**: Access to file shares, user data, and potential pivot points into connected infrastructure.
- **Status**: Zero-day actively exploited; patch status unclear from available reporting.

### Pegasus Spyware Deployment
- **Description**: NSO Group's Pegasus spyware used to repeatedly compromise the mobile device of a European Parliament member investigating spyware abuses.
- **Impact**: Full device compromise including message interception, location tracking, microphone/camera access, and contact exfiltration.
- **Status**: Ongoing targeting of high-value political figures; no user-interaction required in some variants.

## Affected Systems and Products

- **Linux Kernel / Android**: All Linux distributions running vulnerable kernel versions; Android devices across OEMs — privilege escalation via CVE-2026-46242
- **Citrix NetScaler ADC and Gateway**: Appliances running versions vulnerable to CVE-2025-5777 — authentication bypass and initial access
- **Cisco Unified Communications Manager**: Enterprise deployments patched prior to early June 2026 — active exploitation confirmed
- **FatFs-Embedded Devices**: Millions of IoT devices, industrial controllers, automotive systems, and consumer electronics using FatFs library — seven unpatched vulnerabilities
- **Nextcloud Instances**: Self-hosted and managed Nextcloud deployments — zero-day exploited by FortiBleed actors
- **Mobile Devices (iOS/Android)**: High-value targets — Pegasus spyware deployment via zero-click or one-click exploits
- **npm/Packagist/Go/Chrome Extension Ecosystems**: Developer workstations and CI/CD pipelines — 108 malicious packages in PolinRider campaign
- **Microsoft 365 Tenants**: Organizations using OAuth authentication — ConsentFix/ClickFix token theft and ARToken/EvilTokens phishing kits

## Attack Vectors and Techniques

- **Local Privilege Escalation via Epoll**: Exploitation of race condition or reference counting error in Linux kernel's epoll interface — local unprivileged user to root
- **Authentication Bypass on Network Appliances**: Unauthenticated HTTP requests to Citrix NetScaler endpoints — CVE-2025-5777 exploitation for initial access
- **Supply Chain Poisoning**: Publication of typo-squatted and brand-impersonating packages to public registries (npm, Packagist, Go) and Chrome Web Store — 108 packages in PolinRider campaign; Rollup polyfill mimicry for credential theft
- **AI-Automated Attack Chains**: LLM agent orchestrating full ransomware lifecycle from reconnaissance to encryption — JadePuffer ransomware operation
- **OAuth Token Theft via Consent Phishing**: Fake OAuth consent prompts (ConsentFix/ClickFix) stealing Microsoft 365 tokens in seconds — MFA bypass without credential phishing
- **OAuth Abuse for Persistent Email Access**: Malware (Umbrij) leveraging stolen OAuth tokens to access Gmail via Google API — ToddyCat APT
- **Phishing-as-a-Service Infrastructure**: ARToken affiliate platform leveraging EvilTokens toolkit for Microsoft 365 credential harvesting — commoditized phishing campaigns
- **Residential Proxy Botnet Enrollment**: Compromise of Android devices (smart TVs, streaming boxes) into NetNut/Popa proxy network — 2 million devices for traffic relaying
- **Malicious Browser Extensions**: Chrome Web Store extensions with hidden data exfiltration and remote access capabilities — North Korean PolinRider campaign
- **BYOVD (Bring Your Own Vulnerable Driver)**: Ransomware actors loading signed but vulnerable drivers to disable EDR — referenced alongside Citrix Bleed 2 exploitation

## Threat Actor Activities

- **North Korean Actors (Contagious Interview / PolinRider)**: Published 108 malicious packages across npm, Packagist, Go, and Chrome Web Store targeting software developers and build pipelines; separate cluster mimicking Rollup polyfill packages for credential theft
- **Kairos Extortion Group**: Conducted data-theft extortion against a U.S. government entity, securing $1 million payment to prevent leak of stolen files; negotiation chat leaked
- **JadePuffer Operators**: First documented ransomware operation executed entirely by an LLM agent, automating reconnaissance, exploitation, lateral movement, and encryption
- **Anubis Ransomware Group**: Actively exploiting Citrix Bleed 2 (CVE-2025-5777) for initial access; employing BYOVD techniques for defense evasion
- **FortiBleed Actors**: Leveraging access to thousands of compromised Fortinet firewalls; collaborating with Inc and Lynx ransomware gangs for monetization; exploiting Nextcloud zero-day
- **Inc Ransomware Gang**: Partnering with FortiBleed actors for access to pre-compromised Fortinet appliances
- **Lynx Ransomware Gang**: Collaborating with FortiBleed and Inc actors in joint monetization efforts
- **ToddyCat (APT)**: Deployed novel Umbrij malware to abuse OAuth tokens for persistent Gmail access via Google APIs; targets aligned with Chinese strategic interests
- **Armored Likho**: Previously undocumented actor targeting government agencies and electric power sector in Russia, Brazil, and Kazakhstan using BusySnake stealer
- **EvilTokens / ARToken Operators**: Running phishing-as-a-service platform with sophisticated Microsoft 365 toolkit; ARToken operates as EvilTokens affiliate
- **Popa Botnet / NetNut Operators**: Built and maintained residential proxy network spanning 2 million compromised home devices; disrupted by FBI/Google/Lumen joint operation
- **NSO Group (Pegasus)**: Continued deployment of zero-click spyware against high-value political targets including European Parliament members

## Source Attribution

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
- **ToddyCat-Linked Umbrij Malware Abuses OAuth to Access Gmail via Google API**: The Hacker News - https://thehackernews.com/2026/07/toddycat-linked-umbrij-malware-abuses.html
- **Anthropic's AI Finds Bugs. IBM Bets $5B It Can Fix Them.**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/anthropic-s-ai-finds-bugs-ibm-bets-5b-it-can-fix-them-
- **Microsoft fixes bug that removed Copilot buttons in Outlook**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-bug-that-removed-copilot-button-in-outlook/
- **Cisco finally confirms attackers exploiting Unified CM flaw**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisco-finally-confirms-attackers-exploiting-unified-cm-flaw/
