# Exploitation Report

## Executive Summary

Critical exploitation activity spans multiple vectors this period, with authentication bypass flaws in widely deployed remote monitoring and management (RMM) software enabling full administrative takeover of managed customer environments. CISA has added the N-able N-central vulnerability (CVE-2026-18577) to its Known Exploited Vulnerabilities catalog after confirmed customer compromises, and the vendor's initial patch proved incomplete—attackers continue to achieve remote administrative access and pivot to downstream client systems. Simultaneously, a global campaign by Russian state actor Midnight Blizzard (APT29) leverages compromised hotel Wi-Fi networks to deploy custom malware targeting Microsoft 365 accounts, while INC Ransomware has emerged as the dominant operator exploiting recently disclosed SonicWall SMA 1000 series VPN flaws.

Social engineering and identity-based attacks have surged dramatically. Device code phishing has increased 1,500% year-over-year and vishing has doubled, as threat actors adopt techniques that bypass entrenched controls and leave minimal forensic evidence. New "Pass-ta-key" attacks allow malware on compromised Windows devices to hijack Google-synced passkeys without user interaction, and a Russian loader-as-a-service called DOUBLECUP uses ClickFix techniques to hide malicious payloads in browser-cached PNG images, delivering CountLoader cross-platform. Supply chain compromise continues with 18 malicious npm packages targeting Alibaba Cloud developer tool users and a poisoned Adform advertising script rewriting cryptocurrency wallet addresses across customer sites.

High-impact financial theft and data breaches round out the landscape. A firmware flaw in COLDCARD hardware wallets (flawed RNG) enabled theft of approximately $88.6 million in Bitcoin from thousands of wallets, with one sweep draining 1,082.65 BTC (~$70.2 million) in 41 minutes. The ExfilSquad group leaked contact data for over 100,000 UK police officers and criminal justice professionals following a breach of the Police National Legal Database. Chinese-speaking actors are leveraging the leaked DarkSword exploit kit to deploy GHOSTBLADE malware on iOS devices, while another Chinese operation weaponized a Deepseek AI agent to compromise over 1,200 hosts for proxyjacking infrastructure.

## Active Exploitation Details

### N-able N-central Authentication Bypass (CVE-2026-18577)
- **Description**: An authentication bypass vulnerability affecting both hosted and on-premises N-able N-central servers that allows unauthenticated attackers to gain administrator-level access to the RMM platform.
- **Impact**: Attackers achieve full administrative control over N-central servers and can pivot to all downstream customer systems managed through those servers, enabling widespread supply chain compromise across managed service provider (MSP) client bases.
- **Status**: Actively exploited in the wild. CISA added this vulnerability to the Known Exploited Vulnerabilities (KEV) catalog following confirmed customer compromises. N-able released an initial patch that proved incomplete; attackers continued to exploit the bypass after the first fix. A subsequent update has been issued.
- **CVE ID**: CVE-2026-18577

### SonicWall SMA 1000 Series VPN Vulnerabilities
- **Description**: Recently disclosed security flaws in SonicWall Secure Mobile Access (SMA) 1000 series VPN appliances that allow unauthenticated remote attackers to compromise the appliances.
- **Impact**: Full appliance compromise enabling network access, lateral movement, and ransomware deployment across victim organizations.
- **Status**: Actively exploited by INC Ransomware, which has emerged as the dominant threat actor leveraging these flaws. Exploitation is ongoing across multiple victim organizations.
- **CVE ID**: Specific CVE IDs not provided in source articles.

### Hotel Wi-Fi Compromise Campaign (Midnight Blizzard / APT29)
- **Description**: A global campaign targeting hospitality Wi-Fi networks where attackers compromise hotel network infrastructure to deploy custom malware against guests' devices, specifically targeting Microsoft 365 account credentials.
- **Impact**: Credential theft, Microsoft 365 account takeover, potential access to corporate email, documents, and cloud resources for travelers and executives staying at compromised hotels.
- **Status**: Active global campaign attributed to Russian state-sponsored actor Midnight Blizzard (APT29). Custom malware designed for stealth and persistence on victim devices.
- **CVE ID**: No specific CVE identified; leverages network infrastructure compromise and custom malware deployment.

### Pass-ta-key Attacks on Google Password Manager
- **Description**: Three distinct attack techniques allowing malware running as an ordinary user on a compromised Windows device to abuse Google Password Manager's synced passkeys functionality, signing into passkey-protected accounts without any user verification (fingerprint, PIN, or screen prompt).
- **Impact**: Complete bypass of passkey-based multi-factor authentication, enabling account takeover for any service using Google-synced passkeys, with zero user interaction or visible indicators.
- **Status**: Demonstrated by Unit 42 researchers; attacks are practical against current Google Password Manager implementation on Windows. No patch available at time of reporting.
- **CVE ID**: No CVE IDs assigned; these are design/implementation flaws in the passkey sync and authentication flow.

