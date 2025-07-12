# Exploitation Report

During the last week, defenders observed a surge of real-world attacks abusing three high-impact server-side vulnerabilities and one supply-chain compromise. Active exploitation of Citrix NetScaler “Bleed 2”, Fortinet FortiWeb’s pre-auth SQL-injection bug, and Wing FTP Server’s command-injection flaw is enabling unauthenticated attackers to seize enterprise gateways, web application firewalls, and file-transfer infrastructure. Simultaneously, the compromise of the WordPress Gravity Forms build pipeline is distributing back-doored plugins to thousands of sites. Proof-of-concept code for all server bugs is public, exploitation has been confirmed in the wild, and emergency patches are available, making rapid remediation critical.

## Active Exploitation Details

### Citrix Bleed 2 – NetScaler ADC / Gateway Information Leakage & Session Hijack
- **Description**: Memory-handling flaw allows crafted HTTP/HTTPS requests to read sensitive process memory, yielding valid session tokens and credentials for administrator or VPN users.  
- **Impact**: Attackers can hijack active sessions, escalate privileges, and move laterally into internal networks without authentication.  
- **Status**: Confirmed active exploitation; CISA added the flaw to the Known Exploited Vulnerabilities catalog and mandated federal patching within 24 hours. Fixed builds released by Citrix.  
- **CVE ID**: CVE-2025-5777  

### FortiWeb Pre-Auth SQL Injection Leading to Remote Code Execution
- **Description**: Input validation weakness in FortiWeb’s management interface lets unauthenticated actors inject SQL commands that can be pivoted into arbitrary code execution on the underlying OS.  
- **Impact**: Full takeover of the web application firewall, decryption of inspected traffic, credential theft, and use of the device as a foothold for further attacks.  
- **Status**: Working proof-of-concept exploits publicly released; exploitation activity observed in the wild. Fortinet patched the issue and advises upgrading immediately.  
- **CVE ID**: CVE-2025-25257  

### Wing FTP Server Command Injection
- **Description**: Improper sanitization in Wing FTP’s administration endpoint enables unauthenticated command injection via crafted HTTP parameters.  
- **Impact**: Remote attackers gain system-level command execution, allowing data theft, file manipulation, or deployment of ransomware.  
- **Status**: Actively exploited according to Huntress telemetry; vendor has issued security updates and mitigation guidance.  
- **CVE ID**: CVE-2025-47812  

### Gravity Forms Supply-Chain Backdoor
- **Description**: Attackers compromised the developer’s infrastructure and replaced manual installation ZIPs on the official site with trojanized plugin versions containing a PHP backdoor.  
- **Impact**: Any WordPress site that installed or manually updated the plugin during the compromise window grants attackers persistent remote access, data exfiltration capability, and site defacement potential.  
- **Status**: Malicious builds have been removed, but infected sites remain vulnerable until the plugin files are manually cleaned and updated. No CVE was assigned.

## Affected Systems and Products

- **Citrix NetScaler ADC & Gateway**: All maintained branches prior to fixed builds (e.g., 14.1 ≤ 14.1-36.x, 13.1 ≤ 13.1-51.x)  
- **Fortinet FortiWeb**: Versions 7.4.x, 7.2.x, 7.0.x, and 6.3.x prior to vendor-specified hotfixes  
- **Wing FTP Server**: Windows, Linux, and macOS installations prior to 7.3.0 (exact fixed version per vendor advisory)  
- **Gravity Forms WordPress Plugin**: Any copy downloaded from the official site between the time of compromise and takedown (estimated several days in July 2025)

## Attack Vectors and Techniques

- **Token Bleeding via Memory Disclosure (Citrix Bleed 2)**  
  - **Vector**: Crafted HTTP requests to `/oauth/idp/token/` and similar endpoints extract session data from process memory.  

- **SQL Injection to OS Command Execution (FortiWeb)**  
  - **Vector**: Malformed parameters within the management interface’s authentication flow inject SQL, then leverage stacked queries or UDFs to spawn a system shell.  

- **Unauthenticated Command Injection (Wing FTP)**  
  - **Vector**: Specially crafted `taskID` field in administrative CGI endpoint executes arbitrary shell commands under the service account.  

- **Trojanized Update Package (Gravity Forms)**  
  - **Vector**: Victim administrators download and install a modified ZIP containing obfuscated PHP that opens a reverse shell on first page load.  

## Threat Actor Activities

- **Unknown Threat Groups (Citrix Bleed 2)**  
  - **Campaign**: Mass scanning of Internet-facing NetScaler appliances; goal appears to be credential harvesting for subsequent ransomware deployment.  

- **Opportunistic Exploiters (FortiWeb)**  
  - **Campaign**: Rapid weaponization of public PoC, focusing on service providers and hosting companies to intercept tenant traffic.  

- **Multiple Crimeware Operators (Wing FTP)**  
  - **Campaign**: Post-intrusion deployment of Cobalt Strike and ransomware payloads on small-to-medium businesses relying on Wing FTP for file transfer.  

- **Unidentified Supply-Chain Intruder (Gravity Forms)**  
  - **Campaign**: Insertion of backdoors to build a foothold across thousands of WordPress sites for future monetization (SEO poisoning, skimming, or ransomware).  

- **Pay2Key Ransomware (Iran-linked APT)**  
  - **Activity**: RaaS relaunched with 80 % affiliate share, explicitly incentivizing attacks on U.S. and Israeli organizations; likely to leverage the above gateway flaws for initial access.  

Security teams should prioritize patching Citrix NetScaler, Fortinet FortiWeb, and Wing FTP Server installations, verify plugin integrity on WordPress sites, and monitor for indicators associated with Pay2Key and related exploitation activity.