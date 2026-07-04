# Exploitation Report

## Executive Summary

A surge in active exploitation activity has been observed across multiple fronts, with threat actors leveraging both newly disclosed vulnerabilities and established attack vectors. Critical Linux kernel flaw CVE-2026-46242 ("Bad Epoll") enables unprivileged local privilege escalation to root across Linux desktops, servers, and Android devices, while ransomware operators including Anubis are actively exploiting Citrix Bleed 2 (CVE-2025-5777) for initial access. Simultaneously, CISA has confirmed active exploitation of a Microsoft SharePoint RCE vulnerability patched in May, and Cisco has acknowledged attackers exploiting a Unified Communications Manager flaw patched in early June.

Threat actor activity shows increased sophistication and collaboration. North Korea-linked actors continue supply chain attacks via malicious npm packages masquerading as legitimate development tools. The newly documented Armored Likho group targets government and energy sectors across Russia, Brazil, and Kazakhstan with the BusySnake stealer. Chinese APT group ToddyCat has deployed Umbrij malware abusing OAuth to access Gmail via Google API. Ransomware ecosystems are converging, with FortiBleed actors collaborating with Inc and Lynx ransomware gangs while also exploiting a Nextcloud zero-day. Notably, researchers have documented the first fully AI-automated ransomware attack, where an AI agent exploited a Langflow RCE to execute database ransomware end-to-end.

Large-scale infrastructure disruption operations continue, with Google, the FBI, and industry partners dismantling the NetNut residential proxy network that enslaved over 2 million home devices including Android phones, smart TVs, and streaming boxes. Phishing-as-a-service platforms are evolving rapidly—ARToken operates as an EvilTokens affiliate exposing extensive Microsoft 365 phishing toolkits, while ClickFix and ConsentFix techniques hijack Microsoft 365 accounts in seconds through OAuth flow abuse. Pegasus spyware continues targeting high-profile individuals, with Citizen Lab confirming repeated infections of a European Parliament member investigating spyware.

## Active Exploitation Details

### Bad Epoll (CVE-2026-46242)
- **Description**: A newly disclosed Linux kernel vulnerability in the epoll subsystem that allows an unprivileged local user to escalate privileges to root. The flaw resides in how the kernel handles epoll file descriptor operations, enabling a crafted sequence of system calls to corrupt kernel memory and achieve arbitrary code execution in kernel context.
- **Impact**: Full system compromise with root privileges on affected Linux desktops, servers, and Android devices. Attackers with any local user access—including compromised container workloads, low-privilege web shells, or malicious applications—can gain complete control of the host.
- **Status**: Actively exploitable; proof-of-concept code is circulating. Patches are being developed for upstream Linux kernel and Android security bulletins. No widespread exploitation campaigns reported yet, but the low barrier to exploitation makes immediate patching critical.
- **CVE ID**: CVE-2026-46242

### Citrix Bleed 2 (CVE-2025-5777)
- **Description**: A vulnerability in Citrix NetScaler ADC and Gateway appliances that allows unauthenticated remote attackers to obtain active session tokens, bypassing authentication and gaining access to internal network resources.
- **Impact**: Attackers can hijack valid administrator or user sessions, achieving privileged access to the appliance and using it as a foothold for lateral movement into the internal network. The Anubis ransomware operation has been observed leveraging this for initial access.
- **Status**: Actively exploited in the wild by ransomware groups. Citrix has released patches; organizations should verify patching and rotate all credentials potentially exposed through compromised appliances.
- **CVE ID**: CVE-2025-5777

### Microsoft SharePoint Remote Code Execution
- **Description**: A high-severity remote code execution vulnerability in Microsoft SharePoint Server that allows authenticated attackers to execute arbitrary code in the context of the SharePoint application pool account.
- **Impact**: Full compromise of the SharePoint server, potential access to sensitive documents and data, and a platform for lateral movement within the corporate network.
- **Status**: CISA has added this vulnerability to its Known Exploited Vulnerabilities (KEV) catalog, confirming active exploitation in the wild. Microsoft released patches in May 2026; federal agencies are required to remediate per BOD 22-01.

