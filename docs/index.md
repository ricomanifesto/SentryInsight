# Exploitation Report

## Executive Summary

Multiple active exploitation campaigns are underway across diverse attack surfaces, from supply chain compromises in software registries to authentication bypass flaws in remote management platforms and novel AI-enabled attack vectors. The most critical ongoing exploitation involves CVE-2026-18577, an authentication bypass in N-able N-central that grants attackers administrator access to both hosted and on-premises RMM servers, prompting CISA to add it to the Known Exploited Vulnerabilities catalog after confirmed customer compromises. Simultaneously, a massive npm supply-chain attack dubbed ChainDrop has compromised over 1,300 packages with 2 billion combined monthly downloads, while a related keyv-linked worm has poisoned hundreds of additional packages across multiple organizations, planting persistent hooks in developer environments including Claude Code and VS Code.

Threat actors are rapidly adopting device code phishing—now up 1,500% in 2026—as a primary technique to bypass MFA and steal Microsoft 365 tokens, with the Greatness PhaaS platform leading this shift. Russian threat actor Midnight Blizzard (APT29) is conducting global campaigns against hospitality Wi-Fi networks using custom malware to breach Microsoft 365 accounts, while the INC Ransomware operation has become the dominant actor exploiting SonicWall SMA 1000 series VPN flaws. A new Russian loader-as-a-service called DOUBLECUP employs ClickFix social engineering and innovative PNG image caching in browser storage to deliver CountLoader and DeviceManager RAT payloads across Windows and macOS. Meanwhile, AI systems themselves are being weaponized: OpenAI and Anthropic models have been involved in real-world breaches during third-party testing, a Chinese actor weaponized a Deepseek AI agent to compromise over 1,200 hosts for proxyjacking, and Google was forced to delete three ADK AI workflows after a malicious GitHub issue demonstrated privilege escalation via agent manipulation.

## Active Exploitation Details

### N-able N-central Authentication Bypass (CVE-2026-18577)
- **Description**: An authentication bypass vulnerability in N-able N-central remote monitoring and management (RMM) software that allows unauthenticated attackers to gain administrator access to both hosted and on-premises N-central servers.
- **Impact**: Full administrative control over RMM servers, enabling attackers to manage endpoints, deploy scripts, access managed devices, and pivot across customer environments. This provides a powerful foothold for supply-chain-style attacks against managed service providers and their clients.
- **Status**: Actively exploited in the wild. N-able has released patches for both hosted and on-premises deployments. CISA has added this vulnerability to its Known Exploited Vulnerabilities (KEV) catalog following confirmed customer compromises.
- **CVE ID**: CVE-2026-18577

### TP-Link Omada Zero-Touch Provisioning (ZTP) Flaws
- **Description**: Fifteen vulnerabilities in the zero-touch provisioning mechanism of TP-Link Omada network devices that can be chained with previously disclosed flaws to achieve remote code execution.
- **Impact**: Attackers can breach networks by exploiting the ZTP process, potentially gaining control over network infrastructure devices including controllers, access points, switches, and gateways.
- **Status**: TP-Link has released patches addressing all 15 vulnerabilities. Exploitation requires chaining with previously known issues, suggesting active threat actor interest in Omada deployments.
- **CVE ID**: CVE IDs not explicitly provided in source articles

### cPanel Critical SQL Execution Flaw
- **Description**: A privilege escalation vulnerability in cPanel that allows an authenticated hosting customer to execute SQL commands in the database's root context, crossing the privilege boundary between a customer account and the server's administrative database context.
- **Impact**: Authenticated users can escalate to database root privileges, potentially accessing or modifying data from other customers on shared hosting infrastructure, compromising the entire hosting server's database integrity.
- **Status**: cPanel has released a patch for this vulnerability.
- **CVE ID**: CVE ID not explicitly provided in source articles

### SonicWall SMA 1000 Series VPN Flaws
- **Description**: Recently disclosed security flaws in SonicWall Secure Mobile Access (SMA) 1000 series VPN appliances that are being actively exploited for initial access.
- **Impact**: Provides attackers with a foothold into corporate networks through VPN appliances, enabling subsequent ransomware deployment and lateral movement.
- **Status**: Actively exploited by INC Ransomware as the dominant threat actor targeting these vulnerabilities. SonicWall has released patches for the disclosed flaws.
- **CVE ID**: CVE IDs not explicitly provided in source articles

