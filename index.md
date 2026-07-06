# Exploitation Report

## Executive Summary

Critical exploitation activity continues to escalate across multiple vectors, with two confirmed actively exploited vulnerabilities receiving CVE designations. The Linux kernel privilege escalation flaw CVE-2026-46242 ("Bad Epoll") allows unprivileged users to gain root access on Linux desktops, servers, and Android devices. Simultaneously, ransomware operators—including the Anubis operation—are actively exploiting Citrix Bleed 2 (CVE-2025-5777) for initial access. Beyond these patched-but-exploited vulnerabilities, seven unpatched flaws in the ubiquitous FatFs filesystem library expose millions of embedded devices, while a Nextcloud zero-day and a Cisco Unified CM vulnerability patched in June are now confirmed under active exploitation.

Threat actor innovation is accelerating, with North Korean operators conducting massive supply chain campaigns across npm, Packagist, Go, and Chrome extensions (108 malicious packages in the PolinRider campaign alone), and the first documented case of a fully AI-automated ransomware operation (JadePuffer) demonstrating LLM-driven attack chains. Phishing-as-a-Service ecosystems continue to mature, with EvilTokens and its ARToken affiliate exposing sophisticated Microsoft 365 token theft toolkits (ConsentFix/ClickFix), while ToddyCat's Umbrij malware abuses OAuth flows to access Gmail via Google APIs. The NetNut residential proxy botnet—spanning two million compromised Android devices including smart TVs—was disrupted through a joint FBI-Google operation, highlighting the scale of device compromise feeding proxy-for-hire networks.

## Active Exploitation Details

### Bad Epoll (CVE-2026-46242)
- **Description**: A Linux kernel flaw in the epoll subsystem that allows an unprivileged local user to escalate privileges to root. The vulnerability stems from improper handling of file descriptor references in the epoll mechanism, enabling a use-after-free condition that can be exploited for arbitrary kernel code execution.
- **Impact**: Full system compromise with root privileges on affected Linux desktops, servers, and Android devices. Attackers can bypass all access controls, install persistent rootkits, access encrypted data, and pivot laterally across networks.
- **Status**: Actively exploitable; patch availability depends on kernel version and distribution update channels. Android devices await vendor-specific security updates.
- **CVE ID**: CVE-2026-46242

### Citrix Bleed 2 (CVE-2025-5777)
- **Description**: A vulnerability in Citrix NetScaler ADC and NetScaler Gateway that allows unauthenticated remote attackers to obtain active session tokens and bypass authentication mechanisms. The flaw enables session hijacking without requiring user interaction.
- **Impact**: Attackers gain valid authenticated sessions to NetScaler appliances, providing a foothold for lateral movement, data exfiltration, and ransomware deployment. Observed in use by Anubis ransomware operators for initial access.
- **Status**: Actively exploited in the wild by ransomware groups. Patches available from Citrix; organizations urged to rotate all credentials and invalidate sessions post-patching.
- **CVE ID**: CVE-2025-5777

### Cisco Unified Communications Manager Vulnerability
- **Description**: A vulnerability in Cisco Unified Communications Manager (Unified CM) that was patched in early June 2026. Cisco has now confirmed that attackers are actively exploiting this flaw in the wild.
- **Impact**: Successful exploitation could allow unauthenticated remote attackers to execute arbitrary code or cause denial-of-service conditions on affected Unified CM deployments, potentially disrupting enterprise voice and video communications.
- **Status**: Actively exploited post-patch. Cisco has released security updates; administrators should apply patches immediately and monitor for indicators of compromise.
- **CVE ID**: Not specified in source articles

### FatFs Vulnerabilities in FatFs Filesystem Library
- **Description**: Seven vulnerabilities disclosed by runZero in FatFs, a lightweight filesystem library enabling FAT/exFAT support on embedded devices. The flaws include buffer overflows, integer overflows, and out-of-bounds read/write conditions triggered by malformed filesystem images on USB drives or SD cards.
- **Impact**: Remote code execution or device compromise when a malicious storage medium is inserted. Given FatFs's integration into millions of IoT, industrial, automotive, and consumer devices, the attack surface is vast and largely unpatchable in deployed fleets.
- **Status**: Unpatched as of disclosure. No upstream fixes released; mitigation requires vendor-specific firmware updates which may never arrive for many device classes.
- **CVE ID**: Not specified in source articles

 Nextcloud Zero-Day Vulnerability