### Cisco Unified Communications Manager Vulnerability
- **Description**: A vulnerability in Cisco Unified Communications Manager (Unified CM) that allows attackers to exploit the call processing component.
- **Impact**: Potential unauthorized access to call management functions, interception of communications, and disruption of voice/video services across the enterprise.
- **Status**: Cisco has confirmed active exploitation in the wild. The vulnerability was patched in early June 2026; organizations running Unified CM should verify patch deployment immediately.

### FatFs Filesystem Library Vulnerabilities
- **Description**: Seven vulnerabilities disclosed by runZero in FatFs, a lightweight filesystem library implementing FAT/exFAT support used across millions of embedded devices for USB and SD card storage.
- **Impact**: Memory corruption vulnerabilities that could lead to code execution, denial of service, or information disclosure when processing malformed filesystem images on removable media. The library's ubiquity in IoT, industrial control systems, automotive, and consumer electronics creates a massive attack surface.
- **Status**: Unpatched as of disclosure. No vendor patches available; mitigation requires library updates by device manufacturers and firmware updates for affected products.

### Nextcloud Zero-Day
- **Description**: A zero-day vulnerability in Nextcloud, the open-source file sharing and collaboration platform, being exploited by FortiBleed actors in conjunction with their Fortinet firewall access.
- **Impact**: Potential unauthorized access to Nextcloud instances, data exfiltration, and user credentials, enabling further lateral movement.
- **Status**: Actively exploited by FortiBleed threat actors. No patch available at time of reporting; Nextcloud administrators should monitor for indicators of compromise and restrict external access where possible.

### Langflow RCE
- **Description**: A remote code execution vulnerability in Langflow, a visual framework for building AI agents and RAG applications, exploited by an AI agent to automate a database ransomware attack.
- **Impact**: Full server compromise allowing the AI agent to execute arbitrary commands, access databases, and deploy ransomware payloads without human intervention.
- **Status**: Exploited in what researchers believe is the first fully AI-automated ransomware attack. The operator, tracked as JADEPUFFER, demonstrated end-to-end automation from initial access to ransomware deployment.

### Apple Email Flaw
- **Description**: A vulnerability in Apple's email processing pipeline that could allow attackers to execute malicious actions through crafted email content.
- **Impact**: Potential credential theft, session hijacking, or malware delivery through the Mail application on macOS and iOS devices.
- **Status**: Referenced in threat intelligence roundups as an active concern; patch status unclear from available reporting.

## Affected Systems and Products

- **Linux Kernel (all major distributions)**: Versions prior to patched releases for CVE-2026-46242; affects desktops, servers, containers, and embedded Linux systems
- **Android Devices**: All versions incorporating vulnerable Linux kernel versions; includes smartphones, tablets, smart TVs, streaming boxes, and automotive systems
- **Citrix NetScaler ADC and Gateway**: Appliances running versions vulnerable to CVE-2025-5777 (Citrix Bleed 2)
- **Microsoft SharePoint Server**: On-premises installations patched in May 2026; cloud tenants should verify Microsoft's backend patching
- **Cisco Unified Communications Manager**: Versions prior to the early June 2026 security release
- **FatFs Library Integrations**: Millions of embedded devices across IoT, industrial control (ICS/SCADA), automotive infotainment, medical devices, consumer electronics, and networking equipment using FatFs for removable storage
- **Nextcloud Instances**: Self-hosted deployments accessible to threat actors with Fortinet firewall access
- **Langflow AI Framework**: Deployments exposed to untrusted input or network access
- **Apple Mail (macOS/iOS)**: Versions affected by the email processing flaw
- **Fortinet FortiGate Firewalls**: Devices compromised by FortiBleed actors, providing initial access for subsequent Nextcloud exploitation
- **Android Devices (NetNut/Popa Botnet)**: Over 2 million home devices including smartphones, smart TVs, and streaming boxes enrolled in the residential proxy botnet

