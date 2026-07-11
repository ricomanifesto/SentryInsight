# Exploitation Report

## Executive Summary

Multiple critical exploitation campaigns are currently active across diverse technology stacks, ranging from AI-powered development tools and firmware bootloaders to cryptocurrency wallets and enterprise file-sharing platforms. The most immediately dangerous activity involves active exploitation of a critical authentication bypass in the official Gitea Docker image, allowing attackers to impersonate any user including administrators, and the "Ill Bloom" vulnerability in cryptocurrency wallet software that has already enabled theft of over $5 million in digital assets. Progress Software has issued an emergency directive for ShareFile customers to immediately shut down Storage Zone Controllers due to a credible external security threat, while researchers have demonstrated a novel "Ghostcommit" technique hiding prompt injections in PNG images that bypasses AI code reviewers to steal repository secrets.

Supply chain attacks remain prevalent, with unknown threat actors compromising the Injective Labs GitHub repository to publish malicious npm packages targeting cryptocurrency wallet private keys. The China-linked Silver Fox group has deployed a new Rust-based MODBEACON RAT using gRPC streaming for encrypted command-and-control communications. Meanwhile, an exposed attacker server revealed the WP-SHELLSTORM campaign backdooring thousands of WordPress sites. Physical attack vectors are also emerging, as demonstrated by unrecoverable laser fault injection attacks against Tangem hardware wallets. Several critical vulnerabilities remain unpatched, including the XRING flaw in Alibaba's XQUIC library allowing remote HTTP/3 server crashes.

## Active Exploitation Details

### Gitea Docker Image Authentication Bypass
- **Description**: A critical vulnerability in the official Docker image for Gitea, the self-hosted Git service, allows attackers to bypass authentication and impersonate any user including administrators. The flaw resides in the Docker image configuration rather than the core Gitea application code.
- **Impact**: Attackers gain full administrative access to Gitea instances, enabling repository manipulation, source code theft, supply chain compromise, and potential lateral movement within development environments.
- **Status**: Actively exploited in the wild. Users of the official Gitea Docker image should update immediately to patched versions.

### Ill Bloom Cryptocurrency Wallet Vulnerability
- **Description**: A flaw in how certain cryptocurrency wallet software generates recovery phrases (seed phrases), discovered and named "Ill Bloom" by security firm Coinspect. The vulnerability affects the entropy or generation process of mnemonic recovery phrases.
- **Impact**: Attackers can derive or predict wallet recovery phrases, enabling complete takeover of cryptocurrency wallets and drainage of funds. Over $5 million has already been stolen through active exploitation.
- **Status**: Actively exploited. Affected wallet software vendors need to implement patches and users should migrate funds to secure wallets.

### Progress ShareFile Storage Zone Controller Threat
- **Description**: Progress Software has identified a "credible external security threat" affecting ShareFile Storage Zone Controllers running on Windows servers. The exact technical details have not been publicly disclosed, but the severity warranted an emergency shutdown directive.
- **Impact**: Potential compromise of enterprise file sharing infrastructure, data exfiltration, and lateral movement within corporate networks.
- **Status**: Active threat response in progress. Progress Software has instructed all affected customers to immediately shut down Windows servers running Storage Zone Controllers while investigation and remediation proceed.

### Ghostcommit AI Prompt Injection via Images
- **Description**: A novel attack technique where malicious prompt injections are hidden within PNG image files. When AI code review agents (specifically CodeRabbit and Bugbot) process pull requests containing these images, the hidden prompts execute, causing the AI to exfiltrate repository secrets.
- **Impact**: Theft of API keys, credentials, tokens, and other sensitive data from code repositories. The attack bypasses traditional code scanning because the payload resides in image metadata rather than source code.
- **Status**: Demonstrated as proof-of-concept by researchers. No patch available for the fundamental issue; mitigation requires AI agents to sanitize or ignore image content during code review.

### Injective Labs GitHub Repository Compromise
- **Description**: Unknown threat actors compromised the Injective Labs SDK project's GitHub repository and used it to publish a malicious package to the npm registry. The package was designed to steal cryptocurrency wallet private keys from developers who installed it.
- **Impact**: Supply chain compromise affecting developers using the Injective Labs SDK. Theft of private keys leads to cryptocurrency wallet drainage.
- **Status**: Active campaign. The malicious package has been identified and removed, but developers who installed it must rotate all keys and audit systems.

