---
schema_version: 2
report_date: 2026-10-01
generated_at: 2026-10-01T12:31:28Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-10-01/
---
# Exploitation Report

## Executive Summary

Critical authentication bypass vulnerabilities in network infrastructure devices are under active exploitation, with CISA adding Cisco Catalyst SD-WAN Manager flaw CVE-2026-76504 to its Known Exploited Vulnerabilities catalog following confirmed attacks. Multiple vendors including Cisco, Zimbra, and Citrix have issued patches for vulnerabilities that threat actors have already weaponized to deploy web shells, harvest credentials, and achieve remote code execution. These incidents span enterprise networking, email collaboration, and application delivery platforms, indicating a sustained focus on edge infrastructure.

State-sponsored and financially motivated actors are diversifying initial access techniques. Russian APT Star Blizzard has adopted a novel "RedFlick" malware delivery method to deploy CosmicPulse backdoors against Ukrainian-aligned NGOs, think tanks, and journalists, while cybercriminals abused ChatGPT Custom GPTs and MSP360 installers in ClickFix-style phishing campaigns to deliver remote access trojans. A zero-day chain in the Zammad ticketing system facilitated an AI-driven breach of the Dutch Institute for Vulnerability Disclosure, and a third-party security product zero-day enabled the $387.5 million theft from cryptocurrency exchange Bitget.

