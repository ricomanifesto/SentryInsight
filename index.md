# Exploitation Report

## Executive Summary

Multiple high-impact exploitation campaigns are actively underway across diverse technology sectors. A firmware flaw in COLDCARD hardware wallets has been linked to the theft of approximately $158 million in Bitcoin across two major incidents, with one attack draining over 1,000 wallets in just 41 minutes. Simultaneously, threat actors have compromised the Adform advertising supply chain to inject cryptocurrency-stealing scripts across customer websites, while an authentication bypass in N-able N-central allowed attackers to seize administrative control over managed customer environments after an initial patch proved insufficient.

Critical vulnerabilities in enterprise and development platforms are being actively exploited or present imminent risk. Adobe Campaign Classic carries a maximum-severity flaw enabling unauthenticated remote code execution, while the Hugging Face Diffusers library contains three high-severity flaws allowing arbitrary code execution through malicious model repositories. Rails applications face a critical Active Storage vulnerability permitting arbitrary file read and potential RCE escalation. Nation-state activity remains elevated, with suspected Chinese-speaking actors deploying OctLurk and SilkLurk against Central Asian governments and leveraging DeepSeek AI via the Hermes Agent framework for autonomous vulnerability scanning and exploitation. CISA has also warned of escalating attacks against internet-exposed PLCs in U.S. water utilities.

## Active Exploitation Details

### COLDCARD Hardware Wallet RNG Flaw
- **Description**: A vulnerability in COLDCARD hardware wallet firmware involving a flawed random number generator (RNG) that produces predictable or weak entropy for seed generation. This allows attackers to derive private keys and steal funds from affected wallets.
- **Impact**: Attackers can steal Bitcoin from any wallet whose seed was generated using the flawed RNG. Two major thefts have been documented: approximately $88.6 million stolen from thousands of wallets, and a separate 41-minute attack draining 1,196 addresses for 1,082.65 BTC (approximately $70.2 million at time of theft).
- **Status**: Actively exploited in the wild. Firmware updates have been released by COLDCARD to address the RNG flaw.
- **CVE ID**: Not explicitly mentioned in source articles

### N-able N-central Authentication Bypass
- **Description**: An authentication bypass vulnerability in N-able N-central remote monitoring and management (RMM) software that allows unauthenticated attackers to gain administrative access to the N-central server.
- **Impact**: Attackers achieve full administrative control over the N-central server and can pivot to all customer systems managed through that server, enabling widespread supply-chain compromise of managed service provider (MSP) client environments.
- **Status**: Actively exploited. N-able released an initial fix that was incomplete; attackers continued to exploit the vulnerability after the first patch. A subsequent complete fix has been issued.
- **CVE ID**: Not explicitly mentioned in source articles

### Adobe Campaign Classic Remote Code Execution
- **Description**: A maximum-severity vulnerability in Adobe Campaign Classic (ACC), an enterprise marketing automation platform, that allows arbitrary code execution without any user interaction.
- **Impact**: Unauthenticated remote attackers can execute arbitrary code on the Campaign Classic server with the privileges of the application, leading to full system compromise, data exfiltration, and lateral movement.
- **Status**: Adobe has released security updates addressing the flaw. The CVSS 10.0 rating indicates immediate patching is critical.
- **CVE ID**: Not explicitly mentioned in source articles

### Hugging Face Diffusers Arbitrary Code Execution
- **Description**: Three high-severity vulnerabilities in the Hugging Face Diffusers library that allow crafted model repositories to execute arbitrary code when loaded by a victim's machine. The flaws reside in the model loading and deserialization logic.
- **Impact**: Attackers can publish malicious models to Hugging Face Hub or private repositories. When data scientists or ML engineers load these models, arbitrary code executes on their machines, enabling supply-chain attacks against AI/ML development pipelines.
- **Status**: Disclosed and patched. Users must update to the latest Diffusers version.
- **CVE ID**: Not explicitly mentioned in source articles

### Rails Active Storage Arbitrary File Read and RCE
- **Description**: A critical vulnerability in the Active Storage framework of Ruby on Rails that allows unauthenticated attackers to read arbitrary files from the application server. Under certain configurations, this can escalate to remote code execution.
- **Impact**: Attackers can read sensitive files including application source code, configuration files, credentials, and environment variables. In configurations using certain storage backends, deserialization gadgets may enable RCE.
- **Status**: Patched in recent Rails releases. Applications must upgrade immediately.
- **CVE ID**: Not explicitly mentioned in source articles

