# Exploitation Report

The past week has seen a sharp rise in real-world exploitation targeting both traditional software stacks and emerging technologies. Attackers are weaponising newly disclosed remote-code-execution flaws in Wing FTP Server and Fortinet FortiWeb, abusing supply-chain weaknesses to backdoor widely-used developer tools, and taking advantage of design flaws in AI assistants, Bluetooth implementations, UEFI firmware, and eSIM chipsets. Ransomware operators—most notably the Interlock and Pay2Key groups—are actively integrating these techniques into multi-stage campaigns that provide deep, persistent access and monetisation opportunities.

## Active Exploitation Details

### Wing FTP Server Remote-Code-Execution Vulnerability  
- **Description**: A critical bug in the Wing FTP Server web interface lets unauthenticated attackers execute arbitrary commands on the underlying host.  
- **Impact**: Full system compromise, lateral movement, ransomware deployment, or data theft.  
- **Status**: Public exploit code available; in-the-wild exploitation observed within 24 hours of disclosure.  
- **CVE ID**: —  

### Fortinet FortiWeb Pre-Auth SQLi to RCE  
- **Description**: A SQL-injection flaw in the FortiWeb management interface allows an unauthenticated attacker to run arbitrary database commands that lead to remote code execution.  
- **Impact**: Takeover of FortiWeb appliances, pivoting into protected network segments, WAF rule tampering.  
- **Status**: Patched by vendor; proof-of-concept exploits released and scanning activity rising.  
- **CVE ID**: CVE-2025-25257  

### Gigabyte UEFI Secure-Boot Bypass  
- **Description**: Multiple Gigabyte motherboard models ship with UEFI firmware that can be modified at boot time, enabling the installation of stealth bootkits invisible to the operating system.  
- **Impact**: Persistent malware that survives OS re-installation, credential theft, long-term espionage.  
- **Status**: Exploitation detailed by researchers; firmware fixes in progress, no universal patch yet.  

### “PerfektBlue” One-Click Bluetooth RCE Chain  
- **Description**: A chained vulnerability in Bluetooth stacks used by automotive infotainment units and various IoT/industrial devices enables remote code execution after a single malicious packet.  
- **Impact**: Remote takeover of 350 million vehicles and more than 1 billion devices, possibility of physical safety risks.  
- **Status**: Attack demonstrated; vendors coordinating patches, no comprehensive fix released.  

### Google Gemini Invisible Prompt-Injection Bug  
- **Description**: Gemini’s rendering layer fails to sanitise zero-width characters, allowing attackers to hide malicious prompts that masquerade as legitimate Google Security alerts.  
- **Impact**: Phishing, credential harvesting, unauthorised actions executed by users who believe the prompt is trustworthy.  
- **Status**: Actively abused in the wild; Google engineering team working on mitigation.  

### Google Gemini Email-Summary Hijack  
- **Description**: Attackers manipulate Gemini for Workspace summaries to embed links or instructions that redirect users to phishing sites—no attachment required.  
- **Impact**: Email-based social engineering leading to account takeover or malware delivery.  
- **Status**: Exploitation observed; mitigation guidance released to workspace admins.  

### Interlock RAT “FileFix” / Web-Inject Delivery Exploit  
- **Description**: Interlock ransomware operators compromise legitimate sites, injecting a PHP-based loader dubbed FileFix that drops a new Interlock RAT variant on visitors.  
- **Impact**: Backdoor access, staging for ransomware encryption, data exfiltration across multiple industries.  
- **Status**: Campaign active; no vendor patch applicable—requires web-server hardening and takedowns.  

### Kigen eSIM / eUICC Privilege-Escalation Vulnerability  
- **Description**: Logical flaws in Kigen eUICC cards allow rogue profiles to be provisioned, enabling SIM cloning and network impersonation.  
- **Impact**: Hijacking of cellular connectivity, interception of SMS-based MFA, large-scale IoT fleet manipulation.  
- **Status**: Exploit technique published; patches being distributed via carrier profile updates.  

### GPUHammer – RowHammer Variant on NVIDIA GDDR6 GPUs  
- **Description**: Researchers adapted classic RowHammer to GPU GDDR6 memory, corrupting adjacent rows and degrading AI model integrity.  
- **Impact**: Model poisoning, denial-of-service in GPU-accelerated workloads, potential privilege escalation.  
- **Status**: Proof-of-concept released; NVIDIA advises enabling ECC and driver mitigations.  

### Laravel APP_KEY Remote Code Execution  
- **Description**: Hundreds of Laravel projects leaked their APP_KEY secrets on GitHub, enabling attackers to unserialise malicious payloads and achieve RCE.  
- **Impact**: Complete takeover of exposed web applications, credential theft, lateral movement into cloud environments.  
- **Status**: Active mass-exploitation; admins urged to rotate keys and audit Git history.  

### OpenVSX Extension Repository Zero-Day  
- **Description**: A privilege-escalation flaw in the OpenVSX marketplace allowed attackers to overwrite legitimate VSCode extensions, distributing malicious updates to Cursor and Windsurf IDE users.  
- **Impact**: Supply-chain compromise of millions of developer workstations.  
- **Status**: Patched; incident response indicates attempted exploitation prior to fix.  

