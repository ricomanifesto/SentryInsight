# Exploitation Report

## Executive Summary

Multiple critical exploitation campaigns are actively underway across diverse technology stacks. A Windows zero-day exploit dubbed LegacyHive has been publicly released, granting attackers administrative privileges on fully patched systems. Simultaneously, the Inc Ransomware group is chaining two SonicWall SMA zero-day vulnerabilities to achieve root-level access on mobile access appliances, while CISA has added an actively exploited SharePoint RCE zero-day (CVE-2026-58644) to its Known Exploited Vulnerabilities catalog, mandating immediate federal patching.

Public exploit code has surfaced for the "wp2shell" remote code execution vulnerabilities in WordPress Core, creating urgent risk for unpatched sites. The ACR Stealer infostealer campaign has surged against enterprise targets, leveraging ClickFix social engineering lures to harvest browser credentials, Microsoft 365 session tokens, and synchronized OneDrive files. On the supply chain front, seven malicious npm packages targeting the Vite ecosystem have been discovered using blockchain-based command-and-control infrastructure to deliver a remote access trojan.

## Active Exploitation Details

### Windows LegacyHive Zero-Day Privilege Escalation
- **Description**: A security researcher operating under the handle "Nightmare Eclipse" has publicly released a Windows zero-day exploit named LegacyHive that enables privilege escalation on up-to-date Windows systems. The exploit targets a legacy component in the Windows registry hive handling mechanism.
- **Impact**: Attackers can escalate from standard user privileges to full administrative control (SYSTEM) on current Windows versions without requiring authentication bypass or user interaction beyond initial code execution.
- **Status**: Zero-day publicly disclosed with functional exploit code available. No patch available at time of reporting. Organizations should implement application control and monitor for suspicious registry hive operations.

### SonicWall SMA Chained Zero-Day Exploitation
- **Description**: The Inc Ransomware group is actively exploiting two previously unknown vulnerabilities in SonicWall Secure Mobile Access (SMA) appliances. When chained together, these flaws provide unauthenticated attackers with root-level capabilities on the appliance.
- **Impact**: Full administrative compromise of VPN/mobile access gateways, enabling network persistence, credential harvesting, lateral movement, and ransomware deployment across connected enterprise networks.
- **Status**: Actively exploited in the wild by Inc Ransomware. SonicWall has not yet released patches for both vulnerabilities. Administrators should restrict SMA management access to trusted IPs and monitor for anomalous authentication patterns.

### SharePoint Server RCE Zero-Day (CVE-2026-58644)
- **Description**: A remote code execution vulnerability in Microsoft SharePoint Server that allows unauthenticated attackers to execute arbitrary code in the context of the SharePoint application pool.
- **Impact**: Complete compromise of SharePoint servers, potential access to sensitive documents, configuration data, and connected systems. Can serve as initial access vector for broader network intrusion.
- **Status**: Actively exploited in the wild. CISA added to Known Exploited Vulnerabilities catalog on July 17, 2026, requiring federal agencies to patch by July 20, 2026. Microsoft has released security updates.
- **CVE ID**: CVE-2026-58644

### WordPress Core "wp2shell" RCE Vulnerabilities
- **Description**: Two critical remote code execution vulnerabilities in WordPress Core collectively dubbed "wp2shell." The flaws involve a persistent-object-cache condition that enables unauthenticated attackers to achieve code execution. Full exploitation mechanism and working proof-of-concept code have been publicly released.
- **Impact**: Unauthenticated remote code execution on WordPress sites, leading to complete site takeover, data theft, malware distribution, and potential server compromise.
- **Status**: Public exploits available as of July 18, 2026. WordPress has released patched versions. All affected sites should update immediately.
- **CVE ID**: CVE IDs assigned but not specified in source articles

### OpenSSL HollowByte Denial-of-Service
- **Description**: A vulnerability in OpenSSL's TLS message handling where an 11-byte malicious ClientHello message causes the server to allocate up to 131 KB of memory for a message that never arrives. On glibc systems, this memory is not released until the process restarts.
- **Impact**: Unauthenticated denial-of-service leading to memory exhaustion and service unavailability. Can be amplified across multiple connections to rapidly deplete server resources.
- **Status**: Vulnerability disclosed with technical details. OpenSSL has released patches. Servers running unpatched OpenSSL versions are actively exploitable.
- **CVE ID**: Not specified in source articles

### Fortinet FortiSandbox Actively Exploited Vulnerabilities
- **Description**: Two vulnerabilities in the Fortinet FortiSandbox threat detection platform that are being actively exploited in the wild.
- **Impact**: Compromise of sandbox analysis infrastructure, potential bypass of threat detection, and pivot point into management networks.
- **Status**: Actively exploited. CISA has ordered federal agencies to prioritize patching. Fortinet has released security updates.
- **CVE ID**: Not specified in source articles

