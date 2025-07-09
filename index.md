# Exploitation Report

The past week’s intelligence highlights a concentrated wave of real-world exploitation against edge devices, development tooling, and core enterprise software. The most critical developments include a newly disclosed Microsoft SQL Server zero-day, four fresh additions to CISA’s Known Exploited Vulnerabilities (KEV) catalog, and an IoT campaign in which the “RondoDox” botnet is actively roping vulnerable TBK DVRs and Four-Faith industrial routers into DDoS swarms. Supply-chain risk also surged: attackers weaponised a weakness in the “Ethcode” Visual Studio Code extension via malicious pull requests, while mobile users are being abused through the TapTrap Android UI-bypass technique. These threats collectively enable remote code execution, full device takeover, and large-scale network disruption, underlining the need for accelerated patching, hardening, and continuous monitoring.

## Active Exploitation Details

### Microsoft SQL Server Zero-Day (July 2025 Patch Tuesday)
- **Description**: A publicly disclosed flaw in Microsoft SQL Server allowing crafted queries or network messages to escape the database context and achieve elevated privileges or remote code execution.
- **Impact**: Enables full compromise of SQL Server instances, exfiltration or destruction of data, and potential lateral movement into connected Windows hosts.
- **Status**: Patched in Microsoft’s July 2025 updates; exploitation observed in the wild prior to release.
  
### TBK DVR Flaws Exploited by RondoDox
- **Description**: Multiple unauthenticated command-injection and credential-bypass issues in TBK digital video recorders that expose management interfaces directly to the Internet.
- **Impact**: Attackers gain root‐level shell access, allowing device enlistment into botnets, live video hijacking, and pivoting inside physical-security networks.
- **Status**: Actively exploited to build the RondoDox DDoS botnet; no official vendor patch referenced in reporting.

### Four-Faith Industrial Router Vulnerabilities
- **Description**: Remote code-execution weaknesses in Four-Faith F-Series cellular/IIoT routers caused by inadequate input sanitisation on web-management endpoints.
- **Impact**: Full takeover of routers, modification of routing tables, and integration into RondoDox for reflected-amplification attacks.
- **Status**: Exploits circulating publicly; remediation guidance limited to disabling remote administration and applying latest firmware where available.

### Ethcode VS Code Extension Supply-Chain Compromise
- **Description**: Attackers submitted a malicious pull request that exploited inadequate integrity checks in the Ethcode extension’s update pipeline, injecting backdoor code into the package.
- **Impact**: Developers who update or freshly install Ethcode (≈6,000 installs) execute attacker-controlled JavaScript that can steal private keys, source code, and environment tokens.
- **Status**: Campaign confirmed; extension removed from the Visual Studio Marketplace and a clean rebuild published.

### TapTrap Android UI-Bypass Technique
- **Description**: A novel “tapjacking” approach that times invisible UI overlays with transition animations, tricking users into granting permissions or executing destructive actions without visual cues.
- **Impact**: Grants malware access to SMS, accessibility services, or financial apps, bypassing Android’s normal permission prompts.
- **Status**: Technique observed in active malware campaigns; Google working on mitigations in upcoming Android security releases.

### CISA KEV Catalog – Four Newly Exploited Vulnerabilities
- **Description**: CISA added four critical flaws to the KEV list following confirmed exploitation; the set spans VPN, mobile-device-management, web-framework, and managed-file-transfer software.
- **Impact**: Each vulnerability enables remote code execution or authentication bypass, facilitating ransomware deployment and data breaches across federal and private networks.
- **Status**: Vendors have shipped patches, and U.S. federal agencies are mandated to remediate by CISA’s specified deadlines.

## Affected Systems and Products

- **Microsoft SQL Server (all supported builds pre-July 2025)**  
  Platform: Windows Server on-premises and Azure SQL MI

- **TBK DVR Models (generic TBK/NVR series commonly used in CCTV deployments)**  
  Platform: Embedded Linux, web admin over HTTP/RTSP

- **Four-Faith F-Series Industrial Routers (4G/5G, NB-IoT variants)**  
  Platform: Embedded Linux, web & Telnet administration

- **Ethcode VS Code Extension (≤ compromised commit 2.3.1)**  
  Platform: Cross-platform Visual Studio Code environments

- **Android Smartphones running versions 10–14**  
  Platform: All OEMs susceptible to TapTrap overlay abuse

- **Fortinet, Ivanti, Apache Struts, and MOVEit Transfer products**  
  Platform: Multi-vendor VPN, MDM, Java web-framework, and file-transfer appliances listed in CISA KEV

## Attack Vectors and Techniques

- **SQL Network Payload RCE**  
  Vector: Crafted TDS packets or SQL queries sent over port 1433 to unpatched SQL Server.

- **Unauthenticated Web Admin Injection**  
  Vector: HTTP GET/POST requests to `/device.rsp` and similar endpoints on TBK DVRs.

- **Industrial Router Web RCE**  
  Vector: Malformed configuration parameters in the `/goform/` CGI interface on Four-Faith routers.

- **Malicious Pull Request & Extension Auto-Update**  
  Vector: Compromised GitHub PR merged into Ethcode repo; VS Code auto-updates fetch malicious package.

- **TapJacking via Invisible Overlays**  
  Vector: Transparent `View` layered over legitimate UI synchronised with animation frames.

- **Exposed VPN & MDM Endpoints**  
  Vector: Internet-facing SSL-VPN, MDM, and file-transfer portals targeted with publicly available PoC exploits (per CISA KEV).

## Threat Actor Activities

- **RondoDox Botnet Operators**  
  Campaign: Mass-scanning Shodan/Censys for TBK DVRs and Four-Faith routers; building a DDoS army leveraged against gaming and streaming providers.

- **Unknown Supply-Chain Threat Group (Ethcode)**  
  Campaign: Precision targeting of blockchain developers by poisoning a niche VS Code extension to harvest private keys and smart-contract source.

- **Mobile Threat Actor(s) Using TapTrap**  
  Campaign: Distribution of repackaged finance and productivity apps on third-party stores; aims to steal MFA tokens and banking credentials.

- **Unattributed Actors Leveraging SQL Server Zero-Day**  
  Campaign: Limited, opportunistic intrusions into on-prem enterprise databases to gain a foothold for ransomware deployment.

- **Multiple APT & Cybercrime Groups (per CISA KEV)**  
  Campaign: Routine weaponisation of newly listed KEV flaws to access federal civilian executive-branch (FCEB) networks and commercial entities ahead of patch deadlines.

---

Stay vigilant: prioritise patching devices listed above, monitor for suspicious SQL Server traffic, audit VS Code extensions, restrict Android sideloading, and enforce strict perimeter controls on VPN/MDM appliances.