# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse platforms, ranging from widely deployed archiving utilities and content management systems to enterprise security appliances and cloud infrastructure. The most severe activity centers on a Windows zero-day privilege escalation exploit (LegacyHive) released publicly by a researcher, a chain of SonicWall SMA zero-days leveraged by Inc Ransomware for root access, and two actively exploited Fortinet FortiSandbox flaws that prompted a CISA emergency directive for federal agencies. Simultaneously, public proof-of-concept exploits for WordPress Core "wp2shell" RCE vulnerabilities have emerged, creating urgent patching pressure for millions of websites.

Threat actor operations show increased sophistication in initial access and credential theft. The ACR Stealer infostealer campaign has surged against enterprise targets using ClickFix social engineering lures to harvest browser credentials, Microsoft 365 session tokens, and OneDrive files. North Korean actors continue the Contagious Interview campaign, embedding OtterCookie-aligned malware in SVG steganography within fake coding tests. A new Go-based botnet, NadMesh, is actively scanning for exposed AI services to harvest AWS keys and Kubernetes tokens, claiming over 3,800 compromised credentials. On the ransomware front, Inc Ransomware's exploitation of chained SonicWall zero-days and a disruptive attack on Coca-Cola's Fairlife subsidiary demonstrate ongoing operational impact.

Supply chain and infrastructure risks are escalating. Seven malicious npm packages targeting the Vite ecosystem were discovered using blockchain-based command-and-control to deliver a remote access trojan. The DigiCert code-signing certificate theft attributed to the GoldenEyeDog subgroup (CylindricalCanine cluster) raises long-term trust concerns for software supply chains. Additionally, the OpenSSL "HollowByte" flaw enables trivial denial-of-service via 11-byte TLS requests that permanently bloat server memory until process restart.

## Active Exploitation Details

### Windows LegacyHive Zero-Day Privilege Escalation
- **Description**: A Windows zero-day exploit dubbed "LegacyHive" released by security researcher "Nightmare Eclipse" allows attackers to escalate privileges to administrator on fully patched Windows systems. The exploit targets a legacy component in the Windows registry hive handling.
- **Impact**: Attackers gain SYSTEM-level privileges from a standard user context, enabling full system compromise, persistence installation, security tool disabling, and lateral movement.
- **Status**: Zero-day with public exploit code released; no patch available at time of reporting. Microsoft has not yet issued a security update.
- **CVE ID**: Not assigned in available reporting.

### SonicWall SMA Zero-Day Chain (Inc Ransomware)
- **Description**: Two zero-day vulnerabilities in SonicWall Secure Mobile Access (SMA) appliances that, when chained together, provide unauthenticated root-level access to the appliance. Inc Ransomware operators are actively exploiting this chain in the wild.
- **Impact**: Full administrative control over VPN/appliance infrastructure, enabling network pivoting, credential harvesting, persistence, and ransomware deployment across the victim organization.
- **Status**: Actively exploited by Inc Ransomware; zero-day status indicates no vendor patch available at time of exploitation onset. SonicWall advisory and mitigation status should be monitored urgently.
- **CVE ID**: Not assigned in available reporting.

### Fortinet FortiSandbox Actively Exploited Vulnerabilities (CISA KEV)
- **Description**: Two vulnerabilities in the Fortinet FortiSandbox threat detection platform that are confirmed as actively exploited in the wild. CISA has issued an emergency directive ordering federal civilian executive branch agencies to patch by a specified deadline.
- **Impact**: Compromise of the sandbox analysis platform could allow attackers to evade detection, manipulate threat intelligence feeds, and pivot into connected security infrastructure.
- **Status**: Actively exploited; CISA Binding Operational Directive mandates immediate patching. Fortinet patches are available.
- **CVE ID**: Specific CVE IDs not provided in the source article snippet.

