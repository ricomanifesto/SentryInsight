# Exploitation Report

## Executive Summary

Critical exploitation activity continues to accelerate across multiple vectors, with authentication bypass flaws in remote monitoring and management (RMM) platforms enabling full administrative compromise of managed customer environments. The N-able N-central authentication bypass (CVE-2026-18577) has been actively exploited in the wild, prompting CISA to add it to the Known Exploited Vulnerabilities catalog after confirmed customer compromises. Initial vendor patches proved incomplete, allowing threat actors to maintain access and pivot to downstream customer systems.

Simultaneously, social engineering techniques have evolved dramatically—device code phishing has surged 1,500% in 2026 while vishing attacks have doubled. Russian threat actors including Midnight Blizzard (APT29) are leveraging compromised hotel Wi-Fi networks with custom malware to breach Microsoft 365 accounts globally, while a new loader-as-a-service called DOUBLECUP employs ClickFix lures and PNG steganography in browser caches to deliver cross-platform remote access trojans. Hardware supply chain risks materialized with a COLDCARD wallet RNG flaw linked to over $88 million in Bitcoin theft, and INC Ransomware has emerged as the dominant operator exploiting recently disclosed SonicWall SMA 1000 series VPN vulnerabilities.

## Active Exploitation Details

### N-able N-central Authentication Bypass
- **Description**: An authentication bypass vulnerability in N-able N-central remote monitoring and management software that allows unauthenticated attackers to gain administrative access to both hosted and on-premises N-central servers. The flaw enables attackers to take full control of the RMM platform and pivot to all customer systems managed through compromised servers.
- **Impact**: Full administrative control of N-central servers, remote access to all downstream managed customer endpoints, potential for widespread supply chain compromise across managed service provider (MSP) client bases.
- **Status**: Actively exploited in the wild. CISA added to KEV catalog following confirmed customer compromises. Initial vendor patch was incomplete; attackers continued exploitation after first fix. N-able released additional mitigations.
- **CVE ID**: CVE-2026-18577

### cPanel Database Privilege Escalation
- **Description**: A critical flaw in cPanel hosting control panel that allows an authenticated hosting customer to execute SQL commands in the database's root context, crossing the privilege boundary between a cPanel account and the server's administrative database layer.
- **Impact**: Database root access from unprivileged hosting account, potential data theft, modification, or destruction across all databases on shared hosting servers, privilege escalation to server administration level.
- **Status**: Patched by cPanel. Exploitation status in wild not explicitly confirmed but critical severity warrants immediate patching.

### SonicWall SMA 1000 Series VPN Exploitation
- **Description**: Recently disclosed security flaws in SonicWall Secure Mobile Access (SMA) 1000 series VPN appliances being actively exploited for initial access and persistence.
- **Impact**: Unauthenticated remote access to corporate networks, VPN credential theft, lateral movement, ransomware deployment.
- **Status**: Actively exploited by INC Ransomware operation, which has emerged as the dominant threat actor targeting these vulnerabilities. Multiple victim organizations confirmed.

### Google Password Manager Passkey Hijacking (Pass-ta-key Attacks)
- **Description**: Three distinct attack techniques allowing malware running as an ordinary user on a compromised Windows device to abuse Google Password Manager's synced passkeys to authenticate to passkey-protected accounts without any user interaction—no fingerprint, PIN, or screen prompt appears.
- **Impact**: Complete bypass of passkey user verification requirements, account takeover of passkey-protected services (Google, GitHub, Microsoft, etc.), persistence through synced credential theft.
- **Status**: Actively exploitable on compromised Windows endpoints. Unit 42 research demonstrates practical exploitation. No patch available as attacks abuse design functionality.

### COLDCARD Hardware Wallet RNG Flaw
- **Description**: A vulnerability in COLDCARD hardware wallet firmware involving a flawed random number generator used during seed generation, allowing attackers to predict or reconstruct private keys for affected wallets.
- **Impact**: Full private key recovery and cryptocurrency theft. Two major incidents: ~1,196 Bitcoin addresses drained in 41 minutes (1,082.65 BTC ≈ $70.2M), and a broader campaign affecting thousands of wallets totaling ~$88.6M in stolen Bitcoin.
- **Status**: Actively exploited in the wild. Firmware updates available but cannot recover already-compromised seeds. Users must migrate funds to new wallets.

