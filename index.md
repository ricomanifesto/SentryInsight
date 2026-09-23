---
schema_version: 2
report_date: 2026-09-23
generated_at: 2026-09-23T04:13:23Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-23/
---
# Exploitation Report

## Executive Summary

Multiple critical zero-day vulnerabilities are under active exploitation across diverse technology stacks, ranging from network infrastructure and security management platforms to AI gateways and virtualization layers. Chinese-speaking threat actors are leveraging flaws in Zyxel switches and WordPress to compromise government data, while the Check Point Security Management Server zero-day (CVE-2026-93616) has been exploited in targeted attacks since July.

The VeloCloud Orchestrator flaw (CVE-2026-93952) carries a maximum CVSS 10.0 rating and is actively exploited in certificate-based deployments. Meanwhile, phishing-as-a-service platform EvilTokens compromised over 12,000 Microsoft 365 accounts before a coordinated takedown, and the ShinyHunters extortion gang claims a PeopleSoft zero-day breach of FBI systems.

## Active Exploitation Details

### Check Point Security Management Server Zero-Day
- **Description**: A previously unknown flaw in Check Point's Security Management Server allows an attacker with access to the server's web service to run arbitrary scripts without authentication. The vulnerability affects the server that controls firewall policies for Check Point deployments.
- **Impact**: Unauthenticated remote code execution on the management server, enabling full control over firewall policies and network security infrastructure.
- **Status**: Actively exploited in targeted attacks since July 23, 2026. Emergency hotfixes released on September 22, 2026.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-93616
- **Reporting**: [The Hacker News — Check Point Warns of Management Server Zero-Day Exploited in Targeted Attacks](https://thehackernews.com/2026/09/check-point-warns-of-management-server.html), [Bleeping Computer — Check Point warns of Management Server zero-day exploited in attacks](https://www.bleepingcomputer.com/news/security/check-point-patches-management-server-zero-day-exploited-in-attacks/)

### Critical Bifrost AI Gateway Flaw
- **Description**: A critical vulnerability in Bifrost, an open-source AI gateway routing requests to over 20 LLM providers, allows unauthenticated attackers to execute arbitrary commands on the gateway server via a single HTTP request when management authentication is enabled.
- **Impact**: Full server compromise without credentials, potentially exposing all routed LLM traffic and underlying infrastructure.
- **Status**: Vulnerability disclosed with CVSS 9.8 rating. Fixed in Bifrost HTTP transport version 2.1.0.
- **Severity**: critical
- **Exploitation Status**: unknown
- **Action**: patch
- **CVE IDs**: CVE-2026-90898
- **Reporting**: [The Hacker News — Critical Bifrost AI Gateway Flaw Lets Attackers Run Commands Without Credentials](https://thehackernews.com/2026/09/critical-bifrost-ai-gateway-flaw-lets.html)

### D-Link DIR-822A Router Maximum Severity Zero-Day
- **Description**: A maximum-severity vulnerability affecting legacy DIR-822A dual-band Wi-Fi routers with public proof-of-concept exploit code available and no patch released.
- **Impact**: Complete device compromise on end-of-life router models still deployed in home and small office environments.
- **Status**: Zero-day with public PoC, no vendor patch available for legacy hardware.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: investigate
- **CVE IDs**: CVE-2026-86296
- **Reporting**: [Bleeping Computer — D-Link warns of max severity zero-day bug in DIR-822A routers](https://www.bleepingcomputer.com/news/security/d-link-warns-of-max-severity-zero-day-bug-in-dir-822a-routers/)

### VeloCloud Orchestrator Critical Flaw
- **Description**: A CVSS 10.0 vulnerability in on-premises VeloCloud Orchestrator (VCO), the management server for VeloCloud SD-WAN Edge devices, allows remote unauthenticated attackers to privilege internal functions and affect the VCO host. Only orchestrators configured for certificate-based Edge authentication are vulnerable.
- **Impact**: Full compromise of the SD-WAN management plane, potentially enabling network-wide traffic manipulation and lateral movement.
- **Status**: Actively exploited in the wild as of September 22, 2026.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-93952
- **Reporting**: [The Hacker News — New CVSS 10.0 VeloCloud Orchestrator Flaw Actively Exploited in Certificate-Based Setups](https://thehackernews.com/2026/09/new-cvss-100-velocloud-orchestrator.html)

### Linux Kernel KVM ARM64 Virtualization Escape
- **Description**: A flaw in the Linux kernel's KVM virtualization code for ARM64 processors exposes freed host memory to guest virtual machines when nested virtualization is enabled, allowing guests to read and write host kernel memory.
- **Impact**: Virtual machine escape to host-level code execution, compromising the hypervisor and all co-located guests.
- **Status**: Technical details published with exploitability confirmed by researcher; patch status not specified in source.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: investigate
- **CVE IDs**: CVE-2026-89775
- **Reporting**: [The Hacker News — New Linux Kernel Flaw Gives ARM64 KVM Guests Read-Write Access to Host Memory](https://thehackernews.com/2026/09/new-linux-kernel-flaw-gives-arm64-kvm.html)

### SharePoint Server Authenticated RCE
- **Description**: A SharePoint Server vulnerability initially classified by Microsoft as spoofing (CVSS 6.5) actually enables authenticated remote code execution. Affects SharePoint Server 2016, 2019, and Subscription Edition.
- **Impact**: Authenticated attackers can achieve remote code execution on SharePoint servers, potentially leading to data theft and lateral movement.
- **Status**: Patches released for all affected versions following corrected classification.
- **Severity**: high
- **Exploitation Status**: not_observed
- **Action**: patch
- **CVE IDs**: CVE-2026-65660
- **Reporting**: [The Hacker News — SharePoint Flaw Initially Listed as Spoofing by Microsoft Enables Authenticated RCE](https://thehackernews.com/2026/09/sharepoint-flaw-initially-listed-as.html)

### Zyxel GS1900 Series Switch Vulnerability
- **Description**: A high-severity vulnerability in Zyxel GS1900 series Smart Managed Switches actively exploited for data theft from government and other targets. CISA has ordered federal agencies to patch by emergency directive.
- **Impact**: Unauthorized access to switch management and exfiltration of sensitive data from backend databases.
- **Status**: Actively exploited in the wild; CISA emergency directive issued for federal agencies.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Chinese hackers exploit WordPress, Zyxel flaws to steal govt data](https://www.bleepingcomputer.com/news/security/chinese-hackers-exploit-multiple-technologies-to-steal-govt-data/), [Bleeping Computer — CISA orders feds to patch Zyxel flaw exploited for data theft](https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-actively-exploited-zyxel-flaw-by-thursday/)

### WordPress Core Critical Code Execution Flaw
- **Description**: A critical flaw in WordPress core allows unauthenticated attackers to force a site to load a PHP file from outside theme directories, which on some server configurations enables remote code execution. Fixed in WordPress 7.1.2 with backports to all supported branches down to 4.7.
- **Impact**: Unauthenticated remote code execution on vulnerable server configurations, leading to full site and server compromise.
- **Status**: Patched across all supported branches as of September 22, 2026.
- **Severity**: critical
- **Exploitation Status**: unknown
- **Action**: patch
- **Reporting**: [The Hacker News — WordPress Issues Patch for Critical Flaw That Can Enable Code Execution on Some Servers](https://thehackernews.com/2026/09/wordpress-issues-patch-for-critical.html)

### BigDiskBuster Windows Defender Zero-Day
- **Description**: A zero-day proof-of-concept tool that prevents Microsoft Defender from installing platform and signature updates by exhausting all available disk space. No patch, CVE, or Microsoft advisory exists.
- **Impact**: Persistent disabling of antivirus updates, leaving endpoints defenseless against new malware signatures and platform protections.
- **Status**: Public PoC released September 19, 2026; no vendor fix available.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: investigate
- **Reporting**: [The Hacker News — Researcher Drops BigDiskBuster Zero-Day PoC That Blocks Microsoft Defender Updates](https://thehackernews.com/2026/09/researcher-drops-bigdiskbuster-zero-day.html), [Bleeping Computer — New Windows Defender zero-day blocks Microsoft antivirus updates](https://www.bleepingcomputer.com/news/security/new-windows-defender-zero-day-blocks-microsoft-antivirus-updates/)

### PeopleSoft Zero-Day (Claimed)
- **Description**: The ShinyHunters extortion gang claims to have breached FBI systems using a new Oracle PeopleSoft zero-day vulnerability, accessing internal services and stealing sensitive employee and applicant data.
- **Impact**: Alleged compromise of federal law enforcement HR systems and exfiltration of personally identifiable information.
- **Status**: Claimed by threat actor; no independent verification or vendor acknowledgment in source materials.
- **Severity**: unknown
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — ShinyHunters claims FBI hack, data theft in PeopleSoft zero-day breach](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)

## Affected Systems and Products

- **Check Point Security Management Server**: All versions prior to September 22, 2026 hotfix; controls firewall policies for Check Point deployments
- **Bifrost AI Gateway**: All versions of Bifrost HTTP transport before 2.1.0 when management authentication is enabled; routes requests to 20+ LLM providers
- **D-Link DIR-822A Routers**: Legacy dual-band Wi-Fi routers (end-of-life); no patch planned
- **VeloCloud Orchestrator (VCO)**: On-premises deployments configured for certificate-based Edge authentication; manages VeloCloud SD-WAN Edge devices
- **Linux Kernel KVM (ARM64)**: Hosts with nested virtualization enabled running ARM64 guests; affects kernel versions prior to patched releases
- **SharePoint Server**: 2016, 2019, and Subscription Edition; patches available for all versions
- **Zyxel GS1900 Series Switches**: Smart Managed Switches; actively exploited for data theft
- **WordPress Core**: All versions from 4.7 through 7.1.1; patched in 7.1.2 and all maintained branch updates
- **Microsoft Defender / Windows**: All versions vulnerable to BigDiskBuster disk exhaustion attack; no patch available
- **Oracle PeopleSoft**: Version(s) unspecified; zero-day claimed by ShinyHunters in FBI breach

## Attack Vectors and Techniques

- **Unauthenticated Remote Code Execution via Web Management Interfaces**: Exploited in Check Point Management Server (CVE-2026-93616), Bifrost AI Gateway (CVE-2026-90898), and VeloCloud Orchestrator (CVE-2026-93952) — attackers send crafted HTTP requests to management web services without authentication
- **Certificate-Based Authentication Bypass**: VeloCloud Orchestrator flaw (CVE-2026-93952) specifically targets orchestrators using certificate authentication for Edge devices, allowing privilege escalation to internal functions
- **Virtual Machine Escape via Memory Corruption**: Linux KVM ARM64 flaw (CVE-2026-89775) exploits use-after-free in nested virtualization code to grant guests read-write access to host kernel memory
- **Authenticated RCE via Misclassified Spoofing Flaw**: SharePoint Server (CVE-2026-65660) — attackers with valid credentials leverage deserialization/path traversal to execute code, despite Microsoft's initial spoofing classification
- **Network Device Exploitation for Data Theft**: Zyxel GS1900 switches exploited to access backend databases and exfiltrate 18,500+ records from 996 compromised devices
- **Unauthenticated PHP File Inclusion Leading to RCE**: WordPress core flaw allows forcing inclusion of external PHP files, achieving code execution on permissive server configurations (misconfigured PHP allow_url_include or similar)
- **Disk Exhaustion Denial-of-Service Against Security Agents**: BigDiskBuster fills all disk space to block Microsoft Defender update installation, a novel anti-forensics and persistence technique
- **Device Code Phishing (OAuth Device Authorization Flow)**: EvilTokens PhaaS abused Microsoft's device code flow to phish 12,000+ accounts across 10,000+ organizations, using AI at every attack chain step
- **Spear-Phishing with mshta.exe and ReverseRAT**: SideCopy targets Indian academic institutions using malicious scripts executed via mshta.exe to deploy ReverseRAT payload
- **NPM Supply Chain Attacks**: Malicious packages (tw-pkgprobe-7731, indexed-btree) masquerade as legitimate tools; indexed-btree hides loader in runtime code to evade lifecycle-script scanning
- **OAuth Token Theft via Compromised Developer Machine**: Shai-Hulud attackers stole 170 private repositories from CrowdSec using an OAuth token exfiltrated from a former employee's computer through the TanStack npm supply chain compromise
- **AI-Autonomous Post-Exploitation**: ClosedQuorum malware uses Google Gemini, DeepSeek, Qwen, and Mistral models to autonomously determine post-compromise actions

## Threat Actor Activities

- **Chinese-Speaking Threat Actor**: Exploiting Zyxel GS1900 switch vulnerabilities and WordPress flaws to steal government data; compromised 996 devices and exfiltrated 18,500+ records from backend databases (source-178864dedd5d)
- **ShinyHunters Extortion Gang**: Claims breach of FBI systems via PeopleSoft zero-day; alleges access to internal services and theft of employee/applicant data (source-5204aaedc51d)
- **EvilTokens Operators**: Ran phishing-as-a-service platform using device code flow and AI automation; compromised 12,000+ Microsoft 365 accounts across 10,000+ organizations before Microsoft-led takedown seized 50 websites and disabled 150+ domains (source-c75e5a1826c4, source-ac1280aee3db, source-684de1d265d4)
- **SideCopy (APT)**: Expanded targeting from Indian government entities to academic institutions; uses spear-phishing with mshta.exe script execution to deploy ReverseRAT (source-c8f864c65cb4)
- **Shai-Hulud Group**: Conducted npm supply chain attack via TanStack compromise; stole OAuth token from former CrowdSec employee's machine to exfiltrate 170 private GitHub repositories (source-5778eb9fbb8b)
- **Unknown npm Attackers**: Published malicious packages "tw-pkgprobe-7731" (masquerading as Twilio security tool) and "indexed-btree" (mimicking sorted-btree with runtime-hidden loader); both removed from registry after detection (source-b38195d46412, source-9806c677170e)
- **ClosedQuorum Malware Authors**: Developed Windows malware leveraging multiple commercial AI APIs (Gemini, DeepSeek, Qwen, Mistral) for autonomous post-exploitation decision-making (source-724fc722a895)
- **Chinese AI Relay Operators**: Operating 80,000+ relay servers to mask Chinese user access to frontier US LLM models, likely for model extraction/cloning (source-723fd7190de3)