### DOUBLECUP ClickFix Loader-as-a-Service
- **Description**: A Russian-operated loader-as-a-service that uses ClickFix social engineering techniques to hide malicious code within PNG images cached by victims' browsers, ultimately delivering the CountLoader payload to both Windows and macOS devices.
- **Impact**: Cross-platform malware delivery that evades traditional file-based detection by storing payloads in browser cache images; delivers CountLoader which provides persistent remote access and further payload deployment capability.
- **Status**: Active service offering; observed in the wild targeting both Windows and macOS users through ClickFix deception pages.
- **CVE ID**: No CVE; leverages browser caching behavior and social engineering (ClickFix technique).

### Malicious npm Supply Chain Attack (Alibaba Developer Tools)
- **Description**: Eighteen malicious npm packages targeting users of Alibaba Cloud developer tools, delivering a cross-platform remote access trojan (RAT) as part of a sophisticated supply chain campaign.
- **Impact**: Cross-platform RAT installation on developer machines, providing attackers with persistent remote access, credential theft, and potential pivot to production environments and source code repositories.
- **Status**: Active campaign; packages discovered and reported. Affected packages removed from npm registry but may persist in dependent projects.
- **CVE ID**: No CVE IDs assigned; supply chain compromise via malicious package publishing.

### COLDCARD Hardware Wallet RNG Flaw
- **Description**: A firmware vulnerability in COLDCARD hardware wallets involving a flawed random number generator (RNG) that produces predictable seed values, allowing attackers to derive private keys and steal Bitcoin from affected wallets.
- **Impact**: Theft of an estimated $88.6 million in Bitcoin from thousands of wallets whose seeds were generated using the flawed RNG. One observed sweep drained 1,196 addresses (1,082.65 BTC, ~$70.2 million) in 41 minutes.
- **Status**: Actively exploited; flaw linked to large-scale theft events. Firmware updates issued but compromised seeds cannot be remediated—funds must be migrated to new wallets.
- **CVE ID**: No CVE ID provided in source articles.

### DarkSword Exploit Kit / GHOSTBLADE iOS Campaign
- **Description**: A Chinese-speaking threat actor leveraging a publicly leaked version of the DarkSword exploit kit to deploy GHOSTBLADE malware on Apple iOS devices.
- **Impact**: Compromise of iOS devices through exploit chain leveraging leaked kernel vulnerabilities; GHOSTBLADE provides persistent access and data exfiltration capabilities.
- **Status**: Active campaign observed; leverages leaked exploit kit code reducing barrier to entry for iOS exploitation.
- **CVE ID**: Specific CVEs not provided; exploits vulnerabilities present in DarkSword kit (likely older iOS kernel flaws).

### Deepseek AI Agent Proxyjacking Campaign
- **Description**: A Chinese threat actor weaponized a Deepseek AI agent to automate the compromise of over 1,200 hosts for proxyjacking—converting them into proxy infrastructure to launch further attacks.
- **Impact**: Large-scale infrastructure hijacking for anonymous attack launching; compromised hosts used as residential proxy nodes obscuring attacker origin.
- **Status**: Active campaign intercepted and investigated by researchers; demonstrates novel use of AI agents for autonomous vulnerability scanning and exploitation.
- **CVE ID**: No specific CVEs mentioned; likely leverages known vulnerabilities in exposed services.

### Adform Supply Chain Script Poisoning
- **Description**: Attackers compromised a JavaScript file served by advertising technology company Adform, modifying it to function as a browser-side tool that rewrites cryptocurrency wallet addresses on customer websites in real-time.
- **Impact**: Cryptocurrency theft via address substitution on any site loading the poisoned Adform script; supply chain impact across Adform's customer base.
- **Status**: Active incident detected by Adform; script modified to swap wallet addresses during user transactions.
- **CVE ID**: No CVE; supply chain compromise via third-party script modification.

### Fake Roblox Xeno Executor Malware Campaign
- **Description**: Fake installers for the popular Roblox script executor "Xeno" distributed through deceptive channels, infecting players (primarily younger users) with infostealer and remote access trojan (RAT) malware.
- **Impact**: Credential theft, system compromise, and remote access on victim machines; targets gaming community with high-value accounts and potential parental financial data.
- **Status**: Active distribution campaign; fake installers circulating on search results and community forums.
- **CVE ID**: No CVE; social engineering and trojanized software distribution.

