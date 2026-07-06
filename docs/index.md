# Exploitation Report

## Executive Summary

Active exploitation of maximum-severity vulnerabilities has intensified across enterprise software and operating system kernels. Adobe ColdFusion instances are under active attack leveraging CVE-2026-48282, while a newly disclosed Linux kernel flaw tracked as CVE-2026-46242 ("Bad Epoll") enables unprivileged local users to achieve full root compromise on desktops, servers, and Android devices. Both vulnerabilities are confirmed exploited in the wild, demanding immediate patching.

Simultaneously, threat actor operations have diversified in both technique and targeting. North Korean actors linked to the Contagious Interview campaign have flooded open-source registries with 108 malicious packages spanning npm, Packagist, Go, and Chrome extensions under the PolinRider operation, while a suspected China-nexus cluster deploys DcRAT through a trojanized Indian tax filing utility. The JadePuffer ransomware operation marks a milestone as the first documented case of an end-to-end attack orchestrated entirely by an LLM agent. A U.S. government entity paid $1 million to the Kairos extortion group, and the Armored Likho actor targets government and energy infrastructure across Russia, Brazil, and Kazakhstan with the novel BusySnake stealer.

Infrastructure takedowns and supply-chain risks round out the threat landscape. A multi-party operation led by Google and the FBI disrupted the NetNut residential proxy network, severing connectivity for approximately two million compromised Android devices including smart TVs and streaming boxes. Seven unpatched vulnerabilities in the FatFs filesystem library affect millions of embedded devices handling FAT/exFAT storage. The FortiBleed threat actors, having established persistent access to thousands of Fortinet firewalls, are now monetizing that foothold through collaboration with the Inc and Lynx ransomware gangs while also exploiting a Nextcloud zero-day. Pegasus spyware continues to target high-profile political figures, as confirmed by Citizen Lab's finding of repeated infections against a former European Parliament member investigating spyware abuses.

## Active Exploitation Details

### Adobe ColdFusion CVE-2026-48282
- **Description**: A maximum-severity vulnerability in Adobe ColdFusion that allows remote attackers to execute arbitrary code or achieve full system compromise. The flaw has been assigned the highest CVSS severity rating.
- **Impact**: Attackers can achieve complete control over affected ColdFusion servers, leading to data theft, lateral movement, ransomware deployment, and persistent access to enterprise environments.
- **Status**: Actively exploited in the wild as confirmed by vulnerability intelligence company KEVIntel. Adobe has released patches; immediate application is critical.
- **CVE ID**: CVE-2026-48282

### Linux Kernel "Bad Epoll" CVE-2026-46242
- **Description**: A Linux kernel vulnerability in the epoll subsystem that allows an unprivileged local user to escalate privileges to root. The flaw stems from improper handling of file descriptor references in the epoll mechanism.
- **Impact**: Any local user on an affected system can gain full root privileges, resulting in complete system compromise, container escape, and persistence establishment. The vulnerability affects Linux desktops, servers, and Android devices.
- **Status**: Publicly disclosed with exploit code available. Actively exploitable on unpatched kernels across distributions and Android versions.
- **CVE ID**: CVE-2026-46242

### Fortinet FortiBleed Firewall Exploitation
- **Description**: Threat actors tracked as FortiBleed have compromised thousands of Fortinet firewall appliances, establishing persistent footholds in victim networks. The initial access vector leverages vulnerabilities in FortiOS/FortiProxy SSL-VPN components.
- **Impact**: Full network perimeter compromise enabling traffic interception, credential harvesting, lateral movement, and deployment of follow-on payloads including ransomware.
- **Status**: Ongoing campaign. FortiBleed actors are now monetizing access through collaboration with Inc Ransomware and Lynx Ransomware gangs. Actors are also exploiting a Nextcloud zero-day vulnerability to expand compromise.
- **CVE ID**: CVE-2026-46242

