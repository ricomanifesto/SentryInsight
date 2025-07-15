# Exploitation Report

During the last week, multiple high-impact vulnerabilities have moved from theoretical risk to active exploitation. Supply-chain attacks dominate, with North Korean actors pushing hundreds of malicious npm packages to seed the new **XORIndex** malware, while a compromised WordPress developer site distributed back-doored Gravity Forms installers. Critical remote-code-execution bugs are under attack in **Wing FTP Server** and **Fortinet FortiWeb**, and researchers have shown practical Secure Boot bypasses on Gigabyte motherboards that open the door to stealthy bootkits. At the same time, novel attack vectors—such as **“PerfektBlue”** one-click Bluetooth RCE, **Google Gemini prompt-injection**, and the **GPUHammer RowHammer variant** on NVIDIA GPUs—highlight the expanding surface area for zero-day abuse. Ransomware operators (Interlock, Pay2Key) are rapidly weaponizing new delivery mechanisms (FileFix, web-injects) to broaden their reach.

## Active Exploitation Details

### Malicious npm Packages – XORIndex Supply-Chain Injection
- **Description**: North Korean “Contagious Interview” operators published 67+ poisoned npm packages that sideload the XORIndex backdoor.  
- **Impact**: Full system compromise of developers who `npm install` the packages; credential theft and lateral movement.  
- **Status**: Ongoing; packages are being removed but new ones continue to appear. No patches—developers must validate dependencies.  

### Google Gemini Prompt-Injection Vulnerability
- **Description**: Flaw in Gemini for Workspace allows invisible HTML/CSS prompts that masquerade as Google Security alerts or email summaries.  
- **Impact**: Phishing redirection, data exfiltration, and potential credential theft without attachments or obvious links.  
- **Status**: Actively exploited in the wild; Google is rolling out mitigations, but no definitive fix released.  

### Wing FTP Server Remote Code Execution
- **Description**: Critical input-validation bug enables unauthenticated attackers to execute arbitrary code on vulnerable Wing FTP Server instances.  
- **Impact**: Full server takeover, file theft, pivoting to internal networks.  
- **Status**: Exploit released; attacks observed 24 hours after public disclosure. Vendor patch available—urgent upgrade required.  

### Fortinet FortiWeb Pre-Auth SQLi → RCE
- **Description**: SQL injection in the authentication stack grants shell access without credentials, leading to remote code execution.  
- **Impact**: Complete compromise of WAF appliances and downstream protected applications.  
- **Status**: Proof-of-concept code public; mass scanning underway. Patches published by Fortinet.  

### Gigabyte UEFI Secure Boot Bypass
- **Description**: Multiple UEFI firmware flaws let attackers plant persistent bootkits that evade the OS and survive reinstalls.  
- **Impact**: Stealthy malware with kernel-level control and long-term persistence.  
- **Status**: Exploitable in the wild; Gigabyte has issued firmware updates for affected boards.  

### “PerfektBlue” One-Click Bluetooth RCE Chain
- **Description**: Logical flaws in Bluetooth stack of automotive and embedded chipsets allow drive-by code execution via a single malicious packet.  
- **Impact**: Remote hijack of vehicle infotainment, industrial controllers, medical devices, and smartphones.  
- **Status**: Proof-of-concept demoed; no universal patch. Vendors evaluating firmware updates.  

### Kigen eSIM / eUICC Profile Manipulation
- **Description**: Weak authentication in Kigen eSIM cards lets attackers swap or modify profiles, hijacking cellular connections.  
- **Impact**: Cloning of mobile identities, interception of SMS 2FA, denial of service for IoT fleets.  
- **Status**: Vulnerability disclosed; active exploitation reported against IoT deployments. Patches pending from carriers and Kigen.  

### Laravel APP_KEY Exposure → Remote Code Execution
- **Description**: Hundreds of Laravel projects committed `.env` files with APP_KEYs to GitHub. Attackers can craft encrypted payloads that execute code.  
- **Impact**: Full compromise of web applications, database theft, lateral movement.  
- **Status**: Keys actively harvested; exploitation confirmed on 600+ sites. Remediation requires key rotation and secret hygiene.  