### Microsoft SharePoint Server RCE Zero-Day (CVE-2026-58644)
- **Description**: A remote code execution zero-day vulnerability in Microsoft SharePoint Server added to CISA's Known Exploited Vulnerabilities (KEV) catalog, confirming active exploitation in the wild.
- **Impact**: Unauthenticated or authenticated remote code execution on SharePoint servers, leading to full server compromise, data exfiltration, and potential domain escalation via SharePoint service accounts.
- **Status**: Actively exploited; patched by Microsoft; CISA KEV listing mandates federal agency remediation. Organizations should apply July 2026 Patch Tuesday updates immediately.
- **CVE ID**: CVE-2026-58644

### WordPress Core "wp2shell" RCE Vulnerabilities
- **Description**: Critical remote code execution vulnerabilities in WordPress Core collectively dubbed "wp2shell." Public proof-of-concept exploits have been released, and the full exploitation mechanism has been published. A persistent-object-cache condition has been identified as part of the attack chain. Unauthenticated attackers can achieve code execution.
- **Impact**: Complete takeover of WordPress sites, including database access, credential theft, malware distribution to visitors, and use as a platform for further attacks.
- **Status**: Public exploits available; active exploitation highly likely. WordPress has released security updates. The vulnerabilities now carry CVE identifiers (specific IDs not listed in source snippets).
- **CVE ID**: CVE IDs assigned per The Hacker News update but not specified in provided text.

### 7-Zip Remote Code Execution via Malicious Archives
- **Description**: A remote code execution vulnerability in 7-Zip triggered by opening specially crafted compressed archives. The flaw resides in archive parsing logic and allows code execution in the context of the user opening the file.
- **Impact**: Arbitrary code execution on the victim's machine when a malicious archive is opened, leading to malware installation, data theft, and further compromise.
- **Status**: Patched in 7-Zip version 26.02. Users must update immediately. No indication of exploitation prior to patch release, but public disclosure increases risk.
- **CVE ID**: Not provided in source article.

### OpenSSL "HollowByte" Denial-of-Service
- **Description**: A vulnerability in OpenSSL where an 11-byte malicious TLS ClientHello message causes the server to allocate up to 131 KB of memory for an expected message that never arrives. On glibc systems, this memory is not released until the process restarts, enabling efficient memory exhaustion DoS.
- **Impact**: Unauthenticated remote denial-of-service affecting OpenSSL-based TLS servers (web servers, VPNs, mail servers, etc.). Repeated requests can exhaust server memory, causing service outage.
- **Status**: Vulnerability disclosed; patches or mitigations expected from OpenSSL project and downstream distributors. Exploitation is trivial (11-byte payload).
- **CVE ID**: Not provided in source articles.

### NadMesh Botnet Targeting Exposed AI Services
- **Description**: A Go-based botnet (NadMesh) actively scanning for and compromising exposed AI/ML services, model endpoints, and associated cloud infrastructure. The operators use Shodan to maintain a scan queue and harvest AWS access keys, Kubernetes tokens, and other cloud credentials.
- **Impact**: Cloud account takeover, cryptojacking, data exfiltration from AI training data and model artifacts, supply chain poisoning of ML pipelines, and lateral movement within cloud environments.
- **Status**: Active campaign observed since early July 2026. Operator dashboard claims 3,811 unique AWS keys harvested. Ongoing scanning and exploitation.
- **CVE ID**: Not applicable; exploits misconfigurations and exposed services rather than specific CVEs.

### ACR Stealer Infostealer Campaign with ClickFix Lures
- **Description**: A surge in ACR Stealer malware deployment targeting enterprise customers. The malware uses ClickFix social engineering lures (fake CAPTCHA/verification prompts) to trick users into executing PowerShell commands that download and execute the stealer.
- **Impact**: Theft of browser-stored passwords, active session tokens (including Microsoft 365/Entra ID), PDF documents, Microsoft 365 files, and OneDrive-synced data. Enables business email compromise, data exfiltration, and lateral movement.
- **Status**: Active surge observed by Microsoft since 2024, with increased velocity in 2026. Ongoing campaign.
- **CVE ID**: Not applicable; relies on social engineering and malware deployment.

