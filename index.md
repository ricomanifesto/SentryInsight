# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are being actively exploited across diverse platforms, ranging from widely deployed enterprise software to developer tooling and cloud infrastructure. CISA has added a Microsoft SharePoint Server RCE zero-day (CVE-2026-58644) to its Known Exploited Vulnerabilities catalog, mandating immediate federal patching, while also ordering urgent remediation of two actively exploited Fortinet FortiSandbox flaws. Simultaneously, a Windows zero-day dubbed LegacyHive grants attackers admin privileges on fully patched systems, and two chained SonicWall SMA zero-days are being leveraged by Inc Ransomware for root-level appliance compromise.

Supply chain and identity-focused attacks are escalating. Seven malicious npm packages targeting the Vite ecosystem use blockchain-based command-and-control to deliver a remote access trojan, while the NadMesh Go botnet systematically harvests AWS keys and Kubernetes tokens from exposed AI services—claiming over 3,800 unique AWS credentials. North Korean actors tied to the Contagious Interview campaign employ SVG steganography in fake coding tests to deliver OtterCookie-aligned malware, and the ACR Stealer infostealer surge leverages ClickFix social engineering to exfiltrate browser tokens, Microsoft 365 documents, and OneDrive files from enterprise environments.

## Active Exploitation Details

### 7-Zip Remote Code Execution Vulnerability
- **Description**: A remote code execution flaw in 7-Zip allows attackers to execute arbitrary code by convincing users to open specially crafted malicious compressed archives. The vulnerability is triggered upon archive interaction.
- **Impact**: Attackers achieve full code execution in the context of the user opening the archive, potentially leading to system compromise, data theft, and lateral movement.
- **Status**: Actively exploitable; patched in 7-Zip version 26.02. Users and administrators should update immediately.

### WordPress Core "wp2shell" RCE Vulnerabilities
- **Description**: Two critical remote code execution vulnerabilities in WordPress Core, collectively dubbed "wp2shell," allow unauthenticated attackers to execute arbitrary code. A persistent-object-cache condition has been identified as part of the attack surface, and a working proof-of-concept exploit is publicly available.
- **Impact**: Unauthenticated remote code execution on WordPress sites, enabling full site takeover, data exfiltration, and use as a pivot for further attacks.
- **Status**: Public exploits released; patching is imperative. Both flaws have been assigned CVE identifiers.
- **CVE ID**: CVE IDs assigned (specific identifiers not provided in source articles)

### OpenSSL HollowByte Denial-of-Service Vulnerability
- **Description**: The HollowByte flaw allows unauthenticated attackers to send an 11-byte malicious TLS ClientHello message that causes unpatched OpenSSL servers to allocate up to 131 KB of memory for a message that never arrives. On glibc systems, this memory remains unreleased until the process restarts.
- **Impact**: Denial-of-service through memory exhaustion; repeated requests can freeze or crash OpenSSL-dependent services.
- **Status**: Actively exploitable DoS vector; patches or mitigations should be applied to OpenSSL deployments.

### SonicWall SMA Zero-Day Chain
- **Description**: Two zero-day vulnerabilities in SonicWall Secure Mobile Access (SMA) appliances can be chained together to achieve root-level access. Inc Ransomware operators are actively exploiting this chain in the wild.
- **Impact**: Full root compromise of SonicWall SMA mobile access appliances, enabling network persistence, traffic interception, and lateral movement into connected networks.
- **Status**: Actively exploited by Inc Ransomware; zero-day status indicates no vendor patch available at time of reporting.

### Windows LegacyHive Privilege Escalation Zero-Day
- **Description**: A Windows zero-day exploit dubbed LegacyHive, released by researcher "Nightmare Eclipse," enables local privilege escalation to administrator on up-to-date Windows systems.
- **Impact**: Attackers with low-privileged access can elevate to SYSTEM or administrator, bypassing security controls and enabling full system compromise.
- **Status**: Public exploit code released; zero-day with no patch available at time of reporting.

### Fortinet FortiSandbox Actively Exploited Vulnerabilities
- **Description**: Two vulnerabilities in the Fortinet FortiSandbox threat detection platform are being actively exploited in the wild. CISA has ordered federal civilian executive branch agencies to prioritize patching.
- **Impact**: Compromise of the sandbox analysis platform, potentially allowing malware evasion, configuration tampering, and lateral movement.
- **Status**: Actively exploited; CISA-mandated urgent patching for federal agencies. Patches presumed available from Fortinet.

### Microsoft SharePoint Server RCE Zero-Day
- **Description**: A remote code execution zero-day vulnerability in Microsoft SharePoint Server has been added to CISA's Known Exploited Vulnerabilities catalog, confirming active exploitation in the wild.
- **Impact**: Unauthenticated or authenticated remote code execution on SharePoint servers, leading to data breach, credential theft, and domain compromise.
- **Status**: Actively exploited; emergency patching required. CVE-2026-58644 added to KEV on July 2026.
- **CVE ID**: CVE-2026-58644

## Affected Systems and Products

