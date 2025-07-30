# Exploitation Report

A surge of high-impact exploitation is underway across enterprise collaboration platforms, browser engines, and business-critical ERP infrastructure. Attackers are abusing a freshly patched WebKit flaw that was used as a zero-day in Google Chrome, weaponizing an SAP NetWeaver remote-code-execution bug to implant “Auto-Color” malware on Linux hosts, and running mass compromise campaigns against unpatched on-premises Microsoft SharePoint servers in Africa and other regions. State-sponsored operators such as **Silk Typhoon (Hafnium)** and financially-motivated cyber-crime crews are actively leveraging these weaknesses to gain initial access, deploy backdoors, and steal data.

## Active Exploitation Details

### Safari / WebKit Remote Code Execution Zero-Day  
- **Description**: Memory-safety flaw in WebKit that allows maliciously crafted web content to achieve arbitrary code execution in the browser sandbox. Initially surfaced as a Chrome zero-day in Blink’s WebKit fork and now confirmed in Safari.  
- **Impact**: Full takeover of the browsing session, potential malware delivery, and cross-site scripting leading to credential theft.  
- **Status**: Actively exploited in the wild; Apple has released emergency patches for macOS, iOS, iPadOS, tvOS, and watchOS.  

### SAP NetWeaver Critical Flaw (Auto-Color Backdoor Vector)  
- **Description**: Remote unauthenticated vulnerability in SAP NetWeaver Application Server (Java) LM Configuration Wizard that permits creation of arbitrary users and execution of OS commands. Threat actors leveraged it to drop the “Auto-Color” malware inside a U.S. chemicals firm’s Linux estate.  
- **Impact**: Complete system compromise, lateral movement into adjacent Linux servers, data exfiltration, and long-term persistence through the Auto-Color backdoor.  
- **Status**: Patch released by SAP earlier this year; exploits observed in April 2025 indicate widespread availability of weaponized proof-of-concept code.  

### Microsoft SharePoint On-Premises Remote Code Execution Chain  
- **Description**: Cluster of SharePoint remote-code-execution and privilege-escalation bugs being chained to deploy web shells. Attackers scan for exposed servers and exploit vulnerable `_layouts/15/` endpoints.  
- **Impact**: Attackers obtain SYSTEM-level access, siphon sensitive documents, and pivot inside government and private networks.  
- **Status**: Mass exploitation campaign ongoing; Microsoft has issued cumulative security updates, but many servers in South Africa and neighboring countries remain unpatched.  

## Affected Systems and Products

- **Apple Safari / WebKit**  
  - **Platform**: macOS Sonoma & Ventura, iOS/iPadOS 18.x, tvOS, watchOS  

- **Google Chrome (Blink / WebKit components)**  
  - **Platform**: Windows, macOS, Linux – versions prior to the mid-July stable channel update  

- **SAP NetWeaver AS Java (LM Configuration Wizard component)**  
  - **Platform**: Linux and UNIX deployments running unpatched NetWeaver 7.x tracks  

- **Microsoft SharePoint Server 2013, 2016, 2019 (on-premises)**  
  - **Platform**: Windows Server environments exposed to the Internet without latest cumulative updates  

## Attack Vectors and Techniques

- **Drive-By Browser Exploitation**  
  - **Vector**: Malicious or compromised websites trigger the WebKit RCE to execute shellcode in Safari/Chrome.  

- **Unauthenticated SAP Endpoint Abuse**  
  - **Vector**: Direct HTTP POST requests to the `/CTCWebService` interface craft payloads that invoke user creation and OS command execution.  

- **SharePoint Web-Shell Deployment**  
  - **Vector**: Chained RCE vulnerabilities upload `aspx` web shells to the `_layouts` directory, providing persistent remote command execution.  

- **Post-Exploitation Lateral Movement**  
  - **Vector**: Use of harvested credentials and built-in tools (PowerShell Remoting, SSH) to traverse internal networks once initial foothold is established.  

## Threat Actor Activities

- **Silk Typhoon (Hafnium)**  
  - **Campaign**: Continuing long-term espionage against U.S. and European critical sectors; linked subsidiaries filed patents for the very implants and C2 frameworks observed in the wild, highlighting institutional support.  

- **Unknown Crimeware Group (Auto-Color Operators)**  
  - **Campaign**: Targeted U.S. chemical sector breach via SAP NetWeaver exploit; deployed Auto-Color backdoor, exfiltrated R&D data.  

- **Regional SharePoint Intrusion Set**  
  - **Campaign**: Mass exploitation across African public-sector entities including the South African National Treasury; objective appears to be data theft and covert espionage.  

- **Scattered Spider Copycats**  
  - **Campaign**: Activity spike slowed after core member arrests, but splinter groups are attempting to replicate the group’s high-pressure extortion tactics using similar RCE chains and social-engineering playbooks.