### 7-Zip Remote Code Execution
- **Description**: A remote code execution vulnerability in 7-Zip that triggers when users open specially crafted compressed archives. The flaw resides in archive parsing logic.
- **Impact**: Arbitrary code execution in the context of the user opening the malicious archive. Can lead to full system compromise if the user has administrative privileges.
- **Status**: Patched in 7-Zip version 26.02. Users should update immediately.
- **CVE ID**: Not specified in source articles

## Affected Systems and Products

- **Microsoft Windows (all current versions)**: Affected by LegacyHive zero-day privilege escalation exploit
- **SonicWall SMA Appliances (all firmware versions prior to patch)**: Vulnerable to chained zero-day exploitation by Inc Ransomware
- **Microsoft SharePoint Server (all supported versions)**: Affected by CVE-2026-58644 RCE zero-day
- **WordPress Core (versions prior to July 2026 security release)**: Vulnerable to wp2shell unauthenticated RCE
- **OpenSSL (versions prior to July 2026 patch)**: Vulnerable to HollowByte memory exhaustion DoS
- **Fortinet FortiSandbox (unpatched versions)**: Two actively exploited vulnerabilities
- **7-Zip (versions prior to 26.02)**: RCE via malicious archive files
- **Vite/Node.js development environments**: Targeted by seven malicious npm packages in supply chain attack
- **macOS systems**: Targeted by ClickLock information-stealing malware
- **Android devices**: Potential exposure through exposed AI services targeted by NadMesh botnet

## Attack Vectors and Techniques

- **Privilege Escalation via Legacy Registry Handling**: LegacyHive exploits outdated Windows registry hive processing to achieve SYSTEM privileges from standard user context
- **Vulnerability Chaining for Root Access**: Inc Ransomware combines two SonicWall SMA zero-days to escalate from unauthenticated access to root compromise
- **ClickFix Social Engineering**: ACR Stealer uses fake "verification" prompts (ClickFix technique) to trick users into executing malicious PowerShell commands that steal browser data and cloud tokens
- **Steganographic Payload Delivery**: North Korean actors (Contagious Interview campaign) hide OtterCookie malware in SVG flag images within fake coding test repositories
- **Blockchain-Based Command & Control**: Malicious Vite npm packages use blockchain transactions for resilient C2 infrastructure resistant to takedown
- **Supply Chain Compromise**: Seven typosquatted/impersonated npm packages targeting Vite developers to deliver RAT functionality
- **Memory Exhaustion via Minimal Payload**: HollowByte achieves DoS with only 11 bytes of malicious TLS traffic, exploiting OpenSSL's buffer allocation logic
- **Credential & Token Harvesting**: ACR Stealer extracts saved browser passwords, live session tokens, PDFs, Microsoft 365 documents, and OneDrive-synced files
- **AI Service Enumeration**: NadMesh botnet uses Shodan to discover exposed AI/ML services and harvest AWS keys and Kubernetes tokens
- **Code-Signing Certificate Theft**: GoldenEyeDog subgroup compromised DigiCert to steal code-signing certificates for malware distribution

## Threat Actor Activities

- **Inc Ransomware**: Actively exploiting chained SonicWall SMA zero-days for initial access and root-level compromise of enterprise VPN appliances. Demonstrates sophisticated vulnerability research and rapid weaponization capabilities.
- **ACR Stealer Operators**: Conducting large-scale enterprise credential theft campaigns using ClickFix lures. Active since 2024 with recent surge noted by Microsoft. Targets browser-stored credentials, M365 tokens, and cloud-synced files.
- **GoldenEyeDog / CylindricalCanine**: Attributed to April 2026 DigiCert breach resulting in code-signing certificate theft. Subgroup of larger CylindricalCanine cluster. Enables trusted malware distribution via stolen certificates.
- **Contagious Interview (North Korea-linked)**: Running fake job interview campaigns targeting developers. Uses steganography in SVG images to deliver OtterCookie-aligned malware. Persistent social engineering operation.
- **NadMesh Botnet Operator**: Go-based botnet actively scanning for exposed AI services since early July 2026. Operator dashboard claims 3,811 unique AWS keys harvested. Uses Shodan for target enumeration.
- **GoSerpent Actors**: Previously undocumented malware targeting Southeast Asian governments and diplomats since late 2025. Espionage-focused campaign with custom Go-based tooling.
- **Unknown/Unattributed - Fairlife Ransomware**: Ransomware attack on Coca-Cola's Fairlife subsidiary halting US dairy production. Attribution not publicly disclosed.
- **Unknown/Unattributed - Abbott Intrusion**: Two separate incidents involving unauthorized access to legacy Exact Sciences systems in Cancer Diagnostics business. Extortion claims reported.

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