### Opera GX Browser Extension Auto-Install Flaw
- **Description**: A vulnerability in Opera GX (gaming-focused Opera browser variant) that allows malicious websites to silently install browser add-ons (mods) without user interaction or consent prompts.
- **Impact**: Installed malicious mods can extract specific data from any web page the victim visits, including credentials, session tokens, PII, and corporate data. The attack is invisible to the user.
- **Status**: Vulnerability disclosed by researchers. Patch status should be verified with Opera; users should update immediately.

### Nextcloud Zero-Day Exploitation
- **Description**: An undisclosed zero-day vulnerability in Nextcloud collaboration platform being actively exploited by FortiBleed actors as a secondary expansion vector after initial firewall compromise.
- **Impact**: Compromise of file sharing and collaboration instances, leading to data exfiltration, malware hosting, and further lateral movement within organizational networks.
- **Status**: Actively exploited in conjunction with FortiBleed firewall access. No patch available at time of reporting; mitigations should be applied.

### FatFs Filesystem Library Vulnerabilities (7 Flaws)
- **Description**: Seven vulnerabilities disclosed by runZero in FatFs, a lightweight filesystem library implementing FAT/exFAT support for embedded devices. The library is bundled into millions of devices including USB drives, SD cards, IoT sensors, industrial controllers, and automotive systems.
- **Impact**: Vulnerabilities range from denial of service to potential code execution when processing malformed filesystem structures. Given the ubiquity of FatFs in embedded firmware, the attack surface is vast and largely unpatchable in deployed devices.
- **Status**: Unpatched as of disclosure. Vendors of affected embedded devices must incorporate fixes into firmware updates; many devices will never receive patches.

### Pegasus Spyware Deployment
- **Description**: NSO Group's Pegasus spyware deployed against high-value political targets via zero-click or one-click exploits targeting mobile operating systems (iOS and Android).
- **Impact**: Full device compromise including message interception, call recording, location tracking, camera/microphone activation, and credential theft. Persistent surveillance capability.
- **Status**: Confirmed by Citizen Lab investigation targeting former European Parliament member Stelios Kouloglou during his tenure investigating spyware abuses. Repeated infections observed.

## Affected Systems and Products

- **Adobe ColdFusion**: All versions prior to the patched releases addressing CVE-2026-48282. Enterprise application servers running ColdFusion web applications.
- **Linux Kernel**: All kernel versions containing the vulnerable epoll implementation prior to patched releases for CVE-2026-46242. Affected platforms include Linux desktop distributions, server installations, container hosts, and Android devices across multiple versions.
- **Opera GX Browser**: Gaming-focused Opera browser versions prior to the security fix. Windows, macOS, and Linux installations.
- **FatFs Filesystem Library**: Embedded devices incorporating FatFs for FAT/exFAT filesystem support. Affected device categories include USB mass storage devices, SD card controllers, IoT sensors, industrial control systems, automotive infotainment, medical devices, and consumer electronics. Millions of deployed units across vendors.
- **Fortinet FortiGate/FortiProxy**: Firewall and secure access appliances running vulnerable FortiOS versions. SSL-VPN endpoints exposed to internet.
- **Nextcloud**: Self-hosted and managed Nextcloud collaboration platform instances. All versions potentially affected pending zero-day disclosure.
- **Android Devices**: Smartphones, smart TVs, streaming boxes, and other Android-powered devices compromised into the NetNut residential proxy botnet (approximately 2 million devices).
- **iOS/macOS Devices**: Targets of Pegasus spyware deployment. Specific versions depend on exploit chain used.
- **Windows, Linux, macOS**: Platforms targeted by QuimaRAT cross-platform Java-based RAT (Malware-as-a-Service).
- **npm, Packagist, Go Module Proxy, Chrome Web Store**: Supply chain registries hosting 108 malicious packages published by North Korean actors in the PolinRider campaign.

## Attack Vectors and Techniques

