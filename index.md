# Exploitation Report

Recent reporting highlights a surge in active exploitation of both traditional software vulnerabilities and emerging AI-centric weaknesses. Threat actors are simultaneously weaponizing critical remote-code-execution flaws in Wing FTP Server and Fortinet FortiWeb, abusing firmware weaknesses in Gigabyte UEFI, and hijacking Google’s Gemini AI with invisible prompt-injection attacks. Ransomware operators such as Interlock are innovating with the new “FileFix” delivery chain, while large-scale exposures (leaked Laravel APP_KEYs, public Git repos, and an eSIM design flaw in Kigen cards) are expanding attackers’ options for initial access. Hardware attacks (GPUHammer on NVIDIA GPUs and the “PerfektBlue” Bluetooth chain) further broaden the threat surface, underscoring the need for immediate patching, secure-by-design configurations, and rigorous supply-chain validation.

## Active Exploitation Details

### Wing FTP Server Critical RCE
- **Description**: A newly disclosed vulnerability allows unauthenticated attackers to execute arbitrary code on Wing FTP Server instances.
- **Impact**: Full system compromise, data exfiltration, lateral movement, and potential ransomware deployment.
- **Status**: Exploitation observed in the wild within 24 hours of public technical disclosure; vendor patch available.

### Google Gemini Prompt-Injection Bug
- **Description**: Abuse of zero-width and right-to-left override characters lets attackers embed invisible prompts in Gemini chat and email summaries.
- **Impact**: Phishing-grade messages masquerade as legitimate Google security alerts, leading users to credential-harvesting or malware sites.
- **Status**: Active exploitation reported; Google is rolling out mitigations but no full fix confirmed.

### Fortinet FortiWeb Pre-Auth SQLi → RCE
- **Description**: A critical SQL-injection flaw in the FortiWeb web application firewall enables pre-authenticated remote code execution.
- **Impact**: Direct takeover of perimeter security appliances, pivoting into protected networks.
- **Status**: Proof-of-concept exploits released publicly; patches available, with mass-scanning activity already detected.

### Gigabyte UEFI Secure-Boot Bypass
- **Description**: Multiple Gigabyte motherboard firmware images improperly authenticate updates, permitting stealth bootkit installation.
- **Impact**: Persistent malware below the OS layer, evading AV/EDR, surviving OS reinstalls.
- **Status**: Exploitation techniques published; Gigabyte has issued updated firmware for dozens of models.

### Kigen eSIM / eUICC Weakness
- **Description**: Flaws in Kigen’s eSIM remote-profile management allow adversaries to manipulate or clone eSIMs over-the-air.
- **Impact**: Device hijack, interception of SMS-based MFA, large-scale IoT disruption.
- **Status**: Research community demonstrated attack; remediation guidance pending from Kigen and carrier partners.

### “PerfektBlue” 1-Click Bluetooth RCE Chain
- **Description**: A multi-stage attack leveraging Bluetooth service oversights in infotainment and embedded stacks found in vehicles and IoT gear.
- **Impact**: Remote code execution after a single Bluetooth pairing request; affects cars (Mercedes, Skoda, VW) and >1 billion embedded devices.
- **Status**: No vendor patches yet; proof-of-concept demonstrated at scale.

### GPUHammer (RowHammer on NVIDIA GDDR6 GPUs)
- **Description**: Adaptation of classic RowHammer bit-flip to high-bandwidth GPU VRAM, degrading AI model integrity or enabling privilege escalation.
- **Impact**: Silent corruption of ML workloads, potential kernel-mode escapes on shared GPU systems.
- **Status**: NVIDIA advises enabling system-level ECC; no firmware fix announced.

### Laravel APP_KEY Leakage → RCE
- **Description**: Exposed APP_KEY secrets on public GitHub repos let attackers forge encryption/signature tokens, leading to arbitrary command execution on over 600 Laravel apps.
- **Impact**: Complete compromise of affected web applications and their underlying servers.
- **Status**: Exploitation confirmed; remediation requires key rotation and codebase scrubbing.

### Exposed Git Repositories
- **Description**: Publicly reachable .git directories and inadvertent pushes leak API keys, credentials, and proprietary code.
- **Impact**: Credential stuffing, supply-chain poisoning, intellectual-property theft.
- **Status**: Ongoing mass exploitation by automated scanners; mitigation involves proper ACLs and secret scanning.

### Interlock RAT “FileFix” Delivery Chain
- **Description**: A revamped PHP-based Interlock RAT is delivered via a “FileFix” web-inject that abuses website update workflows.
- **Impact**: Remote desktop control, data theft, precursor to Interlock ransomware encryption.
- **Status**: Active campaigns across finance, healthcare, and manufacturing; no vendor patch (attack abuses legitimate sites).

### Malicious VSCode Extension in Cursor IDE
- **Description**: Fraudulent extension side-loads infostealers and RATs within the Cursor AI IDE environment.
- **Impact**: Credential theft and direct monetary loss (e.g., $500 k crypto theft case).
- **Status**: Extension pulled, but sideloaded copies remain in circulation.

