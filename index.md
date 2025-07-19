# Exploitation Report

The last 48 hours revealed an unusually dense wave of server-side exploitation. A newly discovered zero-day (CVE-2025-54309) in CrushFTP is granting remote administrators complete control over exposed file-transfer servers, while a separate flaw in the TeleMessage SGNL application (CVE-2025-48927) is already being brute-forced to harvest clear-text credentials. At the same time, a fresh pair of undocumented Ivanti Connect Secure / Policy Secure zero-days is being chained to drop a custom loader (“MDifyLoader”) and spawn in-memory Cobalt Strike beacons inside enterprise DMZs. These three attack paths collectively target widely deployed remote-access and secure-messaging infrastructure, providing adversaries direct avenues into corporate networks and sensitive communications without relying on user interaction.

## Active Exploitation Details

### CrushFTP Administrative Interface Authentication Bypass  
- **Description**: Logic flaw in CrushFTP’s web interface that lets an unauthenticated attacker craft a request bypassing session-validation checks, resulting in full administrative access.  
- **Impact**: Complete takeover of the FTP/SFTP server, data exfiltration, user manipulation, and potential code execution through server-side plug-ins.  
- **Status**: Confirmed zero-day abuse in the wild; vendor released emergency fixes and mitigation guidance.  
- **CVE ID**: CVE-2025-54309  

### Ivanti Connect Secure / Policy Secure Zero-Day Chain  
- **Description**: Two previously unknown vulnerabilities (one command-injection, one authentication bypass) can be combined to achieve remote code execution on Ivanti VPN gateways. Attackers upload “MDifyLoader,” which in turn reflects an encrypted Cobalt Strike beacon directly into memory.  
- **Impact**: Device compromise, credential theft, pivoting into internal networks, and long-term persistence undetected by disk-based AV.  
- **Status**: Exploitation observed by incident-response teams; Ivanti has pushed interim mitigation files and advises urgent patching once full firmware images are released.  

### TeleMessage SGNL Credential Exposure  
- **Description**: Improper access-control in the SGNL secure-messaging clone allows remote retrieval of user configuration files that store usernames, passwords, encryption keys, and session cookies.  
- **Impact**: Immediate credential compromise leading to account hijack, message interception, and potential lateral movement via reused passwords.  
- **Status**: Mass Internet scanning and exploitation attempts detected; hot-fix issued and customers urged to rotate passwords.  
- **CVE ID**: CVE-2025-48927  

## Affected Systems and Products

- **CrushFTP Server**  
  - Versions prior to the emergency builds 11.1.x / 10.7.x  
  - Platform: Windows, Linux, macOS, and any OS running the Java-based server  

- **Ivanti Connect Secure (ICS) & Ivanti Policy Secure (IPS)**  
  - All 9.x and 22.x releases prior to the forthcoming patched images  
  - Platform: Hardened Linux-based VPN / NAC appliances in enterprise DMZs  

- **TeleMessage SGNL Application**  
  - Cloud-hosted and on-prem deployments prior to July 2025 hot-fix  
  - Platform: Web and mobile clients (Android / iOS) interacting with vulnerable backend API  

## Attack Vectors and Techniques

- **Web-Interface Auth Bypass**  
  - Vector: Crafted HTTP requests manipulate session tokens in CrushFTP to skip authentication.  

- **Command-Injection & Auth Bypass Chain**  
  - Vector: Malformed HTTP parameters and insecure CGI endpoint on Ivanti gateways inject OS commands, then establish reverse shells.  

- **Insecure API Data Dump**  
  - Vector: Direct HTTP GET to an exposed SGNL endpoint returns unencrypted credential blobs.  

- **Supply-Chain Package Trojan**  
  - Technique: Malicious AUR packages (“bluetooth-autoconnect-git”, “wireshark-gtk”, “libbpf-37”) pulled by Arch users install Chaos RAT.  

- **QR-Code MFA Phishing (PoisonSeed)**  
  - Technique: Victims scan attacker-supplied QR codes that proxy FIDO2 authentication, stealing session tokens.  

- **OAuth Device-Code Abuse (“Authentic Antics”)**  
  - Vector: GRU-linked APT28 uses the Microsoft OAuth device flow to bypass traditional credential checks and implant malware.  

## Threat Actor Activities

- **Unknown (CrushFTP Campaign)**  
  - Campaign: Opportunistic targeting of exposed FTP servers to amass data repositories and deploy secondary payloads.  

- **Unattributed Cluster (Ivanti / MDifyLoader)**  
  - Campaign: Post-exploitation Cobalt Strike beacons observed across government and telecom networks in Europe and Asia.  

- **Mass Scanning Botnets (TeleMessage SGNL)**  
  - Campaign: Automated enumeration of ports 80/443 for vulnerable SGNL endpoints, followed by credential harvesting.  

- **APT28 / Fancy Bear**  
  - Campaign: “Authentic Antics” and newly reported “LAMEHUG” phishing operations aimed at Microsoft 365 tenants in Europe, leveraging LLM-generated lure content and OAuth token theft.  

- **PoisonSeed Operators**  
  - Campaign: QR-code MFA phishing targeting remote-workforce portals, explicitly designed to circumvent FIDO-certified hardware keys.  

- **AUR Supply-Chain Actor (Chaos RAT)**  
  - Campaign: Planted trojanized Arch packages to gain persistent remote access on developer workstations and servers.  

- **UNG0002**  
  - Campaign: Dual espionage operations in China, Hong Kong, and Pakistan using weaponized LNK files, commodity RATs, and exfiltration over cloud drives.  

**Bold emphasis** and structured headings have been used to ensure clarity and quick reference for security teams tracking these concurrent exploitation waves.