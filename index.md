# Exploitation Report

## Executive Summary

Active exploitation campaigns are intensifying across multiple vectors, with threat actors targeting critical infrastructure, supply chains, and identity systems. The most severe ongoing activity involves the N-able N-central authentication bypass (CVE-2026-18577), where attackers have achieved full administrative control over managed service provider servers and their downstream customer environments after an initial vendor patch proved incomplete. Simultaneously, INC Ransomware has established dominance exploiting recently disclosed SonicWall SMA 1000 series VPN flaws, while a Chinese-speaking actor leverages the leaked DarkSword exploit kit to deploy GHOSTBLADE malware on iOS devices.

Supply chain compromise remains a prolific vector: malicious npm packages targeting Alibaba developer tools, a poisoned Adform advertising script rewriting cryptocurrency wallet addresses across customer sites, and malicious Arch Linux AUR packages have all delivered remote access trojans and infostealers. Hotel Wi-Fi hijacking campaigns are serving fake browser updates to install the CornFlake surveillance RAT, and fake Roblox "Xeno Executor" installers continue ensnaring younger users with information-stealing malware. A flaw in COLDCARD hardware wallet firmware has been linked to the theft of approximately $70–88 million in Bitcoin, demonstrating the catastrophic impact of cryptographic implementation failures.

Threat actors are diversifying their tooling and targeting. Chinese-speaking groups are conducting espionage against Central Asian governments using OctLurk and SilkLurk, weaponizing AI agents for proxyjacking at scale, and exploiting the PNLD breach to expose over 100,000 UK police and criminal justice professionals' data. The BTMOB Android RAT has evolved into a fragmented underground marketplace of resellers and custom variants. Meanwhile, critical vulnerabilities in Adobe Campaign Classic (CVSS 10.0), Rails Active Storage, and Hugging Face Diffusers present imminent exploitation risk despite patches being available.

## Active Exploitation Details

### N-able N-central Authentication Bypass (CVE-2026-18577)
- **Description**: An authentication bypass vulnerability affecting both hosted and on-premises N-central servers that allows unauthenticated attackers to gain administrative access.
- **Impact**: Attackers achieve remote administrative control over N-central servers and can pivot to all customer systems managed through those servers, enabling widespread downstream compromise.
- **Status**: Actively exploited in the wild. N-able released an initial fix that proved incomplete; attackers continued compromising servers after the patch. A supplemental fix is required.
- **CVE ID**: CVE-2026-18577

### SonicWall SMA 1000 Series VPN Vulnerabilities
- **Description**: Recently disclosed security flaws in SonicWall Secure Mobile Access (SMA) 1000 series appliances.
- **Impact**: Provides initial access for ransomware deployment. INC Ransomware has emerged as the dominant threat actor exploiting these flaws for network intrusion and encryption.
- **Status**: Actively exploited by INC Ransomware operation. Patches available from SonicWall.

### DarkSword Exploit Kit / GHOSTBLADE iOS Malware
- **Description**: A publicly leaked version of the DarkSword exploit kit is being used by an unknown Chinese-speaking threat actor to deploy GHOSTBLADE malware on Apple iOS devices.
- **Impact**: Compromise of iOS devices for surveillance, data exfiltration, and potential further network pivoting.
- **Status**: Active campaign observed leveraging the leaked exploit kit. No patch information provided in source.

### COLDCARD Hardware Wallet RNG Flaw
- **Description**: A vulnerability in COLDCARD hardware wallet firmware involving a flawed random number generator used for seed generation.
- **Impact**: Attackers can derive private keys and drain Bitcoin wallets. Linked to theft of approximately 1,082–1,196 BTC (valued at $70–88.6 million) from thousands of wallets in a 41-minute sweeping attack.
- **Status**: Actively exploited. Firmware updates required.

### Adobe Campaign Classic Critical Flaw
- **Description**: A maximum-severity (CVSS 10.0) security flaw in Adobe Campaign Classic (ACC) enterprise marketing automation platform.
- **Impact**: Arbitrary code execution without user interaction, enabling full server compromise.
- **Status**: Security updates released by Adobe. Exploitation likelihood high given severity.

### Rails Active Storage Vulnerability
- **Description**: Critical vulnerability in the Active Storage framework allowing unauthenticated attackers to read arbitrary files from Rails applications.
- **Impact**: Arbitrary file read with potential escalation to remote code execution (RCE).
- **Status**: Patched by Rails maintainers. Exploitation potential significant for unpatched applications.

