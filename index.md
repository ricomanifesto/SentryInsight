# Exploitation Report

The last week has seen a sharp uptick in real-world exploitation of critical remote-code-execution and privilege-escalation flaws across network appliances, developer ecosystems, and emerging AI platforms. Threat actors are actively weaponizing a pre-authentication SQL injection in Fortinet FortiWeb (CVE-2025-25257), a freshly disclosed RCE in Wing FTP Server, and a supply-chain zero-day in the OpenVSX extension marketplace that has already enabled the theft of US $500,000 in cryptocurrency via a malicious VSCode plug-in. At the same time, prompt-injection weaknesses in Google’s Gemini AI are being leveraged for highly convincing phishing lures, while automotive and IoT vendors grapple with a one-click Bluetooth attack chain dubbed “PerfektBlue.” Interlock ransomware operators have also shifted to a new “FileFix” delivery method that bypasses traditional malware-filtering controls. Collectively, these developments highlight the growing breadth of initial-access vectors—spanning web UIs, firmware, AI assistants, and software-supply-chain infrastructure—and underscore the urgency of rapid patching, hardening, and threat-hunting across all layers of the stack.

## Active Exploitation Details

### Fortinet FortiWeb SQL Injection Leading to Pre-Auth RCE
- **Description**: A critical SQL injection flaw in the FortiWeb web-application firewall allows unauthenticated attackers to run arbitrary database commands and pivot to remote code execution on the underlying system.
- **Impact**: Full takeover of the WAF appliance, lateral movement into protected networks, data exfiltration, and malware deployment.
- **Status**: Proof-of-concept exploits are public and being integrated into attack frameworks; Fortinet has released patches and public advisories urging immediate upgrade.
- **CVE ID**: CVE-2025-25257

### Wing FTP Server Remote Code Execution Vulnerability
- **Description**: A newly disclosed bug in Wing FTP Server permits remote attackers to execute arbitrary commands with the privileges of the service account.
- **Impact**: System compromise, installation of backdoors, and use of the FTP server as a staging point for additional attacks.
- **Status**: Exploitation began within 24 hours of the vulnerability’s technical write-up; official fixes are available from the vendor.

### Google Gemini Prompt-Injection Vulnerability
- **Description**: Logic flaws in Google Gemini’s prompt-handling allow hidden or “invisible” text strings to manipulate Gemini responses, crafting bogus Google Security alerts or hijacking email-summary features in Workspace.
- **Impact**: Phishing redirection, social-engineering at scale, potential credential theft, and misinformation propagation within enterprise workflows.
- **Status**: Actively abused in the wild; Google is rolling out mitigations but no comprehensive fix has been confirmed.

### OpenVSX Extension-Signature Bypass Zero-Day
- **Description**: A zero-day in the OpenVSX marketplace let attackers upload extensions that bypass signature validation, subsequently distributed through Cursor and Windsurf IDEs.
- **Impact**: Remote execution of infostealers and RATs inside developer environments, evidenced by a $500 K cryptocurrency theft traced to a trojanized VSCode extension.
- **Status**: Flaw has been patched, but malicious extensions remain in circulation; users must audit and revoke compromised plug-ins.

### Kigen eUICC / eSIM Provisioning Weakness
- **Description**: Researchers demonstrated a method to exploit protocol weaknesses in Kigen’s eSIM remote-provisioning implementation, enabling SIM profile cloning and device impersonation.
- **Impact**: Hijack of cellular identity, interception of SMS/voice data, and large-scale compromise of IoT fleets relying on eSIM connectivity.
- **Status**: No universal patch; mitigations require carrier- and vendor-level protocol hardening.

### “PerfektBlue” One-Click Bluetooth Attack Chain
- **Description**: A multi-stage exploit chain targeting Bluetooth stacks in automotive head units and embedded devices enables unauthenticated, proximity-based code execution after a single user click.
- **Impact**: Remote vehicle manipulation, firmware planting, and cross-device lateral movement to industrial, medical, and consumer endpoints.
- **Status**: Vendors are assessing exposure; no comprehensive firmware updates released.

### Gigabyte UEFI Secure-Boot Bypass
- **Description**: Vulnerabilities in dozens of Gigabyte motherboard UEFI images let attackers write persistent bootkits that evade Secure Boot and survive OS reinstalls.
- **Impact**: Stealth persistence, full system compromise, and covert control of the boot process.
- **Status**: Public disclosure prompted ongoing firmware updates; active exploitation has been observed in targeted intrusions.

### Laravel APP_KEY Exposure Enabling RCE
- **Description**: Hundreds of Laravel projects published their APP_KEY secrets to GitHub, allowing attackers to forge encrypted cookies and achieve remote code execution.
- **Impact**: Complete application takeover, data theft, and lateral compromise of connected resources.
- **Status**: Keys are still exposed; remediation requires secret rotation and repository sanitization.

## Affected Systems and Products

