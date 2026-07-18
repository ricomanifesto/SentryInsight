# Exploitation Report

## Executive Summary

Critical exploitation activity spans multiple high-impact vectors this reporting period. A Microsoft SharePoint Server remote code execution zero-day (CVE-2026-58644) has been added to CISA's Known Exploited Vulnerabilities catalog, mandating immediate federal agency patching. Simultaneously, a core WordPress vulnerability dubbed "wp2shell" enables unauthenticated remote code execution on all versions 6.9 and 7.0, requiring no plugins for exploitation. CISA has also issued an urgent directive for two actively exploited Fortinet FortiSandbox vulnerabilities. These actively exploited flaws represent immediate risk to internet-facing infrastructure.

Ransomware operations continue leveraging zero-day chains for initial access. The Inc Ransomware group is actively chaining two SonicWall SMA zero-days to achieve root-level compromise of mobile access appliances. A newly disclosed Windows zero-day exploit named "LegacyHive," released by a researcher under the handle "Nightmare Eclipse," provides privilege escalation on fully patched Windows systems. The OpenSSL "HollowByte" denial-of-service flaw allows unauthenticated attackers to exhaust server memory with a mere 11-byte TLS request, affecting unpatched OpenSSL deployments across glibc-based systems.

Threat actor activity shows sophisticated evolution across espionage, cybercrime, and supply chain domains. North Korean actors aligned with the Contagious Interview campaign are employing SVG steganography to deliver OtterCookie malware through fake coding tests. The NadMesh Go botnet has harvested over 3,800 AWS keys by scanning for exposed AI services via Shodan. GoldenEyeDog, a subgroup of the CylindricalCanine cluster, has been attributed to the April 2026 DigiCert breach involving code-signing certificate theft. Meanwhile, infostealers including ACR Stealer, ClickLock, and OkoBot are deploying novel techniques such as ClickFix social engineering, process termination for credential coercion, and multi-payload frameworks targeting cryptocurrency assets.

## Active Exploitation Details

### Microsoft SharePoint Server RCE Zero-Day (CVE-2026-58644)
- **Description**: A remote code execution vulnerability in Microsoft SharePoint Server that has been actively exploited in the wild. The flaw allows unauthenticated attackers to execute arbitrary code on affected SharePoint instances.
- **Impact**: Full remote code execution on SharePoint Server, potentially leading to complete server compromise, data exfiltration, and lateral movement within enterprise networks.
- **Status**: Actively exploited. CISA added this vulnerability to the Known Exploited Vulnerabilities (KEV) catalog on Thursday, requiring Federal Civilian Executive Branch agencies to apply mitigations or patches immediately. Microsoft has released security updates addressing this flaw.
- **CVE ID**: CVE-2026-58644

### WordPress Core "wp2shell" Unauthenticated RCE
- **Description**: A critical vulnerability in WordPress core (not plugin-dependent) that allows unauthenticated remote code execution via a single anonymous HTTP request. The flaw affects all WordPress 6.9 and 7.0 installations in their default configuration.
- **Impact**: Complete compromise of WordPress sites without any authentication or user interaction. Attackers can execute arbitrary PHP code, leading to full site takeover, malware injection, data theft, and use as a platform for further attacks.
- **Status**: Actively exploitable until Friday's patch release. WordPress has issued security updates for versions 6.9 and 7.0. All unpatched sites remain at immediate risk.
- **CVE ID**: Not explicitly provided in source article

### SonicWall SMA Zero-Day Chain (Inc Ransomware)
- **Description**: Two zero-day vulnerabilities in SonicWall Secure Mobile Access (SMA) appliances that, when chained together, provide threat actors with root-level capabilities on the affected devices.
- **Impact**: Full administrative control over SonicWall SMA appliances, enabling VPN credential theft, network pivoting, persistence establishment, and deployment of ransomware payloads across the victim's internal network.
- **Status**: Actively exploited by Inc Ransomware group. SonicWall has not yet released patches for these zero-days at the time of reporting. Organizations should restrict management access and monitor for suspicious authentication attempts.
- **CVE ID**: Not explicitly provided in source article