### Thermo Fisher Applied Biosystems Software File Tampering
- **Description**: A flaw in select Applied Biosystems human identification software products that allows data files to be altered before the analysis software loads them, making tampering nearly undetectable.
- **Impact**: Forensic and research DNA analysis results can be manipulated without detection, potentially compromising criminal investigations, paternity testing, and genetic research integrity.
- **Status**: Patched by Thermo Fisher Scientific in July 2026.
- **CVE ID**: Not explicitly mentioned in source articles

### Adform Supply-Chain Script Compromise
- **Description**: Attackers compromised the JavaScript delivery infrastructure of advertising technology company Adform, modifying a widely deployed script to rewrite cryptocurrency wallet addresses in users' clipboards and on web pages.
- **Impact**: Visitors to any website using Adform's advertising platform were exposed to cryptocurrency theft. Wallet addresses copied to clipboard or displayed on page were silently replaced with attacker-controlled addresses, diverting funds.
- **Status**: Adform detected the incident and remediated the compromised script. Investigation ongoing.
- **CVE ID**: Not explicitly mentioned in source articles

### Hotel Wi-Fi Fake Update Campaign (CornFlake RAT)
- **Description**: Threat actors hijacked hotel Wi-Fi networks to serve fake browser update prompts that deliver the CornFlake remote access trojan (RAT) to connected guests' devices.
- **Impact**: CornFlake provides full remote access including webcam capture, microphone recording, keystroke logging, file exfiltration, and command execution. Targets include business travelers and government personnel staying at compromised hotels.
- **Status**: Active campaign observed by Microsoft. No specific patch; defense relies on network hygiene and endpoint detection.
- **CVE ID**: Not explicitly mentioned in source articles

### Amgen Cloud Data Breach
- **Description**: Threat actors breached multiple third-party cloud service providers used by pharmaceutical company Amgen, exfiltrating corporate data and patient health information.
- **Impact**: Exposure of sensitive patient health data, proprietary pharmaceutical research, and corporate intellectual property. Regulatory implications under HIPAA and GDPR.
- **Status**: Breach confirmed by Amgen. Third-party cloud providers involved; investigation ongoing.
- **CVE ID**: Not explicitly mentioned in source articles

### Arch Linux AUR Package Hijacking
- **Description**: A surge in malicious takeovers of existing Arch User Repository (AUR) packages, where attackers adopt orphaned or abandoned packages and inject malware into build scripts.
- **Impact**: Users installing compromised AUR packages execute malicious code during build/installation, leading to system compromise. Arch Linux temporarily disabled package adoption to stem the flood.
- **Status**: Active campaign. Arch Linux has disabled AUR package adoption temporarily while implementing stronger verification.
- **CVE ID**: Not explicitly mentioned in source articles

### 4G/5G Core Network Vulnerabilities
- **Description**: Researchers disclosed 84 vulnerabilities across 4G and 5G core network implementations, including a session hijacking flaw that allows attackers to intercept or manipulate subscriber sessions.
- **Impact**: Potential for denial-of-service attacks against mobile core networks, session hijacking enabling interception of calls/data, location tracking, and billing fraud. Widespread impact across multiple vendors' implementations.
- **Status**: Disclosed to affected vendors; patching timeline varies. No confirmed active exploitation reported in articles.
- **CVE ID**: Not explicitly mentioned in source articles

### Device Code Phishing (OAuth 2.0 Device Authorization Grant Abuse)
- **Description**: Industrial-scale abuse of the OAuth 2.0 device authorization grant flow, where attackers trick users into authorizing malicious applications on legitimate identity providers, granting persistent access tokens.
- **Impact**: Attackers gain long-lived access to victim resources (email, cloud storage, corporate applications) without stealing credentials. Bypasses MFA in many implementations. Evolved from niche technique to industrial-scale threat in under six months.
- **Status**: Actively exploited at scale. Identity providers implementing mitigations; user education critical.
- **CVE ID**: Not explicitly mentioned in source articles

