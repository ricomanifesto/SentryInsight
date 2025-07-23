# Exploitation Report

Chinese nation-state actors and opportunistic cybercriminals are actively hammering newly disclosed Microsoft SharePoint and SysAid service-desk vulnerabilities, enabling initial access, privilege escalation, and remote data theft across government and enterprise networks. CISA has fast-tracked both sets of flaws to its Known Exploited Vulnerabilities (KEV) catalog, issuing emergency patch directives as in-the-wild exploitation surges. Concurrently, red-team and criminal operators continue to weaponize Kerberoasting for credential compromise, while the Lumma infostealer operation rebounds after takedown, amplifying post-exploitation data-exfiltration risks.

## Active Exploitation Details

### Microsoft SharePoint Server Flaws  
- **Description**: Two critical bugs in on-premises SharePoint Server allow authenticated attackers to chain crafted API requests that bypass permission checks and execute privileged operations.  
- **Impact**: Enables remote code execution, data exfiltration, and full SharePoint farm takeover, often leveraged for subsequent lateral movement inside Windows domains.  
- **Status**: Actively exploited in the wild; emergency patches available from Microsoft. CISA added both flaws to the KEV catalog with a 7-day remediation mandate for U.S. federal agencies.  
- **CVE ID**: CVE-2025-49704  
- **CVE ID**: CVE-2025-49706  

### SysAid IT Support Software Path Traversal & SSRF  
- **Description**: Unauthenticated HTTP requests to vulnerable SysAid endpoints permit arbitrary file read via path traversal and server-side request forgery, exposing internal resources.  
- **Impact**: Attackers can harvest configuration files, credential stores, and pivot into internal networks, establishing persistence and exfiltrating sensitive service-desk data.  
- **Status**: Confirmed active exploitation; vendor hotfixes released and CISA added the flaws to the KEV list.  

### Kerberoasting Abuse in Active Directory  
- **Description**: Attackers request service tickets for Kerberos service accounts, crack the embedded hashes offline, and replay credentials to escalate privileges.  
- **Impact**: Facilitates rapid privilege escalation to domain admin and broad lateral movement without triggering traditional endpoint alerts.  
- **Status**: Continues to be broadly exploited as detections remain brittle; new research highlights improved telemetry-based detection logic rather than point-in-time heuristics.  

### Lumma Infostealer Payload Distribution  
- **Description**: Malware uses browser-credential dumping and clipboard monitoring to harvest account secrets and cryptocurrency wallets.  
- **Impact**: Post-exploitation data theft and resale on underground markets; increases risk of account takeover after initial vulnerability exploitation.  
- **Status**: Infrastructure resurrected after May takedown; observed in fresh spam and malvertising waves.  

## Affected Systems and Products

- **Microsoft SharePoint Server**: On-premises editions 2019, Subscription Edition (current channel and LTSC)  
- **Platform**: Windows Server deployments in enterprise and government networks  

- **SysAid On-Prem**: Self-hosted SysAid Help Desk versions prior to vendor July 2025 hotfix  
- **Platform**: Windows & Linux servers running Apache Tomcat / Java stack  

- **Active Directory Domains**: Any AD forest where service accounts possess SPNs  
- **Platform**: Windows Server 2012 R2 through Windows Server 2025  

- **Endpoints running Chromium-based browsers**: Targets for Lumma post-exploitation payloads  
- **Platform**: Windows, macOS, and Linux workstations  

## Attack Vectors and Techniques

- **SharePoint API Abuse**  
  - **Vector**: Authenticated HTTP POST/GET to `_api/ProjectServer` endpoints with manipulated tokens to bypass ACLs, leading to command execution via workflow injection.  

- **SysAid Path Traversal & SSRF**  
  - **Vector**: Direct unauthenticated GET requests to `/sysaid/*` servlet paths containing `../../../../` sequences or crafted URLs that force the server to fetch attacker-controlled resources.  

- **Kerberoasting**  
  - **Vector**: Use of `GetUserSPNs.py`, Rubeus, or native `SetSPN` enumeration to request RC4-encrypted service tickets for offline cracking.  

- **Malvertising / Spam for Lumma Loader**  
  - **Vector**: Fake software installers and SEO-poisoned ads dropping loader DLLs that beacon to revived C2 domains.  

## Threat Actor Activities

- **Actor/Group**: UNC3886, Storm-0062, and ChamelGang (China)  
  - **Campaign**: Coordinated exploitation of SharePoint CVE-2025-49704/49706 for initial access into defense, telecom, and critical-infrastructure networks, followed by custom web shells and Cobalt Strike beacons.  

- **Actor/Group**: Unnamed financially motivated cluster leveraging SysAid flaws  
  - **Campaign**: Mass scanning of internet-exposed SysAid servers, immediate data harvesting, and sale of access on Russian-language forums.  

- **Actor/Group**: Red-team tools adopted by ransomware affiliates  
  - **Campaign**: Kerberoasting integrated into open-source automation scripts (Impacket, Rubeus) during post-exploitation phases to obtain domain credentials.  

- **Actor/Group**: Lumma Team  
  - **Campaign**: Relaunched infostealer distribution, targeting cryptocurrency users and corporate employees through malvertising, restoring portions of previously seized infrastructure.  

