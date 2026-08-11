# Exploitation Report

## Executive Summary

A surge in supply chain compromises and zero-day exploitation dominates the current threat landscape. The BdThemes supply chain attack demonstrates how attackers can weaponize trusted plugin update mechanisms to inject malicious JSON payloads, creating rogue administrator accounts across WordPress installations. Simultaneously, a maximum-severity zero-day in Metabase business intelligence software is being actively exploited in the wild to achieve unauthenticated administrative access, with no CVE assigned and no patch yet available. These incidents highlight the growing risk of upstream software supply chain manipulation and the danger of exposed management interfaces.

Critical infrastructure remains a primary target, with confirmed breaches of a Polish heat-and-power plant via private APN access to operational technology networks and expanding attacks against internet-exposed PLCs in water systems across a dozen U.S. states—Iran is suspected in the latter campaign. Ransomware operators have rapidly adopted recently patched vulnerabilities in SonicWall SMA1000 appliances (including a critical SSRF flaw) and Progress Kemp LoadMaster command injection vulnerabilities, with CISA confirming active exploitation by multiple ransomware gangs. The Head Mare hacktivist group continues exploiting unpatched TrueConf video conferencing servers to trojanize client installers with the PhantomCore backdoor, targeting Russian instrumentation and electronics firms.

Threat actors are advancing their tooling and tradecraft at pace. North Korea's Kimsuky has deployed an offline AI stack to automate phishing and malware development, while China-linked Storm-1175 (a former Medusa ransomware affiliate) has introduced the new StormEncryptor strain, likely delivered via an N-central flaw. Research into "GhostJacking" reveals identity governance gaps allowing attackers to hijack AI agents through manipulated security alerts, and novel CSS-based attacks are breaking webmail defenses to extract passwords and tokens. Meanwhile, malicious VS Code extensions masquerading as Solidity development tools are stealing cryptocurrency wallets and API keys, signaling a rise in developer-targeted supply chain threats.

## Active Exploitation Details

### BdThemes Supply Chain Attack
- **Description**: Threat actors compromised the upstream infrastructure of BdThemes, a premium WordPress web-design tool developer, and modified a remote JSON feed delivered to administrators' browsers. The poisoned JSON creates rogue WordPress administrator accounts when plugin update checks are performed.
- **Impact**: Attackers gain persistent administrative access to any WordPress site using affected BdThemes plugins, enabling full site takeover, data theft, malware distribution, and further supply chain propagation.
- **Status**: Actively exploited. WordPress.org plugins team temporarily disabled BdThemes plugins. Users must remove compromised plugins and audit for unauthorized admin accounts.
- **CVE ID**: No CVE assigned in reporting

### Metabase Zero-Day (Pre-Auth Admin Access)
- **Description**: A maximum-severity security flaw in Metabase business intelligence and data visualization software allows unauthenticated remote attackers to achieve administrative access. The vulnerability is being exploited in the wild as a zero-day.
- **Impact**: Full administrative control over Metabase instances, access to all connected databases and sensitive business data, potential lateral movement to downstream systems and users.
- **Status**: Actively exploited as zero-day. No patch available at time of reporting. Metabase has issued warnings but no CVE has been assigned.
- **CVE ID**: No CVE assigned (explicitly stated as having no CVE)

### SonicWall SMA1000 Vulnerabilities
- **Description**: Two recently patched vulnerabilities in SonicWall SMA1000 series appliances, including a maximum-severity server-side request forgery (SSRF) flaw, are being actively exploited by ransomware gangs.
- **Impact**: Remote code execution, unauthenticated access to internal networks, deployment of ransomware payloads, data exfiltration, and persistence establishment.
- **Status**: Actively exploited by multiple ransomware groups. CISA has added these to the Known Exploited Vulnerabilities catalog. Patches available; immediate application urged.
- **CVE ID**: No specific CVE IDs provided in source articles

### Progress Kemp LoadMaster Command Injection
- **Description**: A critical-severity command injection vulnerability in Progress Kemp LoadMaster application delivery controllers allows unauthenticated attackers to execute arbitrary commands on the underlying operating system.
- **Impact**: Full system compromise, network pivoting, credential harvesting, deployment of additional malware, and disruption of load balancing services.
- **Status**: Actively exploited in attacks. CISA has issued a warning and added to Known Exploited Vulnerabilities catalog. Patches available from Progress Software.
- **CVE ID**: No specific CVE ID provided in source articles

