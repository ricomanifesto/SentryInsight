# Exploitation Report

## Executive Summary

Critical exploitation activity spans multiple high-impact vectors this period. A Microsoft SharePoint Server remote code execution zero-day (CVE-2026-58644) has been added to CISA's Known Exploited Vulnerabilities catalog, mandating immediate federal patching. Simultaneously, CISA ordered urgent remediation of two actively exploited Fortinet FortiSandbox vulnerabilities. In the WordPress ecosystem, the newly disclosed wp2shell core flaws now carry CVE identifiers, have a public proof-of-concept, and enable unauthenticated remote code execution—posing immediate risk to millions of sites.

Zero-day exploitation remains rampant across diverse platforms. The Inc ransomware group is chaining two SonicWall SMA zero-days to achieve root-level access on mobile access appliances. A Windows privilege escalation zero-day dubbed LegacyHive grants administrative privileges on fully patched systems, with a functional exploit publicly released. The OpenSSL HollowByte flaw allows unauthenticated denial-of-service via a mere 11-byte TLS payload, causing persistent memory exhaustion until process restart. These actively weaponized vulnerabilities demand emergency prioritization.

Threat actor operations show increasing sophistication in supply chain and social engineering domains. North Korean operators behind the Contagious Interview campaign now employ SVG steganography to hide OtterCookie-aligned malware in fake coding tests. The NadMesh Go botnet has harvested over 3,800 unique AWS keys by scanning exposed AI services for cloud credentials and Kubernetes tokens. Seven malicious Vite npm packages leverage blockchain-based command-and-control to deliver a remote access trojan. Meanwhile, the GoldenEyeDog subgroup (CylindricalCanine) has been linked to the April 2026 DigiCert breach and code-signing certificate theft, enabling downstream supply chain compromise.

## Active Exploitation Details

### Microsoft SharePoint Server RCE Zero-Day (CVE-2026-58644)
- **Description**: A remote code execution vulnerability in Microsoft SharePoint Server that was exploited as a zero-day before patching. The flaw allows unauthenticated attackers to execute arbitrary code on affected SharePoint servers.
- **Impact**: Full server compromise, potential lateral movement within organizational networks, data exfiltration, and persistence establishment.
- **Status**: Actively exploited in the wild. CISA added this vulnerability to the Known Exploited Vulnerabilities (KEV) catalog on July 17, 2026, requiring federal agencies to patch by August 7, 2026. Microsoft has released security updates.
- **CVE ID**: CVE-2026-58644

### Fortinet FortiSandbox Actively Exploited Vulnerabilities
- **Description**: Two vulnerabilities in the Fortinet FortiSandbox threat detection platform that are being actively exploited in the wild. Specific vulnerability types were not detailed in the source article.
- **Impact**: Compromise of the threat detection platform itself, potential bypass of security controls, network reconnaissance, and lateral movement.
- **Status**: Actively exploited. CISA issued an emergency directive on July 17, 2026, ordering federal civilian executive branch agencies to prioritize patching by July 20, 2026. Fortinet has released patches.
- **CVE ID**: CVE IDs not specified in source article

### wp2shell WordPress Core Unauthenticated RCE
- **Description**: Two vulnerabilities in WordPress core that, when combined, allow unauthenticated attackers to achieve remote code execution. The flaws involve a persistent object cache condition. Full technical details and a working proof-of-concept exploit have been publicly released.
- **Impact**: Complete takeover of WordPress sites without authentication, arbitrary code execution, malware deployment, data theft, and potential server compromise.
- **Status**: Actively exploitable with public PoC. CVE identifiers have been assigned as of July 18, 2026. WordPress has released patches. Immediate updating is critical.
- **CVE ID**: CVE IDs assigned but not specified in source article

### SonicWall SMA Zero-Day Chain (Inc Ransomware)
- **Description**: Two zero-day vulnerabilities in SonicWall Secure Mobile Access (SMA) appliances that, when chained together, provide threat actors with root-level capabilities on the devices.
- **Impact**: Full administrative control over VPN/appliance infrastructure, network access, credential harvesting, lateral movement, and ransomware deployment.
- **Status**: Actively exploited by Inc ransomware group. Zero-day status means no patches were available at time of reporting. SonicWall has likely released or is developing mitigations.
- **CVE ID**: CVE IDs not specified in source article

