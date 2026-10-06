---
schema_version: 2
report_date: 2026-10-06
generated_at: 2026-10-06T00:51:11Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-10-06/
---
# Exploitation Report

## Executive Summary

Active exploitation campaigns are targeting critical infrastructure and enterprise systems across multiple vectors. A NetScaler zero-day (CVE-2026-88779) has been exploited in targeted attacks against SAML deployments, while Rejetto HFS servers face active scanning and exploitation attempts for a critical session forgery flaw (CVE-2026-61500) that enables remote code execution. Microsoft Exchange Server privilege escalation (CVE-2026-96940) has prompted out-of-band patches. Meanwhile, threat actors are weaponizing both old and new SharePoint vulnerabilities for ransomware deployment, and a Realtek Jungle SDK flaw is being exploited to deliver the Cling botnet with novel STUN-based command-and-control infrastructure.

China-aligned threat group TA419 is conducting sophisticated adversary-in-the-middle phishing campaigns against U.S. AI policy experts, impersonating prominent officials and Anthropic employees. The suspected China-linked actor Warlock continues exploiting SharePoint flaws against critical infrastructure, government, and education sectors in Portuguese- and Spanish-speaking countries. The ShinyHunters extortion group faces disruption with the reported detention of a key member in Jordan who is cooperating with the FBI. Additionally, IoT devices are being compromised at scale through 24 known vulnerabilities to form proxy networks via the ClingSTUN operation.

## Active Exploitation Details

