# Exploitation Report

## Executive Summary

A significant supply chain compromise has impacted WordPress plugin vendor BdThemes, where threat actors poisoned a remote JSON feed delivered to administrators' browsers to create rogue administrative accounts across potentially thousands of WordPress sites. This attack demonstrates the growing risk of supply chain targeting against widely deployed CMS ecosystems and the effectiveness of client-side code injection via compromised configuration files.

Critical infrastructure remains under sustained assault, with confirmed breaches of a Polish heat-and-power plant serving 50,000 residents via private APN access to operational technology networks, and expanding attacks against Internet-exposed PLCs in water systems across at least a dozen U.S. states with suspected Iranian involvement. Simultaneously, ransomware operators are actively exploiting recently patched vulnerabilities in SonicWall SMA1000 appliances and Progress Kemp LoadMaster devices, while the Head Mare hacktivist group continues weaponizing TrueConf server flaws to trojanize client installers with the PhantomCore backdoor.

A maximum-severity zero-day in Metabase business intelligence software is being exploited in the wild without authentication to achieve remote administrator access, though no CVE has been assigned yet. Meanwhile, sophisticated iOS exploit chains (Coruna and DarkSword) previously limited to nation-state actors are proliferating to organized cybercrime groups, and China-linked threat actor Storm-1175 has deployed the new StormEncryptor ransomware strain, likely leveraging an N-central vulnerability. North Korea's Kimsuky group has operationalized an offline AI stack to enhance phishing and automate malware development, signaling a maturation in AI-assisted offensive capabilities.

## Active Exploitation Details

### BdThemes Supply Chain Attack
- **Description**: Threat actors compromised the upstream infrastructure of BdThemes, a developer of premium WordPress web-design tools, and modified a remote JSON configuration feed delivered to administrators' browsers. The poisoned JSON executed malicious JavaScript in admin contexts to create rogue WordPress administrator accounts.
- **Impact**: Attackers gain persistent administrative access to WordPress sites using BdThemes plugins, enabling full site takeover, data exfiltration, malware distribution, and further supply chain propagation.
- **Status**: Actively exploited in the wild. WordPress.org plugins team temporarily disabled BdThemes plugins. Users must update to clean versions and audit for unauthorized admin accounts.
- **CVE ID**: None assigned in available reporting

### Metabase Zero-Day (Pre-Auth Remote Admin Access)
- **Description**: A maximum-severity security flaw in Metabase business intelligence and data visualization software allows unauthenticated remote attackers to achieve full administrator access to the platform and its downstream users.
- **Impact**: Complete compromise of Metabase instances, access to all connected databases and sensitive business data, potential lateral movement to connected systems.
- **Status**: Actively exploited in the wild as a zero-day. No CVE assigned yet. Metabase has issued warnings but patch availability unclear from reporting.
- **CVE ID**: None assigned (explicitly noted as having no CVE)

### SonicWall SMA1000 Vulnerabilities
- **Description**: Two recently patched vulnerabilities in SonicWall SMA1000 series appliances, including a maximum-severity server-side request forgery (SSRF) flaw.
- **Impact**: Ransomware gangs are exploiting these flaws to gain initial access to corporate networks for ransomware deployment.
- **Status**: Actively exploited by ransomware gangs per CISA confirmation. Patches available but exploitation ongoing against unpatched systems.
- **CVE ID**: Not provided in source articles

### Progress Kemp LoadMaster Command Injection
- **Description**: A critical-severity command injection vulnerability in Progress Kemp LoadMaster load balancing appliances.
- **Impact**: Unauthenticated remote code execution leading to full appliance compromise, network pivoting, and potential data theft.
- **Status**: Actively exploited in attacks per CISA warning. Patches available but exploitation confirmed against unpatched instances.
- **CVE ID**: Not provided in source articles

