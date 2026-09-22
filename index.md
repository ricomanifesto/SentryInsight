---
schema_version: 2
report_date: 2026-09-22
generated_at: 2026-09-22T21:10:16Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-22/
---
# Exploitation Report

## Executive Summary

Multiple zero-day vulnerabilities and actively exploited flaws have surfaced across diverse technologies this reporting period, with threat actors targeting networking equipment, AI infrastructure, content management systems, and cloud identity services. Chinese-speaking actors are leveraging Zyxel switch vulnerabilities and WordPress flaws to exfiltrate government data at scale, while the ShinyHunters extortion group claims an FBI breach via an Oracle PeopleSoft zero-day. Critically, a CVSS 10.0 flaw in VeloCloud Orchestrator (CVE-2026-93952) and a CVSS 9.8 vulnerability in the Bifrost AI gateway (CVE-2026-90898) are being actively exploited or present immediate unauthenticated remote code execution risk. Microsoft's takedown of the EvilTokens phishing-as-a-service platform—which compromised over 12,000 Microsoft 365 accounts across 10,000 organizations using AI-driven device code phishing—highlights the industrialization of identity-focused attacks.

Simultaneously, supply chain threats continue to evolve: the Shai-Hulud campaign compromised 170 private GitHub repositories via a stolen OAuth token originating from the TanStack npm supply chain attack, while malicious npm packages (tw-pkgprobe-7731 and indexed-btree) demonstrate increasingly sophisticated evasion techniques hiding payloads in runtime code. Check Point's Security Management Server zero-day (CVE-2026-93616) was exploited in targeted attacks before a September patch, and a Linux kernel KVM flaw (CVE-2026-89775) enables ARM64 guest-to-host escape. CISA has added the Zyxel GS1900 vulnerability (CVE-2026-7273) to its Known Exploited Vulnerabilities catalog, mandating federal patching, while D-Link's end-of-life DIR-822A routers face a maximum-severity zero-day (CVE-2026-86296) with public exploit code and no patch forthcoming.

## Active Exploitation Details

