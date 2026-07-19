# Exploitation Report

## Executive Summary

Multiple critical exploitation campaigns are actively underway across diverse technology stacks, ranging from VPN appliances and archive utilities to content management systems and cryptographic libraries. Threat actors are leveraging zero-day vulnerabilities in SonicWall SMA 1000 series appliances and Windows LegacyHive to achieve root-level access and privilege escalation, while public exploit code for WordPress Core "wp2shell" RCE flaws and 7-Zip RCE vulnerabilities has dramatically lowered the barrier for widespread attacks. Simultaneously, sophisticated social engineering campaigns—including ClickFix CAPTCHA lures and fake coding tests with steganographic payloads—are delivering information stealers and remote access trojans to high-value targets in government, enterprise, and cryptocurrency sectors.

State-sponsored and financially motivated actors are diversifying their toolkits: Russian-aligned UAC-0145 targets Ukrainian entities with ClickFix-driven malware; North Korea's Contagious Interview campaign hides OtterCookie-aligned payloads in SVG flag images; the NadMesh botnet scrapes exposed AI services for cloud credentials; and the GoldenEyeDog subgroup is linked to code-signing certificate theft from DigiCert. Ransomware operators, notably Inc Ransomware, are chaining SonicWall zero-days for initial access, while ACR Stealer campaigns surge across enterprise environments using ClickFix lures to harvest browser tokens, Microsoft 365 documents, and OneDrive files. CISA has issued emergency directives for actively exploited Fortinet FortiSandbox vulnerabilities, underscoring the urgency of patching exposed perimeter defenses.

Supply chain threats continue to evolve with seven malicious Vite npm packages using blockchain-based command-and-control to deliver a RAT, demonstrating innovative persistence and evasion techniques. The OpenSSL HollowByte flaw enables trivial denial-of-service via 11-byte TLS requests, affecting a vast installed base of servers. Organizations must prioritize patching for SonicWall SMA, WordPress Core, 7-Zip, Fortinet FortiSandbox, and Windows systems while hardening defenses against social engineering, supply chain compromise, and credential harvesting campaigns targeting AI/ML infrastructure and cloud environments.

## Active Exploitation Details

### SonicWall SMA 1000 Series Zero-Day Exploitation
- **Description**: Two previously undocumented vulnerabilities in SonicWall Secure Mobile Access (SMA) 1000 series VPN appliances were exploited as zero-days before public disclosure. When chained together, the flaws allow unauthenticated attackers to gain root-level access on the appliance.
- **Impact**: Attackers achieve full administrative control over VPN appliances, enabling network persistence, lateral movement, and potential access to internal resources behind the VPN.
- **Status**: Actively exploited in the wild prior to disclosure. Patches have been released. Inc Ransomware has been observed leveraging these vulnerabilities for initial access.
- **CVE ID**: Not specified in source articles

### WordPress Core "wp2shell" Remote Code Execution
- **Description**: Critical remote code execution vulnerabilities in WordPress Core, collectively dubbed "wp2shell," allow unauthenticated attackers to execute arbitrary code on vulnerable installations. A persistent-object-cache condition has been identified as part of the attack surface.
- **Impact**: Full remote code execution on WordPress sites without authentication, leading to complete site compromise, data theft, and potential server takeover.
- **Status**: Public exploits and proof-of-concept code have been released. The two flaws now carry CVE IDs. Immediate patching is imperative.
- **CVE ID**: Not specified in source articles (articles note CVE IDs assigned but do not list them)

### 7-Zip Remote Code Execution via Malicious Archives
- **Description**: A remote code execution vulnerability in 7-Zip allows attackers to execute malicious code by convincing users to open specially crafted compressed archive files.
- **Impact**: Arbitrary code execution in the context of the user opening the archive, potentially leading to system compromise and malware installation.
- **Status**: Fixed in 7-Zip version 26.02 released June 25. Users must update immediately.
- **CVE ID**: Not specified in source articles

### Windows LegacyHive Zero-Day Privilege Escalation
- **Description**: A Windows zero-day exploit dubbed "LegacyHive" allows attackers to escalate privileges on up-to-date Windows systems, granting administrative access.
- **Impact**: Local privilege escalation to SYSTEM/Administrator level, enabling full control of the compromised host.
- **Status**: Exploit code publicly released by researcher "Nightmare Eclipse." No patch mentioned in source articles.
- **CVE ID**: Not specified in source articles

### OpenSSL HollowByte Denial-of-Service
- **Description**: The "HollowByte" flaw in OpenSSL allows unauthenticated attackers to trigger a denial-of-service condition using a malicious TLS payload of just 11 bytes. The server allocates up to 131 KB of memory for a message that never arrives, and on glibc systems that memory is not released until the process restarts.
- **Impact**: Memory exhaustion leading to service degradation or complete denial of service on affected OpenSSL servers.
- **Status**: Vulnerability publicly disclosed. Patching status not specified in source articles.
- **CVE ID**: Not specified in source articles

