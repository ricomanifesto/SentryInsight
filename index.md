# Exploitation Report

The most pressing exploitation activity this cycle centers on two separate but related Microsoft SharePoint zero-day flaws that adversaries are actively abusing to implant the “ToolShell” web shell, gain remote code-execution, and exfiltrate data from U.S. government agencies and private-sector networks. Microsoft issued an out-of-band patch for the primary bug (CVE-2025-53770), yet exploitation continues—especially against unpatched SharePoint 2016 servers that remain vulnerable. In parallel, a recently resolved flaw in ExpressVPN’s Windows client leaked real user IP addresses during Remote Desktop sessions, exposing sensitive source locations to any RDP server—malicious or otherwise. Law-enforcement disruption of the pro-Russian NoName057(16) collective and new Iran- and China-linked espionage campaigns round out a surge in threat-actor activity leveraging these and other weaknesses.

## Active Exploitation Details

### SharePoint “ToolShell” Remote Code Execution
- **Description**: A server-side flaw in SharePoint’s workflow or API handling allows attackers to upload or modify files and execute the ToolShell web shell with system-level privileges.  
- **Impact**: Complete compromise of SharePoint hosts, lateral movement into connected networks, data theft, and persistent backdoor access.  
- **Status**: Actively exploited since early July; emergency patch released by Microsoft, but widespread exploitation continues where patches are missing—especially on SharePoint 2016 (no vendor fix yet).  
- **CVE ID**: CVE-2025-53770  

### Un-named SharePoint Server Zero-Day (Krebs report)
- **Description**: A separate SharePoint vulnerability under active attack enabling arbitrary code execution prior to authentication. The exploit chain mirrors ToolShell but targets an additional logic flaw disclosed on July 20.  
- **Impact**: Allows threat actors to drop payloads, create administrator accounts, and pivot deeper into enterprise environments.  
- **Status**: Emergency fix issued; exploitation observed in the wild before and after patch release.  

### ExpressVPN RDP Traffic Leak
- **Description**: A routing flaw in the Windows client caused Remote Desktop Protocol (RDP) traffic to bypass the VPN tunnel, revealing the user’s true public IP to remote hosts.  
- **Impact**: Source-IP disclosure, enabling geo-tracking, targeted reconnaissance, or selective blocking/allow-listing by adversaries.  
- **Status**: Bug fixed in the latest ExpressVPN Windows release; users must upgrade to restore full tunnel integrity.  

## Affected Systems and Products

- **Microsoft SharePoint Server 2019 & Subscription Edition**: All builds prior to the July emergency update  
  - **Platform**: On-premises Windows Server deployments  
- **Microsoft SharePoint Server 2016**: Remains unpatched for CVE-2025-53770  
  - **Platform**: On-premises Windows Server deployments  
- **ExpressVPN for Windows (pre-patch builds)**: Versions prior to the hot-fix that corrects RDP routing  
  - **Platform**: Windows 10/11 endpoints running ExpressVPN client software  

## Attack Vectors and Techniques

- **ToolShell Web-Shell Implantation**  
  - **Vector**: Crafted HTTP/S requests to vulnerable SharePoint endpoints upload malicious ASPX pages, providing an interactive command interface.  

- **VPN Tunnel Bypass via Split-Tunnel Misconfiguration**  
  - **Vector**: RDP traffic tagged for local subnet escapes the VPN adapter, exposing the client’s real IP address to the remote RDP server.  

- **Credential Harvesting & Lateral Movement Post-SharePoint Compromise**  
  - **Vector**: Dumping LSASS memory and abusing stolen Kerberos tickets to move to domain controllers.  

## Threat Actor Activities

- **Unknown Nation-State Operators**  
  - **Campaign**: Widespread exploitation of SharePoint “ToolShell” CVE-2025-53770 against U.S. government agencies and commercial firms, establishing persistent footholds.  

- **APT41 (China-Linked)**  
  - **Campaign**: Ongoing espionage in African government IT infrastructures, leveraging hard-coded internal server names and compromised accounts to exfiltrate sensitive data.  

- **MOIS-Linked Operators (Iran)**  
  - **Campaign**: Distribution of “DCHSpy” Android malware disguised as VPN apps to surveil dissidents; complements infrastructure-side zero-day exploitation.  

- **NoName057(16) (Pro-Russian)**  
  - **Campaign**: Coordinated DDoS attacks on European and U.S. targets; recent Europol arrests have fragmented operational capacity but residual members still active.  

**Bolded emphasis** marks key elements; headings and bulleting adhere strictly to the requested structure for clarity and rapid operational consumption.