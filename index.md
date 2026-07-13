# Exploitation Report

## Executive Summary

Active exploitation activity spans multiple critical vectors this period, with phishing-as-a-service operations, supply chain compromises, and state-sponsored infrastructure targeting dominating the threat landscape. The Forg365 PhaaS platform has elevated Microsoft 365 credential theft through combined device code phishing and adversary-in-the-middle techniques, while three distinct Evilginx pharming campaigns were exposed via a misconfigured server. Simultaneously, CISA added two maximum-severity Joomla extension flaws to its Known Exploited Vulnerabilities catalog, confirming active zero-day exploitation against iCagenda and Balbooa Forms.

Supply chain attacks have intensified with the compromise of the jscrambler npm package (version 8.14.0) delivering a Rust-based infostealer via preinstall hooks, and the Injective Labs GitHub repository breach pushing wallet-key-stealing packages to the npm registry. Russian state actors continue targeting critical infrastructure across NATO allies, focusing on vulnerable routers and network edge devices, while the EU and UK have jointly sanctioned GRU-linked hacking groups. A critical authentication bypass in the official Gitea Docker image is under active exploitation, allowing full administrative impersonation.

## Active Exploitation Details

### Forg365 Phishing-as-a-Service Platform
- **Description**: A new phishing-as-a-service operation combining device code phishing with adversary-in-the-middle (AitM) session theft, featuring anti-bot evasion and AI-assisted phishing content generation
- **Impact**: Full Microsoft 365 account compromise including session token theft, bypassing MFA through device code flow abuse and real-time session relay
- **Status**: Actively operating; targets Microsoft 365 tenants globally

### iCagenda and Balbooa Forms Joomla Zero-Day Exploits
- **Description**: Two maximum-severity security flaws in popular Joomla extensions (iCagenda event management and Balbooa Forms builder) added to CISA's Known Exploited Vulnerabilities catalog
- **Impact**: Remote code execution on Joomla sites running affected extensions; exploited as zero-days prior to disclosure
- **Status**: Actively exploited in the wild; CISA KEV listing mandates federal agency patching

### Evilginx Microsoft 365 Phishing Operations
- **Description**: Three distinct pharming campaigns using the Evilginx framework exposed via a misconfigured Python web server with directory listing enabled on port 8080
- **Impact**: Credential and session token harvesting from Microsoft 365 users through transparent reverse-proxy phishing
- **Status**: Active campaigns discovered; infrastructure details revealed through operational security failure

### Russian Critical Infrastructure Router Campaign
- **Description**: Joint advisory from US and eight allied nations warning of Russian state-sponsored hackers targeting vulnerable and poorly configured routers to infiltrate critical infrastructure networks
- **Impact**: Persistent network access, traffic interception, lateral movement into OT/ICS environments
- **Status**: Ongoing campaign; advisories issued with defensive guidance

### Compromised jscrambler npm Supply Chain Attack
- **Description**: Malicious version 8.14.0 of the jscrambler npm package published on July 11, 2026, containing a preinstall hook that executes a Rust-based infostealer during installation
- **Impact**: Credential theft, cryptocurrency wallet compromise, and system enumeration on any machine installing the compromised package
- **Status**: Malicious package published and available; developers who installed v8.14.0 compromised

### RedHook Android Malware Wireless ADB Exploitation
- **Description**: Updated RedHook malware leveraging Android Wireless Debugging (Wireless ADB) to gain shell-level privileges without requiring physical USB connection to a computer
- **Impact**: Full device control, data exfiltration, and persistent access on Android devices with wireless debugging enabled
- **Status**: Active in the wild; novel exploitation of legitimate developer feature

### Gitea Docker Image Authentication Bypass
- **Description**: Critical vulnerability in the official Gitea Docker image allowing attackers to impersonate any user, including administrators, through authentication bypass
- **Impact**: Complete source code repository compromise, supply chain poisoning, and administrative control of self-hosted Git services
- **Status**: Actively exploited; affects containerized deployments

### Critical Zimbra Classic Web Client Vulnerability
- **Description**: Critical security flaw in Zimbra's Classic Web Client allowing arbitrary code execution through crafted emails
- **Impact**: Remote code execution in user sessions via malicious email delivery; no user interaction beyond viewing required
- **Status**: Zimbra urging immediate updates; exploit potential high

### U-Boot Bootloader Firmware Vulnerabilities
- **Description**: Six vulnerabilities in the widely deployed U-Boot bootloader affecting routers, smart cameras, and server management controllers (BMCs)
- **Impact**: Code execution during early boot process, enabling persistent firmware implants surviving OS reinstallation
- **Status**: Disclosed by Binarly; patches in progress across vendor ecosystem

### Injective Labs GitHub Repository Compromise
- **Description**: Unknown threat actors compromised the Injective Labs SDK GitHub repository to publish malicious npm packages designed to steal cryptocurrency wallet private keys
- **Impact**: Cryptocurrency wallet drainage for developers integrating compromised SDK packages
- **Status**: Malicious packages published to npm; repository compromise confirmed

