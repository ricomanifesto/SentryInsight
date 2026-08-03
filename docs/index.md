# Exploitation Report

## Executive Summary

This reporting period reveals a surge in supply chain compromises and hardware-level exploits with immediate financial impact. The most severe activity centers on a random number generator flaw in COLDCARD hardware wallets that enabled the theft of approximately $88 million in Bitcoin across thousands of wallets in a 41-minute automated sweep. Simultaneously, a supply chain attack against advertising technology provider Adform injected cryptocurrency-stealing scripts into customer websites, while attackers leveraged hijacked hotel Wi-Fi networks to deliver the CornFlake surveillance trojan through fake browser updates.

Critical infrastructure remains under sustained assault. CISA has warned of a significant increase in attacks targeting internet-exposed programmable logic controllers (PLCs) at U.S. water and wastewater utilities. In the managed services space, attackers exploited an authentication bypass in N-able N-central servers—persisting even after an initial vendor fix proved incomplete—to gain remote administrative access and pivot into customer environments. These incidents underscore the compounding risk of incomplete patches and exposed management interfaces.

Threat actor activity shows growing sophistication in automation and tooling. A Chinese-speaking operator is using the DeepSeek AI model paired with the open-source Hermes Agent to conduct autonomous vulnerability scanning and exploitation against exposed servers with minimal human intervention. Separately, a Chinese threat actor has weaponized a publicly leaked version of the DarkSword exploit kit to deploy GHOSTBLADE malware on iOS devices. Additional campaigns include suspected Chinese-speaking hackers targeting Central Asian governments with OctLurk and SilkLurk malware, and a spear-phishing operation deploying the novel HollowFrame loader and Matryoshka backdoor against a law firm.

## Active Exploitation Details

### COLDCARD Hardware Wallet RNG Flaw
- **Description**: A vulnerability in COLDCARD hardware wallet firmware's random number generator produced predictable seed values, allowing attackers to derive private keys and reconstruct wallet seeds. The flaw affected wallets whose seeds were generated using the flawed RNG implementation.
- **Impact**: Attackers drained 1,196 Bitcoin addresses in approximately 41 minutes on July 30, stealing 1,082.65 BTC valued at roughly $70.2 million at the time (approximately $88.6 million in broader estimates). Thousands of wallets were compromised in an automated sweep.
- **Status**: Actively exploited in the wild. The theft occurred on July 30, 2026. Galaxy Research mapped the transaction sweep and tied it directly to the firmware flaw.

### N-able N-central Authentication Bypass
- **Description**: An authentication bypass vulnerability in N-able's N-central remote monitoring and management (RMM) platform allowed unauthenticated attackers to gain administrative access to N-central servers.
- **Impact**: Attackers achieved remote administrative control over N-central servers and used that access to reach customer systems managed through those servers. The initial vendor fix was incomplete, allowing continued exploitation.
- **Status**: Actively exploited in the wild. N-able confirmed attackers took over N-central servers after the initial fix proved insufficient. A subsequent remediation was required.

### Adform Supply Chain Attack (Malicious JavaScript Injection)
- **Description**: Attackers compromised a JavaScript file served by advertising technology company Adform, modifying it to function as a browser-side tool that rewrites cryptocurrency wallet addresses copied to visitors' clipboards.
- **Impact**: The poisoned script swapped legitimate cryptocurrency wallet addresses with attacker-controlled addresses across all customer sites loading the Adform script, diverting cryptocurrency payments to threat actors.
- **Status**: Actively exploited. Adform detected the incident and confirmed the supply chain compromise. The malicious script was actively served to customer websites.

### Hotel Wi-Fi Fake Update / CornFlake RAT Deployment
- **Description**: Threat actors hijacked hotel Wi-Fi networks to intercept traffic and serve fake browser update prompts. Users who accepted the update downloaded CornFlake, a remote access trojan (RAT) capable of capturing webcam images, microphone audio, and keystrokes.
- **Impact**: Full surveillance capability on compromised devices, including audio/video capture and credential theft. Targets included travelers using hotel Wi-Fi networks.
- **Status**: Actively exploited in the wild. Microsoft reported the campaign and attributed the CornFlake RAT delivery to this vector.

### DarkSword Exploit Kit / GHOSTBLADE iOS Malware Campaign
- **Description**: An unknown Chinese threat actor leveraged a publicly leaked version of the DarkSword exploit kit to target Apple iOS devices, deploying the GHOSTBLADE malware framework.
- **Impact**: Compromise of iOS devices with GHOSTBLADE, a malware family designed for persistence and data exfiltration on Apple's mobile platform.
- **Status**: Actively exploited. The campaign was observed by attack surface management platforms leveraging the leaked exploit kit code.

### Arch Linux AUR Package Takeovers
- **Description**: Malicious actors conducted a surge of takeovers of existing Arch User Repository (AUR) packages, injecting malware into popular community-maintained packages.
- **Impact**: Users installing or updating compromised AUR packages executed malicious code on their systems. The Arch Linux project temporarily disabled package adoption to stem the flood.
- **Status**: Actively exploited. The surge in malicious takeovers prompted emergency action by the Arch Linux project.

