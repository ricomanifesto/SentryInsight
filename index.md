# Exploitation Report

## Executive Summary

Multiple critical exploitation campaigns are actively unfolding across diverse technology stacks, from managed service provider platforms to hardware wallets and supply chain infrastructure. The most severe ongoing incident involves the N-able N-central authentication bypass (CVE-2026-18577), where attackers have achieved full administrative control over both hosted and on-premises management servers, enabling downstream compromise of customer environments. An initial patch proved insufficient, and threat actors continue to leverage the flaw for remote takeover.

Simultaneously, a supply chain attack on advertising technology provider Adform has injected cryptocurrency-stealing code into JavaScript served across customer websites, while the INC Ransomware operation has established dominance in exploiting SonicWall SMA 1000 series VPN vulnerabilities. In the hardware security space, a random number generator flaw in COLDCARD firmware has been linked to the theft of approximately $88 million in Bitcoin across thousands of wallets. Chinese-speaking threat actors are conducting multiple campaigns: deploying the GHOSTBLADE implant on iOS via the leaked DarkSword exploit kit, targeting Central Asian governments with OctLurk and SilkLurk malware, and leveraging the DeepSeek AI model with the Hermes Agent for autonomous vulnerability scanning and exploitation.

## Active Exploitation Details

### N-able N-central Authentication Bypass (CVE-2026-18577)
- **Description**: An authentication bypass vulnerability affecting both hosted and on-premises N-central servers that allows unauthenticated attackers to gain remote administrative access to the management platform.
- **Impact**: Attackers achieve full administrative control over N-central servers, enabling them to reach and compromise all customer systems managed through those servers. This creates a cascading supply chain risk for managed service providers and their clients.
- **Status**: Actively exploited in the wild. N-able released an initial fix that proved incomplete; attackers continue to compromise servers post-patch. A supplemental fix is required.
- **CVE ID**: CVE-2026-18577

### SonicWall SMA 1000 Series VPN Flaws
- **Description**: Recently disclosed security vulnerabilities in SonicWall Secure Mobile Access (SMA) 1000 series appliances that allow remote attackers to compromise the VPN gateway.
- **Impact**: Full compromise of the VPN appliance, providing network access to internal resources, credential harvesting capabilities, and persistence mechanisms for follow-on ransomware deployment.
- **Status**: Actively exploited by INC Ransomware as their primary initial access vector. The group has emerged as the dominant threat actor leveraging these flaws.
- **CVE ID**: Not specified in source articles

### COLDCARD Hardware Wallet RNG Flaw
- **Description**: A firmware vulnerability in COLDCARD hardware wallets involving a flawed random number generator used during seed generation, resulting in predictable or weak entropy for private keys.
- **Impact**: Attackers can derive private keys for affected wallets and drain funds. Approximately $88.6 million in Bitcoin (1,082.65 BTC) was stolen from 1,196 addresses in a 41-minute automated sweep on July 30.
- **Status**: Actively exploited. The flaw affects wallets whose seeds were generated using the vulnerable firmware. No patch can recover stolen funds; affected users must migrate to new wallets.
- **CVE ID**: Not specified in source articles

### Adform Supply Chain Attack (Malicious JavaScript Injection)
- **Description**: Attackers compromised the JavaScript delivery infrastructure of advertising technology company Adform, modifying a served script to rewrite cryptocurrency wallet addresses in victims' clipboards.
- **Impact**: Any website using Adform's advertising platform inadvertently served the malicious script to visitors, causing cryptocurrency transactions to be redirected to attacker-controlled wallets. Broad reach across Adform's customer base.
- **Status**: Actively exploited until detected by Adform. The malicious script was active across customer sites and actively rewriting wallet addresses.
- **CVE ID**: Not specified in source articles

### GHOSTBLADE iOS Implant via DarkSword Exploit Kit
- **Description**: A Chinese-speaking threat actor is leveraging a publicly leaked version of the DarkSword exploit kit to deploy the GHOSTBLADE surveillance implant on Apple iOS devices.
- **Impact**: Full compromise of targeted iOS devices, enabling surveillance capabilities including data exfiltration, communications monitoring, and persistent access.
- **Status**: Active campaign observed. The use of a leaked exploit kit lowers the barrier to entry for this capability.
- **CVE ID**: Not specified in source articles

### DeepSeek AI Autonomous Attack Campaign
- **Description**: A Chinese-speaking threat actor is using the DeepSeek AI model combined with the open-source Hermes Agent to conduct fully autonomous cyberattacks against internet-exposed servers with minimal human involvement.
- **Impact**: Automated discovery, exploitation, and compromise of vulnerable servers at scale. Over 1,200 hosts targeted for proxyjacking to build infrastructure for further attacks.
- **Status**: Active operations observed by Unit 42 researchers. Represents a significant evolution in AI-assisted offensive operations.
- **CVE ID**: Not specified in source articles

