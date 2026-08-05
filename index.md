# Exploitation Report

## Executive Summary

A significant surge in supply chain attacks targeting developer ecosystems has emerged, with multiple npm worms—ChainDrop and a Keyv-linked variant—compromising over 1,300 packages with billions of monthly downloads. These self-propagating threats plant persistent hooks in development environments including VS Code and Claude Code, enabling credential theft and lateral movement. Simultaneously, phishing-as-a-service platforms have evolved rapidly: Greatness PhaaS now incorporates device code phishing and adversary-in-the-middle techniques to bypass MFA and steal Microsoft 365 tokens, driving a reported 1,500% increase in device code phishing during 2026.

Critical infrastructure flaws are being actively exploited in the wild. CISA added an N-able N-central authentication bypass (CVE-2026-18577) to its Known Exploited Vulnerabilities catalog after confirmed customer compromises, granting attackers full administrator access to RMM servers. Russian threat actor Midnight Blizzard (APT29) is conducting a global campaign against hospitality Wi-Fi networks using custom malware to breach Microsoft 365 accounts, while INC Ransomware has become the dominant operator exploiting SonicWall SMA 1000 VPN vulnerabilities. New attack surfaces continue to appear, including Google Password Manager passkey synchronization flaws exploitable by local malware and a cPanel privilege escalation allowing database root access.

## Active Exploitation Details

### N-able N-central Authentication Bypass
- **Description**: An authentication bypass vulnerability in N-able N-central RMM software that allows unauthenticated attackers to gain administrator access to both hosted and on-premises N-central servers. The flaw enables complete control over the management platform used to monitor and manage client endpoints.
- **Impact**: Attackers achieve full administrative access to RMM servers, enabling deployment of malicious payloads to all managed endpoints, lateral movement across customer networks, and persistent access to managed service provider infrastructure.
- **Status**: Actively exploited in the wild. CISA added this vulnerability to the Known Exploited Vulnerabilities (KEV) catalog following confirmed customer compromises. N-able has released patches for affected versions.
- **CVE ID**: CVE-2026-18577

### SonicWall SMA 1000 Series VPN Vulnerabilities
- **Description**: Security flaws in SonicWall Secure Mobile Access (SMA) 1000 series VPN appliances that allow remote exploitation. The vulnerabilities affect the SSL-VPN functionality used for remote access.
- **Impact**: Successful exploitation provides attackers with network access to internal resources behind the VPN appliance, enabling lateral movement, data exfiltration, and ransomware deployment.
- **Status**: Actively exploited by INC Ransomware, which has emerged as the dominant threat actor leveraging these flaws. SonicWall has released patches; urgent application is recommended.
- **CVE ID**: Specific CVE IDs not provided in source articles.

### cPanel Database Root Privilege Escalation
- **Description**: A critical flaw in cPanel that allows an authenticated hosting customer to execute SQL commands in the database's root context, crossing the privilege boundary between a cPanel account and the server's administrative database user.
- **Impact**: Attackers can escalate from a standard hosting account to full database root privileges, potentially accessing all databases on the server, modifying website content, and achieving further system compromise.
- **Status**: cPanel has released a patch for this vulnerability. Exploitation requires valid hosting credentials.
- **CVE ID**: Specific CVE ID not provided in source articles.

### Google Password Manager Passkey Synchronization Abuse (Pass-ta-key Attacks)
- **Description**: Three distinct attack methods allowing malware running on an already-compromised Windows device to abuse Google Password Manager's synced passkeys. The attacks enable account takeover without user interaction—no fingerprint, PIN, or screen prompt appears.
- **Impact**: Malware can silently sign into victims' passkey-protected accounts (Google, Microsoft, GitHub, and other services supporting passkey sync), bypassing all user verification mechanisms and multi-factor authentication.
- **Status**: Actively exploitable on Windows devices where Google Password Manager sync is enabled. Google has been notified; mitigation guidance includes disabling passkey sync or using hardware security keys.
- **CVE ID**: Specific CVE IDs not provided in source articles.

