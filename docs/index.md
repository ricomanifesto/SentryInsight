# Exploitation Report

## Executive Summary

A critical firmware vulnerability in COLDCARD hardware wallets has been actively exploited to steal approximately $70–88 million in Bitcoin, with attackers draining over 1,000 wallets in just 41 minutes. The flaw resides in the wallet's random number generator, allowing threat actors to predict or reconstruct seed phrases and seize funds at scale. This incident represents one of the largest hardware wallet compromises to date and underscores the catastrophic impact of cryptographic implementation failures in custody solutions.

Simultaneously, multiple supply-chain and infrastructure attacks have emerged. A compromise of Adform's advertising JavaScript delivery infrastructure enabled attackers to inject cryptocurrency wallet address-swapping code across customer websites, demonstrating the reach of third-party script poisoning. In a separate campaign, hijacked hotel Wi-Fi networks served fake browser updates deploying the CornFlake remote access trojan, which captures webcam footage, microphone audio, and keystrokes. CISA has also warned of escalating attacks against internet-exposed programmable logic controllers in U.S. water and wastewater utilities, signaling persistent targeting of critical infrastructure.

Threat actor activity shows growing sophistication in AI-assisted operations. Chinese-speaking actors are leveraging the DeepSeek AI model through the open-source Hermes Agent framework to conduct autonomous vulnerability scanning and exploitation against exposed servers, with initial commands issued via Telegram. Meanwhile, suspected Chinese-speaking hackers are deploying previously undocumented malware families—OctLurk and SilkLurk—against government entities across Central Asia. A novel Go-based loader (HollowFrame) and Rust-based backdoor (Matryoshka) were observed in a spear-phishing campaign targeting a law firm, highlighting continued innovation in post-exploitation tooling.

## Active Exploitation Details

### COLDCARD Hardware Wallet RNG Flaw
- **Description**: A vulnerability in COLDCARD hardware wallet firmware's random number generator allows attackers to predict or reconstruct wallet seed phrases. The flaw affects wallets whose seeds were generated using the flawed RNG implementation.
- **Impact**: Attackers can derive private keys and drain Bitcoin from affected wallets. Over 1,196 addresses were compromised in a single 41-minute operation, resulting in theft of approximately 1,082.65 BTC (valued at $70.2–88.6 million).
- **Status**: Actively exploited in the wild. The vulnerability was used in a large-scale sweep on July 30. Firmware updates and mitigation guidance are expected from the vendor.

### Adobe Campaign Classic Arbitrary Code Execution
- **Description**: A maximum-severity (CVSS 10.0) security flaw in Adobe Campaign Classic (ACC), Adobe's enterprise marketing automation platform, allows unauthenticated remote code execution without user interaction.
- **Impact**: Attackers can execute arbitrary code on affected ACC instances, potentially leading to full system compromise, data exfiltration, and lateral movement within enterprise environments.
- **Status**: Adobe has released security updates addressing the vulnerability. Organizations running ACC should apply patches immediately.

### Rails Active Storage Arbitrary File Read and Potential RCE
- **Description**: A critical vulnerability in the Active Storage framework of Ruby on Rails allows unauthenticated attackers to read arbitrary files from the application server.
- **Impact**: Attackers can access sensitive files including configuration files, credentials, and source code. Under certain conditions, the vulnerability can escalate to remote code execution.
- **Status**: Rails has released patches for the vulnerability. Applications using Active Storage should upgrade to patched versions immediately.

### Adform Supply-Chain Script Compromise
- **Description**: Attackers modified a JavaScript file served by advertising technology company Adform, injecting code that rewrites cryptocurrency wallet addresses in users' clipboards to attacker-controlled addresses.
- **Impact**: Visitors to websites using Adform's ad platform who copy cryptocurrency wallet addresses have them silently replaced, causing funds to be sent to attackers. The compromise affected multiple customer sites simultaneously.
- **Status**: Adform detected the incident and remediated the compromised script. The attack demonstrates the systemic risk of third-party JavaScript dependencies.