### HollowFrame Loader and Matryoshka Backdoor
- **Description**: A previously undocumented Go-based loader framework (HollowFrame) deploying a Rust-based malware family (Matryoshka) via spear-phishing attacks targeting law firms.
- **Impact**: Persistent remote access, credential theft, document exfiltration, and lateral movement within legal sector networks. Matryoshka's modular design allows plugin-based capability extension.
- **Status**: Active campaign documented by Blackpoint Cyber. Attribution ongoing.
- **CVE ID**: Not explicitly mentioned in source articles

### Android TV Box Proxy Botnet
- **Description**: Cheap Android TV boxes shipped with pre-installed applications that spoof device identifiers (mimicking Samsung, Huawei, Xiaomi, Vivo phones) and convert the device into a residential proxy exit node for ad fraud and traffic anonymization.
- **Impact**: Device owners' broadband connections are abused for click fraud, credential stuffing, and anonymizing malicious traffic. Devices silently join a residential proxy botnet operated by the same entities selling the hardware.
- **Status**: Ongoing. Identified by Bitsight. No vendor patch; consumer awareness and network monitoring are primary defenses.
- **CVE ID**: Not explicitly mentioned in source articles

### U.S. Water Utility PLC Attacks
- **Description**: CISA warns of significant increase in attacks targeting internet-exposed programmable logic controllers (PLCs) in water and wastewater treatment facilities.
- **Impact**: Disruption of water treatment operations, potential contamination risks, service outages for communities. Attacks exploit default credentials, unpatched vulnerabilities, and lack of network segmentation.
- **Status**: Active and increasing. CISA urges immediate removal of PLCs from public internet, credential rotation, and patching.
- **CVE ID**: Not explicitly mentioned in source articles

## Affected Systems and Products

- **COLDARK Hardware Wallets (Mk3, Mk4, Q models)**: Firmware versions prior to the RNG fix; all wallets with seeds generated on vulnerable firmware
- **N-able N-central**: All versions prior to the complete authentication bypass patch; MSP environments using N-central for customer management
- **Adobe Campaign Classic (ACC)**: Enterprise on-premises and managed services deployments prior to August 2026 security update
- **Hugging Face Diffusers Library**: Versions prior to the patched release; any AI/ML pipeline loading models from untrusted sources
- **Ruby on Rails Applications**: Rails versions with vulnerable Active Storage component (specific versions detailed in Rails security advisories)
- **Thermo Fisher Applied Biosystems Software**: Human identification software suite (specific product names and versions in vendor advisory)
- **Adform Advertising Platform**: JavaScript delivery infrastructure; all customer websites embedding Adform ad tags during compromise window
- **Hotel Wi-Fi Networks**: Compromised hospitality network infrastructure serving fake browser updates to guest devices
- **Third-Party Cloud Providers (Amgen breach)**: Multiple unnamed cloud service providers hosting Amgen data
- **Arch User Repository (AUR)**: Orphaned and adopted packages with malicious build scripts; Arch Linux package management ecosystem
- **4G/5G Core Network Equipment**: Multiple vendor implementations (Ericsson, Nokia, Huawei, ZTE, others) across mobile network operator deployments
- **OAuth 2.0 Identity Providers**: Major IdPs supporting device authorization grant (Microsoft Entra ID, Google, Okta, Auth0, others)
- **Law Firm IT Environments**: Targeted via spear-phishing delivering HollowFrame/Matryoshka; document management and case management systems
- **Android TV Boxes**: Low-cost devices from unspecified manufacturers running modified Android with pre-installed proxy/spoofing apps
- **Internet-Exposed PLCs**: Programmable logic controllers in water/wastewater facilities directly accessible from public internet

## Attack Vectors and Techniques