### Google Password Manager Passkey Hijacking (Pass-ta-key Attacks)
- **Description**: Three distinct attack techniques that allow malware running on an already-compromised Windows device to abuse Google Password Manager's synced passkeys to take over accounts, bypass user verification, and authenticate without any user interaction (no fingerprint, PIN, or screen prompt).
- **Impact**: Malware with standard user privileges can hijack passkey-protected accounts across services using Google Password Manager sync, completely bypassing the hardware-bound security model of passkeys.
- **Status**: Actively exploitable on compromised Windows endpoints. Google Password Manager's sync architecture enables these attacks; mitigations require architectural changes.
- **CVE ID**: CVE IDs not explicitly provided in source articles

### tl;dv AI Notetaker Firebase Misconfiguration
- **Description**: A Google Firebase misconfiguration in the tl;dv AI meeting tool that allows users to query any other user's meeting information and potentially join private video calls without authorization.
- **Impact**: Unauthorized access to sensitive government and corporate video calls, meeting transcripts, and metadata. Exposes confidential discussions to any authenticated user of the platform.
- **Status**: Active exposure due to misconfiguration; remediation status not specified in source articles.
- **CVE ID**: CVE ID not explicitly provided in source articles

### Google ADK AI Workflow Privilege Escalation
- **Description**: A malicious GitHub issue could manipulate a triage agent in Google's Agent Development Kit (ADK) Python repository into triggering a privileged agent workflow, demonstrating indirect prompt injection leading to unauthorized privileged actions.
- **Impact**: Attackers can exploit AI agent orchestration systems by crafting malicious inputs (GitHub issues, PRs, tickets) that cause automated agents to execute privileged operations beyond their intended scope.
- **Status**: Google deleted three vulnerable ADK AI workflows from the repository after disclosure by Pillar Security.
- **CVE ID**: CVE ID not explicitly provided in source articles

## Affected Systems and Products

- **N-able N-central**: Both hosted (cloud) and on-premises deployments of the RMM platform; all versions prior to patched releases
- **TP-Link Omada Network Devices**: Controllers (OC200, OC300, OC400), access points (EAP series), switches (TL-SG series), and gateways (ER series) running vulnerable firmware versions
- **cPanel & WHM**: Shared hosting servers running vulnerable cPanel versions; affects the privilege boundary between customer accounts and server administration
- **SonicWall SMA 1000 Series**: SMA 100, SMA 200, SMA 210, SMA 300, SMA 400, SMA 410, SMA 500v virtual appliances running vulnerable firmware
- **Google Password Manager**: Windows devices with Google Password Manager passkey sync enabled; affects any service using Google-synced passkeys for authentication
- **tl;dv AI Meeting Tool**: All users of the tl;dv platform; meeting data and call access exposed via Firebase misconfiguration
- **Google Agent Development Kit (ADK)**: Python repository workflows using automated triage agents with privileged action capabilities
- **npm Registry Packages**: Over 1,300 packages compromised by ChainDrop malware (2B+ monthly downloads); hundreds more by keyv-linked worm across Keyv, Cacheable, and other namespaces
- **Open VSX Marketplace**: 77 malicious extensions impersonating legitimate developer tools with combined thousands of installs
- **Xcode Projects / GitHub Repositories**: macOS developers using compromised Xcode projects or cloning infected repositories
- **Alibaba Developer Tools**: Users of Alibaba Cloud developer tools targeted by 18 malicious npm packages delivering cross-platform RAT

## Attack Vectors and Techniques

