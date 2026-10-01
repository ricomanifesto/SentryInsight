---
schema_version: 2
report_date: 2026-10-01
generated_at: 2026-10-01T03:29:40Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-10-01/
---
# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse technology stacks, ranging from network infrastructure and collaboration platforms to AI-driven services. Russian state actor Star Blizzard has adopted a novel "RedFlick" technique to deploy its CosmicPulse backdoor against Ukrainian-linked targets, while financially motivated campaigns weaponize ChatGPT Custom GPTs and dual-RMM phishing lures to deliver remote access trojans. Simultaneously, three high-severity zero-days—in Cisco Catalyst SD-WAN Manager, Citrix NetScaler ADC/Gateway, and Zimbra Collaboration Suite—have been weaponized for pre-authentication remote code execution and administrative privilege escalation, with patches available but exploitation ongoing.

A supply-chain compromise of third-party security products enabled the $387.5 million theft from cryptocurrency exchange Bitget, and a chain of two zero-days in the open-source Zammad ticketing system facilitated an AI-driven breach of the Dutch Institute for Vulnerability Disclosure itself. Apple has confirmed targeted exploitation of an out-of-bounds write flaw, and TeamViewer has disclosed high-severity client vulnerabilities requiring immediate patching. Credential exposure at scale—over 543,000 valid secrets in public GitHub repositories and 13,000 internal images leaked by AI coding agents—amplifies the risk of follow-on intrusion.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Authentication Bypass (CVE-2026-76504)
- **Description**: A critical zero-day authentication bypass in Cisco Catalyst SD-WAN Manager allows unauthenticated remote attackers to access the Manager's API with administrative privileges. The flaw resides in the API authentication mechanism and requires no user interaction.
- **Impact**: Attackers gain full administrative control over SD-WAN infrastructure, enabling network traffic manipulation, policy changes, and lateral movement across managed devices.
- **Status**: Actively exploited in the wild. Cisco has released fixed software versions; no workaround exists.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-76504
- **Reporting**: [The Hacker News — Cisco Warns of Attackers Exploiting Critical Authentication Bypass in SD-WAN Manager](https://thehackernews.com/2026/09/cisco-warns-of-attackers-exploiting.html), [Bleeping Computer — Cisco warns of new SD-WAN zero-day exploited in attacks](https://www.bleepingcomputer.com/news/security/cisco-warns-of-new-sd-wan-authentication-bypass-zero-day-exploited-in-attacks/)

### Citrix NetScaler ADC/Gateway DTLS Memory Overflow (CVE-2026-88772)
- **Description**: A critical memory overflow vulnerability in the Datagram Transport Layer Security (DTLS) protocol handling of Citrix NetScaler ADC and NetScaler Gateway appliances. The flaw is pre-authentication and allows shellcode execution.
- **Impact**: Unauthenticated remote attackers achieve root-level code execution on the appliance, enabling deployment of persistent implants such as WHIPSHOT and SLAPSHOT, credential harvesting, and network pivoting.
- **Status**: Actively exploited since at least September 2026. Citrix has released patches; exploitation observed by Mandiant and Google Threat Intelligence Group targeting government, financial, technology, education, and legal sectors in North America and Europe.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-88772
- **Reporting**: [The Hacker News — Attackers Exploit NetScaler Flaw for Root Access, Deploy WHIPSHOT and SLAPSHOT](https://thehackernews.com/2026/09/attackers-exploit-netscaler-flaw-for.html), [The Hacker News — Citrix NetScaler CVE-2026-88772 Exploit Details Show Pre-Auth Path to Shellcode Execution](https://thehackernews.com/2026/09/citrix-netscaler-cve-2026-88772-exploit.html)

### Zimbra Collaboration Suite Command Injection (CVE-2026-73570)
- **Description**: An unauthenticated operating system command injection flaw in Zimbra Collaboration Suite (ZCS) triggered via Simple Network Management Protocol (SNMP) handling. CVSS 8.9.
- **Impact**: Remote code execution without authentication, leading to web shell deployment, mailbox data exfiltration, and authentication secret harvesting.
- **Status**: Actively exploited in the wild. Microsoft Security Research observed threat actors weaponizing the now-patched vulnerability.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-73570
- **Reporting**: [The Hacker News — Attackers Exploit Zimbra Flaw to Deploy Web Shells and Harvest Authentication Secrets](https://thehackernews.com/2026/09/attackers-exploit-zimbra-flaw-to-deploy.html)

### Apple Out-of-Bounds Write (CVE-2026-86950)
- **Description**: An out-of-bounds write vulnerability in Apple platforms, exploited in an "extremely sophisticated fashion" according to Apple's advisory.
- **Impact**: Targeted code execution on affected Apple devices, likely enabling spyware deployment against high-value individuals.
- **Status**: Actively exploited in targeted attacks. Apple has released patches.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-86950
- **Reporting**: [Dark Reading — Apple Zero-Day Vulnerability Weaponized in Targeted Attacks](https://www.darkreading.com/cyberattacks-data-breaches/apple-zero-day-vulnerability-weaponized-targeted-attacks)

### Zammad Ticketing System Zero-Day Chain
- **Description**: A chain of two zero-day vulnerabilities in the open-source Zammad ticketing system, exploited together to breach the Dutch Institute for Vulnerability Disclosure (DIVD) network in an AI-driven intrusion.
- **Impact**: Full network compromise of a security research organization, demonstrating the feasibility of chaining ticketing-system flaws for initial access and lateral movement.
- **Status**: Exploited in a confirmed breach (DIVD). No CVE IDs assigned at time of reporting; patches or mitigations not publicly detailed in source.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — DIVD says Zammad zero-days enabled AI-driven network breach](https://www.bleepingcomputer.com/news/security/divd-says-zammad-zero-days-enabled-ai-driven-network-breach/)

### Third-Party Security Product Zero-Day (Bitget Supply-Chain Compromise)
- **Description**: A zero-day vulnerability in unspecified third-party security products used by cryptocurrency exchange Bitget, exploited to breach internal systems and steal $387.5 million in assets.
- **Impact**: Complete compromise of exchange infrastructure via trusted security tooling, enabling large-scale asset theft.
- **Status**: Exploited in a confirmed high-value breach. Vendor and CVE details not disclosed in source.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Bitget hacked via zero-day in third-party security products](https://www.bleepingcomputer.com/news/security/bitget-hacked-via-zero-day-in-third-party-security-products/)

### TeamViewer Client/Host High-Severity Vulnerabilities
- **Description**: A set of high-severity vulnerabilities affecting TeamViewer client and host software across platforms, disclosed by the vendor with an urgent patching advisory.
- **Impact**: Potential remote code execution or privilege escalation on systems running vulnerable TeamViewer versions, threatening the remote-access supply chain.
- **Status**: Actively disclosed with urgent patching recommendation. No CVE IDs provided in source; exploitation status not explicitly confirmed but severity warrants immediate action.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [Bleeping Computer — TeamViewer urges users to patch severe flaws “as soon as possible”](https://www.bleepingcomputer.com/news/security/teamviewer-urges-users-to-patch-severe-flaws-as-soon-as-possible/)

### ChatGPT Custom GPTs ClickFix RAT Delivery
- **Description**: Threat actors create malicious Custom GPTs on OpenAI's platform, promoted via sponsored Google results, to lure victims to sites employing ClickFix social-engineering techniques that deliver remote access trojans (RATs).
- **Impact**: Malware installation and persistent remote access on victim endpoints, bypassing traditional email or web filters by abusing a trusted AI platform.
- **Status**: Actively observed by Huntress in late September 2026; ongoing campaign leveraging legitimate OpenAI and Google domains.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [Dark Reading — Malicious Custom GPTs Turn ChatGPT Into RAT Delivery Lure](https://www.darkreading.com/cyberattacks-data-breaches/malicious-custom-gpts-chatgpt-rat-delivery-lure), [The Hacker News — Attackers Abuse ChatGPT Custom GPTs to Deliver RAT via ClickFix Lures](https://thehackernews.com/2026/09/attackers-abuse-chatgpt-custom-gpts-to.html), [Bleeping Computer — Custom ChatGPTs push ClickFix attacks to deploy RAT malware](https://www.bleepingcomputer.com/news/security/custom-chatgpts-push-clickfix-attacks-to-deploy-rat-malware/)

### MSP360/ScreenConnect Dual-RMM Phishing
- **Description**: Phishing campaigns distribute trojanized MSP360 RMM installers disguised as meeting invitations, PDF lures, and software-update prompts. Execution establishes legitimate MSP360 remote management access, followed by ScreenConnect deployment for redundant persistence.
- **Impact**: Full remote control of compromised endpoints via two legitimate RMM tools, enabling data theft, lateral movement, and ransomware staging.
- **Status**: Actively observed by Microsoft; campaign ongoing against diverse sectors.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [The Hacker News — Attackers Abuse MSP360 to Deploy ScreenConnect in Dual-RMM Phishing Attacks](https://thehackernews.com/2026/09/attackers-abuse-msp360-to-deploy.html)

### CSuite Phishing with Microsoft 365 Session Theft and RMM Deployment
- **Description**: US-focused phishing campaign (CSuite) steals Microsoft 365 session tokens and deploys remote monitoring and management (RMM) tools for persistent access. 351 sandbox submissions analyzed, 51% from United States; technology, manufacturing, government, and consulting sectors most targeted.
- **Impact**: Account takeover, business email compromise, fraud, and persistent remote access via RMM tooling.
- **Status**: Active campaign with broad US targeting observed by ANY.RUN researchers.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [The Hacker News — US-Focused CSuite Phishing Steals Microsoft 365 Sessions and Deploys RMM Tools for Remote Access](https://thehackernews.com/2026/09/us-focused-csuite-phishing-steals.html)

### Star Blizzard RedFlick Technique with CosmicPulse Backdoor
- **Description**: Russian state actor Star Blizzard (APT29/Cozy Bear) employs a new "RedFlick" phishing technique—moving away from ClickFix—to target Ukrainian-linked NGOs, think tanks, and journalists, deploying the CosmicPulse backdoor.
- **Impact**: Long-term espionage access to high-value targets aligned with Russian strategic interests; credential theft, data exfiltration, and network persistence.
- **Status**: Active campaign confirmed by multiple intelligence sources; technique specifically designed to evade ClickFix mitigations.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [Bleeping Computer — Russian state hackers use new RedFlick technique to push malware](https://www.bleepingcomputer.com/news/security/russian-state-hackers-use-new-redflick-technique-to-push-malware/), [Dark Reading — Russia's Star Blizzard Ditches ClickFix to Widen Phishing Net](https://www.darkreading.com/threat-intelligence/russia-star-blizzard-apt-ditches-clickfix-widen-phishing-net)

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: All versions prior to fixed releases; enterprise SD-WAN management platforms.
- **Citrix NetScaler ADC and NetScaler Gateway**: Appliances running vulnerable DTLS implementations; widely deployed in enterprise and government networks.
- **Zimbra Collaboration Suite (ZCS)**: Versions vulnerable to CVE-2026-73570; on-premises email and collaboration servers.
- **Apple Platforms**: iOS, iPadOS, macOS, and related operating systems affected by CVE-2026-86950; targeted exploitation suggests high-value individuals.
- **Zammad Ticketing System**: Open-source helpdesk/ticketing platform; two zero-days chained for initial access (specific versions not disclosed).
- **Third-Party Security Products (Bitget)**: Unspecified security tooling used by Bitget; supply-chain vector affecting cryptocurrency exchange infrastructure.
- **TeamViewer Client and Host Software**: Cross-platform remote access software; high-severity flaws in current versions prior to vendor patches.
- **OpenAI ChatGPT Custom GPTs / Google Search**: Legitimate AI platform features abused for lure hosting and distribution; no software vulnerability in the platforms themselves.
- **MSP360 RMM and ScreenConnect**: Legitimate remote monitoring and management tools weaponized via trojanized installers and dual-deployment technique.
- **Microsoft 365 / Entra ID**: Session token theft via phishing; Entra ID script injection protections rolling out October 2026.
- **GitHub Public Repositories**: Over 543,000 valid credentials exposed; 13,000+ internal images leaked via AI coding agents across 300+ organizations.

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: Victims tricked into executing malicious commands (e.g., "Run as Administrator" PowerShell) via fake verification pages, CAPTCHA mimics, or browser-based lures. Now delivered through ChatGPT Custom GPTs and sponsored search results.
- **RedFlick Phishing Technique**: Evolution of ClickFix tailored by Star Blizzard; uses dynamic lure generation and evasion of automated analysis to deploy CosmicPulse backdoor against specific geopolitical targets.
- **Dual-RMM Deployment**: Simultaneous installation of two legitimate RMM agents (MSP360 + ScreenConnect) for redundancy and evasion; distributed via phishing lures mimicking meeting invites, PDFs, and update prompts.
- **Microsoft 365 Session Token Theft + RMM**: Phishing kits (CSuite) harvest Entra ID session cookies, then deploy RMM tools for persistent remote access without needing credentials.
- **Pre-Authentication RCE via Protocol Flaws**: DTLS memory overflow (NetScaler), SNMP command injection (Zimbra), and API authentication bypass (Cisco SD-WAN) enable unauthenticated root/admin access on internet-facing appliances.
- **Supply-Chain Zero-Day in Security Tooling**: Exploitation of a zero-day in third-party security products to breach a high-value target (Bitget), demonstrating trust inversion.
- **AI-Driven Network Breach**: Chained zero-days in Zammad ticketing system exploited in an automated/AI-augmented intrusion against a vulnerability disclosure organization.
- **Malicious AI Model Inspection (Unsloth Studio)**: Patched flaw where `trust_remote_code` during model inspection leads to arbitrary Python execution; supply-chain risk for ML practitioners.
- **Credential/Secret Exposure at Scale**: 543,000+ valid credentials and 13,000+ internal images in public GitHub repos, exacerbated by AI coding agents auto-committing screenshots and artifacts.

## Threat Actor Activities

- **Star Blizzard (APT29/Cozy Bear)**: Russian state-sponsored actor. Shifted from ClickFix to novel "RedFlick" technique; targets Ukrainian-linked NGOs, think tanks, journalists; deploys CosmicPulse backdoor for persistent espionage. Active since at least September 2026.
- **ShinyHunters**: Financially motivated extortion group. Dutch police arrested an alleged leader; FBI urging members to surrender. Associated with data theft and extortion campaigns against numerous organizations.
- **Unknown / Unattributed - NetScaler Exploitation**: Mandiant and GTIG observed exploitation of CVE-2026-88772 deploying WHIPSHOT and SLAPSHOT implants against government, financial, technology, education, and legal sectors in North America and Europe (September 2026).
- **Unknown / Unattributed - Zimbra Exploitation**: Microsoft Security Research observed web shell deployment and mailbox data harvesting via CVE-2026-73570; actor not publicly attributed.
- **Unknown / Unattributed - CSuite Phishing**: US-focused campaign stealing M365 sessions and deploying RMM tools; high volume (351 sandbox analyses) with concentration in technology, manufacturing, government, consulting.
- **Unknown / Unattributed - Bitget Supply-Chain Attack**: Exploited zero-day in third-party security products to steal $387.5M; actor not identified, sophistication suggests well-resourced group.
- **Opportunistic Cybercriminals - ChatGPT Custom GPT / ClickFix**: Abusing legitimate AI platforms and search ads for RAT distribution; low barrier to entry, broad targeting via sponsored results.