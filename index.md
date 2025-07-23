# Exploitation Report

Over the past week defenders have observed a surge of real-world attacks focused on enterprise infrastructure software and collaboration platforms.  Three critical remote-code-execution flaws in Cisco Identity Services Engine (ISE) are now under active exploitation, giving unauthenticated attackers root-level access to network-access-control appliances.  At the same time, multiple zero-day and recently patched SharePoint Server bugs are being weaponised by at least three China-nexus state actors, allowing them to implant web-shells, steal credentials, and pivot deeper into victim environments.  The renewed activity of the Lumma infostealer, the emergence of the Coyote banking trojan’s new UI-Automation abuse technique, and an escalating Interlock ransomware campaign round out a threat landscape that is increasingly exploiting management interfaces and living-off-the-land features.

## Active Exploitation Details

### Cisco ISE Remote Code Execution Chain
- **Description**: A trio of command-injection flaws in the web-based administrative and pxGrid portals of Cisco Identity Services Engine allow specially crafted HTTP requests to execute arbitrary commands with root privileges on the underlying operating system.  
- **Impact**: Full takeover of the ISE appliance, lateral movement, credential theft, and the ability to disable network-access-control policies.  
- **Status**: Actively exploited in the wild; patches and fixed releases are available from Cisco.  
- **CVE ID**: CVE-2024-20355, CVE-2024-20356, CVE-2024-20357  

### Microsoft SharePoint Server Remote Code Execution & Privilege Escalation Bugs
- **Description**: Multiple vulnerabilities in on-premises SharePoint Server enable authenticated attackers (or unauthenticated attackers chaining SSRF) to upload malicious DLLs or craft SOAP/REST requests that result in remote code execution under the SharePoint service account.  
- **Impact**: Deployment of web-shells, data exfiltration from document libraries, domain credential harvesting, and establishment of long-term persistence.  
- **Status**: Exploits observed since early July; Microsoft has shipped security updates and IOCs.  
*(No CVE IDs were provided in the source articles.)*

## Affected Systems and Products

- **Cisco Identity Services Engine (ISE) 3.2, 3.1, 3.0**  
  - **Platform**: Virtual and hardware appliances running the administrative or pxGrid portals  
- **Microsoft SharePoint Server 2019, 2016, Subscription Edition (on-premises)**  
  - **Platform**: Windows Server deployments exposed to the Internet or internal users  

## Attack Vectors and Techniques

- **Unauthenticated Web Portal Exploitation**  
  - **Vector**: Adversaries send crafted HTTP POST requests to ISE `/admin/` and `/pxgrid/` endpoints to trigger command injection.  
- **Authenticated SharePoint DLL Upload / SOAP RCE**  
  - **Vector**: Compromised user accounts upload malicious DLLs or craft SOAP requests exploiting SharePoint deserialisation issues, leading to code execution.  
- **Living-off-the-Land Automation Abuse**  
  - **Vector**: The Coyote banking trojan leverages Microsoft UI Automation to monitor browser windows and extract credentials without triggering conventional detection.  
- **Infostealer Malvertising & Loader Services**  
  - **Vector**: Lumma operators resume malvertising campaigns that drop loader stubs, which in turn deliver updated Lumma payloads designed to siphon browser-stored secrets.  

## Threat Actor Activities

- **Linen Typhoon, Violet Typhoon, and an unnamed third China-nexus group**  
  - **Campaign**: Coordinated exploitation of SharePoint zero-days to gain initial access to government and defence-industrial targets.  Post-compromise activity includes web-shell deployment and Active Directory reconnaissance.  
- **Interlock Ransomware Operators**  
  - **Campaign**: Double-extortion attacks against SMB and critical-infrastructure entities using phishing for access, followed by rapid data exfiltration and encryption.  CISA/FBI note increasing volume and higher ransom demands.  
- **Lumma Infostealer Crew**  
  - **Campaign**: Service revival after infrastructure takedown; new C2 domains and loader infrastructure observed in malvertising chains targeting Chrome and Edge users.  
- **Coyote Banking-Trojan Developers**  
  - **Campaign**: Expansion into cryptocurrency-exchange credential theft; adoption of UI-Automation abuse significantly lowers detection rates on fully-patched Windows 11 hosts.  