### Hugging Face Diffusers Library Flaws
- **Description**: Three high-severity security flaws in Hugging Face's Diffusers library that allow crafted model repositories to execute arbitrary code when loaded.
- **Impact**: Supply chain compromise via malicious ML models; arbitrary code execution on systems loading poisoned models.
- **Status**: Disclosed; patch status not specified in source.

### Google Password Manager Passkey Bypass
- **Description**: Malware running as an ordinary user on Windows can sign into victim's passkey-protected accounts without fingerprint, PIN, or any user-visible prompt.
- **Impact**: Bypass of passkey authentication, account takeover without user interaction.
- **Status**: Research by Unit 42 demonstrates feasibility. Mitigation status unclear.

## Affected Systems and Products

- **N-able N-central**: Both hosted and on-premises server versions affected by CVE-2026-18577; downstream customer environments managed through compromised servers also impacted.
- **SonicWall SMA 1000 Series**: Secure Mobile Access VPN appliances (specific versions not detailed in source).
- **Apple iOS**: Devices targeted via DarkSword exploit kit delivering GHOSTBLADE malware.
- **COLDCARD Hardware Wallets**: Firmware versions with flawed RNG implementation; thousands of wallets compromised.
- **Adobe Campaign Classic (ACC)**: Enterprise marketing automation platform; all unpatched versions vulnerable to CVSS 10.0 flaw.
- **Ruby on Rails Applications**: Applications using Active Storage framework; unpatched versions vulnerable to arbitrary file read and potential RCE.
- **Hugging Face Diffusers Library**: Systems loading model repositories from untrusted sources; three high-severity flaws identified.
- **Windows Systems with Google Password Manager**: Passkey-protected accounts vulnerable to silent sign-in by local malware.
- **Alibaba Developer Tools Users**: Developers installing npm packages from the compromised supply chain (18 malicious packages identified).
- **Adform Advertising Platform Customers**: Websites serving Adform's compromised JavaScript file; visitors' cryptocurrency wallet addresses rewritten.
- **Arch Linux AUR**: Arch User Repository packages; malicious takeovers of existing packages surged, prompting temporary disablement of package adoption.
- **Hotel Wi-Fi Networks**: Compromised networks serving fake browser updates to deliver CornFlake RAT.
- **Roblox Players**: Users downloading fake "Xeno Executor" script launchers; infected with infostealer and RAT malware.
- **Android Devices**: BTMOB RAT malware ecosystem targeting Android; fragmented reseller and custom variant marketplace.
- **Thermo Fisher Applied Biosystems Software**: Human identification software with flaw allowing nearly undetectable DNA file tampering (patched July 2026).
- **PNLD (Police National Legal Database)**: UK police and criminal justice database; contact data of 100,000+ officers and staff exposed.
- **Amgen Cloud Systems**: Third-party cloud service providers hosting patient health data and proprietary information; data breach confirmed.
- **Central Asian Government Networks**: Government organizations in Afghanistan, Kyrgyzstan, Tajikistan, and surrounding regions targeted with OctLurk and SilkLurk malware.

## Attack Vectors and Techniques