Emerging attack surfaces include AI model extraction campaigns and supply chain risks from AI coding agents. OpenAI disrupted a reasoning distillation operation attributed to Moonshot AI associates, while researchers found over 13,000 internal images exposed in public GitHub repositories via AI coding assistants. The Pentagon disclosed a breach of 3 million personnel records from its human resources system, and MetaMask continues investigating an infrastructure incident that prompted Ethereum validator exits. Apple CoreGraphics flaw CVE-2026-86950 now has a public proof-of-concept, with indicators it may have been used in targeted attacks via malicious PDFs.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Authentication Bypass
- **Description**: Critical zero-day authentication bypass vulnerability (CVE-2026-76504, CVSS 9.8) in Cisco Catalyst SD-WAN Manager allows unauthenticated remote attackers to access the system with administrative privileges via the Manager's API.
- **Impact**: Attackers gain full administrative control over SD-WAN management infrastructure, enabling network manipulation, traffic interception, and lateral movement across managed devices.
- **Status**: Actively exploited in the wild; Cisco has released fixed versions with no workaround available. CISA added to KEV catalog mandating federal agency patching.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-76504
- **Reporting**: [The Hacker News — CISA Adds Exploited Cisco Catalyst SD-WAN Manager Auth Bypass to KEV](https://thehackernews.com/2026/10/cisa-adds-exploited-cisco-catalyst-sd.html), [The Hacker News — Cisco Warns of Attackers Exploiting Critical Authentication Bypass in SD-WAN Manager](https://thehackernews.com/2026/09/cisco-warns-of-attackers-exploiting.html), [Bleeping Computer — Cisco warns of new SD-WAN zero-day exploited in attacks](https://www.bleepingcomputer.com/news/security/cisco-warns-of-new-sd-wan-authentication-bypass-zero-day-exploited-in-attacks/)

### Zimbra Collaboration Suite Command Injection
- **Description**: Unauthenticated operating system command injection flaw (CVE-2026-73570, CVSS 8.9) in Zimbra Collaboration Suite exploitable when Simple Network Management Protocol (SNMP) is enabled.
- **Impact**: Remote code execution leading to web shell deployment, mailbox data access, and authentication secret harvesting.
- **Status**: Now-patched vulnerability actively weaponized by threat actors; Microsoft Security Research observed exploitation across multiple environments.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-73570
- **Reporting**: [The Hacker News — Attackers Exploit Zimbra Flaw to Deploy Web Shells and Harvest Authentication Secrets](https://thehackernews.com/2026/09/attackers-exploit-zimbra-flaw-to-deploy.html)

### Apple CoreGraphics Font Parsing Flaw
- **Description**: Memory corruption vulnerability (CVE-2026-86950) in Apple CoreGraphics triggered by malicious PDFs with crafted embedded fonts, causing crashes on unpatched iPhones and Macs.
- **Impact**: Denial of service via application crash; Apple indicates it may have been used in attacks against specific targeted individuals. Public proof-of-concept code exists.
- **Status**: PoC published; Apple acknowledges possible targeted exploitation. Patch status not specified in source.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **CVE IDs**: CVE-2026-86950
- **Reporting**: [The Hacker News — Apple CoreGraphics PoC Emerges as WhatsApp PDF Checks Hint at Possible Delivery Path](https://thehackernews.com/2026/10/apple-coregraphics-poc-emerges-as.html)

### Citrix NetScaler ADC and Gateway Command Injection
- **Description**: Critical pre-authentication command injection vulnerability in Citrix NetScaler ADC and NetScaler Gateway allowing unauthenticated attackers to execute arbitrary commands.
- **Impact**: Web shell deployment, configuration data theft, and creation of superuser accounts for persistent access. LevelBlue THOR team observed exploitation across multiple customer environments.
- **Status**: Actively exploited; post-exploitation payloads mapped to CSS-like URLs for stealth.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Citrix NetScaler Post-Exploitation Payload Creates Superuser, Maps Web Shell to CSS-Like URLs](https://thehackernews.com/2026/10/citrix-netscaler-post-exploitation.html)

### MikroTik RouterOS Pre-Auth RCE
- **Description**: Critical pre-authentication remote code execution vulnerability in MikroTik RouterOS that could also cause denial-of-service conditions.
- **Impact**: Full device compromise and potential network pivoting; CISA issued warning due to severity.
- **Status**: CISA warning issued; exploitation status not explicitly confirmed in source.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [Bleeping Computer — CISA warns of critical pre-auth RCE flaw in MikroTik RouterOS](https://www.bleepingcomputer.com/news/security/cisa-warns-of-critical-pre-auth-rce-flaw-in-mikrotik-routeros/)

### TeamViewer Client and Host Vulnerabilities
- **Description**: Set of high-severity vulnerabilities affecting TeamViewer client and host software across platforms.
- **Impact**: Potential remote access compromise; TeamViewer urges immediate patching.
- **Status**: Vendor advisory released; active exploitation not confirmed in source.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [Bleeping Computer — TeamViewer urges users to patch severe flaws “as soon as possible”](https://www.bleepingcomputer.com/news/security/teamviewer-urges-users-to-patch-severe-flaws-as-soon-as-possible/)

### Zammad Ticketing System Zero-Day Chain
- **Description**: Chain of two zero-day vulnerabilities in the open-source Zammad ticketing system exploited together to breach the Dutch Institute for Vulnerability Disclosure (DIVD) network.
- **Impact**: AI-driven network breach enabling lateral movement and data access; DIVD attributes compromise to this vulnerability chain.
- **Status**: Zero-days exploited in confirmed breach; patch status not specified in source.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — DIVD says Zammad zero-days enabled AI-driven network breach](https://www.bleepingcomputer.com/news/security/divd-says-zammad-zero-days-enabled-ai-driven-network-breach/)

### Bitget Third-Party Security Product Zero-Day
- **Description**: Zero-day vulnerability in third-party security products used by cryptocurrency exchange Bitget, exploited to steal $387.5 million. SlowMist investigation recovered customized attacker tool.
- **Impact**: Massive cryptocurrency theft; compromise of exchange infrastructure through trusted security tooling.
- **Status**: Confirmed exploited; investigation ongoing with SlowMist. Specific product and patch status not disclosed.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Bitget Confirms Third-Party Zero-Day Behind $387.5 Million Cryptocurrency Theft](https://thehackernews.com/2026/10/bitget-confirms-third-party-zero-day.html), [Bleeping Computer — Bitget hacked via zero-day in third-party security products](https://www.bleepingcomputer.com/news/security/bitget-hacked-via-zero-day-in-third-party-security-products/)

### MetaMask Infrastructure Security Incident
- **Description**: Ongoing security incident affecting MetaMask infrastructure, prompting exit of affected Ethereum validators. No immediate threat to user wallets identified.
- **Impact**: Infrastructure compromise requiring validator remediation; potential supply chain risk for Web3 ecosystem.
- **Status**: Active investigation and remediation with external partners; scope still being determined.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Metamask discloses security incident affecting its infrastructure](https://www.bleepingcomputer.com/news/security/metamask-discloses-security-incident-affecting-its-infrastructure/), [The Hacker News — MetaMask Security Incident Prompts Exit of Affected Ethereum Validators](https://thehackernews.com/2026/10/metamask-security-incident-prompts-exit.html)

### Pentagon DMDC Personnel Data Breach
- **Description**: Breach of the Pentagon's Defense Manpower Data Center human resources management system occurring in October 2025, compromising records of over 3 million military service members.
- **Impact**: Large-scale personal data theft affecting military personnel; notification process underway.
- **Status**: Breach confirmed and notifications initiated; exploitation vector not detailed in source.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Hackers stole Pentagon personnel records of over 3 million people](https://www.bleepingcomputer.com/news/security/hackers-breach-pentagon-human-resources-management-system-steal-data-of-nearly-3-million-people/)

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: All versions prior to fixed releases; enterprise SD-WAN management platforms
- **Zimbra Collaboration Suite (ZCS)**: Versions with SNMP enabled prior to patch; email and collaboration servers
- **Apple iOS and macOS**: Devices with unpatched CoreGraphics framework; iPhones and Macs processing malicious PDFs
- **Citrix NetScaler ADC and NetScaler Gateway**: Appliances vulnerable to pre-auth command injection; application delivery controllers and VPN gateways
- **MikroTik RouterOS**: RouterOS versions affected by pre-auth RCE; SOHO and enterprise routing platforms
- **TeamViewer Client and Host**: Client and host software across Windows, macOS, Linux platforms; remote access endpoints
- **Zammad Ticketing System**: Open-source helpdesk/ticketing system deployments; IT service management platforms
- **Bitget Third-Party Security Products**: Unspecified security tooling used by cryptocurrency exchange; third-party vendor infrastructure
- **MetaMask Infrastructure**: Backend infrastructure components; cryptocurrency wallet service platform
- **Pentagon Defense Manpower Data Center (DMDC)**: Human resources management system; government personnel databases
- **OpenAI ChatGPT Custom GPTs**: Custom GPT feature abused for social engineering; AI platform functionality
- **MSP360 Remote Monitoring and Management**: RMM installer distributed via phishing; managed service provider tooling
- **ScreenConnect**: Remote access software deployed via MSP360 installer; dual-RMM attack chain component
- **GitHub Repositories**: Public repositories containing valid credentials exposed by AI coding agents; source code hosting platform

## Attack Vectors and Techniques

- **RedFlick Malware Delivery**: Novel technique used by Star Blizzard to deploy CosmicPulse backdoor via malicious links that trigger malware installation through legitimate-looking redirects, replacing prior ClickFix usage.
- **ClickFix Social Engineering**: Attackers abuse trusted domains (chatgpt.com, Google) to present fake verification prompts that trick users into executing malicious PowerShell commands, delivering remote access trojans.
- **Custom GPT Weaponization**: Threat actors create deceptive ChatGPT Custom GPTs masquerading as legitimate products to lure victims to malicious sites hosting ClickFix lures.
- **Malicious PDF Font Exploitation**: Crafted embedded fonts in PDF files trigger CoreGraphics memory corruption on Apple devices, potentially enabling targeted exploitation via messaging platforms like WhatsApp.
- **Web Shell Deployment via Command Injection**: Unauthenticated OS command injection in edge devices (Citrix NetScaler, Zimbra) used to drop persistent web shells mapped to innocuous URLs (CSS-like paths) for stealth.
- **Dual-RMM Phishing Chain**: Phishing emails deliver legitimate MSP360 installer under deceptive filenames, establishing remote management access that attackers use to deploy ScreenConnect for secondary persistence.
- **AI-Driven Zero-Day Chaining**: Attackers combine multiple zero-days in Zammad ticketing system with AI-assisted techniques to breach and move laterally within defender networks.
- **Third-Party Security Product Exploitation**: Zero-day in trusted security tooling used to bypass defenses and steal cryptocurrency assets, demonstrating supply chain risk in security vendor ecosystems.
- **Credential Harvesting at Scale**: Over 543,000 valid credentials found exposed in public GitHub repositories, many from AI coding agents automatically committing screenshots and configuration files.
- **AI Model Distillation/Extraction**: Coordinated campaign to illicitly extract protected reasoning from proprietary AI models via API abuse, attributed to Moonshot AI associates.

## Threat Actor Activities

- **Star Blizzard (Russian State Actor)**: Deploying CosmicPulse backdoor via new RedFlick technique against Ukrainian-linked NGOs, think tanks, and journalists; previously used ClickFix but switched tactics to widen phishing net.
- **Moonshot AI Associates**: Individuals associated with Beijing-based Chinese AI company conducting coordinated reasoning extraction campaign against OpenAI models from July 2026 onward; operation disrupted by OpenAI.
- **Bitget Attackers**: Unidentified threat group exploiting zero-day in third-party security products to steal $387.5 million; used customized tool recovered by SlowMist investigators.
- **Zimbra Exploitation Actors**: Threat actors weaponizing CVE-2026-73570 to deploy web shells and harvest authentication secrets from mailbox data; observed by Microsoft Security Research.
- **Citrix NetScaler Attackers**: Threat actors exploiting pre-auth command injection across multiple customer environments to create superusers, deploy CSS-mapped web shells, and exfiltrate configuration data; analyzed by LevelBlue THOR.
- **Custom GPT/ClickFix Campaign Operators**: Threat actors abusing ChatGPT Custom GPTs since late September 2026 to deliver RATs via ClickFix lures; observed by Huntress researchers.
- **MSP360/ScreenConnect Phishing Actors**: Operators conducting phishing campaigns with meeting invites, PDF lures, and software update prompts to deploy dual-RMM access; tracked by Microsoft.
- **DIVD Breach Actors**: Unidentified group leveraging Zammad zero-day chain for AI-driven network breach of vulnerability disclosure organization; attributed by DIVD.
- **Pentagon DMDC Breach Actors**: Unidentified hackers who breached Defense Manpower Data Center in October 2025, stealing 3+ million personnel records.