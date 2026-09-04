---
schema_version: 2
report_date: 2026-09-04
generated_at: 2026-09-04T04:01:45Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-04/
---
# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse technology stacks, ranging from network infrastructure and web applications to endpoint security agents and mobile devices. Cisco Nexus 9000 switches, Elementor Pro for WordPress, SonicWall SMA 1000 appliances, and Sangoma Switchvox VoIP platforms all have confirmed exploitation activity with patches available. Simultaneously, two zero-day scenarios demand immediate attention: a privilege escalation flaw in CrowdStrike Falcon (dubbed FalconFlank) with a public proof-of-concept, and NSO Group's Pegasus spyware leveraging an iMessage zero-click exploit against a Serbian activist. Threat actors are also accelerating operations through AI-driven automation, supply chain compromise, and living-off-the-land techniques using trusted binaries like Node.js.

Infostealer ecosystems continue to expand in scope and sophistication. The Shai-Hulud worm variant now harvests credentials from 469 locations across developer environments, CI/CD pipelines, cloud configurations, and AI tooling, while the BraZetsu framework commercializes access to compromised Windows hosts through an underground marketplace model. Social engineering campaigns have grown in scale and precision: the Phantom Deal operation targets enterprises with highly researched fake merger communications, and a broad RMM phishing campaign spans 46 countries with the United States as the primary target. CISA's addition of seven vulnerabilities to its Known Exploited Vulnerabilities catalog—including a maximum-severity SSRF in SonicWall SMA 1000—underscores the breadth of current exploitation activity.

## Active Exploitation Details

