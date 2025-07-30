# Exploitation Report

Over the past week defenders observed a surge of real-world exploitation activity targeting enterprise collaboration platforms, browsers, and business-critical ERP systems. Attackers are chaining newly discovered zero-days with long-patched but still-unfixed server flaws to gain initial footholds, deploy custom malware such as the “Auto-Color” backdoor, and exfiltrate sensitive data. The most consequential activity centers on a WebKit vulnerability that was first weaponised against Google Chrome and has now forced emergency patches across Apple’s Safari ecosystem; simultaneous mass compromise campaigns are abusing Microsoft SharePoint servers throughout Africa, while a critical SAP NetWeaver weakness is being leveraged to breach Linux hosts in chemical-sector environments. State-aligned groups including Silk Typhoon continue to innovate, filing patents for bespoke cyber-espionage tooling, and financially motivated groups such as Scattered Spider copycats are maintaining operational pressure despite recent arrests.

## Active Exploitation Details

### Safari / Chrome WebKit Zero-Day
- **Description**: A memory-safety flaw in the WebKit engine that allows a malicious webpage to execute arbitrary code in the context of the browser. Initially discovered in active attacks against Google Chrome, the same vulnerability impacts Safari across macOS, iOS, and iPadOS.
- **Impact**: Full browser sandbox escape leading to remote code execution, potential installation of spyware, and session hijacking.
- **Status**: Confirmed in-the-wild exploitation; Apple released out-of-band patches for Safari and the underlying WebKit framework. Google previously issued a Chrome fix.

### Microsoft SharePoint Remote Code Execution Campaign
- **Description**: Attackers are exploiting one or more RCE flaws in on-premises Microsoft SharePoint Server, enabling arbitrary file upload and execution via vulnerable API endpoints.
- **Impact**: System-level compromise of SharePoint hosts, lateral movement into Windows domains, credential harvesting, and data theft affecting government and private entities.
- **Status**: Mass exploitation observed across multiple African nations; patches have been available for months but remain unapplied in many environments.

### SAP NetWeaver Critical Flaw (“Auto-Color” Intrusion)
- **Description**: A critical vulnerability in SAP NetWeaver Application Server that allows unauthenticated attackers to craft specially formatted HTTP requests and achieve remote code execution.
- **Impact**: Initial access to Linux-based SAP landscapes followed by deployment of the Auto-Color backdoor, enabling persistent espionage, command execution, and data exfiltration.
- **Status**: Flaw is now patched by SAP; exploitation confirmed in April 2025 against a U.S. chemicals company.

### Silk Typhoon (Hafnium) Exploit Portfolio
- **Description**: Research links more than 15 Chinese corporate patents to tooling that weaponises server-side vulnerabilities—including email, VPN, and cloud collaboration zero-days—previously used by the Silk Typhoon APT.
- **Impact**: Development of proprietary implants and privilege-escalation exploits facilitating long-term espionage against Western defense, healthcare, and tech targets.
- **Status**: Tooling continues to evolve; no public patches because several techniques rely on undisclosed vulnerabilities.

## Affected Systems and Products

- **Apple Safari / WebKit**: macOS Sonoma & Ventura, iOS/iPadOS 18.x, visionOS  
- **Google Chrome**: Stable channel prior to latest emergency release on Windows, macOS, Linux  
- **Microsoft SharePoint Server**: On-premises 2019 and earlier, including out-of-support builds frequently seen in government networks  
- **SAP NetWeaver Application Server (ABAP/Java)**: Versions prior to July 2025 security update; predominantly Linux deployments  
- **Enterprise Windows Domains**: Secondary victims following SharePoint compromise  
- **Linux Servers in Chemical, Manufacturing Sectors**: Hosts running vulnerable SAP stacks breached to install Auto-Color malware  

## Attack Vectors and Techniques

- **Drive-By Browser Exploit**  
  - **Vector**: User visits malicious or compromised website leveraging WebKit memory corruption to run attacker code.

- **Server-Side RCE via SharePoint APIs**  
  - **Vector**: Crafted SOAP / REST requests upload web shells or DLLs, leading to code execution under SharePoint service account.

- **SAP HTTP Request Smuggling / Deserialization**  
  - **Vector**: Unauthenticated HTTP payload bypasses authentication controls in SAP NetWeaver, spawning a remote OS shell.

- **Malware Deployment – Auto-Color Backdoor**  
  - **Vector**: Post-exploitation script fetches ELF implant from attacker CDN, achieving persistence via systemd service.

- **Patent-Derived Exploit Kits (Silk Typhoon)**  
  - **Vector**: APT builds exploits for undisclosed flaws in email servers and cloud interfaces, distributed through spear-phishing and supply-chain attacks.

## Threat Actor Activities

- **Silk Typhoon (Hafnium)**  
  - **Campaign**: Continuous cyber-espionage against defense and tech firms; new patents suggest upcoming exploitation of novel zero-days and stealthy data exfiltration tools.

- **Unknown SharePoint Exploitation Cluster**  
  - **Campaign**: Mass scanning and automated exploitation of unpatched SharePoint servers across South Africa and neighboring regions, including the National Treasury.

- **Auto-Color Operators**  
  - **Campaign**: Targeted intrusion on a U.S. chemicals company using SAP NetWeaver exploit; objectives include intellectual-property theft and long-term persistence.

- **Scattered Spider Copycats**  
  - **Campaign**: Despite core member arrests, derivative crews continue phishing and SIM-swap techniques to infiltrate cloud environments, though overall activity has temporarily dipped.

