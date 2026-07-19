# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse platforms, ranging from widely deployed enterprise software to developer tooling and operating systems. CISA has added a Microsoft SharePoint Server zero-day (CVE-2026-58644) to its Known Exploited Vulnerabilities catalog and ordered federal agencies to patch two actively exploited Fortinet FortiSandbox flaws. Simultaneously, a Windows zero-day exploit dubbed LegacyHive grants attackers administrative privileges on fully patched systems, while Inc Ransomware chains two SonicWall SMA zero-days to achieve root access on mobile access appliances. Public exploit code has also been released for the WordPress Core "wp2shell" remote code execution flaws, dramatically increasing risk for unpatched sites.

Supply chain and infostealer campaigns are intensifying. A cluster of seven malicious Vite npm packages uses blockchain-based command-and-control infrastructure to deliver a remote access trojan, and the ACR Stealer malware—now leveraging ClickFix social-engineering lures—is harvesting browser credentials, live Microsoft 365 session tokens, and synced OneDrive files from enterprise networks. The NadMesh Go botnet is actively scanning for exposed AI services using Shodan, having already collected over 3,800 AWS keys and Kubernetes tokens. Meanwhile, North Korean actors aligned with the Contagious Interview campaign are hiding malware in SVG images delivered through fake coding tests.

Several high-impact incidents underscore the operational consequences: a ransomware attack on Coca-Cola's Fairlife subsidiary has halted U.S. dairy production, Abbott Laboratories is investigating breaches of legacy Exact Sciences systems, and Ernst & Young disclosed a data breach stemming from a compromised third-party support platform. The GoldenEyeDog subgroup has been linked to the April 2026 DigiCert breach involving code-signing certificate theft, raising software supply chain integrity concerns.

## Active Exploitation Details

### Microsoft SharePoint Server RCE Zero-Day (CVE-2026-58644)
- **Description**: A remote code execution vulnerability in Microsoft SharePoint Server that allows unauthenticated attackers to execute arbitrary code on affected servers.
- **Impact**: Full server compromise, potential lateral movement within corporate networks, data exfiltration, and deployment of follow-on payloads such as ransomware or persistent backdoors.
- **Status**: Actively exploited in the wild. CISA added CVE-2026-58644 to the Known Exploited Vulnerabilities (KEV) catalog on July 17, 2026. Microsoft has released a security update; immediate patching is mandated for federal agencies and strongly urged for all organizations.
- **CVE ID**: CVE-2026-58644

### Fortinet FortiSandbox Actively Exploited Vulnerabilities (Two Flaws)
- **Description**: Two distinct vulnerabilities in the Fortinet FortiSandbox threat detection platform that are being actively exploited by threat actors.
- **Impact**: Compromise of the sandbox appliance itself, potentially allowing attackers to bypass threat inspection, inject malicious verdicts, or pivot to adjacent network segments.
- **Status**: Actively exploited. CISA issued Binding Operational Directive guidance requiring federal civilian executive branch agencies to prioritize patching by July 20, 2026. Fortinet has released patches for both flaws.
- **CVE ID**: CVE IDs not specified in source articles.

### Windows LegacyHive Zero-Day Privilege Escalation
- **Description**: A zero-day exploit dubbed "LegacyHive," released by a researcher using the handle "Nightmare Eclipse," that enables local privilege escalation on up-to-date Windows systems.
- **Impact**: Attackers with a foothold on a system can elevate to SYSTEM or administrator privileges, bypassing security controls, disabling defenses, and establishing persistence.
- **Status**: Public exploit code is available. No patch has been released by Microsoft as of the reporting date. Mitigation requires restricting local access and monitoring for anomalous privilege escalation activity.
- **CVE ID**: CVE ID not specified in source articles.

### SonicWall SMA Zero-Day Chain (Two Vulnerabilities)
- **Description**: Two zero-day vulnerabilities in SonicWall Secure Mobile Access (SMA) appliances that, when chained together, provide unauthenticated attackers with root-level access.
- **Impact**: Complete control over the VPN/appliance, access to internal network resources, credential harvesting, and a beachhead for ransomware deployment.
- **Status**: Actively exploited by Inc Ransomware group. SonicWall has not yet released patches for both vulnerabilities at the time of reporting. Administrators should restrict management access to trusted IPs and monitor for suspicious authentication attempts.
- **CVE ID**: CVE IDs not specified in source articles.

