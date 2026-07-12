# Exploitation Report

## Executive Summary

A significant surge in supply chain attacks has emerged as a dominant threat vector, with multiple npm package compromises and a GitHub repository breach delivering credential-stealing malware to developers and cryptocurrency users. The jscrambler 8.14.0 release was weaponized with a preinstall hook that executes a Rust-based infostealer upon installation, while threat actors compromised the Injective Labs SDK GitHub repository to publish malicious npm packages targeting cryptocurrency wallet private keys. These incidents highlight the continuing risk of software supply chain compromise and the difficulty of detecting malicious code in widely used development dependencies.

Concurrently, critical infrastructure and enterprise software vulnerabilities are under active exploitation. Attackers are leveraging an authentication bypass in the official Gitea Docker image to impersonate administrators, while Progress Software has issued an urgent directive for ShareFile customers to immediately shut down Storage Zone Controllers due to a credible external threat. The Australian Cyber Security Centre has warned of a global campaign targeting vulnerable content management systems and plugins, and an exposed attacker server has revealed the WP-SHELLSTORM operation backdooring thousands of WordPress sites. A novel "Ill Bloom" flaw in cryptocurrency wallet recovery phrase generation has already enabled theft of over $5 million.

Emerging attack techniques demonstrate increasing sophistication in bypassing modern defenses. The "Ghostcommit" technique embeds prompt injections in PNG images to deceive AI code reviewers and exfiltrate repository secrets, while voice-based social engineering campaigns abuse Microsoft Entra passkey enrollment to compromise Microsoft 365 accounts. Research into firmware-level vulnerabilities has uncovered six flaws in the U-Boot bootloader affecting routers, cameras, and management controllers, and a laser fault injection attack can reset Tangem hardware wallet passwords on devices that cannot be patched. An unpatched XRING flaw in Alibaba's XQUIC library allows remote denial-of-service against HTTP/3 servers with no available fix.

## Active Exploitation Details

### Compromised jscrambler npm Package (Version 8.14.0)
- **Description**: The jscrambler npm package version 8.14.0 was compromised with a malicious preinstall hook that executes automatically during package installation. The hook deploys a Rust-based infostealer on the victim's machine.
- **Impact**: Attackers gain unauthorized access to sensitive data on developer machines including credentials, browser data, cryptocurrency wallets, and other confidential information. The attack triggers simply by running `npm install` on the compromised version.
- **Status**: Actively exploited in the wild as of July 11, 2026. The malicious version was published to the npm registry. Users who installed version 8.14.0 should assume compromise and rotate all credentials.

### Injective Labs GitHub Repository Compromise
- **Description**: Unknown threat actors compromised the Injective Labs SDK project's GitHub repository and used it to publish a malicious package to the npm registry designed to steal cryptocurrency wallet private keys.
- **Impact**: Developers and users who installed the malicious npm package had their cryptocurrency wallet private keys exfiltrated, leading to potential theft of digital assets.
- **Status**: Active supply chain attack discovered in July 2026. The compromise of a legitimate GitHub repository to publish to npm represents a significant escalation in supply chain threat tactics.

### Gitea Docker Image Authentication Bypass
- **Description**: A critical vulnerability in the official Docker image for Gitea (self-hosted Git service) allows attackers to bypass authentication and impersonate any user, including administrators.
- **Impact**: Full administrative access to Gitea instances, enabling source code theft, repository manipulation, supply chain poisoning, and lateral movement within development environments.
- **Status**: Actively exploited in the wild as of July 2026. The vulnerability exists in the official Docker image distribution.

### Progress ShareFile Storage Zone Controller Threat
- **Description**: Progress Software has identified a "credible external security threat" affecting ShareFile Storage Zone Controllers running on Windows servers, prompting an urgent directive for customers to immediately shut down affected servers.
- **Impact**: Potential unauthorized access to sensitive file sharing infrastructure, data exfiltration, and compromise of enterprise file transfer operations.
- **Status**: Active threat response in progress as of July 2026. No patch available; mitigation requires immediate server shutdown.

### Zimbra Classic Web Client Critical Vulnerability
- **Description**: A critical vulnerability in the Zimbra Classic Web Client allows crafted emails to execute malicious code in user sessions. The flaw affects the web client used to access the Zimbra Collaboration suite.
- **Impact**: Arbitrary code execution in the context of the user's session, enabling account takeover, data theft, and potential lateral movement within organizational email systems.
- **Status**: Actively exploited. Zimbra is urging customers to apply updates immediately. The vulnerability affects the Classic Web Client component.

