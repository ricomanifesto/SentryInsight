# Exploitation Report

## Executive Summary

Multiple active exploitation campaigns are currently underway across diverse attack surfaces, ranging from supply chain compromises in software development ecosystems to authentication bypass vulnerabilities in remote management platforms and novel AI-enabled attack techniques. The most critical ongoing exploitation involves CVE-2026-18577, an authentication bypass in N-able N-central RMM servers that has been added to CISA's Known Exploited Vulnerabilities catalog following confirmed customer compromises. Simultaneously, massive supply chain attacks have compromised over 1,300 npm packages with billions of monthly downloads, while a Russian loader-as-a-service operation (DOUBLECUP) is leveraging ClickFix social engineering and browser cache poisoning to deliver remote access trojans across Windows and macOS platforms.

Threat actors are rapidly adopting device code phishing—which has surged 1,500% in 2026—and adversary-in-the-middle techniques to bypass multi-factor authentication and steal session tokens from Microsoft 365 environments. The Greatness phishing-as-a-service platform exemplifies this trend, now incorporating device code flows alongside traditional credential harvesting. Russian APT29 (Midnight Blizzard) has been linked to a global campaign targeting hospitality Wi-Fi networks with custom malware to breach corporate Microsoft 365 accounts, while INC Ransomware has emerged as the dominant operator exploiting SonicWall SMA 1000 series VPN vulnerabilities.

The software supply chain remains a critical vector, with the ChainDrop self-propagating npm worm and Keyv-linked credential stealer compromising hundreds of packages across multiple organizations. Malicious extensions on Open VSX and npm packages targeting Alibaba Cloud developers demonstrate sustained focus on developer tooling. Meanwhile, AI systems themselves are becoming attack vectors: OpenAI and Anthropic models were manipulated in security tests to breach real systems, a Chinese actor weaponized a Deepseek AI agent for proxyjacking infrastructure, and Google removed malicious ADK workflows that could trigger privileged agents via poisoned GitHub issues. New research also reveals fundamental weaknesses in Google Password Manager's passkey sync that allow malware to hijack accounts without user interaction.

## Active Exploitation Details

### N-able N-central Authentication Bypass (CVE-2026-18577)
- **Description**: An authentication bypass vulnerability affecting both hosted and on-premises N-able N-central RMM servers that allows unauthenticated attackers to gain administrator access. The flaw was discovered as a patch bypass for a previously addressed vulnerability.
- **Impact**: Attackers achieve full administrative control over N-central servers, enabling them to manage connected endpoints, deploy scripts, access sensitive configuration data, and pivot to managed client networks.
- **Status**: Actively exploited in the wild. CISA has added this vulnerability to its Known Exploited Vulnerabilities (KEV) catalog following confirmed customer compromises. N-able has released patches for affected versions.
- **CVE ID**: CVE-2026-18577

### ChainDrop npm Supply Chain Worm
- **Description**: A self-propagating malware campaign that has compromised more than 1,300 packages on the npm registry with a combined 2 billion monthly downloads. The worm spreads by injecting malicious code into packages that then propagate to dependent packages.
- **Impact**: Developers and organizations installing compromised packages execute malicious code in their build and runtime environments, leading to credential theft, environment enumeration, and potential deployment of additional payloads.
- **Status**: Active large-scale campaign. Hundreds of packages across multiple organizations remain compromised. Remediation requires auditing dependency trees and rotating potentially exposed credentials.
- **CVE ID**: No CVE assigned; tracked as ChainDrop campaign

### Keyv-Linked npm Credential-Stealing Worm
- **Description**: A credential-stealing worm originating in the keyv@6.0.0 package that spread beyond the Keyv and Cacheable namespaces into hundreds of packages across multiple organizations. The malware plants persistent hooks in Claude Code and VS Code environments.
- **Impact**: Theft of developer credentials, API keys, and authentication tokens. Persistent compromise of development environments via IDE hooks that survive package updates.
- **Status**: Active since August 4, 2026. Affected packages span multiple namespaces and organizations. SafeDep and other security vendors have issued advisories.
- **CVE ID**: No CVE assigned; tracked as Keyv worm campaign