### North Korean "Contagious Interview" Campaign with SVG Steganography
- **Description**: North Korean threat actors (linked to the Contagious Interview campaign) delivering OtterCookie-aligned malware through fake coding tests. Malicious payloads are concealed via steganography in SVG image files (flag images) provided as part of the interview challenge.
- **Impact**: Compromise of developer and engineering workstations at target organizations, providing access to source code repositories, build pipelines, SSH keys, and cloud credentials.
- **Status**: Active campaign observed in July 2026. Ongoing targeting of technology sector employees.
- **CVE ID**: Not applicable; social engineering and malware delivery.

### Malicious Vite npm Supply Chain Attack (Blockchain C2)
- **Description**: Seven malicious npm packages targeting the Vite frontend build tooling ecosystem. The packages use blockchain-based command-and-control infrastructure (likely for resilience and anonymity) to deliver a remote access trojan (RAT) to developers' machines and CI/CD pipelines.
- **Impact**: Compromise of developer workstations and build systems, potential injection of malicious code into downstream applications, theft of source code and credentials, persistent access via RAT.
- **Status**: Discovered in July 2026. Packages removed from npm; impact assessment ongoing for organizations that may have installed them.
- **CVE ID**: Not applicable; supply chain malware.

### DigiCert Code-Signing Certificate Theft (GoldenEyeDog / CylindricalCanine)
- **Description**: The April 2026 DigiCert security incident involving theft of code-signing certificates has been attributed to a threat activity cluster dubbed "CylindricalCanine," with a subgroup named "GoldenEyeDog" directly linked to the breach.
- **Impact**: Stolen code-signing certificates enable attackers to sign malicious software with trusted certificates, bypassing application control policies, SmartScreen, and user trust mechanisms. Long-term supply chain risk.
- **Status**: Incident occurred April 2026; attribution published July 2026. DigiCert has revoked affected certificates; however, previously signed malware may remain trusted until certificate revocation propagates fully.
- **CVE ID**: Not applicable; certificate authority breach.

### ClickLock macOS Information Stealer
- **Description**: A new macOS malware dubbed ClickLock that terminates all visible user processes (applications, Finder, Dock) to create a fake system lock screen, forcing the user to enter their system login password, which is then captured.
- **Impact**: Theft of the user's primary login credentials, enabling full device access, keychain unlocking, and potential privilege escalation.
- **Status**: Newly discovered in July 2026. Active distribution vector not fully detailed.
- **CVE ID**: Not applicable; malware.

### Fairlife (Coca-Cola) Ransomware Attack
- **Description**: A ransomware attack on Fairlife, a Coca-Cola subsidiary, that halted dairy production across the United States. The attack disrupted operational technology and manufacturing systems.
- **Impact**: Operational shutdown, supply chain disruption, financial loss, potential data exfiltration. Demonstrates ransomware impact on food/beverage critical infrastructure.
- **Status**: Attack disclosed July 2026; production suspended; incident response ongoing. Ransomware group not publicly named.
- **CVE ID**: Not applicable; ransomware incident.

### GoSerpent Malware Targeting Southeast Asian Governments
- **Description**: A previously undocumented Go-based malware (GoSerpent) used in cyber espionage attacks targeting government and diplomatic entities in Southeast Asia since late 2025.
- **Impact**: Long-term persistent access, credential theft, document exfiltration, intelligence collection on political and diplomatic affairs.
- **Status**: Active campaign since late 2025; discovered and reported July 2026. Attribution not specified in source.
- **CVE ID**: Not applicable; malware/espionage campaign.

