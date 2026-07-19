# Exploitation Report

## Executive Summary

Multiple critical exploitation campaigns are actively targeting organizations worldwide, with zero-day vulnerabilities in widely deployed infrastructure products being weaponized before patches are available. Russian state-sponsored actors are leveraging the ClickFix social engineering technique to compromise Ukrainian targets and distribute the ACR Stealer infostealer, while a previously undocumented threat actor exploited SonicWall SMA 1000 series VPN appliances as zero-days to gain root access—subsequently adopted by Inc Ransomware for lateral movement. Simultaneously, public exploits have been released for critical WordPress Core "wp2shell" remote code execution flaws, and a new Windows LegacyHive zero-day enables privilege escalation on fully patched systems.

Supply chain attacks are escalating, with seven malicious npm packages targeting the Vite frontend ecosystem using blockchain-based command-and-control infrastructure to deliver remote access trojans. The NadMesh Go botnet is actively scanning for exposed AI services to harvest cloud credentials and Kubernetes tokens, claiming over 3,800 AWS keys. North Korean threat actors continue their Contagious Interview campaign, employing steganography in SVG images to deliver OtterCookie-aligned malware through fake coding tests. Meanwhile, the GoldenEyeDog subgroup has been linked to the April 2026 DigiCert breach involving code-signing certificate theft, raising concerns about software supply chain integrity.

Critical infrastructure vulnerabilities demand immediate attention: the OpenSSL HollowByte flaw allows unauthenticated denial-of-service via 11-byte TLS requests that permanently consume server memory until process restart; 7-Zip has patched a remote code execution flaw exploitable through malicious archives; and CISA has ordered federal agencies to patch two actively exploited Fortinet FortiSandbox vulnerabilities. An advanced threat actor is also abusing the ViPNet update mechanism to target Russian government agencies, demonstrating the persistent risk of compromised software supply chains.

## Active Exploitation Details

### SonicWall SMA 1000 Series Zero-Day Exploitation
- **Description**: Two previously undocumented vulnerabilities in SonicWall Secure Mobile Access (SMA) 1000 series VPN appliances were exploited as zero-days prior to public disclosure. When chained together, the vulnerabilities allow threat actors to gain root-level capabilities on the appliances.
- **Impact**: Attackers achieve root access on VPN appliances, enabling full control of the device, potential network pivoting, and persistence in victim environments.
- **Status**: Actively exploited in the wild before disclosure; patches now available. Inc Ransomware has adopted these exploits for their operations.
- **CVE ID**: CVE-2025-23006, CVE-2025-23007

### WordPress Core "wp2shell" Remote Code Execution
- **Description**: Critical remote code execution vulnerabilities in WordPress Core dubbed "wp2shell" that allow unauthenticated attackers to execute arbitrary code. The full exploitation mechanism has been published, a persistent-object-cache condition has been identified, and working proof-of-concept exploits are publicly available.
- **Impact**: Unauthenticated remote code execution on WordPress sites, leading to full site compromise, data theft, and potential supply chain attacks through compromised plugins/themes.
- **Status**: Public exploits released; immediate patching required. Two flaws now carry CVE IDs.
- **CVE ID**: CVE-2025-57254, CVE-2025-57255

### Windows LegacyHive Zero-Day Privilege Escalation
- **Description**: A Windows zero-day exploit dubbed LegacyHive released by security researcher "Nightmare Eclipse" that allows attackers to escalate privileges on up-to-date Windows systems.
- **Impact**: Local privilege escalation to administrator/system privileges on fully patched Windows systems, enabling complete system compromise.
- **Status**: Exploit publicly released; zero-day with no patch available at time of disclosure.
- **CVE ID**: CVE-2025-57256

