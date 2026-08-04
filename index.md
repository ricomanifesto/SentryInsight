# Exploitation Report

## Executive Summary

Attackers are actively exploiting an authentication bypass vulnerability (CVE-2026-18577) in N-able N-central remote monitoring and management (RMM) servers, with the vendor confirming that an initial patch proved incomplete and threat actors have achieved full administrative control over both hosted and on-premises instances. This compromise enables lateral access to customer environments managed through these servers, representing a critical supply chain risk for managed service providers and their clients.

Simultaneously, multiple financially motivated and espionage-aligned campaigns are leveraging novel delivery techniques. A Russian loader-as-a-service dubbed DOUBLECUP uses ClickFix social engineering to hide malicious payloads in browser-cached PNG images, delivering the CountLoader implant across Windows and macOS. INC Ransomware has emerged as the dominant operator exploiting recently disclosed SonicWall SMA 1000 series VPN flaws, while a Chinese-speaking actor is weaponizing a leaked DarkSword exploit kit to deploy the GHOSTBLADE implant on iOS devices. Supply chain attacks continue to escalate, with 18 malicious npm packages targeting Alibaba Cloud developer tools, Adform's advertising JavaScript poisoned to swap cryptocurrency wallet addresses, and the Arch Linux AUR repository flooded with malicious package takeovers.

High-impact financial theft and data breaches round out the threat landscape. A random number generator flaw in COLDCARD hardware wallet firmware enabled the theft of approximately $70–88 million in Bitcoin across thousands of wallets in minutes. The ExfilSquad group breached the UK Police National Legal Database, exposing over 100,000 officers' and staff members' contact details. Meanwhile, hijacked hotel Wi-Fi networks are serving fake browser updates to deploy the CornFlake surveillance RAT, and Amgen disclosed a cloud data breach affecting patient health information and proprietary data via third-party service providers.

## Active Exploitation Details

### N-able N-central Authentication Bypass (CVE-2026-18577)
- **Description**: An authentication bypass vulnerability in N-able N-central RMM servers that allows unauthenticated attackers to gain administrator-level access. The flaw affects both hosted (cloud) and on-premises deployments. N-able's initial patch was incomplete, leaving servers exposed to continued exploitation.
- **Impact**: Attackers achieve remote administrative access to the N-central server, enabling them to reach and compromise all customer systems managed through that server. This creates a potent supply chain attack vector affecting managed service providers and their downstream clients.
- **Status**: Actively exploited in the wild. N-able has issued warnings and a subsequent fix after the initial patch proved insufficient. Customers are urged to apply the latest update immediately and audit for signs of compromise.
- **CVE ID**: CVE-2026-18577

### SonicWall SMA 1000 Series VPN Flaws
- **Description**: Recently disclosed security vulnerabilities in SonicWall Secure Mobile Access (SMA) 1000 series appliances. Specific CVE identifiers were not provided in the source articles.
- **Impact**: Exploitation provides remote access to VPN appliances, enabling network ingress, lateral movement, and ransomware deployment.
- **Status**: Actively exploited by INC Ransomware, which has emerged as the dominant threat actor leveraging these flaws. SonicWall has released patches; immediate application is critical.
- **CVE ID**: [CVE identifiers not specified in source articles]

### COLDCARD Hardware Wallet RNG Flaw
- **Description**: A firmware vulnerability in COLDCARD hardware wallets involving a flawed random number generator (RNG) used during seed generation. The weakness allows attackers to predict or derive private keys for wallets generated with affected firmware versions.
- **Impact**: Full compromise of Bitcoin wallets, enabling unauthorized withdrawal of funds. Two related incidents reported: one involving 1,196 addresses drained in 41 minutes (~$70.2 million / 1,082.65 BTC), and a broader campaign estimated at $88.6 million across thousands of wallets.
- **Status**: Actively exploited. Firmware updates available; users must migrate funds to wallets generated with patched firmware.
- **CVE ID**: [CVE identifier not specified in source articles]

### Google Password Manager Passkey Bypass
- **Description**: A design flaw in Google Password Manager on Windows that allows malware running with ordinary user privileges to authenticate to passkey-protected accounts without requiring user interaction (no fingerprint, PIN, or screen prompt).
- **Impact**: Malware can silently sign into any passkey-protected account stored in Google Password Manager, bypassing the primary security model of passkeys.
- **Status**: Demonstrated by Unit 42 researchers; exploitation feasibility confirmed. No patch mentioned in source articles; mitigation requires OS-level or browser-level controls.
- **CVE ID**: [CVE identifier not specified in source articles]

