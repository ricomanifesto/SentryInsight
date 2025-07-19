# Exploitation Report

Over the past week, defenders observed a sharp uptick in hands-on-keyboard intrusions that pivot on newly discovered or recently patched flaws in widely deployed enterprise software. The most critical activity centers on a zero-day in CrushFTP (CVE-2025-54309) that grants full administrative control over vulnerable servers and is already being mass-exploited. Simultaneously, multiple zero-days in Ivanti Connect Secure are being chained to deliver the new “MDifyLoader” malware and in-memory Cobalt Strike beacons. Supply-chain compromises, novel phishing methods that bypass FIDO-based MFA, and state-sponsored credential-theft campaigns against Microsoft 365 tenants round out an increasingly diverse exploitation landscape.

## Active Exploitation Details

### CrushFTP Web Interface Admin Access Zero-Day
- **Description**: An authentication-bypass flaw in the CrushFTP web interface lets remote attackers escalate to full administrative access.  
- **Impact**: Complete takeover of file-transfer servers, data exfiltration, creation of rogue users, and pivoting deeper into corporate networks.  
- **Status**: Actively exploited in the wild; vendor has issued emergency patches and mitigation guidance.  
- **CVE ID**: CVE-2025-54309  

### Ivanti Connect Secure / Policy Secure Zero-Days
- **Description**: Unpatched security flaws in Ivanti’s VPN and NAC appliances are being chained to execute arbitrary commands and drop the MDifyLoader backdoor, which subsequently launches in-memory Cobalt Strike payloads.  
- **Impact**: Unauthenticated remote code execution, persistent access to corporate networks, lateral movement, and post-exploitation tooling deployment.  
- **Status**: Confirmed active exploitation; Ivanti has released patches and recommends immediate upgrade or interim mitigations.  

### “Authentic Antics” Microsoft 365 Credential-Stealing Malware
- **Description**: Spear-phishing campaign attributed to APT28 (Fancy Bear) that deploys custom malware to harvest Microsoft 365 tokens and credentials.  
- **Impact**: Account takeover, email exfiltration, long-term espionage inside cloud tenants.  
- **Status**: Ongoing; Microsoft and UK NCSC have released detection guidance.  

### PoisonSeed MFA-Bypass Phishing Technique
- **Description**: Attackers present victims with a rogue QR code during login that harvests session cookies, sidestepping FIDO-based hardware tokens.  
- **Impact**: Compromise of accounts protected by strong MFA, enabling subsequent privilege escalation.  
- **Status**: Actively leveraged in targeted phishing waves; no vendor patch required—mitigation focuses on user training and advanced session-anomaly detection.  

### Arch Linux AUR Supply-Chain Malicious Packages
- **Description**: Three trojanized AUR packages silently fetched and executed the CHAOS remote-access trojan on install.  
- **Impact**: Backdoor access to Linux workstations and servers, data theft, and potential lateral movement.  
- **Status**: Malicious packages removed; users must audit systems for CHAOS RAT artifacts and reinstall clean builds.  

### MCP Server Default-Authentication Exposure
- **Description**: MCP servers—the backbone for agentic AI workflows—allow optional authentication; roughly 2,000 instances expose full administrative APIs to the Internet with no credentials.  
- **Impact**: Total server control, manipulation of AI agents, data poisoning, and code execution.  
- **Status**: Wide-open exposures remain online; administrators urged to enable authentication immediately.  

### UNG0002 LNK-File Twin Campaigns
- **Description**: An espionage cluster uses weaponized Windows LNK shortcuts to drop RAT implants in China, Hong Kong, and Pakistan.  
- **Impact**: Remote access, surveillance, and data exfiltration across government and telecom sectors.  
- **Status**: Active; defenders advised to block LNK execution and monitor endpoint telemetry.  

## Affected Systems and Products

- **CrushFTP Server**: All supported versions prior to vendor hotfix; cross-platform (Windows, Linux, macOS).  
- **Ivanti Connect Secure / Policy Secure Gateways**: Multiple firmware versions in production deployments; appliance-based VPN/NAC.  
- **Microsoft 365 Tenants**: Cloud email and collaboration services across Windows, macOS, and mobile platforms.  
- **Enterprise Identity Platforms**: Any environment relying on FIDO hardware keys for MFA (PoisonSeed vector).  
- **Arch Linux Systems**: Hosts that installed the pulled AUR packages on x86-64 and ARM architectures.  
- **MCP Servers**: Public instances of the Modular Co-Processor framework (agentic AI infrastructure) on Linux.  
- **Windows Endpoints in East Asia & Pakistan**: Targets receiving UNG0002 weaponized LNK files.  

## Attack Vectors and Techniques

- **Web-Interface Authentication Bypass**  
  - **Vector**: Direct HTTP/S calls to vulnerable CrushFTP endpoints to obtain admin tokens.  

- **VPN Appliance Command Injection**  
  - **Vector**: Crafted requests to Ivanti CGI endpoints leading to shell execution and payload download.  

- **QR-Code Phishing (MFA Bypass)**  
  - **Vector**: Malicious QR code supplied during login workflow, capturing session cookies via attacker-controlled relay server.  

- **Supply-Chain Package Poisoning**  
  - **Vector**: Upload of trojanized packages to Arch Linux AUR; malware executes during package install scripts.  

- **Token & Cookie Theft Malware**  
  - **Vector**: Authentic Antics implants siphon Microsoft 365 OAuth tokens via API calls and browser-session scraping.  

- **Unauthenticated API Exposure**  
  - **Vector**: Direct REST requests to MCP management endpoints with no authentication checks.  

- **LNK Shortcut Droppers**  
  - **Vector**: Social-engineering emails deliver .lnk files that launch PowerShell to fetch RAT binaries.  

## Threat Actor Activities

- **Unknown (CrushFTP Zero-Day Exploitation)**  
  - Broad, opportunistic scanning and takeover of publicly exposed FTP servers for data theft and foothold creation.  

- **Unnamed Operators of MDifyLoader**  
  - Campaign leverages Ivanti zero-days, focuses on dropping in-memory Cobalt Strike for post-exploitation.  

- **APT28 / Fancy Bear**  
  - “Authentic Antics” campaign targeting government and defense sectors to compromise Microsoft 365 environments.  

- **PoisonSeed**  
  - Conducts highly targeted phishing against enterprises that mandate hardware-token MFA, aiming at executive accounts.  

- **Supply-Chain Actor (Chaos RAT)**  
  - Embedded malware in Arch Linux AUR to amass a foothold in developer and DevOps environments.  

- **UNG0002 (Unknown Group 0002)**  
  - Twin espionage operations in China, Hong Kong, and Pakistan using LNK droppers and multiple RAT families.  

- **Opportunistic Hackers Exploiting MCP**  
  - Mass scanning of exposed MCP servers to hijack AI workloads and harvest sensitive data.