### Cisco Nexus 9000 Critical Remote Code Execution
- **Description**: A critical vulnerability in Silicon One-based Cisco Nexus 9000 switches allows unauthenticated, remote attackers to execute arbitrary code with root privileges. The flaw affects 10 specific switch models running vulnerable software versions.
- **Impact**: Full device compromise with root-level code execution, enabling network infrastructure takeover, traffic interception, lateral movement, and persistence in core network segments.
- **Status**: Patches released by Cisco alongside an IOS XR hardening release bundling 7 umbrella CVEs (2 rated CVSS 9.8). No workaround exists for any IOS XR version.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-20212
- **Reporting**: [The Hacker News — Critical Cisco Nexus 9000 Flaw Lets Unauthenticated Remote Attackers Run Code as Root](https://thehackernews.com/2026/09/critical-cisco-nexus-9000-flaw-lets.html)

### Elementor Pro WordPress Plugin Critical Vulnerability
- **Description**: A critical vulnerability in the Elementor Pro plugin for WordPress allows authenticated attackers to upload malicious files and achieve remote code execution. The flaw was recently patched but is already being exploited in the wild.
- **Impact**: Attackers deliver webshell payloads and execute arbitrary commands on the underlying server, leading to complete site takeover, data theft, and potential lateral movement.
- **Status**: Actively exploited post-patch. WordPress site administrators must update immediately.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-32475
- **Reporting**: [Bleeping Computer — Critical Elementor Pro flaw exploited to take over WordPress sites](https://www.bleepingcomputer.com/news/security/critical-elementor-pro-flaw-exploited-to-take-over-wordpress-sites/)

### SonicWall SMA 1000 Server-Side Request Forgery
- **Description**: A server-side request forgery vulnerability in SonicWall SMA 1000 appliances that allows remote, unauthenticated attackers to bypass authentication and achieve remote code execution. This is one of multiple zero-days affecting the platform.
- **Impact**: Unauthenticated RCE on VPN/appliance gateways, providing initial access to internal networks, credential harvesting, and persistence opportunities.
- **Status**: Added to CISA Known Exploited Vulnerabilities catalog. Exploitation activity follows earlier summer attacks on other SonicWall zero-days. Patches available.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-83548
- **Reporting**: [The Hacker News — CISA Adds Seven Exploited Flaws as Attackers Deploy Reverse Shells and Crypto Miners](https://thehackernews.com/2026/09/cisa-adds-seven-exploited-flaws-as.html), [Dark Reading — SonicWall SMA 1000 Zero-Days Enable Unauthenticated RCE](https://www.darkreading.com/vulnerabilities-threats/sonicwall-sma-1000-zero-days-unauthenticated-rce)

### Sangoma Switchvox Unauthenticated SQL Injection
- **Description**: An unauthenticated SQL injection vulnerability in the Sangoma Switchvox VoIP platform that can lead to remote code execution. Attackers are actively exploiting this flaw to deploy reverse shells.
- **Impact**: Unauthenticated attackers achieve RCE on VoIP infrastructure, enabling call interception, credential theft, network pivoting, and persistence.
- **Status**: Actively exploited in the wild. Reverse shells observed. Patches available from Sangoma.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-9586
- **Reporting**: [Bleeping Computer — Hackers exploit Sangoma Switchvox flaw to deploy reverse shells](https://www.bleepingcomputer.com/news/security/hackers-exploit-sangoma-switchvox-flaw-to-deploy-reverse-shells/)

### CrowdStrike Falcon FalconFlank Privilege Escalation Zero-Day
- **Description**: A zero-day privilege escalation vulnerability in CrowdStrike Falcon Sensor, dubbed FalconFlank, that abuses the Office malicious macros remediation functionality. A public proof-of-concept has been released by researcher Chaotic Eclipse (aka INFINITE NIGHTMARE, MSNightmare, Nightmare-Eclipse).
- **Impact**: Local privilege escalation to SYSTEM on endpoints running CrowdStrike Falcon, enabling defense evasion, credential access, and persistence despite EDR presence.
- **Status**: Zero-day with public PoC. No vendor patch available at time of reporting. CrowdStrike investigation likely underway.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: investigate
- **Reporting**: [The Hacker News — Researcher Releases FalconFlank PoC Showing Privilege Escalation in CrowdStrike Falcon](https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html)

### NSO Group Pegasus iMessage Zero-Click Exploit
- **Description**: An iMessage zero-click exploit used to deploy NSO Group's Pegasus spyware on the iPhone of a Serbian student movement member. Confirmed by Citizen Lab in collaboration with SHARE Foundation with high-confidence indicators.
- **Impact**: Full device compromise without user interaction, enabling comprehensive surveillance including message access, call recording, location tracking, and microphone/camera activation.
- **Status**: Active targeted exploitation against civil society. Apple likely investigating or patching. No CVE assigned publicly at time of reporting.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Pegasus Zero-Click Spyware Exploit Infects Serbian Student Movement Member's iPhone](https://thehackernews.com/2026/09/pegasus-zero-click-spyware-exploit.html)

### Coder Registry Supply Chain Compromise
- **Description**: Attackers compromised Coder's Cloudflare infrastructure and added unauthorized registry servers that delivered malicious Terraform modules containing credential-stealing code to downstream users.
- **Impact**: Supply chain compromise affecting Terraform/IaC workflows, leading to credential theft, cloud resource hijacking, and potential infrastructure takeover for organizations using Coder's registry.
- **Status**: Active compromise identified and disclosed. Coder has remediated infrastructure. Users must rotate credentials and audit Terraform state.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Coder's registry infrastructure compromised to push malicious modules](https://www.bleepingcomputer.com/news/security/coders-registry-infrastructure-compromised-to-push-malicious-modules/)

### Shai-Hulud Infostealer Worm Expansion
- **Description**: The Shai-Hulud infostealer worm variant has evolved to scan for credentials across 469 locations across developer environments, CI/CD tooling, cloud configurations, and AI tool configurations—a significant expansion from earlier variants that checked only 189 paths.
- **Impact**: Mass credential harvesting from developer machines and build pipelines, enabling supply chain attacks, cloud account takeover, and lateral movement into production environments.
- **Status**: Active evolution and deployment. GitGuardian researchers tracking expansion. No single CVE; this is malware capability expansion.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [The Hacker News — Shai-Hulud's Reach Just Grew to 469 Credential Locations. Here's What That Means](https://thehackernews.com/2026/09/shai-huluds-reach-just-grew-to-469.html)

### BraZetsu Malware Framework
- **Description**: A sophisticated Python-based Windows malware framework that fuels an underground marketplace commercializing access to compromised hosts. Unlike standard infostealers, BraZetsu empowers Initial Access Brokers by turning compromised systems into highly valuable commercial inventory.
- **Impact**: Commoditized initial access at scale. Compromised hosts inventoried, categorized, and sold to ransomware operators, data theft groups, and other threat actors.
- **Status**: Active marketplace operation. Framework actively maintained and deployed.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [The Hacker News — BraZetsu Malware Turns Compromised Windows Hosts Into Criminal Marketplace Inventory](https://thehackernews.com/2026/09/brazetsu-malware-turns-compromised.html)

### Plex Media Server Vulnerabilities
- **Description**: Multiple security vulnerabilities in Plex desktop clients and media servers requiring immediate patching. Specific CVE identifiers not disclosed in available reporting.
- **Impact**: Potential remote code execution, information disclosure, or authentication bypass on exposed media servers and client endpoints.
- **Status**: Plex has issued urgent patch advisory. Exploitation status unclear but urgency suggests active threat.
- **Severity**: unknown
- **Exploitation Status**: unknown
- **Action**: patch
- **Reporting**: [Bleeping Computer — Plex warns users to patch security vulnerabilities immediately](https://www.bleepingcomputer.com/news/security/plex-warns-users-to-patch-security-vulnerabilities-immediately/)

## Affected Systems and Products

- **Cisco Nexus 9000 Series Switches (Silicon One-based)**: 10 specific models running vulnerable ArubaOS-CX/NX-OS versions; core data center and enterprise network infrastructure
- **Elementor Pro WordPress Plugin**: All versions prior to patched release; WordPress sites with Elementor Pro installed (millions of active installations)
- **SonicWall SMA 1000 Series Appliances**: SMA 1000 series secure mobile access appliances; enterprise VPN and zero-trust network access gateways
- **Sangoma Switchvox VoIP Platform**: Switchvox appliances and software versions prior to patch; on-premises and hosted PBX/UC systems
- **CrowdStrike Falcon Sensor**: Windows endpoints with Falcon Sensor installed; enterprise EDR deployments across all sectors
- **Apple iOS/iPadOS/macOS**: Devices running versions vulnerable to iMessage zero-click exploit; targeted individuals and potentially broader populations
- **Coder Enterprise/Cloud Terraform Registry**: Organizations using Coder's hosted registry service for Terraform module distribution; DevOps and platform engineering teams
- **Developer Workstations and CI/CD Pipelines**: Systems with credentials accessible in 469 locations scanned by Shai-Hulud (IDE configs, Git credentials, cloud CLI configs, AI tool configs, container registries, etc.)
- **Windows Endpoints**: Systems compromised by BraZetsu framework; enterprise and personal Windows hosts globally
- **Plex Media Server and Desktop Clients**: All platforms (Windows, macOS, Linux, NAS devices, Docker containers) running unpatched versions

## Attack Vectors and Techniques

- **Unauthenticated Network Device RCE**: Direct exploitation of network infrastructure (Cisco Nexus, SonicWall SMA, Sangoma Switchvox) without credentials, providing immediate foothold in critical network segments
- **Web Application Exploitation**: Authenticated RCE via WordPress plugin vulnerability (Elementor Pro) leading to webshell deployment and server compromise
- **Zero-Click Mobile Exploitation**: iMessage zero-click exploit chain delivering Pegasus spyware without user interaction; targets high-value individuals
- **EDR Privilege Escalation**: Abuse of security agent functionality (CrowdStrike Falcon macros remediation) to achieve SYSTEM privileges on protected endpoints
- **Supply Chain Compromise**: Infrastructure takeover (Coder's Cloudflare) to inject malicious artifacts into trusted development workflows (Terraform modules)
- **Infostealer Worm Propagation**: Automated credential harvesting across 469 locations in developer environments, CI/CD systems, cloud configs, and AI tooling
- **Access Brokerage Marketplace**: Malware framework (BraZetsu) that inventories, categorizes, and sells compromised host access to downstream operators
- **Living-off-the-Land with Node.js**: Abuse of trusted Node.js runtime (node.exe) to execute malicious payloads while evading detection; targeting government, tech, and hospitality sectors since February 2026
- **Social Engineering at Scale**: Highly researched fake M&A communications (Phantom Deal) targeting mid-level employees for fraudulent wire transfers
- **Multi-Nation Phishing Campaign**: RMM-themed phishing spanning 46 countries using tax/lure documents; 45% targeting US entities; 601 cases linked
- **OAuth and Trusted App Abuse**: Phishing kits leveraging legitimate OAuth flows and trusted applications to bypass security controls
- **AI-Accelerated Attack Chains**: Frontier AI agents compressing attack timelines from two weeks to 10 hours, enabling rapid reconnaissance, exploitation, and scaling

## Threat Actor Activities

- **Phantom Deal Operators**: Conducting highly targeted business email compromise via fake merger and acquisition communications; extreme research on target companies to dupe mid-level employees into large financial transfers
- **ShinyHunters**: Alleged breach of ReliaQuest (cybersecurity firm); known for data theft and extortion operations against high-profile targets
- **BraZetsu Operators / Initial Access Brokers**: Running a commercial marketplace for compromised Windows host access; Python-based framework enables inventory management and resale to ransomware and data theft groups
- **Breeze Comet**: Brazil's most sophisticated threat group targeting financial systems domestically and globally; financially motivated with direct monetization
- **RMM Phishing Campaign Operators**: Broad campaign across 46 countries using CRA tax forms and other lures; shifted from Canadian to US-focused targeting (45% of activity); 601 cases attributed by ANY.RUN
- **NSO Group**: Deploying Pegasus spyware via iMessage zero-click exploits against civil society targets (Serbian student movement); state-sponsored surveillance capability
- **Chaotic Eclipse / INFINITE NIGHTMARE**: Security researcher publishing FalconFlank zero-day PoC for CrowdStrike Falcon; disclosure method raises immediate risk
- **Shai-Hulud Developers/Operators**: Maintaining and evolving infostealer worm with expanding credential harvesting capabilities (189 → 469 locations); targeting developer and CI/CD ecosystems
- **SonicWall/Sangoma Attackers**: Exploiting edge device zero-days (SonicWall SMA 1000, Sangoma Switchvox) for initial access; deploying reverse shells and crypto miners per CISA KEV observations
- **Coder Registry Compromisers**: Unknown actors who breached Cloudflare infrastructure to poison Terraform module supply chain; credential-stealing payloads