### Progress ShareFile Storage Zone Controller Threat
- **Description**: Progress Software directed ShareFile customers to immediately shut down Windows servers running Storage Zone Controllers due to a "credible external security threat"
- **Impact**: Potential data exfiltration, encryption, or destruction on affected file sharing infrastructure
- **Status**: Emergency mitigation in progress; root cause under investigation

### Ghostcommit AI Prompt Injection Technique
- **Description**: Novel attack hiding prompt injections in PNG images to manipulate AI code reviewers (CodeRabbit, Bugbot) into exfiltrating repository secrets
- **Impact**: Bypass of AI-powered security tooling; secret theft from private repositories
- **Status**: Proof-of-concept demonstrated; affects AI-assisted development workflows

### AI-Generated PowerShell Active Directory Reconnaissance
- **Description**: Unknown threat actor used suspected AI-generated ("vibe-coded") PowerShell scripts for Active Directory enumeration and domain mapping
- **Impact**: Automated, sophisticated AD reconnaissance at scale; identification of high-value targets and privilege escalation paths
- **Status**: Observed in active intrusion; represents evolution in offensive tooling

### Russian Coms Caller ID Spoofing Platform
- **Description**: Criminal platform "Russian Coms" enabled over 1.8 million scam calls through caller ID spoofing; UK NCA investigation led to five charges
- **Impact**: Mass-scale social engineering, financial fraud, and identity theft via trusted caller ID manipulation
- **Status**: Platform disrupted; suspects charged; infrastructure dismantled

### Balochistan Police Portal Espionage Campaigns
- **Description**: Sustained cyber espionage against Pakistani law enforcement organizations by suspected China- and India-aligned threat actors weaponizing the Balochistan Police portal
- **Impact**: Intelligence collection, credential harvesting, and persistent access to law enforcement systems
- **Status**: Ongoing multi-group campaigns; attribution to opposing geopolitical interests

### Australian CMS Global Exploitation Campaign
- **Description**: ACSC alert regarding worldwide exploitation campaign targeting vulnerable content management systems and plugins
- **Impact**: Web server compromise, defacement, malware hosting, and supply chain attacks via compromised CMS instances
- **Status**: Active global campaign; patching urgency emphasized

### Lidl Service Provider Data Breach
- **Description**: Personal information of Lidl online shop customers in Germany, Belgium, and Netherlands stolen through a breach at a third-party service provider
- **Impact**: PII exposure including names, addresses, email addresses, and order history
- **Status**: Notification issued; service provider breach investigation ongoing

### Odido Telecommunications Breach
- **Description**: Dutch National Police found "strong indications" of Dutch hacker involvement in February breach at telecommunications provider Odido
- **Impact**: Potential access to customer data, call records, and network infrastructure
- **Status**: Criminal investigation active; attribution to domestic threat actors

### Healthcare Sector Attack Surge
- **Description**: Cyberattacks on healthcare service providers and business associates more than doubled in first half of 2026, while hospital/clinic attacks grew modestly
- **Impact**: Disruption of care delivery, patient data exposure, and operational paralysis across healthcare ecosystem
- **Status**: Escalating trend; supply chain targeting prominent

### Ryuk Ransomware Affiliate Prosecution
- **Description**: Armenian national pleaded guilty to hacking US companies and deploying Ryuk ransomware, facing up to 15 years imprisonment
- **Impact**: Precedent for ransomware affiliate prosecution; insight into Ryuk operational structure
- **Status**: Conviction secured; sentencing pending

### EU/UK Sanctions on Russian GRU Hackers
- **Description**: European Union and United Kingdom jointly sanctioned dozens of Russian individuals and entities, accusing Russia of coordinating a network of hacking groups responsible for attacks across Europe
- **Impact**: Diplomatic and financial pressure on Russian cyber operations; attribution of specific GRU units
- **Status**: Sanctions implemented; coordinated transatlantic response

## Affected Systems and Products

