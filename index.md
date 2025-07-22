# Exploitation Report  

The most critical activity observed this cycle involves two high-impact enterprise-grade products—Cisco Identity Services Engine (ISE) and Microsoft SharePoint. Both platforms are under active attack through separate vulnerability sets that allow unauthenticated remote code execution, immediate privilege escalation to **root/SYSTEM**, and long-term persistence inside corporate networks. The Cisco flaws have now moved from “patch available” to “in-the-wild exploitation,” while the SharePoint zero-day chain is being weaponized by state-sponsored actors for credential theft, key exfiltration, and lateral movement. Together, these campaigns threaten identity infrastructure and collaboration hubs that sit at the core of many organizations’ security models.

## Active Exploitation Details  

### Cisco ISE Unauthenticated RCE Chain  
- **Description**: A trio of critical flaws in Cisco Identity Services Engine (ISE) and ISE Passive Identity Connector allow remote, unauthenticated attackers to upload malicious files and execute arbitrary commands with **root** privileges via the web-based administrative interface.  
- **Impact**: Complete takeover of the ISE appliance, manipulation of network-access policies, credential theft, and deployment of additional malware or backdoors across the identity infrastructure.  
- **Status**: Patches released by Cisco; active exploitation confirmed by Cisco, BleepingComputer, and The Hacker News. Proof-of-concept exploits are circulating in public repositories and underground forums.  

### Microsoft SharePoint Zero-Day Vulnerability Chain  
- **Description**: A previously unknown exploit chain targeting on-premises SharePoint Server leverages specially crafted HTTP requests and malicious application packages (“ToolShell” toolset) to bypass authentication, achieve remote code execution, and drop persistent web shells.  
- **Impact**: Theft of authentication keys, creation of covert admin accounts, persistent access for network reconnaissance, and staging of additional malware (e.g., credential-stealing implants).  
- **Status**: Still **zero-day**—no vendor patch released at publication time. Microsoft has issued temporary mitigation guidance; exploitation traced back to at least 7 July 2025.  

## Affected Systems and Products  

- **Cisco Identity Services Engine (ISE)**: All 3.x and 3.2 releases prior to the latest hotfixes; includes ISE-PIC modules.  
- **Cisco ISE Passive Identity Connector (ISE-PIC)**: Versions aligned with vulnerable ISE builds.  
- **Microsoft SharePoint Server 2016 / 2019 / Subscription Edition (on-prem)**: All builds without the yet-to-be-released security update; cloud-hosted SharePoint Online is not affected.  

## Attack Vectors and Techniques  

- **Unauthenticated Web-UI Exploit (Cisco ISE)**  
  - **Vector**: Direct HTTP(S) requests to the ISE management interface inject malicious payloads that are executed by the underlying root container.  

- **Malicious SharePoint Package Deployment (SharePoint Zero-Day)**  
  - **Vector**: Upload of a specially crafted SharePoint application (.wsp) or API call that triggers the vulnerability chain; culminates with a dropped web shell and “ToolShell” backdoor.  

- **Persistent Web Shell Implantation**  
  - **Vector**: Post-exploitation, attackers plant ASPX or DLL web shells to maintain access even after partial remediation.  

- **Credential & Key Exfiltration**  
  - **Vector**: Memory-scraping and key-dumping utilities executed under SYSTEM/root following successful RCE, enabling lateral movement and cloud pivoting.  

## Threat Actor Activities  

- **Unnamed Crimeware Operators (Cisco ISE Campaign)**  
  - **Campaign**: Mass scanning of port-exposed ISE appliances, rapid weaponization of public PoCs, and resale of obtained root shells in illicit marketplaces.  

- **Chinese State-Sponsored Group (SharePoint Campaign)**  
  - **Campaign**: Strategic espionage wave leveraging the SharePoint zero-day since early July 2025. Focus on technology, defense, and governmental verticals; objectives include credential harvesting and long-term foothold establishment.  

- **APT41 (Observation from Africa)**  
  - **Campaign**: Parallel operations reported by Dark Reading show APT41 expanding into African targets, reaffirming the group’s willingness to exploit freshly disclosed enterprise vulnerabilities to achieve espionage goals.  

- **Criminal Cluster Using AllaKore RAT & Hijack Loader**  
  - **Campaign**: Ongoing attacks in Mexico use phishing and loader malware, often deploying onto systems weakened by unpatched enterprise software, demonstrating the commoditization of post-exploit toolchains.  

---  

Stay vigilant by prioritizing patches for Cisco ISE, applying Microsoft’s interim SharePoint mitigations, and monitoring for web-shell artifacts and suspicious administrative activity.