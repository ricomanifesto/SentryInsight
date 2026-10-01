---
schema_version: 2
report_date: 2026-10-01
generated_at: 2026-10-01T09:26:57Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-10-01/
---
# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse technology stacks, with threat actors leveraging both zero-day flaws and recently patched vulnerabilities to achieve remote code execution, privilege escalation, and persistent access. Citrix NetScaler appliances face two distinct actively exploited vulnerabilities—CVE-2026-88772 (CVSS 9.5) and a pre-authentication command injection flaw—enabling attackers to deploy web shells, create superuser accounts, and execute shellcode without authentication. Simultaneously, a critical zero-day in Cisco Catalyst SD-WAN Manager (CVE-2026-76504) allows unauthenticated attackers to assume administrative API privileges, while CISA has warned of a critical pre-authentication RCE in MikroTik RouterOS. These network infrastructure flaws are being weaponized at scale against government, financial, technology, and legal sectors in North America and Europe.

Threat actor activity shows sophisticated evolution in initial access techniques. Russian state actor Star Blizzard has abandoned ClickFix in favor of a novel "RedFlick" technique to deploy its CosmicPulse backdoor against Ukrainian-linked NGOs, think tanks, and journalists. Separate campaigns abuse legitimate AI platforms: ChatGPT Custom GPTs are being weaponized as ClickFix lures to deliver remote access trojans, while a US-focused CSuite phishing operation combines Microsoft 365 session theft with RMM tool deployment across technology, manufacturing, government, and consulting organizations. The Bitget cryptocurrency exchange lost $387.5 million through a zero-day in third-party security products, and the Dutch Institute for Vulnerability Disclosure suffered an AI-driven network breach via a chain of two zero-days in the Zammad ticketing system.

Proof-of-concept code has emerged for CVE-2026-86950, an Apple CoreGraphics memory corruption flaw triggered by malicious PDFs with crafted embedded fonts that may have been used in targeted attacks against specific individuals. Zimbra Collaboration Suite's patched CVE-2026-73570 (CVSS 8.9) continues to be exploited for web shell deployment and mailbox data harvesting. TeamViewer has urged immediate patching of high-severity client and host vulnerabilities, while OpenSSL addressed a high-severity DTLS heap memory leak. Over 543,000 valid credentials remain exposed in public GitHub repositories, and MetaMask disclosed an ongoing infrastructure security incident prompting Ethereum validator exits.

## Active Exploitation Details