- **Description**: A zero-day vulnerability in Nextcloud referenced in relation to FortiBleed actor activity. Specific technical details were not disclosed in the source articles.
- **Impact**: Presumed to allow unauthorized access, data exfiltration, or remote code execution on Nextcloud instances. Being leveraged by FortiBleed actors alongside Fortinet firewall compromises.
- **Status**: Zero-day; actively exploited. No patch information available in source articles.
- **CVE ID**: Not specified in source articles

 Pegasus Spyware Exploitation
- **Description**: NSO Group's Pegasus spyware used to repeatedly compromise the mobile device of former European Parliament Member Stelios Kouloglou while he was investigating spyware abuses. Pegasus typically exploits zero-click vulnerabilities in mobile operating systems and applications.
- **Impact**: Full device compromise including message interception, call recording, location tracking, camera/microphone activation, and credential theft. Targeted at high-value political figures.
- **Status**: Ongoing exploitation by state-aligned actors. Zero-day vulnerabilities used are not publicly disclosed or patched at time of targeting.
- **CVE ID**: Not specified in source articles

## Affected Systems and Products

- **Linux Kernel (desktops, servers, Android)**: All versions containing the vulnerable epoll implementation prior to patched releases. CVE-2026-46242 affects a broad range of kernel versions across distributions and Android OEM builds.
- **Citrix NetScaler ADC and NetScaler Gateway**: Versions vulnerable to CVE-2025-5777 (Citrix Bleed 2). Appliances exposed to the internet for remote access or load balancing are primary targets.
- **Cisco Unified Communications Manager**: Versions prior to the June 2026 security patch. Enterprise voice/video infrastructure deployments.
- **FatFs Filesystem Library (embedded devices)**: Millions of IoT devices, industrial controllers, automotive systems, medical devices, and consumer electronics integrating FatFs for FAT/exFAT storage support. Specific versions affected not enumerated in source.
- **Nextcloud Instances**: Self-hosted and managed Nextcloud deployments targeted by FortiBleed actors via an undisclosed zero-day.
- **Microsoft 365 Tenants**: Organizations targeted by ConsentFix/ClickFix OAuth token theft attacks and EvilTokens/ARToken PhaaS phishing campaigns.
- **Google Workspace / Gmail Accounts**: Targeted by ToddyCat's Umbrij malware abusing OAuth flows via Google API.
- **Android Devices (smartphones, smart TVs, streaming boxes)**: Two million devices compromised into the NetNut residential proxy botnet; additional devices targeted by malicious packages and Pegasus.
- **macOS Systems**: Targeted by PamStealer info-stealer distributed via fake Maccy clipboard manager websites.
- **npm, Packagist, Go Module Proxy, Chrome Web Store**: Software supply chain ecosystems polluted with 108 malicious packages/extensions in the PolinRider campaign.
- **Fortinet FortiGate Firewalls**: Devices compromised via FortiBleed vulnerabilities (specific CVEs not cited in source), providing persistent access to threat actors.

## Attack Vectors and Techniques

