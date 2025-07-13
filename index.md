# Exploitation Report

Threat hunters observed a sharp increase in critical remote-code-execution activity this week, with multiple enterprise-grade products being targeted in rapid succession. Live exploitation campaigns are abusing freshly disclosed flaws in Wing FTP Server (CVE-2025-47812), Fortinet FortiWeb (CVE-2025-25257), and Citrix NetScaler ADC/Gateway (CVE-2025-5777). At the same time, attackers demonstrated a new GPU-level RowHammer technique (“GPUHammer”) capable of silently corrupting AI workloads on NVIDIA GDDR6 hardware, while supply-chain compromises and misconfiguration-driven RCE paths (Laravel APP_KEY leaks, backdoored Gravity Forms installers) expand the attack surface. Government agencies and MSSPs are urging immediate patching and hardening as proof-of-concept code and automated scanners are already circulating in the wild.

## Active Exploitation Details

### GPUHammer RowHammer Variant
- **Description**: Hardware fault-induction attack that flips bits in adjacent GDDR6 memory rows on NVIDIA GPUs, degrading model weights and inference accuracy of resident AI workloads.  
- **Impact**: Allows model poisoning, integrity loss, and potential privilege escalation in multi-tenant GPU servers.  
- **Status**: Demonstrated by researchers; NVIDIA urges enabling system-level ECC. Patches are not applicable; relies on hardware mitigation.  

### Wing FTP Server Remote Code Execution
- **Description**: Heap-based overflow in the HTTP/FTP engine enabling unauthenticated attackers to execute arbitrary OS commands on the underlying server.  
- **Impact**: Full system compromise, lateral movement, and data exfiltration of hosted file shares.  
- **Status**: Actively exploited since technical details were published; vendor released fixed builds (7.4.1 and later).  
- **CVE ID**: CVE-2025-47812  

### Fortinet FortiWeb Pre-Auth SQLi ➜ RCE
- **Description**: Critical SQL-injection flaw in the web management interface allowing injection of arbitrary SQL followed by command execution via database functions.  
- **Impact**: Unauthenticated remote takeover of FortiWeb appliances, enabling network pivoting and WAF rule tampering.  
- **Status**: Proof-of-concept exploits publicly released; in-the-wild exploitation observed. Hotfixes available for supported branches 7.0.x–7.4.x.  
- **CVE ID**: CVE-2025-25257  

### Citrix Bleed 2 (NetScaler ADC/Gateway)
- **Description**: Memory-handling flaw in the AAA authentication component that leaks session tokens and permits remote code execution on management plane.  
- **Impact**: Credential/session theft, post-auth RCE, and potential VPN gateway hijack impacting enterprise networks.  
- **Status**: Confirmed active exploitation; CISA added to KEV catalog and mandated 24-hour patch deadline for U.S. federal networks. Fixed builds released.  
- **CVE ID**: CVE-2025-5777  

### Laravel APP_KEY Exposure
- **Description**: Publicly committed APP_KEY secrets on GitHub allow attackers to craft malicious encrypted payloads that the Laravel framework deserializes into executable PHP.  
- **Impact**: Remote code execution on over 600 exposed applications, leading to data theft and web-server compromise.  
- **Status**: Keys are already being harvested; administrators must rotate APP_KEY and audit code for unsafe unserialize patterns.  

### Gravity Forms Supply-Chain Backdoor
- **Description**: Official manual installer packages of the Gravity Forms WordPress plugin were replaced with PHP backdoors after the developer environment was breached.  
- **Impact**: Remote shell access to any site that installed the tampered plugin, enabling website defacement and credential theft.  
- **Status**: Malicious files removed, but installations performed during the compromise window remain vulnerable; admins advised to reinstall clean builds.  

## Affected Systems and Products

- **NVIDIA GPUs with GDDR6 memory (RTX 20/30/40 series, A-series data-center cards)**  
  - **Platform**: Windows, Linux, and cloud GPU instances  

- **Wing FTP Server 7.4.0 and earlier**  
  - **Platform**: Windows, Linux, macOS, FreeBSD  

- **Fortinet FortiWeb 7.4.x, 7.3.x, 7.0.x**  
  - **Platform**: Hardware, VM, and cloud images  

- **Citrix NetScaler ADC & Gateway 14.1 / 13.1 / 13.0**  
  - **Platform**: Appliance, virtual appliance, AWS/Azure images  

- **Laravel-based web applications with leaked APP_KEY**  
  - **Platform**: PHP on Linux/Windows, containerized and serverless deployments  

- **WordPress sites running Gravity Forms manual installer packages downloaded between 11–14 July 2025**  
  - **Platform**: LAMP/LEMP stacks, managed WordPress hosting  

## Attack Vectors and Techniques

- **RowHammer Bit-Flipping (GPUHammer)**  
  - **Vector**: Rapid, high-frequency memory row activations targeting GDDR6 cells lacking ECC.  

- **Unauthenticated HTTP/S Exploit (Wing FTP)**  
  - **Vector**: Crafted REST requests triggering memory corruption in the file-transfer daemon.  

- **Blind SQL Injection to OS Command Execution (FortiWeb)**  
  - **Vector**: Malicious POST to `/api/v2.0/?page=` parameter inserting stacked queries and `xp_cmdshell` equivalents.  

- **Session Token Leakage (Citrix Bleed 2)**  
  - **Vector**: Repeated TLS requests causing buffer over-read and disclosure of valid authentication cookies.  

- **Cryptographically Signed Payload Forgery (Laravel)**  
  - **Vector**: Use of stolen APP_KEY to generate serialized PHP objects that the framework decrypts and instantiates.  

- **Supply-Chain Package Poisoning (Gravity Forms)**  
  - **Vector**: Replacement of legitimate ZIP archives with backdoored versions on the vendor’s download portal.  

## Threat Actor Activities

- **Unknown Mass-Scanner Groups**  
  - **Campaign**: Automated enumeration and exploitation of Wing FTP servers globally within 24 hours of PoC release.  

- **Financially Motivated Intruders**  
  - **Campaign**: Leveraging CVE-2025-25257 to compromise FortiWeb appliances protecting e-commerce sites, injecting malicious rewrite rules for skimming.  

- **Suspected State-Aligned Operators & Ransomware Crews**  
  - **Campaign**: Using Citrix Bleed 2 to breach VPN gateways, followed by domain-wide ransomware deployment; CISA attributes some activity to previously seen APTs.  

- **Supply-Chain Actor (unidentified)**  
  - **Campaign**: Breach of Gravity Forms build system to implant PHP web shells, mirroring tactics from the “WP-Toolkit” incident.  

- **Scattered Spider (arrests reported)**  
  - **Activities**: Prior large-scale SIM-swapping, social engineering, and ransomware operations; four members apprehended in the UK, potentially disrupting future campaigns that exploit edge-device vulnerabilities such as Citrix Bleed 2.  

- **Pay2Key RaaS Operators**  
  - **Activities**: Relaunching affiliate program with 80 % revenue share; tooling observed incorporating exploits for recently disclosed network-edge vulnerabilities.  

Organizations should prioritize patching the cited CVEs, audit Laravel secret management, verify plugin integrity, and deploy ECC protections on GPU workloads to diminish immediate exploitation risk.