### tl;dv AI Notetaker Firebase Misconfiguration
- **Description**: A Google Firebase misconfiguration in the tl;dv AI meeting tool that allows any authenticated user to query other users' meeting information and potentially join ongoing or scheduled video calls without authorization.
- **Impact**: Unauthorized access to sensitive government and corporate video conferences, meeting transcripts, participant lists, and confidential discussions. Attackers can silently eavesdrop on privileged conversations.
- **Status**: Active vulnerability with confirmed exposure of government and corporate calls. The misconfiguration allows enumeration and access to meeting data across the platform.
- **CVE ID**: Specific CVE ID not provided in source articles.

### Google ADK AI Workflow Privilege Escalation via GitHub Issues
- **Description**: A vulnerability in Google's Agent Development Kit (ADK) Python repository where a malicious public GitHub issue could manipulate a triage AI agent into triggering a privileged agent with elevated permissions.
- **Impact**: Attackers could exploit the AI agent's access to privileged operations through crafted GitHub issues, potentially leading to unauthorized actions in the development pipeline or connected systems.
- **Status**: Google deleted three vulnerable AI agent workflows from the ADK repository after disclosure by Pillar Security. The issue demonstrates risks in AI agent permission models.
- **CVE ID**: Specific CVE ID not provided in source articles.

## Affected Systems and Products

