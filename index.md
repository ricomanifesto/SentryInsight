# Exploitation Report

## Executive Summary

Critical exploitation activity this period centers on a Microsoft SharePoint zero-day (CVE-2026-58644) added to CISA's Known Exploited Vulnerabilities catalog, confirming active in-the-wild attacks against on-premises SharePoint Server. Simultaneously, CISA issued an emergency directive for federal agencies to patch two actively exploited Fortinet FortiSandbox flaws, signaling broader targeting of network security appliances. A newly released Windows zero-day dubbed LegacyHive provides reliable privilege escalation on fully patched systems, while the HollowByte vulnerability allows unauthenticated denial-of-service against OpenSSL servers with a mere 11-byte payload.

Software supply chain attacks remain a dominant vector. Seven malicious npm packages masquerading as Vite tooling components were discovered delivering a remote access trojan via an innovative blockchain-based command-and-control infrastructure. The April 2026 DigiCert breach has been attributed to the GoldenEyeDog subgroup (tracked as CylindricalCanine), resulting in code-signing certificate theft that could enable future supply chain compromises. North Korean operators behind the Contagious Interview campaign continue refining steganographic techniques, hiding OtterCookie-aligned malware payloads within SVG flag images delivered through fake coding assessments.

Threat actors are aggressively targeting cloud and AI infrastructure. The NadMesh Go botnet systematically scans for exposed AI services using Shodan, harvesting AWS credentials and Kubernetes tokens—its operator dashboard claims over 3,800 unique AWS keys. Infostealers including ACR Stealer, ClickLock, and the new OkoBot framework (deploying 20+ payloads) are evolving delivery via ClickFix social engineering and macOS process manipulation to steal browser sessions, Microsoft 365 documents, and cryptocurrency wallets. GoSerpent malware has conducted espionage against Southeast Asian governments since late 2025, while ransomware disrupted Fairlife dairy production across the United States.

## Active Exploitation Details

### Microsoft SharePoint Server RCE Zero-Day (CVE-2026-58644)
- **Description**: A remote code execution vulnerability in Microsoft SharePoint Server that allows unauthenticated attackers to execute arbitrary code on affected servers. The flaw was patched by Microsoft and immediately added to CISA's Known Exploited Vulnerabilities (KEV) catalog.
- **Impact**: Full server compromise, potential lateral movement within organizational networks, data exfiltration, and persistence establishment.
- **Status**: Actively exploited in the wild. CISA added to KEV on July 17, 2026, requiring federal agencies to remediate immediately. Patches available from Microsoft.
- **CVE ID**: CVE-2026-58644

### Fortinet FortiSandbox Actively Exploited Vulnerabilities
- **Description**: Two vulnerabilities in the Fortinet FortiSandbox threat detection platform that are being actively exploited. Specific technical details were not disclosed in the advisory.
- **Impact**: Compromise of the sandbox analysis environment, potential bypass of threat detection, and use as a pivot point into protected networks.
- **Status**: Actively exploited. CISA issued an emergency directive on July 17, 2026, ordering federal civilian executive branch agencies to prioritize patching by July 20, 2026.
- **CVE ID**: CVE IDs not provided in source article.

### Windows LegacyHive Zero-Day Privilege Escalation
- **Description**: A zero-day privilege escalation vulnerability in Windows, dubbed "LegacyHive," released by a security researcher using the handle "Nightmare Eclipse." The exploit works on up-to-date Windows systems.
- **Impact**: Attackers can escalate from standard user to SYSTEM/admin privileges, achieving full control over the compromised host.
- **Status**: Public exploit code released. Zero-day with no patch available at time of disclosure. Active exploitation risk is high given public availability.
- **CVE ID**: CVE ID not provided in source article.

### HollowByte OpenSSL Denial-of-Service
- **Description**: A vulnerability in OpenSSL servers dubbed "HollowByte" that allows unauthenticated attackers to trigger a denial-of-service condition by sending a malicious payload of only 11 bytes, causing uncontrolled memory consumption.
- **Impact**: Complete service unavailability, resource exhaustion, potential disruption of TLS-dependent services.
- **Status**: Vulnerability disclosed with technical details. Patch status for OpenSSL not specified in source.
- **CVE ID**: CVE ID not provided in source article.

