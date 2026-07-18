# Exploitation Report

## Executive Summary

Critical exploitation activity spans multiple high-impact vectors this reporting period. A Microsoft SharePoint Server remote code execution zero-day (CVE-2026-58644) has been added to CISA's Known Exploited Vulnerabilities catalog, confirming active in-the-wild exploitation against on-premises SharePoint deployments. Simultaneously, a WordPress core vulnerability dubbed "wp2shell" enables unauthenticated remote code execution on all WordPress 6.9 and 7.0 installations—including bare-metal deployments with zero plugins—affecting a massive portion of the internet-facing web surface until emergency patches were released.

Ransomware operations continue to leverage zero-day chains for initial access. The Inc Ransomware group is actively exploiting two chained SonicWall SMA zero-day vulnerabilities to achieve root-level compromise of mobile access appliances. CISA has also mandated immediate federal agency patching for two actively exploited Fortinet FortiSandbox flaws. On the endpoint front, a newly disclosed Windows zero-day exploit named "LegacyHive" grants privilege escalation to administrators on fully patched systems, while the OpenSSL "HollowByte" vulnerability permits denial-of-service via a mere 11-byte TLS request that permanently bloats server memory until process restart.

## Active Exploitation Details

### Microsoft SharePoint Server RCE Zero-Day (CVE-2026-58644)
- **Description**: A remote code execution vulnerability in Microsoft SharePoint Server that was exploited as a zero-day before patching. The flaw allows unauthenticated attackers to execute arbitrary code on affected SharePoint servers.
- **Impact**: Full server compromise, potential lateral movement into connected Active Directory environments, data exfiltration, and persistence establishment.
- **Status**: Actively exploited in the wild. Microsoft has released patches. CISA added this vulnerability to the Known Exploited Vulnerabilities (KEV) catalog on July 2026, requiring Federal Civilian Executive Branch agencies to remediate immediately.
- **CVE ID**: CVE-2026-58644

### WordPress Core "wp2shell" Unauthenticated RCE
- **Description**: A critical vulnerability in WordPress core (not a plugin or theme) that allows unauthenticated remote code execution via a single anonymous HTTP request. The flaw exists in the core codebase, meaning a default WordPress installation with zero plugins is exploitable.
- **Impact**: Complete takeover of affected WordPress sites, including arbitrary code execution, database access, file system manipulation, and potential pivot to underlying server infrastructure.
- **Status**: Actively exploitable against all WordPress 6.9 and 7.0 versions until emergency patches were released on Friday (per article timeline). Sites running these versions require immediate updating.
- **CVE ID**: Not explicitly provided in source article

### SonicWall SMA Zero-Day Chain (Inc Ransomware)
- **Description**: Two zero-day vulnerabilities in SonicWall Secure Mobile Access (SMA) appliances that, when chained together, provide threat actors with root-level capabilities on the device.
- **Impact**: Full administrative control over VPN/appliance infrastructure, network traffic interception, credential harvesting, lateral movement into internal networks, and ransomware deployment staging.
- **Status**: Actively exploited by Inc Ransomware group. SonicWall has not yet released patches at time of reporting (zero-day status).
- **CVE ID**: Not explicitly provided in source article

### Fortinet FortiSandbox Actively Exploited Vulnerabilities (Two Flaws)
- **Description**: Two distinct vulnerabilities in the Fortinet FortiSandbox threat detection platform that are confirmed as actively exploited in the wild.
- **Impact**: Compromise of threat detection infrastructure, potential bypass of security controls, persistence in security management plane, and supply chain risk to connected Fortinet ecosystem.
- **Status**: Actively exploited. CISA issued emergency directive ordering Federal Civilian Executive Branch agencies to prioritize patching by Sunday (per article timeline).
- **CVE ID**: Not explicitly provided in source article

### Windows "LegacyHive" Zero-Day Privilege Escalation
- **Description**: A Windows zero-day exploit released by security researcher "Nightmare Eclipse" that enables local privilege escalation to administrator/system privileges on up-to-date Windows systems.
- **Impact**: Full administrative control over compromised endpoints, bypass of security controls, credential theft, and facilitation of lateral movement.
- **Status**: Public exploit code available (zero-day). No patch available at time of reporting. Actively usable by any threat actor with initial foothold.
- **CVE ID**: Not explicitly provided in source article

### OpenSSL "HollowByte" Denial-of-Service
- **Description**: A vulnerability in OpenSSL where an 11-byte malicious TLS ClientHello message causes the server to allocate up to 131 KB of memory for a message that never arrives. On glibc systems, this memory is never released until the process restarts.
- **Impact**: Resource exhaustion denial-of-service. Repeated exploitation rapidly depletes server memory, causing service degradation or crash. Low-bandwidth, high-impact DoS vector.
- **Status**: Vulnerability disclosed with technical details. Patches expected from OpenSSL project. No active exploitation reported yet, but exploitability is trivial.
- **CVE ID**: Not explicitly provided in source articles

### Anthropic Claude Chrome Extension Flaw
- **Description**: A flaw in the Claude for Chrome browser extension that allows malicious extensions to simulate user clicks and trigger predefined AI actions, potentially abusing Claude's access to browser content and APIs.
- **Impact**: Unauthorized AI actions, potential data exfiltration via Claude's access to page content, session hijacking, and privilege escalation within browser context.
- **Status**: Vulnerability disclosed. Patch status unclear from reporting.
- **CVE ID**: Not explicitly provided in source article

## Affected Systems and Products

