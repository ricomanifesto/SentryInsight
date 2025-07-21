# Exploitation Report

During the past week, defenders observed a surge of high-impact exploits targeting enterprise collaboration platforms, managed file-transfer solutions, and network infrastructure. The most critical activity centers on two Microsoft SharePoint remote-code-execution (RCE) zero-days now weaponized by the “ToolShell” threat actor, a critical CrushFTP authentication-bypass flaw leveraged to hijack more than 1,000 servers, and hard-coded credentials in HPE Aruba Instant On access points that are already being abused for unauthorized administrative access. Additional in-the-wild exploits include an unpatched Google Chrome renderer flaw, an NVIDIA developer-toolkit RCE, and sophisticated phishing tactics that degrade FIDO2 protections. Concerted attacks by groups such as ToolShell, PoisonSeed, EncryptHub, and World Leaks emphasize the need for immediate patching, configuration hardening, and vigilant monitoring.

---

## Active Exploitation Details

### Microsoft SharePoint Server RCE Zero-Days
- **Description**: Two independent vulnerabilities allow unauthenticated attackers to craft malicious API/SOAP requests that trigger remote code execution on SharePoint servers.
- **Impact**: Full takeover of SharePoint sites, lateral movement, data exfiltration, and deployment of web shells.
- **Status**: Actively exploited since 18 July; emergency patches released, but many environments remain unpatched.
- **CVE ID**: CVE-2025-53770  
- **CVE ID**: CVE-2025-53771  

### CrushFTP Authentication Bypass / Admin Hijack
- **Description**: Logic flaw enables path traversal and session fixation, letting remote attackers create or hijack administrative sessions on CrushFTP’s web interface.
- **Impact**: Complete administrative control of the file-transfer server, file theft, configuration tampering, and deployment of ransomware payloads.
- **Status**: Exploitation observed against >1,000 Internet-facing servers; vendor hotfixes available.
- **CVE ID**: CVE-2025-54309  

### HPE Aruba Instant On Access Point Hard-Coded Credentials
- **Description**: Devices ship with embedded, undocumented username/password pairs that bypass normal authentication on the web management portal.
- **Impact**: Remote attackers gain root-level administrative access, allowing network pivoting, traffic snooping, and firmware manipulation.
- **Status**: Exploits reported in the wild; HPE has issued firmware updates and mitigation guidance.

### Google Chrome In-the-Wild Zero-Day Exploit
- **Description**: Memory-safety issue in the Blink/Skia rendering pipeline permits arbitrary code execution when victims visit a booby-trapped website.
- **Impact**: Sandbox escape leading to full browser and potential OS compromise.
- **Status**: Google pushed an emergency stable-channel update; exploitation detected before patch release.

### NVIDIA Toolkit Remote Code Execution
- **Description**: Insecure library loading in NVIDIA’s developer toolkit (used for CUDA and AI workflows) allows execution of attacker-controlled DLLs on launch.
- **Impact**: Local privilege escalation or remote RCE when toolkits are launched from network shares, enabling supply-chain style attacks in DevOps pipelines.
- **Status**: Exploit PoCs circulating; vendor update available.

### FIDO2 / WebAuthn Downgrade Abuse (PoisonSeed)
- **Description**: Social-engineering technique that forces cross-device sign-ins, tricking users into approving push requests on their phone that actually authenticate attackers on separate desktops.
- **Impact**: Successful bypass of hardware-based FIDO2 MFA, leading to account takeover even when security keys are deployed.
- **Status**: Active phishing campaign; no vendor patch (protocol abuse), mitigations rely on user training and stricter sign-in policies.

---

## Affected Systems and Products

- **Microsoft SharePoint Server 2016, 2019, Subscription Edition**  
  - **Platform**: Windows Server installations in on-prem and hybrid environments  

- **CrushFTP versions 10.x and 11.x prior to vendor hotfix**  
  - **Platform**: Windows, Linux, macOS, and other Java-capable OSes  

- **HPE Aruba Instant On AP11/12/15/17 and related firmware lines**  
  - **Platform**: Wireless access points in SMB and branch office deployments  

- **Google Chrome < 118.0.5993.70 (Stable Channel)**  
  - **Platform**: Windows, macOS, Linux desktop browsers  

- **NVIDIA CUDA/Developer Toolkit 12.x (pre-patch)**  
  - **Platform**: Windows and Linux development workstations and CI/CD servers  

- **Any FIDO2-enabled web application using WebAuthn cross-device sign-in**  
  - **Platform**: Cloud services, identity providers, and SaaS portals  

---

## Attack Vectors and Techniques

- **Malicious SharePoint API Calls**  
  - **Vector**: Crafted SOAP/API requests bypass input validation to execute commands under SharePoint service account.  

- **Session Fixation & Path Traversal (CrushFTP)**  
  - **Vector**: Attacker uploads crafted `.desktop` files or manipulates URL paths to hijack admin sessions.  

- **Hard-Coded Credential Abuse (Aruba Instant On)**  
  - **Vector**: Remote HTTP(S) login with embedded default credentials “admin/<hidden>” for full control.  

- **Drive-By Browser Exploit (Chrome)**  
  - **Vector**: Malicious JavaScript & WebAssembly trigger UAF memory corruption, followed by sandbox escape.  

- **DLL Search-Order Hijacking (NVIDIA Toolkit)**  
  - **Vector**: Planting rogue DLLs in writable directories referenced by toolkit binaries.  

- **QR Phishing / Cross-Device WebAuthn Downgrade (PoisonSeed)**  
  - **Vector**: Victim scans QR code, unknowingly approves authentication request for attacker’s session.  

---

## Threat Actor Activities

- **ToolShell**  
  - **Campaign**: Mass exploitation of SharePoint RCE zero-days to deploy web shells and exfiltrate corporate data from at least 85 organizations worldwide.  

- **PoisonSeed**  
  - **Campaign**: Ongoing phishing waves targeting enterprise email users; focuses on defeating FIDO2 MFA by abusing cross-device sign-in flows.  

- **EncryptHub (aka LARVA-208 / Water Gamayun)**  
  - **Campaign**: Fake AI-platform lures distributed to Web3 developers, dropping “Fickle Stealer” malware for credential and wallet theft.  

- **World Leaks Extortion Group**  
  - **Campaign**: Breached Dell’s product-demo lab, weaponizing stolen credentials; leveraging data for double-extortion.  

- **Unknown Actors (CrushFTP)**  
  - **Campaign**: Automated scanning of Internet-exposed CrushFTP instances, immediate admin hijack and deployment of ransomware loaders.  

---

**End of Report**