### Abbott Laboratories Cyber Incidents (Exact Sciences Legacy Systems)
- **Description**: Abbott Laboratories investigating two separate cybersecurity incidents involving unauthorized access to internal legacy Exact Sciences systems within its Cancer Diagnostics business. Extortion claims have been made.
- **Impact**: Potential exposure of sensitive medical and diagnostic data, business disruption, extortion risk.
- **Status**: Under investigation as of July 2026. Law enforcement engaged.
- **CVE ID**: Not applicable; breach investigation.

### Ernst & Young Data Breach (Third-Party Support System)
- **Description**: EY discloses a data breach resulting from the compromise of a third-party support ticket system used by its IT personnel.
- **Impact**: Exposure of customer and employee data handled through the support system. Third-party risk realization.
- **Status**: Breach disclosed July 2026; notifications underway.
- **CVE ID**: Not applicable; third-party compromise.

## Affected Systems and Products

- **7-Zip**: Versions prior to 26.02 (all platforms: Windows, Linux, macOS)
- **WordPress Core**: All versions prior to the July 2026 security release (specific version numbers not in source)
- **SonicWall Secure Mobile Access (SMA) Appliances**: Specific firmware versions not detailed in source; all unpatched versions likely affected
- **Fortinet FortiSandbox**: Specific versions not detailed in source; CISA directive implies affected versions in federal use
- **Microsoft SharePoint Server**: Versions affected by CVE-2026-58644 (specific versions per Microsoft advisory)
- **OpenSSL**: Versions vulnerable to HollowByte (specific version range not in source; likely broad range of 3.x and possibly 1.1.1)
- **Windows**: All supported versions vulnerable to LegacyHive privilege escalation (up-to-date systems affected)
- **Vite / npm Ecosystem**: Developers and CI/CD systems that installed malicious packages: `vite-plugin-...` (seven package names not listed in source)
- **macOS**: Systems targeted by ClickLock malware (version specifics not in source)
- **AI/ML Model Serving Platforms**: Exposed inference endpoints, Jupyter notebooks, MLflow, Kubeflow, and cloud AI services (AWS SageMaker, Azure ML, GCP Vertex AI) with public network access
- **Enterprise Browsers / Microsoft 365 / OneDrive**: Targets of ACR Stealer credential and token theft
- **Developer Workstations (Windows/macOS/Linux)**: Targets of Contagious Interview SVG steganography and malicious npm packages
- **DigiCert Code-Signing Infrastructure**: Certificate issuance and validation trust chain
- **Coca-Cola Fairlife OT/ICS**: Manufacturing and production control systems
- **Abbott Laboratories / Exact Sciences**: Legacy diagnostic systems in Cancer Diagnostics division
- **Ernst & Young**: Third-party IT support ticketing platform
- **Southeast Asian Government Networks**: Targets of GoSerpent espionage malware

## Attack Vectors and Techniques

