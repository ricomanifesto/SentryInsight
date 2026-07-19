# Exploitation Report

## Executive Summary

Critical exploitation activity surged across multiple fronts in July 2026. A Windows zero-day dubbed LegacyHive grants attackers administrative privileges on fully patched systems, while public exploits for the "wp2shell" WordPress Core RCE vulnerabilities place millions of sites at immediate risk. CISA added an actively exploited SharePoint RCE zero-day (CVE-2026-58644) to its Known Exploited Vulnerabilities catalog and ordered federal agencies to patch two Fortinet FortiSandbox flaws under active attack.

Simultaneously, threat actors are chaining SonicWall SMA zero-days for root-level appliance compromise, weaponizing the OpenSSL "HollowByte" DoS flaw with 11-byte payloads, and distributing malware through malicious npm packages targeting the Vite ecosystem. The ACR Stealer infostealer campaign has intensified against enterprise environments using ClickFix social-engineering lures, while a new Go-based botnet (NadMesh) scans exposed AI services to harvest cloud credentials and Kubernetes tokens. North Korean operators continue the Contagious Interview campaign, hiding OtterCookie malware in SVG images delivered via fake coding tests.

## Active Exploitation Details

### Windows LegacyHive Zero-Day Privilege Escalation
- **Description**: A security researcher using the handle "Nightmare Eclipse" released a Windows zero-day exploit named LegacyHive that allows attackers to escalate privileges on up-to-date Windows systems. The exploit targets a legacy component in the Windows registry hive handling.
- **Impact**: Attackers gain administrative privileges on fully patched Windows installations, enabling complete system compromise, persistence, and lateral movement.
- **Status**: Zero-day actively exploited; no patch available at time of disclosure. Microsoft has not yet released a fix.
- **CVE ID**: Not yet assigned in source article

### WordPress Core "wp2shell" RCE Vulnerabilities
- **Description**: Critical remote code execution vulnerabilities in WordPress Core collectively dubbed "wp2shell." The flaws allow unauthenticated attackers to execute arbitrary code on vulnerable WordPress installations. Full exploitation mechanism has been published and a working proof-of-concept is public.
- **Impact**: Complete takeover of WordPress sites without authentication. Attackers can install backdoors, deface sites, steal data, and use compromised servers for further attacks.
- **Status**: Public exploits released; active exploitation expected. WordPress has released patches. Two flaws now carry CVE IDs.
- **CVE ID**: CVE IDs assigned but not specified in source articles

### SharePoint RCE Zero-Day (CVE-2026-58644)
- **Description**: A remote code execution vulnerability in Microsoft SharePoint Server that has been actively exploited in the wild. The flaw allows unauthenticated attackers to execute code on affected SharePoint servers.
- **Impact**: Full compromise of SharePoint servers, potential access to sensitive corporate documents, credentials, and internal networks.
- **Status**: Actively exploited; added to CISA KEV catalog on July 17, 2026. Microsoft has released patches. Federal agencies ordered to patch immediately.
- **CVE ID**: CVE-2026-58644

### Fortinet FortiSandbox Actively Exploited Vulnerabilities
- **Description**: Two vulnerabilities in the Fortinet FortiSandbox threat detection platform that are being actively exploited in the wild.
- **Impact**: Compromise of the sandbox analysis environment, potential bypass of threat detection, and pivot to internal networks.
- **Status**: Actively exploited; CISA ordered federal civilian agencies to prioritize patching by July 20, 2026. Fortinet has released fixes.
- **CVE ID**: CVE IDs not specified in source article

### SonicWall SMA Zero-Day Chain
- **Description**: Two zero-day vulnerabilities in SonicWall Secure Mobile Access (SMA) appliances that, when chained together, allow threat actors to gain root-level capabilities on the appliances.
- **Impact**: Full administrative control over VPN/appliance gateways, enabling network access, credential harvesting, and persistence at the network edge.
- **Status**: Actively exploited by Inc Ransomware group. Zero-days; patches not mentioned in source article.
- **CVE ID**: CVE IDs not specified in source article

