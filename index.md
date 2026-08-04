# Exploitation Report

## Executive Summary

Russian state-sponsored threat actor Midnight Blizzard (APT29) is conducting a global campaign targeting hospitality Wi-Fi networks, deploying custom malware including the CornFlake remote access trojan through fake browser updates to breach Microsoft 365 accounts. This operation demonstrates sophisticated infrastructure compromise enabling surveillance capabilities such as webcam capture, microphone recording, and keystroke logging across international hotel networks.

A critical authentication bypass vulnerability (CVE-2026-18577) in N-able N-central RMM servers is being actively exploited by attackers to gain administrative access and pivot to managed customer environments. N-able's initial patch proved incomplete, allowing continued compromise of both hosted and on-premises servers. Simultaneously, INC Ransomware has emerged as the dominant threat actor exploiting recently disclosed SonicWall SMA 1000 series VPN flaws, while a Chinese-speaking actor leverages the leaked DarkSword exploit kit to deploy GHOSTBLADE malware on iOS devices.

New attack vectors targeting authentication mechanisms are proliferating: researchers identified three "Pass-ta-key" techniques allowing malware to hijack Google-synced passkeys without user interaction, a Russian loader-as-a-service (DOUBLECUP) uses ClickFix social engineering to hide malicious code in browser-cached PNG images, and a COLDCARD hardware wallet RNG flaw facilitated the theft of approximately $88 million in Bitcoin. Supply chain attacks continue with 18 malicious npm packages targeting Alibaba tool users, Adform script poisoning rewriting cryptocurrency wallet addresses, and three high-severity flaws in Hugging Face Diffusers enabling arbitrary code execution through crafted model repositories.

## Active Exploitation Details

### Midnight Blizzard Hotel Wi-Fi Campaign
- **Description**: Russian APT29 (Midnight Blizzard) compromises hotel Wi-Fi infrastructure to serve fake browser updates that deliver CornFlake RAT malware. The malware provides comprehensive surveillance capabilities including webcam access, microphone recording, and keystroke logging.
- **Impact**: Full compromise of Microsoft 365 accounts, persistent surveillance of high-value targets traveling internationally, credential theft, and lateral movement within victim organizations.
- **Status**: Active global campaign. Microsoft has attributed and disclosed the operation. No specific patch for hotel Wi-Fi infrastructure compromise; mitigation requires network monitoring and user awareness against fake updates.
- **CVE ID**: Not explicitly assigned to the Wi-Fi compromise vector itself

### N-able N-central Authentication Bypass (CVE-2026-18577)
- **Description**: An authentication bypass vulnerability in N-able N-central remote monitoring and management (RMM) software allows unauthenticated attackers to gain administrative access to both hosted and on-premises N-central servers.
- **Impact**: Attackers achieve remote administrative control over RMM servers, enabling access to all customer systems managed through those servers. This provides a potent supply chain vector for downstream compromise.
- **Status**: Actively exploited in the wild. N-able released an initial patch that proved incomplete; attackers continued exploitation after the first fix. A subsequent updated patch has been issued.
- **CVE ID**: CVE-2026-18577

### INC Ransomware Exploitation of SonicWall SMA 1000 Flaws
- **Description**: INC Ransomware operation actively exploits recently disclosed security vulnerabilities in SonicWall Secure Mobile Access (SMA) 1000 series VPN appliances to gain initial access for ransomware deployment.
- **Impact**: Network intrusion, data exfiltration, ransomware encryption, and operational disruption for organizations using affected SonicWall VPN appliances.
- **Status**: INC Ransomware identified as the "dominant threat actor" exploiting these flaws. Active exploitation ongoing. SonicWall has released patches for the underlying vulnerabilities.
- **CVE ID**: Specific CVE IDs for the SonicWall SMA 1000 flaws not provided in source articles

