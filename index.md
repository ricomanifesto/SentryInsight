# Exploitation Report

During the past week, threat actors have accelerated the weaponization of multiple high-impact vulnerabilities across enterprise, cloud, and consumer technologies. The most critical activity centers on (1) a pre-authentication SQL-injection flaw in Fortinet FortiWeb that is already being mass-scanned, (2) a remote-code-execution bug in Wing FTP Server that moved from public disclosure to in-the-wild exploitation in less than 24 hours, and (3) prompt-injection weaknesses in Google Gemini that enable convincing phishing lures directly inside Workspace. Simultaneously, firmware weaknesses in Gigabyte motherboards are facilitating stealthy bootkits, while supply-chain attacks against WordPress Gravity Forms, the OpenVSX extension marketplace, and the Cursor IDE demonstrate the growing attacker focus on development ecosystems. Ransomware operators—most visibly Interlock—continue to innovate with “FileFix/ClickFix” loaders that abuse legitimate web assets to drop updated RAT payloads. Collectively, these developments highlight the need for rapid patching, strict supply-chain controls, and continuous monitoring for anomalous web-injection and UEFI activity.

## Active Exploitation Details

### Fortinet FortiWeb Pre-Authentication SQL Injection
- **Description**: A critical SQL-injection flaw in the FortiWeb web-application-firewall interface allows an unauthenticated network attacker to issue arbitrary database commands that lead to full remote-code execution.
- **Impact**: Complete takeover of FortiWeb appliances, lateral movement into protected network segments, and potential tampering with WAF rules to mask further attacks.
- **Status**: Proof-of-concept exploits are public and in use; Fortinet has issued patches and advisories urging immediate upgrade.
- **CVE ID**: CVE-2025-25257

### Wing FTP Server Remote-Code-Execution Vulnerability
- **Description**: A newly disclosed flaw in Wing FTP Server permits attackers to execute arbitrary code with server privileges via crafted network requests.
- **Impact**: Full compromise of file-transfer infrastructure, data theft, and staging points for wider network intrusions.
- **Status**: Exploitation observed one day after disclosure; vendor patches available, but many servers remain unpatched.

### Google Gemini Prompt-Injection Weakness
- **Description**: Gemini for Workspace can be coerced via hidden or “invisible” prompts that appear as legitimate Google Security notices, forcing the AI to insert malicious instructions or phishing links into generated email summaries.
- **Impact**: Highly believable spear-phishing inside Gmail threads, potential credential harvesting, and wider Business Email Compromise (BEC).
- **Status**: Actively abused in the wild; Google is rolling out mitigations but no comprehensive fix is yet confirmed.

### Gigabyte UEFI Secure-Boot Bypass
- **Description**: Multiple Gigabyte motherboard firmware images expose unsigned update mechanisms and insecure flash utilities, allowing attackers to implant persistent bootkits that survive OS re-installs.
- **Impact**: Stealthy, long-term compromise at the firmware level, invisible to most endpoint security controls.
- **Status**: Exploits reported in the wild; Gigabyte has released updated firmware for many—but not all—affected models.

### “FileFix/ClickFix” Loader Abuse (Interlock Campaign)
- **Description**: Interlock ransomware operators leverage a downloader dubbed FileFix (a variant of ClickFix) to inject malicious PHP-based Interlock RAT payloads through compromised, legitimate websites.
- **Impact**: Remote access, data exfiltration, and ransomware deployment in manufacturing, legal, and healthcare environments.
- **Status**: Ongoing campaign; no patch (misuse of legitimate file-conversion features). Mitigation requires hardened web-application controls and threat-intel-driven blocking.

### WordPress Gravity Forms Supply-Chain Backdoor
- **Description**: Attackers compromised the developer’s distribution site and replaced manual-install ZIP packages with backdoored versions of the Gravity Forms plugin.
- **Impact**: Arbitrary code execution on WordPress sites, credential theft, and potential site defacement.
- **Status**: Malicious files removed, but any sites updated during the compromise window remain infected.

### OpenVSX Extension Marketplace Zero-Day
- **Description**: A previously unknown flaw in the OpenVSX registry allowed attackers to hijack extension ownership, enabling a stealth supply-chain attack against Cursor and Windsurf IDE users.
- **Impact**: Arbitrary code execution on millions of developer machines, leading to sensitive source-code theft.
- **Status**: Patched; incident responders advise auditing all extensions obtained prior to the fix.

### Laravel APP_KEY Exposure
- **Description**: Hundreds of Laravel applications on GitHub leaked their APP_KEY environment variable, enabling attackers to generate valid session cookies and execute arbitrary PHP code.
- **Impact**: Full application compromise, database theft, and potential cloud-resource abuse.
- **Status**: Active exploitation confirmed; remediation requires key rotation and code-base sanitization.

