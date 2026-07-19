# Exploitation Report

## Executive Summary

Critical exploitation activity is accelerating across multiple vectors this week. CISA has added an actively exploited SharePoint Server RCE zero-day (CVE-2026-58644) to its Known Exploited Vulnerabilities catalog, mandating immediate federal patching. Simultaneously, public proof-of-concept exploits have been released for the "wp2shell" remote code execution vulnerabilities in WordPress Core, now assigned CVE identifiers, putting millions of unpatched sites at imminent risk. A Windows zero-day dubbed LegacyHive has been publicly released, granting attackers SYSTEM-level privileges on fully patched systems, while the Inc ransomware group is actively chaining two SonicWall SMA zero-days to achieve root access on mobile access appliances.

Supply chain and infostealer campaigns are intensifying in parallel. Seven malicious npm packages targeting the Vite ecosystem have been discovered using blockchain-based command-and-control to deliver a remote access trojan. The ACR Stealer malware—now leveraging ClickFix social engineering lures—is surging across enterprise environments, exfiltrating browser credentials, Microsoft 365 session tokens, and sensitive documents. North Korean operators behind the Contagious Interview campaign are deploying steganographic payloads hidden in SVG flag images during fake coding interviews, while a new GoSerpent malware family conducts espionage against Southeast Asian governments. The NadMesh botnet has compromised over 3,800 AWS credential sets by scanning for exposed AI services.

## Active Exploitation Details

### 7-Zip Remote Code Execution Vulnerability
- **Description**: A remote code execution flaw in 7-Zip allows attackers to execute arbitrary code when users open specially crafted malicious archive files. The vulnerability resides in the archive parsing logic and can be triggered without user interaction beyond opening the file.
- **Impact**: Attackers can achieve full remote code execution on the victim's system with the privileges of the user opening the archive, potentially leading to malware installation, data theft, and lateral movement.
- **Status**: 7-Zip version 26.02 has been released to address this vulnerability. Users should update immediately as exploitation requires only convincing a user to open a malicious archive.

### WordPress Core "wp2shell" Remote Code Execution Vulnerabilities
- **Description**: Two critical remote code execution vulnerabilities in WordPress Core, collectively dubbed "wp2shell," allow unauthenticated attackers to execute arbitrary PHP code on vulnerable installations. The full exploitation mechanism has been published and a working proof-of-concept is publicly available.
- **Impact**: Unauthenticated attackers can achieve complete compromise of WordPress sites, including arbitrary code execution, database access, and persistence mechanism installation. Millions of WordPress installations are potentially affected.
- **Status**: Public exploits are now available. Both flaws have been assigned CVE identifiers. WordPress administrators must apply patches immediately.
- **CVE ID**: CVE identifiers assigned (specific IDs not disclosed in source)

### OpenSSL HollowByte Denial-of-Service Vulnerability
- **Description**: The HollowByte flaw allows unauthenticated attackers to trigger a denial-of-service condition on OpenSSL servers by sending a malicious TLS ClientHello message of just 11 bytes. This causes the server to allocate up to 131 KB of memory for a message that never arrives, with the memory remaining allocated until the process restarts on glibc systems.
- **Impact**: Attackers can exhaust server memory resources, causing service degradation or complete denial of service. The attack is highly efficient—minimal bandwidth produces disproportionate resource consumption.
- **Status**: Vulnerability publicly disclosed with technical details. Patches should be applied from OpenSSL or distribution vendors.
- **CVE ID**: Not specified in source articles

### Windows LegacyHive Privilege Escalation Zero-Day
- **Description**: A security researcher ("Nightmare Eclipse") has publicly released a Windows zero-day exploit dubbed LegacyHive that enables privilege escalation to SYSTEM on up-to-date Windows systems. The exploit targets a legacy registry hive handling mechanism.
- **Impact**: Local attackers can elevate privileges from standard user to SYSTEM, achieving full administrative control over the affected system. This enables bypassing security controls, disabling EDR, and installing persistent implants.
- **Status**: Exploit code is publicly available. No patch available at time of reporting—this is an active zero-day.
- **CVE ID**: Not assigned (zero-day)

### SonicWall SMA Zero-Day Chain
- **Description**: Two zero-day vulnerabilities in SonicWall Secure Mobile Access (SMA) appliances can be chained together to achieve root-level remote code execution without authentication. The Inc ransomware group is actively exploiting this chain in the wild.
- **Impact**: Attackers gain root access on SonicWall SMA appliances, providing a foothold for network penetration, credential harvesting, VPN session hijacking, and ransomware deployment across the organization.
- **Status**: Actively exploited by Inc ransomware. No patches mentioned in source articles.
- **CVE ID**: Not specified in source articles

### Fortinet FortiSandbox Actively Exploited Vulnerabilities
- **Description**: Two vulnerabilities in the Fortinet FortiSandbox threat detection platform are being actively exploited in the wild. CISA has ordered federal agencies to prioritize patching.
- **Impact**: Exploitation of these sandbox analysis platform flaws could allow attackers to bypass threat detection, execute code in the analysis environment, and potentially pivot to the management plane.
- **Status**: CISA has mandated immediate patching for federal agencies (BOD 22-01). Patches available from Fortinet.
- **CVE ID**: Not specified in source articles

