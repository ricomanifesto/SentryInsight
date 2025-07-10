# Exploitation Report

Over the last week, security researchers have observed a surge of high-impact exploitation activity ranging from an unpatched Microsoft Exchange zero-day leveraged by a North-American APT against Chinese organizations to supply-chain style compromises and cloud-side container escapes.  Attackers are actively abusing exposed ASP.NET machine keys, newly disclosed ServiceNow access-control weaknesses, and architecture-level side-channel flaws in AMD CPUs.  The current threat landscape shows a clear preference for initial-access vectors that deliver immediate credential- or privilege-level advantage, followed by data-exfiltration or lateral-movement tooling.

## Active Exploitation Details

### Microsoft Exchange Server Zero-Day
- **Description**: A previously unknown vulnerability in on-premises Microsoft Exchange that allows remote, unauthenticated code execution and mailbox exfiltration.  
- **Impact**: Full takeover of the Exchange server, credential dumping, persistent back-door installation, and access to sensitive email data.  
- **Status**: Actively exploited by a North-American APT; no official patch yet. Microsoft has released interim mitigation guidance (URL rewrite rules and IIS module hardening).

### ServiceNow ACL Enforcement Bypass  
- **Description**: Logical flaw in ServiceNow access-control lists that permits low-privileged users to enumerate or extract records outside their scope when ACLs are mis-configured.  
- **Impact**: Unauthorized disclosure of sensitive corporate and customer data stored in ServiceNow tables.  
- **Status**: Hot-fixes shipped via the ServiceNow Store; exploitation attempts observed against unpatched instances.  
- **CVE ID**: CVE-2025-3648  

### Exposed ASP.NET Machine Key Abuse  
- **Description**: Gold Melody IAB leverages leaked ASP.NET validation/decryption machine keys to forge authentication cookies, bypassing login workflows in custom .NET web apps.  
- **Impact**: Immediate administrative access to web portals followed by network discovery and resale of that access to ransomware affiliates.  
- **Status**: Ongoing exploitation in the wild; mitigation requires key rotation and web-config hardening.

### Transient Scheduler Attacks (TSA) on AMD CPUs  
- **Description**: Micro-architectural side-channel that abuses transient execution in the scheduler to infer data from other processes or VMs.  
- **Impact**: Theft of cryptographic keys and other sensitive in-memory data across privilege boundaries or tenants.  
- **Status**: Proof-of-concept code publicly demonstrated; AMD preparing microcode and firmware updates, no working patch yet.  

### NVIDIA Container Toolkit Container-Escape  
- **Description**: Insecure default mount and namespace handling in the NVIDIA Container Toolkit lets attackers break out of a container, gaining host-level GPU and file-system access.  
- **Impact**: Cross-tenant data exposure in shared AI/ML clusters and potential compromise of Kubernetes nodes.  
- **Status**: Patched in Toolkit version 1.14.0; exploit code published and already folded into red-team toolkits.

### Unpatched Ruckus Wireless Management Flaws  
- **Description**: Multiple remote code-execution and privilege-escalation weaknesses in SmartZone and ZoneDirector management interfaces.  
- **Impact**: Complete compromise of the WLAN controller, ability to intercept traffic, plant rogue firmware, and pivot deeper into networks.  
- **Status**: No vendor patch available; researchers report opportunistic scanning by botnets.

## Affected Systems and Products

- **Microsoft Exchange Server (on-prem)**: All supported versions prior to emergency mitigation  
- **ServiceNow Platform**: Instances running vulnerable ACL configurations prior to Store hot-fix for CVE-2025-3648  
- **Custom ASP.NET Web Applications**: Deployments using machine keys that have leaked or are weakly protected  
- **AMD EPYC, Ryzen, Threadripper CPUs**:  Zen 2, Zen 3, and Zen 4 architectures under all major operating systems  
- **NVIDIA Container Toolkit**: Versions < 1.14.0 on Linux/Kubernetes environments  
- **Ruckus SmartZone & ZoneDirector**: All firmware builds currently offered on vendor site (no patches released)

## Attack Vectors and Techniques

- **Remote Code Execution via Outlook Web Services**  
  - **Vector**: Crafted HTTP requests reach vulnerable Exchange endpoints, triggering the zero-day.

- **ACL Enumeration (“Count(er) Strike”)**  
  - **Vector**: Malformed API queries bypass ServiceNow ACL checks to list restricted table records.

- **Authentication Cookie Forgery**  
  - **Vector**: Stolen ASP.NET machine keys sign arbitrary cookies, granting admin sessions without credentials.

- **Transient Scheduler Side-Channel**  
  - **Vector**: Speculative execution sequences leak data through timing measurements on the CPU scheduler.

- **Container Escape via Insecure Mounts**  
  - **Vector**: Attacker inside a pod binds host paths through NVIDIA Toolkit mounts, accessing root file system.

- **Web-UI RCE on Ruckus Controllers**  
  - **Vector**: Unauthenticated HTTP/HTTPS requests exploit command-injection flaws in management CGI scripts.

## Threat Actor Activities

- **North-American APT**  
  - **Campaign**: Targeted Chinese government entity using the Exchange zero-day for diplomatic espionage.  
  - **Activities**: Deployed custom web shells, performed mailbox searches, staged exfiltration to offshore VPS nodes.

- **Gold Melody (Initial Access Broker)**  
  - **Campaign**: Harvested ASP.NET machine keys from GitHub/Gist and paste sites; sold authenticated access on dark marketplaces to ransomware crews.

- **ZuRu Malware Operators**  
  - **Campaign**: Distributed trojanized ‘Termius’ macOS builds on developer forums; post-install payload provides reverse shell and clipboard monitoring.

- **DoNot APT**  
  - **Campaign**: Delivered LoptikMod payloads against a European foreign ministry, following spear-phishing and potential web-server probing for known .NET weaknesses.

- **Botnet Scanners (Unattributed)**  
  - **Campaign**: Mass-scanning of Ruckus controller IP ranges, seeking to automate exploitation of unpatched RCE paths.

---

**Prepared by:** Threat Hunting & Vulnerability Exploitation Analysis Team  
**Date:** 11 July 2025