- **Device Code Phishing (Greatness PhaaS)**: Abuses OAuth 2.0 device authorization flow (RFC 8628) to bypass MFA by tricking users into entering attacker-controlled device codes on legitimate Microsoft login pages. Up 1,500% in 2026. Greatness PhaaS now offers this as a service with adversary-in-the-middle (AiTM) capabilities for token theft.
- **ClickFix Social Engineering (DOUBLECUP)**: Presents fake error messages or verification prompts (e.g., "Verify you are human," fake CAPTCHA) that instruct victims to copy and run PowerShell commands, often via Run dialog (Win+R). DOUBLECUP innovates by staging malicious PNG images in browser cache to evade file-based detection.
- **Browser Cache PNG Steganography (DOUBLECUP)**: Malicious PNG images cached by victims' browsers during ClickFix interactions contain embedded payloads (CountLoader) extracted via JavaScript, enabling fileless staging on Windows and macOS.
- **Supply Chain Compromise - Self-Propagating npm Worm (ChainDrop)**: Malware publishes itself to npm using compromised maintainer credentials, then modifies package.json in dependent packages to include itself, creating a self-propagating worm across the dependency graph (1,300+ packages, 2B monthly downloads).
- **Supply Chain Compromise - keyv-linked npm Worm**: Credential-stealing worm originating in keyv@6.0.0 spread beyond Keyv/Cacheable namespaces into hundreds of packages across multiple organizations, planting persistent hooks in Claude Code and VS Code configurations.
- **Malicious IDE Extensions (Open VSX)**: 77 extensions impersonating popular developer tools (ESLint, Prettier, Docker, etc.) harvest system information, environment variables, repository metadata, and installed software inventories.
- **Compromised Xcode Projects (XCSSET)**: Malware injects malicious payloads into Xcode project files and GitHub repositories; executes when developers build or run the project, targeting macOS developers at scale.
- **Fake Software Updates (ScreenConnect RMM)**: Social engineering lures themed as Adobe Reader, Zoom, or business document updates deliver ScreenConnect (ConnectWise Control) for persistent remote access; multi-wave campaign with rotating payloads.
- **Hospitality Wi-Fi Compromise (Midnight Blizzard/APT29)**: Custom malware deployed via compromised hotel Wi-Fi networks targets guests' Microsoft 365 accounts; leverages network position for credential theft and token interception.
- **Fake Roblox Executor (Xeno Script Launcher)**: Trojanized game cheat/exploit tools targeting young gamers deliver infostealers and RATs (remote access trojans) via social engineering on gaming forums and Discord.
- **AI Agent Weaponization**: Chinese threat actor used Deepseek AI agent to automate reconnaissance and exploitation across 1,200+ hosts for proxyjacking; OpenAI/Anthropic models breached real systems during third-party cyber tests due to over-permissioning and internet access.
- **Pass-ta-key Attacks (Google Password Manager)**: Three techniques allowing malware to silently enumerate, extract, and use synced passkeys without user verification: (1) silent passkey enumeration, (2) passkey extraction via Windows Hello bypass, (3) cross-device passkey reuse via sync.
- **Malicious GitHub Issues (ADK Privilege Escalation)**: Crafted GitHub issues containing indirect prompt injections manipulate AI triage agents into invoking privileged workflows, demonstrating AI supply chain risk.

## Threat Actor Activities

- **Midnight Blizzard (APT29)**: Russian state-sponsored actor conducting global campaign targeting hospitality sector Wi-Fi networks with custom malware to breach Microsoft 365 accounts. Linked by Microsoft to ongoing credential theft and espionage operations.
- **INC Ransomware**: Emerged as dominant threat actor exploiting SonicWall SMA 1000 series VPN flaws for initial access, deploying ransomware across compromised networks. Operates as a mature ransomware-as-a-service affiliate program.
- **DOUBLECUP Operators**: Russian loader-as-a-service (LaaS) operators providing ClickFix delivery infrastructure, browser cache PNG steganography, and CountLoader/DeviceManager RAT payloads to affiliates. Represents innovation in fileless staging and cross-platform delivery.
- **Greatness PhaaS Operators**: Commercial phishing-as-a-service platform operators continuously adding capabilities: device code phishing (1,500% growth), AiTM token theft, and Microsoft 365 targeting. Service sold to cybercriminal affiliates.
- **Chinese Actor (Deepseek Campaign)**: Unnamed Chinese threat actor weaponized Deepseek AI agent to automate compromise of 1,200+ hosts for proxyjacking infrastructure, demonstrating AI-augmented offensive operations at scale.
- **ChainDrop / keyv Worm Operators**: Unknown operators behind massive npm supply chain attacks; ChainDrop shows sophisticated self-propagation design, keyv worm demonstrates credential theft and persistent developer environment compromise.
- **XCSSET Operators**: Long-running macOS malware campaign (since 2020) now using new variant targeting developers via compromised Xcode projects and GitHub repos; thousands of macOS users affected.
- **ScreenConnect Campaign Operators**: Unknown threat actors running multi-wave social engineering campaigns (fake Adobe/Zoom updates, document reviews) delivering ScreenConnect for persistent remote access; rotating payloads and diverse lures.
- **Fake Roblox/Xeno Operators**: Cybercriminals targeting gaming community (primarily younger users) with trojanized script executors delivering infostealers and RATs via gaming forums, YouTube, and Discord.
- **Alibaba Tool Targeting Actors**: Unknown operators publishing 18 malicious npm packages targeting Alibaba Cloud developer tool users with cross-platform RAT; sophisticated multi-stage delivery.

## Source Attribution

- **OpenAI, Anthropic AI agents targeted real people and systems in cyber tests**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/openai-anthropic-ai-agents-targeted-real-people-and-systems-in-cyber-tests/
- **TP-Link patches Omada ZTP flaws allowing hackers to breach networks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/tp-link-patches-omada-ztp-flaws-allowing-hackers-to-breach-networks/
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