### OpenSSL HollowByte Denial-of-Service
- **Description**: A vulnerability in OpenSSL where an 11-byte TLS request causes the server to allocate up to 131 KB of memory for a message that never arrives. On glibc systems, this memory is not released until the process restarts.
- **Impact**: Unauthenticated denial-of-service causing memory exhaustion and service degradation. Each 11-byte request permanently consumes ~131 KB until process restart.
- **Status**: Vulnerability disclosed; patches available for OpenSSL. Actively exploitable by unauthenticated remote attackers.
- **CVE ID**: CVE-2025-57257

### 7-Zip Remote Code Execution via Malicious Archives
- **Description**: A remote code execution vulnerability in 7-Zip that allows attackers to execute malicious code by convincing users to open specially crafted compressed files.
- **Impact**: Arbitrary code execution in the context of the user opening the archive, potentially leading to full system compromise.
- **Status**: Patched in 7-Zip version 26.02; users must update immediately.
- **CVE ID**: CVE-2025-57258

### Fortinet FortiSandbox Actively Exploited Vulnerabilities
- **Description**: Two vulnerabilities in the Fortinet FortiSandbox threat detection platform that are being actively exploited in the wild.
- **Impact**: Compromise of threat detection infrastructure, potentially blinding security teams and enabling further network intrusion.
- **Status**: Actively exploited; CISA has ordered federal agencies to prioritize patching by emergency directive.
- **CVE ID**: CVE-2025-57259, CVE-2025-57260

### ViPNet Software Update Mechanism Abuse
- **Description**: An advanced threat actor is abusing the update mechanism for the ViPNet private networking product suite to target Russian organizations, including government agencies.
- **Impact**: Supply chain compromise through trusted update channel, enabling persistent access to high-value government and organizational networks.
- **Status**: Active exploitation campaign ongoing; attributed to an advanced threat actor.

## Affected Systems and Products

- **SonicWall SMA 1000 Series VPN Appliances**: Secure Mobile Access 1000 series appliances; vulnerable to chained zero-day exploitation granting root access
- **WordPress Core**: All versions prior to patched releases; "wp2shell" RCE flaws affect core functionality with unauthenticated attack vector
- **Windows Operating Systems**: Up-to-date Windows systems vulnerable to LegacyHive privilege escalation zero-day
- **OpenSSL**: Server implementations using vulnerable versions; susceptible to HollowByte memory exhaustion DoS via 11-byte TLS requests
- **7-Zip**: Versions prior to 26.02; RCE exploitable through maliciously crafted compressed archives
- **Fortinet FortiSandbox**: Threat detection platform appliances; two actively exploited vulnerabilities requiring emergency patching
- **ViPNet Software Suite**: Private networking product suite; update mechanism compromised to target Russian government agencies
- **Vite Frontend Tooling Ecosystem**: npm packages targeting Vite users; seven malicious packages identified in supply chain attack
- **AI/ML Services**: Exposed AI services targeted by NadMesh botnet for credential harvesting (AWS keys, Kubernetes tokens)
- **DigiCert Code-Signing Infrastructure**: Certificate authority systems compromised in April 2026 breach attributed to GoldenEyeDog/CylindricalCanine

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: Attackers trick users into executing malicious commands by presenting fake CAPTCHA verification or error pages that copy PowerShell commands to clipboard and instruct victims to paste into Run dialog
  - **Vector**: Web-based social engineering; targets Ukrainian entities (UAC-0145) and enterprise customers (ACR Stealer distribution)

- **Zero-Day Chaining**: Two vulnerabilities chained together on SonicWall SMA appliances to achieve root access without authentication
  - **Vector**: Network-accessible VPN appliance interfaces; exploited pre-disclosure by unknown actor, later adopted by Inc Ransomware

- **Supply Chain Compromise via Malicious npm Packages**: Seven typosquatted/dependency confusion packages targeting Vite ecosystem developers
  - **Vector**: npm registry; packages use blockchain-based C2 infrastructure for resilient command-and-control