### OctLurk and SilkLurk Campaign Against Central Asian Governments
- **Description**: A suspected Chinese-speaking threat actor deploying custom malware families OctLurk and SilkLurk against government organizations in Central Asia, including Afghanistan, Kyrgyzstan, and Tajikistan.
- **Impact**: Persistent access to government networks, intelligence collection, and potential lateral movement to connected systems.
- **Status**: Fresh wave of attacks observed. Attribution to Chinese-speaking actors based on tooling and infrastructure overlaps.
- **CVE ID**: Not specified in source articles

### Hotel Wi-Fi Fake Update Campaign (CornFlake RAT)
- **Description**: Attackers hijacking hotel Wi-Fi networks to serve fake browser updates that deliver the CornFlake remote access trojan.
- **Impact**: CornFlake captures webcam images, microphone audio, keystrokes, and provides full remote control of infected systems. Targets travelers using hotel networks.
- **Status**: Active campaign reported by Microsoft. Leverages trust in local network infrastructure and software update mechanisms.
- **CVE ID**: Not specified in source articles

### Rails Active Storage Critical Flaw
- **Description**: A critical vulnerability in the Active Storage framework of Ruby on Rails that allows unauthenticated attackers to read arbitrary files from the application server.
- **Impact**: Arbitrary file read with potential escalation to remote code execution (RCE). Affects Rails applications using Active Storage.
- **Status**: Patched by Rails maintainers. Exploitation potential is high given unauthenticated nature and RCE escalation path.
- **CVE ID**: Not specified in source articles

### Adobe Campaign Classic Maximum Severity Flaw
- **Description**: A CVSS 10.0 severity vulnerability in Adobe Campaign Classic (ACC) enterprise marketing automation platform allowing arbitrary code execution without user interaction.
- **Impact**: Unauthenticated remote code execution with no user interaction required. Critical for internet-exposed Campaign Classic instances.
- **Status**: Security updates released by Adobe. Actively exploitable pre-patch; patching urgency is maximum.
- **CVE ID**: Not specified in source articles

### Hugging Face Diffusers Arbitrary Code Execution
- **Description**: Three high-severity vulnerabilities in the Hugging Face Diffusers library that allow crafted model repositories to execute arbitrary code when loaded.
- **Impact**: Supply chain risk for AI/ML pipelines. Developers and systems loading malicious models from repositories achieve remote code execution on the loading machine.
- **Status**: Disclosed; patch status not specified in source. High risk for organizations using Diffusers in model loading workflows.
- **CVE ID**: Not specified in source articles

### PNLD / ExfilSquad Data Breach
- **Description**: Cyberattack on the UK Police National Legal Database (PNLD) resulting in exfiltration and publication of contact data for over 100,000 police officers and criminal justice professionals.
- **Impact**: Exposure of sensitive personal and professional contact information of law enforcement personnel, enabling targeted social engineering, harassment, and operational security risks.
- **Status**: Data published on dark web by ExfilSquad hacking group. Breach confirmed by PNLD.
- **CVE ID**: Not specified in source articles

### Google Password Manager Passkey Bypass
- **Description**: Malware running as an ordinary user on Windows can authenticate to passkey-protected accounts in Google Password Manager without requiring biometric verification, PIN, or any user-visible prompt.
- **Impact**: Bypasses the core security model of passkeys (user presence/verification). Any malware with user-level execution can hijack passkey-protected sessions silently.
- **Status**: Technique demonstrated by Unit 42 researchers. Represents a fundamental implementation weakness in the Windows/Google Password Manager integration.
- **CVE ID**: Not specified in source articles

### BTMOB Android RAT Ecosystem
- **Description**: The BTMOB Android remote access trojan has evolved into a fragmented underground marketplace with resellers, source code vendors, and custom versions.
- **Impact**: Commoditized mobile surveillance and data theft capabilities widely available to threat actors. Active development and distribution ecosystem.
- **Status**: Ongoing underground business analyzed by Flare researchers. Not a single campaign but a thriving malware-as-a-service operation.
- **CVE ID**: Not specified in source articles

### Amgen Cloud Data Breach
- **Description**: Pharmaceutical company Amgen suffered a data breach via third-party cloud service providers, exposing patient health information and proprietary corporate data.
- **Impact**: Compromise of protected health information (PHI) and intellectual property. Highlights supply chain risk in cloud service provider ecosystems.
- **Status**: Breach confirmed by Amgen. Investigation ongoing regarding scope and root cause within third-party systems.
- **CVE ID**: Not specified in source articles