### TrueConf Server Flaws (PhantomCore Campaign)
- **Description**: Head Mare threat actor exploiting security flaws in unpatched TrueConf video conferencing servers to replace legitimate client installers with malicious versions delivering the PhantomCore backdoor.
- **Impact**: Supply chain compromise of TrueConf clients, persistent backdoor access to victim organizations (primarily Russian instrumentation, electronics, and industrial companies), credential theft, and lateral movement.
- **Status**: Actively exploited. TrueConf servers remain vulnerable if unpatched. Campaign ongoing against Russian entities.
- **CVE ID**: Not provided in source articles

### N-central Flaw (StormEncryptor Ransomware Vector)
- **Description**: A vulnerability in N-central (likely N-able N-central RMM platform) being leveraged by China-linked threat actor Storm-1175 to deploy the previously undocumented StormEncryptor ransomware strain.
- **Impact**: Ransomware deployment across managed service provider clients, data encryption, exfiltration, and operational disruption.
- **Status**: Active exploitation by Storm-1175. Patch status of N-central flaw unclear from reporting.
- **CVE ID**: Not provided in source articles

### Coruna and DarkSword iOS Exploit Chains
- **Description**: Sophisticated iPhone exploit chains previously limited to nation-state operations are now proliferating to organized cybercrime groups globally.
- **Impact**: Full device compromise, surveillance, data exfiltration, and persistence on iOS devices without user interaction (likely zero-click or one-click chains).
- **Status**: Actively exploited and spreading beyond nation-state actors to cybercrime groups. Patch status depends on iOS version.
- **CVE ID**: Not provided in source articles

### Solidity Pro VS Code Extension (Malicious Package)
- **Description**: A malicious Microsoft Visual Studio Code extension named "Solidity Pro" (solidity-pro) distributed via the VS Code Marketplace that delivers a browser wallet and credential stealer.
- **Impact**: Theft of cryptocurrency wallets, API keys, credentials, and other sensitive data from developers' environments.
- **Status**: Active in the wild. Extension flagged by researchers; removal status from marketplace unclear.
- **CVE ID**: Not applicable (supply chain / malicious package)

### Atlassian Rovo Data Exfiltration
- **Description**: Attacker-controlled instructions can manipulate Atlassian's Rovo AI assistant to collect Jira or Confluence data accessible to a signed-in user and exfiltrate it to an external server.
- **Impact**: Unauthorized access to sensitive project data, credentials, and internal documentation across Jira and Confluence instances.
- **Status**: Vulnerability demonstrated by two security firms. Patch/mitigation status unclear from reporting.
- **CVE ID**: Not provided in source articles

### CSS-Based Webmail Attacks
- **Description**: Novel CSS injection techniques allowing email content to escape message boundaries and interfere with webmail interfaces across Outlook, Gmail, Fastmail, Proton Mail, Yahoo Mail, and others.
- **Impact**: Credential theft, authentication token exfiltration, and potential account takeover via phishing-resistant MFA bypass.
- **Status**: Demonstrated in research; real-world exploitation status unclear but technique is viable across major webmail providers.
- **CVE ID**: Not applicable (technique/class of vulnerability)

### Polish Energy Plant OT Breach via Private APN
- **Description**: Hackers breached a heat-and-power plant facility in Poland supplying heat to ~50,000 residents by using a private Access Point Name (APN) to access the operational technology (OT) network.
- **Impact**: Unauthorized access to OT systems controlling critical heating infrastructure, potential for physical disruption of heat supply.
- **Status**: Breach occurred "last year" per reporting; discovery and attribution details limited.
- **CVE ID**: Not applicable (network architecture abuse)

### Multistate Water System Attacks (Iran-Suspected)
- **Description**: Attacks targeting water and wastewater systems across a dozen U.S. states, exploiting ill-secured, Internet-exposed programmable logic controllers (PLCs).
- **Impact**: Potential manipulation of water treatment processes, service disruption for communities, erosion of critical infrastructure trust.
- **Status**: Ongoing and widening campaign. Suspected Iranian state-sponsored activity. Mitigation requires removing PLCs from Internet exposure.
- **CVE ID**: Not applicable (misconfiguration/exposure exploitation)