### DOUBLECUP ClickFix Loader-as-a-Service
- **Description**: A Russian loader-as-a-service (LaaS) operation using ClickFix social engineering lures to trick victims into executing malicious commands, staging malware-laced PNG images in browser cache, and extracting payloads to deliver CountLoader and DeviceManager RAT across Windows and macOS.
- **Impact**: Cross-platform remote access, credential theft, persistent foothold, secondary payload delivery. PNG steganography in browser cache evades traditional file-based detection.
- **Status**: Active campaigns observed. New LaaS offering available to cybercriminal affiliates.

### Malicious npm Supply Chain Attack
- **Description**: Eighteen malicious npm packages targeting users of Alibaba developer tools, delivering a cross-platform remote access trojan through typosquatting and dependency confusion techniques.
- **Impact**: Developer machine compromise, source code theft, supply chain contamination, cross-platform RAT persistence on Windows, Linux, and macOS.
- **Status**: Packages identified and removed from npm registry. Active exploitation window before takedown.

### Hotel Wi-Fi Microsoft 365 Breach Campaign
- **Description**: Global campaign compromising hospitality Wi-Fi networks to deploy custom malware that steals Microsoft 365 authentication tokens and credentials from guests' devices.
- **Impact**: Corporate email access, data exfiltration, business email compromise, lateral movement into victim organizations via compromised employee credentials.
- **Status**: Active global campaign attributed to Midnight Blizzard (APT29). Custom malware tooling indicates sophisticated operation.

### DarkSword Exploit Kit / GHOSTBLADE iOS Campaign
- **Description**: Chinese-speaking threat actor leveraging a publicly leaked version of the DarkSword exploit kit to deploy GHOSTBLADE malware on Apple iOS devices.
- **Impact**: iOS device compromise, surveillance, data theft, potential persistence through exploit chain. Leaked exploit kit lowers barrier for additional actors.
- **Status**: Active campaign observed. Public availability of DarkSword kit increases risk of broader adoption.

### PNLD Data Breach
- **Description**: Cyberattack on the UK Police National Legal Database resulting in exfiltration and dark web publication of contact data for over 100,000 police officers, government personnel, and criminal justice professionals.
- **Impact**: Operational security compromise for law enforcement, personal safety risks for officers, potential witness intimidation, intelligence gathering for future targeting.
- **Status**: Data published on dark web. ExfilSquad hackers claimed responsibility. Investigation ongoing.

### Thermo Fisher DNA Analysis Software Flaw
- **Description**: Flaw in Applied Biosystems human identification software that could allow data files to be altered before analysis software loads them, making DNA file tampering nearly undetectable.
- **Impact**: Forensic evidence manipulation, wrongful conviction/acquittal risks, integrity compromise of criminal justice DNA databases, research data corruption.
- **Status**: Patched by Thermo Fisher Scientific in July 2026. No confirmed exploitation in wild but high consequence if abused.

### Hugging Face Diffusers Arbitrary Code Execution
- **Description**: Three high-severity security flaws in Hugging Face's Diffusers library that allow crafted model repositories to execute arbitrary code on machines that load them, enabling supply chain attacks through malicious AI models.
- **Impact**: Remote code execution via model loading, AI/ML pipeline compromise, developer workstation takeover, potential contamination of downstream applications.
- **Status**: Disclosed and patched. High severity due to widespread adoption of Diffusers in AI development workflows.

### Fake Roblox Xeno Launcher Campaign
- **Description**: Fake Xeno Executor script launcher installers targeting Roblox players, distributing infostealer and remote access trojan malware through gaming community distribution channels.
- **Impact**: Credential theft, cryptocurrency wallet drainage, remote access to victim machines, potential pivot to parental/corporate networks from home devices.
- **Status**: Active distribution through search engine poisoning, social media, and gaming forums.

