# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are being actively exploited across diverse technology stacks, from AI-assisted development tools to enterprise collaboration platforms and firmware infrastructure. The most immediately dangerous activity involves active exploitation of a critical authentication bypass in the official Gitea Docker image, allowing attackers to impersonate any user including administrators, and the "Ill Bloom" cryptocurrency wallet flaw that has already drained over $5 million from victim wallets. Progress Software has issued an emergency directive for ShareFile customers to immediately shut down Storage Zone Controllers due to a credible external security threat, while Zimbra has released patches for a critical XSS vulnerability in its Classic Web Client that enables arbitrary code execution via crafted emails.

A new supply chain attack compromised the Injective Labs GitHub repository to publish malicious npm packages targeting cryptocurrency wallet private keys, and an exposed hacker server revealed the WP-SHELLSTORM campaign backdooring thousands of WordPress sites. Researchers disclosed six vulnerabilities in the widely deployed U-Boot bootloader affecting routers, cameras, and data center management chips, alongside an unpatchable hardware flaw in Tangem crypto wallets exploitable via laser fault injection. Threat actors are employing novel techniques including image-based prompt injection against AI code reviewers (Ghostcommit), voice-based social engineering to enroll malicious Microsoft Entra passkeys, and a new Rust-based RAT (MODBEACON) using gRPC streaming for encrypted command-and-control attributed to the China-linked Silver Fox group.

## Active Exploitation Details

### Gitea Docker Image Authentication Bypass
- **Description**: A critical vulnerability in the official Docker image for Gitea, the self-hosted Git service, allows attackers to bypass authentication entirely and impersonate any user on the system, including administrators with full repository access.
- **Impact**: Attackers gain complete control over repositories, can modify code, inject malicious commits, access secrets and credentials stored in repositories, and potentially pivot to supply chain attacks against downstream consumers of the Git service.
- **Status**: Actively exploited in the wild. Users of the official Gitea Docker image should update immediately and audit for unauthorized access.

### Ill Bloom Cryptocurrency Wallet Vulnerability
- **Description**: A flaw in how certain cryptocurrency wallet software generates recovery phrases (seed words), disclosed by security firm Coinspect as "Ill Bloom," creates predictable or weak entropy in the key derivation process.
- **Impact**: Attackers can brute-force or predict recovery phrases to drain cryptocurrency wallets. Over $5 million has already been stolen from victim wallets through active exploitation of this vulnerability.
- **Status**: Actively exploited. Wallet users should verify their software is not affected and migrate funds if using vulnerable implementations.

### Progress ShareFile Storage Zone Controller Threat
- **Description**: Progress Software has identified a "credible external security threat" targeting ShareFile Storage Zone Controllers running on Windows servers, prompting an emergency directive to immediately shut down affected servers.
- **Impact**: Potential unauthorized access to sensitive file sharing and storage infrastructure used by enterprises for secure document exchange. The specific vulnerability details have not been publicly disclosed due to the active threat.
- **Status**: Active threat confirmed by vendor. Immediate shutdown of Storage Zone Controllers recommended until patches are released.

### Zimbra Classic Web Client XSS Vulnerability
- **Description**: A critical cross-site scripting (XSS) vulnerability in the Zimbra Collaboration Suite's Classic Web Client that can be triggered via crafted emails, leading to arbitrary code execution in user sessions.
- **Impact**: Attackers can execute malicious JavaScript in the context of authenticated users, potentially leading to session hijacking, credential theft, email exfiltration, and further lateral movement within the organization.
- **Status**: Patches available. Zimbra is urging all customers to apply updates immediately.

### Injective Labs GitHub Repository Compromise
- **Description**: Unknown threat actors compromised the Injective Labs SDK project's GitHub repository and leveraged it to publish a malicious package on the npm registry designed to steal cryptocurrency wallet private keys.
- **Impact**: Developers and projects using the compromised Injective Labs SDK packages inadvertently introduced wallet-stealing malware into their applications, affecting downstream users and potentially draining cryptocurrency holdings.
- **Status**: Malicious packages identified and reported. Affected developers should audit dependencies and rotate any exposed keys.

### WP-SHELLSTORM WordPress Backdoor Campaign
- **Description**: A cybercrime operation dubbed WP-SHELLSTORM has been backdooring thousands of WordPress sites, with an exposed command-and-control server revealing hacking tools, activity logs, and extensive target lists.
- **Impact**: Persistent access to compromised WordPress installations, enabling data theft, SEO spam, malware distribution todexing, defacement, and use as pivot points for further attacks. Thousands of sites confirmed compromised.
- **Status**: Active campaign. Server exposure has disrupted operations but compromised sites remain backdoored until cleaned.

### U-Boot Bootloader Vulnerabilities (Six Flaws)
- **Description**: Researchers at Binarly discovered six vulnerabilities in U-Boot, the universal bootloader used across embedded devices including home routers, smart cameras, and baseboard management controllers in data center servers.
- **Impact**: Attackers with physical access or supply chain position can execute malicious code during the boot process, enabling persistent firmware implants that survive OS reinstallation and disk replacement. Malicious firmware images can crash devices or achieve code execution at the highest privilege level.
- **Status**: Disclosed to maintainers. Patches in progress. Wide deployment across vendor ecosystems complicates remediation.

### Tangem Wallet Laser Fault Injection
- **Description**: Researchers at Ledger's Donjon security team demonstrated that a precisely timed laser pulse aimed at the chip inside a Tangem crypto wallet card can reset the card's password to an attacker-chosen value.
- **Impact**: Physical attackers can bypass all authentication and gain full control of the cryptocurrency wallet. The vulnerability is in hardware and cannot be patched via software updates.
- **Status**: Unpatchable hardware flaw. Users should consider affected devices compromised if physical access is possible.