- **Authentication Bypass**: CVE-2026-18577 allows unauthenticated administrative access to N-central servers; initial vendor patch was incomplete, enabling continued exploitation.
- **VPN Appliance Exploitation**: INC Ransomware leveraging recently disclosed SonicWall SMA 1000 flaws for initial network access.
- **Leaked Exploit Kit Utilization**: Chinese-speaking actor using publicly leaked DarkSword kit to deploy GHOSTBLADE on iOS, lowering barrier to entry for sophisticated mobile exploitation.
- **Supply Chain Compromise (npm)**: 18 malicious npm packages targeting Alibaba developer tools users, delivering cross-platform RAT.
- **Supply Chain Compromise (Advertising Script)**: Attackers modified Adform's JavaScript file to rewrite cryptocurrency wallet addresses in visitors' clipboards across customer sites.
- **Supply Chain Compromise (AUR Packages)**: Malicious takeovers of existing Arch Linux AUR packages; surge in malware-laden packages prompted temporary adoption freeze.
- **Hardware Wallet Cryptographic Flaw**: Flawed RNG in COLDCARD firmware enabled private key derivation and mass Bitcoin theft (~$70–88M in 41 minutes).
- **Fake Software Updates**: Hijacked hotel Wi-Fi serves fake browser updates delivering CornFlake RAT (webcam, microphone, keystroke capture).
- **Typosquatting/Brand Impersonation**: Fake "Xeno Executor" Roblox script launchers distributed to gamers, installing infostealer and RAT malware.
- **Passkey Authentication Bypass**: Local malware on Windows silently authenticates to passkey-protected accounts via Google Password Manager without user prompts.
- **Malicious ML Model Repositories**: Crafted Hugging Face Diffusers model repositories execute arbitrary code when loaded by victims.
- **AI-Agent Weaponization**: Chinese actor using Deepseek AI agent to scan and compromise 1,200+ hosts for proxyjacking and further attacks.
- **Ransomware Deployment via VPN Flaws**: INC Ransomware establishing dominance in exploiting SonicWall SMA 1000 for encryption and extortion.
- **Arbitrary File Read to RCE**: Rails Active Storage flaw allows unauthenticated file read with potential escalation to remote code execution.
- **Zero-Click Code Execution**: Adobe Campaign Classic CVSS 10.0 flaw enables arbitrary code execution without user interaction.

## Threat Actor Activities

- **INC Ransomware**: Emerged as "dominant threat actor" exploiting SonicWall SMA 1000 VPN flaws for initial access, deployment, and extortion.
- **Chinese-Speaking Threat Actor (DarkSword/GHOSTBLADE)**: Unknown Chinese-speaking group leveraging leaked DarkSword exploit kit to deploy GHOSTBLADE on iOS devices; active campaign observed.
- **Chinese-Speaking Threat Actor (Deepseek AI)**: Actor weaponizing Deepseek AI agent to compromise 1,200+ hosts for proxyjacking and further attacks; intercepted by Jesta researchers.
- **Chinese-Speaking Threat Actor (OctLurk/SilkLurk)**: Suspected Chinese-speaking hackers targeting Central Asian governments (Afghanistan, Kyrgyzstan, Tajikistan, etc.) with OctLurk and SilkLurk malware.
- **ExfilSquad**: Hackers breached UK Police National Legal Database (PNLD), leaking contact data of 100,000+ police officers and criminal justice professionals on dark web.
- **BTMOB RAT Operators**: Fragmented underground ecosystem of resellers, source-code vendors, and custom version creators for Android BTMOB RAT; analyzed by Flare researchers.
- **Adform Supply Chain Attackers**: Unknown actors compromised Adform's JavaScript delivery infrastructure to inject cryptocurrency wallet address-swapping code.
- **Hotel Wi-Fi Compromise Actors**: Unknown group hijacking hotel Wi-Fi to serve fake browser updates delivering CornFlake surveillance RAT; reported by Microsoft.
- **Fake Xeno Executor Distributors**: Threat actors targeting Roblox players with fake script launchers delivering infostealer and RAT malware.
- **COLDCard Wallet Attackers**: Unknown actors exploiting RNG flaw to sweep ~1,196 Bitcoin addresses in 41 minutes, stealing $70–88.6M.
- **Amgen Cloud Intruders**: Threat actors stole corporate data and patient information from multiple third-party cloud service providers used by Amgen.
- **Malicious npm Package Publishers**: Actors publishing 18 malicious packages targeting Alibaba developer tools users with cross-platform RAT.
- **AUR Package Hijackers**: Actors taking over existing Arch Linux AUR packages to inject malware; surge prompted project-wide adoption freeze.

## Source Attribution

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
- **Online ad firm Adform’s script compromised to steal cryptocurrency**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/online-ad-firm-adforms-script-compromised-to-steal-cryptocurrency/
- **OpenAI says its new GPT 5.6 models are becoming more cost-efficient**: Bleeping Computer - https://www.bleepingcomputer.com/news/artificial-intelligence/openai-says-its-new-gpt-56-models-are-becoming-more-cost-efficient/
- **Suspected Chinese-Speaking Hackers Target Central Asian Governments With OctLurk and SilkLurk**: The Hacker News - https://thehackernews.com/2026/08/suspected-chinese-speaking-hackers.html
- **CISA Issues Fresh SBOM Guidance. Did They Get It Right?**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/cisa-issues-fresh-sbom-guidance
