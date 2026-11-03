---
schema_version: 2
report_date: 2026-09-30
generated_at: 2026-09-30T21:21:16Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-30/
---
# Exploitation Report

## Executive Summary

Russian state actor Star Blizzard has escalated its phishing operations against Ukrainian-linked organizations by adopting a novel malware installation technique dubbed "RedFlick" to deploy the CosmicPulse backdoor. This shift from the previously observed ClickFix methodology demonstrates the group's continued adaptation to defensive measures while maintaining focus on NGOs, think tanks, and journalists. Simultaneously, multiple critical infrastructure vulnerabilities have come under active exploitation, including a pre-authentication command injection in Zimbra Collaboration Suite, an authentication bypass in Cisco Catalyst SD-WAN Manager, and a high-severity memory overflow in Citrix NetScaler ADC and Gateway appliances.

Active exploitation of the Citrix NetScaler vulnerability (CVE-2026-88772) has enabled threat actors to achieve root access, deploy custom web shells and tunneling malware, harvest credentials, and move laterally into internal networks across government, financial services, technology, education, and legal sectors in North America and Europe. The Cisco SD-WAN Manager zero-day (CVE-2026-76504) is being exploited to escalate to administrative privileges without authentication, with fixed releases now available but no workaround provided. Apple has also confirmed targeted exploitation of an out-of-bounds write flaw (CVE-2026-86950) in what it describes as an extremely sophisticated manner.

Beyond traditional vulnerability exploitation, attackers are increasingly abusing trusted AI platforms and legitimate remote management tools. Custom ChatGPT GPTs promoted through sponsored search results are being weaponized to deliver ClickFix lures that deploy remote access trojans, while phishing campaigns leveraging MSP360 and ScreenConnect installers are establishing persistent remote access. The Dutch Institute for Vulnerability Disclosure suffered a network breach through a chain of two zero-days in the Zammad ticketing system, and cryptocurrency exchange Bitget lost $387.5 million via a zero-day in unspecified third-party security products. Mass credential exposure on GitHub—over 543,000 valid secrets—continues to fuel initial access operations.

## Active Exploitation Details

