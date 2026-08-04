# Exploitation Report

## Executive Summary

Russian threat actor Midnight Blizzard (APT29) is conducting a global campaign compromising hotel Wi-Fi networks to deliver custom surveillance malware dubbed CornFlake, which captures webcam footage, microphone audio, and keystrokes while targeting Microsoft 365 credentials. Simultaneously, attackers are actively exploiting an authentication bypass vulnerability (CVE-2026-18577) in N-able N-central remote monitoring and management servers, with the vendor's initial patch proving incomplete and threat actors achieving full administrative control over managed customer environments.

Critical supply chain and identity attacks are escalating across multiple fronts. Researchers have uncovered three "Pass-ta-key" attack variants allowing malware on compromised Windows systems to hijack Google Password Manager's synced passkeys without any user interaction or visible prompts. A Russian loader-as-a-service called DOUBLECUP leverages ClickFix social engineering to hide malicious payloads in browser-cached PNG images, delivering the CountLoader payload cross-platform. Meanwhile, INC Ransomware has become the dominant operator exploiting recently disclosed SonicWall SMA 1000 series VPN flaws, and a Chinese-speaking actor is deploying the GHOSTBLADE implant on iOS devices using a leaked DarkSword exploit kit.

High-impact financial and infrastructure targeting continues with a COLDCARD hardware wallet firmware flaw in its random number generator linked to the theft of approximately $88 million in Bitcoin from thousands of wallets, executed in a 41-minute sweep of 1,196 addresses. The ExfilSquad group has leaked contact data for over 100,000 UK police officers and criminal justice professionals following a breach of the Police National Legal Database. Additional active threats include 18 malicious npm packages targeting Alibaba Cloud developer tools with a cross-platform RAT, Adobe Campaign Classic CVSS 10.0 remote code execution flaws, and three high-severity vulnerabilities in Hugging Face's Diffusers library enabling arbitrary code execution through crafted model repositories.

## Active Exploitation Details

### N-able N-central Authentication Bypass (CVE-2026-18577)
- **Description**: An authentication bypass vulnerability affecting both hosted and on-premises N-central servers that allows unauthenticated attackers to gain administrator access. The flaw resides in the patch management component and was initially addressed with an incomplete fix that attackers quickly bypassed.
- **Impact**: Attackers achieve full administrative control over N-central servers, enabling them to reach and compromise all customer systems managed through those servers. This provides a potent supply chain vector targeting managed service providers and their downstream clients.
- **Status**: Actively exploited in the wild. N-able has released a second patch after the initial fix proved insufficient. Organizations using N-central should apply the latest update immediately and audit for signs of compromise.
- **CVE ID**: CVE-2026-18577

### Hotel Wi-Fi CornFlake Campaign (Midnight Blizzard / APT29)
- **Description**: A global campaign compromising hospitality Wi-Fi networks to serve fake browser updates that deliver CornFlake, a remote access trojan with surveillance capabilities. The attack infrastructure is attributed to the Russian threat actor Midnight Blizzard (APT29).
- **Impact**: CornFlake captures webcam images, microphone audio, and keystrokes while targeting Microsoft 365 account credentials. Victims are typically travelers and hospitality sector personnel connecting to compromised hotel networks.
- **Status**: Active exploitation campaign ongoing. Microsoft has linked the activity to Midnight Blizzard. No specific CVE identified; the attack leverages network-level manipulation and social engineering rather than a software vulnerability in the traditional sense.

### Pass-ta-key Attacks on Google Password Manager
- **Description**: Three distinct attack techniques allowing malware running with ordinary user privileges on a compromised Windows device to abuse Google Password Manager's synced passkeys functionality. The attacks bypass user verification requirements (fingerprint, PIN, or screen prompts) entirely.
- **Impact**: Malware can silently sign into a victim's passkey-protected accounts across services without any user interaction or visible authentication prompts, effectively defeating the primary security model of passkey-based authentication.
- **Status**: Demonstrated by Unit 42 researchers as practical attacks against current Google Password Manager implementation on Windows. No patch available at time of reporting; mitigation requires architectural changes to passkey sync and verification flows.

### DOUBLECUP ClickFix Loader-as-a-Service
- **Description**: A Russian-operated loader-as-a-service that uses ClickFix social engineering tactics to trick users into executing malicious commands. The service hides payload code within PNG images cached by the victim's browser, delivering the CountLoader payload to both Windows and macOS systems.
- **Impact**: Cross-platform initial access and payload delivery capability sold as a service, lowering the barrier for operators to deploy follow-on malware including infostealers, RATs, and ransomware.
- **Status**: Active service offering in underground markets. Novel technique of steganographic payload storage in browser cache evades traditional file-based detection.

