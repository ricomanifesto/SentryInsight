# Exploitation Report

The past week has been marked by a rapid escalation of real-world exploitation across both traditional infrastructure and emerging AI/IoT stacks. Threat actors moved quickly to weaponize a critical remote-code-execution flaw in Wing FTP Server only one day after technical details were released, while firmware weaknesses in Gigabyte motherboards are being abused to implant UEFI bootkits that survive OS reinstalls. At the same time, a prompt-injection vulnerability in Google Gemini is enabling highly convincing phishing lures, and newly disclosed weaknesses in Kigen eSIM cards place billions of connected devices at risk of SIM hijacking. Research teams also demonstrated a fresh RowHammer variant—“GPUHammer”—against NVIDIA GPUs, and hundreds of Laravel applications remain exposed because leaked APP_KEY secrets allow attackers to obtain full RCE. Parallel supply-chain attacks—including North Korean actors flooding npm with malicious packages and a rogue VSCode extension inside the Cursor IDE—underscore the widening threat surface. Collectively, these incidents highlight a clear trend: adversaries are pivoting faster from disclosure to active exploitation, especially when cloud, AI, and firmware components are involved.

## Active Exploitation Details

### Wing FTP Server Remote Code Execution
- **Description**: A critical flaw allows unauthenticated attackers to execute arbitrary code on vulnerable Wing FTP Server instances after sending a specially crafted request. Exploitation began within 24 hours of public disclosure.  
- **Impact**: Full system compromise, data exfiltration, lateral movement.
- **Status**: Exploited in the wild; hot-fix released by vendor, but many servers remain unpatched.

### Gigabyte UEFI Firmware Vulnerabilities
- **Description**: Dozens of Gigabyte motherboard models ship with UEFI firmware vulnerabilities that let attackers drop bootkits and bypass Secure Boot controls. The flaws stem from insecure update mechanisms and inadequate firmware validation.
- **Impact**: Stealth persistence below the OS, evasion of AV/EDR, integrity loss of the boot chain.
- **Status**: Active exploitation reported; Gigabyte has issued updated firmware for select models, but coverage is incomplete.

### Google Gemini Prompt-Injection Vulnerability
- **Description**: Gemini’s input-sanitization can be bypassed using invisible Unicode or zero-width characters. Attackers craft prompts that masquerade as legitimate security alerts while embedding malicious instructions.
- **Impact**: Credential phishing, session hijacking, remote download of malware under the guise of Gemini-generated recommendations.
- **Status**: Exploits observed in phishing campaigns; Google is rolling out mitigations but no full patch yet.

### Google Gemini Email-Summary Hijack
- **Description**: Gemini for Workspace can be coerced into generating email summaries that include attacker-controlled links or directives, leveraging implicit user trust.
- **Impact**: Drive-by phishing, business-email-compromise amplification.
- **Status**: Abuse seen in the wild; Google investigating defensive updates.

### Kigen eSIM / eUICC Weakness
- **Description**: Design flaws in Kigen-based eUICC cards permit unauthorized profile downloads and SIM-state cloning.
- **Impact**: Subscriber identity theft, rogue network registration, large-scale IoT disruption.
- **Status**: Proof-of-concept exploit published; no universal patch—requires carrier-level remediation.

### GPUHammer RowHammer Variant (NVIDIA GPUs)
- **Description**: Researchers adapted the classic RowHammer DRAM attack to GPU memory, corrupting model weights and inducing AI inference errors.
- **Impact**: Integrity degradation of AI workloads, potential for data leakage via side channels.
- **Status**: Demonstrated in laboratory and cloud GPU environments; NVIDIA advises enabling ECC and updating drivers with enhanced memory scrubbing.

### Laravel APP_KEY Leakage
- **Description**: Public repositories on GitHub expose Laravel APP_KEY secrets; attackers use the key to decrypt cookies, forge session data, and achieve remote code execution within affected apps.
- **Impact**: Full takeover of web applications, database access, supply-chain pivoting.
- **Status**: Mass-scan exploitation observed against ~600 sites; remediation requires key rotation and code redeploy.