### Adobe Campaign Classic Critical RCE
- **Description**: A maximum-severity (CVSS 10.0) vulnerability in Adobe Campaign Classic (ACC) enterprise marketing automation platform that allows arbitrary code execution without user interaction.
- **Impact**: Unauthenticated remote code execution on the ACC server, potentially leading to full system compromise and access to customer marketing databases.
- **Status**: Adobe has released security updates. Active exploitation status not explicitly confirmed in source articles, but CVSS 10.0 warrants immediate patching.
- **CVE ID**: [CVE identifier not specified in source articles]

### Rails Active Storage File Read / RCE
- **Description**: A critical vulnerability in the Active Storage framework of Ruby on Rails that allows unauthenticated attackers to read arbitrary files from the application server, with potential escalation to remote code execution.
- **Impact**: Arbitrary file read (including source code, credentials, configuration) and potential RCE on vulnerable Rails applications.
- **Status**: Patched in recent Rails releases. Active exploitation not confirmed in source articles.
- **CVE ID**: [CVE identifier not specified in source articles]

### Hugging Face Diffusers Arbitrary Code Execution
- **Description**: Three high-severity flaws in Hugging Face's Diffusers library that allow crafted model repositories to execute arbitrary code when loaded by a victim's machine.
- **Impact**: Supply chain compromise via malicious AI/ML models; code execution on any system loading a poisoned model repository.
- **Status**: Disclosed and patched. Active exploitation not confirmed in source articles.
- **CVE ID**: [CVE identifiers not specified in source articles]

### Thermo Fisher Applied Biosystems Software Flaw
- **Description**: A vulnerability in select Applied Biosystems human identification software that could allow data files to be altered before analysis software loads them, making DNA file tampering nearly undetectable.
- **Impact**: Integrity compromise of forensic and human identification DNA analysis results.
- **Status**: Patched by Thermo Fisher Scientific in July 2026. Active exploitation not confirmed in source articles.
- **CVE ID**: [CVE identifier not specified in source articles]

## Affected Systems and Products

- **N-able N-central**: Both hosted (cloud) and on-premises RMM servers; all versions prior to the corrected patch for CVE-2026-18577
- **SonicWall SMA 1000 Series**: Secure Mobile Access 1000 series VPN appliances; specific firmware versions not detailed in source articles
- **COLDCard Hardware Wallets**: Devices running firmware with the flawed RNG implementation; specific firmware versions not detailed in source articles
- **Google Password Manager**: Windows implementation integrated with Chrome/Chromium browsers; passkey-protected accounts
- **Adobe Campaign Classic (ACC)**: Enterprise marketing automation platform; versions prior to the August 2026 security update
- **Ruby on Rails Active Storage**: Applications using Active Storage framework; versions prior to the patched releases
- **Hugging Face Diffusers Library**: Python library for diffusion models; versions prior to the patched release containing the three high-severity fixes
- **Thermo Fisher Applied Biosystems Software**: Select human identification software products; specific versions detailed in vendor advisory
- **Alibaba Cloud Developer Tools**: Users of the `@alibaba`/`@ali` npm package namespace targeted by 18 malicious packages
- **Arch Linux AUR (Arch User Repository)**: All packages subject to adoption; adoption mechanism temporarily disabled due to malicious takeovers
- **Adform Advertising Platform**: JavaScript files served by Adform's infrastructure; customers embedding Adform scripts on their sites
- **Hotel Wi-Fi Networks**: Compromised hospitality network infrastructure used to serve fake browser updates
- **Amgen Third-Party Cloud Systems**: Multiple cloud service providers operating systems storing Amgen corporate and patient data
- **UK Police National Legal Database (PNLD)**: Central database for police and criminal justice professional contact information
- **Windows and macOS Systems**: Targeted by DOUBLECUP ClickFix campaign delivering CountLoader
- **iOS Devices**: Targeted by Chinese actor using leaked DarkSword exploit kit to deploy GHOSTBLADE
- **Android Devices**: Targeted by BTMOB RAT malware ecosystem

## Attack Vectors and Techniques

