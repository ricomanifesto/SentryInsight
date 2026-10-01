---
schema_version: 2
report_date: 2026-10-01
generated_at: 2026-10-01T06:39:19Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-10-01/
---
# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse technology stacks, with threat actors leveraging zero-days in networking appliances, collaboration platforms, and third-party security products. Cisco Catalyst SD-WAN Manager (CVE-2026-76504), Citrix NetScaler ADC/Gateway (CVE-2026-88772), and Zimbra Collaboration Suite (CVE-2026-73570) are all confirmed targets of in-the-wild attacks, while Apple has acknowledged targeted exploitation of CVE-2026-86950.

A $387.5 million cryptocurrency theft at Bitget was enabled by a zero-day in unspecified third-party security products, and the Dutch Institute for Vulnerability Disclosure (DIVD) suffered a network breach via a chain of two zero-days in the Zammad ticketing system. Russian state actor Star Blizzard has adopted a novel "RedFlick" technique to deploy its CosmicPulse backdoor against Ukrainian-linked targets, while multiple threat groups are abusing ChatGPT Custom GPTs and ClickFix social-engineering lures to deliver remote access trojans.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Authentication Bypass (CVE-2026-76504)
- **Description**: A critical zero-day authentication bypass in Cisco Catalyst SD-WAN Manager allows unauthenticated remote attackers to access the Manager's API with administrative privileges. The flaw affects the central management system for Cisco SD-WAN networks.
- **Impact**: Attackers can escalate to admin privileges, potentially gaining full control over SD-WAN infrastructure, network policies, and connected devices across the enterprise.
- **Status**: Actively exploited in the wild. Cisco has released fixed software versions; no workaround is available.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-76504
- **Reporting**: [The Hacker News — Cisco Warns of Attackers Exploiting Critical Authentication Bypass in SD-WAN Manager](https://thehackernews.com/2026/09/cisco-warns-of-attackers-exploiting.html), [Bleeping Computer — Cisco warns of new SD-WAN zero-day exploited in attacks](https://www.bleepingcomputer.com/news/security/cisco-warns-of-new-sd-wan-authentication-bypass-zero-day-exploited-in-attacks/)

### Citrix NetScaler ADC/Gateway DTLS Memory Overflow (CVE-2026-88772)
- **Description**: A critical memory overflow vulnerability in the Datagram Transport Layer Security (DTLS) protocol handling of Citrix NetScaler ADC and NetScaler Gateway. The pre-authentication flaw (CVSS 9.5) enables shellcode execution without credentials.
- **Impact**: Attackers achieve root-level remote code execution, enabling deployment of web shells (WHIPSHOT, SLAPSHOT), theft of configuration data, creation of superuser accounts, and persistent access via CSS-mapped web shell URLs.
- **Status**: Actively exploited in the wild since at least September 2026. Patches are available. Targeted sectors include government, financial services, technology, education, and legal/professional services across North America and Europe.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-88772
- **Reporting**: [The Hacker News — Citrix NetScaler CVE-2026-88772 Exploit Details Show Pre-Auth Path to Shellcode Execution](https://thehackernews.com/2026/09/citrix-netscaler-cve-2026-88772-exploit.html), [The Hacker News — Citrix NetScaler Post-Exploitation Payload Creates Superuser, Maps Web Shell to CSS-Like URLs](https://thehackernews.com/2026/10/citrix-netscaler-post-exploitation.html), [The Hacker News — Attackers Exploit NetScaler Flaw for Root Access, Deploy WHIPSHOT and SLAPSHOT](https://thehackernews.com/2026/09/attackers-exploit-netscaler-flaw-for.html)

### Zimbra Collaboration Suite Command Injection (CVE-2026-73570)
- **Description**: An unauthenticated operating system command injection flaw (CVSS 8.9) in Zimbra Collaboration Suite that triggers when Simple Network Management Protocol (SNMP) is enabled, leading to remote code execution.
- **Impact**: Threat actors deploy web shells and harvest authentication secrets and mailbox data. The vulnerability has been weaponized post-patch.
- **Status**: Actively exploited; patches available. Microsoft Security Research observed weaponization.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-73570
- **Reporting**: [The Hacker News — Attackers Exploit Zimbra Flaw to Deploy Web Shells and Harvest Authentication Secrets](https://thehackernews.com/2026/09/attackers-exploit-zimbra-flaw-to-deploy.html)

### Apple Zero-Day Out-of-Bounds Write (CVE-2026-86950)
- **Description**: An out-of-bounds write vulnerability in Apple platforms being exploited in an "extremely sophisticated fashion" according to Apple's advisory.
- **Impact**: Targeted attacks against specific individuals or organizations; exact impact depends on the affected component but out-of-bounds writes typically enable code execution or memory corruption.
- **Status**: Actively exploited in targeted attacks. Apple has acknowledged the exploitation.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-86950
- **Reporting**: [Dark Reading — Apple Zero-Day Vulnerability Weaponized in Targeted Attacks](https://www.darkreading.com/cyberattacks-data-breaches/apple-zero-day-vulnerability-weaponized-targeted-attacks)

### Bitget Third-Party Security Product Zero-Day
- **Description**: A zero-day vulnerability in unspecified third-party security products used by cryptocurrency exchange Bitget. SlowMist's investigation identified malicious activity involving these products and recovered a customized attacker tool.
- **Impact**: Full system breach enabling theft of $387.5 million in cryptocurrency assets.
- **Status**: Actively exploited; investigation ongoing. The specific vendor and product have not been publicly disclosed.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Bitget Confirms Third-Party Zero-Day Behind $387.5 Million Cryptocurrency Theft](https://thehackernews.com/2026/10/bitget-confirms-third-party-zero-day.html), [Bleeping Computer — Bitget hacked via zero-day in third-party security products](https://www.bleepingcomputer.com/news/security/bitget-hacked-via-zero-day-in-third-party-security-products/)

### Zammad Ticketing System Zero-Day Chain
- **Description**: A chain of two zero-day vulnerabilities in the open-source Zammad ticketing system that enabled an AI-driven network breach of the Dutch Institute for Vulnerability Disclosure (DIVD).
- **Impact**: Complete network compromise of a vulnerability disclosure organization, demonstrating the risk of chained zero-days in internet-facing helpdesk platforms.
- **Status**: Actively exploited (breach confirmed). Patches or mitigations not specified in reporting.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — DIVD says Zammad zero-days enabled AI-driven network breach](https://www.bleepingcomputer.com/news/security/divd-says-zammad-zero-days-enabled-ai-driven-network-breach/)

### MikroTik RouterOS Pre-Authentication RCE
- **Description**: A critical pre-authentication remote code execution vulnerability in MikroTik RouterOS that could also lead to denial-of-service conditions. CISA has issued an active warning.
- **Impact**: Unauthenticated remote code execution on networking infrastructure, potentially enabling traffic interception, network pivoting, and infrastructure takeover.
- **Status**: CISA warning indicates active or imminent exploitation risk. Patch availability not specified in reporting.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: patch
- **Reporting**: [Bleeping Computer — CISA warns of critical pre-auth RCE flaw in MikroTik RouterOS](https://www.bleepingcomputer.com/news/security/cisa-warns-of-critical-pre-auth-rce-flaw-in-mikrotik-routeros/)

### TeamViewer Client/Host High-Severity Vulnerabilities
- **Description**: A set of high-severity vulnerabilities affecting TeamViewer client and host software across platforms. Specific vulnerability classes not detailed in reporting.
- **Impact**: Potential remote access or control compromise given TeamViewer's purpose as remote management software.
- **Status**: TeamViewer urges immediate patching; active exploitation status not confirmed but risk assessed as severe.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [Bleeping Computer — TeamViewer urges users to patch severe flaws “as soon as possible”](https://www.bleepingcomputer.com/news/security/teamviewer-urges-users-to-patch-severe-flaws-as-soon-as-possible/)

### OpenSSL DTLS Heap Memory Leak
- **Description**: A high-severity flaw in OpenSSL's DTLS implementation where heap memory can be leaked to the peer or cause a program crash during handshake message retransmission under specific timing conditions.
- **Impact**: Memory disclosure to communicating peers or denial of service via crash. No confirmed exploitation.
- **Status**: Fixed in OpenSSL releases dated September 29, 2026. No active exploitation reported.
- **Severity**: high
- **Exploitation Status**: not_observed
- **Action**: patch
- **Reporting**: [The Hacker News — OpenSSL Fixes High-Severity DTLS Flaw That Can Leak Heap Memory Unencrypted](https://thehackernews.com/2026/09/openssl-fixes-high-severity-dtls-flaw.html)

### MetaMask Infrastructure Security Incident
- **Description**: An ongoing security incident affecting part of MetaMask's infrastructure. The wallet provider states no immediate threat to user wallets has been identified.
- **Impact**: Potential exposure of backend systems; user wallet compromise not confirmed.
- **Status**: Active incident response underway with external partners and security advisors.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — MetaMask Security Incident Prompts Exit of Affected Ethereum Validators](https://thehackernews.com/2026/10/metamask-security-incident-prompts-exit.html)

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: All versions prior to fixed releases; central management for Cisco SD-WAN fabric
- **Citrix NetScaler ADC and NetScaler Gateway**: Appliances running vulnerable DTLS implementations; pre-authentication attack surface
- **Zimbra Collaboration Suite (ZCS)**: Versions with SNMP enabled prior to patch; email and collaboration platform
- **Apple Platforms (iOS, macOS, etc.)**: Versions affected by CVE-2026-86950; targeted attack surface
- **Third-Party Security Products (undisclosed vendor)**: Products deployed at Bitget; zero-day enabled $387.5M theft
- **Zammad Ticketing System**: Open-source helpdesk platform; chain of two zero-days enabled DIVD breach
- **MikroTik RouterOS**: Network operating system on RouterBOARD hardware and Cloud Hosted Routers; pre-auth RCE vector
- **TeamViewer Client and Host Software**: Cross-platform remote access software; high-severity flaws in recent versions
- **OpenSSL**: Versions with vulnerable DTLS implementation; fixed in September 29, 2026 releases
- **MetaMask Infrastructure**: Backend services and APIs; ongoing incident investigation

## Attack Vectors and Techniques

- **RedFlick Malware Installation Technique**: Novel tactic used by Star Blizzard (Russian state actor) to deploy CosmicPulse backdoor. Replaces prior ClickFix usage. Targets Ukrainian-linked NGOs, think tanks, and journalists via phishing.
  - **Vector**: Phishing emails with malicious links/attachments triggering RedFlick execution chain

- **ClickFix Social Engineering via ChatGPT Custom GPTs**: Threat actors create malicious Custom GPTs on OpenAI's platform that masquerade as legitimate tools, directing victims to ClickFix pages that trick users into executing PowerShell commands to install RATs.
  - **Vector**: Abuse of trusted AI platform (chatgpt.com domains) → malicious Custom GPT → ClickFix lure → PowerShell execution → malware delivery

- **Dual-RMM Phishing (MSP360 + ScreenConnect)**: Phishing campaigns distribute legitimate MSP360 RMM installers under deceptive filenames (meeting invites, PDF lures, update prompts). Once installed, attackers deploy ScreenConnect for persistent remote access.
  - **Vector**: Email phishing → legitimate RMM installer execution → ScreenConnect deployment → persistent remote control

- **CSuite Phishing with M365 Session Theft**: US-focused campaign stealing Microsoft 365 session tokens via phishing, then deploying RMM tools for remote access. 351 sandbox analyses, 51% US submissions. Targets technology, manufacturing, government, consulting sectors.
  - **Vector**: Phishing → M365 session cookie theft → RMM tool deployment → account compromise and fraud

- **NetScaler Post-Exploitation (WHIPSHOT/SLAPSHOT)**: After exploiting CVE-2026-88772, attackers deploy WHIPSHOT and SLAPSHOT web shells, create superuser accounts, map web shells to CSS-like URLs for stealth, and exfiltrate configuration data.
  - **Vector**: Pre-auth DTLS exploit → root shell → web shell deployment → persistence and data theft

- **Zimbra Web Shell Deployment**: Exploitation of CVE-2026-73570 via SNMP-enabled instances to drop web shells and access mailbox data and authentication secrets.
  - **Vector**: Unauthenticated command injection via SNMP → web shell → mailbox data harvesting

## Threat Actor Activities

- **Star Blizzard (Russian State Actor / APT29/Cozy Bear)**: Active deployment of RedFlick technique against Ukrainian-linked targets (NGOs, think tanks, journalists) to install CosmicPulse backdoor. Has shifted from ClickFix to RedFlick to widen phishing effectiveness.
  - **Campaign**: Ongoing espionage operations leveraging novel social-engineering and malware delivery techniques; infrastructure overlaps with prior Star Blizzard activity

- **Unknown Threat Actors (NetScaler Exploitation)**: Multiple campaigns exploiting CVE-2026-88772 across North America and Europe targeting government, financial services, technology, education, and legal sectors. Mandiant and Google Threat Intelligence Group observed WHIPSHOT/SLAPSHOT deployment in September 2026.
  - **Campaign**: Broad opportunistic and targeted exploitation of NetScaler appliances post-patch release

- **Unknown Threat Actors (Bitget Heist)**: Sophisticated attackers who exploited a zero-day in third-party security products to breach Bitget and steal $387.5 million. Used customized tools recovered by SlowMist.
  - **Campaign**: High-value cryptocurrency exchange targeting with supply-chain-style zero-day exploitation

- **Multiple Threat Groups (ChatGPT Custom GPT Abuse)**: Huntress and Dark Reading report separate but similar campaigns abusing ChatGPT Custom GPTs for ClickFix-based RAT delivery. Indicates trend of AI platform feature abuse.
  - **Campaign**: Late September 2026 activity; leveraging trust in OpenAI domains to bypass security controls

- **CSuite Phishing Operators**: US-focused threat group conducting large-scale phishing (351 samples analyzed) combining M365 session theft with RMM deployment for persistent access and fraud.
  - **Campaign**: Sector-agnostic but concentrated in technology, manufacturing, government, consulting; 51% US-origin submissions

- **Zimbra Exploitation Actors**: Threat actors weaponizing CVE-2026-73570 post-patch to deploy web shells and harvest mailbox data, per Microsoft Security Research.
  - **Campaign**: Post-patch exploitation of known vulnerability; targeting organizations with SNMP-enabled Zimbra instances