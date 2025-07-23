# Exploitation Report

State-sponsored and financially motivated adversaries are concentrating on freshly disclosed server-side vulnerabilities that provide reliable remote code execution paths into enterprise environments. The most impactful activity involves three Chinese nation-state groups chaining multiple, newly published Microsoft SharePoint Server flaws to gain persistent access to public-facing collaboration sites. Simultaneously, attackers are weaponising three critical remote-code-execution bugs in Cisco Identity Services Engine (ISE) only weeks after patches were issued, indicating rapid exploit development and poor organisational patch cadence. These exploits are now feeding data-exfiltration malware, credential-harvesting campaigns, and double-extortion ransomware operations.

## Active Exploitation Details

### Microsoft SharePoint Server Post-Authentication RCE Chain
- **Description**: A set of newly disclosed SharePoint Server vulnerabilities that allow authenticated users (or those with stolen session cookies) to upload malicious payloads, trigger server-side deserialization, and execute arbitrary code with SYSTEM-level privileges.  
- **Impact**: Full takeover of on-premises SharePoint farms, lateral movement into connected Windows domains, and theft of sensitive documents stored in SharePoint libraries.  
- **Status**: Actively exploited in the wild by multiple Chinese nation-state actors; security updates are available from Microsoft but many internet-facing instances remain unpatched.

### Cisco Identity Services Engine (ISE) Remote Code Execution Vulnerabilities
- **Description**: Three independent but related flaws in Cisco ISE’s web-based administrative interface permit unauthenticated attackers to send specially crafted HTTPS requests that bypass input validation and invoke underlying operating-system commands.  
- **Impact**: Remote execution of arbitrary code as root on the network-access-control appliance, enabling attackers to disable authentication policies, create rogue network devices, or pivot deeper into corporate networks.  
- **Status**: Patches were released in the latest Cisco ISE maintenance train; proof-of-concept exploits are public and confirmed active exploitation has been observed by Cisco Talos.

### SharePoint ViewState Deserialization Zero-Day (in use prior to patch release)
- **Description**: A zero-day flaw involving unsafe ViewState handling that allowed remote attackers to inject serialized objects and achieve code execution without valid credentials under certain configuration scenarios.  
- **Impact**: Deployment of web shells, credential dumping, and establishment of resilient command-and-control channels on government and critical-infrastructure SharePoint portals.  
- **Status**: Now patched, but exploitation began at least two weeks before disclosure according to Microsoft telemetry.

## Affected Systems and Products

- **Microsoft SharePoint Server (on-premises)**: Versions 2019, 2016, and older still under extended support; internet-facing deployments hit hardest.  
- **Cisco Identity Services Engine (ISE)**: All 3.x and 4.x releases prior to the July 2025 fixed builds; appliances and virtual ISE nodes are affected.  

## Attack Vectors and Techniques

- **Deserialization RCE via ViewState**  
  - **Vector**: Upload or injection of malicious ViewState payloads into SharePoint pages, triggering .NET object deserialization.  

- **Malicious HTTPS Request Injection**  
  - **Vector**: Crafted REST or SOAP requests sent to Cisco ISE’s administrative API endpoint to bypass authentication checks and execute shell commands.  

- **Credential Stuffing & Cookie Replay**  
  - **Vector**: Stolen session cookies harvested by Lumma and Coyote infostealers reused to obtain authenticated contexts for SharePoint exploitation.  

- **Web Shell Deployment**  
  - **Vector**: Post-exploitation placement of China Chopper–style ASPX web shells in SharePoint _layouts_ directories for persistent remote management.  

- **Double-Extortion Ransomware Loading (Interlock)**  
  - **Vector**: Follow-on from Cisco ISE compromise to push ransomware binaries to NAC-controlled segments, encrypt data, and exfiltrate backups.  

## Threat Actor Activities

- **Linen Typhoon (China)**  
  - **Campaign**: Coordinated exploitation of new SharePoint flaws starting 7 July 2025 to gain footholds in defence-industrial-base organisations.  

- **Violet Typhoon (China)**  
  - **Campaign**: Parallel targeting of European and Middle-Eastern government SharePoint portals, focusing on diplomatic document theft.  

- **Unnamed Third Chinese Group**  
  - **Campaign**: Opportunistic scanning and exploitation of unpatched SharePoint instances worldwide, rapidly deploying web shells for resale on underground markets.  

- **Interlock Ransomware Crew**  
  - **Activities**: Leveraging Cisco ISE compromises and other VPN exposures to run double-extortion attacks against healthcare and manufacturing sectors.  

- **Lumma Infostealer Operators**  
  - **Activities**: Resumed large-scale credential theft after infrastructure takedown; stolen data is facilitating authenticated SharePoint intrusions.  