### BTMOB Android RAT Ecosystem
- **Description**: Analysis of the BTMOB Android remote access trojan revealing a fragmented underground ecosystem of resellers, source-code vendors, custom versions, and subscription-based access.
- **Impact**: Commercialized mobile malware-as-a-service enabling low-skill actors to deploy capable RATs with features including SMS interception, call logging, location tracking, and remote control.
- **Status**: Active underground marketplace; multiple variants and resellers operating across Telegram and dark web forums.
- **CVE ID**: No CVE; malware-as-a-service distribution model.

### Rails Active Storage Critical Flaw
- **Description**: A critical vulnerability in the Rails Active Storage framework allowing unauthenticated attackers to read arbitrary files from the application server, with potential escalation to remote code execution (RCE).
- **Impact**: Arbitrary file read leading to source code exposure, configuration secret theft, and potential RCE on vulnerable Rails applications.
- **Status**: Patched by Rails maintainers; exploitation potential high for unpatched applications. Active exploitation status not explicitly confirmed in source.
- **CVE ID**: Specific CVE not provided in source article.

### Hugging Face Diffusers Arbitrary Code Execution
- **Description**: Three high-severity vulnerabilities in Hugging Face's Diffusers library that allow crafted model repositories to execute arbitrary code on machines that load the models.
- **Impact**: Supply chain compromise of AI/ML pipelines; arbitrary code execution when researchers or automated systems load malicious models from Hugging Face Hub.
- **Status**: Disclosed and patched; high severity due to widespread use of Diffusers in AI development workflows. Exploitation in wild not explicitly confirmed.
- **CVE ID**: Specific CVEs not provided in source article.

### Thermo Fisher Applied Biosystems Software Flaw
- **Description**: A flaw in select Applied Biosystems human identification software that could allow data files to be altered before analysis software loads them, making DNA file tampering nearly undetectable.
- **Impact**: Potential forensic evidence manipulation, wrongful conviction/acquittal risk, compromise of genetic database integrity.
- **Status**: Patched by Thermo Fisher Scientific in July 2026 release; no evidence of exploitation in wild reported.
- **CVE ID**: No CVE provided in source article.

## Affected Systems and Products

- **N-able N-central (Hosted and On-Premises)**: All versions prior to the corrected patch for CVE-2026-18577; both cloud-hosted and customer-deployed on-premises RMM servers affected. Initial patch was incomplete, requiring a second update.
- **SonicWall SMA 1000 Series VPN Appliances**: Secure Mobile Access 1000 series appliances; specific firmware versions not detailed in sources but recently disclosed flaws affect current deployments.
- **Google Password Manager (Windows)**: Passkey synchronization and authentication flow on Windows devices where Google Password Manager is used for passkey storage and auto-fill.
- **COLD Hardware Wallets (COLDCCARD)**: Devices running firmware with the flawed random number generator; specific firmware versions not enumerated but affects wallets whose seeds were generated using the vulnerable RNG.
- **Apple iOS Devices**: Devices vulnerable to exploits contained in the leaked DarkSword exploit kit; likely older iOS versions without patches for the kernel vulnerabilities leveraged by DarkSword.
- **Alibaba Cloud Developer Tools / npm Ecosystem**: Users of Alibaba developer tools who installed any of the 18 malicious npm packages; cross-platform impact (Windows, Linux, macOS) via the delivered RAT.
- **Rails Applications Using Active Storage**: Ruby on Rails applications utilizing the Active Storage framework on unpatched versions; critical severity with RCE potential.
- **Hugging Face Diffusers Library Users**: Any system loading models from Hugging Face Hub using vulnerable Diffusers library versions; affects AI/ML researchers, developers, and automated model deployment pipelines.
- **Thermo Fisher Applied Biosystems Human Identification Software**: Select software versions used in forensic and genetic analysis laboratories; patched in July 2026 release.
- **Adform Advertising Script Customers**: Any website embedding Adform's JavaScript advertising scripts during the compromise window; broad supply chain impact across Adform's publisher network.
- **Android Devices (BTMOB RAT)**: Android devices where users install trojanized applications from unofficial sources; BTMOB variants distributed through underground markets and reseller channels.
- **Roblox Players (Windows/macOS)**: Users downloading fake "Xeno Executor" installers; primarily younger demographic targeted through gaming community channels.
- **Hotel Wi-Fi Infrastructure / Guest Devices**: Hospitality network equipment compromised by Midnight Blizzard; guest devices (laptops, phones) connecting to compromised hotel Wi-Fi and targeted with custom malware for Microsoft 365 credential theft.
- **Police National Legal Database (PNLD) / UK Criminal Justice Systems**: PNLD database and associated systems breached by ExfilSquad, exposing contact data for 100,000+ police officers and criminal justice professionals.

