# Exploitation Report

Over the past week the most critical exploitation activity centers on a newly disclosed zero-day in Microsoft SQL Server, a fast-growing botnet abusing long-standing flaws in TBK DVRs and Four-Faith industrial routers, and several supply-chain style attacks abusing development and mobile ecosystems.  In parallel, CISA has rushed four additional vulnerabilities into its Known Exploited Vulnerabilities (KEV) catalog, underscoring the continuing trend of rapid weaponization once technical details become public.  Mobile users are also at heightened risk from a novel Android “TapTrap” permission-bypass technique, while developers face threats from a compromised Visual Studio Code extension.  Collectively, these issues enable remote code execution, privilege escalation, and large-scale distributed-denial-of-service (DDoS) attacks across enterprise, IoT, and consumer environments.

## Active Exploitation Details

### Microsoft SQL Server Zero-Day
- **Description**: A previously unknown flaw in Microsoft SQL Server that allows attackers to execute code with database-level privileges by sending specially crafted queries.  
- **Impact**: Enables full takeover of the SQL instance, lateral movement, and data theft.  
- **Status**: Publicly disclosed and actively exploited in the wild; Microsoft issued a fix during the July 2025 Patch Tuesday release.  

### TBK Digital Video Recorder (DVR) Authentication/Command Injection Flaws
- **Description**: Multiple long-standing weaknesses in TBK DVR firmware, including an authentication bypass that exposes device APIs and a command-injection pathway in CGI scripts.  
- **Impact**: Remote attackers gain root-level shell access, allowing enlistment of DVRs into DDoS botnets.  
- **Status**: In wide-scale exploitation by the “RondoDox” botnet; no vendor patch publicly released.  

### Four-Faith Router Remote Code Execution Vulnerability
- **Description**: Input-validation weaknesses in the web-management interface of Four-Faith industrial cellular routers permit remote code execution via crafted HTTP requests.  
- **Impact**: Attackers obtain full OS control, pivot into OT networks, and conscript routers into botnets.  
- **Status**: Being actively weaponized by the same RondoDox operators; remediation guidance limited to hardening and network isolation.  

### “TapTrap” Android Permission-Bypass Technique
- **Description**: A tapjacking method that overlays invisible UI elements during animation frames, tricking users into approving dangerous permissions or executing destructive actions.  
- **Impact**: Grants malware access to SMS, Contacts, Accessibility Services, and can initiate device-administration privileges without user awareness.  
- **Status**: Observed in active malware samples circulating in third-party stores and sideloading campaigns; no platform-level patch yet, mitigations rely on UI/overlay restrictions in Android settings.  

### Ethcode VS Code Extension Supply-Chain Flaw
- **Description**: Attackers leveraged a vulnerable pull-request workflow in the Ethcode Visual Studio Code extension, injecting malicious code that executes whenever the extension loads.  
- **Impact**: Leads to remote code execution on developer workstations, credential theft, and wider supply-chain compromise of blockchain-development projects.  
- **Status**: Malicious pull request merged and propagated; maintainers have since pulled the tainted release and advised users to update or remove the extension.  

### Newly Added KEV Catalog Vulnerabilities (4)
- **Description**: Four separate critical vulnerabilities—spanning enterprise software, networking gear, and remote-access platforms—that CISA confirms are under active exploitation.  
- **Impact**: Each flaw enables either unauthenticated remote code execution or privilege escalation, posing immediate risk to federal and private-sector networks.  
- **Status**: Vendors have issued patches; federal agencies are ordered to remediate on an accelerated timeline.  

## Affected Systems and Products

- **Microsoft SQL Server**: All supported on-prem and cloud-hosted versions prior to the July 2025 security update  
- **TBK DVR Models**: Widely deployed “TBK-DVR4104”/“TBK-DVR4216” series running legacy firmware  
- **Four-Faith Routers**: F-R200/F-R300 industrial cellular router families, default configurations exposed to the Internet  
- **Android Devices**: All versions susceptible to overlay abuse; higher risk on Android 11 and earlier where stricter overlay controls are absent  
- **Ethcode VS Code Extension**: Versions pulled from the Marketplace prior to the emergency security patch (installed ~6,000 times)  
- **Various Enterprise/OT Platforms**: Products named in CISA’s latest KEV entry list (federal and commercial deployments)  

## Attack Vectors and Techniques

- **SQL Query Exploit**: Crafted SQL statements via exposed database ports or application connection strings to trigger code execution in SQL Server  
- **Remote Web-Interface Exploit**: HTTP/CGI requests targeting vulnerable scripts on TBK DVRs and Four-Faith routers to inject shell commands  
- **Botnet Recruitment**: Automated scanners locate IoT devices, exploit known flaws, then download RondoDox binaries for DDoS operations  
- **TapJacking (TapTrap)**: Invisible overlay and animation timing to hijack user taps during permission prompts on Android  
- **Malicious Pull Request (Supply Chain)**: Poisoned code merged into an open-source repository; updates auto-pulled by VS Code users leading to RCE  
- **Phishing & Social Engineering**: Used by threat actors such as TAG-140 and DragonForce to deliver initial payloads or ransomware  

## Threat Actor Activities

- **RondoDox Operators**  
  - **Campaign**: Large-scale scanning and exploitation of TBK DVRs and Four-Faith routers to amass a DDoS botnet capable of multi-gigabit attacks against financial-services targets.  

- **Unknown SQL Server Zero-Day Actors**  
  - **Campaign**: Exploiting unpatched SQL instances for data exfiltration and planting web shells on underlying Windows hosts prior to Microsoft’s July 2025 patch release.  

- **TAG-140**  
  - **Campaign**: Targeting Indian government entities with “ClickFix-style” lures that drop a .NET loader and subsequent payloads; leverages social-engineering rather than an application-layer vulnerability.  

- **DragonForce Ransomware Group**  
  - **Campaign**: Breached M&S via sophisticated impersonation, leading to network compromise and large-scale ransomware deployment; exploitation hinged on credential theft post-social-engineering.  

- **Silk Typhoon (Alleged)**  
  - **Campaign**: Chinese state-sponsored espionage involving unauthorized access to protected systems; key suspect arrested in Milan, disrupting ongoing activities.  

- **Shellter-Based Malware Operators**  
  - **Campaign**: Using leaked licenses of the Shellter red-team tool to wrap Lumma Stealer, SectopRAT, and other infostealers in highly obfuscated payloads that evade AV/EDR.  

**Bold emphasis** indicates confirmed active exploitation; organizations should prioritize patching and hardening measures immediately.