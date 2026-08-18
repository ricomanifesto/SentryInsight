---
schema_version: 2
report_date: 2026-08-18
generated_at: 2026-08-18T01:30:40Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-08-18/
---
# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse platforms, from mobile modem firmware and enterprise software to cloud infrastructure and AI agent frameworks. A two-stage exploit chain targeting Unisoc modem firmware enables full Android kernel access via a simple VoLTE video call, with no patch available from the chipset vendor. Simultaneously, recently patched flaws in VMware vCenter (CVE-2026-59310), SAP Commerce Cloud (CVE-2026-58231), and Apple macOS Screen Sharing (CVE-2026-65400) are being actively weaponized—by a suspected China-nexus APT deploying Babuk-derived ransomware, by opportunistic actors within days of disclosure, and to install Monero miners on internet-exposed Macs, respectively.

Critical unauthenticated remote code execution vulnerabilities have been disclosed in widely deployed software including GitLab (CVE-2026-19478, CVSS 9.4), Forminator WordPress plugin (CVE-2026-15748, CVSS 9.8, 600,000+ installations), and SAP Commerce Cloud (CVE-2026-58231, CVSS 10.0). The Microsoft Defender "ShieldBreak" zero-day (CVE-2026-69414) remains unpatched while Microsoft develops a fix. Meanwhile, the Mirai-derived Evooo1Bot Linux botnet is actively exploiting known flaws in edge devices to build SOCKS5 proxy infrastructure, and Iranian nation-state actors continue evolving the Cavern C2 framework using DNS and Google Apps Script for stealthy communications.

Supply chain and identity attacks are escalating: compromised credentials enabled theft of 3.6 million Azure account records from Fortune 500 companies, while Clop ransomware claims breaches at GE and Philips. Third-party breaches at CEVA Logistics (Pokémon Center) and a French tax authority contractor exposed hundreds of thousands of records. The Model Context Protocol (MCP) adoption in enterprise AI introduces new attack surfaces through plaintext configuration files, over-permissioned access, and prompt injection. New macOS malware AmnesiaStealer hijacks browser sessions via ClickFix attacks, demonstrating continued innovation in information-stealing techniques.

## Active Exploitation Details

