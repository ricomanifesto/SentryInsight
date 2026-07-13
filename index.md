# Exploitation Report

## Executive Summary

Active exploitation campaigns are intensifying across multiple vectors, with threat actors targeting critical infrastructure, supply chains, and emerging AI-driven attack surfaces. A credible external security threat has forced Progress Software to instruct ShareFile customers to immediately shut down Storage Zone Controllers, while hackers are actively exploiting a critical authentication bypass in the official Gitea Docker image to impersonate administrators. Simultaneously, supply chain compromises have struck the jscrambler npm package and Injective Labs' GitHub repository, deploying infostealers and wallet-key-stealing malware to downstream users.

Nation-state aligned espionage continues to escalate, with China- and India-aligned groups weaponizing the Balochistan Police Portal in sustained campaigns against Pakistani law enforcement. The Australian Cyber Security Centre has warned of a global exploitation campaign targeting vulnerable CMS platforms and plugins. New attack techniques are emerging rapidly, including the "Ghostcommit" prompt injection method that hides malicious instructions in images to fool AI code reviewers, a laser-based physical attack that resets Tangem hardware wallet passwords on unpatchable devices, and RedHook Android malware's novel abuse of Wireless ADB for shell-level access without a computer connection.

## Active Exploitation Details

### Progress ShareFile Storage Zone Controller Credible Threat
- **Description**: Progress Software identified a credible external security threat affecting ShareFile customers using Storage Zone Controllers on Windows servers. The vendor has instructed all affected customers to immediately shut down their servers while the threat is investigated.
- **Impact**: Potential unauthorized access to file storage systems, data exfiltration, and lateral movement within organizational networks. The urgency of the shutdown directive indicates high severity.
- **Status**: Active threat response in progress; customers directed to power down affected servers immediately. No patch available at time of reporting.

### Gitea Docker Image Authentication Bypass
- **Description**: A critical vulnerability in the official Docker image for the Gitea self-hosted Git service allows attackers to bypass authentication and impersonate any user, including administrators.
- **Impact**: Full administrative control over compromised Gitea instances, enabling repository manipulation, credential theft, supply chain poisoning, and persistent access to source code infrastructure.
- **Status**: Actively exploited in the wild. Users of the official Docker image are at immediate risk.

### Zimbra Classic Web Client Critical Vulnerability
- **Description**: A critical security vulnerability affecting the Zimbra Collaboration Suite Classic Web Client that could allow arbitrary code execution through crafted emails.
- **Impact**: Attackers can execute malicious code in user sessions simply by sending specially crafted emails, leading to session hijacking, data theft, and potential lateral movement.
- **Status**: Zimbra has released patches and is urgently urging customers to apply updates. Exploitation risk is high due to email-based attack vector.

### Compromised jscrambler npm Package (v8.14.0)
- **Description**: The jscrambler npm package version 8.14.0 was compromised with a malicious preinstall hook that executes a Rust-based infostealer during installation.
- **Impact**: Any developer or CI/CD pipeline installing version 8.14.0 executes the infostealer, which can harvest credentials, cryptocurrency wallets, browser data, and other sensitive information from the build machine.
- **Status**: Malicious version published July 11, 2026. Users who installed this version must rotate all credentials and audit systems.

### Injective Labs GitHub Repository Compromise
- **Description**: Unknown threat actors compromised the Injective Labs SDK project's GitHub repository and published a malicious npm package designed to steal cryptocurrency wallet private keys.
- **Impact**: Developers incorporating the compromised SDK or installing the malicious npm package have their wallet private keys exfiltrated, leading to direct cryptocurrency theft.
- **Status**: Malicious package published to npm registry. Investigation ongoing; affected users must revoke compromised keys immediately.

### WP-SHELLSTORM WordPress Backdoor Campaign
- **Description**: A cybercrime operation backdoored thousands of WordPress sites using the WP-SHELLSTORM toolkit. An exposed command-and-control server revealed hacking tools, activity logs, and target lists.
- **Impact**: Persistent administrative access to compromised WordPress sites, enabling content injection, credential harvesting, SEO spam, and use as infrastructure for further attacks.
- **Status**: Campaign active for at least three weeks before server exposure. Thousands of sites confirmed compromised.

## Affected Systems and Products

- **Progress ShareFile Storage Zone Controllers**: Windows servers hosting Storage Zone Controllers for ShareFile file sharing platform; all versions potentially affected pending investigation
- **Gitea Docker Image**: Official Docker image for Gitea self-hosted Git service; specific vulnerable tags not yet enumerated
- **Zimbra Collaboration Suite Classic Web Client**: All versions prior to the latest security patch; affects on-premises deployments using the Classic Web Client interface
- **jscrambler npm Package**: Version 8.14.0 specifically; any project or CI/CD pipeline that installed this version during the compromise window
- **Injective Labs SDK**: GitHub repository and associated npm packages; developers who cloned the repository or installed packages after compromise
- **WordPress Sites**: Thousands of WordPress installations compromised via WP-SHELLSTORM backdoor; affects sites with vulnerable plugins, themes, or weak credentials
- **Android Devices**: Devices with Wireless Debugging (Wireless ADB) enabled, targeted by RedHook malware for shell-level access
- **Tangem Hardware Wallet Cards**: Physical wallet cards vulnerable to laser fault injection attacks that reset passwords; cannot be patched due to hardware design
- **XQUIC HTTP/3 Library**: Alibaba's QUIC and HTTP/3 library (XQUIC) containing the unpatched XRING flaw; affects any server using XQUIC for HTTP/3
- **U-Boot Bootloader**: Widely deployed bootloader across embedded devices including home routers, smart cameras, and data center management chips; six newly discovered flaws
- **OpenClaw AI Assistant**: Personal AI assistant software; three now-patched flaws that formed an attack chain from WhatsApp to host compromise
- **CMS Platforms and Plugins**: Various content management systems and plugins targeted in global exploitation campaign warned by Australian Cyber Security Centre

