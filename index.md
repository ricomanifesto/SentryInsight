# Exploitation Report

A new surge of malicious activity is concentrating on a small set of high-impact vulnerabilities that provide attackers with immediate, unauthenticated control over business-critical systems. The most urgent development is a wave of automated reconnaissance and fresh exploitation attempts against Progress MOVEit Transfer instances, echoing the mass ransomware breaches of 2023–2024. In parallel, a newly publicised flaw affecting 689 Brother printer models is being weaponised to obtain administrator passwords, opening paths for lateral movement in corporate networks. While other critical issues—such as the root-level RCE bugs in Cisco Identity Services Engine (ISE) and a supply-chain takeover flaw in the Open VSX Registry—have not yet been confirmed as exploited, proof-of-concept code and scanning activity suggest exploitation is imminent. Security teams should prioritise patching or mitigating these weaknesses and monitor for related threat-actor tactics detailed below.

## Active Exploitation Details

### MOVEit Transfer Pre-Authentication Vulnerabilities
- **Description**: A set of web-layer flaws in Progress MOVEit Transfer that permit unauthenticated SQL injection and arbitrary file upload, ultimately yielding remote code execution.
- **Impact**: Theft of sensitive data at scale, ransomware deployment, and full system compromise of on-prem or cloud-hosted MOVEit servers.
- **Status**: GreyNoise reports a sharp spike in global scanning beginning 27 May 2025, indicating renewed, in-the-wild exploitation. Vendor hotfixes and cumulative patches are available; unpatched systems remain highly exposed.

### Brother Printer Default-Password Generation Weakness
- **Description**: Hundreds of Brother, Fujifilm, Toshiba, and Konica Minolta printer models ship with a predictable algorithm for generating the default administrator password, allowing remote attackers to calculate valid credentials without physical access.
- **Impact**: Complete administrative control of the printing device, potential network pivoting via stored credentials, and alteration of firmware or print jobs.
- **Status**: Security researchers confirm active exploitation on internet-facing devices; Brother has released updated firmware and mitigation guidance.

## Affected Systems and Products

- **Progress MOVEit Transfer**  
  - Versions: All builds prior to the latest cumulative patch  
  - Platform: Windows / Linux on-prem, Azure and other cloud instances  

- **Brother Printers (689 models total)**  
  - Examples: DCP-L2550DW, HL-L2370DN, MFC-L8900CDW, and associated Fujifilm, Toshiba, Konica Minolta re-brands  
  - Platform: Embedded Linux firmware in network-connected printers and multi-function devices  

## Attack Vectors and Techniques

- **Automated Internet Scanning & SQL Injection (MOVEit)**  
  - **Vector**: Mass-distributed scanners identify MOVEit endpoints and inject malicious SQL payloads into file-upload handlers, spawning web-shells and exfiltrating databases.

- **Default Credential Harvesting (Brother Printers)**  
  - **Vector**: Attackers compute the admin password from publicly exposed device information (e.g., serial number) and authenticate via the web management interface to gain root-level control.

## Threat Actor Activities

- **Cl0p / Lace Tempest Ransomware Group**  
  - **Campaign**: Renewed reconnaissance of MOVEit infrastructure consistent with the 2023 data-extortion wave. Indicators include mass scanning from previously attributed IP blocks and immediate follow-up exploitation on vulnerable hosts.

- **Unidentified Botnet Operators (Printer Exploitation)**  
  - **Campaign**: Opportunistic compromise of office printers to deploy proxy malware, cryptocurrency miners, and collect network credentials. Activity observed across North America and EMEA SMB networks.

---

Security operations teams should deploy virtual patching or network filtering for unpatched MOVEit servers, push the latest firmware to all affected printer models, and continuously monitor for anomalous outbound traffic indicative of successful exploitation.