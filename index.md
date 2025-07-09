# Exploitation Report

Over the past week, security researchers and vendors reported an unusually dense wave of active exploitation spanning enterprise infrastructure, developer tooling, and consumer mobile platforms. Public proof-of-concept (PoC) code is now circulating for the critical CitrixBleed 2 flaw (CVE-2025-5777) in Citrix NetScaler ADC/Gateway, while Microsoft’s July Patch Tuesday disclosed an in-the-wild SQL Server zero-day that attackers are chaining with privilege-escalation techniques for full database takeover. Supply-chain attacks continue to surge: a malicious pull-request against the Ethcode VS Code extension delivered remote code execution to thousands of developers, and threat actors weaponised the Shellter red-team framework to push Lumma and SectopRAT stealers. On the IoT front, the new RondoDox botnet is exploiting long-standing weaknesses in TBK DVRs and Four-Faith industrial routers to amass DDoS firepower. Mobile users are also under fire: a novel “TapTrap” tap-jacking technique bypasses Android’s permission model, and the Anatsa banking trojan again breached Google Play. These concurrent campaigns underscore the need for immediate patching, vigilant supply-chain hygiene, and updated mobile defences.

## Active Exploitation Details

### Citrix NetScaler “CitrixBleed 2”
- **Description**: Memory-handling flaw in HTTP request processing of NetScaler ADC and Gateway appliances that leaks session tokens and permits remote code execution.  
- **Impact**: Allows unauthenticated attackers to hijack valid sessions, pivot inside VPN environments, and run arbitrary commands.  
- **Status**: PoC exploits are publicly available; active scanning observed. Citrix has issued patched firmware.  
- **CVE ID**: CVE-2025-5777  

### Microsoft SQL Server Zero-Day
- **Description**: Privilege-escalation bug in SQL Server allowing low-privileged database users to execute code in the context of the service account.  
- **Impact**: Full database compromise, lateral movement to the underlying Windows host, and potential domain takeover in mixed-mode deployments.  
- **Status**: Actively exploited prior to July Patch Tuesday; Microsoft released fixes across all supported SQL Server branches.  

### OpenSSH “regreSSHion” Remote Code Execution
- **Description**: Signal-handling race condition re-introduced in recent OpenSSH releases enabling unauthenticated remote code execution on glibc-based Linux systems.  
- **Impact**: Remote root shell with no valid credentials required.  
- **Status**: Added to CISA KEV; exploitation observed in the wild. Patches available from OpenSSH 9.8p2 onward.  

### Ethcode VS Code Extension Supply-Chain Compromise
- **Description**: Threat actor pushed a malicious pull-request that introduced obfuscated JavaScript, granting arbitrary command execution when the extension activates.  
- **Impact**: Over-the-air compromise of developer workstations, credential theft, and downstream poisoning of smart-contract code.  
- **Status**: Exploit merged and shipped to ~6,000 users before takedown; patched version released, but manual cleansing required.  

### TBK DVR Default-Cred & Four-Faith Router Command-Injection (RondoDox)
- **Description**: Combination of hard-coded/blank credentials in TBK digital video recorders and a command-injection flaw in Four-Faith industrial routers.  
- **Impact**: Devices are conscripted into the RondoDox botnet to launch high-volume DDoS attacks.  
- **Status**: Ongoing abuse; no vendor patches for many affected models, only mitigations (network isolation, credential change).  

### Android “TapTrap” Tap-Jacking Technique
- **Description**: Leverages invisible UI overlays and animation timing to trick users into granting permissions or executing destructive actions.  
- **Impact**: Silent installation of malware with Accessibility, SMS, and screen-capture privileges; potential for account takeover and data theft.  
- **Status**: Technique observed in active malware samples; Google is reviewing additional mitigations beyond existing overlay protections.  

### Shellter-Based Malware Re-Packing
- **Description**: Attackers use leaked enterprise license of the Shellter red-team tool to re-pack Lumma Stealer, Arechclient2, and Rhadamanthys with advanced AV/EDR evasion.  
- **Impact**: Credential harvesting, system information exfiltration, and foothold for follow-on ransomware.  
- **Status**: Active campaigns distributing re-packed binaries via phishing and cracked-software sites; no vendor patch (tool misuse).  