### Windows LegacyHive Privilege Escalation Zero-Day
- **Description**: A Windows zero-day exploit dubbed "LegacyHive" released by a researcher using the handle "Nightmare Eclipse" that allows attackers to escalate privileges on up-to-date Windows systems.
- **Impact**: Local privilege escalation to SYSTEM/admin rights, bypassing security controls, disabling defenses, and enabling full system compromise.
- **Status**: Public exploit code released. Zero-day status—no patch available at time of disclosure. Microsoft is likely developing a fix.
- **CVE ID**: CVE ID not specified in source article

### OpenSSL HollowByte Denial-of-Service
- **Description**: A vulnerability in OpenSSL where an 11-byte malicious TLS request causes the server to allocate up to 131 KB of memory for a message that never arrives. On glibc systems, this memory is not released until the process restarts, enabling efficient denial-of-service.
- **Impact**: Resource exhaustion DoS, service unavailability, potential amplification across multiple connections. Low-bandwidth, high-impact attack vector.
- **Status**: Vulnerability disclosed with technical details. OpenSSL has released patches (versions 3.0.16, 3.2.2, 3.3.1, and 3.4.0). Server administrators must restart processes to reclaim leaked memory.
- **CVE ID**: CVE ID not specified in source articles

### Seven Malicious Vite npm Packages (Supply Chain Attack)
- **Description**: A cluster of seven malicious npm packages targeting the Vite frontend tooling ecosystem. The packages use blockchain-based command-and-control infrastructure to deliver a remote access trojan (RAT).
- **Impact**: Compromise of developer machines and build pipelines, persistent remote access, credential theft, source code exfiltration, and potential downstream supply chain contamination.
- **Status**: Actively distributed via npm registry. Packages have been identified and likely removed, but compromised environments require incident response.
- **CVE ID**: No CVE IDs assigned (malicious packages, not vulnerabilities in legitimate software)

### NadMesh Botnet Credential Harvesting
- **Description**: A Go-based botnet discovered in early July 2026 that scans for exposed AI services using Shodan to harvest cloud credentials (AWS keys) and Kubernetes tokens. The operator's dashboard claims 3,811 unique AWS keys collected.
- **Impact**: Cloud account takeover, cryptojacking, data exfiltration, infrastructure hijacking, and lateral movement within cloud environments.
- **Status**: Active scanning and exploitation campaign. Organizations with exposed AI/ML services, Kubernetes APIs, and cloud metadata endpoints are at immediate risk.
- **CVE ID**: No CVE IDs (exploitation of misconfigurations and exposed services)

### GoldenEyeDog / CylindricalCanine DigiCert Breach
- **Description**: A threat activity cluster dubbed CylindricalCanine (with subgroup GoldenEyeDog) attributed to the April 2026 DigiCert security incident involving code-signing certificate theft.
- **Impact**: Theft of code-signing certificates enables supply chain attacks through trusted malware signing, bypassing application control policies, and distributing signed malicious payloads.
- **Status**: Breach occurred April 2026; attribution published July 2026. DigiCert has responded. Certificate revocation and reissuance efforts underway. Downstream impact assessment ongoing.
- **CVE ID**: No CVE ID (security incident/breach, not a software vulnerability)

### ACR Stealer ClickFix Campaign
- **Description**: The ACR Stealer infostealer (active since 2024) is using ClickFix social engineering lures to steal browser passwords, live session tokens, PDFs, Microsoft 365 documents, and files from synced OneDrive folders.
- **Impact**: Credential theft, session hijacking, business email compromise enablement, sensitive document exfiltration, and identity theft.
- **Status**: Active campaign. ClickFix technique remains effective against enterprise users. Requires user interaction but high success rate due to social engineering sophistication.
- **CVE ID**: No CVE ID (malware campaign using social engineering)