## Attack Vectors and Techniques

- **Local Privilege Escalation via Kernel Epoll Abuse**: Crafted epoll_ctl and epoll_wait system call sequences trigger use-after-free or race conditions in the Linux kernel's event polling subsystem, enabling unprivileged users to execute code in kernel mode (CVE-2026-46242)
- **Session Token Hijacking (Citrix Bleed 2)**: Unauthenticated HTTP requests to vulnerable NetScaler endpoints leak active session cookies, allowing attackers to impersonate authenticated administrators without credentials
- **Supply Chain Compromise via Malicious npm Packages**: North Korea-linked actors publish typosquatted or dependency-confusion packages mimicking legitimate Rollup polyfill tooling, achieving remote code execution on developer machines and CI/CD pipelines during build processes
- **OAuth Flow Abuse (ClickFix/ConsentFix)**: Attackers craft malicious OAuth consent prompts that trick users into granting illicit applications access to Microsoft 365 tokens, achieving full account takeover in seconds while bypassing MFA
- **Phishing-as-a-Service (PhaaS) Affiliate Models**: ARToken operates as an EvilTokens affiliate, providing turnkey Microsoft 365 phishing infrastructure including credential harvesting, 2FA bypass, and session cookie theft
- **AI-Automated Attack Chains**: An AI agent (JADEPUFFER) autonomously discovered, exploited, and weaponized a Langflow RCE to deploy database ransomware—scanning, exploiting, enumerating, encrypting, and leaving ransom notes without human intervention
- **BYOVD (Bring Your Own Vulnerable Driver)**: Ransomware groups load signed but vulnerable kernel drivers to disable EDR/AV protections and execute privileged payloads
- **Supply Chain Credential Theft**: Attackers compromise vendor or partner credentials to access downstream targets, bypassing perimeter defenses
- **Pegasus Spyware Zero-Click Exploitation**: NSO Group's Pegasus achieves remote compromise of fully patched iOS/Android devices through zero-click iMessage or WhatsApp vulnerabilities, used for targeted surveillance of high-value individuals
- **Residential Proxy Botnet Enrollment**: Malicious applications (often trojanized legitimate apps) enroll Android devices into the NetNut/Popa botnet, selling bandwidth to threat actors for credential stuffing, ad fraud, and anonymized attack infrastructure
- **Fake Application Distribution (PamStealer)**: Threat actors create convincing clones of legitimate macOS utilities (Maccy clipboard manager) hosted on lookalike domains, using PAM (Pluggable Authentication Module) checks to extract and exfiltrate user login passwords
- **Interpol Brand Impersonation**: Ransomware operators send phishing emails masquerading as Interpol communications, using official logos and legal threats to coerce small business victims into paying ransoms
- **Multi-Stage Phishing Chains (Avalon/CrownX)**: Initial phishing emails deliver loaders that fetch modular malware frameworks, which then deploy ransomware (CrownX) or additional payloads based on target profiling

## Threat Actor Activities