### Malicious VSCode Extension in Cursor IDE
- **Description**: A Trojanized VSCode extension distributed via the Cursor AI IDE loaded RATs and infostealers, leading to a recorded $500 K cryptocurrency theft.
- **Impact**: Credential harvesting, crypto-wallet draining, and broader system compromise.
- **Status**: Extension removed; victims must revoke exposed tokens and rebuild compromised systems.

### Kigen eUICC eSIM Vulnerability
- **Description**: Logic flaws in Kigen’s eUICC SIM cards allow remote attackers to manipulate profile download and management procedures over cellular networks.
- **Impact**: SIM-level takeover of billions of IoT devices, enabling intercept, tracking, or denial-of-service attacks.
- **Status**: Researchers disclosed proof-of-concept and notified vendors; patch timelines remain unclear.

### “PerfektBlue” One-Click Bluetooth RCE Chain
- **Description**: A multi-stage exploit targeting Bluetooth stack drivers enables remote code execution on automotive infotainment units and embedded devices after a single pairing prompt.
- **Impact**: Unauthorized control over vehicle systems and industrial / medical devices, posing safety risks.
- **Status**: Demonstrated in the lab; no patches yet issued by major OEMs, making field exploitation plausible.

## Affected Systems and Products

- **Fortinet FortiWeb**: All versions prior to vendor-released fixed builds; hardware and virtual appliances  
- **Wing FTP Server**: Windows, Linux, and macOS builds prior to latest hot-fix  
- **Google Gemini for Workspace**: Web and mobile Workspace environments leveraging Gemini email summarization  
- **Gigabyte Motherboards**: Dozens of Intel/AMD models using vulnerable UEFI firmware revisions  
- **WordPress Gravity Forms Plugin**: Manual installers downloaded during the compromise window  
- **OpenVSX Marketplace**: Cursor and Windsurf IDE extensions prior to registry patch  
- **Laravel Web Applications**: Projects exposing APP_KEYs in public Git repositories  
- **VSCode / Cursor IDE**: Systems that installed the malicious “AI” extension variant  
- **Kigen eUICC eSIM Cards**: Billions of IoT devices and smartphones using affected firmware  
- **Automotive Infotainment (Mercedes, Škoda, Volkswagen)**: Vehicles with unpatched Bluetooth stacks susceptible to PerfektBlue  

## Attack Vectors and Techniques

- **Pre-Auth SQL Injection**: Malformed HTTP requests inject SQL commands into FortiWeb management endpoints.  
- **Crafted FTP Requests**: Specially formatted commands to Wing FTP Server trigger unsafe memory operations leading to RCE.  
- **Invisible Prompt Injection**: Hidden HTML/CSS tokens force Gemini to produce malicious email content.  
- **UEFI Firmware Implantation**: Attackers leverage unsigned update utilities to flash malicious images on Gigabyte boards.  
- **FileFix Web-Injection**: Compromised websites serve manipulated file-conversion pages that sideload Interlock RAT.  
- **Supply-Chain Package Swap**: Adversaries replace legitimate plugin/extension packages (Gravity Forms, OpenVSX, VSCode) with backdoored builds.  
- **Leaked APP_KEY Exploitation**: Attackers generate forged cookies to gain code execution in Laravel apps.  
- **Bluetooth L2CAP Exploit Chain**: PerfektBlue abuses buffer-management flaws to achieve one-click code execution over BLE.  
- **eSIM Profile Manipulation**: Remote over-the-air commands modify eUICC profiles to hijack cellular identities.  

## Threat Actor Activities

- **Interlock Ransomware Group**  
  - **Campaign**: Web-inject/FileFix attacks dropping a new PHP-based Interlock RAT across legal, healthcare, and manufacturing sectors.  
- **Unknown FTP Threat Cluster**  
  - **Campaign**: Mass scanning and exploitation of Wing FTP Server RCE within 24 hours of disclosure.  
- **Unattributed Actors Leveraging Gemini Bugs**  
  - **Campaign**: Phishing operations embedding malicious instructions in AI-generated Gmail summaries to harvest credentials.  
- **Firmware Bootkit Operators**  
  - **Campaign**: Deployment of stealth UEFI implants on Gigabyte motherboards to maintain persistence in enterprise environments.  
- **Supply-Chain Intruders (Gravity Forms / OpenVSX)**  
  - **Campaign**: Compromise of developer infrastructure to insert backdoors in widely used plugins and IDE extensions.  
- **Crypto-Theft Group via VSCode Extension**  
  - **Campaign**: Remote-access and infostealer deployment through malicious Cursor IDE extension, resulting in $500 K loss.  

---