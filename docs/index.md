# Exploitation Report

## Executive Summary

A significant supply chain compromise has emerged targeting the advertising technology provider Adform, where attackers modified a legitimate JavaScript file to intercept and rewrite cryptocurrency wallet addresses on victim websites. This browser-side attack affects all sites loading the compromised Adform script, enabling automated theft of digital assets without requiring direct compromise of the target websites themselves.

Multiple state-sponsored threat actors are conducting diverse campaigns across critical infrastructure and government sectors. Chinese-speaking operators are deploying the OctLurk and SilkLurk malware families against Central Asian government organizations while simultaneously leveraging the DeepSeek AI model through the Hermes Agent framework to automate vulnerability scanning and exploitation against internet-exposed servers. North Korean actors continue their multi-pronged operations, including macOS malvertising campaigns delivering crypto-stealing malware, npm supply chain attacks targeting the Node.js ecosystem, and the hijacking of hotel Wi-Fi networks to deliver the CornFlake surveillance RAT via fake browser updates.

Critical infrastructure remains under sustained assault, with CISA warning of increased attacks against internet-exposed programmable logic controllers in U.S. water and wastewater systems. An Iran-linked actor has targeted over 30 community water systems in Minnesota, while a critical authentication bypass vulnerability in JetBrains TeamCity On-Premises enables unauthenticated remote code execution. Adobe has patched a maximum-severity flaw in Campaign Classic that allows arbitrary code execution without user interaction, and Arch Linux has temporarily disabled AUR package adoption following a surge in malicious package takeovers.

## Active Exploitation Details

### Adform Supply Chain Compromise
- **Description**: Attackers compromised the JavaScript file served by advertising technology company Adform, modifying it to function as a browser-side tool that detects and rewrites cryptocurrency wallet addresses copied to the clipboard or present on web pages. The malicious script replaces legitimate wallet addresses with attacker-controlled addresses across all customer sites loading the Adform script.
- **Impact**: Automated theft of cryptocurrency transactions from visitors to any website using Adform's advertising platform. The attack operates entirely client-side, making detection difficult for website operators.
- **Status**: Active exploitation detected; Adform has identified the incident and is working on remediation. Affected websites must ensure they are loading clean versions of the script.

### Adobe Campaign Classic Critical RCE
- **Description**: A maximum-severity security flaw in Adobe Campaign Classic (ACC), an enterprise marketing automation platform, that allows arbitrary code execution without any user interaction required.
- **Impact**: Unauthenticated remote code execution leading to full system compromise of Campaign Classic instances.
- **Status**: Adobe has released security updates addressing the vulnerability. Organizations running Campaign Classic should apply patches immediately.

### CornFlake RAT Delivery via Hijacked Hotel Wi-Fi
- **Description**: Threat actors compromise hotel Wi-Fi networks to intercept HTTP traffic and inject fake browser update prompts. When users accept the update, they receive the CornFlake remote access trojan capable of capturing webcam images, microphone audio, keystrokes, and other surveillance data.
- **Impact**: Full remote access to victim devices with extensive surveillance capabilities targeting travelers and business professionals.
- **Status**: Active campaign observed by Microsoft; no patch available for the underlying Wi-Fi hijacking technique beyond user awareness and HTTPS enforcement.

### TeamCity Authentication Bypass RCE
- **Description**: A critical authentication bypass vulnerability in JetBrains TeamCity On-Premises that allows unauthenticated attackers to achieve remote code execution on the build management server.
- **Impact**: Complete compromise of CI/CD infrastructure, potential supply chain poisoning of software builds, and lateral movement into development environments.
- **Status**: JetBrains has issued warnings and patches; on-premises instances require immediate updating.

### OctLurk and SilkLurk Government Targeting
- **Description**: A Chinese-speaking threat actor deploys two previously undocumented malware families—OctLurk and SilkLurk—against government organizations primarily in Central Asia, including Afghanistan, Kyrgyzstan, and Tajikistan.
- **Impact**: Persistent access to government networks, data exfiltration, and potential lateral movement within sensitive government infrastructure.
- **Status**: Active campaign with ongoing targeting of Central Asian government entities.