### Unisoc VoLTE Video Call Exploit Chain
- **Description**: A two-stage exploit chain combining two vulnerabilities in Unisoc modem firmware that achieves full Android kernel access when a victim answers a VoLTE video call. The first stage (disclosed March 2026) provided remote code execution in the modem; the second stage (published August 17, 2026) escalates to kernel privilege. No fix is available from the chipset maker.
- **Impact**: Attackers gain full kernel-level control over Android devices running Unisoc modems simply by placing a video call that the victim answers—no user interaction beyond answering required.
- **Status**: Exploit chain publicly disclosed by SSD Secure Disclosure; no vendor patch available.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [Dark Reading — Video Call Exploit Chains Two Flaws in Unisoc Modems](https://www.darkreading.com/mobile-security/video-call-exploit-chains-two-flaws-unisoc-modems), [The Hacker News — Unisoc VoLTE Video Call Exploit Chain Can Give Attackers Full Android Kernel Access](https://thehackernews.com/2026/08/unisoc-volte-video-call-exploit-chain.html)

### GitLab GraphQL Authorization Bypass
- **Description**: A critical vulnerability in GitLab Community Edition and Enterprise Edition GraphQL API that allows unauthenticated attackers to remotely modify or delete public projects and user data under certain conditions.
- **Impact**: Unauthenticated remote modification or deletion of public projects and user data.
- **Status**: Security updates released by GitLab; patch available.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-19478
- **Reporting**: [The Hacker News — Critical GitLab GraphQL Flaw Could Let Unauthenticated Attackers Delete Public Projects](https://thehackernews.com/2026/08/critical-gitlab-graphql-flaw-could-let.html)

### Forminator WordPress Plugin Unauthenticated RCE
- **Description**: Critical security flaw in Forminator Forms WordPress plugin (600,000+ active installations) enabling arbitrary code execution through malicious PHP file uploads without authentication.
- **Impact**: Full remote code execution on vulnerable WordPress sites leading to complete site compromise.
- **Status**: Vulnerability disclosed; patch status unclear from article.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-15748
- **Reporting**: [The Hacker News — Forminator WordPress Flaw Can Enable Unauthenticated RCE via Malicious PHP Uploads](https://thehackernews.com/2026/08/forminator-wordpress-flaw-can-enable.html)

### VMware vCenter Directory Traversal (CVE-2026-59310)
- **Description**: Severe directory-traversal vulnerability in VMware vCenter Server (CVSS 9.8) that allows unauthenticated remote code execution. Actively exploited by a suspected China-nexus APT group to deploy Babuk-derived ransomware.
- **Impact**: Arbitrary code execution on vCenter servers leading to ransomware deployment and full infrastructure compromise.
- **Status**: Newly patched by Broadcom; active exploitation confirmed in the wild.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-59310
- **Reporting**: [The Hacker News — Suspected China-Nexus Actor Exploits VMware vCenter Flaw, Deploys Babuk-Derived Ransomware](https://thehackernews.com/2026/08/suspected-china-nexus-actor-exploits.html)

### SAP Commerce Cloud Authorization Bypass
- **Description**: Maximum-severity vulnerability (CVSS 10.0) involving insufficient authorization checks and input validation that allows unauthenticated attackers to abuse a default authentication client and submit malicious requests.
- **Impact**: Unauthenticated attackers can compromise SAP Commerce Cloud instances.
- **Status**: Patched by SAP; active exploitation attempts observed within days of patch release.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-58231
- **Reporting**: [The Hacker News — SAP Commerce Cloud CVE-2026-58231 Targeted in Exploitation Attempts Days After Patch](https://thehackernews.com/2026/08/sap-commerce-cloud-cve-2026-58231.html)

### Apple macOS Screen Sharing Authentication Bypass
- **Description**: Critical authentication issue (CVSS 9.8) in macOS Screen Sharing component that allows an attacker already on the network to bypass authentication and gain remote access. Actively exploited to deploy Monero cryptocurrency miners on internet-exposed Macs.
- **Impact**: Unauthorized remote access leading to cryptocurrency miner deployment; potential for further compromise.
- **Status**: Recently patched by Apple; active exploitation in the wild confirmed by NCSC-NL.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-65400
- **Reporting**: [The Hacker News — Apple macOS Screen Sharing Flaw Exploited on Internet-Exposed Macs to Install Monero Miner](https://thehackernews.com/2026/08/apple-macos-screen-sharing-flaw.html)

### Microsoft Defender ShieldBreak Zero-Day
- **Description**: Zero-day vulnerability in Microsoft Defender (tracked as CVE-2026-69414) disclosed by researcher "Nightmare Eclipse" that allows bypass of Defender protections.
- **Impact**: Potential bypass of endpoint protection enabling malware execution and persistence.
- **Status**: Microsoft confirmed working on security patch; no patch available yet.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: mitigate
- **CVE IDs**: CVE-2026-69414
- **Reporting**: [Bleeping Computer — Microsoft working on Defender patch for ShieldBreak zero-day](https://www.bleepingcomputer.com/news/security/microsoft-working-on-defender-patch-for-shieldbreak-zero-day/)

### Certighost Enterprise CA Privilege Escalation
- **Description**: Vulnerability (CVE-2026-54121) allowing a standard domain user to convert an Enterprise Certificate Authority into a Domain Controller, effectively escalating to Tier 0 identity infrastructure compromise.
- **Impact**: Full domain compromise through PKI abuse; standing privilege and implicit trust exploitation.
- **Status**: Patch available; article emphasizes the lesson around standing privilege.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-54121
- **Reporting**: [Bleeping Computer — Certighost and the Privilege Hiding in Your Certificate Authority](https://www.bleepingcomputer.com/news/security/certighost-and-the-privilege-hiding-in-your-certificate-authority/)

### Snowflake GitHub Actions Command Injection
- **Description**: GitHub Actions workflow injection vulnerability in Snowflake's public snowflakedb/snowflake-connector-net repository (.github/workflows/jira_issue.yml) that executes when a crafted GitHub issue is created, allowing command execution with internal Jira credentials.
- **Impact**: Command execution in CI/CD pipeline with access to internal Jira credentials; potential supply chain compromise.
- **Status**: Disclosed by Wiz researchers; remediation status not specified.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: investigate
- **Reporting**: [The Hacker News — Snowflake GitHub Actions Flaw Lets Crafted Issues Trigger Command Injection](https://thehackernews.com/2026/08/snowflake-github-actions-flaw-lets_0330881554.html)

### Evooo1Bot Linux Botnet Exploitation
- **Description**: Mirai-derived modular Linux botnet actively exploiting known vulnerabilities in internet-facing gateway devices (routers, edge devices) to compromise them and convert into SOCKS5 proxy relay nodes. Extends Mirai with exploitation modules, credential theft, and reverse SOCKS relays.
- **Impact**: Persistent attacker infrastructure via compromised edge devices; credential theft; traffic relay for further attacks.
- **Status**: Active campaigns observed; exploits known/patched flaws.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Dark Reading — Linux Botnet Evooo1Bot Expands Mirai Capabilities Well Beyond DDoS](https://www.darkreading.com/cyber-risk/linux-botnet-evooo1bot-mirai-capabilities-beyond-ddos), [The Hacker News — Evooo1Bot Linux Botnet Exploits Known Flaws to Turn Edge Devices Into SOCKS5 Proxies](https://thehackernews.com/2026/08/evooo1bot-linux-botnet-exploits-known.html), [Bleeping Computer — New Evooo1Bot Linux botnet turns routers into traffic relay nodes](https://www.bleepingcomputer.com/news/security/new-evooo1bot-linux-botnet-turns-routers-into-traffic-relay-nodes/)

### Cavern C2 Framework Evolution
- **Description**: Iranian nation-state hackers' command-and-control framework (Cavern/Cav3rn) evolved with new components using DNS tunneling and Google Apps Script to blend into legitimate traffic, targeting entities in Israel since December 2025.
- **Impact**: Stealthy, persistent C2 communications evading detection; used in espionage and destructive attacks.
- **Status**: Ongoing threat activity cluster monitored by Kaspersky; new unreported components discovered.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [The Hacker News — Cavern C2 Uses DNS and Google Apps Script to Blend Into Legitimate Traffic](https://thehackernews.com/2026/08/cavern-c2-uses-dns-and-google-apps.html)

### AmnesiaStealer macOS Malware
- **Description**: New information-stealing malware targeting macOS users via ClickFix social engineering attacks, featuring a streaming module for interactive remote control of victim's web browser sessions.
- **Impact**: Browser session hijacking, credential theft, interactive attacker control of victim browser.
- **Status**: Active distribution via ClickFix campaigns.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — New AmnesiaStealer macOS malware hijacks browser sessions via remote control](https://www.bleepingcomputer.com/news/security/new-amnesiastealer-macos-malware-hijacks-browser-sessions-via-remote-control/)

### Clop Ransomware Campaign
- **Description**: Clop ransomware gang claims breaches at General Electric and Philips with data theft; both companies investigating.
- **Impact**: Data exfiltration and potential ransomware deployment at major industrial/tech organizations.
- **Status**: Active claims under investigation by victims.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Philips and GE investigating Clop ransomware data theft claims](https://www.bleepingcomputer.com/news/security/philips-and-ge-investigating-clop-ransomware-data-theft-claims/)

### Azure Credential Compromise Campaign
- **Description**: Threat actor selling employee databases allegedly stolen from Microsoft Azure infrastructure of multiple Fortune 500 companies using compromised credentials; 3.6 million records claimed.
- **Impact**: Large-scale credential theft and corporate data exposure across multiple major organizations.
- **Status**: Actor actively selling data; compromise method confirmed as credential reuse/theft.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Hacker claims 3.6 million Azure account records stolen from major companies](https://www.bleepingcomputer.com/news/security/hacker-claims-36-million-azure-account-records-stolen-from-major-companies/)

### MCP Server Exposure
- **Description**: Model Context Protocol (MCP) servers exposing enterprise secrets through plaintext configuration files, over-permissioned access, and prompt injection—often before security teams know the servers are running.
- **Impact**: Silent exposure of enterprise data and tool access to AI agents; supply chain risk through MCP adoption.
- **Status**: Emerging risk as organizations adopt AI agents; no specific exploitation reported but high potential.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: monitor
- **Reporting**: [The Hacker News — How MCP Servers Can Expose Enterprise Secrets](https://thehackernews.com/2026/08/how-mcp-servers-can-expose-enterprise.html)

### Threema DDoS Attacks
- **Description**: Multiple large-scale distributed denial-of-service attacks targeting Threema secure messaging service causing severe communication disruptions.
- **Impact**: Service availability disruption for secure communications users.
- **Status**: Active DDoS campaign; service disrupted.
- **Severity**: medium
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [Bleeping Computer — Large-scale DDoS attacks disrupted Threema secure messaging service](https://www.bleepingcomputer.com/news/security/large-scale-ddos-attacks-disrupted-threema-secure-messaging-service/)

## Affected Systems and Products

- **Unisoc Modem Firmware**: Android devices with Unisoc chipsets supporting VoLTE video calling; specific modem firmware versions not disclosed; no patch from chipset maker.
- **GitLab CE/EE**: All versions prior to security release addressing CVE-2026-19478; Community Edition and Enterprise Edition both affected.
- **Forminator Forms WordPress Plugin**: Versions prior to patched release; 600,000+ active installations across WordPress sites.
- **VMware vCenter Server**: Versions affected by CVE-2026-59310; Broadcom has released patches for supported versions.
- **SAP Commerce Cloud**: Cloud deployments using default authentication client configurations; patched versions available.
- **Apple macOS**: Versions with Screen Sharing enabled and exposed to internet or local network; patched in recent security updates.
- **Microsoft Defender**: Windows systems running vulnerable Defender versions; patch in development for CVE-2026-69414.
- **Enterprise Certificate Authorities**: Windows Server AD CS deployments with Enterprise CAs; standard domain users can exploit CVE-2026-54121.
- **Snowflake Connector for .NET**: Public repository snowflakedb/snowflake-connector-net GitHub Actions workflows using vulnerable jira_issue.yml.
- **Linux Edge Devices**: Internet-facing routers, gateways, IoT devices running Linux; exploited via known vulnerabilities (specific CVEs not enumerated in articles).
- **Iranian APT Targets**: Organizations in Israel; Cavern C2 infrastructure leveraging DNS and Google Workspace.
- **macOS Systems**: Users targeted via ClickFix social engineering; AmnesiaStealer malware delivery.
- **Fortune 500 Azure Tenants**: Organizations with compromised credentials enabling Azure infrastructure access.
- **MCP Server Deployments**: Enterprise AI agent implementations using Model Context Protocol; configuration files, permission scopes, and prompt handling.
- **Threema Messaging Service**: Secure messaging platform infrastructure targeted by volumetric DDoS.

## Attack Vectors and Techniques

- **VoLTE Video Call Exploit Delivery**: Attacker initiates video call to target device; answering triggers modem firmware exploit chain achieving kernel RCE without further user interaction.
- **Unauthenticated GraphQL API Abuse**: Crafted GraphQL requests to public GitLab instances bypass authorization checks to modify/delete projects.
- **Malicious PHP Upload via WordPress Plugin**: Unauthenticated file upload endpoint in Forminator accepts PHP files leading to RCE.
- **vCenter Directory Traversal**: Path traversal in vCenter services enables unauthenticated file read/write leading to RCE; used for ransomware deployment.
- **SAP Default Auth Client Abuse**: Unauthenticated requests to default authentication client endpoint bypass authorization via insufficient input validation.
- **Screen Sharing Auth Bypass**: Network-level authentication flaw allows remote access without valid credentials on exposed macOS systems.
- **Defender Evasion (ShieldBreak)**: Zero-day technique bypasses Microsoft Defender protections; details withheld pending patch.
- **Enterprise CA Misuse**: Standard user requests certificate templates enabling Domain Controller equivalence; PKI trust chain abuse.
- **GitHub Actions Workflow Injection**: Crafted GitHub issue titles/bodies inject commands into CI/CD workflow executing with elevated credentials.
- **Known Vulnerability Exploitation (Evooo1Bot)**: Automated scanning and exploitation of unpatched flaws in edge device web interfaces/firmware.
- **DNS Tunneling C2**: Cavern framework uses DNS queries/responses for covert command-and-control communication.
- **Google Apps Script C2**: Malicious Apps Script deployments act as C2 relays blending with legitimate Google Workspace traffic.
- **ClickFix Social Engineering**: Fake browser/error prompts trick users into executing malicious commands (AmnesiaStealer delivery).
- **Credential Stuffing/Reuse**: Compromised credentials used to access Azure infrastructure across multiple Fortune 500 companies.
- **Prompt Injection & Config Exposure**: MCP server misconfigurations allow secret leakage and unauthorized tool access via AI agent interactions.
- **Volumetric DDoS**: High-volume traffic floods targeting messaging service infrastructure.
- **Third-Party Supply Chain Breach**: Compromise of logistics provider (CEVA Logistics) and tax authority contractor to access customer data.
- **Ransomware Data Theft & Extortion**: Clop gang exfiltrates data before encryption; double extortion model.

## Threat Actor Activities

- **SSD Secure Disclosure**: Research group publishing Unisoc exploit chain; responsible disclosure followed by public advisory after vendor non-response.
- **Suspected China-Nexus APT**: Advanced persistent threat group exploiting CVE-2026-59310 in VMware vCenter to deploy Babuk-derived ransomware; attributed by cybersecurity researchers.
- **Iranian Nation-State Actors**: Operators of Cavern/Cav3rn C2 framework targeting Israeli entities since December 2025; continuously evolving infrastructure using DNS and Google Apps Script.
- **Evooo1Bot Operators**: Unknown threat actor(s) deploying and maintaining Mirai-derived botnet with extended capabilities (SOCKS5 proxy, credential theft, exploitation modules); targeting edge devices globally.
- **Clop Ransomware Gang**: Established ransomware-as-a-service operation claiming breaches at GE and Philips; data theft for double extortion.
- **Nightmare Eclipse**: Security researcher who disclosed ShieldBreak zero-day (CVE-2026-69414) in Microsoft Defender.
- **Azure Credential Thief**: Unnamed threat actor selling 3.6 million employee records from Fortune 500 Azure tenants; initial access via compromised credentials.
- **AmnesiaStealer Operators**: Unknown group distributing macOS info-stealer via ClickFix campaigns; interactive browser control capability.
- **Wiz Researchers**: Discovered and disclosed Snowflake GitHub Actions vulnerability; coordinated disclosure.
- **DDoS Actors**: Unattributed groups launching large-scale volumetric attacks against Threema messaging infrastructure.