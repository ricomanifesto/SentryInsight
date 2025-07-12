# Exploitation Report

An unusual concentration of critical remote-code-execution (RCE) exploits is driving a sharp uptick in high-impact intrusions this month. The most urgent issues are a pre-authentication SQL-injection flaw in Fortinet FortiWeb, a fresh “CitrixBleed 2” session-hijacking bug in NetScaler ADC / Gateway, and an unauthenticated RCE in Wing FTP Server—all of which now have public proof-of-concept (PoC) code or confirmed in-the-wild exploitation. Simultaneously, a supply-chain compromise of the popular WordPress Gravity Forms plugin and newly disclosed “PerfektBlue” Bluetooth vulnerabilities dramatically expand attackers’ reach across web infrastructures, vehicles, and IoT devices. Ransomware operators such as the Iranian-linked Pay2Key group are actively incentivizing affiliates to exploit these weaknesses, while U.S. federal agencies have been ordered to patch affected Citrix appliances within 24 hours.

## Active Exploitation Details

### CitrixBleed 2 (NetScaler ADC & Gateway)
- **Description**: Memory-handling flaw that allows unauthenticated attackers to retrieve session tokens from vulnerable appliances, bypassing MFA and enabling full administrative takeover.  
- **Impact**: Credential/session theft, lateral movement into internal networks, potential ransomware deployment.  
- **Status**: Added to CISA’s Known Exploited Vulnerabilities catalog; active exploitation observed; fixed updates available and mandated for federal agencies.  
- **CVE ID**: CVE-2025-5777  

### Wing FTP Server Remote Code Execution
- **Description**: Improper input validation in the Wing FTP HTTP interface lets remote, unauthenticated users execute arbitrary OS commands with the privileges of the service account.  
- **Impact**: Full server compromise, data theft, or use as a beachhead for wider network intrusion.  
- **Status**: Huntress has confirmed active exploitation in the wild; vendor patch released.  
- **CVE ID**: CVE-2025-47812  

### Fortinet FortiWeb Pre-Auth SQL Injection to RCE
- **Description**: A critical SQL-injection flaw in request-handling logic can be chained to achieve pre-authentication remote code execution on FortiWeb web-application firewalls.  
- **Impact**: Complete device takeover, web-traffic interception, and pivoting into protected segments.  
- **Status**: PoC exploits publicly released within days of advisory; patches available (FortiWeb 7.4.1 & 7.2.4).  
- **CVE ID**: CVE-2025-25257  

### Gravity Forms Supply-Chain Backdoor
- **Description**: The developer’s download infrastructure was compromised, and manual installer ZIPs of the Gravity Forms WordPress plugin were trojanized with PHP backdoors.  
- **Impact**: Arbitrary code execution on thousands of WordPress sites, leading to site defacement, data theft, or further malware staging.  
- **Status**: Active distribution of backdoored packages detected; clean installers now online and integrity checks recommended.  

### McHire ‘123456’ Credential Exposure
- **Description**: An environment secured only by the password “123456” exposed internal McHire chatbot APIs and Elasticsearch data stores containing 64 million job-applicant records.  
- **Impact**: Massive PII leakage (names, emails, phone numbers, addresses), facilitating identity theft and phishing.  
- **Status**: Vulnerability discovered by researchers and remediated; historical data exposure window unknown.  

### PerfektBlue Bluetooth RCE Flaws
- **Description**: Four vulnerabilities in OpenSynergy’s BlueSDK permit 1-click or proximity-based RCE via crafted Bluetooth L2CAP/SDP traffic against vehicle infotainment units and embedded devices.  
- **Impact**: Remote takeover of vehicle subsystems, mobile devices, and industrial/medical equipment that embed the SDK.  
- **Status**: No exploitation observed yet; patches issued to OEMs, but field deployment status varies.  

