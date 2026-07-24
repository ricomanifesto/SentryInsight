# Exploitation Report

## Executive Summary

Russian state-sponsored threat actors are actively exploiting a zero-day vulnerability in Zimbra Collaboration email servers to conduct espionage against organizations in the United States and Ukraine. The group tracked as Laundry Bear (also known as Void Blizzard) employs "half-click" phishing techniques that require victims to merely open or preview malicious emails, enabling theft of email content and two-factor authentication codes over extended periods. CISA has issued warnings about this ongoing campaign, which has persisted for months across Western targets.

Multiple critical vulnerabilities have been identified in widely deployed infrastructure software. A nine-year-old race condition in the Linux kernel's XFS filesystem (CVE-2026-64600) allows local privilege escalation to root on default RHEL installations, while an actively exploited zero-day in Check Point SmartConsole grants attackers full administrative access to security management consoles. Simultaneously, researchers have uncovered a sandbox escape vulnerability in Anthropic's Claude Cowork AI agent that could permit VM breakout and host file access on macOS systems.

Threat actors are increasingly weaponizing legitimate services and AI capabilities for malicious purposes. The Chaos ransomware group deploys msaRAT malware that routes command-and-control traffic through headless Chrome and Edge browsers to evade detection, while a new Dolphin X remote access trojan incorporates AI-powered victim profiling to prioritize high-value targets. Malvertising campaigns on Bing search distribute SectopRAT via fake Claude installers, and attackers have compromised GitHub Actions runners to build distributed infrastructure targeting cPanel and WHM servers. A China-nexus operation tracked as JadeProx employs a novel TriBack loader against government, healthcare, and education sectors across Asia and Latin America.

## Active Exploitation Details

### Zimbra Collaboration Zero-Day Vulnerability
- **Description**: A zero-click/half-click vulnerability in Zimbra's webmail client that allows attackers to steal email content and two-factor authentication codes when victims open or preview malicious emails. The flaw enables persistent access to mailboxes for extended periods.
- **Impact**: Attackers can read the last 90 days of email communications, exfiltrate 2FA codes, and maintain persistent access to victim mailboxes without requiring user interaction beyond opening or previewing a message.
- **Status**: Actively exploited in the wild by Russian state-sponsored group Laundry Bear (Void Blizzard). CISA has issued warnings. No patch information provided in source articles.

### Check Point SmartConsole Zero-Day
- **Description**: A critical zero-day flaw in Check Point's SmartConsole graphical user interface (GUI) admin panel affecting Security Management and Multi-Domain Management (MDSM) products.
- **Impact**: Allows attackers to gain full administrative access to Check Point security management consoles, potentially compromising entire network security infrastructures.
- **Status**: Actively exploited in attacks. Check Point has released security updates to address multiple vulnerabilities including this critical flaw.

### RefluXFS Linux Kernel XFS Filesystem Vulnerability (CVE-2026-64600)
- **Description**: A nine-year-old race condition vulnerability in the Linux kernel's XFS filesystem that allows local attackers to overwrite protected root-owned files and gain persistent root privileges on default RHEL installations.
- **Impact**: Unprivileged local users can escalate to root access, achieving complete system compromise on affected Linux systems running XFS filesystems.
- **Status**: Disclosed July 2026. Affects default RHEL installations with XFS. Patch availability not specified in source articles.
- **CVE ID**: CVE-2026-64600

### Anthropic Claude Cowork Sandbox Escape
- **Description**: A sandbox escape vulnerability in Anthropic's Claude Cowork AI agent that allows breaking out of the Linux virtual machine confinement to access host Mac filesystem.
- **Impact**: AI agent can escape its VM sandbox and access sensitive files on the host macOS system, potentially exposing user data and system credentials.
- **Status**: Discovered by cybersecurity researchers. No patch information provided in source articles.

### Microsoft Passkey Implementation Flaws
- **Description**: Exploitable flaws in how Microsoft handles passkeys that could allow attackers to impersonate privileged users through implementation weaknesses.
- **Impact**: Attackers can bypass authentication controls and impersonate privileged users despite passkey protections, demonstrating that legacy attack vectors remain effective against new authentication technologies.
- **Status**: Identified by researchers ahead of Black Hat USA. No patch information provided in source articles.

## Affected Systems and Products

