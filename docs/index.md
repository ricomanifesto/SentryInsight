# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse platforms, ranging from enterprise file-sharing and web publishing systems to network security appliances and developer toolchains. The most severe activity involves a SharePoint Server zero-day (CVE-2026-58644) added to CISA's Known Exploited Vulnerabilities catalog, two chained SonicWall SMA zero-days leveraged by Inc Ransomware for root-level compromise, and public exploits now circulating for WordPress Core "wp2shell" RCE flaws. Simultaneously, infostealer campaigns—particularly ACR Stealer using ClickFix social-engineering lures—are harvesting browser credentials, Microsoft 365 tokens, and sensitive documents at scale, while a new Go-based botnet (NadMesh) systematically scans for exposed AI services to steal cloud keys and Kubernetes tokens.

On the supply-chain front, seven malicious npm packages masquerading as Vite tooling have been caught delivering a remote-access trojan via blockchain-based command-and-control, and a North Korean operation (Contagious Interview) continues to weaponize steganographic SVG payloads in fake coding tests. Privilege-escalation risk has spiked with the public release of the Windows "LegacyHive" zero-day exploit, and OpenSSL servers face a low-bandwidth DoS vector (HollowByte) that exhausts memory with 11-byte TLS requests. CISA has also mandated urgent patching of two actively exploited FortiSandbox vulnerabilities, underscoring ongoing targeting of security infrastructure itself.

## Active Exploitation Details

### SharePoint Server RCE Zero-Day (CVE-2026-58644)
- **Description**: A remote code execution vulnerability in Microsoft SharePoint Server that allows unauthenticated attackers to execute arbitrary code on affected servers.
- **Impact**: Full server compromise, potential lateral movement within organizational networks, data exfiltration, and persistence establishment.
- **Status**: Actively exploited in the wild; added to CISA's Known Exploited Vulnerabilities (KEV) catalog on July 17, 2026. Patches available from Microsoft.
- **CVE ID**: CVE-2026-58644

### SonicWall SMA Zero-Day Chain
- **Description**: Two vulnerabilities in SonicWall Secure Mobile Access (SMA) appliances that, when chained together, provide threat actors with root-level capabilities on the device.
- **Impact**: Complete administrative control over the VPN/appliance, enabling network access, credential harvesting, traffic interception, and persistence.
- **Status**: Actively exploited by Inc Ransomware group; zero-day status indicates no patches available at time of disclosure.
- **CVE ID**: Not explicitly provided in source articles.

### WordPress Core "wp2shell" RCE Vulnerabilities
- **Description**: Critical remote code execution vulnerabilities in WordPress Core, collectively dubbed "wp2shell," that allow unauthenticated attackers to execute arbitrary code. Full exploitation mechanism published with working proof-of-concept code publicly available.
- **Impact**: Complete takeover of WordPress sites, web shell deployment, data theft, defacement, and use as pivot points for further attacks.
- **Status**: Public exploits released; administrators urged to patch immediately. Two flaws now carry CVE IDs (specific IDs not provided in source snippets).
- **CVE ID**: CVE IDs assigned but not explicitly stated in provided article text.

### Windows LegacyHive Privilege Escalation Zero-Day
- **Description**: A Windows zero-day exploit dubbed "LegacyHive" released by researcher "Nightmare Eclipse" that allows attackers to escalate privileges on up-to-date Windows systems.
- **Impact**: Local privilege escalation to SYSTEM/admin level, enabling full host control, security product disablement, and lateral movement.
- **Status**: Exploit code publicly released; zero-day with no patch available at disclosure.
- **CVE ID**: Not explicitly provided in source articles.

### 7-Zip Remote Code Execution Flaw
- **Description**: An RCE vulnerability in 7-Zip triggered by opening specially crafted malicious archive files.
- **Impact**: Arbitrary code execution in the context of the user opening the archive, potentially leading to malware installation and system compromise.
- **Status**: Fixed in 7-Zip version 26.02; users advised to update immediately.
- **CVE ID**: Not explicitly provided in source articles.

### Fortinet FortiSandbox Actively Exploited Vulnerabilities
- **Description**: Two vulnerabilities in Fortinet FortiSandbox threat detection platform confirmed as actively exploited in the wild.
- **Impact**: Compromise of security analytics platform, potential blind spots in threat detection, lateral movement from security infrastructure.
- **Status**: CISA ordered federal agencies to prioritize patching by July 19, 2026; patches available from Fortinet.
- **CVE ID**: Not explicitly provided in source articles.

### OpenSSL HollowByte Denial-of-Service Vulnerability
- **Description**: A vulnerability allowing unauthenticated attackers to trigger a DoS condition on OpenSSL servers with a malicious 11-byte TLS payload, causing the server to allocate up to 131 KB of memory per connection that is never released until process restart.
- **Impact**: Memory exhaustion leading to service degradation or complete denial of service; low-bandwidth asymmetric attack.
- **Status**: Vulnerability disclosed; patches expected from OpenSSL project. Affects glibc-based systems.
- **CVE ID**: Not explicitly provided in source articles.