- **Local Privilege Escalation via Kernel epoll Flaw**: **Technique Name**: Bad Epoll (CVE-2026-46242) — **Vector**: Local authenticated access; unprivileged user triggers race condition / reference count error in epoll subsystem to corrupt kernel memory and execute code as root.
- **Remote Code Execution via ColdFusion Deserialization/Injection**: **Technique Name**: CVE-2026-48282 exploitation — **Vector**: Unauthenticated or authenticated HTTP requests to vulnerable ColdFusion endpoints; likely involves deserialization, template injection, or access control bypass leading to arbitrary code execution.
- **Browser Extension Silent Installation**: **Technique Name**: Opera GX mods auto-install — **Vector**: Victim visits attacker-controlled website; malicious script leverages browser flaw to install extension/mod without user prompts; extension then reads cross-origin page data.
- **Trojanized Legitimate Utility (Supply Chain / Social Engineering)**: **Technique Name**: Fake Indian tax filing utility — **Vector**: Attackers distribute trojanized tax preparation software mimicking legitimate government utility; victims download and execute, deploying DcRAT remote access trojan.
- **Malicious Open-Source Package Publication (Supply Chain)**: **Technique Name**: PolinRider campaign package planting — **Vector**: Threat actors publish 108 typosquatted or brand-jacked packages across npm, Packagist (PHP), Go module proxy, and Chrome Web Store; developers install packages believing them legitimate, executing embedded malware.
- **Air-Gapped Data Exfiltration via Video Emissions**: **Technique Name**: TrojPix — **Vector**: Malware on air-gapped system modulates pixel values on display output; emissions from video cable (HDMI/VGA/DisplayPort) carry encoded data receivable by nearby SDR or antenna-equipped receiver.
- **AI Agent Skill Obfuscation via Self-Extracting Packing**: **Technique Name**: SkillCloak — **Vector**: Malicious AI agent skills (plugins) packed with self-extracting stubs that evade static analysis scanners; payload extracts and executes at runtime within AI coding agent environment.
- **Cross-Platform Java RAT Deployment (MaaS)**: **Technique Name**: QuimaRAT — **Vector**: Java-based remote access trojan delivered via phishing, drive-by download, or secondary payload; runs on Windows, Linux, macOS with consistent capability set; offered as Malware-as-a-Service.
- **macOS Credential Theft via PAM Abuse and Typosquatting**: **Technique Name**: PamStealer — **Vector**: Victims lured to fake Maccy (clipboard manager) download sites; installer executes PAM (Pluggable Authentication Module) checks to harvest login passwords; exfiltration via C2.
- **Multi-Stage Phishing to Modular Malware Framework**: **Technique Name**: Avalon / CrownX deployment — **Vector**: Phishing emails deliver staged payloads; initial dropper evades traditional defenses; modular framework Avalon loads CrownX ransomware module for encryption and extortion.
- **Residential Proxy Botnet Enrollment**: **Technique Name**: NetNut / Popa botnet — **Vector**: Android devices (phones, smart TVs, streaming boxes) compromised via malicious apps or firmware supply chain; enrolled into residential proxy network selling bandwidth to threat actors for anonymization.
- **Phishing-as-a-Service (PhaaS) Microsoft 365 Credential Harvesting**: **Technique Name**: ARToken / EvilTokens toolkit — **Vector**: Affiliate PhaaS platform provides turnkey phishing infrastructure targeting Microsoft 365 credentials; includes proxy pages, MFA bypass, and credential management.
- **Zero-Click Mobile Exploit Chain (Pegasus)**: **Technique Name**: Pegasus spyware deployment — **Vector**: Zero-click or one-click exploits targeting iOS Safari, iMessage, or Android Chrome/messaging apps; no user interaction required for zero-click variants; installs full-featured surveillance implant.

## Threat Actor Activities

- **FortiBleed Actors**: **Activities**: Initial access via Fortinet SSL-VPN vulnerabilities; persistent foothold in thousands of firewalls globally. **Campaign**: Monetizing access through partnership with Inc Ransomware and Lynx Ransomware gangs for ransomware deployment; leveraging Nextcloud zero-day for lateral expansion. Targeting enterprise networks across sectors.