### Arch Linux AUR Package Hijacking
- **Description**: Surge in malicious takeovers of Arch User Repository (AUR) packages, where attackers adopt orphaned or vulnerable packages and inject malicious code.
- **Impact**: Supply chain compromise for Arch Linux users installing community packages. Malicious code executes during package build/installation with user privileges.
- **Status**: Arch Linux project temporarily disabled AUR package adoption to stem the flood. Active abuse of the adoption mechanism observed.
- **CVE ID**: Not specified in source articles

### CISA Water Utility PLC Attacks
- **Description**: Significant increase in attacks targeting internet-exposed programmable logic controllers (PLCs) in water and wastewater treatment facilities.
- **Impact**: Potential disruption of critical water infrastructure, manipulation of treatment processes, and physical consequences for public health and safety.
- **Status**: CISA issuing active warnings. Attacks exploit default credentials, unpatched vulnerabilities, and direct internet exposure of OT devices.
- **CVE ID**: Not specified in source articles

### Thermo Fisher DNA Software Flaw
- **Description**: Vulnerability in Applied Biosystems human identification software that could allow alteration of DNA data files before analysis software loads them, making tampering nearly undetectable.
- **Impact**: Integrity compromise of forensic and human identification DNA analysis. Could affect criminal investigations, paternity testing, and medical diagnostics.
- **Status**: Patched by Thermo Fisher in July 2026 release. No evidence of active exploitation reported; classified as a potential integrity risk.
- **CVE ID**: Not specified in source articles

## Affected Systems and Products

- **N-able N-central**: Both hosted (SaaS) and on-premises server deployments. All versions prior to the supplemental patch for CVE-2026-18577.
- **SonicWall SMA 1000 Series**: Secure Mobile Access 1000 series VPN appliances. Specific vulnerable firmware versions not detailed in source.
- **COLD hardware wallets**: COLDCARD devices with firmware versions using the flawed RNG implementation during seed generation. Affected models include MK3 and MK4 per associated reporting.
- **Adform Advertising Platform**: JavaScript delivery infrastructure serving ads across customer websites. All customers loading Adform scripts during the compromise window.
- **Apple iOS Devices**: Targeted via DarkSword exploit kit deploying GHOSTBLADE implant. Specific iOS versions not detailed; likely affects multiple versions.
- **Ruby on Rails Applications**: Any application using Active Storage framework prior to the patched versions (7.1.3.4, 7.2.1.1, 8.0.0.1 per Rails advisory).
- **Adobe Campaign Classic (ACC)**: Enterprise marketing automation platform. On-premises and managed services deployments prior to August 2026 security update.
- **Hugging Face Diffusers Library**: Python library versions prior to the security fix. Affects any system loading models from untrusted or compromised repositories.
- **Google Password Manager on Windows**: Integration with Windows Hello / passkey infrastructure. Affects users relying on Google Password Manager for passkey storage on Windows.
- **Arch Linux AUR**: Arch User Repository packages adopted during the malicious takeover surge. Any user who installed compromised packages.
- **Programmable Logic Controllers (PLCs)**: Internet-exposed PLCs in water/wastewater utilities. Multiple vendors and models affected by poor network hygiene.
- **Applied Biosystems Software**: Thermo Fisher human identification software (HID Real-Time PCR Analysis Software, GeneMapper Software, etc.) prior to July 2026 patches.
- **Amgen Third-Party Cloud Systems**: Multiple unspecified cloud service providers hosting Amgen patient and corporate data.

## Attack Vectors and Techniques