## Attack Vectors and Techniques

- **Authentication Bypass on RMM Platforms**: Exploitation of CVE-2026-18577 in N-able N-central allowing unauthenticated administrative access, enabling supply chain compromise of MSP client environments.
- **Device Code Phishing (1,500% Increase)**: Abuse of OAuth device authorization flow to trick users into authorizing attacker-controlled applications, bypassing traditional credential phishing defenses and leaving minimal logs.
- **Vishing (Voice Phishing) - Doubled in 2026**: Telephone-based social engineering combined with technical pretexting to manipulate victims into performing actions that compromise credentials or install malware.
- **Hotel Wi-Fi Infrastructure Compromise**: Strategic compromise of hospitality network infrastructure to position custom malware for delivery to high-value targets (executives, government travelers) connecting to hotel Wi-Fi.
- **Pass-ta-key Attacks (Passkey Hijacking)**: Three techniques exploiting Google Password Manager's passkey sync on Windows: (1) silent authentication via background process, (2) abuse of sync protocol to extract usable credentials, (3) manipulation of local passkey store to bypass user verification requirements.
- **ClickFix with Browser Cache Steganography (DOUBLECUP)**: Social engineering (ClickFix) lures victims to pages that cache malicious PNG images; payload extracted from browser cache and executed, delivering CountLoader cross-platform.
- **Malicious npm Package Supply Chain**: Typosquatting/dependency confusion targeting Alibaba Cloud developer tool users; packages contain cross-platform RAT with persistence and data theft capabilities.
- **Hardware Wallet RNG Exploitation**: Mathematical attack on flawed random number generation in COLDCARD firmware allowing private key derivation and bulk wallet sweeping (1,196 addresses in 41 minutes).
- **Leaked Exploit Kit Repurposing (DarkSword → GHOSTBLADE)**: Chinese actor leveraging publicly leaked DarkSword iOS exploit kit to deploy custom GHOSTBLADE malware, lowering barrier for iOS exploitation.
- **AI Agent Autonomous Exploitation (Deepseek)**: Weaponization of an AI agent to autonomously scan, exploit, and enroll 1,200+ hosts into proxyjacking infrastructure for anonymous attack launching.
- **Third-Party Script Supply Chain Poisoning (Adform)**: Compromise of advertising technology provider's JavaScript delivery to inject wallet address rewriting logic across all customer sites loading the script.
- **Trojanized Software Distribution (Fake Xeno Executor)**: Social engineering via fake gaming utility installers distributed through search poisoning and community forums, delivering infostealer/RAT payloads.
- **Mobile Malware-as-a-Service (BTMOB Ecosystem)**: Fragmented reseller network providing customized Android RAT builds, subscription access, and source code licenses to low-skill operators.
- **Arbitrary File Read via Deserialization/Path Traversal (Rails Active Storage)**: Unauthenticated exploitation of Active Storage framework to read arbitrary server files, with chaining potential to RCE.
- **Malicious AI Model Repository Code Execution (Hugging Face Diffusers)**: Crafted model repositories exploiting deserialization/processing flaws in Diffusers library to achieve code execution on model load.
- **Forensic Data Integrity Subversion (Thermo Fisher)**: Pre-analysis manipulation of DNA data files exploiting software flaw to alter results undetectably.

## Threat Actor Activities