### Pass-ta-key Attacks on Google Password Manager
- **Description**: Three distinct attack techniques allow malware running as an ordinary user on a compromised Windows device to abuse Google Password Manager's synced passkeys, bypassing user verification (fingerprint, PIN, or screen prompts) to sign into passkey-protected accounts.
- **Impact**: Complete bypass of passkey authentication protections, enabling account takeover of any service using Google-synced passkeys without victim interaction or awareness.
- **Status**: Demonstrated by Unit 42 researchers. Google has been notified. Mitigation requires Google Password Manager architectural changes.
- **CVE ID**: Not explicitly assigned in source articles

### DOUBLECUP ClickFix Loader-as-a-Service
- **Description**: Russian-operated loader-as-a-service using ClickFix social engineering to trick users into executing malicious code. Malware hides in PNG images cached by victims' browsers, delivering CountLoader payload to both Windows and macOS devices.
- **Impact**: Cross-platform initial access, payload delivery evasion through browser cache steganography, persistent foothold for follow-on exploitation.
- **Status**: Active service offered in underground markets. Novel browser cache-based payload staging technique.
- **CVE ID**: Not applicable (service/malware, not a software vulnerability)

### COLDCARD Hardware Wallet RNG Flaw
- **Description**: A vulnerability in COLDCARD hardware wallet firmware's random number generator allows attackers to predict or reconstruct wallet seeds, enabling theft of Bitcoin from wallets generated with the flawed firmware.
- **Impact**: Estimated $88.6 million in Bitcoin stolen from thousands of wallets. One incident drained 1,196 addresses (1,082.65 BTC, ~$70.2 million) in 41 minutes.
- **Status**: Actively exploited. Firmware flaw identified and linked to thefts. COLDCARD has addressed the RNG issue in updated firmware.
- **CVE ID**: Not explicitly assigned in source articles

### SonicWall SMA 1000 Series VPN Vulnerabilities
- **Description**: Recently disclosed security flaws in SonicWall Secure Mobile Access (SMA) 1000 series VPN appliances being exploited for initial access.
- **Impact**: Unauthenticated remote access to internal networks, bypass of VPN authentication, foothold for ransomware deployment (INC Ransomware).
- **Status**: Actively exploited by INC Ransomware as dominant actor. Patches available from SonicWall.
- **CVE ID**: Specific CVE IDs not provided in source articles

### DarkSword Exploit Kit / GHOSTBLADE iOS Campaign
- **Description**: Chinese-speaking threat actor leverages publicly leaked DarkSword exploit kit to deploy GHOSTBLADE malware on Apple iOS devices.
- **Impact**: Compromise of iOS devices, potential persistent access, data exfiltration, and use of compromised devices for proxyjacking and further attacks.
- **Status**: Active campaign observed. Leverages leaked exploit kit code, lowering barrier to entry for iOS exploitation.
- **CVE ID**: Specific CVEs targeted by DarkSword kit not enumerated in source articles

### Adobe Campaign Classic Critical Flaw
- **Description**: Maximum-severity (CVSS 10.0) security flaw in Adobe Campaign Classic (ACC) enterprise marketing automation platform allowing arbitrary code execution without user interaction.
- **Impact**: Unauthenticated remote code execution on ACC servers, full server compromise, potential access to customer marketing data and connected systems.
- **Status**: Adobe has released security updates. Exploitation potential is critical given CVSS 10.0 rating and no user interaction requirement.
- **CVE ID**: Not explicitly provided in source articles

### Rails Active Storage Critical Vulnerability
- **Description**: Critical vulnerability in Rails Active Storage framework allowing unauthenticated attackers to read arbitrary files, with potential escalation to remote code execution.
- **Impact**: File read leading to information disclosure, configuration theft, and potential RCE on Rails applications using Active Storage.
- **Status**: Rails has patched the vulnerability. Applications must update to mitigate.
- **CVE ID**: Not explicitly provided in source articles