### GoSerpent Malware Espionage Campaign
- **Description**: Previously undocumented malware called GoSerpent targeting Southeast Asian government and diplomatic entities since late 2025 for cyber espionage.
- **Impact**: Persistent access to government networks, intelligence collection, diplomatic communication interception, and strategic advantage for threat actor.
- **Status**: Active campaign since late 2025. Attribution and technical details published July 2026. Targeted organizations should conduct compromise assessments.
- **CVE ID**: No CVE ID (malware campaign, exploitation vectors not specified)

### Contagious Interview Campaign (North Korean SVG Steganography)
- **Description**: North Korean threat actors linked to the Contagious Interview campaign employing steganography in SVG image files to conceal malicious payloads (OtterCookie-aligned malware) within fake coding tests for job applicants.
- **Impact**: Developer and engineer compromise, source code access, supply chain infiltration, and persistent access to technology organizations.
- **Status**: Active campaign. Novel use of SVG steganography evades traditional detection. Targets individuals in hiring processes at tech companies.
- **CVE ID**: No CVE ID (social engineering and steganography technique)

### ClickLock macOS Information Stealer
- **Description**: New macOS malware dubbed ClickLock that terminates all visible processes to force users into entering their system login password, which is then captured.
- **Impact**: Full user credential compromise, keychain access, privilege escalation potential, and complete user session takeover.
- **Status**: Active in the wild. Novel anti-analysis and credential harvesting technique specific to macOS.
- **CVE ID**: No CVE ID (malware, not a vulnerability)

### Claude Chrome Extension Flaw
- **Description**: A flaw in Anthropic's Claude for Chrome browser extension that allows malicious extensions to simulate user clicks and trigger predefined AI actions, potentially abusing Claude's access to sensitive data and actions.
- **Impact**: Unauthorized AI actions, data exfiltration through AI, privilege escalation within browser context, and bypass of extension permission models.
- **Status**: Vulnerability disclosed. Anthropic likely developing fix. Users should review installed extensions and limit Claude extension permissions.
- **CVE ID**: CVE ID not specified in source article

## Affected Systems and Products

- **Microsoft SharePoint Server**: All versions affected by CVE-2026-58644 prior to July 2026 security updates. On-premises deployments at highest risk.
- **Fortinet FortiSandbox**: Appliance and virtual appliance versions vulnerable to two actively exploited flaws. Specific version ranges not detailed in source.
- **WordPress Core**: All versions prior to the July 2026 security release containing fixes for the wp2shell vulnerabilities. Millions of sites potentially affected.
- **SonicWall SMA (Secure Mobile Access) Appliances**: SMA 200, 400, 500, 1000, and 10000 series, and virtual appliances. Firmware versions prior to patched releases.
- **Windows**: Up-to-date Windows systems (specific versions not detailed) vulnerable to LegacyHive privilege escalation zero-day.
- **OpenSSL**: Versions prior to 3.0.16, 3.2.2, 3.3.1, and 3.4.0. Affects servers using OpenSSL for TLS termination (web servers, load balancers, VPN gateways, API gateways).
- **Vite/npm Ecosystem**: Developers and CI/CD pipelines using Vite frontend tooling who may have installed malicious packages: `vite-plugin-*` and related supply chain dependencies.
- **Exposed AI/ML Services**: Publicly accessible AI model endpoints, Jupyter notebooks, MLflow servers, Kubeflow dashboards, and Kubernetes API servers with anonymous access enabled.
- **DigiCert Code-Signing Infrastructure**: Organizations relying on DigiCert-issued code-signing certificates for software distribution and application control policies.
- **Enterprise Browsers (Chrome/Edge)**: Users with Anthropic Claude extension installed alongside other extensions; macOS users targeted by ClickLock malware.
- **Southeast Asian Government Networks**: Diplomatic and government entities targeted by GoSerpent malware campaign since late 2025.

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active use of unpatched vulnerabilities in SharePoint (CVE-2026-58644), FortiSandbox, SonicWall SMA (two flaws chained), and Windows (LegacyHive) before vendor fixes available.
- **Unauthenticated Remote Code Execution**: wp2shell WordPress flaws and SharePoint CVE-2026-58644 allow pre-authentication RCE, enabling mass exploitation via automated scanning.
- **Privilege Escalation**: Windows LegacyHive zero-day provides local-to-SYSTEM escalation; ClickLock macOS malware forces credential entry for privilege access.
- **Denial-of-Service via Resource Exhaustion**: OpenSSL HollowByte uses 11-byte TLS ClientHello to trigger unbounded memory allocation (131 KB per connection) that persists until process restart.
- **Supply Chain Compromise (npm)**: Malicious Vite packages published to npm registry with blockchain-based C2 (using smart contracts for resilient command delivery) deploying RAT payloads.
- **Credential Harvesting at Scale**: NadMesh botnet uses Shodan-harvested targets to scan exposed AI services and Kubernetes APIs for AWS keys (3,811+ collected) and cloud tokens.
- **Code-Signing Certificate Theft**: GoldenEyeDog/CylindricalCanine breach of DigiCert enables trusted malware signing for supply chain attacks and defense evasion.
- **ClickFix Social Engineering**: ACR Stealer uses fake "verify you're human" / browser error pages to trick users into executing malicious PowerShell commands.
- **Steganography in SVG Images**: North Korean Contagious Interview campaign hides OtterCookie malware in SVG flag images within fake coding tests for developer targeting.
- **Process Termination for Credential Theft**: ClickLock macOS malware kills all visible processes, forcing authentication prompt to capture login password.
- **Extension-to-Extension Attack**: Malicious Chrome extension simulates clicks on Claude extension UI to trigger AI actions without user consent.
- **Ransomware Deployment via Appliance Compromise**: Inc ransomware leverages SonicWall SMA zero-day chain for initial access and root persistence before encryption.
- **Blockchain-Based C2**: Malicious npm packages use smart contract interactions for command-and-control, providing censorship-resistant and takedown-resistant infrastructure.