### DeepSeek AI Autonomous Attacks
- **Description**: A Chinese-speaking threat actor uses the DeepSeek AI model integrated with the open-source Hermes Agent framework to conduct fully autonomous cyberattacks against exposed servers. After an initial Telegram instruction, the AI autonomously scans, identifies vulnerabilities, and exploits targets with minimal human intervention.
- **Impact**: Accelerated vulnerability exploitation at scale, reducing the time between vulnerability disclosure and mass exploitation.
- **Status**: Active operations observed by Palo Alto Networks Unit 42; represents a significant evolution in AI-assisted offensive operations.

### HollowFrame Loader and Matryoshka Backdoor
- **Description**: A previously undocumented Go-based loader framework (HollowFrame) delivers a Rust-based backdoor (Matryoshka) via spear-phishing attacks targeting a law firm. The multi-stage payload demonstrates sophisticated evasion techniques.
- **Impact**: Persistent network access, credential theft, and data exfiltration from high-value professional services targets.
- **Status**: Active campaign documented by Blackpoint Cyber; indicates continued innovation in loader/backdoor architectures.

### DPRK macOS Malvertising Campaign
- **Description**: North Korean threat actors operate a sophisticated malvertising campaign targeting macOS users, redirecting victims to fake web pages displaying full-screen non-existent update notifications that deliver cryptocurrency-stealing malware.
- **Impact**: Compromise of macOS systems with focus on cryptocurrency wallet theft and financial fraud.
- **Status**: Active campaign attributed to DPRK-linked actors; leverages legitimate advertising networks for distribution.

### NPM Supply Chain Attacks (Debug/Chalk)
- **Description**: North Korean hackers compromised the npm packages "debug" and "chalk" (or typosquat variants) to inject malicious code into the software supply chain, targeting developers and build systems using the Node Package Manager ecosystem.
- **Impact**: Potential compromise of development environments, CI/CD pipelines, and downstream applications incorporating the poisoned packages.
- **Status**: Amazon has attributed the attacks to North Korean actors; affected packages have been quarantined by npm.

### Water Utility PLC Attacks
- **Description**: Threat actors target internet-exposed programmable logic controllers (PLCs) in water and wastewater utilities, exploiting default credentials, unpatched vulnerabilities, and misconfigurations to disrupt operations.
- **Impact**: Potential disruption of water treatment and distribution services, posing risks to public health and safety.
- **Status**: CISA has issued warnings following a significant increase in attacks; an Iran-linked actor targeted over 30 Minnesota community water systems.

### AUR Malicious Package Takeovers
- **Description**: Attackers exploit the Arch User Repository (AUR) package adoption process to take over legitimate but orphaned packages, injecting malicious code that executes when users install or update the packages.
- **Impact**: Supply chain compromise affecting Arch Linux users who install packages from AUR; potential system compromise and data theft.
- **Status**: Arch Linux has temporarily disabled package adoption to stem the flood of malicious takeovers.

### Device Code Phishing (OAuth 2.0 Abuse)
- **Description**: Attackers abuse the OAuth 2.0 device authorization grant flow to steal access tokens by tricking users into entering device codes on attacker-controlled pages, bypassing traditional credential phishing defenses including MFA.
- **Impact**: Account takeover without credential theft, bypassing multi-factor authentication, and persistent access to cloud resources.
- **Status**: Industrial-scale threat observed growing rapidly over six months; affects all platforms supporting device code flow (Microsoft, Google, GitHub, etc.).

## Affected Systems and Products

- **Adform Advertising Platform**: JavaScript library served to customer websites across the ad network; all sites embedding Adform scripts during the compromise window
- **Adobe Campaign Classic (ACC)**: Enterprise marketing automation platform; on-premises and managed cloud instances running unpatched versions
- **JetBrains TeamCity On-Premises**: CI/CD build management servers; all versions prior to the security patch release
- **Hotel Wi-Fi Networks**: Public hospitality networks with insufficient traffic encryption and monitoring; any HTTP-based captive portal or update mechanism
- **Arch User Repository (AUR)**: Community-maintained package repository for Arch Linux; orphaned packages eligible for adoption
- **npm Package Registry**: Node Package Manager ecosystem; specifically the "debug" and "chalk" packages (and typosquat variants)
- **Programmable Logic Controllers (PLCs)**: Internet-exposed industrial controllers in water/wastewater utilities; devices with default credentials or unpatched firmware
- **macOS Systems**: Apple computers targeted via malvertising redirects; users visiting compromised advertising networks
- **Central Asian Government Networks**: Government IT infrastructure in Afghanistan, Kyrgyzstan, Tajikistan, and neighboring states
- **Law Firm Networks**: Professional services organizations targeted via spear-phishing with custom loader/backdoor combinations
- **OAuth 2.0 Device Authorization Implementations**: All identity providers supporting RFC 8628 device code flow including Microsoft Entra ID, Google Workspace, GitHub, and others

