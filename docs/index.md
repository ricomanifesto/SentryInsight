# Exploitation Report

## Executive Summary

Russian state-sponsored threat actors are actively exploiting a zero-day vulnerability in Zimbra Collaboration email servers to conduct espionage against targets in the United States and Ukraine. The group tracked as Laundry Bear (also known as Void Blizzard) employs a "half-click" phishing technique that requires victims only to open or preview a malicious email, enabling theft of up to 90 days of email communications and two-factor authentication codes. CISA has issued warnings about this campaign, which combines phishing with a zero-click exploitation vector.

Multiple critical zero-day vulnerabilities are under active exploitation across diverse platforms. Check Point has patched an actively exploited SmartConsole zero-day that grants attackers full administrative access to security management infrastructure. A nine-year-old race condition in the Linux kernel's XFS filesystem (CVE-2026-64600) allows local privilege escalation to root on default RHEL installations. Meanwhile, the Chaos ransomware group has deployed a novel Rust-based backdoor called msaRAT that routes command-and-control traffic through headless Chrome and Edge browsers to evade detection.

Threat actors are rapidly adopting AI-enhanced tooling and supply chain compromise techniques. The Dolphin X remote access trojan incorporates AI-powered victim profiling to prioritize high-value targets, while malvertising campaigns on Bing distribute SectopRAT via fake Claude AI installers hosted on legitimate domains. China-nexus group JadeProx employs a new TriBack loader against government and healthcare sectors across Asia and Latin America, and attackers have weaponized compromised GitHub Actions runners as distributed infrastructure to brute-force cPanel and WHM servers. Brazilian banking trojans are spreading in Portugal leveraging shared language, and Sandworm-linked malware demonstrates "living off the AI toolchain" tactics.

## Active Exploitation Details

### Zimbra Collaboration Zero-Day
- **Description**: A previously unknown vulnerability in Zimbra's webmail client that enables zero-click and "half-click" exploitation. Attackers send phishing emails that require only message preview or opening to trigger the exploit, stealing email contents and authentication tokens.
- **Impact**: Full access to victim mailboxes including the last 90 days of email, organizational data, and two-factor authentication codes. Enables persistent espionage and lateral movement.
- **Status**: Actively exploited in the wild by Russian state-sponsored group Laundry Bear (Void Blizzard). CISA has issued warnings. No CVE ID disclosed in public reporting.
- **CVE ID**: Not disclosed in source articles

### Check Point SmartConsole Zero-Day
- **Description**: A critical vulnerability in Check Point's SmartConsole graphical user interface (GUI) admin panel for Security Management and Multi-Domain Management (MDSM) products.
- **Impact**: Allows attackers to gain full administrative access to Check Point security management infrastructure, potentially compromising entire network security policies and configurations.
- **Status**: Actively exploited in the wild. Check Point has released security updates addressing multiple vulnerabilities including this critical flaw.
- **CVE ID**: Not disclosed in source articles

### RefluXFS Linux Kernel Privilege Escalation (CVE-2026-64600)
- **Description**: A nine-year-old race condition vulnerability in the Linux kernel's XFS filesystem that allows unprivileged local users to overwrite root-owned files and gain persistent root access on default installations.
- **Impact**: Local privilege escalation to root on affected systems, including default Red Hat Enterprise Linux installations. Provides persistent, stealthy root access.
- **Status**: Publicly disclosed on July 22, 2026. Exploitation requires local access. No indication of active remote exploitation in the wild reported.
- **CVE ID**: CVE-2026-64600

### Notepad++ Plugin Supply Chain Attack (LunchPoke)
- **Description**: Attackers distribute archives containing legitimate Notepad++ applications bundled with a malicious utility called LunchPoke disguised as a plugin, establishing persistence on victim systems.
- **Impact**: Stealthy malware installation and persistence through trusted application supply chain. Victims receive legitimate Notepad++ functionality alongside malicious payload.
- **Status**: Actively exploited in the wild. Discovered by Ukraine's CERT.
- **CVE ID**: Not disclosed in source articles

### Fake Claude AI Malvertising Campaign (SectopRAT)
- **Description**: Malvertising on Bing search promotes a fake Claude desktop application installer hosted on a legitimate Claude.ai subdomain, delivering the SectopRAT remote access trojan.
- **Impact**: Full remote access capabilities including credential theft, screen capture, keystroke logging, and lateral movement. Abuses trust in legitimate AI service domains.
- **Status**: Active campaign observed in the wild.
- **CVE ID**: Not disclosed in source articles