### DeepSeek AI Autonomous Attack Campaign
- **Description**: A Chinese-speaking threat actor utilized the DeepSeek AI model in conjunction with the open-source Hermes Agent to conduct fully autonomous cyberattacks—scanning for vulnerable servers, exploiting them, and establishing persistence with minimal human intervention.
- **Impact**: Automated compromise of internet-exposed vulnerable servers at scale, reducing the time and skill required for widespread intrusion.
- **Status**: Actively exploited. The campaign represents a significant escalation in AI-assisted offensive operations.

### Water Utility PLC Attacks
- **Description**: Threat actors targeted internet-exposed programmable logic controllers (PLCs) in water and wastewater treatment facilities, disrupting operations.
- **Impact**: Operational disruption to critical water infrastructure. CISA warned of a significant increase in such attacks.
- **Status**: Actively exploited. CISA issued a formal warning regarding the rising threat to U.S. water utilities.

### HollowFrame Loader / Matryoshka Backdoor Spear-Phishing
- **Description**: A previously undocumented Go-based loader framework (HollowFrame) delivered a Rust-based malware family (Matryoshka) via spear-phishing emails targeting a law firm.
- **Impact**: Initial access and persistent backdoor deployment on legal sector targets, enabling data theft and lateral movement.
- **Status**: Actively exploited. Blackpoint Cyber researchers documented the campaign against a law firm.

### Android TV Box Identity Spoofing / Proxy Abuse
- **Description**: Cheap Android TV boxes shipped with pre-installed malicious applications that rewrite hardware identifiers to mimic legitimate phones (Samsung, Huawei, Xiaomi, Vivo), then use the device's broadband connection as a proxy for ad-click fraud.
- **Impact**: Device owners' broadband connections hijacked for fraudulent ad clicking; hardware identity spoofing enables evasion of device fingerprinting.
- **Status**: Actively exploited. Bitsight researchers identified the campaign across multiple device models.

### OctLurk / SilkLurk Campaign Against Central Asian Governments
- **Description**: A suspected Chinese-speaking threat actor deployed two malware families—OctLurk and SilkLurk—against government organizations primarily in Central Asia (Afghanistan, Kyrgyzstan, Tajikistan, and others).
- **Impact**: Espionage-focused compromise of government networks in the region, with custom tooling for persistence and data collection.
- **Status**: Actively exploited. The campaign represents a fresh wave of targeting against Central Asian government entities.

## Affected Systems and Products

- **COLDCARD Hardware Wallets**: Devices running firmware with the flawed RNG implementation; seeds generated using the vulnerable firmware versions are compromised.
- **N-able N-central**: RMM platform servers vulnerable to authentication bypass; all versions prior to the complete fix are affected. Customer environments managed through compromised N-central servers are at risk.
- **Adform Advertising Scripts**: JavaScript files served via Adform's ad delivery infrastructure; all customer websites embedding the compromised script were affected.
- **Hotel Wi-Fi Networks**: Compromised hospitality network infrastructure used to intercept and modify HTTP/HTTPS traffic for fake update injection.
- **Apple iOS Devices**: Targeted by GHOSTBLADE malware delivered via the leaked DarkSword exploit kit; specific iOS versions affected depend on the exploit kit's supported vulnerabilities.
- **Arch Linux AUR Packages**: Community-maintained packages in the Arch User Repository that were maliciously adopted and modified; users who installed or updated compromised packages.
- **Internet-Exposed Servers (Various)**: Targets of the DeepSeek/Hermes autonomous attack campaign; any server with unpatched vulnerabilities accessible from the internet.
- **Programmable Logic Controllers (PLCs)**: Internet-exposed PLCs in water and wastewater utility operational technology environments; specific vendors and models not disclosed in the advisory.
- **Law Firm Email/Endpoint Systems**: Targets of the HollowFrame/Matryoshka spear-phishing campaign; initial vector was malicious email attachments or links.
- **Cheap Android TV Boxes**: Specific low-cost models shipping with pre-installed malicious apps that spoof hardware identifiers (Samsung, Huawei, Xiaomi, Vivo) and operate as residential proxies.
- **Central Asian Government Networks**: Government organizations in Afghanistan, Kyrgyzstan, Tajikistan, and neighboring states targeted by OctLurk and SilkLurk malware.

## Attack Vectors and Techniques