### OpenSSL "HollowByte" Denial-of-Service Flaw
- **Description**: A vulnerability in OpenSSL where an 11-byte malicious TLS request causes the server to allocate up to 131 KB of memory for a message that never arrives. On glibc systems, the memory is not released until the process restarts.
- **Impact**: Denial-of-service through memory exhaustion. Repeated attacks can freeze or crash OpenSSL servers, disrupting TLS-dependent services.
- **Status**: Vulnerability disclosed with technical details; patches available in updated OpenSSL versions.
- **CVE ID**: CVE ID not specified in source articles

### 7-Zip Remote Code Execution Flaw
- **Description**: A remote code execution vulnerability in 7-Zip that can be triggered by convincing users to open specially crafted compressed archives.
- **Impact**: Arbitrary code execution in the context of the user opening the archive, leading to malware installation, data theft, and system compromise.
- **Status**: Fixed in 7-Zip version 26.02. Users urged to update immediately.
- **CVE ID**: CVE ID not specified in source article

### Malicious Vite npm Supply Chain Attack
- **Description**: Seven malicious npm packages targeting the Vite frontend tooling ecosystem, using blockchain-based command-and-control infrastructure to deliver a remote access trojan (RAT).
- **Impact**: Compromise of development environments, potential supply chain poisoning of downstream applications, persistent remote access to developer machines.
- **Status**: Packages discovered and reported; npm has likely removed them. Active campaign targeting developers.
- **CVE ID**: Not applicable (supply chain malware)

### NadMesh Botnet Credential Harvesting
- **Description**: A Go-based botnet actively scanning for exposed AI services to harvest AWS keys, Kubernetes tokens, and other cloud credentials. The operator's dashboard claims 3,811 unique AWS keys collected.
- **Impact**: Cloud account takeover, Kubernetes cluster compromise, cryptojacking, data exfiltration, and lateral movement in cloud environments.
- **Status**: Active campaign since early July 2026. Uses Shodan to maintain scan queue of exposed AI/ML endpoints.
- **CVE ID**: Not applicable (credential harvesting campaign)

### ACR Stealer Infostealer Campaign
- **Description**: An information-stealing malware (active since 2024) now surging against enterprise customers. Uses ClickFix social-engineering lures to trick users into executing malicious commands.
- **Impact**: Theft of browser-stored passwords, live session tokens, PDFs, Microsoft 365 documents, and files from synced OneDrive folders.
- **Status**: Active surge observed by Microsoft. ClickFix delivery vector increasing effectiveness.
- **CVE ID**: Not applicable (malware campaign)

### ClickLock macOS Information Stealer
- **Description**: A new macOS malware that terminates all visible processes to force users into entering their system login password, which is then captured.
- **Impact**: Theft of macOS user credentials, enabling full system access and potential keychain compromise.
- **Status**: Newly discovered; active distribution vector not fully detailed.
- **CVE ID**: Not applicable (malware)

### GoSerpent Espionage Malware
- **Description**: Previously undocumented malware targeting Southeast Asian governments and diplomats since late 2025 for cyber espionage.
- **Impact**: Persistent access to government networks, document exfiltration, credential theft, and intelligence gathering.
- **Status**: Active campaign; attribution and full capabilities under analysis.
- **CVE ID**: Not applicable (malware/APT campaign)

### North Korean Contagious Interview Campaign
- **Description**: North Korean threat actors using fake coding tests and steganography in SVG flag images to deliver OtterCookie-aligned malware.
- **Impact**: Compromise of developer and job-seeker systems, potential supply chain access, persistent remote access.
- **Status**: Active campaign; steganographic payload delivery evades standard detection.
- **CVE ID**: Not applicable (targeted attack campaign)

### GoldenEyeDog / CylindricalCanine DigiCert Breach
- **Description**: Threat activity cluster "CylindricalCanine" (subgroup GoldenEyeDog) attributed to the April 2026 DigiCert security incident involving code-signing certificate theft.
- **Impact**: Theft of code-signing certificates enables malware signing to bypass trust controls, supply chain attacks, and privilege escalation via trusted binaries.
- **Status**: Breach occurred April 2026; attribution published July 2026. Certificate revocation and impact assessment ongoing.
- **CVE ID**: Not applicable (intrusion/certificate theft)