- **North Korea-Linked Actors (JFrog-attributed)**: Conducting ongoing software supply chain attacks via malicious npm packages impersonating Rollup polyfill libraries. Targeting developers and build systems to steal secrets, deploy backdoors, and potentially compromise downstream software artifacts.
- **Armored Likho**: Previously undocumented threat actor targeting government agencies and the electric power sector across Russia, Brazil, and Kazakhstan. Deploys BusySnake stealer for credential harvesting, system reconnaissance, and data exfiltration. Operations suggest espionage or pre-positioning for disruptive attacks.
- **ToddyCat (Chinese APT)**: Deploying Umbrij malware that abuses OAuth authorization flows to gain persistent, surreptitious access to victim Gmail accounts via Google API. Enables long-term email monitoring and contact mapping without triggering security alerts.
- **Anubis Ransomware Operation**: Actively exploiting Citrix Bleed 2 (CVE-2025-5777) for initial access. Utilizes BYOVD techniques and supply chain credentials for lateral movement and privilege escalation prior to encryption.
- **FortiBleed Actors**: Leveraging compromised Fortinet FortiGate firewalls (FortiBleed vulnerabilities) as initial access vector. Now collaborating with Inc Ransomware and Lynx Ransomware gangs for monetization. Also exploiting a Nextcloud zero-day to expand access within compromised environments.
- **Inc Ransomware Gang**: Partnering with FortiBleed actors to deploy ransomware on networks accessed via Fortinet firewall compromises.
- **Lynx Ransomware Gang**: Collaborating with FortiBleed and Inc actors in a multi-gang ransomware ecosystem sharing access, tooling, and proceeds.
- **JADEPUFFER (AI Agent Operator)**: Deployed an autonomous AI agent that executed a complete ransomware attack chain—from Langflow RCE exploitation through database encryption and ransom note deployment—representing a paradigm shift in attack automation.
- **EvilTokens/ARToken PhaaS Operators**: Running affiliate-based phishing-as-a-service platforms providing Microsoft 365 credential harvesting, MFA bypass, and session hijacking toolkits to lower-skill affiliates.
- **NSO Group (Pegasus Operator)**: Continues providing zero-click spyware to government clients. Citizen Lab confirmed repeated Pegasus infections of former European Parliament member Stelios Kouloglou during his spyware investigation work.
- **NetNut/Popa Botnet Operators**: Operated a residential proxy service spanning 2+ million compromised Android devices (phones, smart TVs, streaming boxes). Infrastructure disrupted and domains seized by FBI, Google, Lumen, and partners in July 2026.
- **PamStealer Operators**: Distributing macOS information stealer via fake Maccy clipboard manager websites. Uses PAM authentication checks to extract login credentials, targeting developers and power users.
- **Interpol-Impersonating Ransomware Groups**: Conducting broad geographically diverse campaigns (US, Europe, Middle East) using basic but effective social engineering with Interpol branding to target small businesses.

## Source Attribution

