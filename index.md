# Exploitation Report

Over the past week defenders have had to respond to a diverse set of live exploitation events ranging from critical zero-day browser flaws to hard-coded backdoors in core enterprise voice infrastructure. Attackers are actively abusing weaknesses that bypass Mark-of-the-Web protections (“ClickFix” and the new “FileFix” chains), leveraging an in-the-wild Chrome vulnerability for remote code execution, exploiting recently patched authentication-bypass bugs in Citrix NetScaler appliances, and taking advantage of a hard-coded root account in Cisco Unified Communications Manager. WordPress sites are also being compromised through an unauthenticated file-deletion flaw in the popular Forminator plugin. Several campaigns—most notably by the “Silver Fox” threat actor, Spanish-speaking data-theft operators, and cryptocurrency-theft groups seeding malicious Firefox add-ons—are actively weaponising these weaknesses.

## Active Exploitation Details

### ClickFix Spin-off / Browser Mark-of-the-Web Bypass  
- **Description**: A flaw in the way modern browsers (Chrome, Edge, Brave, etc.) save HTML files allows adversaries to deliver HTML attachments that are not tagged with the Mark-of-the-Web (MotW) security flag. When a victim double-clicks the file, scripts execute with local-zone privileges, defeating SmartScreen and other browser-based download protections.  
- **Impact**: Initial code execution on end-user workstations, often leading to malware installation (RATs, stealers).  
- **Status**: Actively exploited in phishing campaigns; no vendor patch because the issue stems from browser file-handling design. Mitigations focus on user awareness and blocking HTML e-mail attachments.

### FileFix Attack Chain  
- **Description**: A related social-engineering chain where victims are convinced to rename files with benign extensions (e.g., “.txt”) back to “.html”, again stripping MotW. This enables one-click execution of malicious JavaScript.  
- **Impact**: Same as ClickFix—arbitrary script execution, credential theft, lateral movement.  
- **Status**: Observed in live attacks; no direct patch. Security teams should hard-block risky extensions and enforce attachment sandboxing.

### Google Chrome Zero-Day Rendering Engine Vulnerability  
- **Description**: Memory-safety flaw in Chrome’s rendering pipeline that allows remote code execution when a user visits a specially crafted web page. Google released an emergency update for all desktop channels.  
- **Impact**: Full browser sandbox escape and potential host compromise.  
- **Status**: Confirmed “exploited in the wild.” Patch available in the latest Chrome stable release.

### Cisco Unified Communications Manager (Unified CM) Hard-Coded Root SSH Credentials  
- **Description**: Legacy build images shipped with an undocumented root-level SSH account that could be accessed remotely if the device’s management interface is exposed.  
- **Impact**: Immediate full system takeover, call interception, lateral movement into VoIP and directory services.  
- **Status**: Cisco has removed the backdoor in new images and pushed fixes via the Cisco Unified CM Software Updates utility. Exploits observed against unpatched public-facing systems.

### Citrix NetScaler ADC / Gateway Authentication-Bypass & DoS Flaws  
- **Description**: Two separate but related bugs let unauthenticated actors bypass login controls or crash the authentication service, locking out legitimate users.  
- **Impact**: Remote administrative access (in auth-bypass scenario) or disruption of VPN/Gateway services (DoS).  
- **Status**: Citrix says exploitation attempts were detected prior to disclosure; patches released but may break custom login pages, delaying some customers’ rollout.

### Forminator WordPress Plugin Unauthenticated Arbitrary File Deletion  
- **Description**: Input-validation weakness in the “forms” function lets an unauthenticated user craft a request that deletes any file the web-server user can access, including wp-config.php.  
- **Impact**: Full site takeover, credential dumping, or re-installation of trojanised plugins.  
- **Status**: Exploitation reported in the wild; WPMU DEV issued an urgent update via WordPress auto-update channel.

## Affected Systems and Products

- **Modern Desktop Browsers**: Google Chrome, Microsoft Edge, Brave, Opera (HTML file handling / MotW bypass)  
- **Cisco Unified Communications Manager (Unified CM)**: Versions prior to the fixed build released on Cisco’s advisory; all supported hardware & virtual appliances  
- **Citrix NetScaler ADC & NetScaler Gateway**: Supported 13.x & 14.x builds prior to July 2025 security update  
- **Google Chrome**: Desktop channels before the emergency version released this week (Windows, macOS, Linux)  
- **WordPress “Forminator” Plugin**: Versions < 1.29.2 (all hosting environments)  
- **Windows Endpoints**: Users receiving malicious HTML/TXT attachments exploiting ClickFix or FileFix chains  

## Attack Vectors and Techniques

- **HTML Attachment MotW Bypass (“ClickFix”)**  
  - **Vector**: Phishing e-mails delivering saved-web-page `.html` files that lack the Zone.Identifier stream, executing with local-zone trust.  

- **Renamed File Execution (“FileFix”)**  
  - **Vector**: Social engineering instructions convincing users to rename `.txt` or `.doc` back to `.html`, removing browser security metadata.  

- **Drive-by RCE via Chrome Zero-Day**  
  - **Vector**: Compromised or malicious websites trigger the rendering-engine flaw to execute shellcode in the renderer process and escape the sandbox.  

- **Hard-Coded Credentials / SSH Backdoor**  
  - **Vector**: Direct SSH connections to public-facing Cisco Unified CM management interfaces using the embedded username/password.  

- **Authentication-Bypass Request Smuggling (Citrix)**  
  - **Vector**: Crafted HTTP requests to `/logon/LogonPoint/index.html` manipulating session tokens to skip MFA/LDAP checks.  

- **Unauthenticated File Deletion (Forminator)**  
  - **Vector**: HTTP POST to the plugin’s AJAX handler with a path traversal payload targeting critical WordPress files.  

## Threat Actor Activities

- **Silver Fox**  
  - **Campaign**: Targeting Taiwanese organisations with DeepSeek-themed installers; DLL sideloading drops a custom Gh0stRAT variant and exploits the Chrome zero-day for initial access.  

- **Spanish Data-Theft Group (recently arrested)**  
  - **Activities**: Phishing and browser-based malware delivery leveraging ClickFix techniques to steal political and media emails.  

- **Cryptocurrency-Theft Operators**  
  - **Campaign**: Over 40 fake Firefox wallet extensions exfiltrating seed phrases; use Chrome zero-day and Forminator compromises for distribution infrastructure.  

- **Unidentified Actors Weaponising Vercel’s v0 AI Tool**  
  - **Activities**: Mass-generating fake login pages for Microsoft 365 and Google Workspace that deliver FileFix HTML payloads.  

- **Aeza-Backed Ransomware Crews**  
  - **Activities**: Using Citrix auth-bypass exploits for initial foothold, staging infrastructure on Aeza bulletproof hosting (now sanctioned by OFAC).  

