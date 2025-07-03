# Exploitation Report

Recent reporting highlights a surge in active exploitation of critical vulnerabilities across widely-used software and infrastructure. The most pressing issues include a new Google Chrome zero-day already weaponized in the wild, a “ClickFix/​FileFix” browser-safeguard bypass that removes the Mark-of-the-Web (MotW) protection from downloaded HTML files, and a backdoor SSH account in Cisco Unified Communications Manager that enables unauthenticated root access. Concurrently, authentication-bypass flaws in Citrix NetScaler appliances and an arbitrary file-deletion bug in the popular WordPress “Forminator” plugin expand attackers’ options for lateral movement and full-site compromise. State-sponsored actors—such as Russia’s Gamaredon and multiple North-Korean groups—are actively folding these weaknesses into phishing, malware, and credential-theft campaigns targeting government, Web3, and cryptocurrency sectors.

## Active Exploitation Details

### Google Chrome Zero-Day (actively exploited)
- **Description**: An undisclosed memory-safety flaw in the Chrome browser that allows remote code execution when a user visits a malicious web page.
- **Impact**: Enables full takeover of the browser context, potential sandbox escape, and subsequent host compromise.
- **Status**: Confirmed exploitation in the wild; Google has released an emergency update for all desktop platforms.

### ClickFix / FileFix MotW Bypass
- **Description**: A logic flaw in the way modern browsers (Chrome, Edge, Firefox) save HTML files locally. By abusing “Save As” functionality, attackers strip the Mark-of-the-Web attribute, disabling Windows’ protected-view warnings.
- **Impact**: Delivers malicious scripts or installers that execute with full user privileges without SmartScreen or Defender prompts.
- **Status**: Actively used in phishing campaigns (“BabyShark,” North-Korean Web3 attacks); no official patch—mitigations are limited to user awareness and endpoint controls.

### Cisco Unified Communications Manager Hardcoded SSH Root Account
- **Description**: Unified CM shipped with an undocumented root level SSH credential, effectively a backdoor.
- **Impact**: Remote attackers with network reach can obtain root shell access, modify configurations, intercept VoIP traffic, or pivot further inside corporate networks.
- **Status**: Cisco has removed the account in a recent security update; customers must upgrade immediately.

### Citrix NetScaler ADC & Gateway Authentication Bypass
- **Description**: Recently disclosed flaws allow unauthenticated attackers to circumvent login mechanisms and, in some cases, trigger denial-of-service conditions.
- **Impact**: Results in remote admin access, session hijacking, or outage of authentication services.
- **Status**: Patches released. Citrix warns that applying them may break some login pages, potentially delaying adoption and leaving devices exposed.

### WordPress Forminator Plugin Arbitrary File Deletion
- **Description**: An unauthenticated endpoint permits attackers to delete arbitrary files on the web server.
- **Impact**: Enables site takeover by deleting critical configuration files (e.g., `wp-config.php`) or security plug-ins, leading to privilege escalation and code execution.
- **Status**: Fixed in the latest Forminator version; exploitation attempts against unpatched sites are already being observed by security researchers.

## Affected Systems and Products

- **Google Chrome (Desktop versions)**  
  Platform: Windows, macOS, Linux

- **Modern Browsers (Chrome, Edge, Firefox) on Windows**  
  Platform: Windows 10/11—local file handling / MotW mechanism

- **Cisco Unified Communications Manager (Unified CM) 15.x and earlier**  
  Platform: Hardened Linux appliance / VMware OVA deployments

- **Citrix NetScaler ADC & NetScaler Gateway (formerly Citrix ADC/Gateway) 14.1, 13.1, 13.0**  
  Platform: Physical and virtual appliances

- **WordPress sites running Forminator ≤ 1.29.0**  
  Platform: PHP / MySQL on Linux, Windows, or managed hosting

## Attack Vectors and Techniques

- **Drive-by Web Exploit**  
  Vector: Malicious website exploiting Chrome zero-day to trigger RCE.

- **Saved-HTML MotW Stripping (ClickFix/FileFix)**  
  Vector: Email or chat delivers a benign-looking HTML attachment; user saves locally; MotW is removed; second-stage script runs without warnings.

- **Backdoor SSH Access**  
  Vector: Automated scanners locate exposed Cisco CM SSH service and log in with hardcoded credentials.

- **Authentication Bypass over HTTP/HTTPS**  
  Vector: Crafted requests to vulnerable NetScaler endpoints skip login checks or exhaust service, enabling DoS or admin session creation.

- **Unauthenticated REST Endpoint Abuse**  
  Vector: Direct POST request to Forminator API endpoint deletes arbitrary server paths.

## Threat Actor Activities

- **Gamaredon (Russia)**  
  Campaign: Intensive spear-phishing against Ukrainian government agencies; weaponizes network drives and potentially leverages ClickFix-style HTML delivery.

- **North-Korean Threat Cluster (“BabyShark,” NimDoor operators)**  
  Campaign: Target Web3 and cryptocurrency firms; deploy NimDoor malware for persistence and crypto-theft; weaponizes ClickFix MotW bypass.

- **Silver Fox**  
  Campaign: Taiwanese intrusion using sideloaded DeepSeek installer to push a Gh0stRAT variant, exploiting user trust in AI tools.

- **Scattered Spider**  
  Campaign: Ongoing breaches in aviation sector (Qantas disclosure) using sophisticated social engineering and identity compromise.

- **Unknown Cyber-criminal Crews**  
  Campaign: Mass production of fake Okta/Microsoft 365 login portals using AI tools (Vercel’s v0) and callback phishing with brand-spoofed PDFs; piggyback on MotW bypass for initial payload delivery.

- **North-Korean IT Worker Network**  
  Activity: Thousands of operatives placed in tech companies to steal code signing certificates and intellectual property, potentially integrating exploits above into supply-chain attacks.

## End of Report