- **Zero-Day Privilege Escalation (LegacyHive)**: Exploitation of a Windows kernel/registry hive flaw for local privilege escalation to SYSTEM; public exploit code enables immediate weaponization.
- **Chained Zero-Day Exploitation (SonicWall SMA)**: Two vulnerabilities combined for unauthenticated root RCE on edge VPN appliances; used by ransomware operators for initial access.
- **N-Day Exploitation of Internet-Facing Appliances (FortiSandbox, SharePoint)**: Active exploitation of recently patched vulnerabilities in security and collaboration platforms; CISA KEV listing confirms operational use.
- **Malicious Archive Parsing (7-Zip)**: User-assisted RCE via crafted archive files; requires social engineering to convince victim to open file.
- **Unauthenticated RCE via Cache Manipulation (wp2shell)**: Exploitation of WordPress Core object caching mechanism combined with deserialization/gadget chains for unauthenticated code execution; public PoC available.
- **Memory Exhaustion DoS (HollowByte)**: 11-byte TLS ClientHello triggers unbounded memory allocation per connection; memory leaked until process restart; highly efficient asymmetric DoS.
- **Cloud Credential Harvesting via Exposed Services (NadMesh)**: Automated Shodan-driven scanning for exposed AI/ML service ports and APIs; extraction of AWS keys, K8s tokens, and cloud metadata from misconfigured endpoints.
- **ClickFix Social Engineering (ACR Stealer)**: Fake browser verification prompts (CAPTCHA, "I am human") trick users into copying/running malicious PowerShell commands from clipboard, delivering infostealer.
- **SVG Steganography (Contagious Interview)**: Malicious payload hidden in SVG image metadata/pixel data; decoded and executed by loader delivered via fake coding challenge repositories or files.
- **Blockchain-Based C2 (Malicious npm Packages)**: Use of blockchain transactions (e.g., Ethereum, Bitcoin OP_RETURN, or smart contract events) for resilient, takedown-resistant command-and-control communication.
- **Code-Signing Certificate Theft (GoldenEyeDog)**: Intrusion into CA infrastructure or certificate subscriber systems to obtain valid code-signing certificates for malware signing.
- **Process Termination UI Spoofing (ClickLock)**: Forceful termination of all user-space GUI processes to simulate a system lock screen; keylogging of unlock password.
- **Ransomware Deployment via VPN Appliance Compromise (Inc Ransomware)**: Initial access via SonicWall zero-day chain → lateral movement → ransomware encryption.
- **Supply Chain Compromise (Malicious npm / Third-Party Support System)**: Injection of malicious code into trusted developer tools or compromise of vendor service provider infrastructure.
- **Espionage Malware Implant (GoSerpent)**: Custom Go-based implant for long-term persistence, command execution, and data exfiltration from high-value government targets.
- **Legacy System Exploitation (Abbott/Exact Sciences)**: Targeting of outdated, unsupported, or poorly segmented legacy systems in acquired business units.

## Threat Actor Activities

- **Inc Ransomware**: Actively exploiting chained SonicWall SMA zero-days for initial access to corporate networks; deploying ransomware following lateral movement. Demonstrates capability to acquire or develop zero-day exploits for edge devices.
- **ACR Stealer Operators**: Conducting high-volume enterprise-targeted infostealer campaigns using ClickFix social engineering; infrastructure and malware updated since 2024; focus on Microsoft 365 ecosystem credential and token theft.
- **NadMesh Botnet Operators**: Running automated cloud credential harvesting campaign targeting exposed AI/ML services; using Shodan for target enumeration; blockchain or decentralized infrastructure implied; claimed 3,811 AWS keys collected.
- **North Korean Actors (Contagious Interview / OtterCookie)**: Persistent campaign targeting developers and engineers via fake job interviews; using SVG steganography for payload delivery; aligning with OtterCookie malware family; strategic focus on software supply chain compromise.
- **GoldenEyeDog Subgroup (CylindricalCanine Cluster)**: Attributed to April 2026 DigiCert breach and code-signing certificate theft; sophisticated intrusion into CA/certificate infrastructure; enables long-term trusted malware distribution.
- **GoSerpent Operators**: Conducting cyber espionage against Southeast Asian government and diplomatic entities since late 2025; custom Go malware; focus on intelligence collection; attribution not publicly assigned.
- **Fairlife Ransomware Affiliates/Group**: Executed disruptive ransomware attack on food manufacturing subsidiary of Coca-Cola; halted US dairy production; group identity not disclosed.
- **Abbott Intruders / Extortion Actors**: Unauthorized access to Exact Sciences legacy systems; extortion claims made; possible data theft; investigation ongoing.
- **EY Third-Party Attackers**: Compromise of IT support ticketing vendor; data breach affecting EY customers/employees; highlights managed service provider risk.
- **Malicious npm Package Publishers**: Supply chain attack on Vite ecosystem; seven packages published with blockchain C2 RAT payload; developer/builder targeting.

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