### Citrix NetScaler ADC and Gateway Memory Overflow (CVE-2026-88772)
- **Description**: A critical memory overflow vulnerability in the Datagram Transport Layer Security (DTLS) protocol handling of Citrix NetScaler ADC and Gateway appliances. The flaw resides in the NetScaler packet processing engine and allows pre-authentication shellcode execution.
- **Impact**: Attackers can achieve unauthenticated remote code execution with root privileges, enabling full appliance compromise, configuration data theft, and lateral movement into internal networks.
- **Status**: Actively exploited in the wild; patches available from Citrix.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-88772
- **Reporting**: [The Hacker News — Citrix NetScaler CVE-2026-88772 Exploit Details Show Pre-Auth Path to Shellcode Execution](https://thehackernews.com/2026/09/citrix-netscaler-cve-2026-88772-exploit.html), [The Hacker News — Attackers Exploit NetScaler Flaw for Root Access, Deploy WHIPSHOT and SLAPSHOT](https://thehackernews.com/2026/09/attackers-exploit-netscaler-flaw-for.html)

### Citrix NetScaler Pre-Authentication Command Injection
- **Description**: A critical pre-authentication command injection vulnerability in Citrix NetScaler ADC and NetScaler Gateway that allows attackers to drop web shells and steal configuration data without authentication.
- **Impact**: Attackers gain persistent access via web shells mapped to CSS-like URLs, create superuser accounts, and exfiltrate sensitive configuration data including certificates and keys.
- **Status**: Actively exploited across multiple customer environments; patches available.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-88772
- **Reporting**: [The Hacker News — Citrix NetScaler Post-Exploitation Payload Creates Superuser, Maps Web Shell to CSS-Like URLs](https://thehackernews.com/2026/10/citrix-netscaler-post-exploitation.html), [The Hacker News — Attackers Exploit NetScaler Flaw for Root Access, Deploy WHIPSHOT and SLAPSHOT](https://thehackernews.com/2026/09/attackers-exploit-netscaler-flaw-for.html)

### Cisco Catalyst SD-WAN Manager Authentication Bypass (CVE-2026-76504)
- **Description**: A critical zero-day authentication bypass vulnerability in Cisco Catalyst SD-WAN Manager that allows a remote, unauthenticated attacker to access the Manager's API with administrative privileges.
- **Impact**: Full administrative control over SD-WAN infrastructure, enabling network traffic manipulation, policy modification, and potential lateral movement across managed network devices.
- **Status**: Actively exploited in attacks; fixed releases available with no workaround.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-76504
- **Reporting**: [The Hacker News — Cisco Warns of Attackers Exploiting Critical Authentication Bypass in SD-WAN Manager](https://thehackernews.com/2026/09/cisco-warns-of-attackers-exploiting.html), [Bleeping Computer — Cisco warns of new SD-WAN zero-day exploited in attacks](https://www.bleepingcomputer.com/news/security/cisco-warns-of-new-sd-wan-authentication-bypass-zero-day-exploited-in-attacks/)

### Zimbra Collaboration Suite Command Injection (CVE-2026-73570)
- **Description**: An unauthenticated operating system command injection flaw in Zimbra Collaboration Suite (ZCS) that enables remote code execution when Simple Network Management Protocol (SNMP) is enabled.
- **Impact**: Attackers deploy web shells to maintain persistent access and harvest authentication secrets and mailbox data from compromised email servers.
- **Status**: Actively exploited in the wild; vulnerability is now patched.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-73570
- **Reporting**: [The Hacker News — Attackers Exploit Zimbra Flaw to Deploy Web Shells and Harvest Authentication Secrets](https://thehackernews.com/2026/09/attackers-exploit-zimbra-flaw-to-deploy.html)

### Apple CoreGraphics PDF Font Parsing Flaw (CVE-2026-86950)
- **Description**: A memory corruption vulnerability in Apple CoreGraphics triggered by a malicious PDF containing a crafted embedded font. Public proof-of-concept code has been published.
- **Impact**: Causes crashes on unpatched iPhones and Macs; Apple states the flaw may have been used in attacks against specific targeted individuals. Memory corruption could potentially be developed into arbitrary code execution.
- **Status**: PoC publicly available; Apple acknowledges possible targeted exploitation; patches expected.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: patch
- **CVE IDs**: CVE-2026-86950
- **Reporting**: [The Hacker News — Apple CoreGraphics PoC Emerges as WhatsApp PDF Checks Hint at Possible Delivery Path](https://thehackernews.com/2026/10/apple-coregraphics-poc-emerges-as.html)

### MikroTik RouterOS Pre-Authentication RCE
- **Description**: A critical pre-authentication remote code execution vulnerability in MikroTik RouterOS that can also lead to denial-of-service conditions.
- **Impact**: Unauthenticated attackers can achieve remote code execution on affected routers, potentially compromising entire network infrastructure and enabling traffic interception or redirection.
- **Status**: CISA has issued an active warning; exploitation likely imminent or occurring.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [Bleeping Computer — CISA warns of critical pre-auth RCE flaw in MikroTik RouterOS](https://www.bleepingcomputer.com/news/security/cisa-warns-of-critical-pre-auth-rce-flaw-in-mikrotik-routeros/)

### TeamViewer Client and Host Vulnerabilities
- **Description**: A set of high-severity vulnerabilities affecting TeamViewer client and host software that could allow remote code execution or privilege escalation.
- **Impact**: Attackers could compromise remote access sessions, take control of endpoints, and pivot within organizational networks.
- **Status**: TeamViewer urges immediate patching; active exploitation not confirmed but risk is high.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [Bleeping Computer — TeamViewer urges users to patch severe flaws “as soon as possible”](https://www.bleepingcomputer.com/news/security/teamviewer-urges-users-to-patch-severe-flaws-as-soon-as-possible/)

### Zammad Ticketing System Zero-Day Chain
- **Description**: A chain of two zero-day vulnerabilities in the open-source Zammad ticketing system that enabled an AI-driven network breach of the Dutch Institute for Vulnerability Disclosure (DIVD).
- **Impact**: Full network compromise through chained exploitation; attackers leveraged AI-driven techniques to automate and accelerate the breach.
- **Status**: Zero-days exploited in targeted breach; patch status unclear from reporting.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — DIVD says Zammad zero-days enabled AI-driven network breach](https://www.bleepingcomputer.com/news/security/divd-says-zammad-zero-days-enabled-ai-driven-network-breach/)

### Third-Party Security Product Zero-Day (Bitget Breach)
- **Description**: A zero-day vulnerability in third-party security products exploited to breach cryptocurrency exchange Bitget, resulting in $387.5 million theft. SlowMist investigation recovered a customized attacker tool.
- **Impact**: Complete compromise of exchange infrastructure enabling massive cryptocurrency theft; highlights supply chain risk in security tooling.
- **Status**: Actively exploited in high-value targeted attack; investigation ongoing.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Bitget Confirms Third-Party Zero-Day Behind $387.5 Million Cryptocurrency Theft](https://thehackernews.com/2026/10/bitget-confirms-third-party-zero-day.html), [Bleeping Computer — Bitget hacked via zero-day in third-party security products](https://www.bleepingcomputer.com/news/security/bitget-hacked-via-zero-day-in-third-party-security-products/)

### MetaMask Infrastructure Security Incident
- **Description**: An ongoing security incident affecting MetaMask infrastructure, prompting the exit of affected Ethereum validators. No immediate threat to user wallets identified.
- **Impact**: Infrastructure compromise affecting validator operations; potential for broader ecosystem impact if validator keys or signing infrastructure were accessed.
- **Status**: Active incident response underway; coordination with external partners and security advisors.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Metamask discloses security incident affecting its infrastructure](https://www.bleepingcomputer.com/news/security/metamask-discloses-security-incident-affecting-its-infrastructure/), [The Hacker News — MetaMask Security Incident Prompts Exit of Affected Ethereum Validators](https://thehackernews.com/2026/10/metamask-security-incident-prompts-exit.html)

### OpenSSL DTLS Heap Memory Leak
- **Description**: A high-severity flaw in OpenSSL's DTLS implementation that can leak heap memory to the peer or crash the program when a handshake retransmission occurs while a larger message is stuck mid-processing.
- **Impact**: Information disclosure of potentially sensitive heap data including cryptographic material; denial of service via application crash.
- **Status**: Fixes released on September 29; active exploitation not reported.
- **Severity**: high
- **Exploitation Status**: not_observed
- **Action**: patch
- **Reporting**: [The Hacker News — OpenSSL Fixes High-Severity DTLS Flaw That Can Leak Heap Memory Unencrypted](https://thehackernews.com/2026/09/openssl-fixes-high-severity-dtls-flaw.html)

## Affected Systems and Products

- **Citrix NetScaler ADC and NetScaler Gateway**: All versions prior to patched releases for CVE-2026-88772 and the pre-auth command injection flaw; appliances exposed to internet-facing DTLS/SSL VPN services.
- **Platform**: Network infrastructure appliances in government, financial services, technology, education, legal, and professional services sectors across North America and Europe.
- **Cisco Catalyst SD-WAN Manager**: Versions prior to fixed releases for CVE-2026-76504; management planes accessible via API endpoints.
- **Platform**: Enterprise SD-WAN deployments managing Cisco network infrastructure.
- **Zimbra Collaboration Suite (ZCS)**: Versions with SNMP enabled prior to patch for CVE-2026-73570.
- **Platform**: On-premises email and collaboration servers in enterprise environments.
- **Apple iOS, iPadOS, macOS**: Unpatched devices vulnerable to CVE-2026-86950 via malicious PDF rendering.
- **Platform**: iPhone, iPad, and Mac endpoints; targeted individuals at elevated risk.
- **MikroTik RouterOS**: Vulnerable versions exposed to internet-facing management interfaces.
- **Platform**: SOHO and enterprise routers, wireless access points, and network infrastructure devices globally.
- **TeamViewer Client and Host**: All versions prior to security updates for high-severity flaws.
- **Platform**: Windows, macOS, Linux endpoints running TeamViewer remote access software.
- **Zammad Ticketing System**: Open-source helpdesk/ticketing installations; specific versions affected by zero-day chain not publicly disclosed.
- **Platform**: Linux-based web application deployments, Docker containers, and package installations.
- **Third-Party Security Products (Bitget Incident)**: Specific products not named; security tooling integrated into cryptocurrency exchange infrastructure.
- **Platform**: Cryptocurrency exchange backend systems and security monitoring infrastructure.
- **MetaMask Infrastructure**: Backend services and API infrastructure; user-facing wallet applications not directly affected.
- **Platform**: Ethereum validator infrastructure and MetaMask service APIs.
- **OpenSSL**: Versions prior to 3.0.16, 3.1.8, 3.2.4, 3.3.2, and 3.4.0 (as per OpenSSL advisory).
- **Platform**: Any application or service using OpenSSL for DTLS/UDP-TLS communications.

## Attack Vectors and Techniques

- **Malicious PDF with Crafted Embedded Font**: Delivery of CVE-2026-86950 exploit via PDF documents containing specially crafted fonts that trigger memory corruption in Apple CoreGraphics during rendering.
- **Vector**: Targeted delivery likely via email, messaging, or web download; WhatsApp PDF processing identified as potential delivery path.
- **Pre-Authentication DTLS Memory Overflow**: Exploitation of CVE-2026-88772 through malformed DTLS packets sent to NetScaler ADC/Gateway UDP ports without authentication.
- **Vector**: Direct network access to internet-facing NetScaler appliances on DTLS ports (typically UDP 443).
- **Pre-Authentication Command Injection**: Unauthenticated HTTP requests with crafted parameters injected into NetScaler management interfaces to execute arbitrary OS commands.
- **Vector**: Web-based management interfaces accessible from internet; leads to web shell deployment at CSS-like URL paths.
- **Authentication Bypass via API**: Unauthenticated API calls to Cisco Catalyst SD-WAN Manager that are processed with administrative privileges due to CVE-2026-76504.
- **Vector**: REST API endpoints on SD-WAN Manager; no valid credentials required.
- **Unauthenticated SNMP Command Injection**: Exploitation of CVE-2026-73570 via SNMP requests that inject OS commands into Zimbra Collaboration Suite.
- **Vector**: SNMP (UDP 161) exposed to attacker-controlled networks; leads to web shell deployment and mailbox access.
- **ClickFix Social Engineering via AI Platforms**: Abuse of ChatGPT Custom GPTs and legitimate OpenAI/Google domains to present convincing lures that trick users into executing malicious commands.
- **Vector**: Links shared via phishing, social media, or search results leading to Custom GPT pages that redirect to ClickFix pages prompting "verification" actions.
- **RedFlick Malware Installation Technique**: Novel tactic used by Star Blizzard involving staged payload delivery that evades traditional detection, deploying the CosmicPulse backdoor.
- **Vector**: Phishing emails with crafted lures targeting Ukrainian-linked NGOs, think tanks, and journalists; multi-stage execution chain.
- **Dual-RMM Phishing with MSP360 and ScreenConnect**: Phishing campaigns distributing legitimate MSP360 RMM installers disguised as meeting invitations or updates, followed by ScreenConnect deployment for persistent remote access.
- **Vector**: Email phishing with social engineering lures (meeting invites, PDF themes, software updates); legitimate RMM software abused for malicious access.
- **CSuite Microsoft 365 Session Theft + RMM Deployment**: Combined attack stealing Microsoft 365 session tokens via phishing, then deploying RMM tools for persistent remote access and lateral movement.
- **Vector**: Phishing pages harvesting M365 credentials and session cookies; follow-up deployment of remote monitoring and management agents.
- **AI-Driven Zero-Day Exploitation Chain**: Automated discovery and chaining of two zero-days in Zammad ticketing system to breach DIVD network infrastructure.
- **Vector**: Internet-accessible Zammad instance; AI tooling used to accelerate vulnerability discovery and exploitation.
- **Supply Chain Zero-Day in Security Products**: Exploitation of unknown vulnerability in third-party security tooling to gain initial access to Bitget exchange infrastructure.
- **Vector**: Compromised security product with privileged access to exchange systems; customized attacker tooling recovered.

## Threat Actor Activities

- **Star Blizzard (Russian State Actor)**: Deploying CosmicPulse backdoor via new RedFlick technique against Ukrainian-linked targets including NGOs, think tanks, and journalists. Previously used ClickFix; has shifted to RedFlick to widen phishing effectiveness and evade detection.
- **Campaign**: Ongoing espionage operation targeting organizations supporting or associated with Ukraine; CosmicPulse provides persistent remote access and data exfiltration.
- **Unknown Actors (Citrix NetScaler Exploitation)**: Exploiting CVE-2026-88772 and pre-auth command injection across North American and European organizations in government, financial services, technology, education, and legal sectors. Deploying WHIPSHOT and SLAPSHOT payloads, creating superuser accounts, mapping web shells to CSS-like URLs.
- **Campaign**: Broad targeting observed by Mandiant Consulting and Google Threat Intelligence Group (GTIG) in September 2026; post-exploitation focuses on configuration data theft and persistent access.
- **Unknown Actors (Zimbra Exploitation)**: Weaponizing CVE-2026-73570 to deploy web shells and harvest authentication secrets and mailbox data from Zimbra Collaboration Suite servers.
- **Campaign**: Observed by Microsoft Security Research team; exploitation continues post-patch against unpatched instances.
- **CSuite Phishing Operators**: Conducting US-focused phishing campaign (51% of 351 sandbox submissions from US) targeting technology, manufacturing, government, and consulting sectors. Stealing Microsoft 365 session tokens and deploying RMM tools for remote access.
- **Campaign**: ANY.RUN-tracked operation combining credential/session theft with persistent remote access tooling; enables business email compromise, fraud, and lateral movement.
- **ChatGPT Custom GPT Abusers**: Weaponizing OpenAI's Custom GPT feature to create legitimate-appearing lures that redirect victims to ClickFix pages delivering remote access trojans.
- **Campaign**: Observed by Huntress in late September 2026; marks continued abuse of trusted AI platforms for initial access; prior campaigns weaponized shared documents and other AI features.
- **Bitget Attackers**: Exploited zero-day in third-party security products to steal $387.5 million from cryptocurrency exchange; used customized tooling recovered by SlowMist investigators.
- **Campaign**: High-value targeted attack on cryptocurrency infrastructure; supply chain compromise via security tooling; significant financial impact.
- **DIVD Breach Actors**: Leveraged AI-driven exploitation of two Zammad zero-days to breach Dutch Institute for Vulnerability Disclosure network.
- **Campaign**: Demonstrates AI-augmented offensive capabilities accelerating vulnerability discovery and exploitation chaining; targeted vulnerability disclosure organization.
- **MSP360/ScreenConnect Phishing Actors**: Distributing legitimate RMM software installers under deceptive filenames to establish remote management access, then deploying ScreenConnect for persistent control.
- **Campaign**: Microsoft-warned phishing operation using meeting invitations, PDF-themed lures, and software update prompts; dual-RMM technique for redundancy and stealth.