## Affected Systems and Products

- **Microsoft SharePoint Server**: All unpatched versions vulnerable to CVE-2026-58644 RCE zero-day
- **SonicWall Secure Mobile Access (SMA) Appliances**: Models running vulnerable firmware versions; chained zero-days provide root access
- **WordPress Core**: All versions prior to patched release; unauthenticated RCE via "wp2shell" flaws
- **Windows (multiple versions)**: Up-to-date systems vulnerable to LegacyHive privilege escalation zero-day
- **7-Zip**: Versions prior to 26.02; RCE via malicious archive files
- **Fortinet FortiSandbox**: Threat detection platform appliances with unpatched vulnerabilities (specific versions not detailed in sources)
- **OpenSSL**: Server implementations on glibc-based systems; vulnerable to HollowByte 11-byte TLS DoS
- **Vite/npm Ecosystem**: Developers and CI/CD pipelines using compromised npm packages (seven identified malicious packages)
- **macOS Systems**: Targeted by ClickLock malware for credential theft
- **AI/ML Services**: Exposed model-serving endpoints, Jupyter notebooks, and Kubernetes clusters hunted by NadMesh botnet
- **DigiCert Infrastructure**: Code-signing certificate infrastructure compromised in April 2026 incident

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: ACR Stealer uses fake CAPTCHA/verification pages to trick users into executing malicious PowerShell commands that steal browser passwords, session tokens, Microsoft 365 documents, and OneDrive-synced files
- **Malicious Archive Files**: 7-Zip RCE triggered by user interaction with crafted compressed files (social engineering / phishing attachment vector)
- **Chained Zero-Day Exploitation**: Inc Ransomware combines two SonicWall SMA vulnerabilities for unauthenticated root access
- **Supply Chain Compromise**: Seven malicious npm packages typosquatting/imitating Vite tooling deliver RAT via blockchain-based C2 (Smart Contract on BSC used for resilient command retrieval)
- **Steganographic Payload Delivery**: North Korean Contagious Interview campaign hides OtterCookie-aligned malware in SVG flag images within fake coding tests
- **Exposed Service Scanning**: NadMesh botnet uses Shodan harvester to continuously scan for exposed AI services (Ollama, TensorFlow Serving, Triton, Kubernetes API) to harvest AWS keys, K8s tokens, and cloud credentials
- **Privilege Escalation via Kernel Exploit**: LegacyHive leverages Windows kernel vulnerability for LOCAL_SYSTEM escalation
- **Asymmetric Resource Exhaustion**: HollowByte sends 11-byte TLS ClientHello with oversized length field, forcing OpenSSL to allocate ~131 KB per connection indefinitely
- **Third-Party Support System Compromise**: Ernst & Young breach originated from compromised third-party IT support ticket system
- **Legacy System Access**: Abbott Laboratories incidents involved unauthorized access to legacy Exact Sciences systems in Cancer Diagnostics division

## Threat Actor Activities

- **Inc Ransomware**: Actively exploiting chained SonicWall SMA zero-days to gain root access on VPN appliances for initial access and lateral movement
- **ACR Stealer Operators**: Conducting large-scale infostealer campaigns against enterprise customers using ClickFix lures; harvesting browser credentials, live session tokens, PDFs, Microsoft 365 documents, and OneDrive files since 2024 with recent surge noted by Microsoft
- **NadMesh Botnet Operator**: Go-based botnet active since early July 2026; operator dashboard claims 3,811 unique AWS keys harvested; targets exposed AI/ML services and Kubernetes clusters for cloud credential theft
- **Contagious Interview / North Korean Actors**: Linked to REvil/DPRK nexus; using fake job interviews and coding tests with SVG steganography to deliver OtterCookie-aligned malware to developers and job seekers
- **GoldenEyeDog / CylindricalCanine**: Subgroup attributed to April 2026 DigiCert breach involving code-signing certificate theft; technical details shared by Expel researchers
- **Fairlife Ransomware Attackers**: Ransomware group disrupted Fairlife (Coca-Cola subsidiary) US dairy production operations
- **GoSerpent Operators**: Previously undocumented malware targeting Southeast Asian governments and diplomats for espionage since late 2025
- **REvil Affiliate (Aleksandr Ermakov)**: Russian national detained in Armenia on US extradition warrant for REvil ransomware activities (lawyers claim mistaken identity)

## Source Attribution

