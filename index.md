# Exploitation Report

Over the past week the most critical exploitation activity centers on two high-impact vulnerabilities: “CitrixBleed 2” (CVE-2025-5777) in Citrix NetScaler ADC/Gateway appliances and a cluster of four VMware ESXi zero-days disclosed and patched after live exploitation at Pwn2Own Berlin 2025.  CitrixBleed 2 is already being weaponised in the wild—well before public proof-of-concept code became available—allowing unauthenticated attackers to hijack sessions and achieve remote code execution on vulnerable appliances.  The VMware flaws, although demonstrated by researchers in a controlled environment, have now been fully disclosed and patched, raising the risk of copy-cat attacks against virtualisation infrastructure that underpins both on-prem and cloud workloads.  Concurrently, Chinese state-sponsored groups continue to leverage a mix of stolen credentials and older n-day bugs to compromise high-value networks in Taiwan’s semiconductor sector and within the U.S. National Guard, while financially-motivated actors abuse Microsoft Teams voice calls and public GitHub repositories to distribute malware at scale.

## Active Exploitation Details

### CitrixBleed 2 (NetScaler ADC/Gateway)
- **Description**: Memory-handling flaw in the VPN/Gateway service that leaks session tokens and enables unauthenticated attackers to execute arbitrary commands on the appliance.  
- **Impact**: Full device compromise leading to lateral movement, data theft, and potential network-wide access.  
- **Status**: Confirmed in-the-wild exploitation began two weeks before PoC releases; patched firmware is now available from Citrix.  
- **CVE ID**: CVE-2025-5777  

### VMware ESXi / Workstation / Fusion Zero-Days
- **Description**: Four distinct vulnerabilities—including stack-based buffer overflows and use-after-free conditions—allow guest-to-host escapes or code execution on the hypervisor layer.  All were exploited as zero-days during the Pwn2Own Berlin 2025 contest.  
- **Impact**: Attackers achieving a successful exploit gain control of the host OS from a guest VM, facilitating full takeover of virtualised workloads or lateral movement into management networks.  
- **Status**: Patched in the May 2025 security updates; no public malicious exploitation confirmed yet, but exploit details are now available.  

### Credential Abuse in National Guard Breach
- **Description**: Salt Typhoon leveraged stolen administrator credentials and living-off-the-land techniques to maintain persistence inside a National Guard network for nine months.  
- **Impact**: Exfiltration of network configuration files, providing detailed topology information that can be weaponised for future attacks.  
- **Status**: Intrusion uncovered; remediation and hardening underway.  No patch is applicable—focus is on credential lifecycle and monitoring improvements.  

### Semiconductor Supply-Chain Intrusions (4 Chinese APTs)
- **Description**: Multiple Chinese APT groups exploited known but unpatched vulnerabilities along with spear-phishing and supply-chain compromises to infiltrate Taiwan’s semiconductor manufacturers.  
- **Impact**: Intellectual-property theft, production disruption, and strategic intelligence collection.  
- **Status**: Ongoing campaigns; organisations are issuing emergency patch directives and network segregation measures.  

## Affected Systems and Products

- **Citrix NetScaler ADC & Gateway**: 14.1-x before 14.1-4.10; 13.1-x before 13.1-51.28; 13.0-x before 13.0-92.21  
  - **Platform**: On-prem hardware & virtual appliances (VPX/MPX) in enterprise and MSP environments  

- **VMware ESXi**: 8.x and 7.x hypervisors  
  - **Platform**: Bare-metal servers running VMware virtualisation stacks  

- **VMware Workstation 18 / Fusion 13 / VMware Tools 12**  
  - **Platform**: Windows, Linux, and macOS endpoints used for local virtualisation  

- **U.S. Army National Guard Windows & Cisco network infrastructure**  
  - **Platform**: Hybrid AD environments, Cisco routers/switches, VPN endpoints  

- **Taiwan Semiconductor Sector**: EDA servers, manufacturing OT networks, email gateways  
  - **Platform**: Mixed Windows/Linux, proprietary manufacturing control systems  

## Attack Vectors and Techniques

- **Session Token Hijacking (CitrixBleed 2)**  
  - **Vector**: Crafted HTTP/HTTPS requests to the VPN gateway leak valid session tokens, enabling direct API calls for code execution.  

- **Guest-to-Host Escape (VMware Zero-Days)**  
  - **Vector**: Malicious code executed inside a VM triggers memory corruption in the hypervisor process, gaining control of the underlying host.  

- **Living-off-the-Land Persistence**  
  - **Vector**: Abuse of built-in Windows utilities (e.g., PowerShell, WMI) and legitimate admin credentials to avoid detection post-breach (Salt Typhoon).  

- **Spear-Phishing & Supply-Chain Packages**  
  - **Vector**: Targeted emails with weaponised attachments and trojanised third-party software updates aimed at semiconductor R&D engineers.  

- **Microsoft Teams Voice-Call Social Engineering**  
  - **Vector**: Attackers impersonate IT helpdesk to initiate Teams calls, dropping Matanbuchus loader via malicious links in the call chat pane.  

- **Malware Hosting on GitHub**  
  - **Vector**: Public repositories store encrypted payloads; Amadey loader retrieves and decrypts them on victim hosts, bypassing traditional web filtering.  

## Threat Actor Activities

- **Unknown Crimeware Groups**  
  - **Campaign**: Early exploitation of CitrixBleed 2 for ransomware deployment and credential harvesting across healthcare and finance sectors.  

- **Security Researchers (Pwn2Own Berlin)**  
  - **Campaign**: Demonstrated functional exploits against VMware products, resulting in coordinated disclosure and rapid vendor patches.  

- **Salt Typhoon (Chinese State-Sponsored)**  
  - **Campaign**: Nine-month covert operation inside National Guard networks focused on reconnaissance and configuration theft.  

- **APT41, BlackTech, UNC4841, and Mustang Panda**  
  - **Campaign**: Parallel operations against Taiwan’s semiconductor supply chain using spear-phishing, proxy tooling, and side-loading techniques to steal IP and disrupt production.  

- **Matanbuchus Operators (FIN-style group)**  
  - **Campaign**: Using Microsoft Teams voice calls to seed initial infections that lead to data theft and follow-on ransomware.  

- **Amadey MaaS Affiliates**  
  - **Campaign**: Leveraging GitHub to host secondary stealers (RedLine, Racoon) while rotating repositories to evade takedowns and detection.  

---

**Prepared by:** Threat Hunting & Vulnerability Exploitation Analysis Team  
**Date:**  2025-07-XX