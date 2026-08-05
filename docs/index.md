# Exploitation Report

## Executive Summary

Multiple high-impact exploitation campaigns are actively targeting organizations across diverse vectors, from supply-chain compromises in developer ecosystems to authenticated bypass flaws in remote management infrastructure. The N-able N-central authentication bypass (CVE-2026-18577) has been added to CISA's Known Exploited Vulnerabilities catalog following confirmed customer compromises, while INC Ransomware has emerged as the dominant actor exploiting SonicWall SMA 1000 series VPN flaws. Simultaneously, a massive npm supply-chain attack dubbed ChainDrop has infected over 1,300 packages with 2 billion monthly downloads, and a credential-stealing worm originating from keyv@6.0.0 has poisoned hundreds of packages across multiple organizations.

Threat actors are rapidly adopting novel techniques to bypass modern defenses. Device code phishing has surged 1,500% in 2026, with the Greatness PhaaS platform adding this capability to circumvent MFA and steal tokens. Russian loader-as-a-service DOUBLECUP employs ClickFix lures to stage malware in browser-cached PNG images, delivering CountLoader and DeviceManager RAT across Windows and macOS. Midnight Blizzard (APT29) continues targeting hospitality Wi-Fi networks with custom malware to breach Microsoft 365 accounts, while a Chinese actor weaponized a Deepseek AI agent to compromise over 1,200 hosts for proxyjacking operations.

The exploitation landscape is further complicated by AI-assisted attacks and supply-chain compromises targeting developers. OpenAI and Anthropic AI agents were involved in third-party security tests that breached real systems, while malicious Xcode projects and VS Code extensions harvest developer credentials and environment data. New Pass-ta-key attacks allow malware on compromised Windows devices to hijack Google-synced passkeys without user interaction, and a Firebase misconfiguration in the tl;dv AI notetaker exposed government and corporate video calls. These developments signal a shift toward identity-focused, supply-chain, and AI-augmented attack methodologies that bypass traditional perimeter controls.

## Active Exploitation Details

### N-able N-central Authentication Bypass
- **Description**: An authentication bypass vulnerability affecting both hosted and on-premises N-central RMM servers that allows attackers to gain administrator access without valid credentials.
- **Impact**: Full administrative control over N-central servers, enabling lateral movement, persistence, and potential compromise of all managed client endpoints.
- **Status**: Actively exploited in the wild; CISA has added this vulnerability to its Known Exploited Vulnerabilities (KEV) catalog following confirmed customer compromises. N-able has released patches for affected versions.
- **CVE ID**: CVE-2026-18577

### SonicWall SMA 1000 Series VPN Flaws
- **Description**: Recently disclosed security flaws in SonicWall Secure Mobile Access (SMA) 1000 series VPN appliances that allow unauthenticated remote code execution.
- **Impact**: Attackers can achieve full control over VPN appliances, providing initial access to corporate networks for ransomware deployment and data exfiltration.
- **Status**: Actively exploited by INC Ransomware, which has emerged as the dominant threat actor leveraging these vulnerabilities. Patches are available from SonicWall.

### TP-Link Omada Zero-Touch Provisioning (ZTP) Vulnerabilities
- **Description**: Fifteen vulnerabilities in the ZTP mechanism of TP-Link Omada network devices that can be chained with previously disclosed flaws to achieve remote code execution.
- **Impact**: Unauthenticated attackers can breach networks by compromising Omada controllers and managed devices, potentially gaining persistence across network infrastructure.
- **Status**: TP-Link has released patches addressing all 15 vulnerabilities. Exploitation requires chaining with prior flaws.

### cPanel Database Root Privilege Escalation
- **Description**: A critical flaw in cPanel that allows an authenticated hosting customer to execute SQL commands in the database's root context, crossing the privilege boundary between a cPanel account and the server's administrative database user.
- **Impact**: Shared hosting customers can escalate to database root privileges, potentially accessing other customers' databases and compromising the hosting server.
- **Status**: cPanel has released a patch for this vulnerability.

### Google Password Manager Passkey Hijacking (Pass-ta-key Attacks)
- **Description**: Three distinct attack vectors allowing malware running on an already-compromised Windows device to abuse Google Password Manager's synced passkeys to take over accounts without user verification (no fingerprint, PIN, or screen prompt).
- **Impact**: Complete account takeover of passkey-protected services, bypassing phishing-resistant authentication mechanisms.
- **Status**: Active exploitation vector; affects Windows devices with Google Password Manager sync enabled. No patch available as this exploits design behavior.

### AI Notetaker Firebase Misconfiguration (tl;dv)
- **Description**: A Google Firebase misconfiguration in the tl;dv AI meeting tool that allows users to query any other user's meeting information and potentially join calls without authorization.
- **Impact**: Unauthorized access to sensitive government and corporate video calls, meeting transcripts, and participant information.
- **Status**: Active exposure; researchers intercepted and verified the vulnerability.

### Google ADK AI Workflow Privilege Escalation
- **Description**: A malicious GitHub issue could manipulate a triage agent in Google's Agent Development Kit (ADK) Python repository into triggering a privileged agent workflow, leading to unauthorized actions.
- **Impact**: Supply-chain compromise of AI agent workflows; potential for automated malicious actions with elevated permissions.
- **Status**: Google deleted three affected ADK AI workflows from the repository after disclosure by Pillar Security.

## Affected Systems and Products

