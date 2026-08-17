---
schema_version: 2
report_date: 2026-08-17
generated_at: 2026-08-17T18:50:12Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-08-17/
---
# Exploitation Report

## Executive Summary

Four critical vulnerabilities with confirmed active exploitation demand immediate attention. A China-nexus APT is exploiting CVE-2026-59310 in VMware vCenter to deploy Babuk-derived ransomware, while SAP Commerce Cloud instances face active attacks against CVE-2026-58231 just days after patching. Internet-exposed macOS systems are being compromised via CVE-2026-65400 to install Monero miners, and Microsoft is racing to patch the ShieldBreak zero-day (CVE-2026-69414) in Defender. These campaigns demonstrate rapid weaponization of recently disclosed flaws across enterprise infrastructure, cloud platforms, and endpoint systems.

Simultaneously, multiple threat actors are leveraging older vulnerabilities and configuration weaknesses. The Mirai-derived Evooo1Bot botnet is actively scanning for and exploiting known flaws in edge devices to build a SOCKS5 proxy network. The Clop ransomware gang claims breaches at Philips, GE, and Shell, though specific entry vectors remain unconfirmed. Mustang Panda (HoneyMyte) has upgraded its CoolClient backdoor with a signed Windows kernel rootkit for stealthy persistence across targets in Southeast Asia. A published two-stage exploit chain for Unisoc modem firmware demonstrates a feasible path to full Android kernel compromise via VoLTE video calls, with no vendor fix available.

Data breaches continue to cascade across sectors. The French tax authority suffered a breach affecting 678,000 individuals, SafePal lost order data for nearly 40,000 cryptocurrency wallet customers, and Scottish prosecutors face a potentially widening incident via a third-party provider. Financial crime persists: Brazilian and European actors were arrested for a €30 million bank fraud exploiting a service provider vulnerability. Meanwhile, threat actors invested nearly $7 million in expired domains to redirect traffic to scams and malware at scale, and large-scale DDoS attacks disrupted the Threema secure messaging service.

## Active Exploitation Details