### TrueConf Server Flaws (PhantomCore Campaign)
- **Description**: The Head Mare threat actor is weaponizing security flaws in unpatched TrueConf video conferencing servers to breach infrastructure and replace legitimate client installers with malicious versions delivering the PhantomCore backdoor.
- **Impact**: Supply chain compromise of TrueConf clients, persistent backdoor access to victim networks, data theft, and potential lateral movement. Targets Russian companies in instrumentation, electronics, and related sectors.
- **Status**: Actively exploited. TrueConf has released patches; administrators must update servers and verify installer integrity.
- **CVE ID**: No specific CVE IDs provided in source articles

### N-central Flaw (StormEncryptor Delivery)
- **Description**: China-linked threat actor Storm-1175 is deploying the previously undocumented StormEncryptor ransomware, likely exploiting a vulnerability in N-central remote monitoring and management software.
- **Impact**: Ransomware encryption, data exfiltration for double extortion, disruption of managed service provider operations and their downstream clients.
- **Status**: Active deployment observed. Microsoft attributes to Storm-1175 (financially motivated, China-linked). Patch status for N-central flaw not specified in reporting.
- **CVE ID**: No specific CVE ID provided in source articles

### Internet-Exposed PLC Attacks (Water Systems)
- **Description**: Attackers are targeting ill-secured, internet-exposed programmable logic controllers (PLCs) across water and wastewater systems in approximately a dozen U.S. states.
- **Impact**: Potential manipulation of water treatment processes, service disruption to residents, physical damage to equipment, and public health risks.
- **Status**: Ongoing campaign widening across multiple states. Iran suspected as the responsible nation-state actor. CISA and FBI have issued advisories on securing OT/ICS assets.
- **CVE ID**: No specific CVE IDs provided; exploitation leverages misconfiguration and exposure rather than software flaws

### Polish Energy Plant Breach via Private APN
- **Description**: Hackers breached a heat-and-power plant in Poland supplying heat to ~50,000 residents by using a private Access Point Name (APN) to directly access the operational technology (OT) network.
- **Impact**: Unauthorized access to OT/ICS environment, potential for physical process manipulation, service disruption to critical heating infrastructure.
- **Status**: Breach occurred "last year" per reporting; details emerging now. Highlights risks of private APN configurations and insufficient OT network segmentation.
- **CVE ID**: No CVE applicable; exploitation of network architecture weakness

### Coruna and DarkSword iOS Exploit Chains
- **Description**: Sophisticated iPhone exploit chains (Coruna and DarkSword), previously limited to nation-state operations, are proliferating to organized cybercrime groups globally.
- **Impact**: Full device compromise, data extraction, surveillance capabilities, persistence across reboots, and potential deployment of additional spyware.
- **Status**: Active proliferation observed. Exploit chains targeting iOS versions; Apple has likely patched underlying vulnerabilities but widespread deployment to criminal groups increases mass exploitation risk.
- **CVE ID**: No specific CVE IDs provided in source articles

### Atlassian Rovo Data Exfiltration
- **Description**: Attacker-controlled instructions can trick Atlassian's Rovo AI assistant into collecting Jira or Confluence data accessible to a signed-in user and sending it to an external server.
- **Impact**: Unauthorized access to sensitive project data, credentials, internal documentation, and proprietary information stored in Atlassian ecosystems.
- **Status**: Vulnerability demonstrated by two security firms. Exploitation requires user interaction with malicious content. Atlassian remediation status not specified.
- **CVE ID**: No specific CVE ID provided in source articles

### CSS-Based Webmail Attacks
- **Description**: Novel CSS injection techniques allow email content to escape message boundaries and interfere with webmail interfaces across Outlook, Gmail, Fastmail, Proton Mail, Yahoo Mail, and others, enabling theft of passwords and authentication tokens.
- **Impact**: Credential harvesting, session hijacking, bypass of phishing-resistant MFA, account takeover across major webmail providers.
- **Status**: Research demonstrations; real-world exploitation potential high due to broad platform impact. Browser and webmail vendor mitigations in progress.
- **CVE ID**: No specific CVE IDs provided in source articles

