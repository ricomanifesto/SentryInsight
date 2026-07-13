# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are being actively exploited across diverse technology stacks, from content management systems and email collaboration platforms to firmware bootloaders. CISA has added two maximum-severity Joomla extension flaws—iCagenda and Balbooa Forms—to its Known Exploited Vulnerabilities catalog, confirming active zero-day exploitation. Simultaneously, a critical authentication bypass in the official Gitea Docker image allows attackers to impersonate any user including administrators, while Progress Software has urgently directed ShareFile customers to shut down Storage Zone Controllers in response to a credible external threat. A critical Zimbra Classic Web Client flaw enables arbitrary code execution via crafted emails, and six newly disclosed U-Boot bootloader vulnerabilities threaten stealthy firmware-level compromise across routers, cameras, and data center management hardware.

Threat actor activity remains intense and multi-faceted. Russian state-sponsored groups continue targeting critical infrastructure through vulnerable routers, prompting a joint warning from the United States and eight allies. The GRU has been formally sanctioned by the EU and UK for coordinating a network of hacking groups across Europe. Chinese and Indian-aligned actors are conducting sustained espionage against Pakistani law enforcement via the Balochistan Police Portal. On the cybercrime front, the Forg365 phishing-as-a-service operation combines device code phishing with adversary-in-the-middle session theft against Microsoft 365, while three distinct Evilginx campaigns were exposed through a misconfigured server. Supply chain attacks have compromised the jscrambler npm package (version 8.14.0) to deliver a Rust-based infostealer and the Injective Labs GitHub repository to publish wallet-key-stealing npm packages.

Novel attack techniques are emerging rapidly. The RedHook Android malware now abuses Wireless ADB for shell-level access without a computer connection. An unknown intruder employed a suspected AI-generated PowerShell script for Active Directory enumeration. The "Ghostcommit" technique hides prompt injections in PNG images to fool AI code reviewers and exfiltrate repository secrets. Healthcare service providers have seen attacks more than double in the first half of 2026. Law enforcement actions continue: UK authorities charged five suspects linked to the Russian Coms caller ID spoofing platform responsible for 1.8 million scam calls, and a Ryuk ransomware member pleaded guilty in the United States.

## Active Exploitation Details

### iCagenda and Balbooa Forms Joomla Zero-Day Exploits
- **Description**: Two maximum-severity security flaws affecting the iCagenda and Balbooa Forms extensions for the Joomla content management system. Both vulnerabilities have been added to CISA's Known Exploited Vulnerabilities catalog, confirming active exploitation in the wild as zero-days.
- **Impact**: Attackers can exploit these flaws to compromise Joomla websites, potentially leading to full site takeover, data theft, and further lateral movement within hosting environments.
- **Status**: Actively exploited as zero-days; CISA has mandated federal agencies to remediate. Joomla administrators should apply updates immediately.

### Critical Gitea Docker Image Authentication Bypass
- **Description**: A critical vulnerability in the official Docker image for Gitea, the self-hosted Git service, allows attackers to bypass authentication and impersonate any user on the instance, including administrators.
- **Impact**: Full account takeover of any Gitea user, including administrative accounts, leading to source code theft, supply chain compromise via malicious commits, and persistent access to development infrastructure.
- **Status**: Actively exploited in the wild. Users of the official Gitea Docker image must update immediately and review access logs for unauthorized administrative activity.

### Progress ShareFile Storage Zone Controller Credible Threat
- **Description**: Progress Software has identified a credible external security threat targeting ShareFile customers who operate Storage Zone Controllers on Windows servers. The vendor has instructed all affected customers to immediately shut down these controllers.
- **Impact**: Potential compromise of file storage and sharing infrastructure, unauthorized access to sensitive corporate documents, and possible lateral movement into connected environments.
- **Status**: Active threat confirmed by vendor; emergency mitigation (shutdown of Storage Zone Controllers) required pending patches or further guidance.

### Critical Zimbra Classic Web Client Code Execution
- **Description**: A critical vulnerability in the Zimbra Classic Web Client allows crafted emails to execute arbitrary code within user sessions. The flaw resides in how the web client processes email content.
- **Impact**: Arbitrary code execution in the context of the victim user's session, enabling account compromise, data exfiltration, and potential privilege escalation within the Zimbra environment.
- **Status**: Zimbra is urging customers to apply updates immediately. Exploitation requires user interaction with a malicious email.