## Threat Actor Activities

- **Inc Ransomware Group**: Actively exploiting chained SonicWall SMA zero-days for initial access to achieve root on VPN appliances, enabling network-wide ransomware deployment. Demonstrates rapid zero-day operationalization.
- **GoldenEyeDog / CylindricalCanine**: Threat activity cluster attributed to April 2026 DigiCert breach and code-signing certificate theft. Expel researchers tracked this group's operations. High-capability actor targeting trust infrastructure.
- **North Korean Contagious Interview Operators**: State-linked actors conducting developer-targeted social engineering via fake job interviews and coding tests. Now using SVG steganography to deliver OtterCookie-aligned malware. Persistent campaign targeting technology sector.
- **NadMesh Botnet Operator**: Unknown threat actor operating Go-based botnet since early July 2026. Uses Shodan for target enumeration, focuses on AI/ML service exposures for cloud credential harvesting. Dashboard shows 3,811+ AWS keys collected.
- **ACR Stealer Operators**: Cybercriminal group distributing infostealer since 2024, now adopting ClickFix technique for enterprise credential and session token theft. Targets Microsoft 365, browser data, and synced cloud files.
- **GoSerpent Espionage Actor**: Previously undocumented threat actor targeting Southeast Asian governments and diplomats since late 2025. Custom Go-based malware suggests state-sponsored espionage motivation.
- **Fairlife/Coca-Cola Ransomware Actor**: Unnamed ransomware group disrupted Fairlife dairy production across US. Operational impact on critical food manufacturing infrastructure.
- **Abbott Laboratories Intruders**: Unknown actors behind two separate incidents targeting legacy Exact Sciences systems in Cancer Diagnostics business. Extortion claims suggest ransomware or data theft motivation.
- **EY Support System Attackers**: Threat actors compromised third-party IT support ticket system used by Ernst & Young personnel, leading to customer data breach.

## Source Attribution

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
- **1M+ Emails Use Hidden Text to Dupe AI Security Filters**: Dark Reading - https://www.darkreading.com/threat-intelligence/1m-emails-hidden-text-dupe-ai-security-filters
- **Claude Chrome extension flaw lets malicious extensions trigger AI actions**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/claude-chrome-extension-flaw-lets-malicious-extensions-trigger-ai-actions/