### Malicious Vite npm Supply Chain Packages
- **Description**: A cluster of seven malicious npm packages targeting the Vite frontend build tooling ecosystem. Packages masquerade as legitimate Vite-related modules and deliver a remote access trojan (RAT) using a blockchain-based command-and-control infrastructure for resilience.
- **Impact**: Compromise of developer machines and build environments, potential downstream supply chain contamination, persistent remote access, credential theft.
- **Status**: Discovered and published. Packages likely removed from npm registry. Active infections possible in development environments that installed the malicious packages.
- **CVE ID**: No CVE IDs assigned (supply chain malware, not a software vulnerability).

### ACR Stealer ClickFix Campaign
- **Description**: The ACR Stealer infostealer (active since 2024) is being distributed via ClickFix social engineering lures—fake error pages or verification prompts that trick users into executing malicious PowerShell commands.
- **Impact**: Theft of saved browser passwords, live session tokens, PDF documents, Microsoft 365 files, and OneDrive-synced data. Enables account takeover and data exfiltration.
- **Status**: Active campaign observed in July 2026. ClickFix technique remains highly effective against enterprise users.
- **CVE ID**: No CVE ID (malware delivery technique, not a vulnerability).

### North Korean Contagious Interview Campaign (OtterCookie/SVG Steganography)
- **Description**: North Korean threat actors linked to the Contagious Interview campaign use fake coding tests delivered as job interview assessments. Malicious payloads aligned with the OtterCookie malware family are concealed within SVG flag images using steganography.
- **Impact**: Initial access to target systems, deployment of custom malware, potential supply chain compromise if developers are targeted.
- **Status**: Active campaign observed in July 2026. Steganographic SVG delivery evades traditional content inspection.
- **CVE ID**: No CVE ID (malware delivery technique).

### NadMesh Botnet Cloud Credential Harvesting
- **Description**: A Go-based botnet called NadMesh systematically scans for exposed AI services using a Shodan harvester to maintain a scan queue. The botnet extracts AWS access keys and Kubernetes service account tokens from compromised or misconfigured services.
- **Impact**: Cloud account takeover, infrastructure compromise, cryptocurrency mining, data theft, lateral movement in cloud environments. Operator dashboard claims 3,811 unique AWS keys harvested.
- **Status**: Active since early July 2026. Ongoing scanning and credential harvesting operations.
- **CVE ID**: No CVE ID (exploits misconfigurations and exposed services, not a specific software vulnerability).

### GoSerpent Espionage Malware
- **Description**: A previously undocumented Go-based malware framework targeting government and diplomatic entities in Southeast Asia since late 2025. Used for cyber espionage operations.
- **Impact**: Persistent access to sensitive government networks, intelligence collection, document exfiltration, credential harvesting.
- **Status**: Active espionage campaign. Malware remained undetected since at least late 2025.
- **CVE ID**: No CVE ID (malware, not a vulnerability).

### ClickLock macOS Credential Theft
- **Description**: A new macOS information-stealing malware dubbed ClickLock that terminates all visible user processes, forcing the victim to enter their system login password to regain control. The malware captures this credential.
- **Impact**: Theft of user login credentials, potential privilege escalation, access to keychain and encrypted data.
- **Status**: Newly discovered in July 2026. Active distribution vector not specified.
- **CVE ID**: No CVE ID (malware behavior, not a vulnerability).

### OkoBot Multi-Payload Theft Framework
- **Description**: A malicious framework called OkoBot that deploys more than 20 distinct payloads focused on stealing cryptocurrency wallet seed phrases, credentials, and other sensitive data.
- **Impact**: Comprehensive data theft including crypto assets, authentication credentials, browser data, and system information.
- **Status**: Newly discovered in July 2026. Active deployment observed.
- **CVE ID**: No CVE ID (malware framework).

