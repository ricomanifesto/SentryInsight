# Exploitation Report

Chinese threat groups are actively exploiting multiple enterprise-grade collaboration and IT-service platforms, with Microsoft SharePoint and SysAid Service Management emerging as top targets. Two newly disclosed SharePoint flaws (CVE-2025-49704 and CVE-2025-49706) are being weaponized in live attacks to gain initial footholds inside government and critical-infrastructure networks. Simultaneously, unpatched SysAid instances are under fire, with adversaries chaining Remote File Access and Server-Side Request Forgery (SSRF) weaknesses to exfiltrate data and pivot laterally. CISA has fast-tracked all of these vulnerabilities into its Known Exploited Vulnerabilities (KEV) catalog and ordered federal agencies to remediate immediately, underscoring the high operational risk.

## Active Exploitation Details

### Microsoft SharePoint Server Privilege-Escalation Flaw  
- **Description**: Logic error in SharePoint’s token validation allows attackers to elevate privileges after authenticating with low-level credentials.  
- **Impact**: Enables takeover of SharePoint sites and underlying Windows servers, facilitating lateral movement and data theft.  
- **Status**: Confirmed active exploitation; Microsoft has released patches and CISA has issued a mandatory remediation directive.  
- **CVE ID**: CVE-2025-49704  

### Microsoft SharePoint Server Remote Code Execution Flaw  
- **Description**: Deserialization issue in SharePoint workflow processing lets remote, authenticated users execute arbitrary code in the web-server context.  
- **Impact**: Full remote code execution (RCE) on SharePoint servers, allowing deployment of web shells and malware payloads.  
- **Status**: Exploited in the wild; security update available and listed in CISA’s KEV catalog.  
- **CVE ID**: CVE-2025-49706  

### SysAid Remote File Access Vulnerability  
- **Description**: Input-validation weakness in the file-upload component permits attackers to read or overwrite arbitrary files on the server.  
- **Impact**: Credential harvesting, planting of malicious scripts, and exposure of sensitive configuration data.  
- **Status**: Under active attack; patch released by SysAid and prioritized by CISA.  

### SysAid Server-Side Request Forgery (SSRF) Vulnerability  
- **Description**: Inadequate sanitization of URL parameters allows crafting of internal requests, enabling attackers to interact with internal services.  
- **Impact**: Bypasses network segmentation to reach internal APIs, conduct port scanning, and retrieve cloud metadata for further compromise.  
- **Status**: Evidence of exploitation in the wild; fix available and flagged by CISA.

## Affected Systems and Products

- **Microsoft SharePoint Server (on-premises)**  
  - Versions: 2019, 2022, and older still in extended support  
  - **Platform**: Windows Server deployments in government and enterprise environments  

- **SysAid On-Premises ITSM Platform**  
  - Versions: All builds prior to the vendor’s July 2025 hotfix release  
  - **Platform**: Windows and Linux servers hosting Java-based SysAid application stacks  

## Attack Vectors and Techniques

- **Web Shell Deployment**  
  - **Vector**: Upload of malicious ASPX/ASPX.cs files via SharePoint RCE to maintain persistent remote access.  

- **Token Forgery & Privilege Escalation**  
  - **Vector**: Manipulation of SharePoint access tokens to jump from user to farm-admin privileges.  

- **Internal Service Pivoting via SSRF**  
  - **Vector**: Crafting malicious URLs in SysAid to force the server to query internal resources (e.g., AWS IMDS, internal APIs).  

- **Arbitrary File Read/Write**  
  - **Vector**: Exploiting SysAid’s file-handling flaw to dump configuration files or drop loaders that launch second-stage malware.  

## Threat Actor Activities

- **Chinese Nation-State Operators**  
  - **Campaign**: Coordinated exploitation of SharePoint CVE-2025-49704/49706 to breach U.S. government and critical-infrastructure networks, observed installing web shells and performing reconnaissance for follow-on ransomware or espionage objectives.  

- **Unattributed Criminal Groups**  
  - **Campaign**: Mass-scanning of internet-facing SysAid servers, chaining Remote File Access and SSRF flaws to steal service-desk databases containing credentials and personally identifiable information.  

- **Broader Ecosystem**  
  - Multiple China-linked clusters highlighted in recent research are engaging in a “virtual feeding frenzy,” rapidly integrating fresh SharePoint exploits into toolkits shared across cybercrime and state-sponsored communities.