- **Microsoft SharePoint Server**: On-premises SharePoint Server versions affected by CVE-2026-58644 (specific versions not detailed in source)
- **WordPress Core**: Versions 6.9 and 7.0 (all installations, including bare-metal with zero plugins)
- **SonicWall Secure Mobile Access (SMA) Appliances**: Vulnerable firmware versions (specific versions not disclosed due to zero-day status)
- **Fortinet FortiSandbox**: Threat detection platform appliances (specific versions not detailed in source)
- **Windows**: Up-to-date Windows systems vulnerable to LegacyHive privilege escalation (specific versions/architectures not detailed)
- **OpenSSL**: Server implementations using vulnerable OpenSSL versions on glibc-based systems (specific version range not detailed)
- **Anthropic Claude for Chrome Extension**: Extension versions containing the click-simulation flaw
- **Exact Sciences Legacy Systems**: Legacy systems within Abbott Laboratories' Cancer Diagnostics business (compromised in breach)
- **Ernst & Young Third-Party Support Ticket System**: Compromised support platform used by IT personnel
- **Fairlife/Coca-Cola Production Systems**: Ransomware-impacted operational technology/production environments
- **Vite/npm Ecosystem**: Developers and CI/CD pipelines that installed any of the seven malicious npm packages

## Attack Vectors and Techniques

- **Unauthenticated HTTP RCE (wp2shell)**: Single anonymous HTTP request achieves remote code execution on WordPress core without authentication, plugins, or user interaction.
- **Zero-Day Chaining (SonicWall SMA)**: Two distinct zero-day vulnerabilities chained to escalate from initial access to root-level appliance compromise.
- **Privilege Escalation via LegacyHive**: Local exploit leveraging Windows legacy hive handling to achieve SYSTEM/admin privileges from standard user context.
- **Resource Exhaustion DoS (HollowByte)**: 11-byte TLS ClientHello triggers unbounded memory allocation per connection, exhausting server RAM with minimal bandwidth.
- **ClickFix Social Engineering (ACR Stealer)**: Fake browser error pages or verification prompts trick users into executing malicious PowerShell commands via clipboard manipulation.
- **Steganographic Payload Delivery (Contagious Interview)**: Malicious code hidden within SVG flag images delivered through fake coding test platforms targeting developers.
- **Blockchain-Based C2 (Vite npm Supply Chain)**: Malicious npm packages use blockchain transactions for command-and-control infrastructure, evading traditional domain/IP blocking.
- **AI Service Enumeration (NadMesh Botnet)**: Automated Shodan-driven scanning for exposed AI/ML services (APIs, notebooks, model endpoints) to harvest cloud credentials and Kubernetes tokens.
- **Code-Signing Certificate Theft (GoldenEyeDog/DigiCert)**: Breach of certificate authority infrastructure to steal valid code-signing certificates for malware signing and trust abuse.
- **Residential Proxy Rotation (Carding Operations)**: Cybercriminals sourcing "clean" residential proxies combined with browser fingerprint spoofing to evade fraud detection during carding.
- **Process Termination Credential Phishing (ClickLock macOS)**: Malware terminates all visible user processes, forcing victim to enter system password to regain control, capturing credentials.
- **Multi-Payload Framework Deployment (OkoBot)**: Modular framework delivering 20+ specialized payloads for credential theft, crypto wallet seed extraction, and data exfiltration.
- **Text Salting/Invisible Character Injection (AI Filter Bypass)**: Phishing emails use hidden Unicode characters to manipulate LLM-based security filters while rendering normally to humans.
- **Third-Party Support System Compromise (EY Breach)**: Attackers target IT support ticketing platforms to gain privileged access to managed environments.
- **Legacy System Exploitation (Abbott/Exact Sciences)**: Unauthorized access to outdated, poorly segmented legacy systems in healthcare diagnostics environment.

## Threat Actor Activities

- **Inc Ransomware Group**: Actively exploiting SonicWall SMA zero-day chain for initial access to corporate networks, deploying ransomware after achieving root on VPN appliances.
- **GoldenEyeDog Subgroup (CylindricalCanine Cluster)**: Attributed to April 2026 DigiCert breach resulting in code-signing certificate theft. Technical details shared by Expel researchers.
- **Contagious Interview Campaign (North Korea-Linked)**: Ongoing campaign using fake job interviews and coding tests to deliver OtterCookie-aligned malware via SVG steganography targeting developers and software engineers.
- **NadMesh Botnet Operator**: Go-based botnet actively scanning for exposed AI services since early July 2026. Operator dashboard claims 3,811 unique AWS keys harvested. Uses Shodan for continuous target enumeration.
- **ACR Stealer Operators**: Infostealer active since 2024, now leveraging ClickFix lures to extract browser passwords, live session tokens, PDFs, Microsoft 365 documents, and OneDrive-synced files from enterprise networks.
- **GoSerpent Malware Operators**: Previously undocumented malware targeting Southeast Asian governments and diplomats since late 2025 for espionage. Go-based, custom toolset.
- **REvil Ransomware Affiliates**: Aleksandr Ermakov detained in Armenia on U.S. extradition warrant for REvil activities (identity contested by defense).
- **OkoBot Framework Operators**: Deploying 20+ payload framework focused on cryptocurrency wallet seed phrases, credentials, and sensitive data theft.
- **Fairlife/Coca-Cola Ransomware Actors**: Unidentified ransomware group disrupted Fairlife dairy production across United States, halting operations.
- **Investment Fraud Money Laundering Network**: New York-based individuals charged with laundering $43 million from cyber-enabled investment fraud scams.

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