### Dolphin X RAT with AI-Powered Victim Profiling
- **Description**: A remote access trojan featuring an AI-powered profiling system that scores and ranks infected users to help operators prioritize high-value targets for further exploitation.
- **Impact**: Automated victim triage at scale, enabling efficient resource allocation for follow-on attacks such as ransomware deployment or data exfiltration.
- **Status**: Newly identified malware family actively deployed.
- **CVE ID**: Not disclosed in source articles

### Chaos Ransomware msaRAT Browser-Based C2
- **Description**: The Chaos ransomware group deploys msaRAT, a Rust-based implant that routes command-and-control traffic through headless Chrome or Edge browser instances on the victim machine to blend with legitimate traffic.
- **Impact**: Evasion of network monitoring and firewall rules by masquerading C2 as legitimate browser traffic. Persistent access for ransomware deployment and data theft.
- **Status**: Actively used by Chaos ransomware group. Detailed by Cisco Talos.
- **CVE ID**: Not disclosed in source articles

### JadeProx TriBack Loader Campaign
- **Description**: China-nexus threat group JadeProx employs a new TriBack loader in attacks against government, healthcare, and education organizations across Asia and Latin America. Infrastructure exposed via misconfigured Alibaba Cloud server.
- **Impact**: Initial access and payload delivery for espionage operations against sensitive sectors. Modular loader enables flexible follow-on exploitation.
- **Status**: Active campaign identified through infrastructure exposure.
- **CVE ID**: Not disclosed in source articles

### Brazilian Banking Trojan Campaign in Portugal
- **Description**: Brazilian banking trojans actively targeting Portuguese businesses, leveraging shared Portuguese language to craft convincing social engineering lures.
- **Impact**: Financial theft, credential harvesting, and banking fraud against Portuguese enterprises.
- **Status**: Actively spreading in Portugal per Dark Reading reporting.
- **CVE ID**: Not disclosed in source articles

### GitHub Actions Runner Weaponization
- **Description**: Large-scale campaign compromising GitHub repositories to turn GitHub Actions runners into distributed attack infrastructure targeting cPanel and WebHost Manager (WHM) servers.
- **Impact**: Abuse of trusted CI/CD infrastructure for credential stuffing, brute-force, and vulnerability scanning against hosting control panels at scale.
- **Status**: Active campaign identified by researchers.
- **CVE ID**: Not disclosed in source articles

### Microsoft Passkey Implementation Flaws
- **Description**: Exploitable flaws in Microsoft's passkey implementation that could allow attackers to impersonate privileged users, demonstrating that legacy attack vectors remain viable against modern authentication.
- **Impact**: Authentication bypass and privilege escalation via passkey manipulation. Presented ahead of Black Hat USA.
- **Status**: Research disclosure; active exploitation status unclear.
- **CVE ID**: Not disclosed in source articles

### Sandworm_Mode AI Toolchain Exploitation
- **Description**: Malware that exploits trusted AI tools and workflows to make malicious activity virtually indistinguishable from normal operations, representing an emerging "living off the AI toolchain" technique.
- **Impact**: Stealthy execution and persistence by blending with legitimate AI-assisted development and operational workflows.
- **Status**: Early example identified; attributed to Sandworm-linked activity.
- **CVE ID**: Not disclosed in source articles

## Affected Systems and Products

- **Zimbra Collaboration Suite**: Email server deployments targeted via zero-day webmail vulnerability; versions affected not specified in public reporting
- **Check Point SmartConsole / Security Management / MDSM**: GUI admin panel for security management products; patched versions released by vendor
- **Linux Kernel XFS Filesystem**: Systems running XFS on kernel versions spanning approximately nine years; confirmed exploitable on default RHEL installations
- **Notepad++**: Windows text editor; malicious plugin bundles distributed via archive files
- **Claude.ai Domain Infrastructure**: Legitimate Anthropic subdomains abused to host fake installer payloads
- **Bing Search Advertising Platform**: Malvertising delivery vector for fake AI application installers
- **GitHub Actions Runners**: CI/CD compute infrastructure compromised and repurposed as attack nodes
- **cPanel & WebHost Manager (WHM)**: Web hosting control panels targeted by distributed brute-force from weaponized GitHub runners
- **Microsoft Passkey Implementation**: Windows/Entra ID passkey authentication flows with identified implementation weaknesses
- **Alibaba Cloud Infrastructure**: Misconfigured server exposed JadeProx operational infrastructure and TriBack loader artifacts

## Attack Vectors and Techniques

