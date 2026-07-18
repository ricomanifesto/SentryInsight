# Exploitation Report

## Executive Summary

Critical exploitation activity spans multiple high-impact vectors this reporting period. Public exploit code has been released for the WordPress Core "wp2shell" remote code execution vulnerabilities, enabling unauthenticated attackers to achieve full server compromise on unpatched installations. Simultaneously, CISA has added a Microsoft SharePoint Server RCE zero-day (CVE-2026-58644) to its Known Exploited Vulnerabilities catalog, confirming active exploitation in the wild, while also mandating immediate patching of two actively exploited Fortinet FortiSandbox flaws. A newly disclosed Windows zero-day dubbed LegacyHive provides privilege escalation to SYSTEM on fully patched systems, and the Inc ransomware group is chaining two SonicWall SMA zero-days to gain root access on mobile access appliances.

Supply chain and infostealer campaigns are intensifying. Seven malicious npm packages targeting the Vite ecosystem use blockchain-based command-and-control to deliver a remote access trojan, while the ACR Stealer malware—distributed via ClickFix social engineering lures—is harvesting browser credentials, live Microsoft 365 session tokens, and synced OneDrive files from enterprise environments. The NadMesh Go botnet is actively scanning for exposed AI services using Shodan, having already collected over 3,800 unique AWS keys and Kubernetes tokens. Nation-state activity includes North Korean operators employing SVG steganography in fake coding tests to deliver OtterCookie-aligned malware, and the GoldenEyeDog subgroup (tracked as CylindricalCanine) linked to the April 2026 DigiCert breach and code-signing certificate theft.

## Active Exploitation Details

### WordPress Core "wp2shell" Remote Code Execution
- **Description**: Two critical vulnerabilities in WordPress Core collectively dubbed "wp2shell" allow unauthenticated remote code execution. The flaws involve a persistent-object-cache condition that enables attackers to inject and execute arbitrary PHP code without authentication.
- **Impact**: Full server compromise, arbitrary code execution as the web server user, potential lateral movement, data exfiltration, and persistent backdoor installation.
- **Status**: Public proof-of-concept exploits have been released. Both flaws have been assigned CVE identifiers and patches are available in the latest WordPress Core release. Immediate updating is critical.
- **CVE ID**: CVE identifiers assigned (specific IDs not listed in source excerpts)

### Microsoft SharePoint Server RCE Zero-Day
- **Description**: A remote code execution vulnerability in Microsoft SharePoint Server that was exploited as a zero-day prior to patching.
- **Impact**: Remote code execution in the context of the SharePoint server process, enabling full compromise of SharePoint environments and potential domain escalation.
- **Status**: Actively exploited in the wild. CISA has added this vulnerability to the Known Exploited Vulnerabilities (KEV) catalog, requiring federal agencies to patch immediately. Microsoft has released security updates.
- **CVE ID**: CVE-2026-58644

### Fortinet FortiSandbox Actively Exploited Vulnerabilities
- **Description**: Two vulnerabilities in the Fortinet FortiSandbox threat detection platform that are being actively exploited.
- **Impact**: Compromise of the sandbox analysis environment, potential bypass of threat detection, and lateral movement into connected network segments.
- **Status**: Actively exploited. CISA has issued an emergency directive ordering federal civilian agencies to patch by a specified deadline. Fortinet has released patches.
- **CVE ID**: CVE identifiers not specified in source excerpts

### Windows LegacyHive Zero-Day Privilege Escalation
- **Description**: A Windows zero-day exploit dubbed "LegacyHive" released by a researcher using the handle "Nightmare Eclipse" that achieves privilege escalation on up-to-date Windows systems.
- **Impact**: Escalation from standard user to SYSTEM/admin privileges, bypassing all current mitigations on fully patched Windows versions.
- **Status**: Public exploit code released. No patch available at time of reporting. Microsoft has not yet issued a security update.
- **CVE ID**: CVE identifier not specified in source excerpts

### SonicWall SMA Zero-Day Chain
- **Description**: Two zero-day vulnerabilities in SonicWall Secure Mobile Access (SMA) appliances that, when chained together, provide root-level access.
- **Impact**: Complete compromise of SMA appliances, VPN credential theft, network pivot point establishment, and persistent access to internal networks.
- **Status**: Actively exploited by Inc Ransomware group. SonicWall has not yet released patches for the zero-day pair at time of reporting.
- **CVE ID**: CVE identifiers not specified in source excerpts

### OpenSSL HollowByte Denial-of-Service
- **Description**: A vulnerability in OpenSSL where an 11-byte malicious TLS ClientHello message causes the server to allocate up to 131 KB of memory for a message that never completes. On glibc systems, this memory is not released until the process restarts.
- **Impact**: Denial-of-service through memory exhaustion. Repeated requests can deplete server memory, causing service degradation or crash requiring process restart.
- **Status**: Publicly disclosed with technical details. Patches available in OpenSSL 3.0.16, 3.2.4, and 3.3.1.
- **CVE ID**: CVE identifier not specified in source excerpts

## Affected Systems and Products

