# Exploitation Report

Active exploitation continues to surge across enterprise-grade collaboration platforms and web infrastructure. The most critical development is an ongoing campaign that leverages an unpatched Microsoft Exchange zero-day to gain footholds inside Chinese networks—a rare case of a North-American aligned APT striking East. Simultaneously, the “Gold Melody” initial-access broker is abusing exposed ASP.NET machine keys to sell privileged access on underground markets. Researchers also disclosed a container-escape flaw in NVIDIA’s Container Toolkit that provides direct breakout from Kubernetes pods, and a newly-discovered ServiceNow logic flaw that lets insiders enumerate otherwise-restricted data. Together these issues underscore the breadth of modern attack surfaces—from email gateways to DevOps pipelines and SaaS back-ends.

## Active Exploitation Details

### Microsoft Exchange Zero-Day Vulnerability
- **Description**: Previously unknown server-side flaw in Microsoft Exchange abused via specially crafted requests against exposed Outlook Web Services.
- **Impact**: Enables remote code execution (RCE) and post-exploitation mail-box theft, lateral movement, and persistent access.
- **Status**: Actively exploited by a North-American APT; Microsoft has not yet released a patch or mitigation guidance.
  
### Exposed ASP.NET Machine Key Exploit (Gold Melody Campaign)
- **Description**: Attackers harvest publicly leaked `machineKey` values from misconfigured ASP.NET applications, allowing them to forge authentication cookies and decrypt ViewState data.
- **Impact**: Full authentication bypass, privilege escalation to web-server context, and subsequent sale of network access.
- **Status**: Ongoing exploitation by the Gold Melody initial-access broker; mitigation requires rotating keys and auditing repositories.

### NVIDIA Container Toolkit Container-Escape Flaw
- **Description**: A bug in the NVIDIA Container Runtime permits containers with GPU access to mount host paths and interact with device files, breaking the container isolation boundary.
- **Impact**: Host-level code execution from a compromised pod, cross-tenant data exposure in multi-user AI clusters.
- **Status**: Proof-of-concept exploit demonstrated; no official patch yet, but configuration hardening and SELinux/AppArmor profiles reduce risk.

### ServiceNow “Count(er) Strike” Enumeration Flaw
- **Description**: Logic flaw allows low-privileged users to abuse the `COUNT()` function to infer the presence and content of restricted database rows.
- **Impact**: Unauthorized disclosure of sensitive records such as incident tickets, employee PII, and financial data.
- **Status**: Vendor rolling out fixes; exploitation feasible with simple API calls and already observed during red-team exercises.

## Affected Systems and Products

- **Microsoft Exchange Server**: All on-prem versions currently supported; internet-facing Outlook Web Services.
- **ASP.NET Web Applications**: Sites that store `machineKey` values in public repos or default configurations.
- **NVIDIA Container Toolkit / nvidia-docker**: GPU-enabled Kubernetes and Docker environments on Linux hosts.
- **ServiceNow SaaS Instances**: All customer instances prior to the vendor’s July 2025 hotfix.

## Attack Vectors and Techniques

- **Server-Side Request Forgery & Deserialization**  
  - **Vector**: Malformed OWA/OAB requests trigger Exchange zero-day, leading to arbitrary file write and RCE.

- **Authentication Cookie Forgery**  
  - **Vector**: Stolen `machineKey` lets attackers sign ASP.NET forms authentication cookies, bypassing login entirely.

- **Container Escape via Device File Manipulation**  
  - **Vector**: Crafted container image accesses `/dev/nvidia*` to mount host volume and execute binaries on the underlying node.

- **Blind Enumeration Through Aggregate Functions**  
  - **Vector**: Repeated `COUNT()` queries with filtered predicates reveal row existence and, by binary search, underlying values in ServiceNow tables.

## Threat Actor Activities

- **North-American APT (Unnamed)**
  - **Campaign**: Targeting Chinese government and defense organizations with Exchange zero-day, exfiltrating mailbox contents and deploying web shells for persistence.

- **Gold Melody Initial-Access Broker**
  - **Campaign**: Harvesting leaked ASP.NET machine keys from public code repositories, breaching corporate portals, and auctioning access on dark markets.

- **DoNot APT**
  - **Campaign**: Spear-phishing European foreign ministries, delivering “LoptikMod” malware post-access; leverages misconfigurations rather than new CVEs.

- **Andariel (North Korea)**
  - **Campaign**: Revenue-generation through fraudulent “remote IT worker” placements; associated malware uses commodity loaders once foothold gained.

- **SatanLock Ransomware Group**
  - **Campaign**: Preparing mass data-leak release following purported shutdown; known to weaponize public PoCs quickly, likely to adopt NVIDIA escape if left unpatched.