### ShieldBreak Zero-Day in Microsoft Defender
- **Description**: Zero-day vulnerability in Microsoft Defender disclosed by security researcher "Nightmare Eclipse" and tracked as CVE-2026-69414. Microsoft is actively developing a security patch.
- **Impact**: Potential bypass or disablement of Defender protections; full impact details not yet publicly disclosed.
- **Status**: Zero-day publicly disclosed; Microsoft working on patch. No fix available at time of reporting.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: mitigate
- **CVE IDs**: CVE-2026-69414
- **Reporting**: [Bleeping Computer — Microsoft working on Defender patch for ShieldBreak zero-day](https://www.bleepingcomputer.com/news/security/microsoft-working-on-defender-patch-for-shieldbreak-zero-day/)

### VMware vCenter Directory Traversal (CVE-2026-59310)
- **Description**: Severe directory-traversal vulnerability in Broadcom VMware vCenter Server (CVSS 9.8) that allows unauthenticated attackers to execute arbitrary code.
- **Impact**: Arbitary code execution on vCenter servers; leveraged by a suspected China-nexus APT to deploy Babuk-derived ransomware.
- **Status**: Newly patched by Broadcom; active exploitation confirmed in the wild by an APT group.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-59310
- **Reporting**: [The Hacker News — Suspected China-Nexus Actor Exploits VMware vCenter Flaw, Deploys Babuk-Derived Ransomware](https://thehackernews.com/2026/08/suspected-china-nexus-actor-exploits.html)

### SAP Commerce Cloud Remote Code Execution (CVE-2026-58231)
- **Description**: Maximum-severity vulnerability (CVSS 10.0) involving insufficient authorization checks and input validation. Allows unauthenticated attackers to abuse a default authentication client and submit malicious requests.
- **Impact**: Remote code execution on SAP Commerce Cloud instances.
- **Status**: Patched by SAP three days prior to reporting; active exploitation attempts observed by threat intelligence firm Defused.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-58231
- **Reporting**: [The Hacker News — SAP Commerce Cloud CVE-2026-58231 Targeted in Exploitation Attempts Days After Patch](https://thehackernews.com/2026/08/sap-commerce-cloud-cve-2026-58231.html), [Bleeping Computer — Max severity SAP Commerce Cloud flaw now targeted in attacks](https://www.bleepingcomputer.com/news/security/max-severity-sap-commerce-cloud-flaw-now-targeted-in-attacks/)

### macOS Screen Sharing Authentication Bypass (CVE-2026-65400)
- **Description**: Critical authentication issue (CVSS 9.8) in the macOS Screen Sharing component that allows an attacker already on the network to bypass authentication controls.
- **Impact**: Full access to exposed Macs; actively used to deploy Monero cryptocurrency miners.
- **Status**: Recently patched by Apple; public exploit code available; active exploitation confirmed by the Netherlands NCSC.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-65400
- **Reporting**: [The Hacker News — Apple macOS Screen Sharing Flaw Exploited on Internet-Exposed Macs to Install Monero Miner](https://thehackernews.com/2026/08/apple-macos-screen-sharing-flaw.html), [Bleeping Computer — Hackers exploit macOS Screen Sharing flaw to deploy Monero miner](https://www.bleepingcomputer.com/news/security/hackers-exploit-macos-screen-sharing-flaw-to-deploy-monero-miner/)

### Unisoc VoLTE Video Call Exploit Chain
- **Description**: Two-stage exploit chain published by SSD Secure Disclosure achieving full Android kernel access on devices running Unisoc modem firmware. The chain is triggered via a malicious VoLTE video call with no user interaction required. The first stage (remote code execution) was disclosed in March 2026; the second stage (kernel privilege escalation) was published August 17, 2026.
- **Impact**: Full Android kernel compromise, granting attackers highest privileges on affected devices.
- **Status**: Full exploit chain publicly documented; no fix available from the chipset maker.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — Unisoc VoLTE Video Call Exploit Chain Can Give Attackers Full Android Kernel Access](https://thehackernews.com/2026/08/unisoc-volte-video-call-exploit-chain.html)

### Evooo1Bot Linux Botnet Campaign
- **Description**: Previously undocumented Mirai-based modular Linux botnet (Evooo1Bot) targeting internet-facing gateway devices. The malware exploits known vulnerabilities in edge devices to gain initial access, then extends the Mirai framework with SOCKS5 proxy capabilities, DDoS modules, and traffic relay functions.
- **Impact**: Compromised devices enrolled as SOCKS5 traffic relay nodes and DDoS bots; persistent access via modular architecture.
- **Status**: Active campaign observed by multiple researchers; exploits "known flaws" in edge device firmware.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Evooo1Bot Linux Botnet Exploits Known Flaws to Turn Edge Devices Into SOCKS5 Proxies](https://thehackernews.com/2026/08/evooo1bot-linux-botnet-exploits-known.html), [Bleeping Computer — New Evooo1Bot Linux botnet turns routers into traffic relay nodes](https://www.bleepingcomputer.com/news/security/new-evooo1bot-linux-botnet-turns-routers-into-traffic-relay-nodes/)

## Affected Systems and Products

- **Microsoft Defender / Windows**: ShieldBreak zero-day (CVE-2026-69414) affects Defender on supported Windows versions; patch in development.
- **VMware vCenter Server**: CVE-2026-59310 affects vCenter Server versions prior to the patched release; exploited by China-nexus APT.
- **SAP Commerce Cloud**: CVE-2026-58231 affects SAP Commerce Cloud instances; patched versions available.
- **Apple macOS**: CVE-2026-65400 affects macOS versions with Screen Sharing enabled and exposed to network; patched in recent security updates.
- **Unisoc Modem Firmware / Android Devices**: Devices using Unisoc modem firmware (common in budget and mid-range Android smartphones) vulnerable to VoLTE video call exploit chain; no vendor fix.
- **Edge Devices / Linux Routers / IoT Gateways**: Evooo1Bot targets internet-facing Linux-based edge devices, routers, and gateways running vulnerable firmware versions; specific affected models not enumerated in reporting.
- **Philips, GE, Shell Enterprise Systems**: Investigating Clop ransomware data theft claims; specific vulnerable components not disclosed.
- **SafePal Customer Database**: Cryptocurrency hardware wallet provider's order management system breached via exploited flaw; 39,798 customers affected.
- **French DGFiP Systems**: General Directorate of Public Finances systems breached; 678,000 individuals' data stolen.
- **Scottish Prosecutor's Office / Third-Party Provider**: Data breach potentially widening across agencies serviced by the same third party.
- **Commerzbank / Service Provider**: Vulnerability at a service provider exploited to withdraw funds from customer accounts; €30M fraud.
- **Threema Messaging Infrastructure**: Targeted by large-scale DDoS attacks causing severe service disruption.

## Attack Vectors and Techniques

- **VoLTE Video Call Exploitation**: Zero-click attack via malicious VoLTE video call targeting Unisoc modem firmware; two-stage chain achieves RCE then kernel privilege escalation.
- **Directory Traversal to RCE**: CVE-2026-59310 in vCenter exploited via path traversal to achieve unauthenticated arbitrary code execution.
- **Default Authentication Client Abuse**: CVE-2026-58231 exploited by unauthenticated attackers leveraging a default authentication client in SAP Commerce Cloud with insufficient authorization checks.
- **Screen Sharing Authentication Bypass**: CVE-2026-65400 exploited on internet-exposed Macs with Screen Sharing enabled; public exploit code used to deploy Monero miners.
- **Known Flaw Exploitation in Edge Devices**: Evooo1Bot leverages existing vulnerabilities in internet-facing Linux devices (routers, gateways) for initial access, then deploys Mirai-derived modular payload.
- **Expired Domain Hijacking (Dropcatch Domains)**: Threat actors acquired ~50,400 expired domains in H1 2026 to inherit traffic and reputation, redirecting victims to scams and malware.
- **ClickFix Social Engineering**: AmnesiaStealer macOS malware delivered via ClickFix attacks tricking users into executing malicious commands.
- **Signed Kernel Rootkit Deployment**: Mustang Panda uses a signed Windows kernel-mode rootkit to hide processes, files, registry objects, and C2 traffic for CoolClient backdoor.
- **Service Provider Vulnerability Exploitation**: Bank fraud actors exploited a flaw at a third-party service provider to access Commerzbank customer accounts.
- **Ransomware Data Theft and Extortion**: Clop ransomware gang claims breaches at Philips, GE, and Shell with data theft (89GB claimed from Shell); extortion likely.
- **Large-Scale DDoS**: Volumetric attacks against Threema messaging infrastructure causing service disruption.
- **Stolen OAuth Token Abuse**: Google Workspace attacks leveraging stolen OAuth tokens to access Gmail, Drive, and connected systems without phishing.

## Threat Actor Activities

- **China-Nexus APT (Unnamed)**: Exploiting CVE-2026-59310 in VMware vCenter to deploy Babuk-derived ransomware; attributed by cybersecurity researchers.
- **Mustang Panda / HoneyMyte**: Chinese-aligned threat actor deploying updated CoolClient backdoor with signed Windows kernel rootkit for stealth; victims identified in Myanmar, Mongolia, Pakistan, and other Southeast Asian countries.
- **Clop Ransomware Gang**: Claiming data theft from Philips, GE, and Shell (89GB); actively investigating by affected organizations; extortion operations ongoing.
- **Evooo1Bot Operators (Unknown)**: Operating Mirai-derived modular botnet for SOCKS5 proxy resale and DDoS-for-hire; infrastructure and attribution not disclosed.
- **Brazilian / European Cybercrime Group**: Four arrested in Brazil, three charged in Europe for €30M bank fraud exploiting service provider vulnerability targeting Commerzbank customers.
- **Dropcatch Domain Operators (Unknown)**: Invested nearly $7M in H1 2026 to acquire 50,400 expired domains for traffic redirection to scams and malware; tracked by Infoblox.
- **AmnesiaStealer Operators (Unknown)**: Distributing macOS information stealer via ClickFix attacks; includes browser session hijacking and interactive remote control module.
- **SafePal Breach Actor (Unknown)**: Claiming to sell stolen order data for 39,798 SafePal customers on underground markets.
- **French Tax Authority Breach Actor (Unknown)**: Accessed DGFiP systems and exfiltrated data for 678,000 individuals.
- **Scottish Government Breach Actor (Unknown)**: Third-party compromise potentially affecting multiple agencies.
- **Nightmare Eclipse (Researcher)**: Disclosed ShieldBreak zero-day (CVE-2026-69414) in Microsoft Defender.
- **SSD Secure Disclosure (Researchers)**: Published two-stage Unisoc VoLTE exploit chain achieving full Android kernel access.