- **Midnight Blizzard (APT29)**: Russian state-sponsored actor conducting global hotel Wi-Fi compromise campaign targeting Microsoft 365 accounts of travelers; uses custom malware for stealthy credential theft and persistence. High-value targeting of executives, government officials, and corporate travelers.
- **INC Ransomware**: Emerged as dominant threat actor exploiting SonicWall SMA 1000 series VPN flaws; leveraging recently disclosed vulnerabilities for initial access, leading to ransomware deployment across multiple victim organizations.
- **ExfilSquad**: Hacker group responsible for breach of UK Police National Legal Database (PNLD), leaking contact information for over 100,000 police officers and criminal justice professionals on the dark web; data includes names, organizations, email addresses, and phone numbers.
- **Chinese-Speaking Threat Actor (DarkSword/GHOSTBLADE)**: Unknown Chinese-speaking group leveraging leaked DarkSword exploit kit to deploy GHOSTBLADE malware on iOS devices; demonstrates rapid weaponization of leaked exploit code for mobile targeting.
- **Chinese Threat Actor (Deepseek AI Agent)**: Chinese operator weaponizing a Deepseek AI agent to autonomously compromise 1,200+ hosts for proxyjacking infrastructure; novel use of AI for scalable vulnerability exploitation and operational anonymization.
- **DOUBLECUP Operators (Russian)**: Russian loader-as-a-service operators running ClickFix campaigns with browser cache steganography (PNG images) to deliver CountLoader cross-platform; commercial malware distribution model.
- **N-able N-central Attackers (Unattributed)**: Threat actors exploiting CVE-2026-18577 authentication bypass to gain administrative access to RMM servers and pivot to managed customer environments; persisted after initial vendor patch, indicating sophisticated capability.
- **Adform Script Poisoners (Unattributed)**: Attackers who compromised Adform's JavaScript delivery infrastructure to inject cryptocurrency wallet address rewriting code; supply chain attack targeting financial transactions across Adform's publisher network.
- **Malicious npm Publishers (Unattributed)**: Actors publishing 18 malicious packages targeting Alibaba Cloud developer tool users; sophisticated supply chain operation delivering cross-platform RAT with persistence.
- **COLDCCARD Wallet Thieves (Unattributed)**: Actors exploiting flawed RNG in hardware wallet firmware to conduct bulk Bitcoin theft (~$88.6M total, including $70.2M in single 41-minute sweep); mathematical exploitation of cryptographic weakness.
- **BTMOB Ecosystem Operators**: Fragmented network of source-code vendors, resellers, and custom-build providers commercializing Android RAT capabilities through underground markets (Telegram, dark web); enabling low-skill actor entry.
- **Fake Xeno Executor Distributors (Unattributed)**: Operators creating and distributing trojanized Roblox script executor installers through search poisoning and community channels; targeting younger gaming demographic for credential theft and system compromise.

## Source Attribution

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
- **⚡ Weekly Recap: Rogue AI Models, $88M Bitcoin Theft, Water-System Attacks and Dangling DNS Hijacks**: The Hacker News - https://thehackernews.com/2026/08/weekly-recap-rogue-ai-models-88m.html
- **Is There Really a Fix for CISO Fatigue?**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/fix-for-ciso-fatigue
- **FOMO in the SOC: Where AI Platforms like Claude Actually Fit**: The Hacker News - https://thehackernews.com/2026/08/fomo-in-soc-where-ai-platforms-like.html
- **Chinese Threat Actor Uses Leaked DarkSword Kit to Deploy GHOSTBLADE on iOS**: The Hacker News - https://thehackernews.com/2026/08/chinese-threat-actor-uses-leaked.html
- **PNLD Breach Exposes U.K. Police and Government Contact Details on Dark Web**: The Hacker News - https://thehackernews.com/2026/08/pnld-breach-exposes-uk-police-and.html
- **Thermo Fisher Patches Flaw That Could Make DNA File Tampering Nearly Undetectable**: The Hacker News - https://thehackernews.com/2026/08/thermo-fisher-patches-flaw-that-could.html
- **N-able Says Attackers Take Over N-central Servers After Initial Fix Proves Incomplete**: The Hacker News - https://thehackernews.com/2026/08/n-able-says-attackers-take-over-n.html
- **Hugging Face Diffusers Flaws Could Let Model Repositories Execute Arbitrary Code**: The Hacker News - https://thehackernews.com/2026/08/hugging-face-diffusers-flaws-could-let.html
- **OpenAI teases Astra, its next major AI model, after it solves 10 long-standing math problems**: Bleeping Computer - https://www.bleepingcomputer.com/news/artificial-intelligence/openai-teases-astra-its-next-major-ai-model-after-it-solves-10-long-standing-math-problems/
- **COLDCARD wallet RNG flaw likely linked to $88 million Bitcoin theft**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/coldcard-wallet-rng-flaw-likely-linked-to-88-million-bitcoin-theft/
- **Google Chrome may soon block New Tab hijacker extensions by default**: Bleeping Computer - https://www.bleepingcomputer.com/news/google/google-chrome-may-soon-block-new-tab-hijacker-extensions-by-default/
- **Coldcard Hardware Wallet Flaw Linked to $70 Million Bitcoin Theft in 41 Minutes**: The Hacker News - https://thehackernews.com/2026/08/coldcard-hardware-wallet-flaw-linked-to.html
- **Rails patches critical Active Storage flaw with RCE potential**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/rails-patches-critical-active-storage-flaw-with-rce-potential/
- **Hackers Poison Adform Script to Swap Crypto Wallet Addresses Across Customer Sites**: The Hacker News - https://thehackernews.com/2026/08/hackers-poison-adform-script-to-swap.html
