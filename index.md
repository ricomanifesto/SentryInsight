# Exploitation Report

## Executive Summary

Russian state-sponsored threat actors are actively exploiting a zero-day vulnerability in Zimbra Collaboration email servers, conducting targeted espionage against organizations in the United States and Ukraine. The group tracked as Laundry Bear (also known as Void Blizzard) employs a "half-click" or zero-click technique where victims need only open or preview a malicious email to trigger compromise, enabling theft of up to 90 days of email communications and two-factor authentication codes. CISA has issued warnings about this ongoing campaign.

Simultaneously, Check Point has disclosed and patched an actively exploited zero-day in its SmartConsole management interface that grants attackers full administrative access to Security Management and Multi-Domain Management systems. In the Linux ecosystem, a nine-year-old race condition in the XFS filesystem (CVE-2026-64600) has been disclosed and is exploitable on default RHEL installations, allowing unprivileged local users to gain persistent root access.

Beyond vulnerability exploitation, threat actors are rapidly evolving their tradecraft. The Chaos ransomware group deploys msaRAT to route command-and-control traffic through headless Chrome and Edge browsers, while China-nexus group JadeProx utilizes a new TriBack loader against government, healthcare, and education targets across Asia and Latin America. Malvertising campaigns on Bing distribute SectopRAT via fake Claude AI installers, and attackers weaponize compromised GitHub Actions runners as distributed infrastructure to brute-force cPanel and WHM servers.

## Active Exploitation Details

### Zimbra Collaboration Zero-Day
- **Description**: A zero-day vulnerability in Zimbra's webmail client that allows remote code execution or data exfiltration when a victim opens or previews a malicious email message. The flaw requires no user interaction beyond viewing the message in the web interface.
- **Impact**: Attackers gain access to the last 90 days of email communications, organizational data, and two-factor authentication codes, enabling persistent access to victim mailboxes and potential lateral movement.
- **Status**: Actively exploited in the wild by Russian state-sponsored actors. No patch information provided in source articles; CISA has issued warnings.
- **CVE ID**: Not provided in source articles

### Check Point SmartConsole Zero-Day
- **Description**: A critical zero-day vulnerability in the SmartConsole graphical user interface (GUI) admin panel used for managing Check Point Security Management and Multi-Domain Management (MDSM) products.
- **Impact**: Allows attackers to obtain full administrative access to the management infrastructure, potentially compromising the entire security policy estate and connected gateways.
- **Status**: Actively exploited in the wild. Check Point has released security updates to address this and multiple other vulnerabilities.
- **CVE ID**: Not provided in source articles

### RefluxFS Linux Kernel XFS Filesystem Race Condition (CVE-2026-64600)
- **Description**: A nine-year-old race condition vulnerability in the Linux kernel's XFS filesystem implementation that allows a local unprivileged user to overwrite root-owned protected files.
- **Impact**: Local privilege escalation to persistent root access on affected systems. The flaw is exploitable on default RHEL installations and likely other distributions using XFS with default configurations.
- **Status**: Publicly disclosed on July 22, 2026. Proof-of-concept exploitation demonstrated. Patches expected from kernel maintainers and distribution vendors.
- **CVE ID**: CVE-2026-64600

### Notepad++ Malicious Plugin Abuse (LunchPoke)
- **Description**: Attackers distribute archives containing the legitimate Notepad++ text editor bundled with a malicious utility named "LunchPoke" disguised as a plugin. When executed, the malicious component establishes persistence on the victim system.
- **Impact**: Stealthy malware installation and persistence on developer and administrator workstations, leveraging trust in the legitimate Notepad++ application.
- **Status**: Actively exploited in attacks uncovered by Ukraine's CERT. No patch required for Notepad++ itself; detection relies on identifying the malicious plugin component.
- **CVE ID**: Not provided in source articles

## Affected Systems and Products