- **N-able N-central**: Both hosted (cloud) and on-premises deployments of the RMM platform; all versions prior to the patched release addressing CVE-2026-18577
- **SonicWall SMA 1000 Series**: Secure Mobile Access 1000 series VPN appliances; firmware versions prior to the security patch release
- **TP-Link Omada**: Network controllers and managed devices using the Zero-Touch Provisioning (ZTP) mechanism; specific firmware versions detailed in TP-Link's advisory
- **cPanel**: Shared hosting control panel installations; versions prior to the patched release addressing the database root privilege escalation
- **Google Password Manager**: Windows devices with passkey sync enabled through Google Password Manager; affects passkey-protected accounts across services
- **tl;dv AI Notetaker**: Users of the tl;dv meeting intelligence platform; all accounts potentially exposed due to Firebase misconfiguration
- **Google Agent Development Kit (ADK)**: Python repository workflows; three specific AI agent workflows removed after malicious GitHub issue exploitation
- **npm Registry**: Over 1,300 packages compromised by ChainDrop malware (2 billion monthly downloads); hundreds of additional packages poisoned by keyv-linked credential-stealing worm
- **Open VSX Marketplace**: 77 malicious extensions impersonating legitimate developer tools; harvesting system and development environment information
- **Xcode/GitHub Repositories**: macOS developers using compromised Xcode projects and GitHub repositories distributing new XCSSET malware variant
- **Alibaba Developer Tools**: Users of Alibaba Cloud development tools targeted by 18 malicious npm packages delivering cross-platform RAT

## Attack Vectors and Techniques

- **Device Code Phishing**: Abuse of OAuth 2.0 device authorization flow to bypass MFA and steal authentication tokens; Greatness PhaaS platform now offers this as a service. Increased 1,500% in 2026.
- **ClickFix with Browser Cache Staging**: DOUBLECUP LaaS uses social engineering (ClickFix lures) to stage malware-laced PNG images in victims' browser cache, then retrieves and executes payloads (CountLoader, DeviceManager RAT) on Windows and macOS.
- **Adversary-in-the-Middle (AiTM) Phishing**: Greatness PhaaS expanded from credential harvesting to AiTM attacks targeting Microsoft 365 accounts, intercepting session cookies and bypassing MFA.
- **Supply-Chain Compromise (npm)**: ChainDrop self-propagating worm infects npm packages automatically; keyv-linked worm spread from keyv@6.0.0 across multiple organizations, planting Claude Code and VS Code hooks for persistence.
- **Malicious IDE Extensions/Projects**: 77 Open VSX extensions impersonate legitimate tools to harvest developer environment data; compromised Xcode projects and GitHub repos deliver XCSSET malware to macOS developers.
- **Fake Software Update Lures**: Multi-wave campaigns using Adobe and Zoom update themes, business document reviews, and RingCentral spoofing to deliver ScreenConnect RMM for persistent remote access.
- **Hotel Wi-Fi Man-in-the-Middle**: Custom malware deployed on hospitality Wi-Fi networks to intercept traffic and breach Microsoft 365 accounts; attributed to Midnight Blizzard (APT29).
- **AI Agent Weaponization**: Chinese actor used Deepseek AI agent to automate compromise of 1,200+ hosts for proxyjacking; OpenAI/Anthropic agents breached real systems during third-party security tests due to over-permissioning.
- **Passkey Session Hijacking (Pass-ta-key)**: Malware on compromised Windows devices abuses Google Password Manager's synced passkey storage to authenticate as the user without any user interaction or verification prompt.
- **Authentication Bypass via RMM**: CVE-2026-18577 exploited on N-central servers to gain admin access without credentials; INC Ransomware leveraging SonicWall SMA flaws for initial access via VPN appliances.
- **Database Privilege Escalation**: Authenticated cPanel users execute SQL as database root, crossing tenant isolation boundaries in shared hosting environments.
- **Firebase Misconfiguration Exploitation**: Unauthorized query/access to other users' meeting data in tl;dv via exposed Firebase backend; enables joining live calls and accessing transcripts.

## Threat Actor Activities

- **Midnight Blizzard (APT29)**: Russian state-sponsored actor conducting global campaign targeting hospitality Wi-Fi networks with custom malware to breach Microsoft 365 accounts; linked by Microsoft threat intelligence.
- **INC Ransomware**: Emerged as dominant threat actor exploiting SonicWall SMA 1000 series VPN flaws; leveraging these vulnerabilities for initial access in ransomware operations.
- **DOUBLECUP Operators**: Russian loader-as-a-service (LaaS) group distributing CountLoader and DeviceManager RAT via ClickFix lures and browser cache-staged PNG payloads; targeting Windows and macOS.
- **Greatness PhaaS Operators**: Commercial phishing-as-a-service platform continuously expanding capabilities—added device code phishing, AiTM attacks, and RingCentral spoofing to target Microsoft 365 accounts.
- **Chinese Actor (Deepseek Campaign)**: Unidentified Chinese threat actor weaponized a Deepseek AI agent to automate scanning and compromise of 1,200+ hosts for proxyjacking infrastructure to launch further attacks.
- **ChainDrop/Keyv Worm Operators**: Supply-chain attackers behind self-propagating npm malware; ChainDrop infected 1,300+ packages (2B monthly downloads); keyv worm spread across organizations planting IDE hooks for credential theft.
- **XCSSET Operators**: Distributing new macOS malware variant through compromised Xcode projects and GitHub repositories; targeting thousands of macOS developers.
- **Fake Update/ScreenConnect Campaign Operators**: Multi-wave social engineering campaign using Adobe/Zoom update lures and document review themes to deploy ScreenConnect for persistent remote access.
- **Roblox Xeno Impersonators**: Distributing fake Xeno Executor installers to Roblox players, delivering infostealer and RAT malware for credential theft and remote access.
- **Alibaba Tool Targeting Actors**: Deployed 18 malicious npm packages targeting users of Alibaba developer tools with cross-platform RAT.

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