### GhostJacking (AI Agent Hijacking)
- **Description**: Attack technique using security alerts and blocked events to manipulate and hijack AI agents, exposing identity governance gaps in autonomous AI systems.
- **Impact**: Unauthorized AI agent actions, potential data access, privilege escalation, and autonomous malicious activity.
- **Status**: Demonstrated in research; represents emerging threat class as AI agents gain more autonomy.
- **CVE ID**: Not applicable (technique/class of vulnerability)

### Passkey Attacks (Synced Key Recovery & MFA Bypass)
- **Description**: Three separate research efforts demonstrating ways to defeat passkey protections without breaking underlying cryptography, including recovery of synced private keys and bypass of phishing-resistant MFA.
- **Impact**: Undermines trust in passkey-based authentication, potential account takeover even with phishing-resistant MFA.
- **Status**: Research demonstrations; real-world exploitation not confirmed but techniques are practical.
- **CVE ID**: Not applicable (protocol/implementation weaknesses)

## Affected Systems and Products

- **BdThemes WordPress Plugins**: Premium web-design tools for WordPress; all versions receiving the poisoned JSON feed; WordPress.org temporarily disabled the plugins
- **Metabase Business Intelligence Platform**: Open-source and enterprise editions; all unpatched versions vulnerable to pre-auth admin takeover
- **SonicWall SMA1000 Series Appliances**: Secure mobile access appliances; unpatched versions vulnerable to SSRF and additional flaw exploited by ransomware gangs
- **Progress Kemp LoadMaster**: Load balancing appliances (virtual and hardware); unpatched versions vulnerable to critical command injection
- **TrueConf Video Conferencing Server**: On-premises video conferencing solution; unpatched servers exploited to trojanize client installers
- **N-able N-central (Likely)**: Remote monitoring and management platform; vulnerability exploited by Storm-1175 for StormEncryptor deployment
- **Apple iOS Devices**: iPhones and iPads vulnerable to Coruna and DarkSword exploit chains; specific version ranges not disclosed in reporting
- **Microsoft Visual Studio Code**: Extensions marketplace; Solidity Pro (solidity-pro) malicious extension targeting cryptocurrency/Web3 developers
- **Atlassian Rovo / Jira / Confluence**: Cloud and potentially Data Center editions; Rovo AI assistant vulnerable to prompt injection data exfiltration
- **Major Webmail Providers**: Outlook, Gmail, Fastmail, Proton Mail, Yahoo Mail; all demonstrated vulnerable to CSS injection boundary escape attacks
- **Polish Heat-and-Power Plant OT Systems**: Industrial control systems accessible via private APN; specific PLC/SCADA platforms not identified
- **U.S. Water/Wastewater PLCs**: Internet-exposed programmable logic controllers across multiple vendors; specific models not identified
- **AI Agent Platforms**: Systems deploying autonomous AI agents with identity governance gaps; specific platforms not named in GhostJacking research
- **Passkey/FIDO2 Implementations**: Syncing implementations (iCloud Keychain, Google Password Manager, etc.) and phishing-resistant MFA flows

## Attack Vectors and Techniques

- **Supply Chain Compromise (Upstream Infrastructure)**: Attackers compromise vendor build/distribution infrastructure to inject malicious code into legitimate software updates or configuration feeds (BdThemes JSON, TrueConf installers, Solidity Pro VS Code extension)
- **Client-Side Code Injection via Poisoned Configuration**: Malicious JSON feed executed in administrator browser context to create rogue admin accounts (BdThemes)
- **Pre-Authentication Remote Code Execution / Admin Bypass**: Zero-day flaws allowing unauthenticated attackers to achieve administrative access (Metabase, LoadMaster command injection)
- **SSRF to Internal Network Access**: Server-side request forgery exploited to reach internal services and pivot (SonicWall SMA1000)
- **RMM/RMM-Like Platform Exploitation**: Targeting remote monitoring and management tools to deploy ransomware at scale across MSP clients (N-central / StormEncryptor)
- **Private APN / Cellular Network Pivot**: Using dedicated cellular connections (private APN) to bypass perimeter defenses and directly access OT networks (Polish energy plant)
- **Internet-Exposed OT/ICS Device Targeting**: Scanning for and exploiting PLCs and industrial controllers directly connected to the Internet (water systems)
- **Prompt Injection / AI Agent Manipulation**: Crafting malicious instructions to hijack AI assistant behavior for data exfiltration (Atlassian Rovo, GhostJacking)
- **CSS Injection / Style-Based Exfiltration**: Abusing CSS parsing to escape email sandbox boundaries and steal credentials/tokens from webmail UI (cross-provider webmail attacks)
- **Zero-Click / One-Click iOS Exploit Chains**: Sophisticated exploit chains targeting iOS Safari, iMessage, or other attack surfaces for silent compromise (Coruna, DarkSword)
- **Offline AI Model Operationalization**: Threat actors deploying local LLMs for phishing content generation, malware development automation, and social engineering at scale (Kimsuky)
- **Passkey Sync Key Recovery**: Exploiting cloud sync mechanisms (iCloud, Google) to extract synced private keys or bypass phishing-resistant authentication flows
- **Trojanized Legitimate Installers**: Replacing authentic client software with backdoored versions on compromised vendor servers (TrueConf / PhantomCore)
- **Ransomware Deployment via Vulnerability Chaining**: Using unpatched edge/remote access appliances as initial access for ransomware (SonicWall, LoadMaster, N-central)