### CornFlake RAT Deployment via Hijacked Hotel Wi-Fi
- **Description**: Threat actors compromised hotel Wi-Fi infrastructure to serve fake browser update prompts that deliver the CornFlake remote access trojan.
- **Impact**: CornFlake provides comprehensive surveillance capabilities including webcam image capture, microphone audio recording, and keystroke logging. Victims are typically travelers connecting to compromised hotel networks.
- **Status**: Active campaign observed by Microsoft. No specific patch exists; mitigation relies on network verification and user awareness against fake update prompts.

### 4G/5G Core Network Vulnerabilities
- **Description**: Researchers disclosed a widespread class of 84 security vulnerabilities impacting 4G and 5G core networks, including a session hijacking flaw.
- **Impact**: Successful exploitation could trigger denial-of-service attacks, enable session hijacking, and allow evasion of security controls in mobile core infrastructure.
- **Status**: Vulnerabilities disclosed to relevant standards bodies and vendors. Patching status varies across telecommunications providers.

## Affected Systems and Products

- **COLDCARD Hardware Wallets**: Firmware versions with flawed RNG implementation used for seed generation. Specific affected firmware versions not disclosed in reporting.
- **Adobe Campaign Classic (ACC)**: Enterprise marketing automation platform. All unpatched versions vulnerable to CVSS 10.0 RCE flaw.
- **Ruby on Rails Active Storage**: Applications using Active Storage framework prior to patched releases. Vulnerable to unauthenticated arbitrary file read and potential RCE.
- **Adform Advertising Platform**: JavaScript delivery infrastructure compromised to serve malicious wallet-swapping code. All customer sites loading Adform scripts during compromise window affected.
- **Hotel Wi-Fi Networks**: Compromised infrastructure at unidentified hotels serving fake browser updates. Affects travelers connecting to compromised networks.
- **Programmable Logic Controllers (PLCs)**: Internet-exposed PLCs in U.S. water and wastewater utility systems. Targeted in ongoing campaigns reported by CISA.
- **4G/5G Core Network Equipment**: Telecommunications core infrastructure from multiple vendors affected by the 84 disclosed vulnerabilities.
- **Android TV Boxes**: Cheap devices shipping with pre-installed apps that rewrite hardware identity to mimic phones and generate fraudulent ad clicks. Specific device models not fully enumerated.

## Attack Vectors and Techniques

- **Cryptographic Implementation Flaw Exploitation**: Attackers exploited a flawed random number generator in hardware wallet firmware to reconstruct seed phrases and derive private keys, enabling mass wallet drainage.
- **Supply-Chain JavaScript Poisoning**: Compromise of a third-party advertising script delivery mechanism allowed injection of malicious code across thousands of downstream websites simultaneously, targeting cryptocurrency clipboard operations.
- **Malicious Captive Portal / Fake Update Delivery**: Hijacked hotel Wi-Fi infrastructure used to intercept HTTP traffic and serve fake browser update prompts, delivering a full-featured surveillance RAT (CornFlake).
- **AI-Automated Vulnerability Scanning and Exploitation**: Chinese-speaking threat actors leverage DeepSeek AI model through the Hermes Agent framework to autonomously identify and exploit vulnerable internet-exposed servers with minimal human intervention.
- **Spear-Phishing with Novel Loader/Backdoor Chain**: Go-based HollowFrame loader delivers Rust-based Matryoshka backdoor via targeted phishing emails, demonstrating modern cross-language malware tooling.
- **Device Code Phishing (OAuth 2.0 Device Authorization Grant Abuse)**: Industrial-scale abuse of the OAuth device flow to steal access tokens without traditional credential harvesting, identified as fastest-growing threat vector.
- **Internet-Exposed PLC Targeting**: Direct targeting of programmable logic controllers in critical infrastructure (water/wastewater) accessible via the internet, enabling operational disruption.
- **AUR Package Takeover**: Malicious actors adopting orphaned or vulnerable Arch User Repository packages to inject malware into the software supply chain for Arch Linux users.
- **Mobile Core Protocol Exploitation**: Exploitation of vulnerabilities in 4G/5G core network protocols (NAS, GTP, HTTP/2) for session hijacking and denial-of-service.