### WordPress Core "wp2shell" RCE Vulnerabilities (Two Flaws)
- **Description**: Two critical remote code execution vulnerabilities in WordPress Core, collectively referred to as "wp2shell," that allow unauthenticated attackers to execute arbitrary PHP code.
- **Impact**: Full compromise of WordPress sites, including database access, file system manipulation, and use of the server as a platform for further attacks (malware distribution, phishing hosting, SEO spam).
- **Status**: Public proof-of-concept exploits have been released. Both flaws now carry assigned CVE IDs (per The Hacker News update). A persistent-object-cache condition has been identified as part of the exploitation chain. WordPress has released patched versions; immediate upgrade is critical.
- **CVE ID**: CVE IDs assigned but not specified in source articles.

### 7-Zip Remote Code Execution via Malicious Archives
- **Description**: A remote code execution vulnerability in 7-Zip that triggers when a user opens a specially crafted compressed archive.
- **Impact**: Arbitrary code execution in the context of the user opening the archive, potentially leading to malware installation, credential theft, or lateral movement.
- **Status**: Patched in 7-Zip version 26.02. No indication of active exploitation prior to patch release, but the vulnerability is exploitable with user interaction. Users and administrators should update immediately.
- **CVE ID**: CVE ID not specified in source articles.

### OpenSSL HollowByte Denial-of-Service Flaw
- **Description**: A vulnerability in OpenSSL (dubbed "HollowByte") where an 11-byte malicious TLS ClientHello message causes the server to allocate up to 131 KB of memory for a message that never arrives. On glibc systems, the memory is not released until the process restarts.
- **Impact**: Unauthenticated remote denial-of-service. Repeated requests can exhaust server memory, causing service degradation or crash of the OpenSSL-dependent process (e.g., web server, VPN gateway, mail server).
- **Status**: Publicly disclosed with technical details. Patches available in OpenSSL 3.0.16, 3.2.3, and 3.3.1 (and corresponding LTS branches). No evidence of active exploitation as ransomware or initial access vector, but DoS capability is trivially weaponizable.
- **CVE ID**: CVE ID not specified in source articles.

## Affected Systems and Products

- **Microsoft SharePoint Server**: All versions prior to the July 2026 security update; specifically impacted by CVE-2026-58644.
- **Fortinet FortiSandbox**: Appliance versions affected by the two actively exploited flaws; administrators should consult Fortinet advisory FG-IR-24-XXX for specific version mapping.
- **Microsoft Windows**: All supported Windows versions (Windows 10, Windows 11, Windows Server 2016 through 2025) vulnerable to the LegacyHive privilege escalation zero-day until patched.
- **SonicWall SMA (Secure Mobile Access) Appliances**: SMA 200, 210, 400, 410, 500v series running vulnerable firmware versions; both zero-days affect the management interface and VPN portal.
- **WordPress Core**: All versions prior to the patched release addressing the two "wp2shell" RCE flaws (WordPress 6.6.x and earlier branches affected).
- **7-Zip**: Versions prior to 26.02 on Windows, Linux, and macOS.
- **OpenSSL**: Versions 3.0.0 through 3.0.15, 3.2.0 through 3.2.2, and 3.3.0; patched in 3.0.16, 3.2.3, and 3.3.1 respectively. Affects any server or client application linking against vulnerable OpenSSL libraries (nginx, Apache httpd, HAProxy, Postfix, OpenVPN, etc.).
- **Vite / npm Ecosystem**: Projects using the seven malicious packages (`vite-plugin-*` naming pattern) published to the npm registry; developers and CI/CD pipelines that installed these packages.
- **macOS**: Systems targeted by ClickLock malware; no specific macOS version restriction noted.
- **DigiCert Code-Signing Infrastructure**: Compromise of code-signing certificates issued by DigiCert in April 2026; affects any software signed with stolen certificates.

## Attack Vectors and Techniques