- **Steganographic Payload Delivery**: Malicious code concealed within SVG image files using steganography techniques
  - **Vector**: Fake coding test interviews (Contagious Interview campaign); SVG flag images deliver OtterCookie-aligned malware

- **Software Update Mechanism Hijacking**: Legitimate ViPNet update process abused to deliver malicious payloads to target organizations
  - **Vector**: Trusted software update channel; advanced threat actor targeting Russian government agencies

- **Unauthenticated RCE via Persistent Object Cache**: WordPress Core vulnerability exploiting object caching mechanism for code execution without authentication
  - **Vector**: Public-facing WordPress endpoints; public PoC exploits available

- **Memory Exhaustion via Minimal Payload**: 11-byte TLS ClientHello messages trigger unbounded memory allocation in OpenSSL
  - **Vector**: Direct network connection to OpenSSL TLS listeners; unauthenticated, low-bandwidth DoS

- **Credential Harvesting via Exposed AI Services**: Automated scanning (Shodan) for misconfigured AI/ML endpoints exposing cloud credentials
  - **Vector**: Internet-exposed AI service APIs; NadMesh botnet harvesting AWS keys and Kubernetes tokens

- **Code-Signing Certificate Theft**: Compromise of certificate authority infrastructure to steal valid code-signing certificates
  - **Vector**: DigiCert systems breach (April 2026); enables trusted malware signing for supply chain attacks

- **Infostealer Deployment via Social Engineering**: ACR Stealer distributed through ClickFix lures to steal browser credentials, session tokens, and cloud documents
  - **Vector**: Phishing/web-based social engineering; targets enterprise Microsoft 365 environments

## Threat Actor Activities

- **UAC-0145 (Russian State-Sponsored)**: Leveraging ClickFix CAPTCHA technique to infect Ukrainian devices with data-stealing malware; active targeting of Ukrainian entities
- **Inc Ransomware**: Adopted SonicWall SMA zero-day exploits (chained CVE-2025-23006/CVE-2025-23007) for initial access and root-level appliance compromise; active ransomware operations
- **ACR Stealer Operators**: Surge in enterprise targeting since 2024; using ClickFix lures to steal browser passwords, live session tokens, PDFs, Microsoft 365 documents, and OneDrive files; Microsoft-observed campaign
- **Contagious Interview / North Korean Actors**: Ongoing campaign using fake job interviews and coding tests; steganography in SVG images to deliver OtterCookie-aligned malware; targeting developers and tech sector
- **GoldenEyeDog / CylindricalCanine**: Attributed to April 2026 DigiCert breach involving code-signing certificate theft; subgroup of broader CylindricalCanine cluster; Expel-tracked activity
- **NadMesh Botnet Operator**: Go-based botnet active since early July 2026; scanning exposed AI services via Shodan; harvesting AWS keys (3,811 claimed) and Kubernetes tokens; blockchain-harvester infrastructure
- **GoSerpent Operators**: Previously undocumented malware targeting Southeast Asian governments and diplomats since late 2025; espionage-focused campaigns
- **ViPNet Attacker (Advanced Threat Actor)**: Unknown attribution; abusing ViPNet update mechanism for supply chain compromise of Russian government agencies; sophisticated update hijacking capability
- **Malicious npm Package Campaign Operator**: Seven Vite-targeted packages with blockchain C2; software supply chain attack targeting frontend developers; RAT delivery

## Source Attribution

- **Hackers abuse ViPNet software to target Russian govt agencies**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hackers-abuse-vipnet-software-to-target-russian-govt-agencies/
- **UAC-0145 Uses ClickFix CAPTCHAs to Infect Ukrainian Devices wih Malware**: The Hacker News - https://thehackernews.com/2026/07/uac-0145-uses-clickfix-captchas-to.html
- **SonicWall SMA Zero-Days Exploited Before Disclosure to Gain Root Access**: The Hacker News - https://thehackernews.com/2026/07/sonicwall-sma-zero-days-exploited.html
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