### Fortinet FortiSandbox Actively Exploited Vulnerabilities
- **Description**: Two vulnerabilities in the Fortinet FortiSandbox threat detection platform are being actively exploited in the wild.
- **Impact**: Compromise of threat detection infrastructure, potentially blinding security operations and enabling further network intrusion.
- **Status**: CISA has ordered federal agencies to prioritize patching by emergency directive. Actively exploited.
- **CVE ID**: Not specified in source articles

### ViPNet Software Update Mechanism Abuse
- **Description**: An advanced threat actor is abusing the update mechanism for the ViPNet private networking product suite to target Russian organizations, including government agencies.
- **Impact**: Supply chain-style compromise via trusted update channel, enabling persistent access to sensitive government networks.
- **Status**: Active campaign observed. Patch status not specified in source articles.
- **CVE ID**: Not specified in source articles

## Affected Systems and Products

- **SonicWall SMA 1000 Series**: Secure Mobile Access VPN appliances (1000 series) — exploited as zero-days for root access
- **WordPress Core**: All versions affected by "wp2shell" RCE flaws prior to patch — unauthenticated remote code execution
- **7-Zip**: Versions prior to 26.02 — RCE via malicious archive files
- **Windows**: Up-to-date Windows systems — LegacyHive zero-day privilege escalation
- **OpenSSL**: Servers using vulnerable OpenSSL versions — HollowByte DoS via 11-byte TLS requests
- **Fortinet FortiSandbox**: Threat detection platform — two actively exploited vulnerabilities
- **ViPNet Software Suite**: Private networking product suite — update mechanism abused for Russian government targeting
- **Vite npm Ecosystem**: Frontend tooling ecosystem — seven malicious packages delivering RAT via blockchain C2
- **AI/ML Services**: Exposed AI services — targeted by NadMesh botnet for AWS keys and Kubernetes tokens
- **DigiCert Infrastructure**: Code-signing certificate infrastructure — breached by GoldenEyeDog/CylindricalCanine cluster

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: Attackers present fake CAPTCHA or verification prompts that trick users into executing malicious PowerShell commands or scripts, used by UAC-0145 against Ukrainian targets and by ACR Stealer campaigns against enterprise customers
- **Steganographic Payload Delivery**: Malicious code hidden within SVG flag images delivered via fake coding tests, employed by North Korea's Contagious Interview campaign to deliver OtterCookie-aligned malware
- **Software Supply Chain Compromise**: Malicious npm packages targeting the Vite frontend tooling ecosystem, using blockchain-based command-and-control for resilience and evasion
- **Zero-Day Exploitation Chaining**: Two vulnerabilities chained on SonicWall SMA appliances to achieve unauthenticated root access, exploited by both an unknown threat actor and Inc Ransomware
- **Update Mechanism Hijacking**: Abuse of legitimate software update channels (ViPNet) to deliver payloads to high-value targets
- **Credential Harvesting from AI Infrastructure**: Automated scanning (Shodan harvester) for exposed AI services to extract cloud credentials (AWS keys, Kubernetes tokens) via the NadMesh Go botnet
- **Code-Signing Certificate Theft**: Breach of certificate authority infrastructure (DigiCert) to obtain valid code-signing certificates for malware distribution
- **Malicious Archive Exploitation**: Specially crafted compressed files exploiting 7-Zip RCE to achieve code execution upon user interaction
- **Privilege Escalation via Kernel/Driver Flaws**: Windows LegacyHive exploit leveraging legacy hive handling for local privilege escalation to SYSTEM
- **Memory Exhaustion DoS**: Trivial 11-byte TLS requests causing unbounded memory allocation in OpenSSL servers (HollowByte)

## Threat Actor Activities

- **UAC-0145 (Russian State-Sponsored)**: Leveraging ClickFix CAPTCHA lures to infect Ukrainian devices with data-stealing malware; ongoing campaign targeting Ukrainian entities
- **Inc Ransomware**: Exploiting chained SonicWall SMA zero-days for initial access to gain root-level capabilities on VPN appliances; ransomware deployment following network compromise
- **ACR Stealer Operators**: Surge in enterprise targeting using ClickFix lures to steal browser-stored passwords, live session tokens, PDFs, Microsoft 365 documents, and OneDrive-synced files; active since 2024
- **Contagious Interview Campaign (North Korea-Linked)**: Fake job coding tests delivering OtterCookie-aligned malware hidden via steganography in SVG flag images; targeting developers and job seekers
- **NadMesh Botnet Operator**: Go-based botnet scanning for exposed AI services via Shodan; harvesting AWS keys (3,811 unique keys claimed) and Kubernetes tokens for cloud compromise
- **GoldenEyeDog / CylindricalCanine Cluster**: Attributed to April 2026 DigiCert security incident involving code-signing certificate theft; enabling trusted malware distribution
- **Unknown Advanced Threat Actor (ViPNet Campaign)**: Abusing ViPNet update mechanism to target Russian government agencies; sophisticated supply chain-style intrusion
- **GoSerpent Operators**: Previously undocumented malware targeting Southeast Asian governments and diplomats for espionage since late 2025
- **Nightmare Eclipse (Security Researcher)**: Publicly released Windows LegacyHive zero-day exploit for privilege escalation on up-to-date Windows systems

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