- **Authentication Bypass**: CVE-2026-18577 in N-able N-central allows unauthenticated administrative access to management consoles, enabling downstream customer compromise.
- **VPN Appliance Exploitation**: Targeting known vulnerabilities in SonicWall SMA 1000 series for initial network access, credential theft, and ransomware deployment staging.
- **Supply Chain Code Injection**: Compromise of Adform's JavaScript delivery to inject cryptocurrency address-rewriting logic served to millions of website visitors.
- **Leaked Exploit Kit Utilization**: Publicly available DarkSword exploit kit repurposed by threat actors for iOS implant (GHOSTBLADE) deployment.
- **AI-Automated Offensive Operations**: DeepSeek LLM combined with Hermes Agent for autonomous target discovery, vulnerability scanning, exploitation, and proxy infrastructure deployment.
- **Custom Malware Deployment**: OctLurk and SilkLurk malware families used in targeted government intrusion campaigns with persistence and lateral movement capabilities.
- **Rogue Access Point / Network Hijacking**: Hotel Wi-Fi compromise to serve fake browser updates, leveraging trust in local network for social engineering delivery of CornFlake RAT.
- **Unauthenticated Arbitrary File Read**: Rails Active Storage flaw enabling file system access without authentication, with RCE escalation via deserialization gadget chains.
- **Zero-Click Remote Code Execution**: Adobe Campaign Classic CVSS 10.0 flaw allowing unauthenticated, no-interaction code execution on exposed servers.
- **Malicious Model Repository**: Crafted Hugging Face Diffusers model repositories that execute code upon loading, targeting AI/ML supply chains.
- **Passkey Verification Bypass**: Windows malware exploiting Google Password Manager's passkey implementation to silently authenticate without user presence verification.
- **Package Repository Hijacking**: Malicious adoption of AUR packages to inject build-time or install-time payloads executed by downstream users.
- **Cloud Service Provider Compromise**: Third-party cloud infrastructure breach leading to exfiltration of pharmaceutical patient data and proprietary information.
- **OT/ICS Direct Internet Exposure**: Attacks on PLCs with default credentials, unpatched firmware, and no network segmentation in water utility environments.
- **Hardware Entropy Failure**: COLDCARD RNG flaw producing predictable seeds, enabling mass private key derivation and automated wallet sweeping.
- **Data Extortion / Leak Operations**: ExfilSquad breach of PNLD with publication of 100,000+ law enforcement records on dark web for notoriety and pressure.

## Threat Actor Activities

- **INC Ransomware**: Dominant operator exploiting SonicWall SMA 1000 flaws for initial access. Conducting ransomware operations with VPN appliances as primary entry vector. High operational tempo and victim volume.
- **Chinese-Speaking Threat Actor (DeepSeek/GHOSTBLADE)**: Multiple linked campaigns: (1) DeepSeek AI + Hermes Agent for autonomous server compromise and proxyjacking (1,200+ hosts); (2) DarkSword exploit kit for GHOSTBLADE iOS implant deployment; (3) OctLurk/SilkLurk targeting Central Asian governments (Afghanistan, Kyrgyzstan, Tajikistan). Consistent tooling, infrastructure, and targeting suggest a single coordinated operator or closely affiliated groups.
- **ExfilSquad**: Hacking group responsible for PNLD breach and publication of 100,000+ UK police/criminal justice records on dark web. Motivation appears to be notoriety and data extortion.
- **Adform Supply Chain Attacker**: Unknown operator who compromised Adform's script delivery infrastructure. Financial motivation (cryptocurrency theft via address rewiping). Sophisticated supply chain access.
- **CornFlake RAT Operator**: Unknown threat actor hijacking hotel Wi-Fi networks to deliver surveillance malware via fake browser updates. Targeted travelers; capability includes webcam, microphone, keystroke capture.
- **BTMOB Ecosystem Operators**: Fragmented network of developers, resellers, source code vendors, and customizers operating an Android RAT malware-as-a-service marketplace. Not a single actor but a criminal ecosystem.
- **COLDCard Wallet Attacker**: Unknown actor(s) who executed automated sweep of 1,196 Bitcoin addresses in 41 minutes, exploiting RNG flaw to derive keys. Highly coordinated, financially motivated.
- **Water Utility PLC Attackers**: Multiple unspecified threat actors targeting internet-exposed PLCs in US water/wastewater sector. CISA notes significant activity increase; attribution not provided in source.

## Source Attribution

- **N-able warns of N-central auth bypass flaw exploited in attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/n-able-warns-of-n-central-auth-bypass-flaw-exploited-in-attacks/
- **Google Password Manager Attacks Could Let Malware Hijack Passkey-Protected Accounts**: The Hacker News - https://thehackernews.com/2026/08/google-password-manager-attacks-could.html
- **INC Ransomware Emerges as Dominant Actor Exploiting SonicWall SMA 1000 Flaws**: The Hacker News - https://thehackernews.com/2026/08/inc-ransomware-emerges-as-dominant.html
- **Chinese Actor Weaponizes DeepSeek AI Agent to Attack Security Firm**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/chinese-actor-deepseek-ai-agent-attack-security-firm
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
- **Hacker uses DeepSeek AI to autonomously attack vulnerable servers**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hacker-uses-deepseek-ai-to-autonomously-attack-vulnerable-servers/
- **CISA warns of cyberattacks disrupting U.S. water utilities**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-warns-of-cyberattacks-disrupting-us-water-utilities/