- **Supply-Chain Compromise (Adform)**: Attackers modified a legitimate JavaScript file served from Adform's CDN, turning a trusted advertising script into a cryptocurrency address swapper executed in victims' browsers across thousands of websites.
- **Firmware/Entropy Attack (COLDARK)**: Exploitation of weak random number generation in hardware wallet firmware to derive private keys from public information or reduced entropy space, enabling mass wallet sweeping.
- **Authentication Bypass (N-central)**: Unauthenticated attackers exploit a logic flaw in N-central's authentication mechanism to escalate directly to administrative privileges without credentials.
- **Model Deserialization Attack (Hugging Face Diffusers)**: Malicious model files exploit unsafe deserialization in the Diffusers library to achieve arbitrary code execution when the model is loaded for inference or fine-tuning.
- **Fake Browser Update / Drive-By Download (Hotel Wi-Fi)**: Man-in-the-middle position on hotel Wi-Fi allows injection of fake update prompts delivering CornFlake RAT; no user interaction beyond clicking "update."
- **Spear-Phishing with Custom Loader (HollowFrame/Matryoshka)**: Targeted emails to law firm personnel deliver a Go-based loader that deploys a modular Rust backdoor with plugin architecture.
- **OAuth Device Code Phishing**: Attackers initiate device authorization flows on legitimate IdPs, then social-engineer victims to approve the authorization on a separate device, granting persistent access tokens.
- **AUR Package Takeover**: Attackers adopt abandoned Arch User Repository packages and inject malicious code into PKGBUILD/install scripts executed during package build.
- **Residential Proxy Botnet (Android TV Boxes)**: Pre-installed apps spoof device fingerprints and route traffic through owners' residential IPs for ad fraud, credential stuffing, and anonymization.
- **Internet-Exposed PLC Exploitation**: Attackers scan for and directly access PLC management interfaces on water utility networks, leveraging default credentials and unpatched vulnerabilities.
- **Third-Party Cloud Compromise (Amgen)**: Threat actors target cloud service providers used by Amgen rather than Amgen directly, exploiting trust relationships and shared infrastructure.
- **AI-Automated Vulnerability Scanning (DeepSeek/Hermes)**: Chinese-speaking actors use DeepSeek LLM via the Hermes Agent framework to autonomously discover, exploit, and post-exploit vulnerable servers with minimal human direction.

## Threat Actor Activities

- **Suspected Chinese-Speaking APT (OctLurk/SilkLurk)**: Targeting government organizations in Central Asia (Afghanistan, Kyrgyzstan, Tajikistan) with custom malware families OctLurk and SilkLurk. Activity indicates strategic intelligence collection against regional governments.
- **Chinese-Speaking Actor (DeepSeek/Hermes Autonomous Operations)**: Using DeepSeek LLM through the open-source Hermes Agent framework to conduct fully autonomous vulnerability discovery, exploitation, and post-exploitation against internet-exposed servers. Initial instructions delivered via Telegram; subsequent operations require no human intervention.
- **Financially Motivated Actors (COLDARK Wallet Sweeps)**: Rapid, automated draining of thousands of Bitcoin addresses within minutes, indicating sophisticated tooling for mass exploitation of the RNG flaw. Two distinct campaigns netted ~$158 million total.
- **Supply-Chain Operators (Adform Compromise)**: Actors capable of compromising ad-tech infrastructure to deploy browser-based cryptocurrency stealers at scale across publisher networks.
- **HollowFrame/Matryoshka Operators**: Previously undocumented threat group targeting legal sector via spear-phishing with custom Go/Rust toolchain. Modular malware design suggests professional development and intent for sustained operations.
- **Water Utility Attackers**: Unattributed actors increasingly targeting OT/ICS environments in U.S. critical infrastructure, specifically water/wastewater PLCs. Motivation unclear (ransomware, hacktivism, or pre-positioning).
- **AUR Package Hijackers**: Opportunistic actors adopting abandoned Arch Linux packages to distribute malware to developer and enthusiast systems. Volume suggests automated or semi-automated adoption and weaponization.

## Source Attribution

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
- **USA Fencing Lunges Into the Hidden Identity Challenge in Amateur Sports**: Dark Reading - https://www.darkreading.com/identity-access-management-security/usa-fencing-hidden-identity-challenge-amateur-sports
- **Three Recent Chrome Releases Fix 1,442 Flaws, More Than Prior 23 Updates Combined**: The Hacker News - https://thehackernews.com/2026/07/three-recent-chrome-releases-fix-1442.html
- **Researchers Report 84 Flaws in 4G and 5G Cores, Including a Session Hijacking Flaw**: The Hacker News - https://thehackernews.com/2026/07/researchers-report-84-flaws-in-4g-and.html
- **6 Reasons Why Device Code Phishing is the Fastest-Growing Threat of 2026**: The Hacker News - https://thehackernews.com/2026/07/6-reasons-why-device-code-phishing-is.html
- **Chinese Hacker Commands DeepSeek via Telegram to Launch Autonomous Attacks**: The Hacker News - https://thehackernews.com/2026/07/chinese-hacker-commands-deepseek-via.html