### Windows "LegacyHive" Zero-Day Privilege Escalation
- **Description**: A Windows zero-day exploit released by security researcher "Nightmare Eclipse" that enables local privilege escalation to SYSTEM/admin privileges on up-to-date Windows systems.
- **Impact**: Local attackers or malware with foothold access can elevate privileges to administrator/SYSTEM level, bypassing security controls, disabling defenses, and achieving full system control.
- **Status**: Public exploit code released (zero-day). No patch available at time of reporting. Microsoft has not yet issued a security update for this vulnerability.
- **CVE ID**: Not explicitly provided in source article

### OpenSSL "HollowByte" Denial-of-Service
- **Description**: A vulnerability in OpenSSL where an 11-byte malicious TLS ClientHello message triggers allocation of up to 131 KB of server memory for a message that never completes. On glibc systems, this memory is not released until the process restarts.
- **Impact**: Unauthenticated remote denial-of-service. Attackers can exhaust server memory by sending repeated small payloads, causing service degradation or crash. Particularly dangerous for high-traffic TLS-terminating services.
- **Status**: Vulnerability disclosed with technical details. OpenSSL has released patches (versions 3.0.16, 3.2.2, 3.3.1, and 3.4.0). Unpatched servers remain vulnerable to trivial DoS attacks.
- **CVE ID**: Not explicitly provided in source articles

### Fortinet FortiSandbox Actively Exploited Vulnerabilities
- **Description**: Two vulnerabilities in Fortinet FortiSandbox threat detection platform that CISA has confirmed are under active exploitation.
- **Impact**: Compromise of the threat detection platform itself, potentially allowing attackers to bypass security monitoring, exfiltrate sandbox analysis results, and pivot to connected network segments.
- **Status**: Actively exploited. CISA issued an emergency directive ordering Federal Civilian Executive Branch agencies to prioritize patching by Sunday. Fortinet has released security updates.
- **CVE ID**: Not explicitly provided in source article

### DigiCert Code-Signing Certificate Theft (GoldenEyeDog/CylindricalCanine)
- **Description**: A security incident at DigiCert in April 2026 attributed to the GoldenEyeDog subgroup of the CylindricalCanine threat activity cluster, resulting in theft of code-signing certificates.
- **Impact**: Stolen code-signing certificates enable attackers to sign malicious software with trusted credentials, bypassing application allowlisting, reputation checks, and user trust mechanisms. Facilitates supply chain attacks and malware distribution.
- **Status**: Incident occurred April 2026; attribution and technical details published by Expel in July 2026. DigiCert has revoked compromised certificates. Organizations must verify software signatures and monitor for misuse of affected certificates.
- **CVE ID**: Not applicable (security incident, not a software vulnerability)

## Affected Systems and Products

- **WordPress**: Versions 6.9 and 7.0 (all default installations, zero plugins required for exploitation)
- **Microsoft SharePoint Server**: Versions affected by CVE-2026-58644 (specific versions per Microsoft advisory)
- **SonicWall Secure Mobile Access (SMA) Appliances**: Models running vulnerable firmware (specific versions per SonicWall advisory)
- **Windows**: All currently supported versions vulnerable to LegacyHive privilege escalation (per researcher claims)
- **OpenSSL**: Versions prior to 3.0.16, 3.2.2, 3.3.1, and 3.4.0 (all series affected)
- **Fortinet FortiSandbox**: Versions affected by the two actively exploited flaws (per Fortinet advisory)
- **DigiCert Code-Signing Infrastructure**: Compromised certificates issued prior to April 2026 revocation
- **npm/Vite Ecosystem**: Developers and CI/CD pipelines that installed seven identified malicious packages
- **macOS**: Systems targeted by ClickLock malware (version specifics not disclosed)
- **Chrome Browser with Claude Extension**: Users with Anthropic's Claude for Chrome extension installed

## Attack Vectors and Techniques