### INC Ransomware Exploitation of SonicWall SMA 1000
- **Description**: INC Ransomware operation actively exploiting recently disclosed security flaws in SonicWall Secure Mobile Access (SMA) 1000 series VPN appliances to gain initial access for ransomware deployment.
- **Impact**: Full network compromise via VPN appliance takeover, leading to data exfiltration and ransomware encryption across victim environments. INC has emerged as the dominant threat actor leveraging these flaws.
- **Status**: Active exploitation campaign. SonicWall has released patches for the underlying vulnerabilities; organizations running SMA 1000 series appliances should prioritize patching and hunt for indicators of compromise.

### GHOSTBLADE iOS Implant via Leaked DarkSword Kit
- **Description**: An unknown Chinese-speaking threat actor leveraging a publicly leaked version of the DarkSword exploit kit to deploy the GHOSTBLADE implant on Apple iOS devices.
- **Impact**: Persistent compromise of iOS devices enabling surveillance, data theft, and potential lateral movement. The use of a leaked exploit kit lowers attribution confidence and increases the threat surface.
- **Status**: Active campaign observed by attack surface management researchers. Apple has not issued a specific advisory at time of reporting; the DarkSword kit's public availability suggests broader misuse is likely.

### COLDCARD Hardware Wallet RNG Flaw
- **Description**: A firmware vulnerability in COLDCARD hardware wallets involving a flawed random number generator used for seed generation. The flaw allows attackers to predict or reconstruct wallet seeds, enabling unauthorized fund withdrawal.
- **Impact**: Estimated $88.6 million in Bitcoin stolen from thousands of wallets in a coordinated sweep of 1,196 addresses executed in approximately 41 minutes. The theft represents one of the largest hardware wallet compromises to date.
- **Status**: Actively exploited. COLDCARD has released firmware updates; users must migrate funds from affected wallets generated with vulnerable firmware versions. No CVE ID publicly assigned in available reporting.

### ExfilSquad PNLD Data Breach
- **Description**: Cyberattack on the UK Police National Legal Database (PNLD) resulting in the compromise and dark web publication of contact data for over 100,000 police officers and criminal justice professionals.
- **Impact**: Exposure of personally identifiable information including names, organizations, email addresses, and phone numbers of law enforcement personnel, creating risks for targeted harassment, social engineering, and operational security failures.
- **Status**: Data published on dark web. PNLD has confirmed the breach. Attribution to ExfilSquad group. No specific vulnerability CVE identified in public reporting.

### Malicious npm Package Campaign Targeting Alibaba Tools
- **Description**: Eighteen malicious npm packages targeting users of Alibaba Cloud developer tools, delivering a cross-platform remote access trojan (RAT) as part of a sophisticated supply chain operation.
- **Impact**: Developer machine compromise with full remote access capabilities, potentially leading to source code theft, CI/CD pipeline poisoning, and downstream software supply chain contamination.
- **Status**: Packages identified and reported. npm has removed the malicious packages; developers who installed them should rotate credentials and audit systems.

### Adobe Campaign Classic CVSS 10.0 Remote Code Execution
- **Description**: A maximum-severity (CVSS 10.0) security flaw in Adobe Campaign Classic (ACC), an enterprise marketing automation platform, allowing arbitrary code execution without user interaction.
- **Impact**: Unauthenticated remote code execution on ACC servers, potentially leading to full server compromise, customer data exposure, and lateral movement within enterprise environments.
- **Status**: Adobe has released security updates. No CVE ID provided in available reporting. Organizations running ACC should apply patches immediately.

### Hugging Face Diffusers Arbitrary Code Execution
- **Description**: Three high-severity vulnerabilities in Hugging Face's Diffusers library that allow crafted model repositories to execute arbitrary code on machines that load them.
- **Impact**: Supply chain compromise of AI/ML workflows; developers and researchers loading malicious models from Hugging Face Hub can suffer full system compromise.
- **Status**: Vulnerabilities disclosed; patches available in updated Diffusers library versions. No CVE IDs provided in available reporting.

### Rails Active Storage Critical Flaw
- **Description**: A critical vulnerability in the Active Storage framework of Ruby on Rails allowing unauthenticated attackers to read arbitrary files from Rails applications, with potential escalation to remote code execution.
- **Impact**: Data exposure and potential full application/server compromise for Rails applications using Active Storage without proper mitigations.
- **Status**: Rails has released patches. No CVE ID provided in available reporting.