### U-Boot Bootloader Vulnerabilities (Six Flaws)
- **Description**: Researchers at Binarly discovered six vulnerabilities in U-Boot, the widely used universal bootloader found in home routers, smart cameras, IoT devices, and management chips inside data center servers. The flaws can be triggered via malicious boot images.
- **Impact**: Attackers with physical access or supply chain influence can execute malicious code during device boot, enabling persistent, stealthy firmware-level implants that survive OS reinstallation and hard drive replacement.
- **Status**: Vulnerabilities disclosed; patching requires firmware updates from device vendors. Exploitation currently requires local/physical access or compromised supply chain, but represents a critical long-term risk.

## Affected Systems and Products

- **Joomla with iCagenda Extension**: All versions prior to patched release; Joomla CMS websites using the iCagenda event management component
- **Joomla with Balbooa Forms Extension**: All versions prior to patched release; Joomla CMS websites using the Balbooa Forms builder component
- **Gitea Docker Image**: Official Docker images prior to patched version; self-hosted Git service deployments using containerized Gitea
- **Progress ShareFile Storage Zone Controllers**: Windows servers running Storage Zone Controller components for ShareFile on-premises/hybrid deployments
- **Zimbra Collaboration Suite**: Classic Web Client installations prior to security update; on-premises email and collaboration deployments
- **U-Boot Bootloader Devices**: Home routers, smart cameras, IoT gateways, and server management controllers (BMCs) using affected U-Boot versions; numerous vendors and hardware platforms
- **Microsoft 365 Tenants**: Organizations targeted by Forg365 PhaaS, Evilginx campaigns, and device code phishing operations
- **Android Devices**: Devices with Wireless Debugging (Wireless ADB) enabled, targeted by RedHook malware
- **npm/Jscrambler Users**: Developers and CI/CD pipelines that installed jscrambler version 8.14.0
- **Injective Labs SDK Users**: Developers using compromised npm packages published from the hijacked GitHub repository
- **Pakistani Law Enforcement Systems**: Balochistan Police Portal and connected infrastructure
- **Content Management Systems Globally**: Vulnerable CMS platforms and plugins targeted in global exploitation campaign warned by ACSC

## Attack Vectors and Techniques

- **Device Code Phishing**: Forg365 PhaaS abuses the OAuth device authorization flow to trick users into granting access to attacker-controlled applications, bypassing traditional credential harvesting.
- **Adversary-in-the-Middle (AitM) Session Theft**: Forg365 and Evilginx frameworks proxy legitimate authentication sessions, capturing session tokens and MFA cookies to bypass multi-factor authentication.
- **Authentication Bypass via Docker Configuration**: Gitea Docker image flaw allows unauthenticated attackers to assume any user identity through manipulated requests to the containerized service.
- **AI-Generated PowerShell for Active Directory Enumeration**: Unknown threat actor deployed a suspected LLM-written PowerShell script to map domain controllers, enumerate users/groups, and identify high-value targets.
- **Wireless ADB Exploitation**: RedHook malware abuses Android's Wireless Debugging feature to gain shell-level access without physical USB connection, enabling remote device control.
- **Supply Chain Compromise (npm Preinstall Hook)**: Malicious jscrambler 8.14.0 package executes a Rust-based infostealer during `npm install` via a preinstall script, harvesting credentials and cryptocurrency wallets.
- **GitHub Repository Hijacking**: Attackers compromised Injective Labs' GitHub repository to publish malicious npm packages that steal cryptocurrency private keys from developers' environments.
- **Prompt Injection via Steganography (Ghostcommit)**: Malicious PNG images containing hidden prompt injections fool AI code review agents (CodeRabbit, Bugbot) into exfiltrating repository secrets during automated reviews.
- **Caller ID Spoofing Platform (Russian Coms)**: Criminal service enabling 1.8 million scam calls by falsifying caller ID information, facilitating social engineering and fraud.
- **Evilginx Phishing Framework Deployment**: Three distinct campaigns used Evilginx reverse-proxy phishing kits hosted on a misconfigured Python web server with directory listing enabled, targeting Microsoft 365 credentials.
- **Malicious Boot Image Firmware Attack**: U-Boot vulnerabilities allow code execution during the boot process via crafted firmware images, enabling persistent pre-OS compromise.
- **Critical Infrastructure Router Exploitation**: Russian state actors target vulnerable and poorly configured edge routers to gain initial access to critical infrastructure networks.
- **Crafted Email Code Execution**: Zimbra flaw triggered by malicious email content rendered in the Classic Web Client, requiring victim to view/open the message.

## Threat Actor Activities