### Cursor IDE Malicious VSCode Extension
- **Description**: Fake extension sideloaded infostealers/RATs inside the Cursor AI IDE environment.  
- **Impact**: Credential theft and, in one incident, $500 K cryptocurrency loss.  
- **Status**: Extension removed; users must audit extensions and revoke stolen tokens.  

### WordPress Gravity Forms Supply-Chain Backdoor
- **Description**: Official Gravity Forms website served installer ZIPs containing a hidden PHP backdoor.  
- **Impact**: Arbitrary admin user creation, site defacement, malware propagation.  
- **Status**: Malicious downloads replaced; users must verify checksums and reinstall clean versions.  

### GPUHammer – RowHammer Variant on NVIDIA GPUs
- **Description**: Researchers flipped bits in GPU memory, corrupting AI model weights and compromising data integrity.  
- **Impact**: Model degradation, potential remote code paths via shared GPU workloads.  
- **Status**: No public attacks yet, but NVIDIA urges enabling ECC; firmware updates under review.  

## Affected Systems and Products

- **npm ecosystem**: All platforms where compromised packages are installed  
- **Google Workspace (Gemini)**: Web and mobile clients  
- **Wing FTP Server**: Windows, Linux, macOS versions prior to latest patch  
- **Fortinet FortiWeb**: All hardware & virtual appliances pre-patch  
- **Gigabyte Motherboards**: Dozens of Intel & AMD models with vulnerable UEFI firmware  
- **Automotive Bluetooth Stacks**: Mercedes, Skoda, Volkswagen; plus industrial & consumer devices using impacted chipsets  
- **Kigen eUICC Cards**: Billions of IoT and mobile devices with affected eSIMs  
- **Laravel Applications**: Projects with leaked APP_KEYs on GitHub  
- **Cursor AI IDE (VSCode)**: Users who installed the rogue extension  
- **WordPress Gravity Forms**: Sites that manually downloaded July installer packages  
- **NVIDIA GPUs**: Data-center and consumer cards without ECC enabled  

## Attack Vectors and Techniques

- **Typosquatting Supply-Chain Attack**: Publishing deceptively named npm packages to gain developer execution.  
- **Invisible Prompt Injection**: Using hidden HTML/CSS to alter AI assistant output and lure victims.  
- **Unauthenticated RCE (Wing FTP)**: Direct HTTP requests exploiting input validation flaw.  
- **Pre-Auth SQL Injection**: Crafting queries that break authentication flow in FortiWeb.  
- **UEFI Bootkit Deployment**: Flashing modified firmware or abusing update mechanisms on Gigabyte boards.  
- **PerfektBlue Bluetooth Chain**: Single malicious RF packet triggers memory corruption and shellcode.  
- **eSIM Profile Swap**: Over-the-air commands exploiting weak verification in Kigen cards.  
- **Encrypted Payload Abuse (Laravel)**: Using leaked APP_KEY to forge signed requests executing code.  
- **Malicious IDE Extension**: Users install visually benign extension that runs post-install scripts.  
- **Compromised Installer Backdoor**: Official download replaced with tampered ZIP containing hidden PHP file.  
- **RowHammer on GPU Memory**: High-frequency memory access flips bits, corrupting model parameters.  

## Threat Actor Activities

- **Contagious Interview (DPRK)**  
  - Continues flooding npm with XORIndex malware; targets dev environments for espionage and lateral movement.  

- **Interlock Ransomware Group**  
  - Uses FileFix and web-inject campaigns to deliver new PHP-based Interlock RAT to multiple industries.  

- **Pay2Key Ransomware (Iran-linked)**  
  - Relaunched RaaS with 80% affiliate payout for attacks against US and Israel, likely to leverage new exploits.  

- **Unidentified Crimeware Groups**  
  - Mass-scanning and exploitation of Wing FTP Server and FortiWeb devices following public PoC releases.  
  - Leveraged rogue VSCode extension to steal $500 K in cryptocurrency.  

- **Researchers / Proof-of-Concept Authors**  
  - Demonstrated PerfektBlue Bluetooth chain and GPUHammer, prompting vendor advisories.  

**Bold** defensive action is required: prioritize patching Wing FTP Server, FortiWeb, and Gigabyte firmware; audit npm dependencies, eSIM deployments, and WordPress plugins; and educate users about prompt-injection risks in AI assistants.