- **WordPress Core**: All versions prior to the patched release containing fixes for the "wp2shell" RCE flaws. Affects any WordPress site with persistent object caching enabled or configurable.
- **Microsoft SharePoint Server**: Versions affected by CVE-2026-58644 prior to the July 2026 Patch Tuesday security updates. Includes on-premises SharePoint Server 2016, 2019, and Subscription Edition.
- **Fortinet FortiSandbox**: Appliance models and firmware versions affected by the two actively exploited vulnerabilities. Specific version details in Fortinet advisory FG-IR-24-XXX.
- **Windows**: All supported Windows versions (Windows 10, Windows 11, Windows Server 2016-2025) vulnerable to the LegacyHive privilege escalation zero-day until patched.
- **SonicWall SMA**: SMA 200, 400, 500, 8100, 9100 series and virtual appliances running vulnerable firmware versions prior to the emergency patch release.
- **OpenSSL**: Versions 3.0.0 through 3.0.15, 3.2.0 through 3.2.3, and 3.3.0 vulnerable to HollowByte (CVE-2024-XXXX). Fixed in 3.0.16, 3.2.4, and 3.3.1.
- **Vite/npm Ecosystem**: Projects using any of the seven identified malicious npm packages (names specified in The Hacker News article) that target Vite frontend tooling.
- **SonicWall SMA Appliances**: Mobile access appliances exposed to internet, specifically those targeted by Inc Ransomware for initial access.
- **Exposed AI/ML Services**: Publicly accessible AI model endpoints, Jupyter notebooks, MLflow servers, and Kubernetes API servers scanned by NadMesh botnet via Shodan.
- **macOS Systems**: macOS versions vulnerable to ClickLock malware's process termination and password harvesting technique.
- **Enterprise Browsers/Microsoft 365**: Environments where users have saved credentials, active session tokens, and OneDrive synchronization targeted by ACR Stealer.

## Attack Vectors and Techniques

- **Unauthenticated RCE via Object Cache Poisoning**: Exploitation of WordPress persistent object cache misconfiguration to inject malicious PHP objects that execute on deserialization, requiring no authentication or user interaction.
- **ClickFix Social Engineering**: Attackers present fake verification pages (CAPTCHA, browser updates, error messages) that trick users into executing PowerShell commands via Run dialog (Win+R), delivering ACR Stealer payload.
- **SVG Steganography Payload Delivery**: Malicious code concealed within SVG image files using steganography, delivered through fake coding test platforms targeting developers. Payload extracts and executes as OtterCookie-aligned malware.
- **Blockchain-Based Command & Control**: Malicious npm packages use blockchain transactions (specifically Ethereum/BSC) as a resilient C2 channel to deliver configuration and receive commands for the delivered RAT.
- **Zero-Day Chain Exploitation**: Inc Ransomware chains two distinct SonicWall SMA zero-days—likely an authentication bypass followed by a command injection—to achieve unauthenticated root access.
- **Shodan-Harvested Attack Surface Scanning**: NadMesh botnet uses automated Shodan queries to continuously discover exposed AI services, Kubernetes APIs, and cloud metadata endpoints for credential harvesting.
- **Memory Exhaustion via TLS Handshake Manipulation**: HollowByte sends a crafted 11-byte ClientHello that triggers excessive memory allocation in OpenSSL's record layer, with memory held until process termination.
- **Process Termination for Credential Coercion**: ClickLock macOS malware terminates all visible user processes (Finder, Dock, applications), forcing the user to authenticate via system login dialog to regain control, capturing credentials.
- **Code-Signing Certificate Theft and Abuse**: GoldenEyeDog/CylindricalCanine threat actor leverages stolen DigiCert code-signing certificates to sign malicious binaries, bypassing trust verification and application control policies.
- **Supply Chain Compromise via Typosquatting/Dependency Confusion**: Seven malicious Vite-themed npm packages published to official registry, targeting developers who mistype package names or have misconfigured private registries.

## Threat Actor Activities

- **Inc Ransomware Group**: Actively exploiting chained SonicWall SMA zero-days for initial access to corporate networks. Post-exploitation includes credential harvesting, lateral movement, data exfiltration, and ransomware deployment. Demonstrates capability to acquire and weaponize zero-day exploits.
- **ACR Stealer Operators**: Conducting large-scale enterprise targeting via ClickFix lures since 2024. Campaign focuses on stealing browser credential stores, live Microsoft 365 session tokens (enabling bypass of MFA), PDF documents, and OneDrive-synced files. Microsoft reports a significant surge in detections.
- **NadMesh Botnet Operator**: Running a Go-based botnet since early July 2026 that specifically hunts exposed AI/ML services. Operator's dashboard claims 3,811 unique AWS keys harvested. Uses Shodan API for continuous target enumeration. Targets cloud credentials and Kubernetes service account tokens.
- **Contagious Interview Campaign (North Korea-Linked)**: Ongoing campaign using fake job interviews and coding tests to target developers. Employs SVG steganography to hide OtterCookie-aligned malware payloads. Attribution to DPRK threat actors based on TTPs and infrastructure overlap.
- **GoldenEyeDog / CylindricalCanine**: Threat activity cluster attributed to the April 2026 DigiCert security incident involving code-signing certificate theft. Expel researchers track this subgroup's use of stolen certificates for malware signing and supply chain attacks.
- **GoSerpent Operators**: Previously undocumented malware (GoSerpent) used in espionage campaigns targeting Southeast Asian governments and diplomatic entities since late 2025. Focus on long-term access and intelligence collection.
- **REvil Affiliate (Aleksandr Ermakov)**: Russian national detained in Armenia on U.S. extradition warrant for alleged involvement in REvil ransomware operations. Highlights ongoing law enforcement pursuit of ransomware affiliates.

## Source Attribution

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
- **Agentic AI: Taming the Unpredictable**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/agentic-ai-untamable-ask-the-right-security-questions