- **Hardware Supply Chain / Firmware Flaw Exploitation**: Exploitation of a cryptographic RNG weakness in hardware wallet firmware to predict seed phrases and derive private keys at scale.
- **Authentication Bypass in Management Software**: Unauthenticated access to administrative interfaces of RMM platforms, enabling full control over managed customer environments.
- **Software Supply Chain Compromise (Third-Party JavaScript)**: Injection of malicious code into a widely embedded third-party advertising script, achieving broad distribution across customer websites.
- **Network Traffic Interception / Man-in-the-Middle (Hotel Wi-Fi)**: Hijacking of local network infrastructure to modify HTTP responses and inject fake software update prompts.
- **Leaked Exploit Kit Weaponization**: Adaptation of publicly leaked exploit kit code (DarkSword) for targeted malware deployment (GHOSTBLADE) against mobile platforms.
- **Package Repository Poisoning (AUR)**: Malicious adoption of legitimate community packages to inject payloads into the software supply chain of end users.
- **AI-Automated Vulnerability Exploitation**: Use of large language models (DeepSeek) combined with agent frameworks (Hermes) to autonomously discover, exploit, and persist on vulnerable servers.
- **OT/ICS Targeting (Exposed PLCs)**: Direct targeting of internet-connected industrial control systems in critical infrastructure sectors.
- **Spear-Phishing with Novel Loader/Backdoor**: Social engineering delivery of a custom Go-based loader (HollowFrame) deploying a Rust-based backdoor (Matryoshka).
- **Device Identity Spoofing / Residential Proxy Abuse**: Malicious firmware/apps rewriting hardware identifiers to masquerade as legitimate mobile devices and monetize broadband as proxy exit nodes.
- **Custom Malware Deployment for Espionage (OctLurk/SilkLurk)**: Use of previously undocumented malware families for targeted government espionage in a specific geographic region.

## Threat Actor Activities

- **Unknown Operator (COLDCard Bitcoin Theft)**: Executed an automated sweep of 1,196 Bitcoin addresses in 41 minutes, leveraging the RNG flaw to derive keys and drain ~1,082 BTC. Demonstrates high-capability cryptocurrency-focused actor with automated tooling.
- **Unknown Operator (N-able N-central Exploitation)**: Actively exploited authentication bypass post-patch, indicating monitoring of vendor advisories and rapid reverse-engineering of incomplete fixes. Targeted MSP supply chain for downstream customer access.
- **Unknown Operator (Adform Supply Chain)**: Compromised Adform's script delivery infrastructure to inject clipboard-hijacking code. Financially motivated, targeting cryptocurrency transactions across a broad victim set.
- **Unknown Operator (Hotel Wi-Fi / CornFlake)**: Deployed surveillance malware (CornFlake RAT) via fake updates on compromised hospitality networks. Capabilities include webcam, microphone, and keystroke capture—consistent with targeted espionage.
- **Chinese Threat Actor (DarkSword/GHOSTBLADE)**: Leveraged leaked DarkSword exploit kit to deploy GHOSTBLADE on iOS. Demonstrates rapid weaponization of public exploit code for mobile platform targeting.
- **Malicious AUR Package Maintainers (Multiple Actors)**: Coordinated surge in malicious package adoptions, suggesting either a single group automating takeovers or multiple opportunistic actors exploiting weak package ownership controls.
- **Chinese-Speaking Threat Actor (DeepSeek/Hermes)**: Pioneering fully autonomous AI-driven attack chains using DeepSeek LLM and Hermes Agent for vulnerability discovery, exploitation, and post-exploitation with minimal human oversight.
- **Unknown Actors (Water Utility PLC Targeting)**: Increased activity against exposed OT assets in water sector. CISA advisory suggests multiple actors or broad opportunistic scanning.
- **Unknown Operator (HollowFrame/Matryoshka)**: Deployed novel Go/Rust toolchain via spear-phishing against legal sector. Custom loader and backdoor indicate dedicated development resources and targeted intent.
- **Device Manufacturers/Supply Chain Actors (Android TV Boxes)**: Pre-installation of identity-spoofing proxy malware on consumer devices. Blurs line between supply chain compromise and malicious product design.
- **Suspected Chinese-Speaking Actor (OctLurk/SilkLurk)**: Espionage campaign against Central Asian governments using two custom malware families. Regional focus and tooling suggest state-aligned or state-sponsored operation.

## Source Attribution

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
- **Hacker uses DeepSeek AI to autonomously attack vulnerable servers**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hacker-uses-deepseek-ai-to-autonomously-attack-vulnerable-servers/
- **CISA warns of cyberattacks disrupting U.S. water utilities**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-warns-of-cyberattacks-disrupting-us-water-utilities/
- **HollowFrame Loader Deploys Matryoshka Backdoor in Spear-Phishing Attack on Law Firm**: The Hacker News - https://thehackernews.com/2026/07/hollowframe-loader-deploys-matryoshka.html
- **Cheap Android TV Boxes Pose as Phones and Turn Owners’ Broadband Into Proxies**: The Hacker News - https://thehackernews.com/2026/07/cheap-android-tv-boxes-pose-as-phones.html
- **ESET tracks rise in malicious AI skills and adaptable malware**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/eset-tracks-rise-in-malicious-ai-skills-and-adaptable-malware/
- **The Morning After We Pull a Root of Trust, Nobody Owns It**: Dark Reading - https://www.darkreading.com/cyber-risk/morning-after-we-pull-root-of-trust-nobody-owns-it
- **Interpol Leverages Global System to Curtail Fraud Payments**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/interpol-leverages-global-system-curtail-fraud-payments
- **DROP Platform Lets Californians Reduce Digital Footprint**: Dark Reading - https://www.darkreading.com/data-privacy/drop-platform-lets-californians-ditch-their-data