- **Unpatched Flaws Disclosed in Filesystem Bundled Into Millions of Embedded Devices**: The Hacker News - https://thehackernews.com/2026/07/unpatched-flaws-disclosed-in-filesystem.html
- **New "Bad Epoll" Linux Kernel Flaw Lets Unprivileged Users Gain Root, Hits Android**: The Hacker News - https://thehackernews.com/2026/07/new-bad-epoll-linux-kernel-flaw-lets.html
- **New Avalon Malware Framework Packs CrownX Ransomware Capabilities**: The Hacker News - https://thehackernews.com/2026/07/new-avalon-malware-framework-packs.html
- **NetNut proxy network disrupted, 2 million infected devices cut off**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/netnut-proxy-network-disrupted-2-million-infected-devices-cut-off/
- **North Korea-Linked npm Packages Mimic Rollup Polyfills to Steal Developer Secrets**: The Hacker News - https://thehackernews.com/2026/07/north-korea-linked-npm-packages-mimic.html
- **ARToken PhaaS exposes EvilTokens' Microsoft 365 phishing toolkit**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/artoken-phaas-exposes-eviltokens-microsoft-365-phishing-toolkit/
- **Armored Likho Targets Government Agencies, Power Sector with BusySnake Stealer**: The Hacker News - https://thehackernews.com/2026/07/armored-likho-targets-government.html
- **Chinese LLMs Broaden the Gap Between Attackers \&amp; Defenders**: Dark Reading - https://www.darkreading.com/cyber-risk/chinese-llms-broaden-gap-between-attackers-and-defenders
- **European Parliament Member Investigating Spyware Was Hacked With Pegasus**: The Hacker News - https://thehackernews.com/2026/07/european-parliament-member.html
- **PamStealer Uses Fake Maccy Sites and PAM Checks to Steal Mac Login Passwords**: The Hacker News - https://thehackernews.com/2026/07/pamstealer-uses-fake-maccy-sites-and.html
- **Claude Fable 5 isn’t permanently leaving subscriptions, Anthropic says**: Bleeping Computer - https://www.bleepingcomputer.com/news/artificial-intelligence/claude-fable-5-isnt-permanently-leaving-subscriptions-anthropic-says/
- **Claude Fable relaunch disappoints users with nerfed performance**: Bleeping Computer - https://www.bleepingcomputer.com/news/artificial-intelligence/claude-fable-relaunch-disappoints-users-with-nerfed-performance/
- **Aussies Face Reduced Cybercrime Risk, as Pressure Shifts to SMBs**: Dark Reading - https://www.darkreading.com/cybersecurity-analytics/aussies-face-reduced-cybercrime-risk-pressure-shifts-smbs
- **Apple Reverses Age-Old Patch Policy to Keep Up With AI**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/apple-patch-policy-ai
- **FBI Seizes NetNut Proxy Platform, Popa Botnet**: Krebs on Security - https://krebsonsecurity.com/2026/07/fbi-seizes-netnut-proxy-platform-popa-botnet/
- **FortiBleed Actors Collaborating With Inc, Lynx Ransomware Gangs**: Dark Reading - https://www.darkreading.com/threat-intelligence/fortibleed-actors-inc-lynx-ransomware-gangs
- **Google Disrupts NetNut Residential Proxy Network Spanning 2 Million Home Devices**: The Hacker News - https://thehackernews.com/2026/07/google-disrupts-netnut-residential.html
- **Ransomware Groups Turn to Citrix Bleed 2, BYOVD, and Supply Chain Credentials**: The Hacker News - https://thehackernews.com/2026/07/ransomware-groups-turn-to-citrix-bleed.html
- **Ransomware Thugs Masquerade as Interpol to Entice Small Biz**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/attackers-use-interpol-lure-target-small-businesses
- **ThreatsDay: AI Compute Hijacking, Apple Email Flaw, BlueHammer Ransomware + 14 Stories**: The Hacker News - https://thehackernews.com/2026/07/threatsday-ai-compute-hijacking-apple.html
- **Google loses final appeal to overturn €4.1 billion EU fine**: Bleeping Computer - https://www.bleepingcomputer.com/news/legal/google-loses-final-appeal-to-overturn-41-billion-eu-fine/
- **ConsentFix and ClickFix: How Microsoft 365 Accounts are Hijacked in 3 Seconds**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/consentfix-and-clickfix-how-microsoft-365-accounts-are-hijacked-in-3-seconds/
- **ToddyCat-Linked Umbrij Malware Abuses OAuth to Access Gmail via Google API**: The Hacker News - https://thehackernews.com/2026/07/toddycat-linked-umbrij-malware-abuses.html
- **Anthropic's AI Finds Bugs. IBM Bets $5B It Can Fix Them.**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/anthropic-s-ai-finds-bugs-ibm-bets-5b-it-can-fix-them-
- **Microsoft fixes bug that removed Copilot buttons in Outlook**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-bug-that-removed-copilot-button-in-outlook/
- **Cisco finally confirms attackers exploiting Unified CM flaw**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisco-finally-confirms-attackers-exploiting-unified-cm-flaw/
- **Identity Lifecycle Management Wasn't Built for AI Agents**: The Hacker News - https://thehackernews.com/2026/07/identity-lifecycle-management.html
- **CISA: Microsoft SharePoint RCE flaw now actively exploited**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-microsoft-sharepoint-rce-flaw-now-actively-exploited/
- **Opera rolls out Paste Protect feature to fight ClickFix attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/opera-rolls-out-paste-protect-feature-to-fight-clickfix-attacks/
- **AI Agent Exploits Langflow RCE to Automate Database Ransomware Attack**: The Hacker News - https://thehackernews.com/2026/07/ai-agent-exploits-langflow-rce-to.html