### Adform Script Supply Chain Attack
- **Description**: Attackers compromised a JavaScript file served by advertising technology company Adform, modifying it to rewrite cryptocurrency wallet addresses in victims' browsers across customer sites.
- **Impact**: Financial theft via cryptocurrency transaction hijacking on any site loading the compromised Adform script. Broad impact across Adform's customer base.
- **Status**: Adform detected and remediated the incident. Attack demonstrates the risk of third-party script dependencies.

### Fake Roblox Xeno Executor Malware Campaign
- **Description**: Fake installers for the popular Roblox script executor "Xeno" distributed via search engine poisoning and social media, delivering infostealer and remote access trojan malware to primarily young gamers.
- **Impact**: Credential theft, system compromise, and potential parental financial data exposure on infected home systems.
- **Status**: Active distribution campaign. No specific vulnerability exploited; relies on social engineering and brand impersonation.

### BTMOB Android RAT Ecosystem
- **Description**: Analysis of the BTMOB Android remote access trojan revealing a fragmented underground ecosystem of resellers, source code vendors, and custom variants operating as a malware-as-a-service.
- **Impact**: Widespread Android device compromise enabling surveillance, data theft, and financial fraud. Low barrier to entry for operators due to service model.
- **Status**: Active underground marketplace. No specific vulnerability exploited; relies on social engineering for installation.

### Chinese Actor Deepseek AI Agent Proxyjacking
- **Description**: A Chinese threat actor weaponizing a Deepseek AI agent to automate the compromise of over 1,200 hosts for proxyjacking operations, enabling further attacks through the proxy network.
- **Impact**: Large-scale infrastructure hijacking for anonymous attack launching, credential stuffing, and traffic monetization.
- **Status**: Active campaign intercepted by researchers. Novel use of AI agent for autonomous vulnerability scanning and exploitation.

## Affected Systems and Products

- **N-able N-central (hosted and on-premises)**: All versions prior to the latest security update addressing CVE-2026-18577; both cloud-hosted and self-hosted deployments affected
- **SonicWall SMA 1000 series VPN appliances**: Versions with recently disclosed vulnerabilities; specific version details in SonicWall security advisories
- **Google Password Manager on Windows**: Systems with passkey sync enabled; affects Chrome and Edge browsers using Google Password Manager integration
- **COLDCARD hardware wallets**: Devices running firmware versions with the flawed random number generator; Mk3, Mk4, and Q models potentially affected
- **Adobe Campaign Classic (ACC)**: Enterprise deployments prior to the August 2026 security update release
- **Hugging Face Diffusers library**: Versions prior to the patched release containing fixes for the three high-severity flaws
- **Ruby on Rails Active Storage**: Rails applications using Active Storage prior to the patched versions (7.1.3.4, 7.2.1.1, 8.0.0.beta1 or later)
- **Alibaba Cloud developer tools / npm ecosystem**: Developers who installed any of the 18 identified malicious npm packages
- **Apple iOS devices**: Versions vulnerable to the DarkSword exploit kit components; specific versions not publicly detailed
- **UK Police National Legal Database (PNLD)**: Centralized database systems and associated web applications
- **Adform advertising script infrastructure**: All customer sites loading the compromised Adform JavaScript file during the incident window
- **Hotel Wi-Fi network infrastructure**: Hospitality network equipment and captive portal systems compromised to serve malicious updates
- **Android devices**: Devices where users sideloaded BTMOB RAT variants or fake applications
- **Windows and macOS systems**: Targets of DOUBLECUP ClickFix campaign delivering CountLoader via browser cache steganography

## Attack Vectors and Techniques