### Microsoft SharePoint Server RCE Zero-Day
- **Description**: A remote code execution zero-day vulnerability in Microsoft SharePoint Server has been added to CISA's Known Exploited Vulnerabilities catalog, confirming active exploitation in the wild.
- **Impact**: Authenticated attackers can execute arbitrary code on SharePoint servers, potentially leading to full server compromise, data exfiltration, and lateral movement within the corporate network.
- **Status**: Actively exploited. CISA KEV addition mandates federal patching by specified deadline. Microsoft has released patches.
- **CVE ID**: CVE-2026-58644

## Affected Systems and Products

- **7-Zip**: Versions prior to 26.02 on Windows, Linux, and macOS platforms
- **WordPress Core**: All unpatched versions affected by the wp2shell vulnerabilities; specific version ranges not detailed in sources
- **OpenSSL**: Unpatched versions vulnerable to HollowByte DoS; affects servers using OpenSSL for TLS termination on glibc-based Linux distributions
- **Microsoft Windows**: All supported Windows versions vulnerable to LegacyHive privilege escalation zero-day; exploit confirmed working on up-to-date systems
- **SonicWall SMA Appliances**: Secure Mobile Access 100, 200, 400, 500, and 1000 series appliances; specific firmware versions not detailed
- **Fortinet FortiSandbox**: FortiSandbox threat detection platform; specific versions not detailed in sources
- **Microsoft SharePoint Server**: On-premises SharePoint Server versions affected by CVE-2026-58644; SharePoint Online not affected
- **Vite/npm Ecosystem**: Developers and CI/CD pipelines using compromised npm packages: `vite-plugin-*` variants (seven packages total)
- **macOS**: Systems targeted by ClickLock information-stealing malware
- **AI/ML Services**: Exposed AI inference endpoints, model serving platforms, and Kubernetes clusters scanned by NadMesh botnet

## Attack Vectors and Techniques

- **Malicious Archive Handling**: Crafted 7-Zip archives exploiting parsing vulnerabilities to achieve RCE upon opening; delivered via phishing emails, compromised downloads, or supply chain
- **Unauthenticated Web RCE**: Direct HTTP requests to vulnerable WordPress endpoints exploiting wp2shell flaws; no authentication required, enabling mass exploitation via automated scanning
- **TLS Protocol Abuse**: 11-byte malicious ClientHello messages sent to OpenSSL servers triggering unbounded memory allocation; requires only network access to TLS port
- **Legacy Registry Hive Manipulation**: LegacyHive exploit abuses Windows' handling of legacy registry hive files to corrupt kernel structures and elevate to SYSTEM
- **Appliance Chaining**: Two distinct SonicWall SMA vulnerabilities chained—initial access followed by privilege escalation to root—enabling full appliance compromise
- **Blockchain C2**: Malicious npm packages use blockchain transactions (smart contract interactions) for command-and-control communication, evading traditional network detection
- **ClickFix Social Engineering**: Fake CAPTCHA/verification pages trick users into executing PowerShell commands that deploy ACR Stealer; leverages clipboard manipulation and "Run" dialog execution
- **Steganographic Payload Delivery**: Malicious code hidden in SVG flag images using steganography; extracted and executed during fake coding interview scenarios
- **AI Service Enumeration**: Shodan-based scanning for exposed AI/ML endpoints, Jupyter notebooks, MLflow servers, and Kubernetes API servers to harvest cloud credentials
- **Code-Signing Certificate Theft**: Compromise of DigiCert infrastructure to steal valid code-signing certificates for signing malicious binaries (GoldenEyeDog/CylindricalCanine)
- **Third-Party Support System Compromise**: Supply chain attack via compromised IT support ticketing system leading to data breach at Ernst & Young
- **Ransomware via Appliance Exploitation**: Inc ransomware using SonicWall SMA zero-day chain as initial access vector for enterprise encryption campaigns

## Threat Actor Activities

- **Inc Ransomware Group**: Actively exploiting chained SonicWall SMA zero-days to gain root access on SSL VPN appliances; using access for ransomware deployment across victim networks
- **ACR Stealer Operators**: Conducting surge campaigns against enterprise customers using ClickFix social engineering lures; exfiltrating browser-stored passwords, live session tokens, Microsoft 365 documents, PDFs, and OneDrive-synced files
- **Contagious Interview Campaign (North Korea-linked)**: Deploying OtterCookie-aligned malware via fake coding tests; using SVG steganography to hide payloads in flag images; targeting developers and job seekers in technology sector
- **NadMesh Botnet Operators**: Running Go-based botnet scanning for exposed AI services via Shodan; harvesting AWS keys (3,811 unique keys claimed), Kubernetes tokens, and cloud credentials; maintaining persistent scan infrastructure
- **GoldenEyeDog / CylindricalCanine**: Attributed to April 2026 DigiCert breach and code-signing certificate theft; certificates used to sign malicious binaries for defense evasion
- **GoSerpent Operators**: Previously undocumented malware family targeting Southeast Asian government entities and diplomats since late 2025; focused on cyber espionage and intelligence collection
- **ClickLock Developers**: New macOS information-stealer that terminates visible processes to force users into entering system login passwords; captures credentials for further compromise
- **Fairlife Ransomware Actors**: Ransomware attack on Coca-Cola's Fairlife dairy subsidiary halting US production operations; impact on critical food supply chain infrastructure

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