- **Russian GRU (Main Intelligence Directorate)**: Sanctioned by EU and UK for coordinating a network of hacking groups responsible for cyberattacks across Europe. Attributed to critical infrastructure targeting, espionage, and disruptive operations.
- **Russian State-Sponsored Critical Infrastructure Actors**: Targeting vulnerable routers across critical infrastructure sectors in the US and allied nations. Joint advisory from nine countries (US, UK, Canada, Australia, New Zealand, Germany, Netherlands, Poland, Latvia) details TTPs and mitigations.
- **Forg365 PhaaS Operators**: Running a commercial phishing-as-a-service platform combining device code phishing, AitM session theft, anti-bot evasion, and AI-assisted lure generation. Actively targeting Microsoft 365 tenants globally.
- **Evilginx Campaign Operators (Three Distinct Groups)**: Running concurrent Microsoft 365 phishing operations exposed via a single misconfigured server. Each campaign used customized Evilginx phishlets and lure themes.
- **China-Aligned Threat Actors**: Suspected involvement in sustained cyber espionage against Pakistani law enforcement via the Balochistan Police Portal, alongside Indian-aligned groups.
- **India-Aligned Threat Actors**: Suspected involvement in the same multi-group espionage campaigns targeting Balochistan Police Portal and related Pakistani organizations.
- **RedHook Malware Developers/Operators**: Actively updating Android banking/remote access trojan with novel Wireless ADB exploitation technique for shell access without computer tethering.
- **Unknown Actor (jscrambler Supply Chain)**: Compromised the jscrambler npm package publishing pipeline to inject version 8.14.0 with a Rust infostealer preinstall hook. Attribution unknown.
- **Unknown Actor (Injective Labs GitHub Compromise)**: Hijacked the Injective Labs SDK GitHub repository to publish wallet-key-stealing npm packages. Targeting cryptocurrency developers and users.
- **Unknown Actor (AI-Generated PowerShell AD Enumeration)**: Conducted intrusion using a suspected vibe-coded PowerShell script for Active Directory reconnaissance. Script characteristics suggest LLM authorship.
- **Russian Coms Platform Operators**: Ran a major caller ID spoofing service (Russian Coms) facilitating 1.8 million scam calls. Five suspects charged by UK NCA; platform infrastructure disrupted.
- **Ryuk Ransomware Affiliate**: Armenian national pleaded guilty in US court to hacking companies and deploying Ryuk ransomware. Faces up to 15 years imprisonment.
- **Dutch Hackers (Suspected)**: Dutch National Police found "strong indications" of Dutch threat actor involvement in the February 2026 breach of telecommunications provider Odido.

## Source Attribution

- **Lidl discloses online shop breach after service provider hack**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/lidl-discloses-online-shop-breach-after-service-provider-hack/
- **Breach at the Beach: Play the Ultimate Entra ID CTF**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/breach-at-the-beach-play-the-ultimate-entra-id-ctf/
- **UK charges suspects linked to Russian Coms call spoofing platform**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/uk-charges-suspects-linked-to-russian-coms-call-spoofing-platform/
- **Forg365 PhaaS Targets Microsoft 365 with Device Code and AitM Session Theft**: The Hacker News - https://thehackernews.com/2026/07/forg365-phaas-targets-microsoft-365.html
- **Turning the Tables on Email Scammers With 'ScamBuster'**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/turning-tables-email-scammers-scambuster
- **Meta Files Patent for AI That Can Listen All Day and Track How You're Feeling**: The Hacker News - https://thehackernews.com/2026/07/meta-files-patent-for-ai-that-can.html
- **Thinking Fast and Slow in the SOC: The Case for Combining Autonomous AI with Analyst Copilots**: The Hacker News - https://thehackernews.com/2026/07/thinking-fast-and-slow-in-soc-case-for.html
- **EU sanctions Russian GRU military hackers over cyberattacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/eu-and-uk-hit-russia-with-first-joint-cyber-sanctions-package/
- **Attacker Uses Suspected AI-Generated PowerShell Script to Map Active Directory**: The Hacker News - https://thehackernews.com/2026/07/attacker-uses-suspected-ai-generated.html
- **US and allies warn of Russian critical infrastructure attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/us-and-allies-share-defense-tips-against-russian-hackers-targeting-critical-infrastructure/
- **Misconfigured Server Reveals Three Evilginx Phishing Operations Targeting Microsoft 365**: The Hacker News - https://thehackernews.com/2026/07/misconfigured-server-reveals-three.html
- **iCagenda and Balbooa Forms Joomla Flaws Reportedly Exploited as Zero-Days**: The Hacker News - https://thehackernews.com/2026/07/icagenda-and-balbooa-forms-joomla-flaws.html
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