### WP-SHELLSTORM WordPress Backdoor Campaign
- **Description**: An exposed attacker server revealed the inner workings of the WP-SHELLSTORM operation, which has backdoored thousands of WordPress sites. The server contained hacking tools, activity logs, and target lists.
- **Impact**: Persistent access to compromised WordPress sites enabling data theft, SEO spam, malware distribution, and use as pivot points for further attacks.
- **Status**: Active campaign discovered in July 2026. Thousands of WordPress sites confirmed compromised. The exposed server provided intelligence on the operation's scope and tooling.

### Ill Bloom Cryptocurrency Wallet Vulnerability
- **Description**: A flaw dubbed "Ill Bloom" exists in how some cryptocurrency wallet software generates recovery phrases (seed words). Attackers are actively exploiting this vulnerability to drain funds from affected wallets.
- **Impact**: Over $5 million stolen from cryptocurrency wallets as of the disclosure date. The vulnerability allows attackers to derive or predict recovery phrases, granting full control over victim wallets.
- **Status**: Actively exploited in the wild. Disclosed by security firm Coinspect in July 2026. Affected wallet software vendors need to address the entropy/generation flaw.

### Global CMS Exploitation Campaign
- **Description**: The Australian Cyber Security Centre (ACSC) has issued an alert regarding a global exploitation campaign targeting vulnerable content management systems and plugins.
- **Impact**: Mass compromise of websites running outdated or vulnerable CMS platforms and plugins, leading to data breaches, malware hosting, and infrastructure hijacking.
- **Status**: Active global campaign as of July 2026. ACSC alert indicates widespread targeting across multiple sectors and geographies.

### Ghostcommit AI Code Reviewer Bypass
- **Description**: A technique called "Ghostcommit" hides prompt injections within PNG images that are not opened or analyzed by AI code review tools (specifically CodeRabbit and Bugbot). When processed by AI agents, the hidden prompts cause the AI to exfiltrate repository secrets.
- **Impact**: Theft of sensitive repository data including API keys, credentials, and proprietary code. The attack bypasses automated security review processes that organizations rely on.
- **Status**: Demonstrated as a practical attack technique in July 2026. Represents a novel class of attacks targeting AI-assisted development workflows.

### Microsoft Entra Passkey Enrollment Social Engineering
- **Description**: Threat actors are conducting voice-based (vishing) attacks that impersonate security requests, prompting Microsoft 365 users to enroll a new Microsoft Entra passkey controlled by the attacker.
- **Impact**: Full account takeover of Microsoft 365 users, enabling access to email, documents, Teams, and other organizational resources. Multi-sector targeting reported.
- **Status**: Active campaign as of July 2026. Exploits the legitimate passkey enrollment flow combined with social engineering.

## Affected Systems and Products

- **jscrambler npm package**: Version 8.14.0 specifically; JavaScript/Node.js development environments using this obfuscation tool
- **Injective Labs SDK**: GitHub repository and associated npm packages; blockchain/cryptocurrency development workflows
- **Gitea Docker image**: Official Docker Hub distribution; self-hosted Git service deployments using containerized installations
- **Progress ShareFile Storage Zone Controllers**: Windows Server installations running the Storage Zone Controller component; enterprise file sharing infrastructure
- **Zimbra Collaboration Suite**: Classic Web Client component; on-premises and hosted Zimbra email deployments
- **WordPress**: Sites with vulnerable plugins/themes/core; thousands confirmed compromised in WP-SHELLSTORM campaign
- **Cryptocurrency wallet software**: Multiple wallet implementations with flawed recovery phrase generation (specific products not named in disclosure)
- **Content Management Systems**: Multiple CMS platforms and plugins globally; specific platforms not enumerated in ACSC alert
- **AI code review tools**: CodeRabbit, Bugbot, and potentially other AI-assisted code review platforms vulnerable to image-based prompt injection
- **Microsoft Entra ID / Microsoft 365**: Organizations using passkey authentication; users across multiple industry sectors
- **U-Boot bootloader**: Versions containing the six discovered flaws; embedded devices including home routers, smart cameras, and server management controllers (BMCs)
- **Tangem hardware wallet cards**: Physical crypto wallet cards with vulnerable chips; unpatchable hardware vulnerability
- **OpenClaw AI assistant**: Versions prior to patching of three disclosed flaws; personal AI assistant deployments
- **XQUIC library**: Alibaba's QUIC/HTTP/3 library containing the unpatched XRING flaw; HTTP/3 server implementations using this library