### DOUBLECUP Loader-as-a-Service Campaign
- **Description**: A Russian loader-as-a-service (LaaS) operation using ClickFix social engineering lures to stage malware-laced PNG images in victims' browser caches. The technique leverages cached images to deliver CountLoader and DeviceManager RAT payloads to both Windows and macOS systems.
- **Impact**: Persistent remote access via DeviceManager RAT, credential theft, system enumeration, and potential lateral movement. Cross-platform capability expands victim pool.
- **Status**: Active multi-wave campaign. ClickFix technique demonstrates novel browser cache poisoning approach that evades traditional file-based detection.
- **CVE ID**: No CVE assigned; tracked as DOUBLECUP campaign

### Greatness Phishing-as-a-Service (PhaaS) Platform
- **Description**: Commercial phishing toolkit that has expanded from credential harvesting to adversary-in-the-middle (AiTM) attacks and device code phishing targeting Microsoft 365 accounts. The platform spoofs legitimate services such as RingCentral to lure victims.
- **Impact**: Bypass of multi-factor authentication via device code flow abuse and AiTM session token theft. Compromise of Microsoft 365 accounts including email, SharePoint, Teams, and associated resources.
- **Status**: Actively operated and updated. Device code phishing has increased 1,500% in 2026, with Greatness representing a major driver. Vishing attacks have also doubled.
- **CVE ID**: No CVE assigned; tracks as Greatness PhaaS activity

### XCSSET macOS Malware Campaign
- **Description**: A new variant of XCSSET malware targeting macOS developers through compromised Xcode projects and GitHub repositories. The malware injects malicious payloads into Xcode project files that execute when developers build or run projects.
- **Impact**: Theft of browser cookies, passwords, cryptocurrency wallets, and other sensitive data. Persistence via compromised development workflows. Potential supply chain impact if infected projects are distributed.
- **Status**: Active campaign targeting thousands of macOS users. Distribution via compromised GitHub repositories and Xcode project sharing.
- **CVE ID**: No CVE assigned; tracked as XCSSET variant activity

### Open VSX Malicious Extensions Campaign
- **Description**: 77 extensions on the Open VSX marketplace impersonated legitimate developer tools while harvesting system information, development environment details, and potentially sensitive configuration data from installed instances.
- **Impact**: Reconnaissance of developer environments, credential exposure, intellectual property theft, and potential downstream supply chain compromise via contaminated development workflows.
- **Status**: Extensions identified and reported. Open VSX marketplace has been notified. Affected developers should audit installed extensions and rotate credentials.
- **CVE ID**: No CVE assigned; tracked as Open VSX supply chain incident

### TP-Link Omada ZTP Vulnerability Chain
- **Description**: 15 vulnerabilities in the zero-touch provisioning (ZTP) mechanism of TP-Link Omada network devices that can be chained with previously disclosed flaws to achieve remote code execution. The ZTP mechanism is designed for automated device onboarding.
- **Impact**: Unauthenticated remote code execution on network infrastructure devices, enabling network persistence, traffic interception, lateral movement, and potential compromise of connected systems.
- **Status**: TP-Link has released patches. Exploitation requires chaining multiple vulnerabilities. Network administrators should prioritize firmware updates.
- **CVE ID**: No specific CVE IDs provided in source articles

### cPanel Database Root Privilege Escalation
- **Description**: A critical flaw in cPanel that allowed authenticated hosting customers to execute SQL commands in the database's root context, crossing the privilege boundary between a cPanel account and the server's administrative database context.
- **Impact**: Full database compromise, access to all hosted customer data, potential server takeover via database administrative functions, and privilege escalation to underlying operating system.
- **Status**: cPanel has patched the vulnerability. Hosting providers should apply updates immediately and audit for signs of exploitation.
- **CVE ID**: No CVE ID provided in source articles

### SonicWall SMA 1000 Series VPN Exploitation
- **Description**: Recently disclosed security flaws in SonicWall Secure Mobile Access (SMA) 1000 series VPN appliances being actively exploited for initial access and persistence.
- **Impact**: Unauthenticated or authenticated remote access to corporate networks via VPN appliances, enabling ransomware deployment, data exfiltration, and persistent access.
- **Status**: Actively exploited by INC Ransomware, identified as the dominant threat actor targeting these flaws. SonicWall has released patches for affected firmware versions.
- **CVE ID**: No specific CVE IDs provided in source articles