- **Zero-Click / Half-Click Email Exploitation**: Malicious emails execute payloads when previewed or opened in Zimbra webmail, requiring no user interaction beyond viewing the message
- **Phishing with Zero-Day Chaining**: Combining social engineering emails with browser/client zero-days for reliable initial access
- **Malvertising on Trusted Search Platforms**: Bing ads delivering fake AI application installers hosted on legitimate service domains (Claude.ai)
- **Software Supply Chain Compromise**: Legitimate Notepad++ archives trojanized with malicious plugins (LunchPoke) for persistence
- **AI-Powered Victim Profiling**: Dolphin X RAT uses machine learning to score infected hosts and prioritize high-value targets automatically
- **Browser-Based C2 Tunneling**: msaRAT routes command traffic through headless Chrome/Edge instances to masquerade as legitimate web traffic
- **CI/CD Infrastructure Weaponization**: Compromised GitHub Actions runners repurposed as distributed botnet for cPanel/WHM credential attacks
- **Modular Loader Deployment**: TriBack loader provides flexible payload delivery for JadeProx espionage operations
- **Language-Based Social Engineering**: Brazilian banking trojans adapted for Portuguese targets using shared linguistic and cultural context
- **Passkey Authentication Bypass**: Implementation flaws in FIDO2/WebAuthn flows enabling privilege escalation via authentication manipulation
- **AI Toolchain Living-off-the-Land**: Sandworm_Mode leverages legitimate AI development tools and workflows to camouflage malicious activity
- **Infrastructure Exposure via Cloud Misconfiguration**: Alibaba Cloud server misconfiguration revealed JadeProx operational details

## Threat Actor Activities

- **Laundry Bear / Void Blizzard (Russian State-Sponsored)**: Multi-month espionage campaign exploiting Zimbra zero-day against US and Ukrainian targets. Steals email archives and 2FA codes. Uses half-click phishing and zero-click exploitation. CISA-attributed activity.
- **Chaos Ransomware Group**: Deploys msaRAT Rust implant with innovative browser-based C2 routing. Operates ransomware campaigns with advanced evasion techniques. Infrastructure analyzed by Cisco Talos.
- **JadeProx (China-Nexus, Group-IB tracking)**: Espionage operations targeting government, healthcare, and education sectors across Asia and Latin America. Uses new TriBack loader. Infrastructure exposed via Alibaba Cloud misconfiguration.
- **Brazilian Banking Trojan Operators**: Financially motivated campaigns targeting Portuguese businesses leveraging Portuguese language for social engineering. Active spreading reported in Portugal.
- **Sandworm-Linked Actors (Sandworm_Mode)**: Pioneering "living off the AI toolchain" techniques, using trusted AI workflows to disguise malicious operations. Early-stage capability demonstration.
- **Unknown / Multiple Actors (GitHub Actions Campaign)**: Large-scale compromise of GitHub repositories to build distributed attack infrastructure targeting cPanel/WHM. Attribution not specified in reporting.
- **Unknown / Multiple Actors (SectopRAT Malvertising)**: Bing malvertising campaign delivering SectopRAT via fake Claude installers. Operator attribution not specified.
- **Upbound Group Intrusion Actors**: Breached fintech systems and leveraged stolen data to create $13 million in fraudulent Acima leases. Attribution not specified.
- **Origin Energy Breach Actors**: Unauthorized access and leak of customer PII from Australian energy provider. Attribution not specified.
- **South Korean Diplomatic Academy Breach Actors**: Ten-month compromise of National Diplomatic Academy online education system stealing diplomat PII. Attribution not specified.
- **Japanese Food/Logistics Ransomware Actors**: Ransomware attack disrupting frozen food supply chain affecting thousands of clients including KFC franchises. Attribution not specified.

## Source Attribution