### CISA KEV – Newly Added Critical Flaws
- **Description**: Four distinct vulnerabilities across network, cloud, and application-layer technologies confirmed exploited and now mandated for federal remediation.  
- **Impact**: Ranges from remote code execution to authentication bypass.  
- **Status**: Active exploitation; vendors have issued security updates which federal agencies must apply within prescribed deadlines.  

## Affected Systems and Products

- **Citrix NetScaler ADC/Gateway**: Appliance builds prior to patched firmware 14.1-12.35 and 13.1-55.19  
  - **Platform**: On-prem and cloud-hosted NetScaler VPN gateways  
- **Microsoft SQL Server**: 2017, 2019, 2022, and Azure-managed instances pre-July 2025 cumulative patches  
  - **Platform**: Windows Server / Azure SQL  
- **OpenSSH (glibc variants)**: Versions 8.5p1 – 9.8p1 on major Linux distributions  
  - **Platform**: Linux servers and embedded systems  
- **VS Code Ethcode Extension**: Versions 0.0.24 – 0.0.27 (compromised builds)  
  - **Platform**: Windows, macOS, Linux developer workstations  
- **TBK DVR**: TBK Vision H.264 series with factory/default credentials enabled  
  - **Platform**: Physical DVR appliances exposed to the Internet  
- **Four-Faith Industrial Routers**: F-G100 & F-N200 lines running vulnerable firmware (pre-Feb 2024)  
  - **Platform**: ARM-based Linux IoT routers  
- **Android devices (all brands)** running OS 12 – 14 without enhanced overlay restrictions  
  - **Platform**: Mobile handsets and tablets  
- **Endpoints receiving Shellter-packed malware**: Windows 10/11, limited Linux build support  
  - **Platform**: Desktop and server environments  

## Attack Vectors and Techniques

- **Session Token Leakage (CitrixBleed 2)**  
  - **Vector**: Crafted HTTP/2 requests exploit improper bounds checking to dump memory containing session IDs.  

- **T-SQL Privilege Chain (SQL Server Zero-Day)**  
  - **Vector**: Malicious stored procedure triggers improper memory access, escalating to sysadmin privileges.  

- **Race-Condition Exploitation (OpenSSH regreSSHion)**  
  - **Vector**: Flood of authentication requests manipulates SIGALRM timing to execute attacker-controlled code.  

- **Malicious Pull-Request Injection (Ethcode)**  
  - **Vector**: Supply-chain compromise via GitHub PR introducing auto-executed JavaScript payload.  

- **Default-Credential Telnet Bruteforce (TBK DVR)**  
  - **Vector**: Automated scanners log in with “admin/123456” then download bot client.  

- **Command-Injection Over HTTP (Four-Faith Router)**  
  - **Vector**: Unauthenticated POST to /boaform/admin/formPing with shell metacharacters.  

- **Tap-Jacking UI Overlay (TapTrap)**  
  - **Vector**: Transparent View overlay timed to match system permission dialogs, hijacking user taps.  

- **Shellter Re-Packing & NTFS ADS Loading**  
  - **Vector**: Malware implanted into legitimate PE files, delivered via phishing, executed from Alternate Data Streams.  

## Threat Actor Activities

- **DragonForce Ransomware**  
  - **Campaign**: Social-engineering compromise of M&S leading to network-wide encryption; leveraged stolen credentials over VPN.  

- **Silk Typhoon (China)**
  - **Activity**: Suspected member arrested in Milan; group linked to long-running cyber-espionage targeting US entities.  

- **RondoDox Botnet Operators**  
  - **Campaign**: Mass exploitation of DVRs/routers to build DDoS botnet; primarily targets telecom and gaming providers.  

- **Shellter-Malware Operators**  
  - **Campaign**: Distributing Lumma, Arechclient2, Rhadamanthys via warez sites and spam; focus on credential theft at scale.  

- **TAG-140**  
  - **Campaign**: “ClickFix-style” phishing against Indian government, delivering BroaderAspect .NET loader and secondary payloads.  

- **DPRK ‘NimDoor’ Group**  
  - **Campaign**: macOS malware laced into fake Zoom invitations on Telegram, targeting Web3/crypto employees.  

- **Bert Ransomware**  
  - **Campaign**: Cross-platform Go-based strain using aggressive multithreading to encrypt Windows & Linux servers.  

- **Anatsa Banking Trojan Actors**  
  - **Campaign**: Malicious “PDF Reader” app on Google Play (>50 k installs) steals credentials from major US banks.  

## End of Report