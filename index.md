# Exploitation Report

## Executive Summary

Critical exploitation activity spans multiple high-impact vectors this reporting period. A SharePoint Server remote code execution zero-day (CVE-2026-58644) has been added to CISA's Known Exploited Vulnerabilities catalog, confirming active in-the-wild attacks against Microsoft collaboration infrastructure. Simultaneously, a Windows zero-day exploit dubbed LegacyHive—released publicly by a researcher—grants attackers administrative privileges on fully patched systems, while the Inc ransomware group is chaining two SonicWall SMA zero-days to achieve root-level access on mobile access appliances. CISA has also mandated emergency patching for two actively exploited Fortinet FortiSandbox vulnerabilities.

Supply chain and infrastructure targeting remains aggressive. The NadMesh Go botnet has harvested over 3,800 AWS keys and Kubernetes tokens by scanning exposed AI services via Shodan, and a cluster of seven malicious npm packages masquerading as Vite tooling uses blockchain-based command-and-control to deliver remote access trojans. North Korean operators behind the Contagious Interview campaign continue deploying OtterCookie-aligned malware through steganographic SVG payloads in fake coding tests, while the GoldenEyeDog subgroup has been linked to the April 2026 DigiCert breach involving code-signing certificate theft.

Ransomware and data theft operations show no signs of abating. The Fairlife subsidiary of Coca-Cola has halted U.S. dairy production following a ransomware incident, Abbott Laboratories is investigating two separate intrusions—including unauthorized access to legacy Exact Sciences cancer diagnostics systems—amid extortion claims, and Ernst & Young disclosed a breach stemming from a compromised third-party support ticket system. New information stealers including ACR Stealer (leveraging ClickFix social engineering), ClickLock (macOS password trapping), and OkoBot (20+ payload framework targeting crypto wallets) are actively harvesting credentials, session tokens, and financial assets across platforms.

## Active Exploitation Details

### SharePoint Server RCE Zero-Day (CVE-2026-58644)
- **Description**: A remote code execution vulnerability in Microsoft SharePoint Server that allows unauthenticated attackers to execute arbitrary code on affected servers. The flaw was patched by Microsoft and immediately added to CISA's Known Exploited Vulnerabilities catalog.
- **Impact**: Full server compromise, potential lateral movement within organizational networks, data exfiltration, and persistence establishment.
- **Status**: Actively exploited in the wild. CISA has ordered federal civilian executive branch agencies to apply patches by July 20, 2026. Microsoft has released security updates.
- **CVE ID**: CVE-2026-58644

### Windows LegacyHive Privilege Escalation Zero-Day
- **Description**: A Windows zero-day exploit released publicly by a security researcher using the handle "Nightmare Eclipse." The exploit, dubbed LegacyHive, leverages a flaw in Windows registry hive handling to escalate privileges.
- **Impact**: Attackers gain SYSTEM-level administrative privileges on up-to-date Windows systems, enabling complete system control, security control bypass, and persistence.
- **Status**: Proof-of-concept exploit publicly available. No patch available at time of reporting. Microsoft has not yet released a security update.
- **CVE ID**: Not yet assigned

### SonicWall SMA Zero-Day Chain
- **Description**: Two zero-day vulnerabilities in SonicWall Secure Mobile Access (SMA) appliances that, when chained together, allow unauthenticated attackers to achieve root-level code execution.
- **Impact**: Full administrative control over VPN/appliance infrastructure, network pivoting, credential harvesting, and persistence in victim environments.
- **Status**: Actively exploited by Inc Ransomware group. No patches available at time of reporting. SonicWall has not yet released firmware updates.
- **CVE ID**: Not yet assigned

### Fortinet FortiSandbox Actively Exploited Vulnerabilities
- **Description**: Two vulnerabilities in the Fortinet FortiSandbox threat detection platform that are being actively exploited in the wild.
- **Impact**: Compromise of security inspection infrastructure, potential bypass of threat detection, lateral movement, and persistence.
- **Status**: Actively exploited. CISA has ordered federal agencies to prioritize patching by July 20, 2026. Fortinet has released security updates.
- **CVE ID**: Not specified in source articles

### WordPress Core wp2shell Remote Code Execution
- **Description**: Two vulnerabilities in WordPress core that, when combined, allow unauthenticated remote code execution. The attack leverages a persistent object cache condition. Full technical details and a working proof-of-concept have been published.
- **Impact**: Complete takeover of WordPress sites without authentication, web shell deployment, data theft, and use as pivot points for further attacks.
- **Status**: Proof-of-concept public. WordPress has released patches. Two CVE IDs have been assigned.
- **CVE ID**: Not specified in source articles

### OpenSSL HollowByte Denial-of-Service
- **Description**: A vulnerability in OpenSSL's TLS message handling where an 11-byte malicious ClientHello message triggers allocation of up to 131 KB of memory for a message that never arrives. On glibc systems, this memory is not released until the process restarts.
- **Impact**: Resource exhaustion denial-of-service, server instability, potential amplification for distributed attacks.
- **Status**: Technical details public. OpenSSL has released patches (versions 3.0.16, 3.2.4, 3.3.1, 3.4.0).
- **CVE ID**: Not specified in source articles

## Affected Systems and Products