### npm Registry Package Poisoning (XORIndex)
- **Description**: North Korean actors published 67 malicious npm packages that sideload the XORIndex malware, mirroring legitimate libraries to lure developers.
- **Impact**: Developer workstation compromise, CI/CD pipeline intrusion, downstream supply-chain infection.
- **Status**: Packages actively downloaded before takedown; ongoing actor persistence efforts noted.

### Malicious VSCode Extension in Cursor IDE
- **Description**: A forged extension masquerading as a productivity add-on drops RATs and infostealers. One confirmed incident led to a $500 k cryptocurrency theft.
- **Impact**: Source-code theft, wallet draining, remote desktop control.
- **Status**: Extension removed, but cloned variants still circulate on unofficial marketplaces.

### FileFix Delivery Mechanism Abuse (Interlock Ransomware)
- **Description**: Interlock operators embed their PHP-based RAT inside a “FileFix” payload delivered via web injects and macro-laden documents.
- **Impact**: Initial foothold for eventual ransomware deployment, credential harvesting.
- **Status**: Campaign ongoing; no vendor patch—defense relies on web-filtering and macro disabling.

## Affected Systems and Products

- **Wing FTP Server 7.x and earlier**: Windows, Linux
- **Gigabyte Motherboards (Z790, X670, B650 series)**: UEFI firmware across Windows/Linux environments
- **Google Gemini AI (Workspace and consumer versions)**: Web, mobile, Gmail integration
- **Kigen eUICC-based eSIM cards**: Smartphones, IoT sensors, M2M modules
- **NVIDIA GPUs (A100, H100, RTX 30/40 series without ECC)**: Data-center and workstation platforms
- **Laravel Framework Applications**: Any deployment with exposed APP_KEY
- **npm JavaScript Ecosystem**: Developers installing XORIndex-tainted packages on Node.js
- **Cursor IDE with rogue VSCode extension**: Windows, macOS
- **Organizations receiving FileFix-laden documents**: Multi-industry, primarily finance and manufacturing

## Attack Vectors and Techniques

- **Unauthenticated HTTP Exploit**: Crafted request triggers RCE in Wing FTP Server.
- **UEFI Bootkit Injection**: Malicious firmware module flashed via vulnerable Gigabyte updater.
- **Invisible Prompt Injection**: Zero-width Unicode slips malicious commands into Gemini conversations.
- **Email-Summary Manipulation**: Gemini auto-summary altered to embed phishing URLs.
- **SIM Profile Cloning**: Rogue SM-DP+ requests abuse Kigen provisioning workflow.
- **GPU RowHammer (GPUHammer)**: High-frequency memory accesses flip GPU DRAM bits.
- **Leaked Secret Key Usage**: Laravel APP_KEY enables cookie forgery and remote artisan commands.
- **Package Typosquatting**: XORIndex modules named close to popular libraries infect dev machines.
- **Malicious IDE Extension**: User-installed add-on executes post-install scripts to fetch RAT.
- **FileFix Macro Chain**: Weaponized documents call “FileFix” loader which deploys Interlock RAT.

## Threat Actor Activities

- **North Korean APT (Contagious Interview lineage)**  
  - Flooding npm with XORIndex malware; targeting software supply chains worldwide.

- **Interlock Ransomware Group**  
  - Deploying new PHP-based RAT through FileFix loaders; leveraging web injects and malicious docs.

- **State-Backed Group (HazyBeacon)**  
  - Using AWS Lambda to host C2 for Windows backdoor targeting Southeast Asian governments.

- **Iran-Linked Pay2Key RaaS**  
  - Offering 80% affiliate revenue to incentivize attacks on U.S. and Israeli organizations.

- **Unknown Financially Motivated Operators**  
  - Exploiting Wing FTP Server RCE for data theft and lateral movement in corporate networks.

- **Crypto-Theft Crew behind Cursor IDE Extension**  
  - Leveraged fake VSCode plugin to steal $500 k in cryptocurrency; continuing to target blockchain developers.

- **Research Community (GPUHammer team)**  
  - Demonstrated GPU RowHammer variant; disclosure prompted vendor mitigations.

- **Cloud Threat Actors**  
  - Abusing Gemini prompt-injection and email-summary flaws in high-volume phishing campaigns.