### Chinese Actor Deepseek AI Agent Attacks
- **Description**: Chinese threat actor weaponizing a Deepseek AI agent to automate reconnaissance and exploitation attempts against a security firm, attempting to compromise over 1,200 hosts for proxyjacking infrastructure.
- **Impact**: Automated vulnerability scanning at scale, proxy network construction for attack anonymization, potential AI-assisted exploit development.
- **Status**: Intercepted and investigated. Demonstrates emerging AI-powered offensive capabilities.

## Affected Systems and Products

- **N-able N-central**: Both hosted (SaaS) and on-premises deployments. All versions prior to patched releases containing fixes for CVE-2026-18577.
- **cPanel**: Hosting control panel installations. Specific affected versions not disclosed in reporting; all unpatched instances at risk.
- **SonicWall SMA 1000 Series**: Secure Mobile Access 1000 series VPN appliances. Firmware versions prior to security patches for recently disclosed flaws.
- **Google Password Manager / Chrome / Android**: Windows devices with Google Password Manager passkey sync enabled. Affects passkey authentication flow across relying parties (Google, GitHub, Microsoft, etc.).
- **COLDCOARD Hardware Wallets**: Mk3, Mk4, and Q models with firmware versions using flawed RNG implementation. Seeds generated on vulnerable firmware irrecoverably compromised.
- **DOUBLECUP Target Platforms**: Windows and macOS systems via browser-based ClickFix delivery. CountLoader and DeviceManager RAT payloads.
- **npm Ecosystem / Alibaba Developer Tools**: Developers using Alibaba Cloud SDKs and tools who installed malicious typosquatted packages.
- **Hotel Wi-Fi Networks / Microsoft 365**: Hospitality network infrastructure globally. Endpoints connecting to compromised networks with Microsoft 365 accounts.
- **Apple iOS Devices**: iOS versions vulnerable to DarkSword exploit kit chains. GHOSTBLADE malware deployment observed.
- **UK Police National Legal Database (PNLD)**: Centralized legal reference database for UK law enforcement. Contact data for 100,000+ personnel.
- **Thermo Fisher Applied Biosystems Software**: Human identification software versions prior to July 2026 patches. Forensic and research laboratories.
- **Hugging Face Diffusers Library**: All versions prior to security patches. AI/ML developers loading models from untrusted repositories.
- **Roblox Players / Windows**: Gamers downloading fake Xeno Executor launchers. Windows-based infostealer and RAT payloads.

## Attack Vectors and Techniques

- **Authentication Bypass (CVE-2026-18577)**: Unauthenticated administrative access to N-able N-central RMM servers via flawed authentication logic, enabling full platform takeover and downstream customer compromise.
- **Database Privilege Escalation**: cPanel account to database root via SQL execution context confusion, crossing tenant isolation boundaries in shared hosting environments.
- **VPN Appliance Exploitation**: Targeting SonicWall SMA 1000 series flaws for unauthenticated network access, credential harvesting, and ransomware deployment.
- **Passkey Verification Bypass (Pass-ta-key)**: Three techniques abusing Google Password Manager's sync architecture—malware invokes passkey authentication silently without user presence verification, exploiting missing user interaction enforcement.
- **Hardware RNG Subversion**: Exploitation of flawed entropy source in COLDCARD wallet firmware during seed generation, enabling private key reconstruction and deterministic wallet compromise.
- **ClickFix Social Engineering**: Deceptive browser prompts tricking users into executing attacker-controlled commands (PowerShell, bash, etc.) under guise of verification/error resolution.
- **Browser Cache Steganography**: Malicious PNG images cached by victim browsers, with payloads extracted via JavaScript from canvas/image data—evades disk-based malware scanning.
- **Supply Chain / Typosquatting (npm)**: Malicious packages mimicking legitimate Alibaba Cloud dependencies, executed during development workflows on engineer workstations.
- **Evil Twin / Rogue Access Point (Hotel Wi-Fi)**: Compromise of hospitality network infrastructure to intercept traffic, deploy custom malware via captive portals or drive-by downloads, steal Microsoft 365 tokens.
- **Leaked Exploit Kit Utilization**: Publicly available DarkSword exploit kit repurposed for iOS targeting with GHOSTBLADE payload—demonstrates risk of exploit code proliferation.
- **Database Exfiltration / Dark Web Publication**: Direct compromise of centralized sensitive database (PNLD), bulk data theft, and publication for operational disruption.
- **Pre-Analysis Data Tampering**: Manipulation of DNA data files before forensic software ingestion, exploiting trust in file integrity prior to cryptographic verification.
- **Malicious Model Repository (AI Supply Chain)**: Crafted Hugging Face model repositories exploiting Diffusers deserialization/loading flaws for arbitrary code execution on model download.
- **Gaming Social Engineering / Fake Tooling**: Trojanized game utility installers (Roblox script executors) distributed via SEO poisoning and community channels.
- **AI-Automated Reconnaissance/Exploitation**: Deepseek AI agent directed to scan, fingerprint, and exploit targets at scale for proxy infrastructure deployment.
- **Device Code Phishing (1,500% increase)**: Abuse of OAuth device authorization flow—attackers initiate login on controlled device, send user code via phishing, user completes auth on legitimate site, attacker gains token.
- **Vishing (Voice Phishing, 2x increase)**: Telephone-based social engineering combined with technical pretexts (IT support, security alerts) for credential theft and MFA bypass.

