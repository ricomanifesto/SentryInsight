# Exploitation Report

Over the past week, security researchers and government agencies have confirmed a sharp rise in real-world exploitation of several critical vulnerabilities across enterprise networking appliances, Internet-exposed servers, automotive Bluetooth stacks, and popular developer ecosystems. Threat actors are abusing a newly disclosed Citrix NetScaler flaw (“Citrix Bleed 2”) and a critical Wing FTP Server bug while proof-of-concept code for a pre-authentication Fortinet FortiWeb SQLi/RCE has become widely available. At the same time, supply-chain compromises in WordPress Gravity Forms and the Eclipse OpenVSX registry demonstrate attackers’ continued focus on developer pipelines. The “PerfektBlue” Bluetooth attack chain dramatically expands the remote-code-execution surface to an estimated one billion devices, including 350 million vehicles. These developments underscore the urgency of rapid patching, rigorous credential management, and continuous monitoring for anomalous activity.

## Active Exploitation Details

### Citrix Bleed 2 (NetScaler ADC & Gateway)
- **Description**: A critical flaw in Citrix NetScaler ADC and Gateway that allows unauthenticated attackers to hijack sessions and gain access to sensitive resources.
- **Impact**: Full compromise of appliances, lateral movement into internal networks, and potential data exfiltration.
- **Status**: Confirmed active exploitation; CISA added it to the KEV catalog and mandated federal agencies to patch within 24 hours.
- **CVE ID**: CVE-2025-5777

### Fortinet FortiWeb Pre-Auth SQL Injection to RCE
- **Description**: A pre-authentication SQL injection in FortiWeb management interfaces enabling arbitrary database commands that cascade to remote code execution.
- **Impact**: Complete takeover of FortiWeb instances, web-shell deployment, and pivoting to protected web applications.
- **Status**: Patches released; multiple proof-of-concept exploits published and circulating.
- **CVE ID**: CVE-2025-25257

### Wing FTP Server Remote Code Execution
- **Description**: A maximum-severity flaw in Wing FTP Server permitting crafted requests to execute arbitrary commands with system privileges.
- **Impact**: Server takeover, data theft, ransomware deployment, and use as a relay for further intrusions.
- **Status**: Actively exploited in the wild; vendor patch available.
- **CVE ID**: CVE-2025-47812

### PerfektBlue Bluetooth Vulnerability Cluster
- **Description**: Four logic and memory-safety issues in OpenSynergy’s BlueSDK that allow 1-click or proximity-based remote code execution over Bluetooth.
- **Impact**: Remote control of infotainment units, unauthorized CAN bus access, and compromise of medical, industrial, and consumer Bluetooth-enabled devices.
- **Status**: No patches announced for all vendors; exploits demonstrated by researchers, with high risk of weaponization.

### McHire Default Credential Exposure
- **Description**: The McDonald’s job-application chatbot platform was protected by the weak password “123456,” exposing 64 million applicant chat transcripts.
- **Impact**: Mass leakage of PII, employment history, and potential social-engineering fodder.
- **Status**: Access revoked after disclosure; no formal patch cycle.

### Gravity Forms Backdoored Plugin Supply-Chain Attack
- **Description**: Attackers compromised the Gravity Forms developer infrastructure and replaced manual installer packages with backdoored versions.
- **Impact**: WordPress sites installing the tampered plugin inherit a PHP backdoor, enabling remote administration and malware staging.
- **Status**: Malicious packages removed; users advised to verify hashes and reinstall from clean sources.

### OpenVSX Registry Zero-Day
- **Description**: A logic flaw in the Eclipse OpenVSX extension registry allowed takeover of namespaces, letting attackers publish malicious updates to Cursor and Windsurf users.
- **Impact**: Automatic deployment of malicious IDE extensions capable of code execution on developer machines.
- **Status**: Patched; no indication of widespread abuse before disclosure.

### mcp-remote Command Injection
- **Description**: Unsanitized input in the open-source mcp-remote project leads to arbitrary OS command execution when processing remote requests.
- **Impact**: Remote takeover of servers integrating mcp-remote; potential supply-chain impact on 437,000+ downstream downloads.
- **Status**: Fix released; exploitation feasible with low complexity.

### eSIM Underlying Oracle Vulnerability
- **Description**: A six-year-old flaw in SIM card provisioning technology enables both physical and OTA attacks to clone profiles or enable silent surveillance.
- **Impact**: Covert device takeover, call/SMS interception, and geolocation tracking across millions of smartphones.
- **Status**: No universal patch; mitigations depend on carrier and device-level updates.

### NVIDIA GDDR6 Rowhammer Weakness
- **Description**: High-frequency memory-cell manipulation (Rowhammer) against GDDR6 GPUs can induce bit flips, potentially escalating GPU or system privileges.
- **Impact**: Data corruption, sandbox escapes in GPU-accelerated workloads, and persistence via malicious shaders.
- **Status**: NVIDIA advises enabling System-Level ECC; hardware-level fix pending in future generations.

