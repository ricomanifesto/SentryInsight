# Exploitation Report

## Executive Summary

Multiple high-severity exploitation campaigns are underway across diverse attack surfaces, from software supply chains and content management platforms to AI-assisted development workflows and cryptocurrency infrastructure. A compromised npm package (jscrambler 8.14.0) executes a Rust-based infostealer during installation, while a separate GitHub repository compromise at Injective Labs delivered wallet-key-stealing npm packages. Attackers are actively exploiting a critical authentication bypass in the official Gitea Docker image to impersonate administrators, and a global campaign documented by the Australian Cyber Security Centre targets vulnerable CMS platforms and plugins at scale. An unpatchable hardware flaw in Tangem wallet cards allows laser-based password resets, and the "Ill Bloom" vulnerability in cryptocurrency wallet recovery phrase generation has already enabled theft exceeding $5 million.

Simultaneously, threat actors are expanding techniques against emerging technologies. The "Ghostcommit" method embeds prompt injections in PNG images to deceive AI code reviewers and exfiltrate repository secrets, while voice-based social engineering campaigns abuse Microsoft Entra passkey enrollment to compromise Microsoft 365 environments. China-linked group Silver Fox has deployed a new Rust-based RAT (MODBEACON) leveraging gRPC streaming for encrypted command-and-control. Six vulnerabilities in the widely deployed U-Boot bootloader enable stealthy firmware attacks across embedded devices, and an unpatched flaw in Alibaba's XQUIC library permits denial-of-service against HTTP/3 servers. An exposed operator server revealed the WP-SHELLSTORM campaign backdooring thousands of WordPress sites, while suspected China- and India-aligned groups conduct sustained espionage against Pakistani law enforcement through a compromised police portal.

## Active Exploitation Details

### Compromised jscrambler npm Package (Supply Chain Attack)
- **Description**: The jscrambler npm package version 8.14.0 was compromised with a malicious preinstall hook that executes a Rust-based infostealer on the victim's machine during package installation. The malicious code runs automatically when developers or CI/CD pipelines install the package.
- **Impact**: Full system compromise on any machine installing the poisoned package, including theft of credentials, environment variables, browser data, cryptocurrency wallets, and other sensitive information. The attack affects development environments, build systems, and any downstream consumers.
- **Status**: Actively exploited in the wild. Version 8.14.0 published on July 11, 2026. Users must avoid this version and audit systems where it was installed.

### Injective Labs GitHub/NPM Supply Chain Attack
- **Description**: Unknown threat actors compromised the Injective Labs SDK project's GitHub repository and used it to publish malicious packages to the npm registry designed to steal cryptocurrency wallet private keys.
- **Impact**: Theft of cryptocurrency wallet private keys from developers and users who install the compromised packages, leading to direct financial loss.
- **Status**: Active compromise. The malicious packages were published to npm via the hijacked GitHub repository. Users of Injective Labs SDK should verify package integrity and rotate any exposed keys.

### Critical Authentication Bypass in Gitea Docker Image
- **Description**: A critical vulnerability in the official Docker image for Gitea (self-hosted Git service) allows attackers to bypass authentication and impersonate any user, including administrators.
- **Impact**: Complete takeover of Gitea instances, including source code theft, supply chain poisoning via malicious commits, privilege escalation, and lateral movement within development environments.
- **Status**: Actively exploited in the wild. The vulnerability affects the official Docker image deployment.

### Global CMS Platform Exploitation Campaign
- **Description**: The Australian Cyber Security Centre (ACSC) has issued an alert regarding a global exploitation campaign targeting vulnerable content management systems (CMS) and their plugins.
- **Impact**: Mass compromise of websites running outdated or vulnerable CMS platforms, leading to web shells, data exfiltration, defacement, and use as infrastructure for further attacks.
- **Status**: Ongoing global campaign. Organizations using CMS platforms are urged to apply security updates immediately and review plugin inventories.