### Hugging Face Diffusers Arbitrary Code Execution Flaws
- **Description**: Three high-severity vulnerabilities in Hugging Face's Diffusers library that allow crafted model repositories to execute arbitrary code when loaded.
- **Impact**: Supply chain compromise through malicious AI models, arbitrary code execution on systems loading poisoned models, potential compromise of ML pipelines and inference infrastructure.
- **Status**: Disclosed and patched. Users must update Diffusers library.
- **CVE ID**: Specific CVE IDs not provided in source articles

### Thermo Fisher Applied Biosystems Software Flaw
- **Description**: Flaw in select Applied Biosystems human identification software allowing data files to be altered before analysis software loads them, making DNA file tampering nearly undetectable.
- **Impact**: Integrity compromise of forensic and genetic analysis data, potential miscarriages of justice, undetectable evidence tampering.
- **Status**: Patched by Thermo Fisher Scientific in July 2026 release.
- **CVE ID**: Not explicitly provided in source articles

## Affected Systems and Products

- **N-able N-central**: Both hosted (cloud) and on-premises deployments of the RMM platform. All versions prior to the corrected patch for CVE-2026-18577.
- **SonicWall SMA 1000 Series**: Secure Mobile Access VPN appliances (specific affected firmware versions not detailed in sources). Enterprise VPN gateways.
- **Google Password Manager**: Windows clients with synced passkeys enabled. Affects any service using Google-synced passkeys for authentication.
- **COLDCCARD Hardware Wallets**: Devices running firmware with the flawed RNG implementation. Specific firmware versions not enumerated in sources.
- **Hotel Wi-Fi Infrastructure**: Compromised hospitality network equipment (routers, access points, captive portal systems) used to inject fake updates.
- **Adobe Campaign Classic (ACC)**: Enterprise marketing automation platform deployments. All unpatched versions vulnerable to CVSS 10.0 RCE.
- **Rails Applications with Active Storage**: Ruby on Rails applications using the Active Storage framework for file uploads. Unpatched versions.
- **Hugging Face Diffusers Library**: Python environments with vulnerable Diffusers versions installed. ML model hosting and inference platforms.
- **Thermo Fisher Applied Biosystems Software**: Select human identification software versions prior to July 2026 patch. Forensic and genetic analysis labs.
- **Adform Ad Serving Infrastructure**: JavaScript delivery infrastructure compromised to serve malicious wallet-swapping code. Adform customer websites loading the poisoned script.
- **npm Registry / Alibaba Developer Tools**: 18 malicious packages targeting users of Alibaba Cloud development tooling. Cross-platform (Windows, Linux, macOS).
- **Apple iOS Devices**: Targeted by GHOSTBLADE malware delivered via DarkSword exploit kit. Specific iOS versions not detailed.
- **Android Devices**: BTMOB RAT malware ecosystem targeting Android platform through various distribution channels.

## Attack Vectors and Techniques