- **Russian Hackers Exploit Zimbra Zero-Day Against US, Ukraine Targets**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/russian-hackers-zimbra-zero-day-us-ukraine-targets
- **New Dolphin X malware uses AI to rank high-value targets**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-dolphin-x-malware-uses-ai-to-rank-high-value-targets/
- **Australian energy provider Origin says data breach exposes client data**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/australian-energy-provider-origin-says-data-breach-exposes-client-data/
- **Fake Claude app promoted by Bing ads pushes SectopRAT malware**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/fake-claude-app-promoted-by-bing-ads-pushes-sectoprat-malware/
- **Russian Espionage Group Exploited Zimbra Zero-Day to Steal Mail and 2FA Codes**: The Hacker News - https://thehackernews.com/2026/07/russian-espionage-group-exploited.html
- **Russian hackers exploit Zimbra zero-click flaw for email theft**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/russian-hackers-exploit-zimbra-zero-click-flaw-for-email-theft/
- **Hackers abuse Notepad++ plugins to stealthily install malware**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hackers-abuse-notepad-plus-plus-plugins-to-stealthily-install-malware/
- **Microsoft 365 outage affects Teams, SharePoint and other services**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-365-outage-affects-teams-sharepoint-and-other-services/
- **ThreatsDay: Android Spyware, PLC Attacks, AI Image Prompt Injection + 12 More Stories**: The Hacker News - https://thehackernews.com/2026/07/threatsday-android-spyware-plc-attacks.html
- **FedRAMP Rev5 Is Ending: What the 20x Transition Really Requires**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/fedramp-rev5-is-ending-what-the-20x-transition-really-requires/
- **Claude Cowork Flaw Could Let AI Agent Escape Its VM and Access Mac Files**: The Hacker News - https://thehackernews.com/2026/07/claude-cowork-flaw-could-let-ai-agent.html
- **Chaos Ransomware Uses msaRAT to Route C2 Traffic Through Headless Chrome and Edge**: The Hacker News - https://thehackernews.com/2026/07/chaos-ransomware-uses-msarat-to-route.html
- **EU fines Google $1 billion for search, app store antitrust violations**: Bleeping Computer - https://www.bleepingcomputer.com/news/google/eu-fines-google-1-billion-for-digital-markets-act-breaches-in-search-and-play-store/
- **China-Nexus JadeProx Uses New TriBack Loader in Government and Healthcare Attacks**: The Hacker News - https://thehackernews.com/2026/07/china-nexus-jadeprox-uses-new-triback.html
- **How Synthetic Identity Fraud is Coming for Machine Identities**: The Hacker News - https://thehackernews.com/2026/07/how-synthetic-identity-fraud-is-coming.html
- **New RefluXFS Linux flaw lets attackers gain root privileges**: Bleeping Computer - https://www.bleepingcomputer.com/news/linux/new-refluxfs-linux-flaw-lets-attackers-gain-root-privileges/
- **Attackers Weaponize GitHub Actions Runners to Target cPanel and WHM Servers**: The Hacker News - https://thehackernews.com/2026/07/attackers-weaponize-github-actions.html
- **Agentic AI Challenges Progress in Confidential Computing**: Dark Reading - https://www.darkreading.com/endpoint-security/agentic-ai-challenges-progress-in-confidential-computing
- **Google Adds Selfie Video Recovery for Users Locked Out of Their Accounts**: The Hacker News - https://thehackernews.com/2026/07/google-adds-selfie-video-recovery-for.html
- **New msaRAT malware uses Chrome, Edge browsers to route C2 traffic**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-msarat-malware-uses-chrome-edge-browsers-to-route-c2-traffic/
- **Microsoft working to fix Exchange Online mailbox quarantine issue**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-working-to-fix-exchange-online-mailbox-quarantine-issue/
- **Check Point warns of SmartConsole zero-day exploited in attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/check-point-patches-smartconsole-zero-day-exploited-in-attacks/
- **Nine-Year-Old RefluXFS Linux Flaw Gives Local Users Root on Default RHEL Installs**: The Hacker News - https://thehackernews.com/2026/07/nine-year-old-refluxfs-linux-flaw-gives.html
- **Brazilian Banking Trojan Actively Spreading in Portugal**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/brazilian-banking-trojan-spreading-portugal
- **Check Point Patches Exploited SmartConsole Flaw Allowing Full Admin Access**: The Hacker News - https://thehackernews.com/2026/07/check-point-patches-exploited.html
- **Ransomware Attack Puts a Chill on Japanese Frozen-Food Chain**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/ransomware-attack-japanese-frozen-food-chain
- **Flaws in Passkey Implementation Show Old Attacks Still Work**: Dark Reading - https://www.darkreading.com/identity-access-management-security/flaws-passkeys-implementation-old-attacks-work
- **Upbound says hack caused $13 million in fraudulent Acima leases**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/upbound-says-hack-caused-13-million-in-fraudulent-acima-leases/
- **Attackers Are Learning to Live Off the AI Toolchain**: Dark Reading - https://www.darkreading.com/cyber-risk/attackers-live-off-ai-toolchain
- **South Korea discloses data breach impacting diplomats worldwide**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/south-korea-discloses-data-breach-impacting-diplomats-worldwide/