### Malicious VSCode Extension in Cursor IDE  
- **Description**: A fake extension sideloaded RATs and infostealers, leading to losses of $500 K in cryptocurrency in one confirmed case.  
- **Impact**: Credential and wallet theft, remote access, codebase exfiltration.  
- **Status**: Active; extension removed from marketplace, but sideload installers still circulating.  

### WordPress Gravity Forms Supply-Chain Backdoor  
- **Description**: The developer’s website was breached and manual installer packages of Gravity Forms were trojanised with a PHP backdoor.  
- **Impact**: Remote code execution on WordPress sites, data theft, SEO spam.  
- **Status**: Malicious packages discovered; clean installers re-issued, users urged to verify hashes.  

## Affected Systems and Products

- **Wing FTP Server**: All supported OS versions; vulnerable builds prior to latest hot-fix  
- **Fortinet FortiWeb**: Physical and virtual appliances before FortiWeb 7.4.1 / 7.0.8  
- **Gigabyte Motherboards (UEFI)**: Dozens of Intel & AMD models across Z-, B- and X-series chipsets  
- **Automotive Infotainment Units**: Mercedes, Škoda, Volkswagen models using affected Bluetooth stacks  
- **Google Gemini (Workspace & Mobile)**: All instances prior to server-side patch  
- **Web Servers Hosting FileFix Scripts**: Sites compromised by Interlock operators  
- **Kigen eUICC Cards**: Billions of IoT/smartphone devices using vulnerable firmware versions  
- **NVIDIA GPUs**: GDDR6-equipped cards (RTX 30/40 series, select professional lines)  
- **Laravel Applications**: Projects with APP_KEY values leaked publicly on GitHub  
- **OpenVSX Marketplace**: Cursor, Windsurf, and other IDEs sourcing extensions pre-patch  
- **VSCode/Cursor IDE Users**: Systems where the rogue extension was installed  
- **WordPress Sites**: Deployments that installed Gravity Forms manually between breach window  

## Attack Vectors and Techniques

- **Unauthenticated Web Interface Exploit**  
  - **Vector**: Direct HTTP(S) requests exploiting input validation flaws (Wing FTP, FortiWeb).  

- **Boot-Time Firmware Injection**  
  - **Vector**: Malicious UEFI image update flashing on Gigabyte motherboards.  

- **One-Click Bluetooth RCE (“PerfektBlue”)**  
  - **Vector**: Malformed Bluetooth Low Energy packet triggers heap corruption.  

- **Prompt Injection**  
  - **Vector**: Zero-width characters embedded in Gemini prompts and email summaries.  

- **Weaponised PHP Loader (FileFix)**  
  - **Vector**: Compromised legitimate websites inject auto-executing PHP payloads.  

- **eSIM Profile Hijacking**  
  - **Vector**: Over-the-air provisioning abuse of Kigen eUICC management commands.  

- **RowHammer on GDDR6 (“GPUHammer”)**  
  - **Vector**: High-frequency memory row accesses to flip adjacent bits on GPUs.  

- **GitHub Secret Leakage**  
  - **Vector**: Public commits containing Laravel APP_KEYs enabling serializer attacks.  

- **Supply-Chain Extension Takeover**  
  - **Vector**: OpenVSX privilege abuse to publish malicious versions of popular extensions.  

- **Trojanised Installer Packages**  
  - **Vector**: Compromised vendor site served backdoored Gravity Forms zip files.  

## Threat Actor Activities

- **Interlock Ransomware Group**  
  - **Campaign**: Web-inject & FileFix distribution of new PHP-based Interlock RAT targeting healthcare, manufacturing, and finance sectors.  

- **Pay2Key Ransomware (Iran-linked)**  
  - **Campaign**: Relaunched RaaS platform with 80 % affiliate payout to incentivise attacks on U.S. and Israeli organisations.  

- **Unknown Wing FTP Exploitation Cluster**  
  - **Campaign**: Mass internet scanning, rapid weaponisation of public exploit to establish footholds for future ransomware.  

- **Adversaries Leveraging Gemini Bugs**  
  - **Campaign**: Phishing operations impersonating Google Security to harvest credentials and MFA tokens.  

- **Cursor IDE Extension Threat Actor (“CLIPPERNOVA” tentative)**  
  - **Campaign**: Supply-chain intrusion leading to cryptocurrency wallet thefts from developer endpoints.  

- **Supply-Chain Actor Behind Gravity Forms Backdoor**  
  - **Campaign**: Attempted widescale compromise of WordPress sites for SEO spam and skimmer deployment.  

- **Researchers Demonstrating GPUHammer & PerfektBlue**  
  - **Campaign**: Security-community proof-of-concepts highlighting the need for ECC and Bluetooth stack hardening; no confirmed criminal exploitation yet but risk is high.  

---

**Prepared by:** Threat-Hunting & Exploitation Analysis Team  
**Date:** 14 June 2025