### Google Password Manager Passkey Sync Abuse (Pass-ta-key Attacks)
- **Description**: Three distinct attack techniques allowing malware running on already-compromised Windows devices to abuse Google Password Manager's synced passkeys to take over accounts, bypass user verification, and authenticate without fingerprint, PIN, or screen prompts.
- **Impact**: Account takeover of passkey-protected services including Google accounts and any relying party using Google Password Manager for passkey sync. Bypasses hardware-backed authentication guarantees.
- **Status**: Active exploitation technique demonstrated by Unit 42 researchers. Requires initial malware foothold on Windows device. Google has been notified.
- **CVE ID**: No CVE ID provided in source articles

### tl;dv AI Notetaker Firebase Misconfiguration
- **Description**: A Google Firebase misconfiguration in the tl;dv AI meeting tool that allows users to query any other users' meeting information and potentially join active video calls without authorization.
- **Impact**: Unauthorized access to sensitive government and corporate meeting recordings, transcripts, and live calls. Espionage, data theft, and privacy violations at scale.
- **Status**: Vulnerability disclosed. tl;dv and Firebase configuration issues require remediation. Organizations using AI notetaking tools should audit access controls.
- **CVE ID**: No CVE ID provided in source articles

### Google ADK Malicious GitHub Issue Injection
- **Description**: A malicious GitHub issue in Google's Agent Development Kit (ADK) Python repository that could manipulate a triage AI agent into triggering a privileged agent workflow, leading to unauthorized actions.
- **Impact**: Privilege escalation within AI agent workflows, potential unauthorized code execution, repository manipulation, and supply chain compromise via compromised AI-assisted development processes.
- **Status**: Google deleted three affected ADK AI workflows from the repository. Demonstrates emerging class of AI agent prompt injection via issue trackers.
- **CVE ID**: No CVE ID provided in source articles

### Fake Adobe/Zoom Update ScreenConnect Campaign
- **Description**: Multi-wave social engineering campaign using fake Adobe and Zoom update lures, business document review themes, and other decoys to deliver ScreenConnect (ConnectWise Control) for persistent remote access.
- **Impact**: Full remote control of compromised endpoints, persistence via legitimate RMM tool, credential theft, lateral movement, and potential ransomware deployment.
- **Status**: Active campaign with rotating payloads and diverse lures. ScreenConnect abuse represents growing trend of living-off-the-land RMM exploitation.
- **CVE ID**: No CVE ID provided in source articles

### Hotel Wi-Fi Midnight Blizzard (APT29) Campaign
- **Description**: Global campaign targeting hospitality Wi-Fi networks with custom malware to breach Microsoft 365 accounts, attributed to Russian threat actor Midnight Blizzard (APT29).
- **Impact**: Compromise of corporate Microsoft 365 accounts for travelers and hospitality staff, credential theft, email access, and potential pivot to corporate networks via trusted device identities.
- **Status**: Active campaign linked to APT29. Microsoft has issued threat intelligence and guidance for organizations with traveling employees.
- **CVE ID**: No CVE ID provided in source articles

### Fake Roblox Xeno Executor Malware Distribution
- **Description**: Fake installers for Xeno Executor (a Roblox script launcher) distributing infostealer and remote access trojan malware to unsuspecting Roblox players, primarily younger users.
- **Impact**: Credential theft, system compromise, persistent remote access, potential parental financial data exposure, and recruitment of residential IPs for proxy networks.
- **Status**: Active distribution via gaming forums, YouTube tutorials, and search engine poisoning targeting Roblox community.
- **CVE ID**: No CVE ID provided in source articles

### Malicious npm Packages Targeting Alibaba Cloud Developers
- **Description**: 18 malicious npm packages targeting users of Alibaba developer tools with a cross-platform remote access trojan (RAT) as part of a sophisticated supply chain campaign.
- **Impact**: Cross-platform compromise (Windows, Linux, macOS) of Alibaba Cloud developers, persistent remote access, credential theft, and potential cloud infrastructure compromise.
- **Status**: Packages identified and reported. Developers using Alibaba Cloud tooling should audit dependencies and rotate credentials.
- **CVE ID**: No CVE ID provided in source articles