### Check Point Security Management Server Zero-Day (CVE-2026-93616)
- **Description**: A previously unknown flaw in Check Point's Security Management Server allows an attacker with access to the server's web service to execute arbitrary scripts without authentication. The vulnerability was exploited in a handful of targeted attacks on July 23, 2026, before Check Point released a fix on September 22.
- **Impact**: Unauthenticated script execution on the server that controls firewall policies for Check Point deployments, potentially allowing full control over network security infrastructure.
- **Status**: Patched as of September 22, 2026. Emergency hotfixes released for affected versions.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-93616
- **Reporting**: [The Hacker News — Check Point Warns of Management Server Zero-Day Exploited in Targeted Attacks](https://thehackernews.com/2026/09/check-point-warns-of-management-server.html), [Bleeping Computer — Check Point warns of Management Server zero-day exploited in attacks](https://www.bleepingcomputer.com/news/security/check-point-patches-management-server-zero-day-exploited-in-attacks/)

### VeloCloud Orchestrator Critical Flaw (CVE-2026-93952)
- **Description**: A maximum-severity vulnerability (CVSS 10.0) in on-premises VeloCloud Orchestrator (VCO), the management server for VeloCloud SD-WAN Edge devices. The flaw allows a remote unauthenticated attacker to privilege internal functions and affect the VCO host, but only impacts orchestrators configured to authenticate Edges with certificates.
- **Impact**: Full compromise of the SD-WAN management plane, potentially enabling network-wide traffic manipulation, lateral movement, and persistence across branch offices.
- **Status**: Actively exploited in the wild as of September 22, 2026. Arista has acknowledged active exploitation.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-93952
- **Reporting**: [The Hacker News — New CVSS 10.0 VeloCloud Orchestrator Flaw Actively Exploited in Certificate-Based Setups](https://thehackernews.com/2026/09/new-cvss-100-velocloud-orchestrator.html)

### Zyxel GS1900 Series Switches Buffer Overflow (CVE-2026-7273)
- **Description**: A stack-based buffer overflow vulnerability (CVSS 8.8) in Zyxel GS1900 series Smart Managed Switches that allows arbitrary operating system command execution. CISA has added this vulnerability to its Known Exploited Vulnerabilities catalog citing evidence of active exploitation.
- **Impact**: Attackers gain command-line access to network switches, enabling network reconnaissance, traffic interception, lateral movement, and persistence in victim environments.
- **Status**: Patched. CISA ordered federal agencies to patch by September 25, 2026. Actively exploited by Chinese-speaking threat actors against government targets.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-7273
- **Reporting**: [Bleeping Computer — Chinese hackers exploit WordPress, Zyxel flaws to steal govt data](https://www.bleepingcomputer.com/news/security/chinese-hackers-exploit-multiple-technologies-to-steal-govt-data/), [Bleeping Computer — CISA orders feds to patch Zyxel flaw exploited for data theft](https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-actively-exploited-zyxel-flaw-by-thursday/), [The Hacker News — Zyxel and Veeam Flaws Under Active Exploitation With Command and SYSTEM Access](https://thehackernews.com/2026/09/zyxel-and-veeam-flaws-under-active.html)

### WordPress Comment2Shell Vulnerability (CVE-2026-93485)
- **Description**: A WordPress core flaw dubbed "Comment2Shell" (CVE-2026-93485) that allows an anonymous visitor to leave a comment containing a hidden script. When a logged-in administrator views the comment, the script executes and can achieve remote code execution on the server. Fixed in WordPress 7.1.1 on September 17, 2026, with patches backported to all supported branches.
- **Impact**: Unauthenticated stored XSS that escalates to authenticated RCE via administrator session hijacking, leading to full site and server compromise.
- **Status**: Patched in WordPress 7.1.1 and all supported branches back to 4.7. Active exploitation reported.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-93485
- **Reporting**: [The Hacker News — WordPress Comment2Shell Flaw Can Turn Anonymous Comment XSS Into RCE via Admin Session](https://thehackernews.com/2026/09/wordpress-comment2shell-flaw-can-turn.html)

### WordPress Critical Core Flaw (CVE Not Provided)
- **Description**: A critical vulnerability in WordPress core that allows an unauthenticated attacker to make a site load a PHP file from outside its theme directories. On some server configurations, this enables arbitrary code execution. Fixed in WordPress 7.1.2 on September 22, 2026, with patches for all supported branches back to version 4.7.
- **Impact**: Unauthenticated remote code execution on vulnerable server configurations, leading to complete site and server compromise.
- **Status**: Patched as of September 22, 2026. WordPress urges immediate updates.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — WordPress Issues Patch for Critical Flaw That Can Enable Code Execution on Some Servers](https://thehackernews.com/2026/09/wordpress-issues-patch-for-critical.html), [Bleeping Computer — Chinese hackers exploit WordPress, Zyxel flaws to steal govt data](https://www.bleepingcomputer.com/news/security/chinese-hackers-exploit-multiple-technologies-to-steal-govt-data/)

### Oracle PeopleSoft Zero-Day (CVE Not Provided)
- **Description**: The ShinyHunters extortion group claims to have breached FBI systems using a previously unknown (zero-day) vulnerability in Oracle PeopleSoft, gaining access to internal services and stealing sensitive data on employees and job applicants.
- **Impact**: Alleged compromise of FBI internal systems, exfiltration of sensitive personnel and applicant data.
- **Status**: Zero-day; no patch information available at time of reporting. ShinyHunters claims active exploitation.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — ShinyHunters claims FBI hack, data theft in PeopleSoft zero-day breach](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)

### Bifrost AI Gateway Unauthenticated RCE (CVE-2026-90898)
- **Description**: A critical vulnerability (CVSS 9.8) in Bifrost, an open-source AI gateway routing requests to 20+ LLM providers. The flaw allows an unauthenticated attacker to execute arbitrary commands on the gateway server with a single HTTP request when management authentication is enabled. Affects all versions before 2.1.0.
- **Impact**: Full server compromise of AI inference infrastructure, potential access to LLM API keys, model manipulation, and pivot to connected systems.
- **Status**: Patched in version 2.1.0. No active exploitation reported but critical severity and trivial exploitation warrant immediate action.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-90898
- **Reporting**: [The Hacker News — Critical Bifrost AI Gateway Flaw Lets Attackers Run Commands Without Credentials](https://thehackernews.com/2026/09/critical-bifrost-ai-gateway-flaw-lets.html)

### D-Link DIR-822A Router Zero-Day (CVE-2026-86296)
- **Description**: A maximum-severity zero-day vulnerability in legacy DIR-822A dual-band Wi-Fi routers with public proof-of-concept exploit code available. D-Link has confirmed no patch will be released for this end-of-life device.
- **Impact**: Complete router compromise, enabling network traffic interception, DNS hijacking, and use as a pivot point for internal network attacks.
- **Status**: Unpatched, end-of-life device. Public PoC exists. No vendor fix forthcoming.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: mitigate
- **CVE IDs**: CVE-2026-86296
- **Reporting**: [Bleeping Computer — D-Link warns of max severity zero-day bug in DIR-822A routers](https://www.bleepingcomputer.com/news/security/d-link-warns-of-max-severity-zero-day-bug-in-dir-822a-routers/)

### Linux Kernel ARM64 KVM Guest Escape (CVE-2026-89775)
- **Description**: A flaw in the Linux kernel's KVM virtualization code for ARM64 processors that exposes freed host memory to a guest virtual machine when nested virtualization is enabled. The researcher who discovered it confirms the bug can be used to escape the guest and execute code on the host.
- **Impact**: Virtual machine escape to host kernel code execution, compromising all guests on the host and the hypervisor itself.
- **Status**: CVE assigned. Patch status not specified in source. Requires nested virtualization enabled to exploit.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-89775
- **Reporting**: [The Hacker News — New Linux Kernel Flaw Gives ARM64 KVM Guests Read-Write Access to Host Memory](https://thehackernews.com/2026/09/new-linux-kernel-flaw-gives-arm64-kvm.html)

### SharePoint Server Authenticated RCE (CVE-2026-65660)
- **Description**: A SharePoint Server vulnerability initially misclassified by Microsoft as spoofing (CVSS 6.5) but actually enables authenticated remote code execution. Affects SharePoint Server 2016, 2019, and Subscription Edition. Technical details published by Viettel Cyber Security researcher Dinh Ho Anh Khoa.
- **Impact**: Authenticated attackers can achieve remote code execution on SharePoint servers, leading to data theft, lateral movement, and persistence.
- **Status**: Patches have been released by Microsoft.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-65660
- **Reporting**: [The Hacker News — SharePoint Flaw Initially Listed as Spoofing by Microsoft Enables Authenticated RCE](https://thehackernews.com/2026/09/sharepoint-flaw-initially-listed-as.html)

### BigDiskBuster / Windows Defender Zero-Day (CVE Not Provided)
- **Description**: A zero-day proof-of-concept tool (BigDiskBuster) released by researcher Abdelhamid Naceri (Nightmare Eclipse) that prevents Microsoft Defender from installing platform and signature updates by exhausting all available disk space. No patch, CVE, or Microsoft advisory exists.
- **Impact**: Persistent disablement of antivirus updates, leaving endpoints vulnerable to subsequent malware infections without detection capability refresh.
- **Status**: Unpatched zero-day with public PoC. No vendor acknowledgment or fix.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — Researcher Drops BigDiskBuster Zero-Day PoC That Blocks Microsoft Defender Updates](https://thehackernews.com/2026/09/researcher-drops-bigdiskbuster-zero-day.html), [Bleeping Computer — New Windows Defender zero-day blocks Microsoft antivirus updates](https://www.bleepingcomputer.com/news/security/new-windows-defender-zero-day-blocks-microsoft-antivirus-updates/)

### EvilTokens Device Code Phishing Service
- **Description**: A phishing-as-a-service platform (EvilTokens) that compromised over 12,000 Microsoft 365 accounts across 10,000+ organizations using device code authentication flows. The service used AI at every step of the attack chain. Microsoft's Digital Crimes Unit led a court-authorized takedown seizing 50 websites and disabling 150+ domains with support from Health-ISAC, Cloudflare, Coinbase, OpenAI, Railway, SpyCloud, and Shadowserver.
- **Impact**: Large-scale credential theft and persistent access to Microsoft 365 environments, enabling business email compromise, data exfiltration, and supply chain attacks.
- **Status**: Service disrupted via legal and technical takedown. Compromised accounts require remediation.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Dark Reading — Microsoft Disrupts EvilTokens Device Code Phishing Service](https://www.darkreading.com/identity-access-management-security/microsoft-disrupts-eviltokens-device-code-phishing-service), [The Hacker News — Microsoft Takes Down EvilTokens Device-Code Phishing Service Tied to 12,000 Inbox Compromises](https://thehackernews.com/2026/09/microsoft-takes-down-eviltokens-device.html), [Bleeping Computer — EvilTokens PhaaS disrupted after compromising 12,000 Microsoft accounts](https://www.bleepingcomputer.com/news/security/eviltokens-phaas-disrupted-after-compromising-12-000-microsoft-accounts/)

### Shai-Hulud / TanStack npm Supply Chain Attack
- **Description**: Threat actors stole 170 private GitHub repositories from cybersecurity firm CrowdSec using an OAuth token compromised from a former employee's computer through the TanStack npm supply chain attack. The campaign demonstrates downstream impact of developer-targeted supply chain compromises.
- **Impact**: Theft of proprietary source code, potential injection of malicious code into downstream dependencies, credential exposure.
- **Status**: Active campaign. OAuth token revoked; repositories compromised.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Dark Reading — Shai-Hulud Attack Nips Cyber-Firm CrowdSec's GitHub Data](https://www.darkreading.com/cyberattacks-data-breaches/shai-hulud-attack-cyber-firm-crowdsec-github-data)

### Malicious npm Package: tw-pkgprobe-7731
- **Description**: A malicious npm package masquerading as a Twilio bug-bounty security tool ("tw-pkgprobe-7731") uploaded in mid-August 2026 by account "twdepprobe7731." The package targets developers integrating Twilio and attempts to exfiltrate sensitive credentials.
- **Impact**: Credential theft from development environments, potential access to Twilio accounts and associated communications infrastructure.
- **Status**: Package removed from npm registry. Developers who installed it should rotate credentials.
- **Severity**: medium
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — Malicious npm Package Poses as Twilio Bug-Bounty Probe, Can Exfiltrate Credentials](https://thehackernews.com/2026/09/malicious-npm-package-poses-as-twilio.html)

### Malicious npm Package: indexed-btree
- **Description**: A malicious npm package ("indexed-btree") mimicking the legitimate "sorted-btree" package that hides its malicious loader within application runtime code rather than lifecycle scripts, indicating evolving evasion tactics against security controls.
- **Impact**: Supply chain compromise of applications incorporating the package; runtime code execution in production environments.
- **Status**: Package observed and removed. Detection requires runtime analysis rather than static dependency scanning.
- **Severity**: medium
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — Malicious npm Package indexed-btree Hid Its Loader in Runtime Code Before Removal](https://thehackernews.com/2026/09/malicious-npm-package-indexed-btree-hid.html)

### ClosedQuorum AI-Driven Windows Malware
- **Description**: A new Windows malware family (ClosedQuorum) that leverages multiple AI models (Google Gemini, DeepSeek, Qwen, Mistral) to autonomously determine post-compromise actions, representing a shift toward AI-orchestrated attack decision-making.
- **Impact**: Adaptive, resilient post-exploitation behavior that can dynamically respond to environment conditions and defensive measures.
- **Status**: Active malware family. No specific exploitation vector detailed; initial access method unspecified.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: monitor
- **Reporting**: [Bleeping Computer — New ClosedQuorum Windows malware uses AI for attack decisions](https://www.bleepingcomputer.com/news/security/new-closedquorum-windows-malware-uses-ai-for-attack-decisions/)

### Meta Muse AI Assistant Backdoor (macOS)
- **Description**: A proof-of-concept demonstrating that malware already running on a Mac can hijack Meta's Muse AI assistant by modifying a hidden setting, redirecting dictated prompts to the attacker instead of Meta. Requires pre-existing malware execution on the target system.
- **Impact**: Eavesdropping on voice dictation, potential command injection via voice interface, persistence mechanism leveraging legitimate AI assistant permissions.
- **Status**: Proof-of-concept only. No active exploitation reported. Requires initial compromise.
- **Severity**: medium
- **Exploitation Status**: potential
- **Action**: monitor
- **Reporting**: [The Hacker News — One Hidden Meta Muse Setting Could Let Attackers Turn the AI Assistant Into a Backdoor](https://thehackernews.com/2026/09/one-hidden-meta-muse-setting-could-let.html)

## Affected Systems and Products

- **Check Point Security Management Server**: All versions prior to September 22, 2026 hotfix. Platform: Network security management appliances controlling firewall policies.
- **VeloCloud Orchestrator (VCO)**: On-premises deployments configured for certificate-based Edge authentication. Platform: VMware/Arista SD-WAN management servers.
- **Zyxel GS1900 Series Smart Managed Switches**: Vulnerable firmware versions prior to vendor patch. Platform: Network switching equipment deployed in enterprise and government environments.
- **WordPress Core**: All versions from 4.7 through 7.1.1 (for CVE-2026-93485) and through 7.1.1 (for critical core flaw patched in 7.1.2). Platform: Web servers running WordPress CMS.
- **Oracle PeopleSoft**: Versions affected by undisclosed zero-day. Platform: Enterprise ERP and HR systems.
- **Bifrost AI Gateway**: All versions before 2.1.0 with management authentication enabled. Platform: Open-source AI inference gateway servers routing to 20+ LLM providers.
- **D-Link DIR-822A Dual-Band Wi-Fi Routers**: End-of-life legacy routers. No patch available. Platform: Consumer/small business networking equipment.
- **Linux Kernel KVM (ARM64)**: Versions with vulnerable KVM virtualization code when nested virtualization is enabled. Platform: ARM64 hypervisors hosting virtual machines.
- **Microsoft SharePoint Server**: 2016, 2019, and Subscription Edition. Platform: On-premises SharePoint deployments.
- **Microsoft Defender / Windows**: All versions susceptible to disk-space exhaustion attack (BigDiskBuster). Platform: Windows endpoints with Microsoft Defender.
- **Microsoft 365 / Entra ID**: Accounts targeted by EvilTokens device code phishing. Platform: Cloud identity and productivity suite.
- **GitHub / npm Ecosystem**: Repositories and packages affected by TanStack supply chain attack and malicious packages (tw-pkgprobe-7731, indexed-btree). Platform: Developer build environments and CI/CD pipelines.
- **Meta Muse Assistant**: macOS installations with Muse assistant granted microphone access. Platform: Apple macOS desktop systems.

## Attack Vectors and Techniques

- **Device Code Phishing (OAuth Device Authorization Flow)**: EvilTokens abused the OAuth device code flow to phish Microsoft 365 credentials without traditional credential harvesting pages. AI automated lure generation, token capture, and session persistence across 10,000+ organizations.
- **Unauthenticated Remote Code Execution via Web Management Interfaces**: Check Point (CVE-2026-93616), VeloCloud (CVE-2026-93952), and Bifrost (CVE-2026-90898) all expose management web services that allow unauthenticated script/command execution.
- **Stored XSS to RCE via Privileged User Interaction**: WordPress Comment2Shell (CVE-2026-93485) plants malicious scripts in comments that execute only when an administrator views the page, bridging unauthenticated input to authenticated code execution.
- **Network Device Buffer Overflow for Command Execution**: Zyxel GS1900 (CVE-2026-7273) stack-based buffer overflow yields arbitrary OS command execution on switching infrastructure.
- **Supply Chain Compromise via Malicious npm Packages**: Both typosquatting (indexed-btree mimicking sorted-btree) and social engineering (tw-pkgprobe-7731 posing as bug-bounty tool) deliver credential stealers to developer machines.
- **OAuth Token Theft from Developer Endpoints**: Shai-Hulud campaign stole a former employee's OAuth token from a compromised computer, then accessed 170 private GitHub repositories.
- **Virtual Machine Escape via Kernel Use-After-Free**: Linux KVM flaw (CVE-2026-89775) on ARM64 with nested virtualization allows guest VMs to read/write freed host kernel memory, achieving hypervisor escape.
- **AI-Orchestrated Post-Exploitation**: ClosedQuorum malware queries multiple LLM APIs (Gemini, DeepSeek, Qwen, Mistral) to autonomously decide lateral movement, persistence, and data collection actions.
- **Disk Exhaustion for Security Evasion**: BigDiskBuster fills disk space to prevent Microsoft Defender signature and platform updates, creating a persistent blind spot.
- **Legacy Device Exploitation with Public PoC**: D-Link DIR-822A (CVE-2026-86296) exploits end-of-life routers with no patch path, using publicly available exploit code.
- **Spear-Phishing with Living-off-the-Land Binaries**: SideCopy uses mshta.exe to execute malicious scripts via phishing lures targeting Indian academic institutions, deploying ReverseRAT.
- **AI Assistant Permission Abuse**: Meta Muse PoC shows how broad microphone/accessibility permissions granted to AI assistants can be repurposed as a covert channel by local malware.

## Threat Actor Activities

- **Chinese-Speaking Threat Actor (Government Data Theft)**: Actively exploiting Zyxel GS1900 switches (CVE-2026-7273) and WordPress vulnerabilities to compromise 996 devices and exfiltrate over 18,500 records from government backend databases. CISA KEV listing confirms active exploitation.
- **ShinyHunters Extortion Group**: Claims breach of FBI systems via Oracle PeopleSoft zero-day, stealing employee and applicant data. Known for high-profile data theft and extortion campaigns against corporate and government targets.
- **EvilTokens Operators (Phishing-as-a-Service)**: Ran a commercial PhaaS platform compromising 12,000+ Microsoft 365 accounts across 10,000+ organizations. Leveraged AI for lure crafting, device code flow abuse, and infrastructure management. Disrupted by Microsoft DCU with multi-industry coalition.
- **SideCopy (APT)**: Pakistan-nexus threat actor expanding targeting from Indian government entities to academic institutions. Uses spear-phishing with mshta.exe execution and ReverseRAT payload for persistent access.
- **Shai-Hulud / TanStack Supply Chain Actors**: Compromised npm supply chain to steal OAuth tokens from developer machines, then accessed 170 private GitHub repositories belonging to cybersecurity firm CrowdSec.
- **Abdelhamid Naceri (Nightmare Eclipse)**: Former Microsoft security researcher publicly releasing Microsoft Defender zero-day exploits (BigDiskBuster and prior Defender exploits used in-the-wild). Demonstrates insider knowledge of AV internals.
- **Unknown Actors (VeloCloud Exploitation)**: Actively exploiting CVE-2026-93952 in certificate-configured VeloCloud Orchestrators. Attribution not provided in source material.
- **Malicious npm Publishers**: Operators of "twdepprobe7731" account and indexed-btree package conducting targeted credential theft against Twilio developers and generic supply chain compromise respectively.