### Fairlife Ransomware Attack
- **Description**: A ransomware attack against Fairlife, a Coca-Cola dairy subsidiary, that halted production operations across the United States.
- **Impact**: Operational disruption, production suspension, financial loss, potential data exfiltration.
- **Status**: Disclosed July 2026. Recovery operations underway. Ransomware variant and initial access vector not specified.
- **CVE ID**: No CVE ID (ransomware incident).

### DigiCert Code-Signing Certificate Theft
- **Description**: The April 2026 DigiCert security incident resulted in the theft of code-signing certificates. The breach has been attributed to a threat activity cluster dubbed CylindricalCanine, with a subgroup named GoldenEyeDog.
- **Impact**: Stolen certificates could be used to sign malicious software, bypassing trust controls and enabling supply chain attacks against downstream users.
- **Status**: Breach occurred April 2026. Attribution published July 2026. Certificate revocation and reissuance likely underway.
- **CVE ID**: No CVE ID (security breach/incident).

### Ernst & Young Third-Party Support System Breach
- **Description**: Compromise of a third-party support ticket system used by EY IT personnel led to a data breach affecting customers.
- **Impact**: Exposure of customer data processed through the support system. Supply chain risk via IT service providers.
- **Status**: Disclosed July 2026. Notification to affected customers in progress.
- **CVE ID**: No CVE ID (third-party compromise).

## Affected Systems and Products

- **Microsoft SharePoint Server**: On-premises SharePoint Server versions affected by CVE-2026-58644. Specific versions not detailed in source.
- **Fortinet FortiSandbox**: Threat detection appliance platform. Specific firmware versions affected by the two actively exploited flaws not detailed in source.
- **Windows (all supported versions)**: LegacyHive zero-day privilege escalation affects up-to-date Windows systems per researcher disclosure.
- **OpenSSL Servers**: Servers running vulnerable OpenSSL versions susceptible to HollowByte DoS (11-byte payload). Specific versions not detailed.
- **npm/Vite Ecosystem**: Developers and build systems using Vite frontend tooling; seven specific malicious package names not listed in source excerpt.
- **Google Chrome / Anthropic Claude Extension**: Claude for Chrome browser extension flaw allows malicious extensions to simulate clicks and trigger AI actions.
- **macOS Systems**: ClickLock malware targets macOS users; specific OS versions not detailed.
- **AWS / Kubernetes Environments**: NadMesh botnet targets exposed AI services to harvest AWS keys and Kubernetes tokens.
- **Southeast Asian Government Networks**: GoSerpent malware targets diplomatic and government entities in Southeast Asia.
- **Fairlife / Coca-Cola Production Systems**: Ransomware impacted US dairy production operations.
- **DigiCert Code-Signing Infrastructure**: Certificate authority systems breached in April 2026; code-signing certificates stolen.
- **Ernst & Young Third-Party Support Platform**: Support ticket system used by EY IT personnel compromised.

## Attack Vectors and Techniques

