# Exploitation Report

## Executive Summary

Active exploitation activity spans multiple critical vectors this reporting period, with threat actors rapidly weaponizing newly disclosed vulnerabilities across enterprise software, infrastructure components, and emerging AI-driven attack surfaces. Chinese-aligned operators are conducting targeted campaigns against academic institutions and Indian financial sectors, while Iranian MOIS-affiliated groups deploy novel command-and-control frameworks against Israeli organizations. North Korean actors continue large-scale software supply chain poisoning through the PolinRider campaign. Critically, the first fully LLM-automated ransomware operation (JadePuffer) has been documented, marking a significant evolution in offensive AI capabilities.

Multiple high-severity vulnerabilities are under active exploitation or immediate probing. Adobe ColdFusion CVE-2026-48282 (maximum severity) is being exploited in the wild. Gitea Docker CVE-2026-20896 drew attacker attention within 13 days of disclosure. The "Bad Epoll" Linux kernel flaw (CVE-2026-46242) provides unprivileged root access on desktops, servers, and Android. BeyondTrust's remote access products contain critical authentication bypass flaws requiring immediate patching. A 16-year-old Linux KVM escape vulnerability (Januscape) affects virtualized environments on Intel and AMD x86 systems.

Threat actor diversification continues with financially motivated groups like Armored Likho (BusySnake) compromising critical infrastructure across Russia, Brazil, and Kazakhstan, and the Kairos extortion group extracting seven-figure payments from a U.S. government entity. Social engineering campaigns leverage Microsoft Teams voice calls (EtherRAT delivery) and multi-brand job interview phishing (Google credential harvesting). Novel data exfiltration techniques (TrojPix) demonstrate air-gap bypass via video cable emissions, while AI agent skill obfuscation (SkillCloak) evades static analysis.

## Active Exploitation Details

### Adobe ColdFusion Critical Vulnerability (CVE-2026-48282)
- **Description**: Maximum-severity vulnerability in Adobe ColdFusion actively exploited in attacks according to vulnerability intelligence company KEVIntel.
- **Impact**: Attackers can achieve remote code execution and full system compromise on affected ColdFusion servers.
- **Status**: Actively exploited in the wild. Adobe has released patches; immediate application is critical.
- **CVE ID**: CVE-2026-48282

### Gitea Docker Critical Flaw (CVE-2026-20896)
- **Description**: Critical security flaw in Gitea Docker images disclosed and patched recently. Threat actors began probing for exploitation within 13 days of disclosure according to Sysdig observations.
- **Impact**: Successful exploitation could allow unauthorized access to source code repositories, supply chain manipulation, and lateral movement within development environments.
- **Status**: Actively probed by threat actors. Patches available; Docker images must be updated immediately.
- **CVE ID**: CVE-2026-20896

### Linux Kernel "Bad Epoll" Privilege Escalation (CVE-2026-46242)
- **Description**: Newly disclosed Linux kernel flaw dubbed "Bad Epoll" allows an ordinary unprivileged user to gain full root control of the machine.
- **Impact**: Complete system compromise on affected Linux desktops, servers, and Android devices. Attackers can escalate from any user context to root without authentication.
- **Status**: Recently disclosed with proof-of-concept likely available. Patches expected in kernel updates; Android vendor patches required for mobile devices.
- **CVE ID**: CVE-2026-46242

### Linux KVM Hypervisor Escape (Januscape)
- **Description**: A 16-year-old use-after-free bug in Linux's KVM hypervisor that can be triggered from a guest virtual machine to corrupt the shadow-page state of the host kernel.
- **Impact**: Guest VM escape to host kernel on Intel and AMD x86 systems, enabling compromise of the hypervisor and all other guest VMs on the same host.
- **Status**: Tracked as CVE-2026-XXXXX (CVE number truncated in source). Long-standing vulnerability now publicly disclosed; kernel patches required.
- **CVE ID**: CVE-2026-XXXXX

### BeyondTrust Remote Support and PRA Authentication Bypass
- **Description**: Two critical security flaws in BeyondTrust Remote Support (RS) and Privileged Remote Access (PRA) software that allow attackers to bypass authentication mechanisms.
- **Impact**: Unauthenticated attackers can gain administrative access to remote support and privileged access management systems, potentially compromising entire enterprise environments.
- **Status**: BeyondTrust has released updates addressing both flaws. Immediate patching required for all RS and PRA deployments.
- **CVE ID**: CVE-2026-XXXXX

### Roundcube Webmail Vulnerabilities
- **Description**: Vulnerabilities in Roundcube webmail software exploited by suspected China-aligned threat actors targeting physics and engineering departments at U.S. and Canadian universities.
- **Impact**: Unauthorized access to email communications, credential harvesting, and potential lateral movement within academic networks.
- **Status**: Actively exploited in targeted campaign. Roundcube patches should be applied; network monitoring for suspicious webmail access recommended.