### WordPress Gravity Forms Supply-Chain Backdoor
- **Description**: Attackers compromised the developer’s website and replaced manual installer archives with backdoored plugin versions.
- **Impact**: PHP shell access to any site that manually downloaded the tampered package.
- **Status**: Discovery led to site takedown and clean installer; infections under investigation.

### McHire “123456” Password Misconfiguration
- **Description**: An administrative chatbot back-end guarded by a trivial password exposed >64 million job application chat logs.
- **Impact**: Leakage of PII, social-engineering fodder, and hiring analytics.
- **Status**: Misconfiguration fixed after disclosure; data already widely scraped.

## Affected Systems and Products

- **Wing FTP Server**: All supported versions prior to emergency patch; Windows, Linux, macOS  
- **Google Gemini / Gemini for Workspace**: Web and mobile clients across ChromeOS, Android, iOS  
- **Fortinet FortiWeb**: Physical and virtual WAF appliances running vulnerable firmware builds  
- **Gigabyte Motherboards**: ~90 consumer and gaming boards with affected UEFI firmware (Intel & AMD platforms)  
- **Kigen eUICC eSIM Cards**: Billions of IoT/industrial devices and modern smartphones using Kigen remote-SIM provisioning  
- **Automotive Infotainment Systems**: Mercedes-Benz, Skoda, Volkswagen models with vulnerable Bluetooth stacks  
- **NVIDIA GPUs**: GDDR6-equipped cards (RTX 30-series, some RTX 20-series) in servers, desktops, and laptops  
- **Laravel-based Web Applications**: Sites with leaked APP_KEY values on GitHub  
- **Public Git Repositories**: Enterprise and open-source projects exposing sensitive directories or secrets  
- **Websites Using “FileFix”**: Compromised legitimate domains hosting weaponized installers or JavaScript  
- **Cursor IDE / VSCode Extensions**: Users who installed the rogue extension from unofficial sources  
- **WordPress Gravity Forms**: Sites that downloaded manual installers between compromise window  
- **McHire Job Chatbot Platform**: U.S.-based instance prior to credential correction  

## Attack Vectors and Techniques

- **Invisible Prompt Injection**: Zero-width & RTL characters embed hidden commands in AI prompts/email summaries.  
- **Pre-Auth SQL Injection**: Crafted HTTP requests exploit FortiWeb input validation to execute OS commands.  
- **Unauthenticated RCE Payload Upload**: Wing FTP flaw lets attackers push DLL/Shell payloads without login.  
- **UEFI Bootkit Implantation**: Malicious firmware image signed/bypassed to execute before OS boot.  
- **Remote eSIM Profile Swap**: OTA SMS or management server abuse to reconfigure Kigen eSIMs.  
- **RowHammer (GPUHammer)**: High-frequency VRAM access flips bits, corrupting adjacent rows.  
- **1-Click Bluetooth Pairing Exploit**: PerfektBlue chain executes once victim accepts a single pairing prompt.  
- **APP_KEY Token Forgery**: Using leaked keys to sign serialized payloads that Laravel unserializes into code execution.  
- **FileFix Web-Inject**: Tampered update packages sideload a PHP-based Interlock RAT.  
- **Supply-Chain Backdooring**: Compromise of developer distribution sites/extensions to ship malware.  
- **Credential Misconfiguration**: Weak admin password (“123456”) exposes sensitive backend APIs.  

## Threat Actor Activities

- **Interlock Ransomware Group**  
  - **Campaign**: Deploying PHP-based Interlock RAT via FileFix; targeting finance, healthcare, manufacturing.  

- **Unknown Actors Exploiting Wing FTP & FortiWeb**  
  - **Campaign**: Mass Internet scanning, automatic exploitation for botnet building and ransomware footholds.  

- **Bootkit Operators**  
  - **Campaign**: Leveraging Gigabyte UEFI flaw to implant stealth rootkits that survive OS reinstallations.  

- **PerfektBlue Research/Threat Group**  
  - **Campaign**: Demonstrated Bluetooth RCE chain across automotive and IoT devices; threat actors likely to weaponize.  

- **Cryptocurrency-Focused Threat Cluster**  
  - **Campaign**: Distributed malicious VSCode extension in Cursor IDE; theft of $500 k in crypto from at least one victim.  

- **Pay2Key Ransomware (Iran-linked)**  
  - **Campaign**: Offering 80% affiliate share for attacks on U.S. and Israeli targets; may incorporate FortiWeb/Wing FTP exploits for ingress.  

- **Scattered Spider (Weekly Recap)**  
  - **Campaign**: Arrest news suggests temporary disruption; prior history of exploiting edge appliances similar to FortiWeb.  

- **Data-Harvesting Actors**  
  - **Campaign**: Continuously mining exposed Git repos, Laravel keys, and McHire chatbot logs for credentials and PII.  

**Bold and immediate patching, configuration hardening, and supply-chain scrutiny are required to mitigate the above exploitation activity.**