- **Fortinet FortiWeb**: Versions prior to the patched build released July 2025  
  **Platform**: Physical and virtual FortiWeb appliances  
- **Wing FTP Server**: All editions up to the vulnerable release (vendor bulletin July 2025)  
  **Platform**: Windows, Linux, macOS  
- **Google Workspace & Gemini**: Gmail “Summarize” feature, standalone Gemini AI chat  
  **Platform**: Web, Android, iOS  
- **OpenVSX Ecosystem**: Cursor IDE, Windsurf IDE, any tool auto-syncing from OpenVSX  
  **Platform**: Developer desktops (Windows/macOS/Linux)  
- **Gigabyte Motherboards**: Z690, B760, X670, and other models running affected UEFI firmware versions F7-F10  
  **Platform**: Windows and Linux PCs with affected boards  
- **Vehicles Using Vulnerable Bluetooth Stack**: Mercedes, Skoda, Volkswagen infotainment units  
  **Platform**: Automotive head units, underlying embedded Linux/RTOS  
- **Kigen eUICC-Enabled Devices**: Smartphones and billions of IoT sensors using Kigen eSIM cards  
  **Platform**: Android, embedded RTOS, Linux-based IoT  
- **Laravel Applications**: Any deployment where APP_KEY leaked via public GitHub repos  
  **Platform**: PHP web applications across cloud and on-prem environments

## Attack Vectors and Techniques

- **Prompt Injection**: Crafting hidden or zero-font text that manipulates AI assistant output for phishing and social engineering.  
  **Vector**: Malicious emails, chat messages, or document content processed by Gemini.

- **Pre-Authenticated SQL Injection**: Direct database-command insertion into FortiWeb URI parameters, escalating to RCE.  
  **Vector**: Internet-facing FortiWeb management interfaces.

- **Unauthenticated Command Execution**: Exploiting improper input validation in Wing FTP Server.  
  **Vector**: Crafted FTP or HTTP requests to exposed server endpoints.

- **Malicious Extension Supply-Chain Attack**: Uploading unsigned or tampered extensions to OpenVSX; IDEs auto-pull the payload.  
  **Vector**: Automatic plug-in synchronization in Cursor/Windsurf.

- **FileFix Malware Delivery**: Abuse of the Windows “.filefix” association repair mechanism to side-load Interlock RAT without triggering common filters.  
  **Vector**: Phishing emails with disguised FileFix attachments.

- **Bluetooth “PerfektBlue” Chain**: Leveraging stack overflows and logic flaws in infotainment Bluetooth implementations.  
  **Vector**: Proximity-based Bluetooth connection plus single user approval click.

- **UEFI Bootkit Implantation**: Writing malicious firmware volumes that bypass Secure Boot on Gigabyte boards.  
  **Vector**: Local or remote flashing utilities, firmware update hijacking.

- **RowHammer Variant “GPUHammer”**: Bit-flip manipulation of GDDR6 memory to corrupt AI model data.  
  **Vector**: Unprivileged GPU memory-access patterns via user-land code.

- **Leaked Secret Abuse**: Harvesting Laravel APP_KEY values from public Git repos to forge encrypted session cookies.  
  **Vector**: Automated GitHub searches and HTTP cookie injection.

## Threat Actor Activities

- **Interlock Ransomware Group**  
  **Campaign**: Deploying PHP-based Interlock RAT via FileFix attachments; targets span healthcare, manufacturing, and legal sectors for double-extortion attacks.

- **Unattributed Cryptocurrency Theft Crew**  
  **Campaign**: Leveraged OpenVSX zero-day to push fake VSCode extension, compromising developer wallets and stealing US $500,000 in crypto assets.

- **Unknown Actors Exploiting Wing FTP RCE**  
  **Campaign**: Mass scanning of internet-exposed Wing FTP instances for initial access, followed by deployment of web shells and commercial C2 frameworks.

- **Multiple APT and Cyber-Crime Groups**  
  **Campaign**: Incorporating FortiWeb CVE-2025-25257 exploits into toolchains; observed reconnaissance traffic and exploitation attempts across finance, telecom, and government networks.

- **Pay2Key Ransomware-as-a-Service (RaaS)**  
  **Campaign**: Offering affiliates 80 % profit share to focus on US and Israeli organizations; expected to adopt new initial-access vectors such as FortiWeb and Wing FTP flaws.

- **Supply-Chain Saboteurs**  
  **Campaign**: Compromising the Gravity Forms developer infrastructure to distribute backdoored WordPress plugins, enabling persistence on high-traffic sites.

- **Bluetooth-Focused Research & Grey-Hat Community**  
  **Campaign**: Publicly releasing proof-of-concept demos for PerfektBlue, increasing risk of adoption by opportunistic attackers.

---

Security teams should prioritize patching FortiWeb appliances, Wing FTP servers, and Gigabyte firmware; audit IDE extensions; harden Gemini deployment settings; rotate exposed Laravel keys; and monitor for anomalous Bluetooth and FileFix activity.