### Citrix NetScaler Memory Disclosure Flaw
- **Description**: Latest memory disclosure vulnerability in Citrix NetScaler products (ADC and Gateway) being actively targeted after researchers published a proof-of-concept exploit.
- **Impact**: Memory disclosure enabling information leakage, potential session hijacking, and credential theft from affected NetScaler appliances.
- **Status**: Actively exploited post-PoC publication. Citrix has released mitigations; immediate application recommended.

### Tenda Router Hidden Admin Backdoor
- **Description**: Undocumented authentication backdoor embedded in several firmware versions from Chinese manufacturer Tenda, enabling administrative access to device web interfaces.
- **Impact**: Full administrative control of affected routers, network traffic interception, DNS manipulation, and persistent foothold in network infrastructure.
- **Status**: CERT/CC warning issued. No vendor patch available; mitigation requires firmware replacement or device isolation.

### Langflow Vulnerability (JadePuffer Campaign)
- **Description**: Flaw in Langflow (AI agent workflow framework) exploited by the JadePuffer ransomware operation—the first documented fully LLM-driven ransomware attack.
- **Impact**: Data exfiltration from production database servers and encryption of other systems, all orchestrated autonomously by an LLM agent.
- **Status**: Actively exploited in novel AI-driven campaign. Langflow users should update immediately and audit AI agent permissions.

### Opera GX Browser Extension Auto-Install Flaw
- **Description**: Flaw in Opera GX gaming browser allowing malicious websites to silently install browser add-ons (mods) and use them to steal specific data from visited pages.
- **Impact**: Data theft from any page visited by the user, including credentials, session tokens, and sensitive personal information, without user interaction.
- **Status**: Actively exploitable. Opera has released patches; users should update browser immediately.

## Affected Systems and Products

- **Adobe ColdFusion**: All versions affected by CVE-2026-48282; maximum severity rating indicates critical risk for web application servers
- **Gitea Docker Images**: Containerized deployments of Gitea self-hosted Git service; CVE-2026-20896 affects recent versions prior to patch
- **Linux Kernel**: All Linux distributions running vulnerable kernel versions (desktops, servers, embedded); Android devices across multiple OEMs affected by CVE-2026-46242
- **Linux KVM Hypervisor**: Virtualization hosts running Linux KVM on Intel and AMD x86 processors; affects cloud providers, on-premises virtualization, and development environments
- **BeyondTrust Remote Support (RS)**: Enterprise remote support software deployments; versions prior to security update release
- **BeyondTrust Privileged Remote Access (PRA)**: Privileged access management solutions; versions prior to security update release
- **Roundcube Webmail**: Self-hosted webmail deployments at educational institutions and enterprises; specific versions targeted in academic campaign
- **Citrix NetScaler ADC and Gateway**: Application delivery controllers and secure access gateways; memory disclosure flaw affects current supported versions
- **Tenda Routers**: Multiple firmware versions across Tenda router product lines; embedded devices in home and small business networks
- **Langflow**: AI agent workflow framework deployments; production instances with database connectivity
- **Opera GX Browser**: Gaming-focused browser versions prior to security patch; Windows and macOS platforms

## Attack Vectors and Techniques

- **Vulnerability Exploitation (Public-Facing Applications)**: Rapid weaponization of CVEs (CVE-2026-48282, CVE-2026-20896, CVE-2026-46242) within days of disclosure or PoC publication
- **Virtual Machine Escape**: Guest-to-host kernel corruption via KVM use-after-free (Januscape) enabling hypervisor compromise
- **Authentication Bypass**: Unauthenticated administrative access to BeyondTrust RS/PRA and Tenda router web interfaces via embedded backdoors
- **Memory Disclosure**: Citrix NetScaler information leakage enabling session hijacking and credential theft
- **AI-Agent Orchestrated Attacks**: Fully autonomous ransomware operation (JadePuffer) using LLM to exploit Langflow, exfiltrate data, and encrypt systems
- **Software Supply Chain Compromise**: North Korean PolinRider campaign publishing 108 malicious packages across npm, Packagist, Go, and Chrome Web Store
- **Social Engineering via Collaboration Platforms**: Microsoft Teams voice calls impersonating IT support to deliver EtherRAT malware
- **Multi-Brand Phishing Campaigns**: Fake job interview lures impersonating 30+ major brands (Adobe, Netflix, Coca-Cola, OpenAI) targeting marketing professionals for Google credential theft
- **Trojanized Legitimate Utilities**: Fake Indian tax filing utility distributing DcRAT remote access trojan to taxpayers and finance teams
- **Air-Gap Data Exfiltration**: TrojPix technique manipulating video cable emissions to leak data from isolated systems
- **AI Agent Skill Obfuscation**: SkillCloak self-extracting packing technique evading static scanners for malicious AI coding agent add-ons
- **Modular C2 Frameworks**: Iranian Cavern (C2F) framework providing flexible command-and-control for Israeli targeting
- **Infostealer Deployment**: BusySnake malware targeting government and electrical power entities across multiple countries
- **Ransomware with Data-Theft Extortion**: Kairos group extracting $1M payment from U.S. government entity under threat of data leak