- **Microsoft 365 / Entra ID**: Targeted by Forg365 PhaaS (device code phishing + AitM) and three Evilginx phishing campaigns
- **Joomla CMS (iCagenda extension)**: Maximum-severity zero-day exploit; event management component affected
- **Joomla CMS (Balbooa Forms extension)**: Maximum-severity zero-day exploit; form builder component affected
- **Zimbra Collaboration Suite (Classic Web Client)**: Critical RCE via crafted email; webmail interface vulnerable
- **U-Boot Bootloader**: Six firmware vulnerabilities affecting home routers, smart cameras, server BMCs, and embedded devices
- **Gitea (Official Docker Image)**: Authentication bypass allowing full admin impersonation; containerized deployments
- **Progress ShareFile Storage Zone Controllers**: Windows servers hosting on-premises storage zones; emergency shutdown advised
- **Android OS (Wireless ADB)**: RedHook malware abusing wireless debugging feature for shell access
- **npm Registry (jscrambler package v8.14.0)**: Compromised JavaScript obfuscation library with malicious preinstall hook
- **GitHub / npm (Injective Labs SDK)**: Compromised repository publishing wallet-stealing packages to npm
- **CMS Platforms (Global)**: Multiple unspecified CMS and plugin vulnerabilities under active exploitation per ACSC
- **Network Edge Devices / Routers**: Russian state targeting of vulnerable configurations for critical infrastructure access
- **Balochistan Police Portal**: Weaponized as espionage platform against Pakistani law enforcement
- **Russian Coms Platform**: Caller ID spoofing infrastructure used for 1.8M+ scam calls
- **Lidl Service Provider Systems**: Third-party breach exposing customer PII across Germany, Belgium, Netherlands
- **Odido Telecommunications Infrastructure**: Dutch telecom provider breached in February 2026
- **Healthcare Service Providers**: Business associates and supply chain partners experiencing doubled attack rates
- **AI Code Review Tools (CodeRabbit, Bugbot)**: Vulnerable to Ghostcommit image-based prompt injection

## Attack Vectors and Techniques

- **Device Code Phishing**: Forg365 abuses OAuth device authorization flow to trick users into granting access to attacker-controlled apps
- **Adversary-in-the-Middle (AitM)**: Real-time session relay through transparent proxies (Forg365, Evilginx) bypassing MFA
- **Evilginx Framework**: Mature phishing toolkit deploying reverse-proxy pharming for credential and session theft
- **Supply Chain Compromise (npm)**: Malicious code injected into legitimate packages (jscrambler) executing on install via lifecycle hooks
- **Supply Chain Compromise (GitHub)**: Repository takeover (Injective Labs) to publish malicious downstream packages
- **Wireless ADB Exploitation**: RedHook leverages Android's wireless debugging for unauthorized shell access without USB
- **Authentication Bypass**: Gitea Docker flaw allows session impersonation without valid credentials
- **Email-Based RCE**: Zimbra vulnerability triggered by viewing crafted malicious emails in web client
- **Firmware/Bootloader Exploitation**: U-Boot flaws enable persistent implants surviving OS reinstall via early boot code execution
- **Prompt Injection via Steganography**: Ghostcommit hides malicious prompts in PNG images targeting AI code reviewers
- **AI-Generated Offensive Tooling**: Suspected LLM-created PowerShell scripts for automated Active Directory reconnaissance
- **Caller ID Spoofing**: Russian Coms platform enabling mass social engineering through trusted number impersonation
- **Router/Edge Device Exploitation**: Russian actors targeting default credentials, unpatched vulnerabilities, and misconfigurations
- **CMS/Plugin Vulnerability Exploitation**: Automated scanning and exploitation of known flaws in web content management systems
- **Service Provider Compromise**: Third-party breaches (Lidl, potentially Odido) as initial access vector for customer data
- **Ransomware Deployment**: Ryuk affiliate operations involving initial access, lateral movement, and encryption

## Threat Actor Activities

- **Forg365 PhaaS Operators**: Running commercial phishing service targeting Microsoft 365 with advanced evasion and AI-assisted lure generation
- **Evilginx Campaign Operators (3 groups)**: Distinct phishing operations sharing infrastructure exposed via misconfigured server; targeting Microsoft 365 credentials
- **Russian State-Sponsored Actors (GRU-linked)**: Coordinated critical infrastructure targeting across NATO allies; router exploitation focus; subject of EU/UK sanctions
- **jscrambler Supply Chain Attackers**: Unknown group compromising npm package publish pipeline to distribute Rust infostealer
- **Injective Labs Repository Compromisers**: Unknown actors targeting cryptocurrency developers via malicious SDK packages
- **RedHook Malware Developers**: Android threat actors innovating with Wireless ADB exploitation for persistent device access
- **Gitea Docker Exploiters**: Active exploitation of authentication bypass in containerized Git service deployments
- **China-Aligned Threat Actors**: Suspected involvement in Balochistan Police Portal espionage against Pakistani targets
- **India-Aligned Threat Actors**: Suspected parallel espionage campaign against same Pakistani law enforcement targets
- **Dutch Hacker Group(s)**: Strong indications of involvement in Odido telecommunications breach (per Dutch National Police)
- **Ryuk Ransomware Affiliate**: Armenian national convicted for US corporate intrusions and ransomware deployment
- **Ghostcommit Researchers/Attackers**: Demonstrated novel AI-targeted prompt injection technique; potential adoption by threat actors
- **AI-Assisted Intrusion Actor**: Unknown operator using suspected LLM-generated PowerShell for AD reconnaissance
- **Russian Coms Platform Operators**: Criminal service providing caller ID spoofing for 1.8M+ fraud calls; five individuals charged by UK NCA
- **Global CMS Exploitation Campaign Actors**: Unattributed groups conducting mass exploitation of vulnerable web platforms per ACSC

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