## Attack Vectors and Techniques

- **Software Supply Chain Compromise**: Malicious code injection into legitimate npm packages (jscrambler) and GitHub repository takeover (Injective Labs) to distribute credential-stealing malware to developers
- **Preinstall Hook Abuse**: Leveraging npm's `preinstall` lifecycle script to execute malicious code automatically during package installation without user interaction
- **Docker Image Vulnerability Exploitation**: Targeting authentication flaws in official container images to gain administrative access to Git infrastructure
- **Urgent Infrastructure Shutdown**: Credible threat to file sharing infrastructure requiring immediate operational disruption as mitigation (ShareFile)
- **Email-Based Client-Side Code Execution**: Crafted emails exploiting web client vulnerabilities to achieve arbitrary code execution in user sessions (Zimbra)
- **Mass CMS/Plugin Exploitation**: Automated scanning and exploitation of known vulnerabilities in content management systems and their plugin ecosystems
- **WordPress Backdoor Deployment**: Large-scale compromise of WordPress sites with persistent backdoors for ongoing access and monetization
- **Cryptographic Entropy Weakness**: Exploitation of flawed recovery phrase generation in wallet software enabling seed phrase prediction/derivation
- **Image-Based Prompt Injection**: Embedding malicious prompts in PNG images that exploit AI code reviewers' multimodal processing to exfiltrate secrets
- **Voice Phishing (Vishing) with Passkey Abuse**: Social engineering via phone calls combined with legitimate authentication flows (Entra passkey enrollment) for account takeover
- **Firmware-Level Bootloader Exploitation**: Six vulnerabilities in U-Boot enabling code execution during device boot process on embedded/IoT devices
- **Laser Fault Injection**: Physical attack using precisely timed laser pulses to induce hardware faults and reset authentication on unpatchable devices
- **AI Assistant Attack Chain**: Chaining multiple vulnerabilities in AI assistant software (OpenClaw) for credential theft and privilege escalation from messaging platforms
- **Encrypted C2 via gRPC Streaming**: Rust-based RAT (MODBEACON) using gRPC streaming for stealthy command-and-control communications
- **HTTP/3 Denial-of-Service**: Unpatched flaw in QUIC library allowing remote server crash with minimal legitimate traffic

## Threat Actor Activities

- **Unknown/Unattributed Supply Chain Actors**: Compromised jscrambler npm package and Injective Labs GitHub repository; motivation appears to be credential theft and cryptocurrency wallet key stealing; capabilities include registry publishing and repository compromise
- **Silver Fox (China-linked cybercrime group)**: Attributed to the MODBEACON RAT, a Rust-based remote access trojan using gRPC streaming for encrypted C2 traffic; active development of custom malware tooling
- **WP-SHELLSTORM Operators**: Cybercrime crew operating a large-scale WordPress backdoor campaign; exposed server revealed tools, logs, and target lists spanning thousands of compromised sites; operational security failure led to intelligence exposure
- **China- and India-Aligned Espionage Groups**: Sustained cyber espionage against Pakistani law enforcement organizations; weaponized Balochistan Police portal; multi-group activity suggesting possible coordination or parallel operations
- **Microsoft 365 Vishing Operators**: Threat actors conducting voice-based social engineering across multiple sectors to abuse Entra passkey enrollment; fluent in security terminology and procedures to appear legitimate
- **Global CMS Exploitation Campaign Operators**: Unattributed group(s) conducting worldwide scanning and exploitation of vulnerable CMS platforms and plugins; ACSC alert indicates organized, large-scale activity
- **Ill Bloom Exploiters**: Active attackers draining cryptocurrency wallets (over $5 million stolen); exploiting entropy flaws in recovery phrase generation; likely technically sophisticated given cryptographic nature of attack
- **Gitea Docker Exploiters**: Actively exploiting authentication bypass in official Docker image; targeting self-hosted Git infrastructure for source code access and supply chain positioning

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