### WP-SHELLSTORM WordPress Backdoor Campaign
- **Description**: A cybercrime operation deploying the WP-SHELLSTORM backdoor across thousands of WordPress sites. An exposed attacker server revealed hacking tools, activity logs, and target lists documenting the campaign's scope.
- **Impact**: Persistent remote access to compromised WordPress sites, enabling data theft, SEO spam, malware distribution, and use as infrastructure for further attacks.
- **Status**: Active campaign discovered via OPSEC failure. Thousands of sites confirmed compromised; cleanup and remediation ongoing.

### U-Boot Bootloader Vulnerabilities (Six Flaws)
- **Description**: Six vulnerabilities discovered by Binarly researchers in U-Boot, the universal bootloader used across embedded devices including home routers, smart cameras, and data center management controllers (BMCs). Flaws allow malicious firmware images to execute code during the boot process.
- **Impact**: Stealthy firmware-level persistence surviving OS reinstallation and disk replacement. Pre-OS execution enables hypervisor/detected malware deployment, hardware manipulation, and supply chain attacks.
- **Status**: Vulnerabilities disclosed; patch availability varies by vendor and device. Long deployment cycles for firmware updates create extended exposure windows.

### XRING Flaw in XQUIC HTTP/3 Library
- **Description**: A single-variable bug in XQUIC (Alibaba's QUIC and HTTP/3 library) allows any remote client to crash an HTTP/3 server with a short burst of completely valid, protocol-compliant traffic. The flaw is in the XRING component.
- **Impact**: Denial of service for any service using XQUIC for HTTP/3. No authentication or malformed packets required; attack traffic appears legitimate.
- **Status**: Unpatched. No fix available at time of reporting. FoxIO researchers disclosed the vulnerability.

### Tangem Wallet Laser Fault Injection
- **Description**: Researchers at Ledger's Donjon security team demonstrated that a precisely timed laser pulse aimed at the chip inside a Tangem crypto wallet card can reset the card's password to an attacker-chosen value.
- **Impact**: Complete bypass of hardware wallet authentication. The attack is unpatchable as it exploits physical hardware characteristics.
- **Status**: Proof-of-concept demonstrated. No firmware or software mitigation possible; requires physical security controls.

### OpenClaw AI Assistant Vulnerabilities (Patched)
- **Description**: Three now-patched security flaws in the OpenClaw personal AI assistant that formed an attack chain from WhatsApp message processing to host system compromise.
- **Impact**: Credential theft, privilege escalation, and potential full host compromise via malicious WhatsApp messages processed by the AI assistant.
- **Status**: Patched. Users should update to latest versions.

### Fake Microsoft Entra Passkey Enrollment (Vishing Campaign)
- **Description**: Threat actors conduct voice-based social engineering (vishing) campaigns impersonating Microsoft security requests, prompting Microsoft 365 users to enroll a new Entra passkey under attacker control.
- **Impact**: Full Microsoft 365 account takeover bypassing MFA. Attackers gain persistent access to email, SharePoint, Teams, and connected services.
- **Status**: Active campaign targeting multiple sectors. Mitigation requires user education and conditional access policies restricting passkey enrollment.

### MODBEACON RAT Deployment by Silver Fox
- **Description**: The China-linked cybercrime group Silver Fox has deployed a new Rust-based remote access trojan (RAT) called MODBEACON, which uses gRPC streaming for encrypted command-and-control communications.
- **Impact**: Stealthy persistent access with encrypted C2 evading network inspection. Rust implementation provides cross-platform capability and analysis resistance.
- **Status**: Active deployment. Attributed to Silver Fox by QiAnXin researchers.

## Affected Systems and Products

- **Gitea Docker Image**: Official Docker Hub images for Gitea self-hosted Git service; all versions prior to patched releases
- **Cryptocurrency Wallets (Ill Bloom)**: Multiple wallet software implementations with flawed recovery phrase generation; specific vendors not publicly named pending coordinated disclosure
- **Progress ShareFile Storage Zone Controllers**: Windows servers running Storage Zone Controller components for on-premises/hybrid ShareFile deployments
- **AI Code Review Agents**: CodeRabbit and Bugbot (confirmed vulnerable); potentially other AI agents processing image content in pull requests
- **Injective Labs SDK / npm Registry**: Developers who installed the compromised npm package published from the hijacked GitHub repository
- **WordPress Sites**: Thousands of sites compromised with WP-SHELLSTORM backdoor; all WordPress versions potentially affected if vulnerable plugins/themes or weak credentials present
- **U-Boot Bootloader Devices**: Home routers, IoT devices, smart cameras, data center BMCs, and embedded systems using vulnerable U-Boot versions
- **XQUIC Library Users**: Any service or application using Alibaba's XQUIC library for HTTP/3/QUIC implementation
- **Tangem Hardware Wallets**: Tangem crypto wallet cards (all versions; hardware-level flaw cannot be patched)
- **OpenClaw AI Assistant**: All versions prior to security patches addressing the three disclosed flaws
- **Microsoft 365 / Entra ID**: Organizations using Microsoft Entra passkey authentication; users targeted by vishing campaigns
- **MODBEACON RAT Targets**: Organizations targeted by Silver Fox group; cross-platform (Windows, Linux, macOS) due to Rust implementation

## Attack Vectors and Techniques

- **Docker Image Supply Chain Compromise**: Exploitation of misconfigured or vulnerable official Docker images to bypass authentication (Gitea)
- **Cryptographic Entropy Failure**: Flawed randomness in mnemonic phrase generation enabling seed phrase prediction (Ill Bloom)
- **Emergency Shutdown Advisory**: Vendor-directed infrastructure shutdown indicating active exploitation or imminent threat (ShareFile)
- **Steganographic Prompt Injection**: Malicious instructions hidden in PNG image metadata/pixel data executed by multimodal AI agents (Ghostcommit)
- **GitHub Repository Hijacking**: Compromise of legitimate project repositories to publish malicious packages to package registries (Injective Labs)
- **WordPress Backdoor Deployment**: Automated exploitation of vulnerable plugins, themes, or credentials to install persistent PHP backdoors (WP-SHELLSTORM)
- **Firmware/Bootloader Exploitation**: Malicious firmware images exploiting bootloader parsing flaws for pre-OS code execution (U-Boot)
- **Protocol-Compliant DoS**: Valid protocol traffic triggering logic flaws to crash servers without malformed packets (XRING/XQUIC)
- **Laser Fault Injection**: Physical hardware attack using precisely timed laser pulses to induce computational errors (Tangem Wallet)
- **AI Assistant Attack Chain**: Chained vulnerabilities in AI message processing enabling host compromise from messaging platform input (OpenClaw)
- **Voice Phishing (Vishing) for MFA Bypass**: Social engineering via phone calls tricking users into enrolling attacker-controlled passkeys (Entra Passkey)
- **gRPC Streaming C2**: Encrypted command-and-control using gRPC bidirectional streaming for traffic analysis resistance (MODBEACON RAT)

## Threat Actor Activities

- **Silver Fox (China-linked cybercrime group)**: Deploying MODBEACON RAT with gRPC streaming C2; attributed by QiAnXin researchers; active campaign
- **Unknown Actors - Injective Labs Compromise**: Compromised GitHub repository credentials or supply chain to publish wallet-stealing npm package; cryptocurrency-focused
- **WP-SHELLSTORM Operators**: Cybercrime crew operating automated WordPress compromise infrastructure; OPSEC failure exposed server with tools, logs, and target lists
- **Ill Bloom Exploiters**: Active threat group(s) exploiting wallet seed phrase flaw; over $5 million in cryptocurrency stolen per Coinspect
- **Gitea Docker Exploiters**: Actively scanning for and exploiting vulnerable Gitea Docker deployments for administrative access
- **Vishing Campaign Operators**: Conducting voice-based social engineering targeting Microsoft 365 users across multiple sectors for Entra passkey enrollment fraud
- **Ryuk/BlackCat Ransomware Affiliates**: Armenian national pleaded guilty to Ryuk deployments; former DigitalMint negotiator sentenced for BlackCat (ALPHV) attacks; demonstrates ongoing ransomware ecosystem activity
- **Dutch Hackers (Odido Breach)**: Suspected by Dutch National Police in February 2026 breach of telecommunications provider Odido
- **OpenMandriva Saboteur**: Internal contributor attempted project sabotage following dispute; insider threat example

## Source Attribution

- **'Ghostcommit' hides prompt injection in images to fool AI agents, steal secrets**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/ghostcommit-hides-prompt-injection-in-images-to-fool-ai-agents-steal-secrets/
- **Critical Zimbra Flaw Could Let Crafted Emails Run Malicious Code in User Sessions**: The Hacker News - https://thehackernews.com/2026/07/critical-zimbra-flaw-could-let-crafted_0483473395.html
- **New U-Boot flaws could enable stealthy firmware attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-u-boot-flaws-could-enable-stealthy-firmware-attacks/
- **Jen Ellis: Connecting Cyber Community With Political Machinery**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/jen-ellis-connecting-cyber-community-political-machinery
- **Ryuk ransomware member pleads guilty in the US, faces 15 years in prison**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/ryuk-ransomware-member-pleads-guilty-in-the-us-faces-15-years-in-prison/
- **Cybercriminals Flock to Healthcare Businesses as Attacks Surge**: Dark Reading - https://www.darkreading.com/threat-intelligence/cybercriminals-healthcare-businesses-attacks-surge
- **Police suspects Dutch hackers were involved in Odido breach**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/police-suspects-dutch-hackers-were-involved-in-odido-breach/
- **URGENT - Progress Tells ShareFile Customers to Shut Down Storage Zone Controllers Over Security Threat**: The Hacker News - https://thehackernews.com/2026/07/urgent-progress-tells-sharefile.html
- **Injective Labs GitHub Compromise Pushes Wallet-Key-Stealing npm Packages**: The Hacker News - https://thehackernews.com/2026/07/injective-labs-github-compromise-pushes.html
- **Progress urges ShareFile admins to shut down servers over “credible” threat**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/progress-urges-sharefile-customers-to-shut-down-servers-over-credible-threat/
- **Six New U-Boot Flaws Could Let Malicious Images Crash Devices or Run Code at Boot**: The Hacker News - https://thehackernews.com/2026/07/six-new-u-boot-flaws-could-let.html
- **Hackers exploit critical auth bypass in Gitea Docker image**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-auth-bypass-in-gitea-docker-image/
- **Money launderer accused of stealing seized crypto while in prison**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/money-launderer-accused-of-stealing-seized-crypto-while-in-prison/
- **Laser Attack Resets Tangem Wallet Passwords on Cards That Can't Be Patched**: The Hacker News - https://thehackernews.com/2026/07/laser-attack-resets-tangem-wallet.html
- **Researcher Details WhatsApp-to-Host Attack Chain Using Three OpenClaw Flaws**: The Hacker News - https://thehackernews.com/2026/07/researcher-details-whatsapp-to-host.html
- **The Replicant in Your Directory: AI Agents and the Identity Security Gap**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/the-replicant-in-your-directory-ai-agents-and-the-identity-security-gap/
- **Fresh ATM Crypto Software Bugs: Jackpot or Bust?**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/atm-crypto-software-bugs-jackpot-bust
- **More Countries Jump on the Social Media 'Ban Wagon'**: Dark Reading - https://www.darkreading.com/cyber-risk/more-countries-jump-on-the-social-media-ban-wagon
- **New MODBEACON RAT Uses gRPC Streaming for Encrypted C2 Traffic**: The Hacker News - https://thehackernews.com/2026/07/new-modbeacon-rat-uses-grpc-streaming.html
- **AI Coding: Do Security Risks Outweigh Productivity Gains?**: Dark Reading - https://www.darkreading.com/application-security/ai-coding-security-risks-productivity-gains
- **Unpatched XRING Flaw in XQUIC Lets Remote Clients Crash HTTP/3 Servers**: The Hacker News - https://thehackernews.com/2026/07/unpatched-xring-flaw-in-xquic-lets.html
- **Zimbra urges customers to patch critical web client XSS flaw**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/zimbra-urges-customers-to-patch-critical-web-client-xss-flaw/
- **From 17,000 to 1.1 Million Assets: How Lumen Technologies Rebuilt Exposure Management at Scale**: The Hacker News - https://thehackernews.com/2026/07/from-17000-to-11-million-assets-how.html
- **Exposed Hacker Server Reveals WP-SHELLSTORM Backdooring Thousands of WordPress Sites**: The Hacker News - https://thehackernews.com/2026/07/exposed-hacker-server-reveals-wp.html
- **Study of 281 Free Android VPN Apps Finds Traffic Leaks, Unencrypted Data, and Tracking**: The Hacker News - https://thehackernews.com/2026/07/study-of-281-free-android-vpn-apps.html
- **Hackers Use Fake Microsoft Entra Passkey Enrollment to Gain Microsoft 365 Access**: The Hacker News - https://thehackernews.com/2026/07/hackers-use-fake-microsoft-entra.html
- **Attackers Exploit 'Ill Bloom' Vulnerability to Drain Over $5 Million From Cryptocurrency Wallets**: The Hacker News - https://thehackernews.com/2026/07/attackers-exploit-ill-bloom.html
- **Former ransomware negotiator gets 4 years for BlackCat attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/us-ransomware-negotiator-gets-4-years-in-prison-for-blackcat-attacks/
- **Ransomware Negotiator Gets 70 Months in Prison for Aiding BlackCat Attacks**: The Hacker News - https://thehackernews.com/2026/07/ransomware-negotiator-gets-70-months-in.html
- **OpenMandriva Linux says contributor tried to sabotage the project**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/openmandriva-linux-says-contributor-tried-to-sabotage-the-project/