## Attack Vectors and Techniques

- **Credential External Security Threat (ShareFile)**: Progress Software describes a "credible external security threat" targeting Storage Zone Controllers; specific vector under investigation but likely involves exposed management interfaces or authentication flaws
- **Authentication Bypass via Docker Image (Gitea)**: Attackers exploit a flaw in the official Docker image configuration or entrypoint to bypass authentication controls and impersonate any user including administrators
- **Email-Based Code Execution (Zimbra)**: Crafted emails sent to Zimbra users trigger arbitrary code execution in the victim's browser session when viewing messages in the Classic Web Client
- **Supply Chain Compromise (jscrambler)**: Malicious code injected into legitimate npm package's preinstall hook; executes automatically during `npm install` without user interaction beyond package installation
- **GitHub Repository Hijacking (Injective Labs)**: Threat actors gained write access to the Injective Labs SDK repository, modified build/publish pipelines, and pushed malicious packages to npm registry
- **WordPress Backdoor Deployment (WP-SHELLSTORM)**: Automated toolkit installs persistent backdoors on compromised WordPress sites, likely leveraging vulnerable plugins, weak credentials, or unpatched core vulnerabilities
- **Wireless ADB Abuse (RedHook)**: Malware enables Wireless Debugging on Android devices programmatically and connects locally to gain shell access without requiring physical USB connection to a computer
- **Image-Based Prompt Injection (Ghostcommit)**: Malicious instructions embedded in PNG images via steganography or metadata; AI code reviewers (CodeRabbit, Bugbot) process images and execute hidden prompts, exfiltrating repository secrets
- **Laser Fault Injection (Tangem Wallet)**: Precisely timed laser pulse targets the secure element chip during password verification, inducing a fault that resets the password to an attacker-chosen value; requires physical access but leaves no software trace
- **WhatsApp-to-Host Attack Chain (OpenClaw)**: Three chained vulnerabilities in OpenClaw AI assistant allow escalation from a WhatsApp message to credential theft, privilege escalation, and host compromise
- **XRING Denial-of-Service (XQUIC)**: Single malformed variable in QUIC/HTTP/3 implementation allows any remote client to crash the server with a short burst of legitimate-appearing traffic; no authentication required
- **gRPC Streaming C2 (MODBEACON)**: Rust-based RAT uses gRPC streaming for encrypted command-and-control traffic, evading traditional network inspection and blending with legitimate gRPC service traffic
- **Global CMS Exploitation Campaign**: Automated scanning and exploitation of known vulnerabilities in CMS platforms and plugins; likely leveraging public proof-of-concept exploits for recently disclosed flaws

## Threat Actor Activities

- **Silver Fox (China-linked)**: Attributed to the new MODBEACON RAT, a Rust-based remote access trojan using gRPC streaming for encrypted C2 communications. QiAnXin researchers note the group operates as a cybercrime entity with possible state alignment.
- **China- and India-Aligned Espionage Groups**: Sustained cyber espionage campaigns targeting Pakistani law enforcement organizations through the weaponized Balochistan Police Portal. Multiple threat groups suspected of coordinating or operating in parallel.
- **Ryuk Ransomware Affiliate**: 34-year-old Armenian national pleaded guilty in U.S. court to hacking U.S. companies and deploying Ryuk ransomware; faces 15 years in prison. Confirms ongoing affiliate model for Ryuk operations.
- **WP-SHELLSTORM Operators**: Cybercrime crew operating automated WordPress compromise infrastructure; exposed C2 server revealed operational security failures including activity logs and target lists naming thousands of victims.
- **Unknown Actors (jscrambler Compromise)**: Supply chain attackers who injected malicious code into the jscrambler npm package build pipeline; used Rust-based infostealer suggesting sophisticated tooling.
- **Unknown Actors (Injective Labs Compromise)**: Compromised GitHub repository credentials or CI/CD tokens to publish wallet-key-stealing npm packages; targeted cryptocurrency developers and users.
- **Dutch Hackers (Odido Breach)**: Dutch National Police found "strong indications" that Dutch nationals were involved in the February 2026 breach of telecommunications provider Odido; investigation ongoing.
- **Global CMS Campaign Operators**: Threat actors conducting wide-scale exploitation of vulnerable CMS platforms and plugins as warned by Australian Cyber Security Centre; likely opportunistic cybercrime groups leveraging automated tooling.

## Source Attribution

- **OpenAI temporarily relaxes GPT-5.6 Sol usage limits**: Bleeping Computer - https://www.bleepingcomputer.com/news/artificial-intelligence/openai-temporarily-relaxes-gpt-56-sol-usage-limits/
- **Claude Fable 5 stays free for paid users until July 19 as Anthropic buys more time**: Bleeping Computer - https://www.bleepingcomputer.com/news/artificial-intelligence/claude-fable-5-stays-free-for-paid-users-until-july-19-as-anthropic-buys-more-time/
- **RedHook Android malware now uses Wireless ADB for shell access**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/redhook-android-malware-now-uses-wireless-adb-for-shell-access/
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
