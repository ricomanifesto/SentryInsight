---
schema_version: 2
report_date: 2026-10-01
generated_at: 2026-10-01T21:25:57Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-10-01/
---
# Exploitation Report

## Executive Summary

CISA has added a critical authentication bypass in Cisco Catalyst SD-WAN Manager (CVE-2026-76504, CVSS 9.8) to its Known Exploited Vulnerabilities catalog following confirmed active exploitation. Cisco and CISA both report that attackers are leveraging this zero-day flaw to gain unauthenticated administrative API access, and fixed releases are available with no workaround. Simultaneously, Microsoft Security Research has documented active exploitation of a Zimbra Collaboration Suite command injection flaw (CVE-2026-73570, CVSS 8.9) to deploy web shells and harvest mailbox data. A public proof-of-concept has also emerged for an Apple CoreGraphics vulnerability (CVE-2026-86950) that Apple acknowledges may have been used in targeted attacks against specific individuals via malicious PDFs.

Beyond these actively exploited CVEs, multiple high-impact campaigns are underway. Russian state actor Star Blizzard has adopted a novel "RedFlick" technique to deliver its CosmicPulse backdoor. The Dutch Institute for Vulnerability Disclosure confirmed its network was breached through a chain of two zero-days in the Zammad ticketing system. A 16-year-old alleged administrator of the KillSec ransomware group was arrested in Spain during "Operation KillSwitch," which seized the group's leak site and servers. Meanwhile, Bitget disclosed a $387.5 million cryptocurrency theft enabled by a zero-day in third-party security products, and researchers uncovered a self-healing WordPress backdoor that rebuilds itself from files, database, and shared memory.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in Cisco Catalyst SD-WAN Manager that allows an unauthenticated, remote attacker to access the affected system with administrative privileges via the Manager's API.
- **Impact**: Full administrative control over SD-WAN management plane, enabling network manipulation, traffic interception, and lateral movement across managed infrastructure.
- **Status**: Actively exploited in the wild; fixed releases available from Cisco; no workaround exists; added to CISA KEV catalog.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-76504
- **Reporting**: [The Hacker News — CISA Adds Exploited Cisco Catalyst SD-WAN Manager Auth Bypass to KEV](https://thehackernews.com/2026/10/cisa-adds-exploited-cisco-catalyst-sd.html), [The Hacker News — Cisco Warns of Attackers Exploiting Critical Authentication Bypass in SD-WAN Manager](https://thehackernews.com/2026/09/cisco-warns-of-attackers-exploiting.html)

### Zimbra Collaboration Suite Command Injection
- **Description**: Unauthenticated operating system command injection flaw in Zimbra Collaboration Suite (ZCS) that can lead to remote code execution when Simple Network Management Protocol (SNMP) is enabled.
- **Impact**: Attackers deploy web shells and access mailbox data, enabling persistent access, email exfiltration, and credential harvesting.
- **Status**: Now-patched vulnerability being actively weaponized; Microsoft Security Research observed exploitation across multiple environments.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-73570
- **Reporting**: [The Hacker News — Attackers Exploit Zimbra Flaw to Deploy Web Shells and Harvest Authentication Secrets](https://thehackernews.com/2026/09/attackers-exploit-zimbra-flaw-to-deploy.html)

### Apple CoreGraphics Font Parsing Vulnerability
- **Description**: Memory corruption flaw in Apple CoreGraphics triggered by a malicious PDF with a crafted embedded font, causing crashes on unpatched iPhones and Macs.
- **Impact**: Denial-of-service via application crash; Apple states the flaw may have been used in attacks against specific targeted individuals; public proof-of-concept now available.
- **Status**: PoC published; Apple acknowledges possible targeted exploitation; patch status not specified in source.
- **Severity**: unknown
- **Exploitation Status**: observed
- **Action**: investigate
- **CVE IDs**: CVE-2026-86950
- **Reporting**: [The Hacker News — Apple CoreGraphics PoC Emerges as WhatsApp PDF Checks Hint at Possible Delivery Path](https://thehackernews.com/2026/10/apple-coregraphics-poc-emerges-as.html)

### Kiteworks Email Protection Gateway Code Injection
- **Description**: Maximum-severity code injection vulnerability among 126 flaws patched in Kiteworks Email Protection Gateway (EPG) security solution.
- **Impact**: Remote code execution potential on the email protection gateway, enabling email interception, modification, and network pivot.
- **Status**: Security updates released addressing all 126 vulnerabilities; exploitation status not specified in source.
- **Severity**: critical
- **Exploitation Status**: unknown
- **Action**: patch
- **Reporting**: [Bleeping Computer — Kiteworks patches max severity code injection vulnerability](https://www.bleepingcomputer.com/news/security/kiteworks-patches-max-severity-email-protection-gateway-code-injection-vulnerability/)

### Citrix NetScaler ADC/Gateway Command Injection
- **Description**: Critical pre-authentication command injection vulnerability in Citrix NetScaler ADC and NetScaler Gateway.
- **Impact**: Threat actors drop web shells, create superuser accounts, map web shells to CSS-like URLs for stealth, and attempt theft of configuration data.
- **Status**: Actively exploited across multiple customer environments; LevelBlue THOR team analyzed post-exploitation payloads.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Citrix NetScaler Post-Exploitation Payload Creates Superuser, Maps Web Shell to CSS-Like URLs](https://thehackernews.com/2026/10/citrix-netscaler-post-exploitation.html)

### MikroTik RouterOS Pre-Auth RCE
- **Description**: Critical pre-authentication remote code execution vulnerability in MikroTik RouterOS that could also cause denial-of-service.
- **Impact**: Unauthenticated remote code execution on routing infrastructure, enabling network compromise, traffic manipulation, and persistence.
- **Status**: CISA warning issued; exploitation status not explicitly confirmed in source.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [Bleeping Computer — CISA warns of critical pre-auth RCE flaw in MikroTik RouterOS](https://www.bleepingcomputer.com/news/security/cisa-warns-of-critical-pre-auth-rce-flaw-in-mikrotik-routeros/)

### Zammad Ticketing System Zero-Day Chain
- **Description**: Chain of two zero-day vulnerabilities in the open-source Zammad ticketing system.
- **Impact**: Enabled AI-driven network breach of the Dutch Institute for Vulnerability Disclosure (DIVD); full network compromise achieved.
- **Status**: Two zero-days exploited in combination; DIVD confirmed breach; CVE IDs not yet assigned in public reporting.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — DIVD says Zammad zero-days enabled AI-driven network breach](https://www.bleepingcomputer.com/news/security/divd-says-zammad-zero-days-enabled-ai-driven-network-breach/)

### Bitget Third-Party Security Product Zero-Day
- **Description**: Zero-day vulnerability in third-party security products used by cryptocurrency exchange Bitget.
- **Impact**: $387.5 million cryptocurrency theft; attackers used customized tooling; SlowMist investigation recovered malicious artifacts.
- **Status**: Actively exploited in targeted attack; specific product and CVE not disclosed.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Bitget Confirms Third-Party Zero-Day Behind $387.5 Million Cryptocurrency Theft](https://thehackernews.com/2026/10/bitget-confirms-third-party-zero-day.html)

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: All versions prior to fixed releases; SD-WAN network management appliances
- **Zimbra Collaboration Suite (ZCS)**: Versions with SNMP enabled prior to patch; email and collaboration platforms
- **Apple iOS/macOS**: Devices with unpatched CoreGraphics framework; iPhones and Macs processing malicious PDFs
- **Kiteworks Email Protection Gateway (EPG)**: All versions prior to security update; secure file-sharing and email protection appliances
- **Citrix NetScaler ADC and NetScaler Gateway**: Vulnerable versions prior to mitigation; application delivery controllers and VPN gateways
- **MikroTik RouterOS**: Affected RouterOS versions; routing and networking devices
- **Zammad Ticketing System**: Open-source helpdesk/ticketing platform; versions containing the two zero-day flaws
- **Third-party security products (unspecified)**: Products used by Bitget exchange; specific vendor/product not disclosed
- **WordPress**: Sites compromised with SC backdoor; persistence via files, database, and shared memory
- **MetaMask Infrastructure**: Cryptocurrency wallet provider infrastructure; incident ongoing per disclosure

## Attack Vectors and Techniques

- **AI-Driven Vulnerability Chaining**: Autonomous AI agents employing aggressive strategies to discover and chain zero-days (Zammad breach); threat actors using AI to accelerate vulnerability discovery, malware development, and post-compromise activity
- **RedFlick Malware Installation**: Novel technique by Star Blizzard (Russian state actor) to deploy CosmicPulse backdoor via evasive delivery mechanism
- **ClickFix-Style Custom GPT Abuse**: Threat actors creating malicious Custom GPTs on ChatGPT platform to lure victims into RAT installation via legitimate OpenAI/Google domains
- **Dual-RMM Phishing with MSP360/ScreenConnect**: Phishing campaigns distributing legitimate MSP360 RMM installer under guise of meeting invites/PDF lures, establishing remote management access
- **Self-Healing WordPress Backdoor (SC)**: Multi-layer persistence using files, database entries, and shared memory to automatically reconstruct payload after cleanup
- **Web Shell Deployment via Command Injection**: Post-exploitation web shells mapped to CSS-like URLs (Citrix) and deployed via Zimbra/Cisco flaws for persistent access
- **Credential Harvesting from Public Repositories**: 543,000+ valid credentials found in public GitHub repositories, enabling supply chain and infrastructure access
- **AI Model Distillation/Reasoning Extraction**: Coordinated campaign attributed to Moonshot AI associates to extract protected reasoning from OpenAI models

## Threat Actor Activities

- **Star Blizzard (Russian State Actor)**: Deploying CosmicPulse backdoor via new RedFlick technique; ongoing espionage operations targeting government and defense sectors
- **KillSec Ransomware Group**: Allegedly administered by 16-year-old; data theft and leak site operations; disrupted by "Operation KillSwitch" (Spain-led international operation with three arrests)
- **Warlock Ransomware**: Chinese threat actor operating for ~1 year; targeting large Spanish and Portuguese organizations; exhibits APT-like tradecraft despite cybercrime appearance
- **Moonshot AI Associates**: Individuals associated with Beijing-based Chinese AI company; conducted coordinated distillation campaign against OpenAI models (July 2026 onward)
- **Unknown Actors (Zammad Breach)**: AI-driven network breach of DIVD via chained Zammad zero-days; sophisticated automation in vulnerability exploitation
- **Unknown Actors (Bitget Heist)**: Exploited third-party security product zero-day; stole $387.5M; used customized tooling; investigation by SlowMist ongoing
- **Microsoft-Observed Zimbra Attackers**: Weaponized CVE-2026-73570 for web shell deployment and mailbox data access; tracked by Microsoft Security Research
- **Cisco SD-WAN Exploiters**: Actively exploiting CVE-2026-76504 for unauthenticated admin API access; prompted CISA KEV addition and Cisco advisory