### Zimbra Collaboration Suite Unauthenticated Command Injection
- **Description**: An unauthenticated operating system command injection flaw in Zimbra Collaboration Suite (ZCS) that allows remote code execution when Simple Network Management Protocol (SNMP) is enabled. The vulnerability resides in the SNMP component and can be triggered without authentication.
- **Impact**: Attackers can deploy web shells, access mailbox data, harvest authentication secrets, and achieve full compromise of the email server.
- **Status**: The vulnerability has been patched, but active exploitation has been observed in the wild by Microsoft Security Research team.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-73570
- **Reporting**: [The Hacker News — Attackers Exploit Zimbra Flaw to Deploy Web Shells and Harvest Authentication Secrets](https://thehackernews.com/2026/09/attackers-exploit-zimbra-flaw-to-deploy.html)

### Cisco Catalyst SD-WAN Manager Authentication Bypass
- **Description**: A critical zero-day authentication bypass vulnerability in Cisco Catalyst SD-WAN Manager that allows a remote, unauthenticated attacker to access the Manager's API with administrative privileges. The flaw enables privilege escalation to admin level without any prior credentials.
- **Impact**: Full administrative control over the SD-WAN management platform, enabling network-wide configuration changes, traffic manipulation, and potential lateral movement across managed devices.
- **Status**: Actively exploited in the wild. Cisco released fixed versions on September 30, 2026. No workaround is available.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-76504
- **Reporting**: [The Hacker News — Cisco Warns of Attackers Exploiting Critical Authentication Bypass in SD-WAN Manager](https://thehackernews.com/2026/09/cisco-warns-of-attackers-exploiting.html), [Bleeping Computer — Cisco warns of new SD-WAN zero-day exploited in attacks](https://www.bleepingcomputer.com/news/security/cisco-warns-of-new-sd-wan-authentication-bypass-zero-day-exploited-in-attacks/)

### Citrix NetScaler ADC and Gateway DTLS Memory Overflow
- **Description**: A critical memory overflow vulnerability in the Datagram Transport Layer Security (DTLS) protocol handling of Citrix NetScaler ADC and NetScaler Gateway appliances. The flaw allows pre-authentication shellcode execution through a carefully crafted DTLS handshake.
- **Impact**: Attackers achieve root access on the appliance, deploy custom web shells and tunneling malware (WHIPSHOT and SLAPSHOT), steal credentials, and pivot into internal networks. Targeted sectors include government, financial services, technology, education, and legal/professional services in North America and Europe.
- **Status**: Actively exploited as a zero-day before patching. Exploit details have been publicly disclosed. Mandiant Consulting and Google Threat Intelligence Group observed exploitation in September 2026.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-88772
- **Reporting**: [The Hacker News — Attackers Exploit NetScaler Flaw for Root Access, Deploy WHIPSHOT and SLAPSHOT](https://thehackernews.com/2026/09/attackers-exploit-netscaler-flaw-for.html), [The Hacker News — Citrix NetScaler CVE-2026-88772 Exploit Details Show Pre-Auth Path to Shellcode Execution](https://thehackernews.com/2026/09/citrix-netscaler-cve-2026-88772-exploit.html), [Bleeping Computer — Hackers exploit Citrix NetScaler zero-day to deploy web shells](https://www.bleepingcomputer.com/news/security/hackers-exploit-citrix-netscaler-zero-day-to-deploy-web-shells/)

### Apple Out-of-Bounds Write Zero-Day
- **Description**: An out-of-bounds write vulnerability in Apple products that is being weaponized in highly targeted attacks. Apple characterizes the exploitation as extremely sophisticated.
- **Impact**: Targeted compromise of Apple devices, likely enabling arbitrary code execution with elevated privileges.
- **Status**: Actively exploited in targeted attacks. Patch status not specified in available reporting.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **CVE IDs**: CVE-2026-86950
- **Reporting**: [Dark Reading — Apple Zero-Day Vulnerability Weaponized in Targeted Attacks](https://www.darkreading.com/cyberattacks-data-breaches/apple-zero-day-vulnerability-weaponized-targeted-attacks)

### Zammad Ticketing System Zero-Day Chain
- **Description**: A chain of two zero-day vulnerabilities in the open-source Zammad ticketing system that were exploited to breach the Dutch Institute for Vulnerability Disclosure (DIVD) network. The exploitation was described as AI-driven.
- **Impact**: Full network breach of a vulnerability disclosure organization, potentially exposing vulnerability intelligence and coordination data.
- **Status**: Zero-days exploited in the wild against a high-value target. Patch status not specified in available reporting.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — DIVD says Zammad zero-days enabled AI-driven network breach](https://www.bleepingcomputer.com/news/security/divd-says-zammad-zero-days-enabled-ai-driven-network-breach/)

### MikroTik RouterOS Pre-Auth RCE
- **Description**: A critical pre-authentication remote code execution vulnerability in MikroTik RouterOS that can also cause denial-of-service conditions. CISA has issued a warning about this flaw.
- **Impact**: Remote code execution on routing infrastructure without authentication, enabling network interception, traffic manipulation, and infrastructure compromise.
- **Status**: CISA warning issued indicating active exploitation risk. Patch availability not specified in available reporting.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: patch
- **Reporting**: [Bleeping Computer — CISA warns of critical pre-auth RCE flaw in MikroTik RouterOS](https://www.bleepingcomputer.com/news/security/cisa-warns-of-critical-pre-auth-rce-flaw-in-mikrotik-routeros/)

### TeamViewer Client and Host Vulnerabilities
- **Description**: A set of high-severity vulnerabilities affecting TeamViewer client and host software. TeamViewer has urged customers to patch "as soon as possible."
- **Impact**: Potential remote code execution or privilege escalation through the remote access software, which could lead to full system compromise.
- **Status**: Vendors urging immediate patching. Active exploitation status not explicitly confirmed in available reporting.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [Bleeping Computer — TeamViewer urges users to patch severe flaws “as soon as possible”](https://www.bleepingcomputer.com/news/security/teamviewer-urges-users-to-patch-severe-flaws-as-soon-as-possible/)

### OpenSSL DTLS Heap Memory Leak
- **Description**: A high-severity flaw in OpenSSL's DTLS implementation that can leak heap memory to the peer or crash the program. The issue occurs when a handshake message retransmission starts while a larger handshake message is partially processed.
- **Impact**: Memory disclosure potentially exposing cryptographic material or sensitive data, and denial-of-service via application crash.
- **Status**: Fixed in OpenSSL releases dated September 29, 2026. No active exploitation reported.
- **Severity**: high
- **Exploitation Status**: not_observed
- **Action**: patch
- **Reporting**: [The Hacker News — OpenSSL Fixes High-Severity DTLS Flaw That Can Leak Heap Memory Unencrypted](https://thehackernews.com/2026/09/openssl-fixes-high-severity-dtls-flaw.html)

### Unsloth Studio Code Execution via Model Inspection
- **Description**: A vulnerability in Unsloth Studio that allows malicious AI models to execute arbitrary Python code during routine model inspection through the trust_remote_code setting.
- **Impact**: Arbitrary code execution on systems inspecting untrusted AI models, enabling supply chain compromise through machine learning model sharing.
- **Status**: Patched. Exploitation status in the wild not reported.
- **Severity**: high
- **Exploitation Status**: not_observed
- **Action**: patch
- **Reporting**: [Dark Reading — Unsloth Studio Flaw Turns Routine Model Inspection Into Code Execution](https://www.darkreading.com/application-security/unsloth-studio-flaw-model-inspection-code-execution)

### Bitget Third-Party Security Product Zero-Day
- **Description**: A zero-day vulnerability in unspecified third-party security products that was exploited to breach cryptocurrency exchange Bitget, resulting in $387.5 million theft.
- **Impact**: Full compromise of exchange infrastructure leading to massive cryptocurrency theft.
- **Status**: Zero-day exploited in the wild. Vendor and product not publicly identified in available reporting.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Bitget hacked via zero-day in third-party security products](https://www.bleepingcomputer.com/news/security/bitget-hacked-via-zero-day-in-third-party-security-products/)

## Affected Systems and Products

- **Zimbra Collaboration Suite**: Versions with SNMP enabled prior to the patched release addressing CVE-2026-73570
- **Platform**: Email and collaboration servers exposed to internet or internal networks with SNMP accessible
- **Cisco Catalyst SD-WAN Manager**: All versions prior to the fixed releases issued September 30, 2026
- **Platform**: Enterprise SD-WAN management appliances and virtual appliances
- **Citrix NetScaler ADC and NetScaler Gateway**: Appliances running vulnerable firmware versions prior to the patched releases addressing CVE-2026-88772
- **Platform**: Application delivery controllers and VPN gateways in enterprise and service provider environments
- **Apple Products**: Devices running vulnerable operating system versions (specific versions not disclosed in reporting)
- **Platform**: iOS, macOS, and potentially other Apple operating systems
- **Zammad Ticketing System**: Open-source helpdesk/ticketing system installations (specific versions not disclosed)
- **Platform**: Linux/Unix servers, Docker containers, and cloud deployments running Zammad
- **MikroTik RouterOS**: RouterOS versions affected by the pre-auth RCE flaw (specific versions not disclosed in CISA warning)
- **Platform**: MikroTik router and wireless hardware running RouterOS
- **TeamViewer Client and Host**: All versions prior to the patched releases for high-severity flaws
- **Platform**: Windows, macOS, Linux, mobile platforms running TeamViewer remote access software
- **OpenSSL**: Versions with the vulnerable DTLS implementation prior to September 29, 2026 releases
- **Platform**: All platforms using OpenSSL for DTLS/UDP TLS connections (Linux, Windows, embedded systems, appliances)
- **Unsloth Studio**: Versions prior to the patched release addressing the trust_remote_code code execution flaw
- **Platform**: Python-based AI/ML development environments using Unsloth for model training and inspection
- **Third-Party Security Products (Bitget breach)**: Unspecified security products used by cryptocurrency exchange Bitget
- **Platform**: Enterprise security infrastructure (exact products not disclosed)

## Attack Vectors and Techniques

- **RedFlick Malware Installation Technique**: A novel tactic used by Star Blizzard (Russian APT) to deploy the CosmicPulse backdoor. Replaces the group's previous ClickFix methodology. Delivered through phishing targeting Ukrainian-linked NGOs, think tanks, and journalists.
- **Vector**: Phishing emails with malicious links/attachments leading to RedFlick execution chain
- **ClickFix Social Engineering Lures**: Attackers use deceptive UI prompts (fake CAPTCHAs, verification dialogs, error messages) to trick users into executing malicious PowerShell commands or scripts. Now being delivered through Custom ChatGPT GPTs promoted via sponsored Google search results.
- **Vector**: Web-based social engineering via compromised/trusted AI platforms and search results
- **Dual-RMM Phishing with MSP360 and ScreenConnect**: Phishing campaigns distribute legitimate MSP360 RMM installers disguised as meeting invitations, PDF lures, or software updates. Once executed, the attacker gains persistent remote management access and deploys ScreenConnect for additional control.
- **Vector**: Email phishing with legitimate RMM software installers renamed to deceptive filenames
- **Web Shell Deployment via Command Injection**: Exploitation of CVE-2026-73570 in Zimbra and CVE-2026-88772 in NetScaler to deploy persistent web shells for long-term access, credential harvesting, and lateral movement.
- **Vector**: Unauthenticated HTTP/HTTPS requests to vulnerable management interfaces (SNMP for Zimbra, DTLS for NetScaler)
- **DTLS Protocol Exploitation**: Memory corruption in DTLS handshake processing (NetScaler CVE-2026-88772, OpenSSL flaw) enabling pre-auth code execution or memory disclosure.
- **Vector**: Crafted UDP DTLS packets sent to exposed DTLS services on port 443 or custom ports
- **Authentication Bypass via API Abuse**: CVE-2026-76504 in Cisco SD-WAN Manager allows unauthenticated API calls with administrative privileges.
- **Vector**: Direct API requests to the SD-WAN Manager's REST interface without authentication tokens
- **AI Platform Abuse for Malware Delivery**: Custom ChatGPT GPTs and AI coding agents are being weaponized—GPTs to host ClickFix lures, coding agents to exfiltrate internal screenshots and credentials to public GitHub repositories.
- **Vector**: Sponsored search results for malicious GPTs; misconfigured AI agent permissions in development workflows
- **Credential Harvesting from Public Repositories**: Over 543,000 valid credentials (API keys, tokens, passwords) found in public GitHub repositories in July 2026, despite GitHub's secret scanning.
- **Vector**: Automated scanning of public repositories; credentials exposed by developers and AI coding agents
- **Zero-Day Chaining for Network Breach**: Two zero-days in Zammad chained together for initial access and privilege escalation/ lateral movement in the DIVD breach, described as AI-driven.
- **Vector**: Web application attack chain against internet-facing ticketing system

## Threat Actor Activities

- **Star Blizzard (Russian State Actor)**: Conducting phishing campaigns against Ukrainian-linked targets (NGOs, think tanks, journalists) using the new RedFlick technique to deploy CosmicPulse backdoor. Previously used ClickFix; has adapted tactics to evade detection. Active since at least late September 2026.
- **Campaign**: RedFlick phishing campaign targeting Ukrainian civil society organizations
- **Unknown Threat Actors (NetScaler Exploitation)**: Observed by Mandiant Consulting and Google Threat Intelligence Group exploiting CVE-2026-88772 in September 2026. Deploying WHIPSHOT and SLAPSHOT malware, achieving root access, stealing credentials, and moving laterally. Targeting government, financial services, technology, education, and legal/professional services in North America and Europe.
- **Campaign**: NetScaler zero-day exploitation campaign (September 2026)
- **CSuite Phishing Operators**: Running US-focused phishing campaign across 351 sandbox analyses (51% US submissions). Combines Microsoft 365 session theft with RMM tool (MSP360/ScreenConnect) deployment for persistent remote access. Highest exposure in technology, manufacturing, government, and consulting sectors.
- **Campaign**: CSuite phishing campaign (2026)
- **Custom ChatGPT Abuse Operators**: Creating malicious Custom GPTs promoted via sponsored Google results to deliver ClickFix lures that deploy remote access trojans. Observed by Huntress in late September 2026.
- **Campaign**: Malicious GPT distribution via search engine advertising
- **ShinyHunters Extortion Group**: Dutch police arrested an alleged leader; FBI warning members to surrender. Group known for data theft and extortion campaigns against numerous organizations.
- **Campaign**: Historical data theft and extortion operations (law enforcement action reported September 2026)
- **Bitget Attackers**: Exploited a zero-day in third-party security products to breach the cryptocurrency exchange and steal $387.5 million. Attribution not specified in available reporting.
- **Campaign**: Bitget exchange breach (September 2026)
- **DIVD Breach Actors**: Exploited a chain of two zero-days in Zammad ticketing system to compromise the Dutch Institute for Vulnerability Disclosure network. Described as an AI-driven breach.
- **Campaign**: DIVD network intrusion (date not specified in reporting)