# Exploitation Report

Multiple critical vulnerabilities are under active exploitation, with Microsoft SharePoint zero-days (CVE-2025-53770, CVE-2025-53771) leading the charge in widespread compromise campaigns attributed to the “ToolShell” threat actor. At the same time, attackers are hijacking more than 1,000 publicly-exposed CrushFTP servers via CVE-2025-54309, abusing hard-coded credentials in HPE Aruba “Instant On” access points, and weaponizing new techniques to bypass FIDO2 security keys in high-profile phishing waves. Supply-chain abuse continues through npm package hijacking, while thousands of websites are silently monetized through revived browser-based cryptojacking tactics. Organizations should prioritize patching, disable unnecessary exposure of management interfaces, and harden authentication workflows immediately.

## Active Exploitation Details

### Microsoft SharePoint Server Remote Code Execution Zero-Days  
- **Description**: Logic flaw in SharePoint’s web services layer allows unauthenticated attackers to upload arbitrary files and execute them with SharePoint service privileges.  
- **Impact**: Full remote code execution, lateral movement into Microsoft 365 and on-prem hybrid environments, data theft, and installation of webshells (“ToolShell”).  
- **Status**: Actively exploited since 18 July; emergency out-of-band patches released by Microsoft.  
- **CVE ID**: CVE-2025-53770  
- **CVE ID**: CVE-2025-53771  

### CrushFTP Administrative Interface Authentication Bypass  
- **Description**: Flaw in session validation within CrushFTP’s web interface lets remote attackers escalate to administrator privileges over HTTP/S.  
- **Impact**: Hijack of file-transfer servers, data exfiltration, and deployment of ransomware via built-in scripting.  
- **Status**: Active exploitation in the wild; vendor patch available, but >1,000 servers remain unpatched.  
- **CVE ID**: CVE-2025-54309  

### HPE Aruba “Instant On” Access Point Hard-Coded Credentials  
- **Description**: Devices ship with undocumented static username/password that grants full administrative web access.  
- **Impact**: Network takeover, pivoting into corporate LAN/WLAN, rogue firmware uploads, and man-in-the-middle attacks.  
- **Status**: Exploitation observed in the wild; HPE has issued firmware updates and a hardening guide.  

### Google Chrome In-Browser Code Execution Exploit  
- **Description**: Type-confusion flaw in V8 JavaScript engine triggered via crafted webpages, enabling sandbox escape.  
- **Impact**: Remote code execution in user context, subsequent malware installation.  
- **Status**: Exploit seen in watering-hole campaigns; Google has released a stable-channel update.  

### NVIDIA Nsight Compute Toolkit RCE  
- **Description**: Unsafe deserialization in remote profiling component allows attackers to run arbitrary code on developer workstations.  
- **Impact**: Compromise of systems used for AI/ML workloads, credential theft, and supply-chain poisoning of CUDA projects.  
- **Status**: Weaponized proof-of-concept circulating on offensive forums; patches available from NVIDIA.  

## Affected Systems and Products

- **Microsoft SharePoint Server 2019 / Subscription Edition**  
  - **Platform**: Windows Server, on-prem & hybrid deployments  

- **CrushFTP 10.x and early 11.x builds (before vendor hotfix)**  
  - **Platform**: Windows, Linux, macOS, Solaris  

- **HPE Aruba Instant On AP11, AP12, AP15, AP17, AP22 (all firmware prior to July 2025)**  
  - **Platform**: Hardware Wi-Fi access points, SMB networks  

- **Google Chrome < 127.0.6535.78 (Stable channel)**  
  - **Platform**: Windows, macOS, Linux, Android  

- **NVIDIA Nsight Compute CLI Toolkit prior to 2025.3.1**  
  - **Platform**: Developer workstations running Windows & Linux  

## Attack Vectors and Techniques

- **Web Service File Upload Abuse (SharePoint)**  
  - **Vector**: Crafted SOAP/REST requests upload ASPX payloads leading to RCE.  

- **Unauthenticated Web Interface Hijack (CrushFTP)**  
  - **Vector**: Direct HTTP POST to /WebInterface/login.html bypasses token check.  

- **Static Credential Reuse (HPE Aruba)**  
  - **Vector**: Automated scanning for exposed AP web GUIs, login with hard-coded creds.  

- **Type-Confusion Drive-By (Chrome)**  
  - **Vector**: Malicious JavaScript triggers memory corruption when victim visits compromised site.  

- **Cross-Device FIDO2 Downgrade (PoisonSeed)**  
  - **Vector**: QR-code phishing lures victims into approving logins on secondary device, circumventing hardware keys.  

- **Browser-Based Cryptojacking**  
  - **Vector**: Injected obfuscated JavaScript over WebSocket channels mines Monero on visitor machines.  

- **npm Supply-Chain Poisoning**  
  - **Vector**: Stolen maintainer tokens used to push trojanized updates (eslint-config-prettier, eslint-plugin-prettier).  

## Threat Actor Activities

- **ToolShell / UNCxxxx**  
  - **Campaign**: Mass scanning & exploitation of SharePoint CVE-2025-53770/53771; deployment of webshells and lateral movement scripts.  

- **Unknown CrushFTP Cluster**  
  - **Campaign**: Automated takeover of exposed CrushFTP servers to steal corporate archives and plant ransomware loaders.  

- **PoisonSeed**  
  - **Campaign**: Global phishing operation targeting tech and banking staff, leveraging QR phishing to bypass FIDO2 MFA protections.  

- **World Leaks Extortion Group**  
  - **Campaign**: Breach of Dell’s product-demo lab, theft of test data, ongoing ransom demands under new branding.  

- **EncryptHub (aka LARVA-208 / Water Gamayun)**  
  - **Campaign**: Fake AI SaaS portals lure Web3 developers; drops “Fickle Stealer” for crypto-wallet and credential theft.  

- **Cryptojacking Collective (Unattributed)**  
  - **Campaign**: Compromised 3,500 legitimate sites to inject stealth miners, focusing on news & e-commerce domains.  

- **npm Phishing Actors (Unattributed)**  
  - **Campaign**: Targeted phishing of open-source maintainers to hijack popular linter packages as malware droppers.  

---

Organizations should treat all highlighted vulnerabilities as priority-one, apply available patches or mitigations without delay, and monitor for the described adversary TTPs across endpoint, network, and cloud telemetry.