- **7-Zip**: Versions prior to 26.02 on Windows, Linux, and macOS platforms
- **WordPress Core**: All unpatched versions affected by the wp2shell RCE flaws; specific version range not disclosed in sources
- **OpenSSL**: Server deployments using vulnerable OpenSSL versions on glibc-based Linux systems; client implementations unaffected
- **SonicWall SMA (Secure Mobile Access)**: Mobile access appliance firmware versions vulnerable to the chained zero-days; specific firmware versions not disclosed
- **Microsoft Windows**: Up-to-date Windows systems vulnerable to LegacyHive privilege escalation; all supported versions potentially affected
- **Fortinet FortiSandbox**: FortiSandbox appliances running vulnerable firmware; specific versions not disclosed in sources
- **Microsoft SharePoint Server**: On-premises SharePoint Server installations vulnerable to CVE-2026-58644; SharePoint Online unaffected per typical KEV context
- **Vite/npm Ecosystem**: Developers and CI/CD pipelines using the Vite frontend tooling; seven specific malicious packages identified (names not listed in sources)
- **Exposed AI/Cloud Services**: Publicly accessible AI inference endpoints, Kubernetes API servers, and cloud metadata services scanned via Shodan
- **macOS**: Systems targeted by ClickLock malware; specific macOS versions not disclosed
- **DigiCert Infrastructure**: Code-signing certificate issuance systems compromised in April 2026 incident

## Attack Vectors and Techniques

- **Malicious Archive Delivery**: Attackers distribute specially crafted 7-Zip archives via email, web download, or file sharing; exploitation triggers upon user interaction (opening/extracting).
- **Unauthenticated WordPress RCE**: Exploitation of wp2shell flaws requires no authentication; attackers send crafted HTTP requests to vulnerable endpoints, leveraging persistent object cache manipulation.
- **ClickFix Social Engineering**: ACR Stealer operators use fake "ClickFix" verification pages or error messages that trick users into copying and executing malicious PowerShell commands, leading to infostealer deployment.
- **TLS ClientHello Memory Exhaustion**: HollowByte attackers send an 11-byte TLS ClientHello fragment that induces unbounded memory allocation in OpenSSL's record layer; no handshake completion required.
- **Chained Appliance Zero-Days**: Inc Ransomware chains two distinct SonicWall SMA vulnerabilities—likely an authentication bypass followed by command injection—to escalate from unauthenticated access to root shell.
- **Blockchain-Based C2**: Malicious Vite npm packages embed command-and-control logic within blockchain transactions (e.g., smart contract interactions or memo fields), evading traditional network detection.
- **Shodan-Driven Reconnaissance**: NadMesh botnet operators use automated Shodan queries to maintain a live queue of exposed AI services, cloud metadata endpoints, and Kubernetes control planes for credential harvesting.
- **SVG Steganography Payload Delivery**: North Korean Contagious Interview campaign embeds malicious code within SVG image files (e.g., flag graphics) delivered via fake coding test platforms; payload extracts and executes via steganographic decoding.
- **LegacyHive Local Privilege Escalation**: Local attacker executes the LegacyHive exploit binary/tool on a compromised Windows host, leveraging a kernel or driver flaw to escalate to SYSTEM.
- **Third-Party Support System Compromise**: Attackers breach vendor ticketing/support platforms (e.g., Exact Sciences legacy systems at Abbott, EY's third-party support system) to pivot into target organizations.
- **Ransomware Deployment via Appliance/Edge Compromise**: Inc Ransomware uses SonicWall SMA root access as initial access vector; Fairlife ransomware disrupts OT/production environments via unspecified initial access.

## Threat Actor Activities

- **Inc Ransomware**: Actively exploiting chained SonicWall SMA zero-days to gain root access on edge appliances, facilitating ransomware deployment across victim networks.
- **ACR Stealer Operators**: Conducting large-scale infostealer campaigns against enterprise customers since 2024; recently surging via ClickFix lures to harvest browser credentials, session tokens, Microsoft 365 documents, PDFs, and OneDrive-synced files.
- **NadMesh Botnet Operators**: Running a Go-based botnet since early July 2026 that scans for exposed AI services using Shodan; dashboard claims 3,811 unique AWS keys harvested alongside Kubernetes tokens and cloud credentials.
- **GoldenEyeDog Subgroup / CylindricalCanine**: Attributed to the April 2026 DigiCert security incident involving code-signing certificate theft; described as a threat activity cluster by Expel researchers.
- **North Korean Contagious Interview Campaign**: Linked to Lazarus/APT38-adjacent activity; uses fake job interviews and coding tests on developer platforms to deliver OtterCookie-aligned malware via SVG steganography.
- **GoSerpent Operators**: Deploying previously undocumented GoSerpent malware since late 2025 against Southeast Asian government entities and diplomats for espionage; Go-based tooling suggests custom development.
- **Nightmare Eclipse**: Independent security researcher who publicly released the LegacyHive Windows zero-day exploit code; motivation appears to be disclosure/research rather than malicious operation.
- **Fairlife Ransomware Attackers**: Unidentified ransomware group that compromised Coca-Cola's Fairlife dairy subsidiary, halting U.S. production operations; attribution not disclosed.
- **REvil Affiliates**: Referenced in context of U.S. extradition request for alleged REvil ransomware suspect Aleksandr Ermakov; indicates ongoing law enforcement pursuit of ransomware ecosystem actors.

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