### Ghostcommit: Prompt Injection via Images Targeting AI Code Reviewers
- **Description**: A novel attack technique dubbed "Ghostcommit" embeds malicious prompt injections within PNG images. When AI code review agents (specifically CodeRabbit and Bugbot) process pull requests containing these images, the hidden prompts instruct the AI to exfiltrate repository secrets.
- **Impact**: Bypass of AI-powered security controls, theft of API keys, tokens, credentials, and other secrets from repositories using affected AI review tools. The attack succeeds because the AI agents do not open or analyze image content.
- **Status**: Demonstrated as practical against CodeRabbit and Bugbot. Represents a new class of supply chain risk in AI-augmented development workflows.

### Critical Zimbra Classic Web Client Vulnerability
- **Description**: A critical security vulnerability in the Zimbra Collaboration Suite Classic Web Client allows crafted emails to execute arbitrary code in user sessions.
- **Impact**: Remote code execution in the context of the victim user when viewing a malicious email, leading to email compromise, data theft, and potential lateral movement.
- **Status**: Zimbra is urging customers to apply updates immediately. Patches are available.

### U-Boot Bootloader Vulnerabilities (Six Flaws)
- **Description**: Researchers at Binarly discovered six vulnerabilities in U-Boot, the universal bootloader used across embedded devices including routers, smart cameras, and server management chips (BMCs). The flaws allow malicious code execution during the boot process via crafted boot images.
- **Impact**: Stealthy, persistent firmware-level compromise that survives OS reinstallation. Affects a vast ecosystem of network infrastructure, IoT devices, and data center hardware.
- **Status**: Vulnerabilities disclosed. Patches may vary by vendor and device. No active exploitation reported in articles, but high risk due to deployment scale and stealth potential.

### Progress ShareFile Storage Zone Controllers Threat
- **Description**: Progress Software has instructed all ShareFile customers using Storage Zone Controllers to immediately shut down their Windows servers due to a "credible external security threat."
- **Impact**: Potential compromise of file storage and sharing infrastructure, data exfiltration, and network access via the Storage Zone Controller component.
- **Status**: Active threat response in progress. Progress confirmed responding to a credible threat. Customers directed to power down affected servers immediately.

### Tangem Wallet Laser Fault Injection Attack
- **Description**: Researchers at Ledger's Donjon team demonstrated that a precisely timed laser pulse targeting the chip inside a Tangem crypto wallet card can reset the card's password to an attacker-chosen value.
- **Impact**: Physical theft of cryptocurrency assets from Tangem wallet cards. The vulnerability is unpatchable as it resides in hardware.
- **Status**: Proof-of-concept demonstrated. No software mitigation possible; physical security of the card is the only defense.

### OpenClaw AI Assistant Vulnerability Chain (WhatsApp-to-Host)
- **Description**: Three now-patched security flaws in the OpenClaw personal AI assistant could be chained to enable credential theft, privilege escalation, and ultimately a WhatsApp-to-host attack chain.
- **Impact**: Compromise of the host system via the AI assistant's integration with WhatsApp, leading to data theft and system control.
- **Status**: Vulnerabilities have been patched. Users should update OpenClaw immediately.

### MODBEACON RAT Deployment by Silver Fox
- **Description**: The China-linked cybercrime group Silver Fox has deployed a new Rust-based remote access trojan (RAT) called MODBEACON, which uses gRPC streaming for encrypted command-and-control communications.
- **Impact**: Persistent remote access, data exfiltration, and lateral movement within victim networks. The gRPC-based C2 evades traditional network monitoring.
- **Status**: Active deployment attributed to Silver Fox (China-linked). QiAnXin researchers tracking the campaign.