- **Unauthenticated HTTP RCE**: Single anonymous HTTP request to WordPress core endpoint achieves code execution (wp2shell)
- **Zero-Day Vulnerability Chaining**: Two SonicWall SMA flaws combined for root access without authentication
- **TLS Protocol Memory Exhaustion**: 11-byte ClientHello triggers unbounded memory allocation in OpenSSL (HollowByte)
- **Local Privilege Escalation**: LegacyHive exploit elevates standard user to SYSTEM/admin on patched Windows
- **SVG Steganography**: Malicious payloads concealed in SVG flag images, decoded at runtime (Contagious Interview/OtterCookie)
- **ClickFix Social Engineering**: Fake browser error prompts trick users into executing malicious PowerShell commands (ACR Stealer)
- **Process Termination for Credential Coercion**: ClickLock terminates all visible GUI processes, forcing macOS users to authenticate
- **Blockchain-Based C2**: Malicious npm packages use blockchain transactions for command-and-control resilience
- **Shodan-Harvested Target Lists**: NadMesh botnet uses continuous Shodan scanning to queue exposed AI service endpoints
- **Text Salting/Hidden Text**: Phishing emails embed invisible characters to evade AI/ML-based security filters
- **Malicious Extension Click Simulation**: Rogue Chrome extensions simulate user clicks on Claude extension to trigger AI actions
- **Multi-Payload Framework Deployment**: OkoBot delivers 20+ specialized payloads for credential theft, crypto wallet drainage, and data exfiltration
- **Residential Proxy Abuse**: Carding operations leverage "clean" residential proxies combined with browser fingerprinting to evade fraud detection
- **Third-Party Support System Compromise**: EY breach originated from compromised IT support ticketing platform

## Threat Actor Activities

- **Inc Ransomware**: Actively exploiting chained SonicWall SMA zero-days for initial access to corporate networks, deploying ransomware after achieving root on VPN appliances
- **NadMesh Botnet Operator**: Go-based botnet scanning for exposed AI/ML services via Shodan; dashboard claims 3,811 unique AWS keys and Kubernetes tokens harvested since early July 2026
- **GoldenEyeDog (CylindricalCanine Subgroup)**: Attributed to April 2026 DigiCert breach; stole code-signing certificates enabling trusted malware signing; technical details shared by Expel
- **Contagious Interview / North Korean Actors**: Ongoing campaign using fake coding tests and SVG steganography to deliver OtterCookie-aligned malware; targets developers and job seekers
- **ACR Stealer Operators**: Infostealer active since 2024; recently adopted ClickFix lures to steal browser passwords, session tokens, Microsoft 365 documents, and OneDrive files
- **GoSerpent Operators**: Previously undocumented malware targeting Southeast Asian governments and diplomats since late 2025; espionage-focused with modular Go-based architecture
- **ClickLock Operators**: New macOS info-stealer using aggressive process termination to coerce user credentials; distribution vector not fully characterized
- **OkoBot Operators**: Framework deploying 20+ payloads targeting cryptocurrency wallet seed phrases, browser credentials, and sensitive documents
- **Fairlife Ransomware Attackers**: Undisclosed ransomware group disrupted Coca-Cola's Fairlife dairy production across the United States
- **REvil Affiliates**: Law enforcement action (Armenia/US) targeting alleged REvil ransomware suspect Aleksandr Ermakov; highlights ongoing ransomware ecosystem disruption
- **Malicious npm Package Publishers**: Seven Vite-targeted packages published to npm registry with blockchain C2 and RAT capabilities; supply chain attack on frontend developers

## Source Attribution

- **New wp2shell WordPress Core Flaw Lets Unauthenticated Attackers Run Code**: The Hacker News - https://thehackernews.com/2026/07/new-wp2shell-wordpress-core-flaw-lets.html
- **Abbott Laboratories probes two cyber incidents amid extortion claims**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/abbott-laboratories-probes-two-cyber-incidents-amid-extortion-claims/
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
- **1M+ Emails Use Hidden Text to Dupe AI Security Filters**: Dark Reading - https://www.darkreading.com/threat-intelligence/1m-emails-hidden-text-dupe-ai-security-filters
- **Claude Chrome extension flaw lets malicious extensions trigger AI actions**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/claude-chrome-extension-flaw-lets-malicious-extensions-trigger-ai-actions/
- **New OkoBot framework deploys 20 payloads to steal data, crypto**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-okobot-framework-deploys-20-payloads-to-steal-data-crypto/