- **Zimbra Collaboration Suite**: Email and collaboration servers deployed by organizations in the US, Ukraine, and potentially other regions. Specific versions not disclosed in source articles.
- **Check Point Security Management and Multi-Domain Management (MDSM)**: Management platforms running the SmartConsole GUI admin panel. All versions prior to the July 2026 security update.
- **Linux Systems with XFS Filesystem**: Default installations of Red Hat Enterprise Linux (RHEL) and potentially other distributions using XFS as the default or common filesystem. Kernel versions spanning approximately nine years.
- **Notepad++**: Windows text editor application. The legitimate application is not vulnerable but is used as a delivery vehicle for the malicious LunchPoke plugin.
- **cPanel and WebHost Manager (WHM) Servers**: Web hosting control panels targeted by brute-force attacks originating from compromised GitHub Actions runners.
- **Windows Systems with Chrome/Edge Browsers**: Targets of the msaRAT implant used by Chaos ransomware for C2 traffic routing through headless browser instances.
- **GitHub Actions Runners**: Compromised repository automation infrastructure repurposed as distributed attack platforms.

## Attack Vectors and Techniques

- **Zero-Click / Half-Click Email Exploitation**: Victims compromised by simply opening or previewing a malicious email in Zimbra's webmail interface. No clicks, attachments, or credential entry required.
- **Malvertising via Bing Search Ads**: Threat actors purchase advertisements on Bing that promote a fake Claude desktop application installer hosted on a legitimate-appearing subdomain of claude.ai, delivering SectopRAT.
- **Living-off-the-Land Browser C2 Routing**: The msaRAT implant (Chaos ransomware) spawns headless Chrome or Edge instances on the victim machine and routes command-and-control traffic through them, blending malicious traffic with legitimate browser processes.
- **GitHub Actions Runner Weaponization**: Attackers compromise GitHub repositories and their associated Actions runners, converting CI/CD infrastructure into a distributed botnet for targeting cPanel/WHM login portals.
- **Supply Chain / Trojanized Legitimate Software**: Distribution of legitimate Notepad++ bundles containing a malicious plugin (LunchPoke) that establishes persistence when the user runs the application.
- **AI-Powered Victim Profiling**: Dolphin X RAT incorporates an AI-driven scoring system that automatically ranks infected hosts by value, allowing operators to prioritize high-value targets for manual interaction.
- **TriBack Loader Deployment**: China-nexus group JadeProx uses a new custom loader (TriBack) for initial access and payload delivery against government, healthcare, and education sectors.
- **Local Privilege Escalation via Filesystem Race Condition**: Exploitation of CVE-2026-64600 by local users to overwrite root-owned files on XFS filesystems, achieving persistent root access.

## Threat Actor Activities

- **Laundry Bear / Void Blizzard**: Russian state-sponsored espionage group conducting targeted campaigns against US and Ukrainian organizations using the Zimbra zero-day. Operations focus on email exfiltration and 2FA code theft for persistent access.
- **Chaos Ransomware Group**: Deploys the msaRAT Rust-based implant for stealthy C2 communications via headless browsers. Operates as a ransomware affiliate or independent group with advanced evasion capabilities.
- **JadeProx**: China-nexus threat cluster tracked by Group-IB, targeting government, healthcare, and education organizations across Asia and Latin America using the new TriBack loader. Infrastructure exposed via a misconfigured Alibaba Cloud server.
- **Brazilian Banking Trojan Operators**: Portuguese-language cybercriminals actively targeting businesses in Portugal, leveraging shared language for social engineering and financial fraud.
- **Sandworm_Mode Operators**: Threat actor(s) developing malware that exploits trusted AI toolchains and workflows, making malicious activity nearly indistinguishable from legitimate AI-assisted operations.
- **Unknown Operators (GitHub Actions Campaign)**: Unattributed group compromising GitHub repositories to weaponize Actions runners as distributed brute-force infrastructure against cPanel/WHM servers.
- **SectopRAT Distributors**: Cybercriminals running malvertising campaigns on Bing to deliver SectopRAT via fake AI application installers.

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
