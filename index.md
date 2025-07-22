# Exploitation Report

A surge of hostile activity is currently centered on Microsoft SharePoint. Security vendors and Microsoft confirm that a zero-day flaw nicknamed “ToolShell” is being mass-exploited to gain initial footholds in U.S. government agencies and private organizations worldwide. Attackers are weaponizing the vulnerability to upload web shells, execute arbitrary code, and pivot deeper into victim networks. Microsoft issued an out-of-band fix, but large numbers of Internet-facing servers remain unpatched, keeping the threat level high. Separately, a privacy-impacting bug in ExpressVPN’s Windows client was patched after it leaked users’ real IP addresses during Remote Desktop sessions.

## Active Exploitation Details

### Microsoft SharePoint “ToolShell” Remote Code Execution
- **Description**: A flaw in SharePoint Server allows a remote, unauthenticated attacker to upload and execute arbitrary files (“ToolShell” payloads) by sending specially crafted HTTP requests to vulnerable endpoints. Successful exploitation results in full compromise of the underlying Windows host.  
- **Impact**: Remote code execution, installation of persistent web shells, lateral movement, data theft, and potential full domain takeover.  
- **Status**: Actively exploited in the wild; Microsoft released an emergency security update on July 20 2025. All on-premises SharePoint deployments should patch immediately or remove external exposure.  
- **CVE ID**: CVE-2025-53770  

### ExpressVPN Windows Client RDP Traffic Leak
- **Description**: A routing flaw in ExpressVPN’s Windows application caused Remote Desktop Protocol (RDP) traffic to bypass the encrypted VPN tunnel, revealing the user’s true IP address to remote systems.  
- **Impact**: Loss of anonymity, exposure of the user’s physical location, and increased susceptibility to targeted attacks or network reconnaissance.  
- **Status**: Patch released; users must update to the latest Windows client version. No confirmed in-the-wild exploitation, but the bug created real-world exposure windows.  

## Affected Systems and Products

- **Microsoft SharePoint Server 2019 & SharePoint Server Subscription Edition**  
  - **Platform**: On-premises Windows Server installations exposed to the Internet  

- **ExpressVPN Windows Client (pre-patch builds prior to June 2025)**  
  - **Platform**: Windows 10/11 endpoints using RDP while connected to ExpressVPN  

## Attack Vectors and Techniques

- **Malicious HTTP Payload Upload (SharePoint)**  
  - **Vector**: Crafted HTTP requests exploit the “ToolShell” flaw to upload web shells and execute PowerShell commands remotely.  

- **VPN Tunnel Bypass via RDP (ExpressVPN)**  
  - **Vector**: RDP traffic exits the local interface instead of the VPN adapter, leaking source IP information to the RDP server.  

## Threat Actor Activities

- **Unknown Nation-State Operators**  
  - **Campaign**: Leveraging CVE-2025-53770 to breach U.S. government departments and commercial enterprises; post-exploitation activities include credential dumping and data exfiltration.  

- **APT41 (China-Linked)**  
  - **Campaign**: Ongoing espionage against African government IT services using hard-coded internal hostnames and stealthy implants (no new CVE identified, but activity coincides with broader exploitation of unpatched enterprise apps).  

- **NoName057(16)**  
  - **Campaign**: DDoS operations disrupted by recent Europol sting; group’s infrastructure and membership fractured, reducing immediate threat but potentially spawning splinter cells.  

**Bold patching action and continuous monitoring of SharePoint servers remain the highest priority to mitigate the current wave of zero-day exploitation.**