## Attack Vectors and Techniques

- **Supply Chain Compromise (Adform)**: Legitimate third-party JavaScript modified at source to inject malicious functionality across all downstream consumers
- **Supply Chain Compromise (npm)**: Malicious code injected into widely-used open-source packages or typosquat variants targeting developer ecosystems
- **Supply Chain Compromise (AUR)**: Abuse of community package adoption process to insert malware into legitimate software distribution channels
- **Wi-Fi Hijacking / Man-in-the-Middle**: Compromise of public wireless networks to inject malicious content into unencrypted HTTP traffic
- **Fake Software Updates**: Social engineering via counterfeit browser or system update prompts delivered through compromised networks or malvertising
- **Malvertising**: Use of legitimate advertising networks to redirect victims to exploit pages or malware downloads
- **Spear-Phishing with Custom Loaders**: Targeted email delivery of multi-stage payloads (HollowFrame → Matryoshka) using novel Go/Rust tooling
- **AI-Automated Vulnerability Exploitation**: Large language models (DeepSeek) driving autonomous scanning, exploitation, and post-exploitation via agent frameworks (Hermes)
- **OAuth Device Code Phishing**: Abuse of legitimate device authorization flow to trick users into authorizing attacker-controlled sessions
- **Unauthenticated RCE via Authentication Bypass**: Exploitation of logic flaws in authentication mechanisms to achieve code execution without credentials (TeamCity, Adobe Campaign Classic)
- **Default Credential Exploitation**: Targeting internet-exposed industrial systems (PLCs) using factory-default usernames and passwords
- **Cryptocurrency Address Rewriting**: Client-side JavaScript monitoring clipboard and DOM for wallet addresses and substituting attacker-controlled addresses

## Threat Actor Activities

- **Chinese-Speaking APT (OctLurk/SilkLurk)**: Conducting sustained espionage against Central Asian government organizations using custom malware families; also operating AI-autonomous attack infrastructure leveraging DeepSeek and Hermes Agent for opportunistic server compromise
- **DPRK / North Korean Actors (Lazarus / sub-groups)**: Running multiple concurrent campaigns including macOS malvertising for crypto theft, npm supply chain attacks targeting developers, and hotel Wi-Fi hijacking delivering CornFlake RAT for surveillance
- **Iran-Linked Actors**: Targeting U.S. critical infrastructure, specifically community water systems in Minnesota, exploiting exposed PLCs to disrupt operations
- **Unknown/Unattributed Actors**: Exploiting Adform supply chain for cryptocurrency theft; conducting AUR package takeovers; operating device code phishing at industrial scale; deploying HollowFrame/Matryoshka against legal sector targets

## Source Attribution

