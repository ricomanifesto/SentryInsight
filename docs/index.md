# Exploitation Report

## Executive Summary

Multiple critical zero-day vulnerabilities are under active exploitation across widely deployed platforms, including WordPress core, Microsoft SharePoint, SonicWall SMA appliances, Fortinet FortiSandbox, and Windows. The WordPress wp2shell flaw permits unauthenticated remote code execution on all 6.9 and 7.0 sites, while a chained SonicWall exploit grants root access on mobile access appliances. CISA has added the actively exploited SharePoint RCE zero-day CVE-2026-58644 to its Known Exploited Vulnerabilities catalog and ordered federal agencies to patch two FortiSandbox flaws immediately. A Windows privilege escalation zero-day dubbed LegacyHive has been publicly released, and the OpenSSL HollowByte flaw enables memory-exhaustion DoS with a mere 11-byte TLS request.

Supply chain and malware campaigns are intensifying. Seven malicious Vite npm packages leverage blockchain-based command-and-control to deliver a remote access trojan, while the NadMesh Go botnet has harvested over 3,800 AWS keys by scanning exposed AI services. North Korean operators behind the Contagious Interview campaign are using steganographic SVG payloads in fake coding tests to deploy OtterCookie-aligned malware. The GoldenEyeDog subgroup (tracked as CylindricalCanine) has been linked to the April 2026 DigiCert breach involving code-signing certificate theft. Meanwhile, infostealers including ACR Stealer, ClickLock, and OkoBot are evolving tactics—from ClickFix lures and forced authentication prompts to multi-payload frameworks targeting cryptocurrency wallets and Microsoft 365 data.

## Active Exploitation Details

### WordPress Core wp2shell Remote Code Execution
- **Description**: An unauthenticated HTTP request can achieve remote code execution on WordPress core installations without any plugins. The vulnerability exists in core functionality, making bare installations exploitable.
- **Impact**: Full remote code execution on affected WordPress sites, leading to complete site compromise, data theft, and potential lateral movement.
- **Status**: Actively exploitable on all WordPress 6.9 and 7.0 sites until patched on Friday (per article publication date). Patch available via WordPress update.

### OpenSSL HollowByte Denial-of-Service
- **Description**: An 11-byte malicious TLS request causes unpatched OpenSSL servers to allocate up to 131 KB of memory for a message that never arrives. On glibc systems, the memory is not released until the process restarts.
- **Impact**: Memory exhaustion denial-of-service; repeated requests can deplete server memory and cause service instability or crash.
- **Status**: Vulnerability disclosed with technical details; patches expected from OpenSSL project. No active exploitation reports cited beyond proof-of-concept.

### SonicWall SMA Zero-Day Chain
- **Description**: Two vulnerabilities in SonicWall Secure Mobile Access (SMA) appliances that, when chained together, allow threat actors to gain root-level capabilities.
- **Impact**: Full root access on SMA appliances, enabling network pivoting, credential theft, and persistent access.
- **Status**: Actively exploited by Inc Ransomware group. Zero-day status indicates no patch available at time of reporting.

### Microsoft SharePoint Server RCE Zero-Day (CVE-2026-58644)
- **Description**: A remote code execution vulnerability in Microsoft SharePoint Server that has been exploited in the wild.
- **Impact**: Remote code execution on SharePoint Server, potentially leading to data exfiltration, lateral movement, and persistence in enterprise environments.
- **Status**: Actively exploited. CISA added to Known Exploited Vulnerabilities (KEV) catalog. Patch available from Microsoft.
- **CVE ID**: CVE-2026-58644

### Fortinet FortiSandbox Actively Exploited Flaws
- **Description**: Two vulnerabilities in the Fortinet FortiSandbox threat detection platform that are under active exploitation.
- **Impact**: Compromise of threat detection infrastructure, potential bypass of security controls, and network infiltration.
- **Status**: Actively exploited. CISA ordered federal agencies to prioritize patching by Sunday (per article date). Patches available from Fortinet.

### Windows LegacyHive Privilege Escalation Zero-Day
- **Description**: A zero-day exploit released by researcher "Nightmare Eclipse" that allows attackers to escalate privileges on up-to-date Windows systems.
- **Impact**: Local privilege escalation to administrator/SYSTEM, enabling full system compromise from low-privilege foothold.
- **Status**: Publicly released proof-of-concept exploit. Zero-day status; no patch available at time of reporting.

### DigiCert Code-Signing Certificate Theft
- **Description**: A security incident at DigiCert in April 2026 resulting in the theft of code-signing certificates, attributed to the GoldenEyeDog subgroup (CylindricalCanine).
- **Impact**: Stolen code-signing certificates can be used to sign malicious software, bypassing trust controls and enabling supply chain attacks.
- **Status**: Incident disclosed; certificates presumably revoked. Attribution to GoldenEyeDog/CylindricalCanine by Expel researchers.

## Affected Systems and Products