- **North Korean Actors (Contagious Interview / PolinRider Cluster)**: **Activities**: Large-scale supply chain poisoning via malicious package publication; developer targeting for credential theft and environment compromise. **Campaign**: PolinRider — 108 unique malicious packages across npm, Packagist, Go, and Chrome Web Store mimicking legitimate libraries (including Rollup polyfills); additional npm packages targeting developers via typosquatting. Attribution to DPRK-linked threat groups.

- **Suspected China-Nexus Threat Cluster**: **Activities**: Social engineering via localized lure (Indian tax filing); deployment of DcRAT for persistent remote access and data theft. **Campaign**: Targeting Indian taxpayers, tax professionals, and corporate finance teams; trojanized utility distributed through phishing or fake download portals.

- **JadePuffer Ransomware Operators**: **Activities**: First documented fully AI-agent-orchestrated ransomware operation. **Campaign**: LLM agent autonomously executed reconnaissance, initial access, lateral movement, data exfiltration, encryption, and extortion negotiation without human operator intervention.

- **Kairos Ransomware / Extortion Group**: **Activities**: Data theft extortion with encryption; direct negotiation with victims. **Campaign**: Compromised U.S. government entity; exfiltrated sensitive files; collected $1 million ransom payment to prevent leak per leaked negotiation logs analyzed by Ransom-ISAC.

- **Armored Likho**: **Activities**: Previously undocumented threat actor deploying custom BusySnake information stealer. **Campaign**: Targeting government agencies and electric power sector organizations in Russia, Brazil, and Kazakhstan; focused on credential theft, system enumeration, and potential OT/ICS reconnaissance.

- **NetNut / Popa Botnet Operators**: **Activities**: Operation of massive residential proxy service built on compromised consumer Android devices. **Campaign**: Infected approximately 2 million devices (smartphones, smart TVs, streaming boxes); sold proxy access to cybercriminals for credential stuffing, ad fraud, scraping, and anonymized attack infrastructure. Disrupted by Google/FBI/Lumen joint operation.

- **EvilTokens / ARToken PhaaS Operators**: **Activities**: Development and operation of Phishing-as-a-Service platform targeting Microsoft 365. **Campaign**: ARToken operates as EvilTokens affiliate; provides comprehensive toolkit including reverse-proxy phishing pages, MFA interception, session token capture, and affiliate management dashboard.

- **Pegasus Spyware Operators (NSO Group customers)**: **Activities**: Targeted surveillance of high-profile political figures. **Campaign**: Repeated infection of former European Parliament member Stelios Kouloglou's mobile devices during his legislative work investigating spyware abuses; confirmed by Citizen Lab forensic analysis.

- **QuimaRAT MaaS Operators (LevelBlue-tracked)**: **Activities**: Development and sale of cross-platform Java RAT. **Campaign**: Offering QuimaRAT as subscription service; capability includes file management, command execution, keylogging, screen capture, and persistence across Windows, Linux, macOS.

## Source Attribution

- **Software Is Now Written at the Speed of Thought. Security Isn't.**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/software-is-now-written-at-the-speed-of-thought-security-isnt/
- **Max severity Adobe ColdFusion flaw now exploited in attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/max-severity-adobe-coldfusion-flaw-now-exploited-in-attacks/
- **⚡ Weekly Recap: Proxy Botnets, Browser Ransomware, AI Agent Tricks, Fake PoC Malware and More**: The Hacker News - https://thehackernews.com/2026/07/monday-recap-proxy-botnets-browser.html
- **How to Evaluate an AI SOC Platform in 2026: 6 Capabilities That Separate Leaders from Bolt-On AI solutions**: The Hacker News - https://thehackernews.com/2026/07/how-to-evaluate-ai-soc-platform-in-2026.html
- **Suspected China-Nexus Hackers Use Fake Indian Tax Filing Utility to Deploy DcRAT**: The Hacker News - https://thehackernews.com/2026/07/suspected-china-nexus-hackers-use-fake.html
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