- **Zero-Day Privilege Escalation**: LegacyHive exploit provides reliable SYSTEM-level access on patched Windows; public exploit code released by "Nightmare Eclipse."
- **Remote Code Execution via Unpatched Server**: CVE-2026-58644 exploited in SharePoint for initial access and code execution without authentication.
- **Network Appliance Exploitation**: Two FortiSandbox flaws actively exploited to compromise security monitoring infrastructure.
- **DoS via Minimal Payload**: HollowByte triggers OpenSSL memory exhaustion with 11-byte unauthenticated packet.
- **Software Supply Chain (npm)**: Seven malicious Vite packages published to npm registry; blockchain-based C2 for resilience against takedown.
- **Code-Signing Certificate Theft**: DigiCert breach (CylindricalCanine/GoldenEyeDog) enables future signed malware distribution.
- **Third-Party IT Service Compromise**: EY breach via support ticket system used by internal IT staff.
- **Steganographic Payload Delivery**: North Korean Contagious Interview campaign hides OtterCookie malware in SVG flag images within fake coding tests.
- **ClickFix Social Engineering**: ACR Stealer uses fake verification/error prompts to trick users into executing malicious PowerShell.
- **Exposed Service Scanning (Shodan)**: NadMesh botnet uses Shodan harvester to continuously identify exposed AI services for credential harvesting.
- **Cloud Credential Harvesting**: Automated extraction of AWS keys and Kubernetes tokens from misconfigured/exposed services.
- **Multi-Payload Modular Framework**: OkoBot deploys 20+ specialized payloads for crypto wallet seeds, credentials, browser data.
- **macOS Process Manipulation**: ClickLock terminates visible processes to force password entry and capture credentials.
- **Ransomware Deployment**: Fairlife attack halted US dairy production; initial access vector unspecified.
- **AI Filter Evasion (Text Salting)**: 1M+ phishing emails use hidden text techniques to bypass LLM-based security filters.
- **Browser Extension Abuse**: Flaw in Claude Chrome extension allows malicious extensions to simulate user clicks and trigger AI actions.
- **Residential Proxy Infrastructure**: Carding operations increasingly rely on "clean" residential proxies combined with browser fingerprinting.

## Threat Actor Activities

- **CylindricalCanine / GoldenEyeDog**: Attributed to April 2026 DigiCert breach and code-signing certificate theft. Expel provided technical details. Subgroup GoldenEyeDog specifically linked to the operation.
- **North Korean Contagious Interview Operators**: Ongoing campaign using fake job interviews and coding tests; employs SVG steganography to deliver OtterCookie-aligned malware. Active July 2026.
- **NadMesh Botnet Operator**: Go-based botnet hunting exposed AI services since early July 2026. Uses Shodan harvester. Dashboard claims 3,811 unique AWS keys. Targets cloud credentials and Kubernetes tokens.
- **ACR Stealer Operators**: Infostealer active since 2024; adopted ClickFix delivery in 2026. Targets browser tokens, M365 documents, OneDrive files, passwords.
- **GoSerpent Espionage Actors**: Previously undocumented malware targeting Southeast Asian governments and diplomats since late 2025. Cyber espionage focus.
- **Scattered Spider (0ktapus/Scatter Swine)**: Two members (Owen Flowers, 18; Thalha Jubair, 20) sentenced to 5.5 years each for 2024 Transport for London hack causing £29M damage and 148 station disruptions.
- **REvil Ransomware Affiliate**: Aleksandr Ermakov detained in Armenia on US extradition request (June 28, 2026). Lawyers claim mistaken identity.
- **Fairlife Ransomware Operators**: Ransomware attack on Coca-Cola subsidiary halted US dairy production. Variant and group unidentified.
- **OkoBot Framework Operators**: New multi-payload theft framework (20+ payloads) targeting crypto wallets, credentials, sensitive data. Discovered July 2026.
- **ClickLock Developers**: New macOS info-stealer using process termination to force credential entry. Discovered July 2026.
- **"Nightmare Eclipse" Researcher**: Published Windows LegacyHive zero-day privilege escalation exploit. Handle associated with exploit release.
- **Financially Motivated Carding Actors**: Shifting to "clean" residential proxies with browser fingerprinting as proxy reputation systems improve.

## Source Attribution

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
- **Two Scattered Spider Hackers Get 5.5 Years Each for £29 Million TfL Hack**: The Hacker News - https://thehackernews.com/2026/07/two-scattered-spider-hackers-get-55.html
- **ThreatsDay: Game Cheat Spyware, 24-Hour Ransomware, Chrome Sync Stalking + 12 More Stories**: The Hacker News - https://thehackernews.com/2026/07/threatsday-game-cheat-spyware-24-hour.html
- **AI Agents Broke the Security Playbook. Here's What Replaces It.**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/ai-agents-broke-the-security-playbook-heres-what-replaces-it/
- **23andMe to pay $18 million in new genetics data breach settlement**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/23andme-to-pay-18-million-in-new-genetics-data-breach-settlement/