- **N-able N-central RMM**: Both hosted (cloud) and on-premises deployments affected by CVE-2026-18577 authentication bypass. All versions prior to patched releases.
- **SonicWall SMA 1000 Series**: Secure Mobile Access 1000 series VPN appliances (SMA 1000, 1040, 1080 models) running vulnerable firmware versions.
- **cPanel & WHM**: Web hosting control panel installations where customers have shell/database access. Affected versions prior to the security patch release.
- **Google Password Manager / Chrome Sync**: Windows devices with Google Password Manager passkey synchronization enabled. Affects passkeys synced across Chrome browsers and Android devices.
- **tl;dv (AI Meeting Notetaker)**: Web and desktop application users. Firebase backend misconfiguration exposes all user meeting data cross-account.
- **Google Agent Development Kit (ADK)**: Python repository AI workflows. Three specific workflows removed; other ADK implementations may share similar architectural risks.
- **npm Registry (Node Package Manager)**: Over 1,300 packages compromised by ChainDrop worm (2 billion monthly downloads); hundreds more by Keyv-linked worm. Affected packages span Keyv, Cacheable, and numerous transitive dependencies.
- **Open VSX Marketplace**: 77 malicious extensions impersonating legitimate developer tools, harvesting system and environment telemetry.
- **Xcode / GitHub Repositories**: macOS developers using Xcode projects from compromised GitHub repositories infected with XCSSET malware variant.
- **Alibaba Cloud Developer Tools**: Users of Alibaba developer tooling targeted by 18 malicious npm packages delivering cross-platform RAT.
- **Microsoft 365 / Entra ID**: Targeted by Greatness PhaaS device code phishing, adversary-in-the-middle attacks, and Midnight Blizzard hotel Wi-Fi campaign.
- **ScreenConnect / ConnectWise Control**: Abused as persistent remote access tool in multiple campaigns (Smoke#Screen, fake Adobe/Zoom updates).
- **Android Devices**: BTMOB RAT ecosystem targeting Android users through underground distribution channels; Fake Roblox Xeno launchers targeting younger users.
- **cPanel Shared Hosting Environments**: Multi-tenant servers where database privilege boundary crossing affects all hosted customers.

## Attack Vectors and Techniques

- **Device Code Phishing (OAuth Device Authorization Flow Abuse)**: Attackers initiate legitimate device code flows with Microsoft/Google, then social-engineer victims into entering the code on authentic login pages. Bypasses MFA because the victim authenticates directly to the identity provider. Greatness PhaaS now automates this at scale. **Vector**: Phishing emails, SMS, Teams messages with urgent lures (voicemail, document review, IT request).

- **Adversary-in-the-Middle (AiTM) Phishing**: Greatness PhaaS proxies authentication traffic between victim and Microsoft 365, capturing session cookies and MFA tokens in real time. **Vector**: Phishing links leading to proxy sites that mirror legitimate login pages.

- **ClickFix / "Fake Update" Social Engineering**: Victims are tricked into copying and pasting malicious PowerShell commands into Run dialog or terminal (Windows+R, Win+X). DOUBLECUP uses this to stage PNG payloads in browser cache. **Vector**: Fake Adobe/Zoom update pages, CAPTCHA verification pages, document viewing lures, business review requests.

- **Browser Cache Poisoning via PNG Steganography**: DOUBLECUP hides malicious code in PNG images cached by the victim's browser during ClickFix interaction. JavaScript then extracts and executes the payload from cache. **Vector**: Malicious PNGs served from attacker-controlled domains during ClickFix flow; affects Windows and macOS.

- **Supply Chain Compromise (npm Worms)**: ChainDrop and Keyv-linked worms self-propagate by modifying package.json dependencies and publishing new versions to npm. ChainDrop infected 1,300+ packages (2B monthly downloads); Keyv worm spread from keyv@6.0.0 across namespaces. **Vector**: `npm install` / `npm update` in CI/CD pipelines and developer machines; transitive dependency resolution.

- **IDE/Editor Extension Malware**: 77 Open VSX extensions and malicious VS Code hooks planted by npm worms exfiltrate environment data, credentials, and project metadata. XCSSET compromises Xcode projects to infect macOS developers. **Vector**: Extension marketplace installation; cloned/infected GitHub repositories opened in Xcode.

- **RMM Abuse for Persistent Access**: ScreenConnect deployed via phishing (Smoke#Screen, fake updates) and N-central compromise (CVE-2026-18577) provides attackers with legitimate remote administration tools that bypass EDR. **Vector**: Phishing-delivered ScreenConnect installers; direct RMM server compromise enabling mass agent deployment.

- **Hotel Wi-Fi / Network Infrastructure Compromise**: Midnight Blizzard (APT29) deploys custom malware on hospitality Wi-Fi networks to intercept traffic and breach Microsoft 365 accounts. **Vector**: Compromised hotel network equipment, rogue access points, or supply chain compromise of hospitality IT vendors.

- **Passkey Sync Abuse (Pass-ta-key)**: Local malware on Windows uses Google Password Manager's local RPC/Chrome extension interfaces to trigger passkey authentication silently, exporting credentials for synced accounts. **Vector**: Post-exploitation on already-compromised Windows endpoints with Chrome sync enabled.

- **Firebase/Backend Misconfiguration Exploitation**: tl;dv's overly permissive Firebase rules allow cross-account data access without authentication bypass. **Vector**: Authenticated API calls to Firebase endpoints enumerating meeting IDs and joining calls.

- **AI Agent Prompt Injection / Privilege Escalation**: Malicious GitHub issues crafted to manipulate AI triage agents into invoking privileged downstream agents in Google ADK. **Vector**: Public GitHub issue submission on repositories using vulnerable AI workflows.

- **Fake Software Installers (Trojanized Legitimate Tools)**: Fake Roblox Xeno script executors, fake Adobe/Zoom updaters, and trojanized Alibaba tool npm packages deliver RATs and infostealers. **Vector**: Search engine poisoning, GitHub repositories, npm registry, social media/Discord distribution.

- **Proxyjacking / Host Compromise for Residential Proxies**: Chinese actor using Deepseek AI agent compromised 1,200+ hosts to build residential proxy networks for further attacks. **Vector**: AI-automated vulnerability scanning and exploitation at scale.

## Threat Actor Activities

- **Midnight Blizzard (APT29 / Cozy Bear)**: Russian state-sponsored actor conducting global campaign targeting hospitality Wi-Fi networks with custom malware to breach Microsoft 365 accounts. Linked by Microsoft to hotel network compromises across multiple countries. High-value targeting of government, NGO, and corporate travelers.

- **INC Ransomware**: Emerged as dominant threat actor exploiting SonicWall SMA 1000 series VPN flaws. Conducting opportunistic and targeted ransomware operations leveraging unpatched VPN appliances for initial access. Rapid weaponization of disclosed vulnerabilities.

- **Greatness PhaaS Operators**: Commercial phishing-as-a-service platform continuously adding capabilities—device code phishing, AiTM, MFA bypass. Services sold to criminal affiliates targeting Microsoft 365 credentials at scale. Infrastructure supports high-volume credential harvesting and session token theft.

- **DOUBLECUP Operators (Russian LaaS)**: Loader-as-a-service operation using ClickFix and browser cache steganography to deliver CountLoader and DeviceManager RAT. Targets Windows and macOS. Commercial malware distribution model with rotating payloads and evasion techniques.

- **ExfilSquad**: Hacking group responsible for breach of UK Police National Legal Database (PNLD), leaking contact data of 100,000+ police officers and criminal justice professionals. Data published on leak sites; motivation appears to be notoriety and data exposure.

- **Chinese State-Sponsored Actor (Deepseek AI Campaign)**: Weaponized Deepseek AI agent to automate compromise of 1,200+ hosts for proxyjacking infrastructure. Demonstrates AI-augmented offensive operations at scale. Targeted a security firm during reconnaissance phase.

- **BTMOB RAT Ecosystem (Android)**: Fragmented underground marketplace of resellers, source-code vendors, and custom variant developers. Thousands of underground posts analyzed; operates as malware-as-a-service with modular capabilities for credential theft, SMS interception, and remote control.

- **ChainDrop / Keyv Worm Authors**: Unknown operators behind self-propagating npm supply chain worms. ChainDrop achieved massive scale (1,300+ packages, 2B downloads); Keyv worm demonstrated cross-namespace propagation via dependency confusion and maintainer credential theft.

- **XCSSET Malware Operators**: Targeting macOS developers through compromised Xcode projects on GitHub. New variant shows enhanced evasion and persistence. Likely financially motivated targeting of cryptocurrency wallets and developer credentials.

## Source Attribution

- **Phishing service spoofs RingCentral to steal Microsoft 365 accounts**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/phishing-service-spoofs-ringcentral-to-steal-microsoft-365-accounts/
- **New XCSSET variant targets macOS devs via compromised Xcode projects**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-xcsset-variant-targets-macos-devs-via-compromised-xcode-projects/
- **77 Open VSX extensions found harvesting developer info**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/77-open-vsx-extensions-found-harvesting-developer-info/
- **Smoke#Screen RMM Takeover Gambit Exposes Threat Actor Playbook**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/latest-rmm-fueled-phishing-attack-exposes-threat-actor-playbook
- **Greatness PhaaS Adds Device Code Phishing to Bypass MFA and Steal Tokens**: The Hacker News - https://thehackernews.com/2026/08/greatness-phaas-adds-device-code.html
- **Massive ChainDrop npm supply-chain attack infects hundreds of packages**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/massive-chaindrop-npm-supply-chain-attack-infects-hundreds-of-packages/
- **Varonis Agent IBAC keeps AI agents within their intended boundaries**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/varonis-agent-ibac-keeps-ai-agents-within-their-intended-boundaries/
- **Keyv-Linked npm Worm Poisons Hundreds of Packages, Plants Claude Code and VS Code Hooks**: The Hacker News - https://thehackernews.com/2026/08/keyv-linked-npm-worm-poisons-hundreds.html
- **Fake Adobe and Zoom Updates Install ScreenConnect for Persistent Remote Access**: The Hacker News - https://thehackernews.com/2026/08/fake-adobe-and-zoom-updates-install.html
- **AI Notetaker Lets Hackers Spy on Government, Corporate Video Calls**: Dark Reading - https://www.darkreading.com/application-security/ai-notetaker-spy-government-corporate-video-calls
- **When Vibe Hacking Turns AI into the Junior Hacker Every Adversary Always Wanted**: The Hacker News - https://thehackernews.com/2026/08/when-vibe-hacking-turns-ai-into-junior.html
- **Google Deletes 3 ADK AI Workflows After Malicious GitHub Issue Could Trigger Privileged Agent**: The Hacker News - https://thehackernews.com/2026/08/google-deletes-3-adk-ai-workflows-after.html
- **New cPanel Critical Flaw Could Let Hosting Customers Run SQL as Database Root**: The Hacker News - https://thehackernews.com/2026/08/new-cpanel-critical-flaw-could-let.html
- **DOUBLECUP Uses ClickFix and Cached PNGs to Deliver CountLoader and DeviceManager RAT**: The Hacker News - https://thehackernews.com/2026/08/doublecup-uses-clickfix-and-cached-pngs.html
- **CISA Adds Exploited N-able N-central Flaw to KEV After Customer Compromises**: The Hacker News - https://thehackernews.com/2026/08/cisa-adds-exploited-n-able-n-central.html
- **Device Code Phishing Up 1,500% in 2026; Vishing Doubles**: Dark Reading - https://www.darkreading.com/cybersecurity-analytics/device-code-phishing-vishing-doubles
- **Hotel Wi-Fi attacks use custom malware to breach Microsoft 365 accounts**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hotel-wi-fi-attacks-use-custom-malware-to-breach-microsoft-365-accounts/
- **New Pass-ta-key attacks let malware hijack Google-synced passkeys**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-pass-ta-key-attacks-let-malware-hijack-google-synced-passkeys/
- **Attackers Exploit N-able Patch Bypass Flaw on RMM Servers**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/attackers-exploit-n-able-patch-bypass-flaw
- **New Tool Traces AI Videos Back to Their Source**: Dark Reading - https://www.darkreading.com/cyber-risk/new-tool-advances-ai-generated-video-detection
- **Anthropic: Claude Attacks Result of Security Gaps, Not Model Issues**: Dark Reading - https://www.darkreading.com/cyber-risk/anthropic-ai-issues-result-security-gaps
- **New DOUBLECUP ClickFix service hides malware in browser cache images**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-doublecup-clickfix-service-hides-malware-in-browser-cache-images/
- **Fake Roblox Xeno script launcher pushes infostealer, RAT malware**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/fake-roblox-xeno-script-launcher-pushes-infostealer-rat-malware/
- **18 Malicious npm Packages Deliver Cross-Platform RAT to Alibaba Tool Users**: The Hacker News - https://thehackernews.com/2026/08/18-malicious-npm-packages-deliver-cross.html
- **N-able warns of N-central auth bypass flaw exploited in attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/n-able-warns-of-n-central-auth-bypass-flaw-exploited-in-attacks/
- **Google Password Manager Attacks Could Let Malware Hijack Passkey-Protected Accounts**: The Hacker News - https://thehackernews.com/2026/08/google-password-manager-attacks-could.html
- **INC Ransomware Emerges as Dominant Actor Exploiting SonicWall SMA 1000 Flaws**: The Hacker News - https://thehackernews.com/2026/08/inc-ransomware-emerges-as-dominant.html
- **Chinese Actor Weaponizes Deepseek AI Agent to Attack Security Firm**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/chinese-actor-deepseek-ai-agent-attack-security-firm
- **ExfilSquad hackers leak info of over 100,000 UK police officers, staff**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/exfilsquad-hackers-leak-info-of-over-100-000-uk-police-officers-staff/
- **Inside the Underground Business of the Android BTMOB RAT malware**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/inside-the-underground-business-of-btmob-rat/