- **Zimbra Collaboration Email Servers**: Webmail client vulnerable to zero-click/half-click exploitation; targeted by Russian state-sponsored actors against US and Ukrainian organizations
- **Check Point Security Management and Multi-Domain Management (MDSM)**: SmartConsole GUI admin panel affected by actively exploited zero-day granting full admin access
- **Linux Kernel XFS Filesystem (CVE-2026-64600)**: Nine-year-old race condition affecting default RHEL installations with XFS; allows local privilege escalation to root
- **Anthropic Claude Cowork**: AI agent sandbox escape vulnerability allowing VM breakout and macOS host filesystem access
- **Microsoft Passkey Infrastructure**: Implementation flaws in passkey handling enabling privileged user impersonation
- **cPanel and WebHost Manager (WHM) Servers**: Targeted by large-scale campaign using compromised GitHub Actions runners as distributed attack infrastructure
- **Notepad++ with Malicious Plugins**: Legitimate application bundled with malicious "LunchPoke" utility disguised as plugin for persistence establishment

## Attack Vectors and Techniques

- **Half-Click/Zero-Click Phishing**: Russian actors send malicious emails that exploit Zimbra vulnerability when victims merely open or preview messages—no click required
- **AI-Powered Victim Profiling**: Dolphin X RAT uses AI to score and rank infected users, automatically identifying high-value targets for prioritized exploitation
- **Browser-Based C2 Obfuscation**: msaRAT malware (Chaos ransomware) routes command-and-control traffic through headless Chrome and Edge browsers to blend with legitimate traffic and evade detection
- **Malvertising via Legitimate Search Platforms**: Fake Claude desktop app installers promoted through Bing ads, hosted on legitimate Claude.ai domains to deliver SectopRAT
- **Supply Chain/Repository Compromise**: Attackers weaponize compromised GitHub repositories and GitHub Actions runners to create distributed attack infrastructure targeting hosting control panels
- **Legitimate Application Bundling**: Malicious archives containing genuine Notepad++ installer alongside malicious "LunchPoke" plugin disguised as legitimate functionality
- **Novel Loader Deployment**: China-nexus JadeProx operation uses new TriBack loader for initial access and persistence in government, healthcare, and education targets
- **AI Toolchain Living-Off-The-Land**: Sandworm_Mode malware exploits trusted AI tools and workflows to make malicious activity indistinguishable from normal operations
- **Race Condition Exploitation**: RefluxFS leverages nine-year-old XFS filesystem race condition for local privilege escalation through protected file overwrite

## Threat Actor Activities

- **Laundry Bear / Void Blizzard (Russian State-Sponsored)**: Conducting prolonged espionage campaign exploiting Zimbra zero-day against US and Ukrainian targets; steals email content and 2FA codes over months-long operations using half-click phishing
- **Chaos Ransomware Group**: Deploys msaRAT Rust-based implant for C2 communications routed through victim's own browsers; operates ransomware campaigns with novel browser-based traffic obfuscation
- **JadeProx (China-Nexus, tracked by Group-IB)**: Targets government, healthcare, and education organizations across Asia and Latin America using newly discovered TriBack loader; infrastructure revealed via exposed Alibaba Cloud server
- **Dolphin X Operators (Cybercriminal)**: Distributes AI-enhanced RAT with automated victim profiling and scoring to maximize criminal ROI through targeted follow-on exploitation
- **SectopRAT Distributors**: Runs malvertising campaigns on Bing search promoting fake Claude AI application installers hosted on legitimate domains
- **GitHub Actions Abusers**: Large-scale campaign compromising GitHub repositories to weaponize Actions runners as distributed brute-force infrastructure against cPanel/WHM servers
- **Sandworm-Associated Actors**: Developing "Sandworm_Mode" malware that lives off AI toolchains, blending malicious activity with legitimate AI workflows for stealth
- **Brazilian Banking Trojan Operators**: Actively targeting Portuguese businesses leveraging shared language for social engineering and financial fraud
- **Origin Energy Breach Actors**: Unauthorized access and leak of customer PII from Australian energy provider systems
- **Upbound Group Attackers**: Leveraged stolen data to create $13 million in fraudulent Acima leases through identity theft and financial fraud
- **South Korean Diplomatic Academy Breach Actors**: Maintained ten-month persistent access to online education system, exfiltrating personal information of current and former Ministry of Foreign Affairs employees
- **Japanese Frozen-Food Chain Ransomware Actors**: Disrupted supply chain for major franchises including KFC through ransomware attack on food logistics firm

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