### OpenVSX Extension Registry Zero-Day
- **Description**: Namespace-collision flaw allowed hostile takeover of popular VS Code extensions hosted on OpenVSX, enabling supply-chain attacks on Cursor and Windsurf IDE users.  
- **Impact**: Stealthy compromise of developer machines and CI/CD pipelines through malicious extension updates.  
- **Status**: Patched; no confirmed malicious exploitation before disclosure.  

### mcp-remote Command Injection
- **Description**: The mcp-remote automation project contains unsanitized command execution paths that let remote callers inject shell commands.  
- **Impact**: Direct OS-level code execution on systems running vulnerable versions (~437 k downloads).  
- **Status**: Fixed version released; exploitation not yet reported but considered low-barrier.  

## Affected Systems and Products

- **Citrix NetScaler ADC & Gateway**: All firmware branches prior to fixed builds (13.1-51.17, 14.1-4.5)  
- **Wing FTP Server**: Versions prior to 7.0.5 on Windows, Linux, and macOS  
- **Fortinet FortiWeb**: 7.2.x < 7.2.4 and 7.4.x < 7.4.1, including all hardware & VM form factors  
- **WordPress Gravity Forms**: Manual installers downloaded from the vendor site between 2 July – 9 July 2025  
- **McHire (Paradox.ai) Recruitment Platform**: U.S., Canada, U.K., Australia, Germany deployments using vulnerable Elasticsearch/Kibana endpoints  
- **Vehicles Using OpenSynergy BlueSDK**: Mercedes-Benz (MBUX), Volkswagen Group (VW, Skoda) 2021-2025 models; plus industrial, medical, and IoT devices embedding BlueSDK 3.x/4.x  
- **Developer Tools**: Cursor IDE, Windsurf, and any IDE pulling extensions from OpenVSX before the July patch  
- **mcp-remote Project**: All versions < 2.5.1 across npm and GitHub

## Attack Vectors and Techniques

- **Session Token Harvesting (CitrixBleed 2)**  
  - **Vector**: Crafted HTTP/HTTPS requests extract session ID data from process memory.  

- **Unauthenticated SQL Injection to Command Execution (FortiWeb)**  
  - **Vector**: Malicious query parameters inject SQL, write web-shells, and spawn system commands.  

- **Raw OS Command Injection (Wing FTP)**  
  - **Vector**: Malformed HTTP POST to administrative endpoint bypasses auth and appends shell commands.  

- **Trojanized Update / Supply-Chain Attack (Gravity Forms & OpenVSX)**  
  - **Vector**: Users install legitimate-looking packages laced with PHP or JavaScript backdoors.  

- **Bluetooth L2CAP/SDP Malformation (PerfektBlue)**  
  - **Vector**: Nearby attacker sends crafted Bluetooth packets triggering stack overflow in BlueSDK.  

- **Weak/Default Credential Abuse (McHire)**  
  - **Vector**: Direct API calls authenticated by hard-coded “123456” password.  

## Threat Actor Activities

- **Pay2Key (Iran-Linked RaaS)**  
  - **Campaign**: Relaunched platform offers 80% profit share for affiliates targeting U.S. and Israeli organizations, likely to leverage CitrixBleed 2 and FortiWeb exploits for initial access.  

- **Unattributed Supply-Chain Intrusion (Gravity Forms)**  
  - **Activities**: Compromised developer account, inserted web-shell loader, and re-signed malicious ZIPs.  

- **Unidentified Actors Exploiting Wing FTP & CitrixBleed 2**  
  - **Activities**: Huntress telemetry shows mass scanning and automated exploitation; CISA confirms federal-network targeting.  

- **Scattered Spider (Arrests)**  
  - **Campaign**: Four suspected members arrested in the U.K.; group previously used token theft and social engineering similar to CitrixBleed-style tactics.  

- **Rowhammer & Bluetooth Research Community**  
  - **Activities**: NVIDIA and independent researchers releasing mitigations and PoCs, increasing likelihood of follow-on exploitation by opportunistic attackers.  

**End of Report**