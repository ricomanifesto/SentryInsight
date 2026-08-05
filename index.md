# Exploitation Report

## Executive Summary

A significant surge in supply-chain attacks targeting developer ecosystems has emerged, with two major npm malware campaigns—ChainDrop and a Keyv-linked worm—compromising over 1,300 packages collectively and achieving billions of monthly downloads. These self-propagating threats inject malicious code into legitimate packages, plant persistent hooks in development environments (Claude Code, VS Code), and exfiltrate credentials, demonstrating the growing risk of poisoned open-source dependencies.

Simultaneously, phishing-as-a-service platforms are rapidly evolving to defeat modern authentication controls. The Greatness PhaaS has added device-code phishing and adversary-in-the-middle capabilities to bypass MFA and steal Microsoft 365 session tokens, while a parallel campaign leverages fake Adobe and Zoom updates to deploy ScreenConnect for persistent remote access. Device-code phishing has surged 1,500% in 2026, signaling a strategic shift toward techniques that leave minimal forensic evidence.

Russian threat actors remain highly active across multiple fronts. Midnight Blizzard (APT29) is exploiting hospitality Wi-Fi networks with custom malware to breach Microsoft 365 accounts globally. The DOUBLECUP loader-as-a-service employs novel ClickFix lures and cached PNG steganography to deliver CountLoader and DeviceManager RAT across Windows and macOS. Separately, N-able N-central authentication bypass (CVE-2026-18577) is under active exploitation against RMM servers, prompting CISA to add it to the Known Exploited Vulnerabilities catalog. INC Ransomware has become the dominant actor exploiting recently disclosed SonicWall SMA 1000 series VPN flaws.

## Active Exploitation Details

### N-able N-central Authentication Bypass (CVE-2026-18577)
- **Description**: An authentication bypass vulnerability in N-able N-central that allows attackers to gain administrator access to both hosted and on-premises N-central servers without valid credentials. The flaw crosses privilege boundaries within the RMM platform.
- **Impact**: Attackers achieve full administrative control over RMM servers, enabling them to deploy payloads, manage endpoints, and pivot across managed customer networks. This provides a powerful foothold for downstream supply-chain compromise.
- **Status**: Actively exploited in the wild. CISA has added this vulnerability to its Known Exploited Vulnerabilities (KEV) catalog following confirmed customer compromises. N-able has released patches for affected versions.
- **CVE ID**: CVE-2026-18577

### SonicWall SMA 1000 Series VPN Vulnerabilities
- **Description**: Recently disclosed security flaws in SonicWall Secure Mobile Access (SMA) 1000 series appliances that allow unauthenticated or authenticated attackers to compromise the VPN gateway.
- **Impact**: Successful exploitation provides network access to internal resources, enabling ransomware deployment, data exfiltration, and lateral movement. INC Ransomware has emerged as the dominant threat actor leveraging these flaws.
- **Status**: Actively exploited by INC Ransomware operation. SonicWall has released patches; organizations are urged to apply updates immediately and review VPN logs for signs of compromise.

### cPanel Critical Privilege Escalation Flaw
- **Description**: A vulnerability in cPanel that allows an authenticated hosting customer to execute SQL commands in the database's root context, crossing the privilege boundary between a customer account and the server's administrative database user.
- **Impact**: Attackers can read, modify, or delete any database on the shared hosting server, compromise other customers' data, and potentially escalate to full server compromise.
- **Status**: cPanel has patched the flaw. Hosting providers should apply updates and audit database access logs for anomalous root-context queries.

### Google Password Manager Passkey Hijacking (Pass-ta-key Attacks)
- **Description**: Three distinct attack techniques that allow malware running as an ordinary user on a compromised Windows device to abuse Google Password Manager's synced passkeys. The attacks bypass user verification (fingerprint, PIN, screen prompts) to silently authenticate to passkey-protected accounts.
- **Impact**: Malware can take over Google accounts, Microsoft accounts, and any other services using Google-synced passkeys without any user interaction or visible prompts, effectively defeating passkey-based MFA.
- **Status**: Actively exploitable on Windows devices with Google Password Manager configured. Google has been notified; mitigations require browser/OS-level changes to enforce user presence verification.

### tl;dv AI Meeting Tool Firebase Misconfiguration
- **Description**: A Google Firebase misconfiguration in the tl;dv AI notetaker application that allows any authenticated user to query other users' meeting information and potentially join active video calls without authorization.
- **Impact**: Attackers can spy on government and corporate video calls, access meeting transcripts, recordings, and metadata, and potentially inject themselves into sensitive meetings.
- **Status**: The misconfiguration was disclosed to the vendor. Organizations using tl;dv should audit meeting access logs and consider restricting the tool's permissions.

### Google ADK GitHub Issue Injection
- **Description**: A vulnerability in Google's Agent Development Kit (ADK) where a maliciously crafted public GitHub issue could manipulate a triage AI agent into triggering a privileged agent workflow, leading to unintended privileged actions.
- **Impact**: Attackers could abuse AI agent workflows to perform privileged operations within the ADK environment, potentially accessing sensitive data or executing unauthorized code.
- **Status**: Google deleted three affected AI agent workflows from the ADK Python repository following responsible disclosure by Pillar Security.