### GhostJacking (AI Agent Hijacking)
- **Description**: Attackers manipulate security alerts and blocked events to hijack AI agents, exploiting identity governance gaps in autonomous AI systems.
- **Impact**: Unauthorized AI agent actions, data exfiltration, privilege escalation, and potential automation of malicious workflows under the guise of legitimate AI operations.
- **Status**: Research demonstration of novel attack class. No confirmed wild exploitation reported, but represents emerging threat vector as AI agent adoption grows.
- **CVE ID**: No CVE applicable; architectural/design vulnerability class

### Malicious VS Code Extension (Solidity Pro)
- **Description**: A malicious Visual Studio Code extension named "Solidity Pro" (solidity-pro) delivers a browser wallet and credential stealer targeting cryptocurrency developers.
- **Impact**: Theft of cryptocurrency wallets, API keys, credentials, and sensitive development artifacts. Supply chain compromise of developer tooling.
- **Status**: Actively distributed via VS Code Marketplace. Microsoft has been notified; extension removal and user cleanup required.
- **CVE ID**: No CVE applicable; malicious software distribution

### Passkey Bypass Attacks
- **Description**: Three independent research efforts demonstrated methods to defeat passkey protections without breaking underlying cryptography, including recovery of synced private keys and bypass of phishing-resistant MFA.
- **Impact**: Undermines primary authentication security control, enables account takeover even with FIDO2/WebAuthn credentials, potential for large-scale credential compromise.
- **Status**: Research demonstrations; proof-of-concept level. Highlights implementation and ecosystem weaknesses rather than protocol flaws.
- **CVE ID**: No specific CVE IDs provided in source articles

## Affected Systems and Products

- **BdThemes WordPress Plugins**: Premium web-design plugins for WordPress; all versions that fetch the compromised JSON feed. Platform: WordPress CMS installations using BdThemes products.
- **Metabase Business Intelligence Platform**: All unpatched versions of Metabase BI and data visualization software. Platform: Linux, Windows, Docker, and cloud deployments (AWS, Azure, GCP).
- **SonicWall SMA1000 Series**: SMA 1000 series secure mobile access appliances. Platform: Appliance firmware versions prior to patched releases.
- **Progress Kemp LoadMaster**: LoadMaster application delivery controllers (hardware, virtual, and cloud instances). Platform: All unpatched firmware versions across deployment models.
- **TrueConf Video Conferencing Server**: TrueConf Server on-premises deployments. Platform: Windows and Linux server installations; client installers for Windows, macOS, Linux, Android, iOS.
- **N-central RMM**: N-able N-central remote monitoring and management platform. Platform: Cloud and on-premises MSP infrastructure; specific version range not disclosed.
- **Programmable Logic Controllers (PLCs)**: Internet-exposed PLCs from multiple vendors in water/wastewater sector. Platform: Various OT/ICS hardware with management interfaces exposed to internet.
- **Private APN / OT Network Infrastructure**: Cellular private APN configurations providing direct access to OT networks. Platform: Critical infrastructure facilities using private APN for remote OT access.
- **Apple iOS Devices**: iPhones and iPads running iOS versions vulnerable to Coruna/DarkSword exploit chains. Platform: iOS; specific version ranges not disclosed in reporting.
- **Atlassian Rovo / Jira / Confluence**: Atlassian Cloud and Data Center deployments with Rovo AI assistant enabled. Platform: Cloud and on-premises Atlassian stack.
- **Major Webmail Platforms**: Microsoft Outlook, Google Gmail, Fastmail, Proton Mail, Yahoo Mail web interfaces. Platform: Browser-based email clients across desktop and mobile.
- **AI Agent Frameworks**: Autonomous AI agent systems with identity governance gaps. Platform: Enterprise AI agent deployments, copilot systems, and automated workflow platforms.
- **VS Code Extensions (Solidity Pro)**: Microsoft Visual Studio Code with Solidity Pro extension installed. Platform: Windows, macOS, Linux development environments.
- **Passkey/FIDO2 Implementations**: Syncing password managers, browser credential managers, and platform authenticators supporting passkey synchronization. Platform: Cross-platform (iOS, Android, Windows, macOS, Linux).

## Attack Vectors and Techniques

