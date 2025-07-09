# Exploitation Report

During the past week, defenders observed a diverse range of active exploitation, spanning enterprise servers, IoT devices, developer tooling, and the Android ecosystem. A publicly-disclosed zero-day in Microsoft SQL Server is already being weaponized, while CISA fast-tracked four additional critical flaws to its Known Exploited Vulnerabilities (KEV) catalog following confirmed in-the-wild attacks. Simultaneously, the new RondoDox botnet is abusing long-neglected issues in TBK DVRs and Four-Faith industrial routers, and threat actors are leveraging a vulnerable Visual Studio Code extension (“Ethcode”) to poison developer environments. Mobile users are not spared: the “TapTrap” tapjacking technique bypasses Android’s permission UI, and the Anatsa banking Trojan continues to infiltrate Google Play. Collectively, these developments underscore the need for rapid patching, aggressive network segmentation, and continuous monitoring of both traditional infrastructure and developer supply-chain components.

## Active Exploitation Details

### Microsoft SQL Server Zero-Day
- **Description**: A flaw in how Microsoft SQL Server processes authenticated requests allows attackers to execute arbitrary code with database engine privileges.  
- **Impact**: Full compromise of the SQL Server instance, potential lateral movement, and theft or destruction of data stored in enterprise databases.  
- **Status**: Publicly disclosed and observed in targeted attacks; Microsoft issued an out-of-band fix in the July 2025 Patch Tuesday bundle.  
- **CVE ID**: (explicit CVE listed in article)

### CISA KEV – Four Newly Added Critical Vulnerabilities
- **Description**: CISA added four separate high-severity vulnerabilities affecting widely-deployed networking and web-application platforms after confirming active exploitation.  
- **Impact**: Ranges from remote code execution on edge devices to unauthenticated access and data exfiltration from web services.  
- **Status**: Exploits are circulating publicly; vendors have released patches or mitigations which CISA now requires federal agencies to apply under BOD 22-01 timelines.

### TBK DVR Remote-Code-Execution Flaw
- **Description**: An authentication-bypass vulnerability in TBK brand digital video recorders enables adversaries to issue crafted HTTP requests that spawn root-level shells.  
- **Impact**: Attackers gain full control of DVRs, integrate them into botnets, and leverage the devices for DDoS or proxying malicious traffic.  
- **Status**: Being exploited by the emerging RondoDox botnet; no official vendor patch available, only aftermarket IPS signatures.

### Four-Faith Router Command-Injection Bug
- **Description**: Improper input validation in the Web-based admin interface lets remote actors inject system commands through POST parameters.  
- **Impact**: Complete takeover of industrial or critical-infrastructure gateways, enabling network reconnaissance and pivoting into OT segments.  
- **Status**: Active exploitation by RondoDox; limited firmware updates released for newer hardware, legacy models remain unpatched.

### Ethcode VS Code Extension Supply-Chain Weakness
- **Description**: Attackers submitted a malicious pull request that leveraged inadequate integrity checking in the Ethcode extension’s update workflow, inserting backdoor code executed every time the extension starts.  
- **Impact**: Compromised developer workstations, credential theft, and potential downstream poisoning of smart-contract projects compiled on infected hosts.  
- **Status**: Exploit confirmed; extension was temporarily delisted while maintainers pushed a fixed version.

### Android “TapTrap” Tapjacking Technique
- **Description**: A UI-overlay abuse that synchronizes invisible view animations with legitimate permission dialogs, tricking users into granting high-risk permissions or activating destructive actions.  
- **Impact**: Stealth installation of spyware, unauthorized financial transfers, or factory resets without user intent.  
- **Status**: Demonstrated in the wild against devices running Android 11–14; Google is evaluating mitigations, but no OS patch yet.

## Affected Systems and Products

- **Microsoft SQL Server**: All supported on-prem and Azure-hosted builds prior to the July 2025 cumulative update  
  - **Platform**: Windows Server, Azure SQL Managed Instance  
- **TBK Digital Video Recorders**: Multiple models in the 5000/7000 series running legacy firmware  
  - **Platform**: Embedded Linux/BusyBox  
- **Four-Faith Industrial Routers (F-DD and F-NB series)**  
  - **Platform**: Linux-based embedded OS in OT/SCADA deployments  
- **Ethcode VS Code Extension ≤ v0.3.x**  
  - **Platform**: Cross-platform (Windows, macOS, Linux) developer IDEs  
- **Android Smartphones (v11–14)**  
  - **Platform**: Google Android with OEM skins; exploit demonstrated on Pixel, Samsung, and OnePlus devices  
- **Multiple Network & Web Products (per CISA KEV additions)**  
  - **Platform**: Enterprise network appliances and web-application stacks as enumerated by CISA

## Attack Vectors and Techniques

- **SQL Payload Injection**  
  - **Vector**: Crafted T-SQL statements over authenticated connections exploit internal parsing flaw.  
- **Unauthenticated HTTP API Abuse**  
  - **Vector**: Direct requests to `/device.rsp?opt=user&cmd=list` on TBK DVRs bypass login controls.  
- **Web-Interface Command Injection**  
  - **Vector**: POSTing system commands within `hostname` parameter on Four-Faith routers.  
- **Malicious Extension Update (Supply Chain)**  
  - **Vector**: Pull request merged into open-source repository pushes tainted package to VS Code Marketplace.  
- **Tapjacking (Invisible UI Synchronization)**  
  - **Vector**: Overlay window matches animation frames of system permission dialog, capturing user taps.  
- **Phishing & Social Engineering**  
  - **Vector**: Used in DragonForce ransomware initial breach of M&S and by TAG-140’s “ClickFix” lure targeting Indian government users.

## Threat Actor Activities

- **RondoDox Botnet Operators**  
  - **Campaign**: Mass-exploitation of TBK DVRs and Four-Faith routers to amass DDoS firepower; observed targeting telecom and financial services.  
- **Unknown SQL Server Exploit Group**  
  - **Campaign**: Highly targeted intrusions against U.S. healthcare and manufacturing entities leveraging the SQL zero-day prior to patch release.  
- **TAG-140 (Suspected South-Asian APT)**  
  - **Campaign**: “ClickFix-style” spear-phishing delivering .NET loader to Indian government endpoints.  
- **DragonForce Ransomware**  
  - **Campaign**: Gained initial foothold at M&S via sophisticated impersonation phishing; deployed double-extortion tactics.  
- **Silk Typhoon (China-linked)**  
  - **Campaign**: Long-running U.S. cyber-espionage; law-enforcement arrested an alleged member in Milan, disrupting current operations.  
- **Supply-Chain Threat Actors abusing Ethcode**  
  - **Campaign**: Infected >6,000 developer environments, with emphasis on blockchain and fintech projects.  

**Defenders should prioritize patching SQL Server, isolate or retire vulnerable DVRs/routers, validate integrity of VS Code extensions, and deploy mobile-device management policies to counter TapTrap abuse.**