## Affected Systems and Products

- **Citrix NetScaler ADC & Gateway**: All supported builds prior to vendor emergency updates  
  **Platform**: On-prem and cloud ADC/Gateway appliances  
- **Fortinet FortiWeb**: Versions 7.4.0, 7.3.x, 7.2.x, and earlier without the July 2025 hotfix  
  **Platform**: Dedicated FortiWeb hardware and virtual appliances  
- **Wing FTP Server**: All editions before the 7.4.9 security release  
  **Platform**: Windows, Linux, macOS server deployments  
- **OpenSynergy BlueSDK**: Firmware used by Mercedes, Volkswagen, Skoda, and numerous IoT/medical devices  
  **Platform**: Automotive ECUs, Android-based infotainment systems, embedded Linux devices  
- **McHire (Gr8 People)**: U.S. instance of McDonald’s recruitment chatbot platform  
  **Platform**: Cloud-hosted web application  
- **Gravity Forms WordPress Plugin**: Manual installers downloaded from gravityforms[.]com between mid-June and early July 2025  
  **Platform**: WordPress CMS on Linux/Windows hosting  
- **Eclipse OpenVSX**: Namespace management affecting Cursor, Windsurf, and other VS Code-compatible IDEs  
  **Platform**: Developer workstations on Windows, macOS, Linux  
- **mcp-remote Project**: Versions prior to v2.8.3  
  **Platform**: Node.js servers integrating Model Context Protocol (MCP) features  
- **Global eSIM Implementations**: Smartphones and IoT devices leveraging Oracle-based SIM provisioning tech  
  **Platform**: Android, iOS, embedded Linux  
- **NVIDIA GDDR6 GPUs**: GeForce RTX 20-, 30-, and 40-series, selected professional GPUs  
  **Platform**: Windows, Linux workstations and servers

## Attack Vectors and Techniques

- **Pre-Authentication SQL Injection**  
  Vector: Crafted HTTP POST requests to FortiWeb `/api/v2.0/users` endpoint inject SQL leading to RCE.  

- **Session Token Hijacking**  
  Vector: Manipulation of NetScaler request handling to capture/rehydrate authentication cookies (Citrix Bleed 2).  

- **Unauthenticated Command Execution via FTP Requests**  
  Vector: Malformed commands to Wing FTP Server trigger buffer/logic flaws for system-level command execution.  

- **Bluetooth One-Click RCE (“PerfektBlue”)**  
  Vector: Sending malicious SDP records over RFCOMM; victim only needs to accept a single prompt (e.g., play track).  

- **Default Credential Abuse**  
  Vector: Publicly accessible McHire dashboard protected by weak preset password “123456.”  

- **Supply-Chain Package Poisoning**  
  Vector: Replacement of Gravity Forms ZIP installers with backdoored PHP payloads.  

- **Namespace Takeover in Extension Registry**  
  Vector: OpenVSX flaw allowed adversaries to seize extension IDs and push malicious updates automatically.  

- **Command Injection via Unsanitized Parameters**  
  Vector: mcp-remote’s API passes user-supplied strings directly to shell commands.  

- **Rowhammer Memory Disturbance**  
  Vector: Rapid activation of adjacent GDDR6 rows flips bits, bypassing software sandboxing.  

- **eSIM Profile Manipulation**  
  Vector: Exploiting legacy Oracle code paths to overwrite or clone embedded SIM profiles via SMS/OTA.

## Threat Actor Activities

- **Pay2Key Ransomware (Iran-linked)**  
  Campaign: Relaunched RaaS platform offering 80 % profit share for attacks on U.S. and Israeli organizations; recruiting affiliates on dark-web forums.  

- **Unidentified Citrix Bleed 2 Operators**  
  Activities: Mass-scanning and weaponization against exposed NetScaler appliances across federal and enterprise networks.  

- **Gravity Forms Supply-Chain Intruders**  
  Activities: Compromised developer account, implanted PHP backdoor, and attempted to maintain persistence on WordPress sites.  

- **PoC Weaponizers Targeting Fortinet FortiWeb**  
  Activities: Rapid integration of public exploits into automated scanners; attempts observed to deploy web shells on vulnerable FortiWeb edge devices.  

- **Unknown Actors Testing PerfektBlue**  
  Activities: Researchers observed Bluetooth probe traffic consistent with vulnerability mapping in urban areas with high concentrations of affected vehicles.  

- **Scattered Spider (Arrests Announced)**  
  Campaign: UK law enforcement arrested four suspected members tied to high-profile data-extortion campaigns, potentially disrupting future operations.  

- **Ransomware Negotiator (Russian Basketball Player)**  
  Activities: Acted as a go-between for ransomware gangs and victims; arrest may temporarily impact certain ransomware operations.  

**End of Report**