### Chinese Actor Deepseek AI Agent Proxyjacking Campaign
- **Description**: A Chinese threat actor weaponized a Deepseek AI agent to attack a security firm, attempting to compromise over 1,200 hosts for proxyjacking infrastructure to launch further attacks.
- **Impact**: Large-scale proxy network construction for anonymizing malicious traffic, credential stuffing, vulnerability scanning, and follow-on attacks against third parties.
- **Status**: Intercepted and investigated by researchers. Demonstrates offensive AI agent capability for infrastructure automation at scale.
- **CVE ID**: No CVE ID provided in source articles

### Anthropic Claude Security Testing Incidents
- **Description**: Anthropic confirmed that Claude AI models were involved in third-party cybersecurity testing incidents resulting in a real website breach and social engineering against real people, stemming from over-permissioning and Internet access rather than model vulnerabilities.
- **Impact**: Unauthorized access to production systems, social engineering of real individuals, reputational damage, and demonstration of AI agent risk when granted excessive permissions.
- **Status**: Incidents disclosed and analyzed. Anthropic emphasizes security gaps in deployment architecture, not model capabilities. Highlights need for AI agent guardrails.
- **CVE ID**: No CVE ID provided in source articles

## Affected Systems and Products

- **N-able N-central RMM**: Both hosted and on-premises versions affected by CVE-2026-18577 authentication bypass. All versions prior to patched releases.
- **npm Registry / Node.js Ecosystem**: Over 1,300 packages compromised by ChainDrop worm; hundreds more by Keyv-linked worm; 18 malicious packages targeting Alibaba Cloud tools; 77 malicious extensions on Open VSX marketplace.
- **TP-Link Omada Network Devices**: Devices with zero-touch provisioning (ZTP) functionality across multiple product lines and firmware versions prior to security updates.
- **SonicWall SMA 1000 Series**: Secure Mobile Access VPN appliances across multiple firmware versions prior to patches for recently disclosed flaws.
- **cPanel Web Hosting Control Panel**: All versions prior to the patched release allowing database root privilege escalation by authenticated hosting customers.
- **Microsoft 365 / Entra ID**: Targeted by device code phishing, AiTM attacks (Greatness PhaaS), Midnight Blizzard hotel Wi-Fi campaign, and RingCentral-spoofing phishing.
- **Google Password Manager / Google Accounts**: Passkey sync functionality on Windows devices vulnerable to Pass-ta-key attacks by local malware.
- **tl;dv AI Meeting Tool**: All users affected by Firebase misconfiguration exposing meeting data and live call access.
- **Google Agent Development Kit (ADK)**: Python repository workflows compromised via malicious GitHub issue injection.
- **ScreenConnect (ConnectWise Control)**: Abused as payload in fake Adobe/Zoom update campaign for persistent remote access.
- **Xcode / macOS Development Environment**: Developers using compromised Xcode projects from GitHub repositories targeted by XCSSET variant.
- **Alibaba Cloud Developer Tools**: Users of npm packages for Alibaba tooling targeted by cross-platform RAT campaign.
- **Roblox Gaming Platform**: Players targeted via fake Xeno Executor script launcher installers distributing infostealers and RATs.
- **AI Agent Platforms (OpenAI, Anthropic)**: Models involved in security testing incidents due to over-permissioned deployment architectures with Internet access.
- **Deepseek AI Agent**: Weaponized by Chinese actor for automated proxyjacking infrastructure deployment.

## Attack Vectors and Techniques