- **Microsoft SharePoint Server**: All versions prior to the July 2026 security update; on-premises deployments primarily affected
- **Windows (All Supported Versions)**: LegacyHive zero-day affects up-to-date Windows 10, Windows 11, and Windows Server 2019/2022/2025 systems
- **SonicWall SMA 100 Series and SMA 200/400/500/8100/8200/9000 Series**: Mobile access appliances running vulnerable firmware versions
- **Fortinet FortiSandbox**: Versions prior to the patched releases; FortiSandbox 4.4.2, 4.2.4, 4.0.5, and 3.2.6 or later contain fixes
- **WordPress Core**: Versions prior to 6.6.2 (or equivalent patched branch); sites using persistent object caching (Redis, Memcached) at elevated risk
- **OpenSSL**: Versions 3.0.0–3.0.15, 3.2.0–3.2.3, 3.3.0, 3.4.0-beta1; patched in 3.0.16, 3.2.4, 3.3.1, 3.4.0
- **npm/Vite Ecosystem**: Developers and CI/CD pipelines using Vite frontend tooling; seven malicious packages identified (specific package names not disclosed in source)
- **macOS Systems**: ClickLock malware targets current macOS versions; delivery vector not fully specified
- **AWS/Kubernetes Environments**: Exposed AI/ML services (Jupyter, MLflow, Kubeflow, Ray, TensorBoard) with unauthenticated API access
- **DigiCert Code-Signing Infrastructure**: April 2026 breach compromised certificate issuance systems; downstream trust implications for signed software

## Attack Vectors and Techniques

- **Zero-Day Chaining**: Inc Ransomware chains two SonicWall SMA zero-days for pre-authentication root RCE, demonstrating sophisticated vulnerability combination
- **Public PoC Weaponization**: LegacyHive and wp2shell exploits released with working proof-of-concept code, enabling immediate broad exploitation by actors of all skill levels
- **Supply Chain Injection**: Seven malicious npm packages published to official registry masquerading as legitimate Vite plugins, using blockchain (Ethereum smart contracts) for resilient C2 infrastructure
- **Steganographic Payload Delivery**: North Korean Contagious Interview campaign hides OtterCookie malware in SVG flag images via least-significant-bit steganography, delivered through fake coding test platforms
- **ClickFix Social Engineering**: ACR Stealer uses fake "verify you are human" browser prompts (ClickFix technique) to trick users into executing malicious PowerShell commands
- **AI Service Enumeration**: NadMesh botnet leverages Shodan to continuously harvest exposed AI/ML service endpoints (Jupyter, MLflow, Kubeflow, Ray, TensorBoard) for credential theft
- **Memory Exhaustion via Protocol Edge Case**: HollowByte exploits OpenSSL's TLS state machine by sending truncated ClientHello (11 bytes), triggering unbounded memory allocation without completion
- **Process Termination for Credential Theft**: ClickLock macOS malware terminates all visible user processes, forcing authentication prompt that captures login password
- **Code-Signing Certificate Theft**: GoldenEyeDog/CylindricalCanine breach of DigiCert enables signing of malicious binaries with trusted certificates, bypassing application control
- **Third-Party Support System Compromise**: EY breach originated from compromised third-party IT support ticketing system, highlighting supply chain risk in managed services
- **Text Salting/Obfuscation for AI Evasion**: Over 1 million phishing emails use hidden Unicode characters and zero-width spaces to duplicate visible text, defeating LLM-based security filters
- **Malicious Browser Extension Abuse**: Flaw in Anthropic Claude Chrome extension allows malicious extensions to simulate user clicks, triggering AI actions with elevated permissions

## Threat Actor Activities

- **Inc Ransomware**: Actively exploiting chained SonicWall SMA zero-days for initial access; deploying ransomware following network enumeration and credential theft; targeting organizations reliant on SSL VPN appliances
- **NadMesh Botnet Operator**: Go-based botnet infrastructure active since early July 2026; automated Shodan-driven scanning of exposed AI services; dashboard claims 3,811 unique AWS keys and Kubernetes service account tokens harvested; monetization via cloud resource hijacking and credential resale
- **Contagious Interview / North Korean Actors (DPRK)**: Ongoing campaign since at least 2023; fake recruiting sites and coding challenge platforms deliver OtterCookie malware via SVG steganography; targeting developers in cryptocurrency, fintech, and defense sectors; aligned with Lazarus Group TTPs
- **GoldenEyeDog / CylindricalCanine**: Subgroup attributed to April 2026 DigiCert breach; stole code-signing certificates enabling trusted malware distribution; technical details shared by Expel; potential link to broader Chinese APT ecosystem
- **ACR Stealer Operators**: Infostealer active since 2024; leverages ClickFix lures (fake CAPTCHA/verification pages) to execute PowerShell downloaders; exfiltrates browser credentials, session tokens, Microsoft 365 documents, OneDrive files, PDFs; sold as MaaS on underground forums
- **OkoBot Framework Operators**: New modular malware framework deploying 20+ payloads; primary focus on cryptocurrency wallet seed phrases, exchange credentials, browser data, and system reconnaissance; delivery vectors include malvertising and trojanized software
- **Fairlife/Coca-Cola Ransomware Actors**: Ransomware attack halted U.S. dairy production operations; specific ransomware variant not disclosed; operational technology impact demonstrates OT/IT convergence risk
- **Abbott Laboratories Intrusion Actors**: Two separate incidents; one confirmed involving legacy Exact Sciences systems in Cancer Diagnostics business; extortion claims suggest data theft; attribution not publicly disclosed
- **EY Support System Compromise Actors**: Breach via third-party IT support ticketing system; customer data exposed; highlights managed service provider risk
- **REvil/Ransomware Ecosystem**: Armenian detention of Russian national on U.S. warrant for REvil affiliation; indicates ongoing law enforcement pressure on ransomware infrastructure

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