## Threat Actor Activities

- **Head Mare (Hacktivist Group)**: Actively exploiting unpatched TrueConf servers to replace client installers with PhantomCore backdoor; targeting Russian companies in instrumentation, electronics, and industrial sectors; repeated campaigns against same vendor
- **Storm-1175 (China-Linked, Financially Motivated)**: Deploying new StormEncryptor ransomware strain; likely leveraging N-central vulnerability for initial access; previously associated with other ransomware operations; Microsoft-tracked actor
- **Kimsuky / APT43 (North Korea State-Sponsored)**: Building and operating offline AI stack on own infrastructure to enhance phishing campaigns and automate malware development; moving beyond public LLM APIs for operational security
- **Iranian State-Sponsored Actors (Suspected)**: Conducting widespread attacks against U.S. water and wastewater systems via Internet-exposed PLCs; campaign spanning at least a dozen states; ongoing and widening
- **Ransomware Gangs (Multiple, Unnamed)**: Actively exploiting SonicWall SMA1000 and Progress LoadMaster vulnerabilities for initial access; per CISA confirmation, multiple gangs involved
- **Former Medusa Affiliate (Financially Motivated)**: Operating new StormEncryptor ransomware; connection to Storm-1175 deployment suggests possible collaboration or shared infrastructure
- **The Com (Cybercrime Collective)**: Loose-knit group targeting children and teenagers for blackmail and sextortion; one member sentenced to two years for offenses against ~120 victims
- **Unknown / Unattributed Actors**: Polish energy plant breach via private APN; BdThemes supply chain compromise; Metabase zero-day exploitation; Solidity Pro malicious extension publisher

## Source Attribution

