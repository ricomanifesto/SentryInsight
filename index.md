# Exploitation Report

The most critical exploitation activity this week centers on the continued weaponization of enterprise-grade infrastructure vulnerabilities. Attackers are actively abusing the “CitrixBleed 2” flaw (CVE-2025-5777) in NetScaler ADC/Gateway appliances and began doing so weeks before public proof-of-concept code appeared. Simultaneously, VMware rushed out emergency patches for four ESXi, Workstation, and Fusion zero-day bugs after they were successfully exploited at the Pwn2Own Berlin contest. Cisco also disclosed a maximum-severity pre-authentication flaw (CVE-2025-20337) in Identity Services Engine (ISE) that could grant root access. These high-impact weaknesses are being folded into broader intrusion campaigns by Chinese state-sponsored groups targeting Taiwan’s semiconductor sector and U.S. military networks, while cyber-criminal operators leverage novel delivery techniques—including Microsoft Teams voice-call lures and GitHub-hosted payloads—to distribute malware such as Matanbuchus, Amadey, and the AI-assisted “LameHug.”

## Active Exploitation Details

### CitrixBleed 2 (NetScaler ADC/Gateway)
- **Description**: Memory-handling flaw in the NetScaler AAA component that allows unauthenticated attackers to leak session tokens and other sensitive data via crafted HTTP requests.  
- **Impact**: Enables credential theft, session hijacking, and ultimately full administrative takeover of Citrix appliances, leading to lateral movement across corporate networks.  
- **Status**: Actively exploited in the wild at least two weeks before public PoCs; patches and mitigations are available from Citrix.  
- **CVE ID**: CVE-2025-5777  

### VMware ESXi / Workstation / Fusion Zero-Days
- **Description**: Four distinct vulnerabilities demonstrated during Pwn2Own Berlin that allow guest-to-host escapes, code execution, and privilege escalation across VMware hypervisor products.  
- **Impact**: Attackers achieving a VM escape can run arbitrary code on the host, access other guest workloads, and compromise cloud or on-prem virtual environments.  
- **Status**: Exploited as zero-days by researchers; VMware released urgent security updates that fully address all four flaws.  

### Cisco ISE Pre-Auth Command Execution
- **Description**: Input-validation weakness in the web-based interface of Cisco Identity Services Engine (ISE) and ISE-PIC permitting unauthenticated file uploads and arbitrary command execution.  
- **Impact**: Remote attackers can gain root privileges, implant backdoors, and pivot into protected network segments managed by ISE.  
- **Status**: No confirmed exploitation yet, but public disclosure and “CVSS 10” rating make rapid exploitation likely; patches are available from Cisco.  
- **CVE ID**: CVE-2025-20337  

## Affected Systems and Products

- **Citrix NetScaler ADC & Gateway**: All supported versions prior to the fixed builds released in July 2025  
  - **Platform**: On-prem or cloud-hosted NetScaler deployments (VPX, MPX, SDX)  
- **VMware ESXi**: 8.x, 7.x, and 6.7 hypervisors before July 2025 patches  
  - **Platform**: Bare-metal hypervisor in data-center and cloud environments  
- **VMware Workstation & Fusion**: Consumer and Pro editions for Windows, Linux, and macOS prior to build-numbers issued July 2025  
  - **Platform**: Desktop virtualization platforms  
- **Cisco Identity Services Engine (ISE) / ISE-PIC**: 3.x and 2.x trains up to, but excluding, fixed versions 3.3.0.443 & 2.7.0.919  
  - **Platform**: Dedicated ISE appliances and virtual machines managing network access control  

## Attack Vectors and Techniques

- **Session Token Leakage (CitrixBleed 2)**  
  - **Vector**: Malformed HTTP GET/POST requests to the /oauth/idp/profile endpoint leak memory containing valid session cookies.  
- **Guest-to-Host Escape (VMware Zero-Days)**  
  - **Vector**: Exploitation of virtual device emulation flaws from within a malicious VM to execute code on the hypervisor.  
- **Pre-Auth File Upload (Cisco ISE)**  
  - **Vector**: Crafted HTTPS multipart/form-data requests allow placement of executable files into the web root, followed by direct invocation.  
- **Teams Voice-Call Social Engineering**  
  - **Vector**: Attackers impersonate IT staff in unsolicited Microsoft Teams voice calls, dropping malicious ZIPs that sideload the Matanbuchus loader.  
- **GitHub-Hosted Payload Delivery**  
  - **Vector**: Public GitHub repos host Amadey loaders and Raccoon-style stealers, downloaded via PowerShell one-liners to bypass email/web filters.  
- **LLM-Generated Commands (LameHug)**  
  - **Vector**: Malware queries an embedded large language model to dynamically craft PowerShell and WMI commands for data exfiltration, complicating static detection.  

## Threat Actor Activities

- **Salt Typhoon (Chinese State-Sponsored)**  
  - **Campaign**: Nine-month clandestine presence in U.S. Army National Guard network, exfiltrating configuration files—likely initial access via vulnerable edge device.  
- **Multiple PRC APTs (Unnamed in report)**  
  - **Campaign**: Coordinated attacks on Taiwan’s semiconductor industry employing spear-phishing, supply-chain infiltration, and exploitation of edge services.  
- **Unidentified Crimeware Group (CitrixBleed 2)**  
  - **Campaign**: Mass scanning and compromise of Internet-exposed NetScaler appliances to harvest tokens and deploy ransomware-as-a-service payloads.  
- **Matanbuchus Operators**  
  - **Campaign**: Using Microsoft Teams voice lures to distribute loader that fetches Cobalt Strike beacons.  
- **Amadey MaaS Operators**  
  - **Campaign**: Leveraging GitHub to host rotating payloads, increasing resilience against takedowns and content filtering.  
- **BadBox 2.0 Botnet Controllers**  
  - **Campaign**: Infected 10 million Android devices via malicious firmware supply chain; currently facing Google civil action to disrupt C2 and ad-fraud infrastructure.  