### XQUIC XRING Flaw (Unpatched HTTP/3 Denial-of-Service)
- **Description**: A single incorrect variable in XQUIC (Alibaba's QUIC and HTTP/3 library) allows any remote client to crash the server with a short burst of legitimate traffic.
- **Impact**: Denial-of-service against any server using the vulnerable XQUIC library for HTTP/3. No authentication or complex attack required.
- **Status**: Unpatched. No fix available at time of reporting. FoxIO researchers disclosed the flaw.

### WP-SHELLSTORM WordPress Backdoor Campaign
- **Description**: An exposed hacker server revealed the operations of a cybercrime crew using a toolkit dubbed WP-SHELLSTORM to backdoor thousands of WordPress sites. The server contained hacking tools, activity logs, and target lists.
- **Impact**: Persistent access to compromised WordPress sites, enabling data theft, SEO spam, malware distribution, and use as pivot points.
- **Status**: Active campaign exposed via operator error (server left open for three weeks). Thousands of sites confirmed compromised.

### Microsoft Entra Passkey Enrollment Social Engineering
- **Description**: Threat actors are conducting voice-based social engineering campaigns (vishing) that trick Microsoft 365 users into enrolling a new Microsoft Entra passkey under attacker control.
- **Impact**: Full account takeover of Microsoft 365 identities, bypassing MFA, with access to email, SharePoint, Teams, and connected resources.
- **Status**: Active campaign targeting multiple sectors. Relies on social engineering rather than software vulnerability.

### Ill Bloom Cryptocurrency Wallet Vulnerability
- **Description**: A flaw dubbed "Ill Bloom" in how certain cryptocurrency wallet software generates recovery phrases (seed words) allows attackers to derive private keys and drain wallets.
- **Impact**: Theft of cryptocurrency assets. Over $5 million already stolen from vulnerable wallets. The flaw affects the entropy/generation process of recovery phrases.
- **Status**: Actively exploited in the wild. Disclosed by security firm Coinspect. Affected wallet software vendors need to patch generation logic.

### Balochistan Police Portal Espionage Campaigns
- **Description**: Sustained cyber espionage activity against Pakistani law enforcement organizations conducted via a compromised Balochistan Police portal, attributed to suspected China- and India-aligned threat actors.
- **Impact**: Intelligence collection from law enforcement systems, potential compromise of investigations, personnel data, and operational security.
- **Status**: Ongoing multi-group campaigns. Researchers have disclosed details of the sustained activity.

## Affected Systems and Products

- **jscrambler npm package version 8.14.0**: JavaScript obfuscation tool; malicious preinstall hook executes Rust infostealer on installation
- **Injective Labs SDK GitHub repository / npm packages**: Blockchain development SDK; compromised repo used to publish wallet-key-stealing packages
- **Gitea Docker image (official)**: Self-hosted Git service; critical auth bypass in containerized deployment
- **Content Management Systems (multiple) and plugins**: Various CMS platforms globally; ACSC warns of widespread exploitation of unpatched instances
- **CodeRabbit and Bugbot AI code review agents**: AI-powered PR review tools; vulnerable to prompt injection via PNG images (Ghostcommit)
- **Zimbra Collaboration Suite Classic Web Client**: Enterprise email and collaboration platform; critical RCE via crafted emails
- **U-Boot bootloader**: Universal bootloader on embedded devices (routers, cameras, BMCs, IoT); six vulnerabilities enabling firmware attacks
- **Progress ShareFile Storage Zone Controllers (Windows)**: On-premises file storage component; credible threat requiring immediate shutdown
- **Tangem hardware cryptocurrency wallet cards**: Hardware wallet cards; unpatchable laser fault injection resets passwords
- **OpenClaw personal AI assistant**: AI assistant with WhatsApp integration; three patched flaws enabling host compromise chain
- **MODBEACON RAT infrastructure**: Rust-based malware using gRPC streaming C2; deployed by Silver Fox group
- **XQUIC library (Alibaba)**: QUIC/HTTP/3 implementation; unpatched XRING flaw allows remote server crash
- **WordPress sites (thousands)**: CMS installations backdoored via WP-SHELLSTORM toolkit; exposed operator server revealed scale
- **Microsoft Entra ID / Microsoft 365**: Cloud identity and productivity suite; passkey enrollment abused via vishing
- **Cryptocurrency wallet software (multiple)**: Wallets with flawed recovery phrase generation (Ill Bloom); active exploitation draining funds
- **Balochistan Police portal**: Law enforcement web portal; compromised for multi-group espionage against Pakistani agencies

## Attack Vectors and Techniques

- **Software Supply Chain Compromise (npm)**: Malicious code injected into legitimate package (jscrambler 8.14.0) executes on install via preinstall hook
- **GitHub Repository Hijacking**: Compromised Injective Labs SDK repo used as distribution channel for malicious npm packages
- **Container Image Vulnerability Exploitation**: Critical auth bypass in official Gitea Docker image exploited for admin impersonation
- **Mass CMS/Plugin Exploitation**: Automated scanning and exploitation of known vulnerabilities in unpatched CMS platforms and plugins globally
- **AI Prompt Injection via Steganography**: Malicious prompts hidden in PNG images (Ghostcommit) target AI code reviewers that don't inspect images
- **Email-Based Client-Side RCE**: Crafted emails exploit Zimbra Classic Web Client to execute code in victim's browser session
- **Firmware/Bootloader Exploitation**: Malicious boot images target U-Boot vulnerabilities for persistent pre-OS code execution
- **Infrastructure Shutdown Advisory**: Vendor-directed emergency shutdown of ShareFile Storage Zone Controllers due to active threat
- **Hardware Fault Injection**: Precision laser glitching attacks Tangem wallet secure element to reset authentication
- **AI Assistant Attack Chain**: Chained vulnerabilities in OpenClaw exploited via WhatsApp integration for host compromise
- **Encrypted C2 via gRPC Streaming**: MODBEACON RAT uses gRPC for stealthy, encrypted command-and-control communications
- **HTTP/3 Protocol DoS**: Single malformed-but-valid request sequence crashes XQUIC-based servers (unpatched)
- **WordPress Backdoor Deployment**: WP-SHELLSTORM toolkit automates persistent backdoor installation across thousands of sites
- **Voice Phishing (Vishing) for MFA Bypass**: Social engineering calls trick users into enrolling attacker-controlled Entra passkeys
- **Cryptographic Entropy Flaw Exploitation**: Ill Bloom flaw in recovery phrase generation enables private key derivation and wallet draining
- **Web Portal Compromise for Espionage**: Balochistan Police portal weaponized as access vector for multi-group intelligence collection

## Threat Actor Activities

- **Unknown Operator (jscrambler compromise)**: Compromised npm publishing credentials or build pipeline for jscrambler to insert Rust infostealer in version 8.14.0
- **Unknown Operator (Injective Labs compromise)**: Hijacked GitHub repository credentials to publish wallet-stealing npm packages via legitimate CI/CD
- **Active Exploitation Group (Gitea Docker)**: Actively scanning for and exploiting vulnerable Gitea Docker deployments for admin takeover
- **Global Campaign Operators (CMS targeting)**: Coordinated campaign exploiting vulnerable CMS platforms at scale per ACSC alert; attribution not specified
- **Silver Fox (China-linked cybercrime group)**: Deploying MODBEACON RAT with gRPC streaming C2; attributed by QiAnXin researchers
- **WP-SHELLSTORM Crew**: Cybercrime group operating automated WordPress backdoor campaign; exposed via their own misconfigured server left open for three weeks
- **Vishing Operators (Entra Passkey)**: Conducting voice-based social engineering across multiple sectors to enroll attacker-controlled passkeys
- **Ill Bloom Exploiters**: Actively draining cryptocurrency wallets (>$5M stolen) by exploiting recovery phrase generation flaws
- **China-Aligned APT Actors**: Suspected attribution for espionage against Balochistan Police portal and Pakistani law enforcement
- **India-Aligned APT Actors**: Suspected second attribution for same Balochistan Police portal espionage campaigns
- **Binarly Researchers**: Discovered and disclosed six U-Boot vulnerabilities; not threat actors but relevant to defensive posture
- **Ledger Donjon Researchers**: Demonstrated Tangem wallet laser attack; not threat actors but revealed unpatchable hardware risk
- **Coinspect Researchers**: Disclosed Ill Bloom vulnerability; not threat actors but confirmed active exploitation
- **FoxIO Researchers**: Disclosed unpatched XRING flaw in XQUIC; not threat actors

## Source Attribution

- **Compromised jscrambler 8.14.0 npm Release Drops Rust Infostealer During Install**: The Hacker News - https://thehackernews.com/2026/07/compromised-jscrambler-8140-npm-release.html
- **Hackers Weaponize Balochistan Police Portal in Multi-Group Espionage Campaigns**: The Hacker News - https://thehackernews.com/2026/07/hackers-weaponize-balochistan-police.html
- **Australia warns of global campaign targeting vulnerable CMS platforms**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/australia-warns-of-global-campaign-targeting-vulnerable-cms-platforms/
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