- **BdThemes Supply Chain Attack Poisons JSON to Create Rogue WordPress Admins**: The Hacker News - https://thehackernews.com/2026/08/bdthemes-supply-chain-attack-poisons.html
- **Hackers breached a small Polish energy plant via private APN last year**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hackers-breached-a-small-polish-energy-plant-via-private-apn-last-year/
- **'GhostJacking' Exposes Identity Governance Gaps in AI Agents**: Dark Reading - https://www.darkreading.com/cyber-risk/ghostjacking-identity-governance-gaps-ai-agents
- **Multistate Water System Attacks Widen, Iran Suspected**: Dark Reading - https://www.darkreading.com/ics-ot-security/multistate-water-system-attacks-widen-iran-suspected
- **BdThemes plugins supply-chain hack creates rogue WordPress admins**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/bdthemes-plugins-supply-chain-hack-creates-rogue-wordpress-admins/
- **Metabase SQL Zero-Day Attacks Could Have Wide Blast Radius**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/metabase-sql-zero-day-attacks-wide-blast-radius
- **OpenAI releases ChatGPT 5.6 Cyber, but it's only for approved users**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/openai-releases-chatgpt-56-cyber-but-its-only-for-approved-users/
- **The Patch Gap: Why Defenders Need to Think in Chains, Not Checklists**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/patch-gap-defenders-chains-not-checklists
- **New StormEncryptor ransomware used by former Medusa affiliate**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-stormencryptor-ransomware-used-by-former-medusa-affiliate/
- **Shipping 10–50× More Code? Watch This Webinar on Securing AI-Speed Development**: The Hacker News - https://thehackernews.com/2026/08/shipping-1050-more-code-watch-this.html
- **Coruna, DarkSword iOS Exploits Proliferate Globally**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/coruna-darksword-ios-exploits-proliferate-globally
- **China-Linked Hackers Deploy New StormEncryptor Ransomware, Likely via N-central Flaw**: The Hacker News - https://thehackernews.com/2026/08/china-linked-hackers-deploy-new.html
- **Outdated Cybercrime Laws Put Security Researchers at Risk**: Dark Reading - https://www.darkreading.com/application-security/outdated-cybercrime-laws-security-researchers-risk
- **Sherlock Holmes was the “OG” Social Engineer**: Dark Reading - https://www.darkreading.com/cyber-risk/sherlock-holmes-was-the-og-social-engineer
- **⚡ Weekly Recap: AI Goes Rogue, Metabase 0-Day, MCP Supply-Chain Attacks, and Router Backdoors**: The Hacker News - https://thehackernews.com/2026/08/weekly-recap-ai-goes-rogue-metabase-0.html
- **CISA: SonicWall SMA1000 flaws now exploited by ransomware gangs**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-sonicwall-sma1000-flaws-now-exploited-by-ransomware-gangs/
- **When Credentials Are No Longer Enough: Device Trust in the AI Era**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/when-credentials-are-no-longer-enough-device-trust-in-the-ai-era/
- **Kimsuky Builds Offline AI Stack to Boost Phishing and Automate Malware Development**: The Hacker News - https://thehackernews.com/2026/08/kimsuky-builds-offline-ai-stack-that.html
- **Member of The Com sent to prison for blackmail, sextortion**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/member-of-the-com-sent-to-prison-for-blackmail-sextortion/
- **New Passkey Attacks Can Recover Synced Private Keys or Bypass Phishing-Resistant MFA**: The Hacker News - https://thehackernews.com/2026/08/new-passkey-attacks-can-recover-synced.html
- **LexisNexis shuts down services after suspicious activity on servers**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/lexisnexis-shuts-down-services-after-suspicious-activity-on-servers/
- **Valve notifies Steam hardware customers of a data breach**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/valve-notifies-steam-hardware-customers-of-a-data-breach/
- **TrueConf Server Flaws Exploited to Replace Client Installers with PhantomCore**: The Hacker News - https://thehackernews.com/2026/08/head-mare-exploits-trueconf-flaws-to.html
- **Critical Progress LoadMaster flaw now actively exploited in attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-warns-of-critical-progress-loadmaster-flaw-exploited-in-attacks/
- **Solidity Pro VS Code Extensions Steal Crypto Wallets, API Keys, and Credentials**: The Hacker News - https://thehackernews.com/2026/08/solidity-pro-vs-code-extensions-steal.html
- **OpenAI's Next AI Model Astra Shows Cyber Performance Strong Enough to Trigger Pause**: The Hacker News - https://thehackernews.com/2026/08/openais-next-ai-model-astra-shows-cyber.html
- **Hackers breach TrueConf to trojanize client installers with backdoors**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hackers-breach-trueconf-to-trojanize-client-installers-with-backdoors/
- **Atlassian Rovo Can Be Tricked Into Sending Jira and Confluence Data to Attackers**: The Hacker News - https://thehackernews.com/2026/08/atlassian-rovo-can-be-tricked-into.html
- **New CSS Attacks Can Break Webmail Defenses to Steal Passwords and Tokens**: The Hacker News - https://thehackernews.com/2026/08/new-css-attacks-can-break-webmail.html
- **Metabase Zero-Day Exploited in Wild Allows Admin Access Without Authentication**: The Hacker News - https://thehackernews.com/2026/08/metabase-zero-day-exploited-in-wild.html