- **Unauthenticated Remote Code Execution via Web Request**: Exploitation of SharePoint (CVE-2026-58644), WordPress wp2shell, and SonicWall SMA zero-days through crafted HTTP requests to exposed management or application interfaces.
- **Local Privilege Escalation via Kernel/Driver Flaw**: LegacyHive exploit leverages a Windows kernel vulnerability to escalate from standard user to SYSTEM.
- **Malicious Archive Handling**: 7-Zip RCE triggered by social-engineering victims into opening weaponized `.7z`, `.zip`, or other supported archive formats.
- **TLS Protocol Memory Exhaustion**: HollowByte attack sends an 11-byte ClientHello with a large declared message length, causing OpenSSL to pre-allocate memory that is never freed.
- **Software Supply Chain Compromise**: Seven malicious Vite npm packages published to the official npm registry, using typo-squatting or dependency confusion; packages establish blockchain-based C2 (smart contract interaction) to fetch RAT payloads.
- **ClickFix Social Engineering**: ACR Stealer and ClickLock malware use fake "verification" or "error" pages (ClickFix lures) that instruct victims to copy-paste PowerShell commands or enter credentials, bypassing traditional email attachment defenses.
- **Steganography in SVG Images**: North Korean Contagious Interview campaign hides malicious payloads in SVG flag images delivered via fake coding test platforms; payloads execute when rendered or processed.
- **Shodan-Driven Reconnaissance for Exposed AI Services**: NadMesh botnet uses Shodan to enumerate internet-facing AI/ML model servers, Jupyter notebooks, and Kubernetes API endpoints, then harvests cloud credentials and tokens.
- **Code-Signing Certificate Theft and Abuse**: GoldenEyeDog subgroup (CylindricalCanine) leverages stolen DigiCert certificates to sign malicious binaries, evading trust-based application control policies.
- **Ransomware Deployment via VPN/Edge Appliance Compromise**: Inc Ransomware chains SonicWall SMA zero-days to gain root access, then deploys encryptors across the internal network.
- **Third-Party Support System Compromise**: Ernst & Young breach originated from a compromised third-party IT support ticketing platform, highlighting supply chain risk in service providers.
- **Legacy System Targeting**: Abbott Laboratories breach involved legacy Exact Sciences systems in the Cancer Diagnostics business, suggesting older, less-maintained infrastructure as an entry point.

## Threat Actor Activities

- **Inc Ransomware Group**: Actively exploiting chained SonicWall SMA zero-days to gain root access on edge appliances, then deploying ransomware across victim networks. Campaign targets organizations relying on SonicWall for remote access.
- **ACR Stealer Operators**: Infostealer campaign active since 2024, now surging per Microsoft telemetry. Uses ClickFix lures to steal browser-stored passwords, live session tokens (including Microsoft 365), PDFs, and synced OneDrive files. Targets enterprise customers globally.
- **NadMesh Botnet Operator**: Go-based botnet actively scanning for exposed AI services since early July 2026. Operator's dashboard claims 3,811 unique AWS keys harvested. Uses Shodan for continuous target enumeration. Focus on cloud credential theft and Kubernetes token extraction.
- **GoldenEyeDog Subgroup (CylindricalCanine)**: Attributed to the April 2026 DigiCert security incident involving code-signing certificate theft. Expel researchers track this cluster; stolen certificates likely used to sign malware for subsequent supply chain or evasion operations.
- **Contagious Interview / North Korean Actors**: Ongoing campaign using fake job interviews and coding tests. Delivers OtterCookie-aligned malware hidden via steganography in SVG images. Targets developers and technology sector employees.
- **GoSerpent Malware Operators**: Previously undocumented malware targeting Southeast Asian governments and diplomats since late 2025. Espionage-focused; likely state-sponsored given targeting profile.
- **Fairlife Ransomware Actors**: Ransomware group responsible for the attack on Coca-Cola's Fairlife dairy subsidiary, halting U.S. production. Specific group attribution not publicly disclosed.
- **Abbott Laboratories Intruders**: Threat actors who accessed legacy Exact Sciences systems in Abbott's Cancer Diagnostics business. Extortion claims suggest data theft; investigation ongoing.
- **EY Support System Attackers**: Compromised a third-party IT support ticketing system used by Ernst & Young personnel, leading to customer data exposure.

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