- **Local Privilege Escalation via Kernel Exploit**: Bad Epoll (CVE-2026-46242) leverages a use-after-free in the epoll subsystem. Attackers with local user access trigger the flaw via crafted epoll_ctl sequences to achieve root.
- **Unauthenticated Session Hijacking**: Citrix Bleed 2 (CVE-2025-5777) allows attackers to extract valid session tokens from NetScaler appliances without credentials, enabling immediate authenticated access.
- **Supply Chain Poisoning**: North Korean actors (Contagious Interview/PolinRider) publish malicious packages mimicking legitimate libraries (Rollup polyfills, etc.) across npm, Packagist, Go, and Chrome Web Store. Developers installing these packages execute attacker code in build/runtime environments.
- **Phishing-as-a-Service (PhaaS) Token Theft**: EvilTokens and ARToken platforms provide ready-made phishing kits (ConsentFix, ClickFix) that steal Microsoft 365 OAuth tokens in seconds via fake consent prompts, bypassing MFA.
- **OAuth Abuse for Email Access**: ToddyCat's Umbrij malware obtains OAuth tokens to access Gmail via Google APIs, enabling surreptitious email monitoring and data exfiltration without triggering traditional malware detection.
- **Bring Your Own Vulnerable Driver (BYOVD)**: Ransomware groups (including Anubis) load known vulnerable kernel drivers to disable security tools and escalate privileges in post-exploitation phases.
- **Residential Proxy Botnet Enrollment**: NetNut/Popa botnet compromised Android devices (including smart TVs/streaming boxes) via malicious apps/firmware, enrolling them as exit nodes for rented proxy traffic used in credential stuffing, scraping, and fraud.
- **Zero-Click Mobile Exploitation**: Pegasus spyware leverages zero-day vulnerabilities in iOS/Android to achieve full device compromise without user interaction, targeting high-profile individuals.
- **Multi-Stage Phishing Chains**: Avalon malware framework uses multi-stage phishing to bypass traditional email/security gateway defenses, delivering CrownX ransomware payloads.
- **Fake Legitimate Software Sites**: PamStealer distributes via typosquatted/fake websites impersonating the Maccy clipboard manager, employing PAM (Pluggable Authentication Module) checks to steal macOS login passwords.
- **AI-Automated Attack Chains**: JadePuffer ransomware operation documented as the first fully LLM-agent-driven attack, automating reconnaissance, exploitation, lateral movement, and encryption without human operators.
- **Data-Theft Extortion**: Kairos group exfiltrates sensitive data and demands payment to prevent leakage; successfully extracted $1M from a U.S. government entity.
- **Credential Theft via Supply Chain**: Malicious npm packages target developer environments to steal cloud credentials, SSH keys, and cryptocurrency wallets.

## Threat Actor Activities

- **North Korean Actors (Contagious Interview / PolinRider Campaign)**: Published 108 unique malicious packages and browser extensions across npm, Packagist, Go module proxy, and Chrome Web Store. Masqueraded as Rollup polyfill tooling to steal developer secrets. Attribution to DPRK-nexus threat groups.
- **JadePuffer Ransomware Operators**: Conducted the first documented fully AI-automated ransomware attack using an LLM agent to execute the entire kill chain—reconnaissance, vulnerability exploitation, lateral movement, data exfiltration, and encryption—without human intervention.
- **Kairos Extortion Group**: Executed data-theft extortion against a U.S. government entity, securing a $1M payment to prevent data leakage. Negotiation chat logs leaked, revealing operational details.
- **ToddyCat (Chinese APT)**: Deployed new Umbrij malware that abuses OAuth authorization flows to gain persistent, surreptitious access to victim Gmail accounts via Google APIs. Targets align with Chinese strategic intelligence priorities.
- **Armored Likho (New Threat Actor)**: Previously undocumented group targeting government agencies and the electric power sector across Russia, Brazil, and Kazakhstan using the BusySnake information stealer. Motivation and attribution under investigation.
- **Anubis Ransomware Operation**: Actively exploiting Citrix Bleed 2 (CVE-2025-5777) for initial access. Also employing BYOVD techniques and supply chain credential theft in intrusion campaigns.
- **FortiBleed Actors**: Maintain persistent access to thousands of compromised Fortinet FortiGate firewalls. Now monetizing access through collaboration with Inc Ransomware and Lynx Ransomware gangs. Also exploiting a Nextcloud zero-day.
- **Inc Ransomware Gang**: Partnering with FortiBleed actors to leverage compromised Fortinet appliances for ransomware deployment.
- **Lynx Ransomware Gang**: Collaborating with FortiBleed actors and Inc Ransomware in joint monetization of firewall access.
- **EvilTokens / ARToken PhaaS Operators**: Operate a mature Phishing-as-a-Service ecosystem providing Microsoft 365 token theft toolkits (ConsentFix, ClickFix) to affiliates. ARToken functions as an EvilTokens affiliate, expanding distribution.
- **NetNut / Popa Botnet Operators**: Ran a residential proxy service spanning two million compromised Android devices (smartphones, smart TVs, streaming boxes). Infrastructure seized/disrupted by joint FBI-Google-Lumen operation.
- **NSO Group (Pegasus Spyware)**: Provided Pegasus zero-click exploit capability used to repeatedly hack European Parliament Member Stelios Kouloglou during spyware investigations. State-aligned clientele.
- **PamStealer Operators**: Distribute macOS information stealer via fake Maccy clipboard manager websites, using PAM authentication prompts to harvest login credentials.

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