## Threat Actor Activities

- **Chinese-Speaking Threat Actor (DeepSeek/Hermes Campaign)**: Using DeepSeek AI model via Telegram commands to drive the open-source Hermes Agent for autonomous scanning and exploitation of vulnerable servers. Activity attributed by Palo Alto Networks Unit 42. Demonstrates operationalization of LLMs for offensive cyber operations.
- **Chinese-Speaking Threat Actor (OctLurk/SilkLurk Campaign)**: Deploying previously undocumented malware families OctLurk and SilkLurk against government organizations in Central Asia (Afghanistan, Kyrgyzstan, Tajikistan, and surrounding regions). Suspected Chinese origin based on language artifacts and targeting patterns.
- **Unknown Operator (COLDRAIN/COLDCARD Sweep)**: Executed highly coordinated drainage of 1,196 Bitcoin addresses in 41 minutes, netting ~1,082 BTC. Technical sophistication suggests deep understanding of the RNG flaw and automated sweeping infrastructure. Attribution unknown.
- **Unknown Operator (Adform Supply-Chain Compromise)**: Compromised Adform's script delivery infrastructure to inject cryptocurrency wallet address-swapping code. Motivation: financial theft via clipboard hijacking. Attribution unknown.
- **Unknown Operator (CornFlake Hotel Wi-Fi Campaign)**: Compromised hotel Wi-Fi networks to deliver CornFlake RAT via fake browser updates. Surveillance-focused malware suggests espionage motivation. Microsoft tracking but attribution not publicly assigned.
- **HollowFrame/Matryoshka Operator**: Conducted spear-phishing campaign against a law firm using novel Go-based loader (HollowFrame) and Rust-based backdoor (Matryoshka). Tooling previously undocumented. Attribution unknown; analyzed by Blackpoint Cyber.
- **AUR Package Hijackers**: Surge in malicious takeovers of Arch User Repository packages, injecting malware into community-maintained software. Multiple actors suspected; prompted Arch Linux to temporarily disable package adoption.
- **Water Utility PLC Attackers**: Targeting internet-exposed PLCs in U.S. water and wastewater systems per CISA warning. Motivations potentially disruptive or reconnaissance for future operations. Multiple campaigns observed.

## Source Attribution

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
- **USA Fencing Lunges Into the Hidden Identity Challenge in Amateur Sports**: Dark Reading - https://www.darkreading.com/identity-access-management-security/usa-fencing-hidden-identity-challenge-amateur-sports
- **Three Recent Chrome Releases Fix 1,442 Flaws, More Than Prior 23 Updates Combined**: The Hacker News - https://thehackernews.com/2026/07/three-recent-chrome-releases-fix-1442.html
- **Researchers Report 84 Flaws in 4G and 5G Cores, Including a Session Hijacking Flaw**: The Hacker News - https://thehackernews.com/2026/07/researchers-report-84-flaws-in-4g-and.html
- **6 Reasons Why Device Code Phishing is the Fastest-Growing Threat of 2026**: The Hacker News - https://thehackernews.com/2026/07/6-reasons-why-device-code-phishing-is.html
- **Chinese Hacker Commands DeepSeek via Telegram to Launch Autonomous Attacks**: The Hacker News - https://thehackernews.com/2026/07/chinese-hacker-commands-deepseek-via.html
- **Anthropic Says Claude Mistook the Open Internet for a CTF and Breached Three Organizations**: The Hacker News - https://thehackernews.com/2026/07/anthropic-says-claude-mistook-open.html
- **Anthropic's Claude breached 3 orgs, uploaded PyPI malware during tests**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/anthropics-claude-breached-3-orgs-uploaded-pypi-malware-during-tests/
- **South Korea fines telco giant KT $39 million for customer data breach**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/south-korea-fines-telco-giant-kt-39-million-for-customer-data-breach/