- **Network-Level Traffic Manipulation (Hotel Wi-Fi)**: Attackers compromise hotel network infrastructure to intercept HTTP/HTTPS traffic and inject fake browser update prompts, delivering CornFlake RAT via drive-by download
- **Authentication Bypass (CVE-2026-18577)**: Unauthenticated HTTP requests to N-central patch management endpoints manipulate session state to achieve administrative privileges without credentials
- **Passkey Sync Abuse (Pass-ta-key)**: Malware leverages Windows Hello and Google Password Manager IPC mechanisms to request passkey assertions without user presence verification, exploiting design gaps in cross-device sync architecture
- **ClickFix Social Engineering**: Users tricked into copying and executing malicious PowerShell commands via fake CAPTCHA, verification, or error pages; commands download and execute payloads
- **Browser Cache Steganography (DOUBLECUP)**: Malicious PNG images served to victims contain encoded payload data in pixel values; JavaScript extracts and reassembles the payload from cached image data
- **VPN Appliance Exploitation (SonicWall SMA 1000)**: Exploitation of authentication bypass and command injection flaws in SSL-VPN web interfaces for unauthenticated remote code execution
- **Leaked Exploit Kit Utilization (DarkSword)**: Publicly available iOS exploit chain components repurposed for GHOSTBLADE implant deployment, reducing operator development cost
- **Hardware Wallet Seed Prediction**: Cryptanalysis of flawed RNG output allows reconstruction of BIP-39 seed phrases, enabling deterministic wallet compromise at scale
- **Supply Chain Compromise (npm/Adform)**: Malicious code injected into legitimate distribution channels (npm registry, third-party CDN) to reach downstream consumers automatically
- **AI-Automated Vulnerability Scanning**: Deepseek AI agent autonomously identifies, exploits, and manages compromised hosts for proxy infrastructure
- **Brand Impersonation / SEO Poisoning**: Fake software installers (Xeno Executor) distributed via search manipulation and social media to target specific user communities
- **Third-Party Script Hijacking**: Compromise of advertising/analytics provider infrastructure to inject malicious JavaScript across thousands of customer sites simultaneously
- **Maximum-Severity RCE (Adobe Campaign Classic)**: Unauthenticated deserialization or template injection flaw allowing arbitrary code execution via crafted HTTP requests
- **Model Repository Code Execution (Hugging Face Diffusers)**: Malicious model configuration files trigger code execution during model loading through unsafe deserialization or plugin mechanisms
- **Arbitrary File Read to RCE (Rails Active Storage)**: Path traversal in blob key handling allows reading sensitive files; chained with deserialization gadgets for potential code execution

## Threat Actor Activities

- **Midnight Blizzard (APT29)**: Russian state-sponsored actor conducting global hotel Wi-Fi compromise campaign targeting travelers and hospitality sector for Microsoft 365 credential theft and surveillance via CornFlake RAT; demonstrates continued focus on identity and cloud service targeting
- **INC Ransomware**: Emerged as dominant ransomware operator exploiting SonicWall SMA 1000 VPN flaws; conducting rapid exploitation, data exfiltration, and encryption campaigns against organizations with unpatched appliances
- **ExfilSquad**: Hacktivist or criminal group responsible for PNLD breach and publication of 100,000+ UK law enforcement personnel records on dark web; politically motivated or opportunistic data theft
- **DOUBLECUP Operators**: Russian-speaking loader-as-a-service providers offering ClickFix delivery with browser cache steganography; selling CountLoader access to affiliate operators for follow-on payload deployment
- **Chinese-Speaking Actor (GHOSTBLADE/DarkSword)**: Unknown attribution Chinese-language operator leveraging leaked DarkSword iOS exploit kit for targeted surveillance campaigns; demonstrates proliferation of nation-state-grade exploit code
- **Alibaba npm Supply Chain Actor**: Sophisticated operator publishing 18 malicious packages over time targeting Alibaba Cloud developer ecosystem; likely espionage or software supply chain contamination objectives
- **COLDARD Wallet Attacker**: Unknown actor executing coordinated $88M Bitcoin sweep across 1,196 addresses in 41 minutes; demonstrates advanced cryptanalysis capability and operational security
- **Adform Script Compromise Actor**: Unknown actor who breached Adform's build or deployment pipeline to inject wallet-swapping JavaScript; financially motivated cryptocurrency theft at scale
- **BTMOB Ecosystem Operators**: Fragmented group of resellers, source code vendors, and custom variant developers operating Android RAT-as-a-service; low-skill operators enabled by commercial malware marketplace
- **Deepseek AI Agent Operator**: Chinese threat actor deploying autonomous AI agent for mass vulnerability exploitation and proxyjacking; represents evolution toward AI-driven offensive operations
- **Fake Xeno Executor Distributors**: Opportunistic actors targeting Roblox/gaming community via SEO poisoning and social media; financially motivated through infostealer and RAT deployment
- **Unknown Actors (Hugging Face / Rails / Adobe)**: No specific attribution in available reporting for actors exploiting the Hugging Face Diffusers, Rails Active Storage, or Adobe Campaign Classic vulnerabilities

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