## Affected Systems and Products

- **N-able N-central**: Both hosted and on-premises RMM server versions prior to patched releases. Affected platforms include Windows and Linux server deployments managing endpoint fleets.
- **SonicWall SMA 1000 Series**: Secure Mobile Access 1000 series VPN appliances (firmware versions prior to security patches). Used for remote access across enterprise and government networks.
- **cPanel & WHM**: Web hosting control panel installations on Linux servers (CloudLinux, AlmaLinux, Ubuntu, etc.) running vulnerable versions before the privilege escalation patch.
- **Google Password Manager / Google Chrome / Android**: Windows devices with Google Password Manager enabled and passkeys synced via Google account. Affects Chrome browser and Android ecosystem passkey synchronization.
- **tl;dv (AI Meeting Notetaker)**: Web and desktop application users of the tl;dv AI meeting tool. Firebase backend misconfiguration exposed all users' meeting data cross-tenant.
- **Google Agent Development Kit (ADK)**: Python repository workflows using AI agent triage systems that process public GitHub issues. Three specific workflows removed.
- **npm Registry / Node.js Ecosystem**: Over 1,300 packages compromised by ChainDrop malware (2 billion monthly downloads) and hundreds more by Keyv-linked worm. Affected packages span Keyv, Cacheable, and numerous downstream dependencies across multiple organizations.
- **Open VSX Marketplace**: 77 malicious extensions impersonating legitimate developer tools, harvesting system and development environment telemetry.
- **Xcode / GitHub Repositories**: macOS developers using Xcode projects cloned from compromised GitHub repositories infected with XCSSET malware variant.
- **ScreenConnect (ConnectWise Control)**: Remote monitoring and management tool abused as a persistent backdoor in multiple campaigns (fake updates, Smoke#Screen).
- **Microsoft 365 / Entra ID**: Target of device-code phishing, adversary-in-the-middle (Greatness PhaaS), and Midnight Blizzard hospitality Wi-Fi campaigns.
- **Google Firebase / Google Cloud**: Backend infrastructure for tl;dv and potentially other AI applications with similar misconfigurations.
- **Android Devices**: BTMOB RAT malware ecosystem targeting Android users through underground markets and repackaged applications.
- **Roblox / Xeno Executor**: Windows users downloading fake Roblox script launchers (Xeno Executor) delivering infostealers and RATs.
- **Alibaba Developer Tools / npm**: Users of Alibaba Cloud developer tools targeted by 18 malicious npm packages delivering cross-platform RAT.
- **Hotel/Hospitality Wi-Fi Networks**: Global hospitality sector networks compromised by Midnight Blizzard (APT29) using custom malware to intercept and breach Microsoft 365 authentication.

## Attack Vectors and Techniques

- **Device Code Phishing**: Exploits the OAuth 2.0 device authorization grant flow. Attackers generate a legitimate device code from Microsoft/Google, send it to the victim via phishing lure, and capture the resulting tokens when the victim authenticates. Bypasses traditional MFA because the victim authenticates directly to the identity provider. Greatness PhaaS now automates this; observed 1,500% increase in 2026.
- **Adversary-in-the-Middle (AiTM) Phishing**: Proxy-based phishing kits (Greatness PhaaS) that sit between victim and legitimate login page, capturing credentials, session cookies, and MFA tokens in real time. Enables full session takeover.
- **ClickFix Social Engineering**: Attackers present fake error messages or verification prompts (e.g., "Verify you are human," "Copy this command to fix") that trick victims into executing malicious PowerShell/command-line payloads. DOUBLECUP uses this to stage PNG payloads in browser cache.
- **Cached PNG Steganography / Browser Cache Poisoning**: Malicious code embedded in PNG images cached by the victim's browser during a ClickFix interaction. JavaScript later extracts and executes the payload from the browser cache, evading network-based detection. Used by DOUBLECUP to deliver CountLoader and DeviceManager RAT.
- **Supply-Chain Compromise (npm)**: Self-propagating worms (ChainDrop, Keyv-linked) that inject malicious code into published packages. ChainDrop modifies `package.json` and entry points to execute on install; Keyv worm spreads via dependency chains and plants persistent hooks in Claude Code and VS Code configurations.
- **Typosquatting / Impersonation Extensions**: Malicious Open VSX extensions (77 identified) and npm packages (18 targeting Alibaba tools) that mimic legitimate tool names to trick developers into installing them. Harvest environment variables, system info, credentials, and SSH keys.
- **Compromised Development Artifacts**: XCSSET malware injected into Xcode projects on GitHub. Developers cloning and building these projects inadvertently execute malicious payloads on macOS, leading to data theft, browser hijacking, and persistence.
- **Fake Software Update Lures**: Social engineering campaigns distributing ScreenConnect via fake Adobe Acrobat/Reader updates, Zoom installer updates, and business document review lures. Multi-wave campaigns with rotating payloads and infrastructure.
- **RMM Abuse / Living-off-the-Land**: Exploitation of N-central (CVE-2026-18577) and ScreenConnect deployment for persistent remote access. Attackers leverage legitimate administrative tools to blend in with normal IT operations.
- **VPN Appliance Exploitation**: INC Ransomware leveraging SonicWall SMA 1000 flaws for initial access, followed by ransomware deployment and data extortion.
- **Privilege Escalation via Database Root Access**: cPanel flaw allowing authenticated users to execute arbitrary SQL as database root, bypassing tenant isolation in shared hosting.
- **Passkey Session Hijacking (Pass-ta-key)**: Malware on compromised Windows devices abuses Google Password Manager's IPC/automation interfaces to trigger passkey authentication silently, bypassing user presence checks (biometric, PIN, screen unlock).
- **Firebase Misconfiguration / Insecure Direct Object References (IDOR)**: tl;dv's Firebase rules allowed cross-user data access. Attackers enumerate meeting IDs and join/access calls without authentication bypass.
- **AI Agent Prompt Injection / Tool Manipulation**: Malicious GitHub issues crafted to manipulate AI triage agents (Google ADK) into invoking privileged workflows. Demonstrates risks of autonomous agents processing untrusted input.
- **Infostealer Distribution via Gaming Lures**: Fake Roblox script launchers (Xeno Executor) distributed via YouTube, Discord, and search results, delivering information stealers and RATs to young/gaming demographics.
- **Android RAT Ecosystem (BTMOB)**: Fragmented reseller market for Android remote access trojans with modular capabilities (SMS theft, call logs, location, keylogging, overlay attacks). Distributed via repackaged apps and underground forums.
- **Hospitality Wi-Fi Compromise / Evil Twin / Custom Malware**: Midnight Blizzard deploys custom malware on hotel Wi-Fi infrastructure to intercept and manipulate Microsoft 365 authentication traffic, enabling credential theft and token replay.

## Threat Actor Activities

- **Midnight Blizzard (APT29 / Cozy Bear)**: Russian state-sponsored actor conducting global campaign targeting hospitality sector Wi-Fi networks. Uses custom malware to breach Microsoft 365 accounts of travelers and employees. High-value targeting of government, diplomatic, and corporate victims.
- **INC Ransomware**: Emerged as dominant ransomware operation exploiting SonicWall SMA 1000 VPN flaws. Conducts rapid exploitation, data exfiltration, and encryption. Opportunistic scanning for vulnerable appliances globally.
- **DOUBLECUP Operators**: Russian loader-as-a-service (LaaS) group operating CountLoader and DeviceManager RAT delivery infrastructure. Innovates with ClickFix + browser cache PNG steganography. Targets Windows and macOS. Service offered to other cybercriminals.
- **Greatness PhaaS Operators**: Commercial phishing-as-a-service platform continuously adding capabilities: credential phishing → AiTM → device-code phishing. Sells kits to affiliates; targets Microsoft 365 credentials and session tokens at scale.
- **Smoke#Screen / ScreenConnect Campaign Operators**: Threat actor(s) running multi-wave social engineering campaigns (fake Adobe/Zoom updates, document lures) deploying ScreenConnect for persistent access. Rotating payloads and infrastructure; playbook exposed by researchers.
- **ChainDrop / Keyv Worm Author(s)**: Supply-chain attackers behind self-propagating npm worms. ChainDrop: 1,300+ packages, 2B monthly downloads. Keyv worm: originated in keyv@6.0.0, spread across Keyv/Cacheable namespaces, planted Claude Code/VS Code hooks. Likely credential theft and persistence goals.
- **XCSSET Developers**: Long-running macOS malware family (since 2020) now distributing via compromised Xcode projects on GitHub. Targets developers; capabilities include browser data theft, cryptocurrency wallet theft, and persistence.
- **ExfilSquad**: Hacktivist/cybercriminal group claiming breach of UK Police National Legal Database (PNLD). Leaked contact data of 100,000+ police officers and criminal justice professionals. Motivation appears political/ideological.
- **Chinese Actor (Deepseek AI User)**: Unidentified Chinese threat actor weaponizing Deepseek AI agent to scan and compromise 1,200+ hosts for proxyjacking (turning devices into proxy nodes for further attacks). Demonstrates AI-assisted offensive operations.
- **BTMOB Ecosystem Actors**: Fragmented network of resellers, source-code vendors, and custom-version builders operating Android RAT marketplace. Not a single group but a supply chain of malware-as-a-service participants.
- **Fake Xeno/Roblox Distributors**: Operators using gaming lures (YouTube, Discord, SEO poisoning) to deliver infostealers and RATs to Roblox players. Financially motivated; likely affiliate-based distribution.
- **Alibaba Tool Targeting Actor**: Unknown group publishing 18 malicious npm packages targeting Alibaba Cloud developer tool users with cross-platform RAT. Sophisticated, targeted supply-chain operation.

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