- **Compromised Network Infrastructure / Evil Twin / Rogue AP**: Attackers gain control of legitimate hotel Wi-Fi infrastructure to serve malicious content (fake browser updates) to high-value targets. No user deception beyond trusting the hotel network.
- **Fake Browser Update Social Engineering**: Malicious JavaScript/HTML served over compromised networks mimics legitimate browser update prompts, tricking users into downloading and executing CornFlake RAT.
- **ClickFix Social Engineering**: DOUBLECUP service uses fake CAPTCHA/verification pages that instruct victims to copy-paste PowerShell commands, executing malware downloaders.
- **Browser Cache Steganography / Payload Staging**: DOUBLECUP hides malicious code in PNG images cached by the browser, retrieving and executing payloads from the local cache to evade network inspection.
- **Authentication Bypass (CVE-2026-18577)**: Unauthenticated attackers exploit flawed authentication logic in N-central to achieve administrative access without credentials.
- **VPN Appliance Exploitation**: INC Ransomware exploits vulnerabilities in SonicWall SMA 1000 series for unauthenticated remote network access.
- **Passkey Synchronization Abuse (Pass-ta-key)**: Three techniques exploit Google Password Manager's cross-device passkey sync: (1) abusing the sync protocol to register attacker-controlled authenticators, (2) manipulating local passkey database to bypass user verification, (3) exploiting Windows Hello integration gaps.
- **Supply Chain / Malicious Package Injection**: 18 typosquatted/obfuscated npm packages targeting Alibaba tool users deliver cross-platform RAT. Adform script poisoning modifies third-party JavaScript to rewrite crypto wallet addresses client-side.
- **AI/ML Model Supply Chain Attack**: Crafted Hugging Face Diffusers model repositories exploit deserialization/code execution flaws when loaded by victim pipelines.
- **Hardware RNG Subversion**: COLDCARD firmware flaw produces predictable entropy, allowing seed reconstruction and wallet draining without physical device access.
- **Leaked Exploit Kit Utilization**: Chinese actor uses publicly leaked DarkSword kit (originally for iOS) to deploy GHOSTBLADE, demonstrating commodity iOS exploitation.
- **RMM-as-Attack-Platform**: Compromised N-central servers used to push malicious scripts, deploy ransomware, or access managed customer endpoints at scale.
- **DNS / Dangling Subdomain Hijacking**: Referenced in weekly recap as active technique for subdomain takeover and credential harvesting.

## Threat Actor Activities

- **Midnight Blizzard (APT29)**: Russian state-sponsored actor conducting global hotel Wi-Fi compromise campaign targeting travelers for Microsoft 365 credential theft and surveillance. High operational security, custom malware (CornFlake), infrastructure compromise focus.
- **INC Ransomware**: Dominant ransomware operation exploiting SonicWall SMA 1000 VPN flaws for initial access. Rapid weaponization of disclosed vulnerabilities. Ransomware deployment, data theft, extortion.
- **DOUBLECUP Operators**: Russian-speaking group operating loader-as-a-service (CountLoader delivery). ClickFix social engineering, browser cache steganography, cross-platform (Windows/macOS). Service model suggests affiliate/customer structure.
- **ExfilSquad**: Hacktivist/cybercriminal group claiming breach of UK Police National Legal Database (PNLD). Leaked contact data of 100,000+ police officers and criminal justice professionals on dark web. Politically motivated or notoriety-seeking.
- **Chinese Deepseek AI Actor**: Chinese-speaking threat actor weaponizing Deepseek AI agent to attack a security firm. Compromised 1,200+ hosts for proxyjacking infrastructure. Novel AI-assisted offensive operations.
- **Chinese DarkSword/GHOSTBLADE Actor**: Unknown Chinese-speaking actor leveraging leaked DarkSword exploit kit for iOS targeting. Deploys GHOSTBLADE malware. Opportunistic use of leaked offensive tools.
- **BTMOB RAT Ecosystem**: Fragmented Android malware operation involving source-code vendors, resellers, custom version developers. Commercialized RAT distribution with modular capabilities.
- **Malicious npm Package Authors**: Unknown actors publishing 18 packages targeting Alibaba Cloud developer toolchain users. Cross-platform RAT delivery. Supply chain focus.
- **Adform Script Poisoners**: Unknown actors who compromised Adform's JavaScript delivery infrastructure to inject crypto wallet address swapping code. Financially motivated, targeting cryptocurrency users across Adform's customer base.
- **COLDCCARD Wallet Thieves**: Unknown actors exploiting RNG flaw to drain Bitcoin wallets. Highly automated, rapid execution (41 minutes for 1,196 addresses). Sophisticated understanding of wallet seed generation flaws.

## Source Attribution

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
- **Adobe Campaign Classic CVSS 10.0 Flaw Could Run Code Without User Interaction**: The Hacker News - https://thehackernews.com/2026/08/adobe-campaign-classic-cvss-100-flaw.html
- **Hijacked Hotel Wi-Fi Pushes Fake Updates to Deliver Surveillance Malware**: The Hacker News - https://thehackernews.com/2026/08/hijacked-hotel-wi-fi-pushes-fake.html