- **Authentication Bypass (CVE-2026-18577)**: Unauthenticated attackers exploit incomplete patch in N-central to gain administrative access directly via the management interface.
- **ClickFix Social Engineering**: DOUBLECUP service tricks users into executing malicious commands (e.g., "fix" prompts) that load payloads from browser-cached PNG images, delivering CountLoader on Windows and macOS.
- **Malicious npm Packages (Supply Chain)**: 18 packages published to npm registry targeting Alibaba tool users, delivering a cross-platform RAT when installed by developers.
- **Fake Software Installers**: Trojanized Xeno Executor installers targeting Roblox players, distributing infostealer and RAT malware.
- **VPN Appliance Exploitation**: INC Ransomware leverages SonicWall SMA 1000 flaws for initial access, followed by ransomware deployment.
- **Leaked Exploit Kit Usage**: Chinese actor utilizes publicly leaked DarkSword kit to target iOS devices with GHOSTBLADE implant.
- **Proxyjacking via AI Agent**: Chinese actor weaponizes Deepseek AI agent to compromise 1,200+ hosts for proxy infrastructure to launch further attacks.
- **Passkey Authentication Bypass**: Malware on Windows exploits Google Password Manager design to silently authenticate passkey-protected accounts without user presence.
- **Advertising Script Poisoning (Supply Chain)**: Attackers modify Adform's served JavaScript to rewrite cryptocurrency wallet addresses on customer websites in real time.
- **Hardware Wallet RNG Exploitation**: Flawed entropy in COLDCARD firmware enables private key derivation and mass Bitcoin theft.
- **Fake Browser Updates via Compromised Wi-Fi**: Hijacked hotel networks serve fake update prompts delivering CornFlake RAT (webcam, microphone, keystroke capture).
- **Malicious AUR Package Adoption**: Attackers takeover orphaned or vulnerable Arch User Repository packages to inject malware into user builds.
- **Cloud Supply Chain Breach**: Threat actors compromise third-party cloud service providers to access Amgen's patient health data and proprietary information.
- **Database Exfiltration**: ExfilSquad breaches PNLD and publishes 100,000+ police and criminal justice professionals' contact details on dark web.
- **Android RAT Ecosystem (BTMOB)**: Fragmented underground marketplace of resellers, source-code vendors, and custom variants of BTMOB remote access trojan.

## Threat Actor Activities

- **INC Ransomware**: Dominant threat actor exploiting SonicWall SMA 1000 VPN flaws for initial access and ransomware deployment; identified as primary operator leveraging these vulnerabilities.
- **DOUBLECUP Operators**: Russian-speaking loader-as-a-service providers running ClickFix campaigns; deliver CountLoader via browser cache steganography (PNG images) to Windows and macOS.
- **ExfilSquad**: Hacking group responsible for breach of UK Police National Legal Database; leaked contact data of 100,000+ police officers and criminal justice staff on dark web.
- **Chinese Deepseek AI Actor**: Unknown Chinese-speaking group weaponizing Deepseek AI agent to compromise 1,200+ hosts for proxyjacking infrastructure.
- **Chinese DarkSword/GHOSTBLADE Actor**: Unknown Chinese-speaking actor leveraging leaked DarkSword exploit kit to deploy GHOSTBLADE malware on iOS devices.
- **Adform Script Poisoners**: Unidentified attackers who compromised Adform's JavaScript delivery infrastructure to inject crypto wallet address swapper.
- **COLDCard Wallet Attackers**: Unidentified actors exploiting RNG flaw to drain 1,196 Bitcoin addresses in 41 minutes (~$70M) and thousands more in broader campaign (~$88M).
- **Amgen Cloud Intruders**: Unidentified threat actors who accessed Amgen data via compromised third-party cloud service providers; stole patient health information and proprietary data.
- **BTMOB Ecosystem Operators**: Fragmented network of resellers, source-code vendors, and customizers maintaining and distributing the BTMOB Android RAT.
- **CornFlake RAT Operators**: Unidentified group using hijacked hotel Wi-Fi to deliver fake browser updates installing CornFlake surveillance malware (webcam, microphone, keylogging).
- **Malicious npm Publishers**: Unidentified actors publishing 18 packages targeting Alibaba Cloud developer ecosystem with cross-platform RAT.
- **Fake Xeno Executor Distributors**: Unidentified actors targeting Roblox players with trojanized script launchers delivering infostealer and RAT payloads.

## Source Attribution

- **Attackers Exploit N-able Patch Bypass Flaw on RMM Servers**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/attackers-exploit-n-able-patch-bypass-flaw
- **New Tool Traces AI Videos Back to Their Source**: Dark Reading - https://www.darkreading.com/cyber-risk/new-tool-advances-ai-generated-video-detection
- **Anthropic: AI Attacks Result of Security Gaps, Not Model Issues**: Dark Reading - https://www.darkreading.com/cyber-risk/anthropic-ai-issues-result-security-gaps
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
- **Amgen says cloud data breach exposed patient health, proprietary info**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/amgen-says-cloud-data-breach-exposed-patient-health-proprietary-info/
- **Arch Linux disables AUR package adoption to stop malware flood**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/arch-linux-disables-aur-package-adoption-to-stop-malware-flood/