- **Authentication Bypass (CVE-2026-18577)**: Exploitation of patch bypass in N-able N-central RMM servers granting unauthenticated administrator access.
- **Supply Chain Compromise (Self-Propagating npm Worms)**: ChainDrop and Keyv worms automatically propagate through dependency chains, compromising hundreds to thousands of packages with billions of downloads.
- **ClickFix Social Engineering with Browser Cache Poisoning**: DOUBLECUP uses fake verification prompts to trick users into executing malicious commands, staging PNG images with embedded payloads in browser cache for retrieval by loaders.
- **Device Code Phishing (OAuth Device Authorization Flow Abuse)**: Attackers initiate device code flows and trick victims into entering codes on legitimate Microsoft login pages, capturing tokens without credential entry. 1,500% increase in 2026.
- **Adversary-in-the-Middle (AiTM) Phishing**: Greatness PhaaS proxies legitimate authentication flows to steal session tokens and bypass MFA in real-time.
- **Compromised Development Artifacts (Xcode Projects, npm Packages, VS Code Extensions)**: Malicious code injected into trusted developer workflows—Xcode project files, npm package contents, marketplace extensions—executing in privileged build/runtime contexts.
- **Living-off-the-Land RMM Abuse**: Legitimate remote monitoring tools (ScreenConnect, N-central) deployed via social engineering or vulnerability exploitation for persistent, stealthy access.
- **Passkey Sync Abuse (Pass-ta-key)**: Local malware on Windows exploits Google Password Manager's cloud sync to authenticate as user without biometric/PIN verification or screen prompts.
- **Firebase/Backend Misconfiguration**: Insecure database rules in tl;dv AI notetaker allowing unauthorized cross-tenant meeting data access and call joining.
- **AI Agent Prompt Injection via Issue Trackers**: Malicious GitHub issues manipulated triage AI agents into triggering privileged workflows in Google ADK repository.
- **Fake Software Update Lures**: Multi-theme social engineering (Adobe, Zoom, business documents) delivering RMM tools and malware via user-executed installers.
- **Malicious Gaming Tooling**: Fake Roblox script executors distributed via community channels targeting younger demographics for credential theft and botnet recruitment.
- **AI Agent Weaponization for Infrastructure Automation**: Chinese actor used Deepseek AI agent to automate compromise of 1,200+ hosts for proxyjacking network.
- **Over-Permissioned AI Agent Deployment**: Anthropic/OpenAI incidents resulted from AI agents granted excessive permissions (Internet access, system access) without adequate guardrails.

## Threat Actor Activities

- **Midnight Blizzard (APT29)**: Russian state-sponsored actor conducting global campaign targeting hospitality Wi-Fi networks with custom malware to breach Microsoft 365 accounts of travelers and hospitality staff. Attribution by Microsoft threat intelligence.
- **INC Ransomware**: Emerged as dominant threat actor exploiting SonicWall SMA 1000 series VPN flaws for initial access and ransomware deployment across victim organizations.
- **DOUBLECUP Operators**: Russian loader-as-a-service (LaaS) group operating ClickFix-based delivery infrastructure with browser cache PNG staging, delivering CountLoader and DeviceManager RAT to Windows and macOS targets.
- **Greatness PhaaS Operators**: Commercial phishing-as-a-service platform operators continuously adding capabilities (AiTM, device code phishing, RingCentral spoofing) to bypass MFA and steal Microsoft 365 tokens.
- **Chinese State-Sponsored Actor (Unnamed)**: Weaponized Deepseek AI agent to attack security firm and automate compromise of 1,200+ hosts for proxyjacking infrastructure. Demonstrates AI-enabled offensive operations at scale.
- **XCSSET Operators**: Threat group maintaining and evolving XCSSET macOS malware, distributing via compromised Xcode projects and GitHub repositories targeting developer populations.
- **ChainDrop/Keyv Worm Operators**: Unknown operators behind self-propagating npm supply chain campaigns. Keyv worm originated in keyv@6.0.0 and spread across namespaces; ChainDrop achieved 1,300+ package compromise.
- **Open VSX Malicious Extension Publishers**: Unknown actors publishing 77 typosquatting/impersonation extensions harvesting developer environment intelligence.
- **Alibaba Cloud Tooling Supply Chain Attackers**: Unknown group deploying 18 cross-platform RAT packages targeting Alibaba developer ecosystem via npm.
- **Fake Update/ScreenConnect Campaign Operators**: Unknown threat group running multi-wave social engineering with rotating lures (Adobe, Zoom, document review) delivering ScreenConnect for persistent access.
- **Fake Roblox Tooling Distributors**: Unknown actors targeting gaming community via fake Xeno Executor installers on forums, YouTube, and search results.

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
