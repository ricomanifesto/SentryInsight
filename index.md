# Exploitation Report

The most critical exploitation activity observed across the referenced articles involves Chinese nation-state actors conducting live attacks against unpatched on-premises Microsoft SharePoint servers by chaining two recently disclosed vulnerabilities (CVE-2025-49704 and CVE-2025-49706). The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has rushed these flaws into its Known Exploited Vulnerabilities (KEV) catalog and issued an emergency directive for federal agencies to apply updates. In parallel, CISA warns that still-unpatched weaknesses in SysAid IT Service Management (ITSM) software are being leveraged in the wild to achieve remote file access and server-side request forgery (SSRF). Combined, these exploits enable threat actors to gain initial access to enterprise networks, exfiltrate sensitive data, and pivot laterally using well-known post-exploitation techniques such as Kerberoasting.

## Active Exploitation Details

### Microsoft SharePoint Server Flaws
- **Description**: Two distinct SharePoint vulnerabilities allow remote attackers to bypass authentication controls, upload malicious payloads, and execute arbitrary code on vulnerable servers. Attack chains frequently culminate in web-shell deployment and privilege escalation.
- **Impact**: Full compromise of SharePoint servers, data theft from document libraries, credential harvesting, and the ability to pivot deeper into corporate networks.
- **Status**: Actively exploited in the wild; emergency patches are available from Microsoft and mandated by CISA.
- **CVE ID**: CVE-2025-49704  
- **CVE ID**: CVE-2025-49706  

### SysAid ITSM Remote File Access & SSRF Flaws
- **Description**: Unpatched weaknesses in SysAid’s on-prem IT support platform permit unauthenticated attackers to perform path traversal that exposes arbitrary server files and carry out SSRF to reach internal services.
- **Impact**: Theft of configuration files, credential exposure, internal network reconnaissance, and potential follow-on code execution.
- **Status**: Under active exploitation according to CISA; vendor patches have been released and should be applied immediately.

## Affected Systems and Products

- **Microsoft SharePoint Server (Subscription Edition, 2019, 2016)**  
  - **Platform**: Windows Server environments running on-prem SharePoint deployments.

- **SysAid IT Service Management (on-prem installations)**  
  - **Platform**: Windows and Linux servers hosting SysAid web application and associated services.

## Attack Vectors and Techniques

- **Web-Shell Deployment via SharePoint Upload**  
  - **Vector**: Exploit of SharePoint authentication bypass to upload `.aspx` or `.ashx` payloads that serve as persistent web-shells.

- **Server-Side Request Forgery (SSRF) in SysAid**  
  - **Vector**: Crafted HTTP requests abusing vulnerable endpoints to force the SysAid server to initiate connections to internal resources.

- **Kerberoasting**  
  - **Vector**: Post-exploitation technique wherein attackers request Kerberos service tickets (TGS) for service accounts and offline crack the embedded hashes to obtain plaintext passwords.

## Threat Actor Activities

- **Actor/Group**: Multiple China-based nation-state actors  
  - **Campaign**: Coordinated targeting of unpatched SharePoint servers to gain strategic footholds in government and defense contractor networks.

- **Actor/Group**: Unnamed threat actors leveraging SysAid flaws  
  - **Campaign**: Opportunistic exploitation to exfiltrate support logs and credentials, followed by lateral movement using harvested data.

- **Actor/Group**: Lumma Infostealer Operators  
  - **Campaign**: Resumed distribution of the Lumma stealer malware, capitalizing on newly compromised endpoints (including those accessed through SharePoint and SysAid breaches) to siphon browser-stored credentials, cryptocurrency wallets, and system information.