- **Update now: 7-Zip fixes RCE flaw exploitable with malicious archives**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/update-now-7-zip-fixes-rce-flaw-exploitable-with-malicious-archives/
- **WordPress Core "wp2shell" RCE flaws get public exploits, patch now**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/wordpress-core-wp2shell-rce-flaws-get-public-exploits-patch-now/
- **Microsoft warns of surge in ACR Stealer attacks on customers**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/microsoft-warns-of-surge-in-acr-stealer-attacks-on-customers/
- **The Future of Age Verification: Your Face Never Leaves Your Device**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/the-future-of-age-verification-your-face-never-leaves-your-device/
- **New wp2shell WordPress Core Flaw Lets Unauthenticated Attackers Run Code**: The Hacker News - https://thehackernews.com/2026/07/new-wp2shell-wordpress-core-flaw-lets.html
- **Abbott probes two cyber incidents amid extortion claims**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/abbott-laboratories-probes-two-cyber-incidents-amid-extortion-claims/
- **OpenSSL HollowByte Flaw Could Freeze Server Memory with 11-Byte TLS Requests**: The Hacker News - https://thehackernews.com/2026/07/openssl-hollowbyte-flaw-could-freeze.html
- **Inc Ransomware Exploits SonicWall SMA Zero-Days**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/inc-ransomware-exploits-sonicwall-sma-zero-days
- **Seven Malicious Vite npm Packages Use Blockchain C2 to Deliver a RAT**: The Hacker News - https://thehackernews.com/2026/07/seven-malicious-vite-npm-packages-use.html
- **HollowByte DDoS flaw bloats OpenSSL server memory with 11-byte payload**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hollowbyte-ddos-flaw-bloats-openssl-server-memory-with-11-byte-payload/
- **New NadMesh Botnet Hunts Exposed AI Services for Cloud Keys and Kubernetes Tokens**: The Hacker News - https://thehackernews.com/2026/07/new-nadmesh-botnet-hunts-exposed-ai.html
- **The Real AI Threat Is Blind Trust**: Dark Reading - https://www.darkreading.com/application-security/real-ai-threat-blind-trust
- **GoldenEyeDog Subgroup Linked to DigiCert Breach and Code-Signing Certificate Theft**: The Hacker News - https://thehackernews.com/2026/07/goldeneyedog-subgroup-linked-to.html
- **Ernst \& Young discloses data breach after support system hack**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/ernst-and-young-discloses-data-breach-after-support-system-hack/
- **Inside the Search for "Clean" Residential Proxies for Carding**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/inside-the-search-for-clean-residential-proxies-for-carding/
- **Fake Coding Tests Deliver OtterCookie-Aligned Malware Hidden in SVG Flag Images**: The Hacker News - https://thehackernews.com/2026/07/north-korea-linked-hackers-hide.html
- **Gold Eagle Clearinghouse Targets Security Gap, but How Is Unclear**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/gold-eagle-clearinghouse-targets-security-gap
- **Google Bets 'Agentic Defense' Strategy Can Outpace Attackers**: Dark Reading - https://www.darkreading.com/cloud-security/google-bets-agentic-defense-strategy-outpace-attackers
- **E.U. Orders Google to Open Android Mic, Camera and Screen to Rival AI Assistants**: The Hacker News - https://thehackernews.com/2026/07/eu-orders-google-to-open-android-mic.html
- **The Race to Field Military Autonomy Is On, Can Trusted Information Infrastructure Keep Pace?**: The Hacker News - https://thehackernews.com/2026/07/the-race-to-field-military-autonomy-is.html
- **New Windows LegacyHive zero-day gives hackers admin privileges**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-windows-legacyhive-zero-day-exploit-grants-hackers-admin-access/
- **Armenia Detains Russian Tourist on U.S. Warrant for REvil Hacker, Lawyers Say Wrong Man**: The Hacker News - https://thehackernews.com/2026/07/armenia-detains-russian-tourist-on-us.html
- **Windows Server 2022 reach end of mainstream support in 90 days**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/windows-server-2022-reach-end-of-mainstream-support-in-90-days/
- **ACR Stealer Uses ClickFix Lures to Steal Browser Tokens and Microsoft 365 Files**: The Hacker News - https://thehackernews.com/2026/07/acr-stealer-uses-clickfix-lures-to.html
- **New GoSerpent Malware Targets Southeast Asian Governments and Diplomats for Espionage**: The Hacker News - https://thehackernews.com/2026/07/new-goserpent-malware-targets-southeast.html
- **US charges two over laundering $43 million from investment fraud**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/us-charges-two-over-laundering-43-million-from-investment-fraud/
- **CISA urges immediate action on actively exploited Fortinet flaws**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-warns-feds-to-patch-exploited-fortinet-fortisandbox-flaws-by-sunday/
- **CISA Adds Exploited SharePoint RCE Zero-Day CVE-2026-58644 to KEV**: The Hacker News - https://thehackernews.com/2026/07/cisa-adds-exploited-sharepoint-rce-zero.html
- **New ClickLock macOS malware traps users into revealing login password**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-clicklock-macos-malware-traps-users-into-revealing-login-password/
- **Coca-Cola says Fairlife ransomware attack halts US dairy production**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/coca-cola-says-fairlife-ransomware-attack-halts-us-dairy-production/
