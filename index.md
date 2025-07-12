# Exploitation Report

During the past week, exploitation activity has centered on high-impact remote-code-execution flaws affecting public-facing infrastructure and widely deployed software. The most pressing threats are the actively exploited Citrix Bleed 2 vulnerability in NetScaler ADC/Gateway appliances, an in-the-wild attack wave targeting Wing FTP Server, and newly released proof-of-concept (PoC) exploits for a pre-authentication Fortinet FortiWeb SQL-injection bug. In parallel, supply-chain compromises (WordPress Gravity Forms) and large-scale exposure of Bluetooth stacks in vehicles (PerfektBlue) expand the attack surface, while ransomware crews such as Pay2Key and the data-theft collective Scattered Spider intensify their operations.

## Active Exploitation Details

### Citrix Bleed 2 (NetScaler ADC & Gateway)
- **Description**: A critical information-disclosure and session-hijacking flaw that allows remote, unauthenticated attackers to harvest session tokens and execute arbitrary actions on Citrix NetScaler ADC and Gateway appliances.  
- **Impact**: Full device takeover, lateral movement into internal networks, credential theft, and potential deployment of ransomware.  
- **Status**: Confirmed **actively exploited**; CISA added the bug to the KEV catalog and ordered U.S. federal agencies to patch immediately. Vendor fixes are available.  
- **CVE ID**: CVE-2025-5777  

### Fortinet FortiWeb Pre-Auth SQL Injection / RCE
- **Description**: A critical SQL-injection flaw in FortiWeb’s management interface enables attackers to execute arbitrary SQL commands leading to pre-authentication remote-code execution.  
- **Impact**: Complete compromise of FortiWeb appliances, web-application tampering, credential extraction, and further network intrusion.  
- **Status**: Fortinet released patches; public PoC exploits have been published, dramatically increasing exploitation risk. No vendor-reported in-the-wild incidents yet, but exploitation is expected to accelerate.  
- **CVE ID**: CVE-2025-25257  

### Wing FTP Server Directory-Traversal / RCE
- **Description**: A maximum-severity vulnerability in Wing FTP Server that attackers leverage to bypass authentication and execute commands with system privileges.  
- **Impact**: Remote code execution, data exfiltration, creation of rogue administrative accounts, and deployment of malware.  
- **Status**: **Actively exploited in the wild** according to Huntress; patches are available and must be applied urgently.  
- **CVE ID**: CVE-2025-47812  

### PerfektBlue Bluetooth Stack Vulnerabilities
- **Description**: Four flaws in OpenSynergy’s BlueSDK used by automotive, industrial, medical, and consumer devices. A single malicious Bluetooth packet can lead to one-click remote code execution.  
- **Impact**: Remote takeover of in-vehicle infotainment systems (Mercedes, Skoda, Volkswagen), industrial controllers, and up to 1 billion embedded or mobile devices.  
- **Status**: No public patches announced; vendors are assessing mitigations. No confirmed exploitation reports yet, but the attack surface is vast and close-range exploits are trivial once details are public.  

### Gravity Forms Supply-Chain Backdoor
- **Description**: Attackers compromised the Gravity Forms developer’s infrastructure and inserted a PHP backdoor into manual installer packages downloaded from the official site.  
- **Impact**: WordPress sites deploying the infected plugin inherit a remote shell, enabling full site compromise, credential theft, and malicious content injection.  
- **Status**: Malicious packages have been removed; users must verify hashes and replace affected versions.  

### McHire “123456” Credential Exposure
- **Description**: Researchers discovered that McDonald’s job-application chatbot (McHire) used the trivial password “123456” to protect MongoDB chat logs.  
- **Impact**: Unauthenticated access to conversations of 64 million applicants, exposing PII and employment data that can fuel credential-stuffing or phishing.  
- **Status**: Vulnerability disclosed and remediated; no public evidence yet of mass data theft, but exposure persisted for an extended period.  

## Affected Systems and Products

- **Citrix NetScaler ADC / Gateway**: All unsupported and unpatched versions prior to vendor fix; on-prem and cloud deployments  
  - **Platform**: Network edge / SSL-VPN appliances  
- **Fortinet FortiWeb (Web Application Firewall)**: Versions identified in advisory prior to 7.4.1; physical and virtual appliances  
  - **Platform**: Linux-based security appliance  
- **Wing FTP Server**: Windows, Linux, macOS editions prior to current hotfix  
  - **Platform**: Cross-platform FTP/SFTP/HTTP server software  
- **Vehicles using OpenSynergy BlueSDK**: Mercedes-Benz, Skoda, Volkswagen, and additional OEMs; plus industrial and medical devices with same Bluetooth stack  
  - **Platform**: Embedded Linux / RTOS environments with Bluetooth connectivity  
- **WordPress Sites running Gravity Forms manual installer (backdoored build)**  
  - **Platform**: PHP / WordPress CMS  
- **McHire Chatbot Infrastructure**: MongoDB back-end storing applicant chats  
  - **Platform**: Cloud-hosted web application  

## Attack Vectors and Techniques

- **Token Hijacking over HTTP(S)**  
  - **Vector**: Crafting requests to Citrix NetScaler endpoints to exfiltrate valid session tokens, then replaying them for unauthorized access.  
- **Pre-Auth SQL Injection → Command Execution**  
  - **Vector**: Injecting malicious SQL in FortiWeb login parameters to pivot to shell commands via database procedures.  
- **Directory Traversal & Auth-Bypass**  
  - **Vector**: Manipulating URL paths in Wing FTP Server to escape intended directories and upload/execute payloads.  
- **Bluetooth One-Click RCE (PerfektBlue)**  
  - **Vector**: Sending a single malformed L2CAP packet via Bluetooth Classic to trigger memory corruption in BlueSDK.  
- **Supply-Chain Backdoor Distribution**  
  - **Vector**: Replacing legitimate Gravity Forms ZIP installers with trojanized versions on the vendor’s download portal.  
- **Insecure Credential Exposure**  
  - **Vector**: Direct MongoDB queries over the Internet using weak hard-coded password “123456.”  

## Threat Actor Activities

- **Pay2Key (Iran-linked RaaS)**  
  - **Campaign**: Relaunched service offering 80% revenue share for affiliates targeting U.S. and Israeli organizations; expected to leverage new Citrix and Fortinet exploits for initial access.  
- **Unidentified Actors Exploiting Citrix Bleed 2**  
  - **Activities**: Mass scanning of Internet-accessible NetScaler appliances, token dumping, and follow-on ransomware deployment observed by CISA.  
- **Unknown Threat Actors (Wing FTP Campaign)**  
  - **Activities**: Active exploitation observed by Huntress; attackers create new admin users, deploy web shells, and siphon data.  
- **Supply-Chain Intruder (Gravity Forms)**  
  - **Activities**: Compromised developer’s infrastructure, inserted backdoor, and attempted wide distribution via legitimate channels.  
- **Scattered Spider**  
  - **Campaign**: UK arrests highlight ongoing investigations; group known for SIM-swap, help-desk social engineering, and leveraging VPN/VDI exploits similar to Citrix bugs for access.  

Organizations running any of the affected products should patch or mitigate immediately, monitor for anomalous authentication events, and hunt for signs of compromise related to the techniques outlined above.