## Threat Actor Activities

- **China-Aligned Threat Activity Cluster (Academic Targeting)**: Exploiting Roundcube flaws against physics and engineering departments at U.S. and Canadian universities; likely intelligence collection on sensitive research
- **China-Nexus Threat Activity Cluster (Indian Financial Targeting)**: Deploying fake Indian tax filing utility to deliver DcRAT to taxpayers, tax professionals, and corporate finance teams; credential theft and financial espionage
- **Iranian MOIS-Affiliated Group**: Utilizing novel Cavern (C2F) modular command-and-control framework to target Israeli organizations; previously undocumented C2 infrastructure
- **Armored Likho (BusySnake Operators)**: Compromising government agencies and electrical power entities in Russia, Brazil, and Kazakhstan; critical infrastructure targeting with infostealer malware
- **North Korean Contagious Interview / PolinRider Campaign**: Publishing 108 malicious packages and browser extensions across npm, Packagist, Go, and Chrome Web Store; large-scale software supply chain poisoning
- **JadePuffer Operator (Agentic Threat Actor)**: First documented fully LLM-autonomous ransomware operation; exploited Langflow flaw for data theft and encryption without human intervention
- **Kairos Extortion Group**: Conducted data-theft extortion against U.S. government entity resulting in ~$1M payment; negotiation chat leaked via Ransom-ISAC case study
- **EtherRAT Operators**: Abusing Microsoft Teams voice calling functionality to impersonate corporate IT support and deliver remote access trojan
- **Multi-Brand Job Interview Phishing Actors**: Operating large-scale credential harvesting campaign impersonating 30+ major brands targeting marketing professionals' Google accounts

## Source Attribution

- **Microsoft to enable Windows settings backup by default for orgs**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-to-enable-windows-backup-for-organizations-by-default/
- **Suspected China-Aligned Hackers Exploit Roundcube Flaws Against Universities**: The Hacker News - https://thehackernews.com/2026/07/suspected-china-aligned-hackers-exploit.html
- **BeyondTrust warns of critical flaws in remote access software**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/beyondtrust-warns-of-critical-flaws-in-remote-access-software/
- **Microsoft testing new Cloud Rebuild Windows 11 recovery feature**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-testing-new-cloud-rebuild-windows-11-recovery-feature/
- **CERT/CC Warns of Hidden Admin Backdoor in Tenda Router Firmware**: The Hacker News - https://thehackernews.com/2026/07/certcc-warns-of-hidden-admin-backdoor.html
- **BeyondTrust Patches Critical Auth Bypass Flaws in Remote Support and PRA**: The Hacker News - https://thehackernews.com/2026/07/beyondtrust-patches-critical-auth.html
- **'BusySnake' Infostealer Slithers into Critical Infrastructure Networks**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/busysnake-infostealer-critical-infrastructure-networks
- **CitrixBleed-ing Again? NetScaler Vulnerability Under Attack**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/citrixbleed-ing-again-netscaler-vulnerability-under-attack
- **Phishing poses as big-brand job interview to steal Google accounts**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/phishing-poses-as-big-brand-job-interview-to-steal-google-accounts/
- **Fake IT support calls on Microsoft Teams push EtherRAT malware**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/fake-it-support-calls-on-microsoft-teams-push-etherrat-malware/
- **Iran-Linked Hackers Use New Cavern C2 Framework to Target Israeli Organizations**: The Hacker News - https://thehackernews.com/2026/07/iran-linked-hackers-use-new-cavern-c2.html
- **Vietnam arrests suspects behind HiAnime anime piracy service**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/vietnam-arrests-suspects-behind-hianime-anime-piracy-service/
- **16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel and AMD x86 Systems**: The Hacker News - https://thehackernews.com/2026/07/16-year-old-linux-kvm-flaw-lets-guest.html
- **JadePuffer: The First Complete LLM-Driven Ransomware Attack**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/jadepuffer-first-complete-llm-driven-ransomware-attack
- **Threat Actors Probe Gitea Docker Flaw CVE-2026-20896 13 Days After Disclosure**: The Hacker News - https://thehackernews.com/2026/07/threat-actors-probe-gitea-docker-flaw.html
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