## Threat Actor Activities

- **Midnight Blizzard (APT29)**: Russian state-sponsored actor conducting global hotel Wi-Fi compromise campaign targeting Microsoft 365 accounts. Custom malware tooling, hospitality sector focus, credential theft for espionage and follow-on intrusion.
- **DOUBLECUP Operators**: Russian loader-as-a-service (LaaS) providers offering ClickFix delivery with browser cache steganography. CountLoader and DeviceManager RAT payloads. Cross-platform (Windows/macOS). Affiliate model for distribution.
- **INC Ransomware**: Emerged as dominant actor exploiting SonicWall SMA 1000 vulnerabilities. Rapid weaponization of disclosed flaws. Ransomware deployment via VPN access. Active victim extortion.
- **ExfilSquad**: Hacktivist/cybercriminal group claiming PNLD breach. Published 100,000+ UK police/government contact records on dark web. Motivations appear mixed (notoriety, disruption, potential sale).
- **Chinese Threat Actor (Unnamed)**: Leveraging leaked DarkSword exploit kit for iOS targeting with GHOSTBLADE malware. Separate campaign using Deepseek AI agent for automated proxyjacking infrastructure build (1,200+ target hosts). Demonstrates AI-augmented operations.
- **COLDCOARD Wallet Attackers**: Unknown operator(s) exploiting RNG flaw for mass Bitcoin theft. Two major sweeps: 1,082.65 BTC ($70.2M) in 41 minutes (July 30), and broader campaign netting ~$88.6M. Highly automated, blockchain-analyzed operations.
- **Malicious npm Publishers**: Unknown actors conducting supply chain attack via 18 typosquatted Alibaba Cloud packages. Cross-platform RAT delivery. Sophisticated packaging to evade detection.
- **Roblox Xeno Impersonators**: Unknown threat actors distributing fake script executors to gaming community. Infostealer + RAT combo. Financially motivated (credential/crypto theft).

## Source Attribution

- **New cPanel Critical Flaw Could Let Hosting Customers Run SQL as Database Root**: The Hacker News - https://thehackernews.com/2026/08/new-cpanel-critical-flaw-could-let.html
- **DOUBLECUP Uses ClickFix and Cached PNGs to Deliver CountLoader and DeviceManager RAT**: The Hacker News - https://thehackernews.com/2026/08/doublecup-uses-clickfix-and-cached-pngs.html
- **CISA Adds Exploited N-able N-central Flaw to KEV After Customer Compromises**: The Hacker News - https://thehackernews.com/2026/08/cisa-adds-exploited-n-able-n-central.html
- **Device Code Phishing Up 1,500% in 2026; Vishing Doubles**: Dark Reading - https://www.darkreading.com/cybersecurity-analytics/device-code-phishing-vishing-doubles
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