### OpenClaw AI Assistant Vulnerability Chain
- **Description**: Three now-patched security flaws in the OpenClaw personal AI assistant that, when chained together, enable a WhatsApp-to-host attack path allowing credential theft and privilege escalation.
- **Impact**: Attackers could leverage the AI assistant's integration with WhatsApp to escape containment and execute code on the host system, stealing credentials and escalating privileges.
- **Status**: Patched in recent updates. Users should ensure OpenClaw is updated to the latest version.

## Affected Systems and Products

- **Gitea Docker Image**: Official Docker Hub images for Gitea self-hosted Git service; all versions prior to patched release affected
- **Cryptocurrency Wallets (Ill Bloom)**: Wallet implementations with flawed recovery phrase generation; specific affected products not publicly named pending responsible disclosure
- **Progress ShareFile Storage Zone Controllers**: Windows servers running Storage Zone Controller components for ShareFile on-premises/hybrid deployments
- **Zimbra Collaboration Suite**: Classic Web Client component; all versions prior to security patch releases
- **Injective Labs SDK**: npm packages published from compromised GitHub repository; versions published during compromise window
- **WordPress Sites**: Thousands of installations compromised via WP-SHELLSTORM campaign; all unpatched or misconfigured WordPress instances potentially at risk
- **U-Boot Bootloader**: Widely deployed across embedded Linux devices including home routers (consumer and enterprise), IP cameras, IoT devices, and server baseboard management controllers (BMCs)
- **Tangem Crypto Wallet Cards**: Hardware wallet cards with vulnerable secure element chips; all cards of affected hardware revisions
- **OpenClaw AI Assistant**: Personal AI assistant software with WhatsApp integration; versions prior to security patches

## Attack Vectors and Techniques

- **Ghostcommit (Image-Based Prompt Injection)**: Malicious PNG images containing hidden prompt injections that fool AI code reviewers (CodeRabbit, Bugbot) into executing unintended actions, including exfiltrating repository secrets. The technique exploits the fact that AI reviewers process image content but human reviewers do not.
- **Authentication Bypass via Docker Configuration**: Exploitation of misconfiguration or vulnerability in the official Gitea Docker image allowing unauthenticated attackers to assume any user identity, including administrators.
- **Supply Chain Compromise (GitHub → npm)**: Threat actors compromise legitimate GitHub repositories to publish malicious packages to npm registry, targeting downstream developers and cryptocurrency users.
- **Crafted Email XSS Delivery**: Malicious emails sent to Zimbra users exploit XSS in the Classic Web Client to execute code in victim browsers upon email viewing.
- **Voice-Based Social Engineering (Vishing)**: Attackers use phone calls posing as security personnel to trick Microsoft 365 users into enrolling attacker-controlled Entra passkeys, granting persistent access.
- **Laser Fault Injection**: Precisely timed laser pulses targeting secure element chips to induce computational faults that bypass authentication mechanisms (Tangem wallets).
- **Firmware Image Manipulation**: Malicious U-Boot firmware images crafted to exploit parser vulnerabilities during boot, achieving code execution before OS load.
- **gRPC Streaming for C2**: MODBEACON RAT uses gRPC bidirectional streaming to establish encrypted command-and-control channels that blend with legitimate traffic and evade traditional network monitoring.
- **Recovery Phrase Entropy Reduction**: Ill Bloom vulnerability reduces entropy in BIP-39 seed phrase generation, enabling practical brute-force attacks on cryptocurrency wallets.
- **WordPress Backdoor Deployment**: WP-SHELLSTORM campaign uses automated tooling to identify vulnerable WordPress sites, deploy persistent backdoors, and maintain centralized control via exposed C2 infrastructure.

## Threat Actor Activities

- **Silver Fox (China-linked Cybercrime Group)**: Attributed to the development and deployment of MODBEACON, a new Rust-based remote access trojan using gRPC streaming for encrypted command-and-control. QiAnXin researchers link this group to ongoing cybercrime operations targeting multiple sectors.
- **WP-SHELLSTORM Operators**: Cybercrime crew operating a large-scale WordPress compromise campaign. An exposed server revealed their tooling, activity logs spanning three weeks, and target lists naming thousands of compromised sites across multiple countries.
- **Unknown Threat Actors (Injective Labs Compromise)**: Unidentified group compromised the Injective Labs GitHub repository and published wallet-stealing npm packages. Attribution remains unknown; operation suggests financially motivated actors targeting cryptocurrency ecosystem.
- **Ryuk Ransomware Affiliate**: 34-year-old Armenian national pleaded guilty to deploying Ryuk ransomware against U.S. companies. Sentencing pending (faces 15 years). Indicates continued law enforcement pressure on ransomware affiliates.
- **BlackCat/ALPHV Ransomware Insider**: Former DigitalMint ransomware negotiator sentenced to 70 months in prison for conspiring with BlackCat operators to attack U.S. companies. Rare case of insider threat from incident response industry.
- **Dutch Hackers (Odido Breach)**: Dutch National Police have "strong indications" that Dutch hackers were involved in the February 2026 breach of telecommunications provider Odido. Investigation ongoing.
- **OpenMandriva Saboteur**: Internal contributor attempted to sabotage the OpenMandriva Linux project following a dispute. Insider threat detected and mitigated before damage occurred.
- **Bulgarian Money Launderer**: Charged with stealing $290,000 in government-seized cryptocurrency while serving 121-month sentence for laundering millions from U.S. fraud victims. Demonstrates persistent criminal capability even from prison.

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