- **Software Supply Chain Compromise**: Attackers infiltrate vendor build/release infrastructure to inject malicious code into legitimate software artifacts (BdThemes JSON feed, TrueConf client installers, VS Code extension).
- **Zero-Day Exploitation**: Active exploitation of undisclosed, unpatched vulnerabilities before vendor remediation (Metabase, potentially N-central).
- **N-Day Exploitation of Recently Patched Flaws**: Rapid weaponization of vulnerabilities for which patches exist but deployment is incomplete (SonicWall SMA1000, Progress LoadMaster).
- **Private APN / Direct OT Network Access**: Leveraging private cellular APN configurations to bypass perimeter defenses and connect directly to operational technology networks.
- **Internet-Exposed Management Interfaces**: Scanning for and exploiting PLCs, load balancers, VPN appliances, and conferencing servers with management interfaces exposed to the public internet.
- **AI Agent Manipulation (GhostJacking)**: Exploiting identity governance gaps by feeding manipulated security events/alerts to autonomous AI agents to induce malicious actions.
- **CSS Injection / Style-Based Exfiltration**: Crafting malicious CSS in email content to break out of message sandboxing and interact with parent webmail DOM to steal credentials/tokens.
- **Malicious Instruction Injection for AI Assistants**: Embedding attacker-controlled prompts in accessible content (Jira tickets, Confluence pages) to hijack AI assistant behavior and exfiltrate data.
- **Ransomware Deployment via RMM/VPN Flaws**: Using vulnerabilities in remote management or access solutions to deploy ransomware across managed environments (StormEncryptor via N-central, SonicWall).
- **Developer Tooling Supply Chain Attacks**: Publishing malicious extensions/plugins to official marketplaces targeting cryptocurrency and blockchain developers.
- **Passkey Ecosystem Abuse**: Exploiting implementation flaws in passkey synchronization, backup, and recovery mechanisms to bypass phishing-resistant authentication.
- **Nation-State OT/ICS Targeting**: Strategic targeting of critical infrastructure (water, energy) by suspected state actors (Iran, China-linked groups) for disruption or positioning.

## Threat Actor Activities

- **Head Mare (Hacktivist Group)**: Exploiting TrueConf server vulnerabilities to breach Russian organizations in instrumentation, electronics, and related sectors. Replaces client installers with PhantomCore backdoor for persistent access. Active since at least 2023; escalating supply chain tactics.
- **Storm-1175 (China-Linked, Financially Motivated)**: Former Medusa ransomware affiliate now deploying novel StormEncryptor ransomware. Likely exploiting N-central RMM vulnerability for initial access. Microsoft tracks as China-linked; operates with financial motivation.
- **Kimsuky (North Korea State-Sponsored, APT43/Thallium)**: Deploying offline AI stack on dedicated infrastructure to automate spear-phishing content generation and malware development. Enhances scale and sophistication of espionage operations targeting policy, defense, and research sectors.
- **Iran-Linked Actors (Suspected)**: Conducting widespread scanning and exploitation of internet-exposed PLCs in U.S. water/wastewater systems across ~12 states. Consistent with previous Iranian IRGC-linked cyber operations against critical infrastructure.
- **Medusa Ransomware Affiliate (Now Storm-1175)**: Former affiliate of Medusa RaaS operation transitioned to independent StormEncryptor deployment. Indicates affiliate churn and rebranding within ransomware ecosystem.
- **Multiple Ransomware Gangs (Unnamed)**: Actively exploiting SonicWall SMA1000 and Progress LoadMaster vulnerabilities for initial access and ransomware deployment. CISA confirms multiple distinct groups leveraging these flaws.
- **The Com (Loose Cybercrime Collective)**: Targeting children and teenagers for blackmail and sextortion. One member sentenced to two years; group remains active across platforms. Represents low-sophistication, high-volume social engineering threat.
- **Unknown Actors (BdThemes Supply Chain)**: Unattributed group compromised BdThemes infrastructure to poison plugin update mechanism. Sophistication suggests organized operation; possible initial access broker or targeted campaign.
- **Security Researchers (Passkey/CSS/GhostJacking)**: Multiple independent research teams disclosing novel attack classes against passkeys, webmail CSS boundaries, and AI agent identity governance. No wild exploitation confirmed; proof-of-concept demonstrations driving vendor mitigations.

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