- **WordPress**: Versions 6.9 and 7.0 (core installations, no plugins required)
- **OpenSSL**: Servers running vulnerable OpenSSL versions on glibc-based systems
- **SonicWall SMA**: Secure Mobile Access appliances (specific versions not disclosed)
- **Microsoft SharePoint Server**: Versions affected by CVE-2026-58644 (specific versions per Microsoft advisory)
- **Fortinet FortiSandbox**: Threat detection platform (specific versions per Fortinet advisory)
- **Windows**: Up-to-date Windows systems (specific versions not disclosed; LegacyHive affects current releases)
- **DigiCert Infrastructure**: Code-signing certificate issuance systems (April 2026 incident)
- **Vite/npm Ecosystem**: Developers using Vite frontend tooling; seven malicious packages identified
- **macOS**: Systems targeted by ClickLock malware (version specifics not disclosed)
- **Chrome Browser**: Users with Anthropic Claude extension installed (extension flaw)

## Attack Vectors and Techniques

- **Unauthenticated HTTP Request (WordPress)**: Direct exploitation via crafted HTTP request to vulnerable core endpoint; no authentication or user interaction required.
- **Memory Exhaustion via Minimal TLS Payload (OpenSSL)**: 11-byte TLS ClientHello or similar record triggers excessive memory allocation; repeated connections amplify DoS impact.
- **Vulnerability Chaining (SonicWall SMA)**: Two distinct flaws combined—likely authentication bypass plus command injection or deserialization—to achieve root from unauthenticated context.
- **Supply Chain Compromise (npm/Vite)**: Malicious packages published to npm registry targeting Vite users; packages execute on install or build, establishing blockchain-based C2.
- **Blockchain Command-and-Control**: C2 infrastructure leveraging blockchain transactions or smart contracts for resilient, censorship-resistant communication.
- **Shodan-Harvested Scanning (NadMesh)**: Automated scanning of exposed AI/ML services using Shodan data to build target queues for credential harvesting.
- **Steganographic Payload Delivery (Contagious Interview)**: Malicious code concealed within SVG image files (flag images) using steganography; delivered via fake coding test platforms.
- **Social Engineering via Fake Job Interviews**: North Korean operators pose as recruiters, direct targets to coding challenge sites hosting steganographic payloads.
- **ClickFix Social Engineering (ACR Stealer)**: Victims tricked into executing malicious commands via fake verification prompts (e.g., "Click to verify you're human").
- **Forced Authentication Prompt (ClickLock)**: Malware terminates all visible GUI processes, leaving only a system authentication dialog; user enters credentials, which are captured.
- **Multi-Payload Modular Framework (OkoBot)**: Framework deploying 20+ discrete payloads for credential theft, cryptocurrency wallet seed extraction, and data exfiltration.
- **Malicious Extension Click Simulation (Claude Chrome)**: Compromised or malicious Chrome extension simulates user clicks on Claude extension UI to trigger privileged AI actions.

## Threat Actor Activities

- **Inc Ransomware Group**: Actively exploiting chained SonicWall SMA zero-days to gain root access on appliances; likely using access for initial intrusion and lateral movement in ransomware operations.
- **NadMesh Botnet Operator**: Go-based botnet active since early July 2026; scans for exposed AI services via Shodan, harvests cloud credentials (3,811 unique AWS keys claimed) and Kubernetes tokens; infrastructure suggests financially motivated credential theft.
- **GoldenEyeDog / CylindricalCanine**: Subgroup attributed to April 2026 DigiCert breach involving code-signing certificate theft; tracked by Expel; capability suggests supply chain focus and high-value targeting.
- **North Korean Actors (Contagious Interview Campaign)**: Ongoing campaign using fake job interviews and coding tests to deliver malware via steganographic SVG payloads; deploys OtterCookie-aligned malware; targets developers and organizations globally.
- **Nightmare Eclipse (Researcher/Handle)**: Published Windows LegacyHive zero-day privilege escalation exploit; motivation appears to be vulnerability disclosure via full public release rather than coordinated disclosure.
- **ACR Stealer Operators**: Infostealer active since 2024; evolved to use ClickFix lures; targets browser passwords, session tokens, PDFs, Microsoft 365 documents, and OneDrive-synced files; enterprise-focused.
- **GoSerpent Operators**: Previously undocumented malware targeting Southeast Asian governments and diplomats since late 2025; espionage-focused; likely state-sponsored given targeting.
- **OkoBot Operators**: New modular framework deploying 20+ payloads for cryptocurrency wallet seed phrases, credentials, and sensitive data; financially motivated.
- **REvil Ransomware Affiliates**: Referenced in context of U.S. extradition request for suspect Aleksandr Ermakov (detained in Armenia); indicates ongoing law enforcement pursuit of ransomware ecosystem actors.

## Source Attribution

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
- **New OkoBot framework deploys 20 payloads to steal data, crypto**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-okobot-framework-deploys-20-payloads-to-steal-data-crypto/