### NetScaler ADC/Gateway Zero-Day (CVE-2026-88779)
- **Description**: A memory overflow vulnerability in Citrix NetScaler ADC and NetScaler Gateway that can lead to denial-of-service conditions. Researchers are investigating whether it can also be exploited for remote code execution. The flaw specifically impacts SAML deployments.
- **Impact**: Attackers can knock SAML deployments offline, disrupting authentication services. Potential for remote code execution remains under investigation.
- **Status**: Emergency security updates released by Citrix. Actively exploited in targeted zero-day attacks.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-88779
- **Reporting**: [The Hacker News — New NetScaler Zero-Day Exploited in Targeted Attacks Can Knock SAML Deployments Offline](https://thehackernews.com/2026/10/new-netscaler-zero-day-exploited-in.html), [Bleeping Computer — Citrix patches NetScaler SAML zero-day exploited in attacks](https://www.bleepingcomputer.com/news/security/citrix-patches-netscaler-saml-zero-day-exploited-in-attacks/)

### Rejetto HFS Weak Signing Key / Session Forgery (CVE-2026-61500)
- **Description**: A critical vulnerability in Rejetto HTTP File Server (HFS) stemming from a weak pseudo-random number generator (PRNG) that produces predictable signing keys. This enables session forgery, administrative account takeover, and remote code execution.
- **Impact**: Attackers can forge admin sessions, take over accounts, and achieve remote code execution on vulnerable HFS servers.
- **Status**: Actively scanned and exploited in the wild per VulnCheck telemetry. CVSS 9.3.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-61500
- **Reporting**: [Bleeping Computer — Rejetto HFS servers now actively scanned for critical RCE flaw](https://www.bleepingcomputer.com/news/security/rejetto-hfs-servers-now-actively-scanned-for-critical-rce-flaw/), [The Hacker News — Attackers Target Rejetto HFS Flaw That Enables Admin Session Forgery and RCE](https://thehackernews.com/2026/10/attackers-target-rejetto-hfs-flaw-that.html)

### Microsoft Exchange Server Privilege Escalation (CVE-2026-96940)
- **Description**: Weak authorization in Microsoft Exchange Server allows an authenticated attacker to elevate privileges and read other users' mailboxes under certain conditions.
- **Impact**: Authenticated attackers can escalate privileges to access and read mailboxes of other users, compromising email confidentiality.
- **Status**: Out-of-band security updates released by Microsoft. CVSS 8.8.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: patch
- **CVE IDs**: CVE-2026-96940
- **Reporting**: [The Hacker News — Microsoft Exchange Flaw Lets Authenticated Attackers Read Other Users' Mailboxes](https://thehackernews.com/2026/10/microsoft-exchange-flaw-lets.html)

### Dell System Update (DSU) CLI Critical Vulnerability
- **Description**: A critical vulnerability in the Dell System Update (DSU) command-line interface deployment tool that allows attackers to gain root privileges.
- **Impact**: Local or remote attackers can achieve root-level code execution on affected systems.
- **Status**: Dell has warned customers to patch as soon as possible.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: patch
- **Reporting**: [Bleeping Computer — New Dell System Update flaw lets hackers gain root privileges](https://www.bleepingcomputer.com/news/security/new-dell-system-update-flaw-lets-hackers-gain-root-privileges/)

### Realtek Jungle SDK Exploit (Cling Botnet Delivery)
- **Description**: A now-patched critical security flaw in the Realtek Jungle software development kit (SDK) being exploited to deploy the Cling botnet malware. The botnet repurposes ordinary STUN (Session Traversal Utilities for NAT) behavior into a practical command-and-control channel.
- **Impact**: Compromised IoT devices are enrolled into a botnet with resilient STUN-based C2 infrastructure that obscures communications.
- **Status**: Vulnerability is patched; exploit attempts observed in the wild delivering Cling botnet.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Realtek Jungle SDK Exploit Attempts Deliver Cling Botnet With STUN-Based C2](https://thehackernews.com/2026/10/realtek-jungle-sdk-exploit-attempts.html)

### Microsoft SharePoint Vulnerabilities (Warlock Campaign)
- **Description**: Suspected China-linked threat actor Warlock is weaponizing both old and new Microsoft SharePoint vulnerabilities to disable security tools and deploy ransomware.
- **Impact**: Ransomware deployment, security tool disablement, compromise of critical infrastructure, government, and education organizations.
- **Status**: Active exploitation observed by Symantec and Carbon Black Threat Hunter Team targeting Portuguese- and Spanish-speaking countries.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Warlock Exploits SharePoint Flaws to Disable Security Tools and Deploy Ransomware](https://thehackernews.com/2026/10/warlock-exploits-sharepoint-flaws-to.html)

### ClingSTUN IoT Proxy Network (24 Known Flaws)
- **Description**: A Linux backdoor operation exploiting 24 known vulnerabilities in IoT devices to compromise them and repurpose legitimate public STUN servers as proxy nodes to obscure communications.
- **Impact**: Large-scale IoT device compromise for proxy networks, enabling further attacks while hiding origin.
- **Status**: Active exploitation of known flaws across IoT device fleets.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Dark Reading — ClingSTUN Turns Vulnerable IoT Devices Into Proxy Nodes](https://www.darkreading.com/iot/clingstun-vulnerable-iot-devices-proxy-nodes)

### FortiMail Zero-Day
- **Description**: An actively exploited zero-day vulnerability in FortiMail referenced in weekly threat recap.
- **Impact**: Details not fully disclosed; active exploitation confirmed.
- **Status**: Actively exploited; patch status unclear from available reporting.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — ⚡ Weekly Recap: NetScaler and FortiMail 0-Days, AI Coding Leaks, Spectre v2 and Ransomware Arrests](https://thehackernews.com/2026/10/weekly-recap-netscaler-and-fortimail-0.html)

## Affected Systems and Products

- **Citrix NetScaler ADC and NetScaler Gateway**: Versions vulnerable to CVE-2026-88779 memory overflow in SAML deployments
- **Rejetto HTTP File Server (HFS)**: Versions with weak PRNG-based signing key generation vulnerable to CVE-2026-61500
- **Microsoft Exchange Server**: Versions affected by CVE-2026-96940 weak authorization allowing mailbox access
- **Dell System Update (DSU) CLI**: Deployment tool versions with critical root privilege escalation flaw
- **Realtek Jungle SDK**: Versions with patched critical flaw exploited for Cling botnet delivery
- **Microsoft SharePoint**: Multiple versions with old and new vulnerabilities exploited by Warlock for ransomware
- **IoT Devices (Various Vendors)**: Devices with 24 known vulnerabilities exploited by ClingSTUN for proxy node recruitment
- **FortiMail**: Versions affected by actively exploited zero-day vulnerability

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: CVE-2026-88779 exploited as zero-day in targeted attacks against NetScaler SAML deployments before patch availability
- **Session Forgery via Weak PRNG**: CVE-2026-61500 exploited through predictable signing keys from weak pseudo-random number generation, enabling admin session forgery and RCE
- **Privilege Escalation via Weak Authorization**: CVE-2026-96940 exploited by authenticated attackers to elevate privileges and access other users' mailboxes
- **Adversary-in-the-Middle (AitM) Phishing**: TA419 uses AitM phishing infrastructure impersonating prominent economists, AI policymakers, and Anthropic employees to harvest credentials from AI policy experts
- **STUN-Based Command and Control**: Cling botnet repurposes legitimate public STUN servers as C2 channels, obscuring malicious traffic within normal NAT traversal behavior
- **IoT Proxy Network via Known Flaws**: ClingSTUN exploits 24 known IoT vulnerabilities to build proxy infrastructure using STUN servers for communication obfuscation
- **SharePoint Weaponization for Ransomware**: Warlock exploits SharePoint vulnerabilities (both patched and unpatched) to disable security tools and deploy ransomware payloads
- **Root Privilege Escalation via Deployment Tool**: Dell DSU CLI flaw allows attackers to gain root access through the deployment tool interface

## Threat Actor Activities

- **TA419 (China-Aligned)**: Conducting credential phishing campaigns targeting U.S. AI policy experts at think tanks, universities, and legal organizations. Uses AitM phishing impersonating prominent economists, AI policymakers, and an Anthropic employee. Attributed to multiple campaigns observed by Proofpoint.
- **Warlock (Suspected China-Linked)**: Actively weaponizing Microsoft SharePoint vulnerabilities (old and new) to disable security tools and deploy ransomware. Targeting critical infrastructure, government, and education organizations in Portuguese- and Spanish-speaking countries. Activity observed by Symantec and Carbon Black Threat Hunter Team.
- **ShinyHunters (Extortion Group)**: Member "Rey" (Saif al-Din Khader) reportedly detained in Jordan on September 29, 2026, and cooperating with FBI to identify other group members. Group responsible for digital extortion and data theft campaigns.
- **Cling Botnet Operators**: Exploiting Realtek Jungle SDK vulnerability to deploy Cling malware with novel STUN-based C2 infrastructure. Repurposes legitimate STUN servers for resilient command-and-control.
- **ClingSTUN Operators**: Running large-scale IoT compromise operation exploiting 24 known vulnerabilities to build proxy networks using public STUN servers for traffic obfuscation.
- **China's MSS (Ministry of State Security)**: Per MI5, funding research involving 100+ U.K.-linked academics through the China General Technology Research Institute (CGTRI) to boost intelligence gathering efforts.