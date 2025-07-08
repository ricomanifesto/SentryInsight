# Exploitation Report

During the past week, multiple high-impact vulnerabilities moved from disclosure to active exploitation, significantly elevating risk for enterprise networks and consumer devices alike. The most critical events include the weaponization of a new “CitrixBleed 2” flaw in NetScaler appliances (CVE-2025-5777), an unpatched zero-day in Microsoft SQL Server that is already being abused in the wild, and IoT weaknesses leveraged by the emerging RondoDox botnet to conscript DVRs and industrial routers. At the same time, CISA expanded its Known Exploited Vulnerabilities (KEV) catalog with four additional bugs under active attack, underscoring a diverse threat landscape that stretches from core data-center services to developer tools and mobile platforms.

## Active Exploitation Details

### CitrixBleed 2 NetScaler Gateway/ADC Information-Disclosure
- **Description**: Critical request-smuggling flaw in Citrix NetScaler Gateway and Application Delivery Controller allowing unauthenticated attackers to extract session tokens and perform subsequent session hijacking.  
- **Impact**: Enables credential theft, lateral movement, and potential full network compromise. Public PoCs streamline mass exploitation.  
- **Status**: Proof-of-concept exploit released; Citrix has issued patches and urges immediate upgrades.  
- **CVE ID**: CVE-2025-5777

### Microsoft SQL Server Zero-Day
- **Description**: Privilege-escalation vulnerability in Microsoft SQL Server disclosed during July 2025 Patch Tuesday. Exploitation allows execution of arbitrary code under SQL Server service context.  
- **Impact**: Attackers can pivot from database layer to underlying OS, exfiltrate data, and deploy additional payloads.  
- **Status**: Microsoft released security updates; exploitation observed prior to patch availability (zero-day).

### RondoDox Botnet Exploits TBK DVR & Four-Faith Router Flaws
- **Description**: Combination of authentication-bypass and command-injection weaknesses in TBK digital video recorders and Four-Faith industrial cellular routers.  
- **Impact**: Devices are enslaved into a DDoS botnet capable of high-bandwidth attacks.  
- **Status**: Exploits circulating in botnet tooling; no vendor fixes referenced in reporting.

### Four Newly Added KEV Vulnerabilities
- **Description**: A set of critical flaws added by CISA to the Known Exploited Vulnerabilities catalog indicating verified in-the-wild abuse. Specifics span network appliances and widely used software.  
- **Impact**: Varies by product but includes code execution and privilege escalation.  
- **Status**: Exploitation confirmed; agencies must remediate by deadlines imposed by CISA.

### Ethcode VS Code Extension Supply-Chain Weakness
- **Description**: Maintainer account compromise (or equivalent) allowed attackers to push a malicious pull request to the Ethcode extension, slipping backdoored updates to developers.  
- **Impact**: Remote code execution within developer environments, potential theft of cryptocurrency-related secrets.  
- **Status**: Malicious version taken down; users instructed to verify extension integrity.

## Affected Systems and Products

- **Citrix NetScaler Gateway / ADC**: All firmware builds prior to vendor’s July 2025 hotfix  
  - **Platform**: On-prem and cloud-hosted network appliances  
- **Microsoft SQL Server**: Supported editions affected prior to July 2025 cumulative security update  
  - **Platform**: Windows Server environments hosting SQL Server workloads  
- **TBK DVRs**: Specific NVR/DVR lines used in physical security deployments  
  - **Platform**: Embedded Linux-based IoT devices  
- **Four-Faith Industrial Routers**: F-NBxx/F-R4xxx series  
  - **Platform**: Arm-based cellular gateways in OT and SCADA networks  
- **Visual Studio Code Ethcode Extension**: Versions pulled from the VS Code marketplace prior to clean rebuild  
  - **Platform**: Cross-platform developer workstations (Windows, macOS, Linux)  
- **Multiple Products Listed by CISA KEV**: (e.g., enterprise VPN, browser component, IoT firmware)  
  - **Platform**: Broad; agencies advised to consult KEV list for specifics  

## Attack Vectors and Techniques

- **Unauthenticated HTTP Request-Smuggling**  
  - **Vector**: Crafted requests to vulnerable Citrix NetScaler endpoints               

- **Database Privilege Escalation via SQL Server Engine**  
  - **Vector**: Malicious T-SQL or extended stored procedures exploiting zero-day  

- **Botnet Device Enrollment via Default Credentials & Command Injection**  
  - **Vector**: Internet-wide scanning for TBK/Four-Faith devices on known ports

- **Malicious Pull Request / Extension Hijack**  
  - **Vector**: Compromised GitHub workflow updates pushed to Ethcode users

- **Mass Exploit Automation Using Published PoCs**  
  - **Vector**: Script-based exploitation frameworks weaponizing newly disclosed flaws

## Threat Actor Activities

- **Unidentified Crimeware Operators (CitrixBleed 2)**  
  - **Campaign**: Rapid adoption of PoC to steal active sessions across enterprises; focus on remote access gateways.

- **Unknown Actor(s) Exploiting MSSQL Zero-Day**  
  - **Campaign**: Targeted intrusions against data-rich environments prior to Microsoft patch release.

- **RondoDox Botnet Maintainers**  
  - **Campaign**: Ongoing DDoS-for-hire service leveraging compromised DVRs and routers; observed infrastructure growth.

- **CISA-Flagged Actors**  
  - **Campaign**: Diverse; exploitation of four newly cataloged KEV flaws against U.S. federal and critical-infrastructure networks.

- **Supply-Chain Adversary in Ethcode Incident**  
  - **Campaign**: Aimed at blockchain developers; weaponized VS Code extension to implant backdoors and steal cryptocurrency keys.