## Affected Systems and Products

- **7-Zip**: Versions prior to 26.02 on Windows, Linux, and macOS
- **WordPress Core**: All versions prior to patched releases; specific versions not detailed in source articles
- **Microsoft SharePoint Server**: Versions affected by CVE-2026-58644; specific versions not detailed in source article
- **Fortinet FortiSandbox**: Affected versions not specified in source article; threat detection platform appliances
- **SonicWall SMA (Secure Mobile Access)**: Appliance firmware versions vulnerable to the two zero-days; specific versions not detailed
- **OpenSSL**: Versions vulnerable to HollowByte flaw; specific versions not detailed in source articles (affects glibc-based systems)
- **Vite/npm Ecosystem**: Developers using Vite frontend tooling; seven specific malicious packages named in source article
- **AI/ML Services**: Exposed AI model endpoints, Jupyter notebooks, MLflow servers, and Kubernetes API servers accessible from internet
- **Windows**: All supported versions vulnerable to LegacyHive privilege escalation zero-day
- **macOS**: Systems targeted by ClickLock malware; specific versions not detailed
- **DigiCert Code-Signing Infrastructure**: Certificate authorities and subscribers affected by code-signing certificate theft

## Attack Vectors and Techniques

- **Malicious Archive Execution**: Crafted 7-Zip archives triggering RCE when opened by users
- **Unauthenticated Web RCE**: Direct exploitation of WordPress Core and SharePoint Server without credentials
- **Zero-Day Chaining**: Combining two SonicWall SMA zero-days for root-level appliance compromise
- **TLS Memory Exhaustion**: 11-byte malicious ClientHello/request triggering unbounded memory allocation in OpenSSL (HollowByte)
- **Software Supply Chain Compromise**: Typosquatting/brandjacking npm packages targeting Vite developers with blockchain C2
- **Credential Harvesting at Scale**: Automated scanning (Shodan) of exposed AI/ML services for cloud keys and Kubernetes tokens
- **ClickFix Social Engineering**: Fake "verify you are human" / error pages tricking users into pasting malicious PowerShell commands
- **Steganographic Payload Delivery**: Malicious code hidden in SVG image files (flag images) delivered via fake coding tests
- **Process Termination Credential Phishing**: ClickLock terminates visible processes to force macOS password entry
- **Code-Signing Certificate Theft**: Intrusion into CA infrastructure to steal trusted signing certificates for malware distribution
- **Ransomware Deployment via Edge Appliances**: Inc Ransomware using SonicWall zero-days for initial access
- **Infostealer Distribution**: ACR Stealer delivered via ClickFix; GoSerpent via targeted spear-phishing (inferred)

## Threat Actor Activities

- **Nightmare Eclipse (Researcher/Handle)**: Publicly released Windows LegacyHive zero-day exploit; motivation appears to be disclosure/research but enables malicious use
- **Inc Ransomware Group**: Actively exploiting chained SonicWall SMA zero-days for initial access to deploy ransomware
- **ACR Stealer Operators**: Conducting surge campaign against enterprise customers using ClickFix lures; infrastructure active since 2024
- **NadMesh Botnet Operator**: Running Go-based botnet harvesting AWS keys and Kubernetes tokens from exposed AI services; dashboard shows 3,811 AWS keys collected
- **Contagious Interview / North Korean Actors (DPRK)**: Running fake job interview campaigns targeting developers; using SVG steganography for OtterCookie malware delivery
- **CylindricalCanine / GoldenEyeDog**: Threat cluster attributed to April 2026 DigiCert breach and code-signing certificate theft; Expel shared technical details
- **GoSerpent Operators**: Conducting espionage against Southeast Asian governments and diplomats since late 2025; previously undocumented malware
- **REvil Affiliate (Aleksandr Ermakov)**: Russian tourist detained in Armenia on U.S. warrant for REvil ransomware activities; lawyers claim mistaken identity

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