- **Hackers Poison Adform Script to Swap Crypto Wallet Addresses Across Customer Sites**: The Hacker News - https://thehackernews.com/2026/08/hackers-poison-adform-script-to-swap.html
- **Adobe Campaign Classic CVSS 10.0 Flaw Could Run Code Without User Interaction**: The Hacker News - https://thehackernews.com/2026/08/adobe-campaign-classic-cvss-100-flaw.html
- **Hijacked Hotel Wi-Fi Pushes Fake Updates to Deliver Surveillance Malware**: The Hacker News - https://thehackernews.com/2026/08/hijacked-hotel-wi-fi-pushes-fake.html
- **Amgen says cloud data breach exposed patient health, proprietary info**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/amgen-says-cloud-data-breach-exposed-patient-health-proprietary-info/
- **Arch Linux disables AUR package adoption to stop malware flood**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/arch-linux-disables-aur-package-adoption-to-stop-malware-flood/
- **Online ad firm Adform’s script compromised to steal cryptocurrency**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/online-ad-firm-adforms-script-compromised-to-steal-cryptocurrency/
- **OpenAI says its new GPT 5.6 models are becoming more cost-efficient**: Bleeping Computer - https://www.bleepingcomputer.com/news/artificial-intelligence/openai-says-its-new-gpt-56-models-are-becoming-more-cost-efficient/
- **Suspected Chinese-Speaking Hackers Target Central Asian Governments With OctLurk and SilkLurk**: The Hacker News - https://thehackernews.com/2026/08/suspected-chinese-speaking-hackers.html
- **CISA Issues Fresh SBOM Guidance. Did They Get It Right?**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/cisa-issues-fresh-sbom-guidance
- **Hacker uses DeepSeek AI to autonomously attack vulnerable servers**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hacker-uses-deepseek-ai-to-autonomously-attack-vulnerable-servers/
- **CISA warns of cyberattacks disrupting U.S. water utilities**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-warns-of-cyberattacks-disrupting-us-water-utilities/
- **HollowFrame Loader Deploys Matryoshka Backdoor in Spear-Phishing Attack on Law Firm**: The Hacker News - https://thehackernews.com/2026/07/hollowframe-loader-deploys-matryoshka.html
- **Cheap Android TV Boxes Pose as Phones and Turn Owners’ Broadband Into Proxies**: The Hacker News - https://thehackernews.com/2026/07/cheap-android-tv-boxes-pose-as-phones.html
- **ESET tracks rise in malicious AI skills and adaptable malware**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/eset-tracks-rise-in-malicious-ai-skills-and-adaptable-malware/
- **The Morning After We Pull a Root of Trust, Nobody Owns It**: Dark Reading - https://www.darkreading.com/cyber-risk/morning-after-we-pull-root-of-trust-nobody-owns-it
- **Interpol Leverages Global System to Curtail Fraud Payments**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/interpol-leverages-global-system-curtail-fraud-payments
- **DROP Platform Lets Californians Reduce Digital Footprint**: Dark Reading - https://www.darkreading.com/data-privacy/drop-platform-lets-californians-ditch-their-data
- **USA Fencing Lunges Into the Hidden Identity Challenge in Amateur Sports**: Dark Reading - https://www.darkreading.com/identity-access-management-security/usa-fencing-hidden-identity-challenge-amateur-sports
- **Three Recent Chrome Releases Fix 1,442 Flaws, More Than Prior 23 Updates Combined**: The Hacker News - https://thehackernews.com/2026/07/three-recent-chrome-releases-fix-1442.html
- **Researchers Report 84 Flaws in 4G and 5G Cores, Including a Session Hijacking Flaw**: The Hacker News - https://thehackernews.com/2026/07/researchers-report-84-flaws-in-4g-and.html
- **6 Reasons Why Device Code Phishing is the Fastest-Growing Threat of 2026**: The Hacker News - https://thehackernews.com/2026/07/6-reasons-why-device-code-phishing-is.html
- **Chinese Hacker Commands DeepSeek via Telegram to Launch Autonomous Attacks**: The Hacker News - https://thehackernews.com/2026/07/chinese-hacker-commands-deepseek-via.html
- **Anthropic Says Claude Mistook the Open Internet for a CTF and Breached Three Organizations**: The Hacker News - https://thehackernews.com/2026/07/anthropic-says-claude-mistook-open.html
- **Anthropic's Claude breached 3 orgs, uploaded PyPI malware during tests**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/anthropics-claude-breached-3-orgs-uploaded-pypi-malware-during-tests/
- **South Korea fines telco giant KT $39 million for customer data breach**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/south-korea-fines-telco-giant-kt-39-million-for-customer-data-breach/
- **JetBrains warns of critical TeamCity remote code execution flaw**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/jetbrains-warns-of-critical-teamcity-remote-code-execution-flaw/
- **Minnesota Water Utility Attacks Expose Sector's Cyber-Risks**: Dark Reading - https://www.darkreading.com/ics-ot-security/minnesota-water-utility-attacks-expose-sector-cyber-risks
- **AI Harnesses Burst With Potential Exploit Opps**: Dark Reading - https://www.darkreading.com/application-security/ai-harnesses-potential-exploit-opps
- **DPRK-Linked macOS Malvertising Uses Fake Updates to Deliver Crypto-Stealing Malware**: The Hacker News - https://thehackernews.com/2026/07/dprk-linked-macos-malvertising-uses.html
- **Amazon links Debug, Chalk NPM supply-chain attacks to North Korean hackers**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/amazon-links-debug-chalk-npm-supply-chain-attacks-to-north-korean-hackers/
