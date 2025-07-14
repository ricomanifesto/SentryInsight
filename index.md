# Exploitation Report

During the past week, defenders observed a sharp rise in real-world exploitation of several critical server-side flaws. Three enterprise-grade remote-code-execution vulnerabilities—Wing FTP Server (CVE-2025-47812), Fortinet FortiWeb (CVE-2025-25257), and Citrix NetScaler ADC/Gateway “CitrixBleed 2” (CVE-2025-5777)—moved from disclosure to weaponisation in a matter of hours, with working exploits circulating publicly and first compromises already reported. In parallel, attackers abused leaked Laravel APP_KEY secrets to seize hundreds of web applications, and a supply-chain compromise of the WordPress Gravity Forms plugin injected a backdoor into new installs. These attacks collectively enable unauthenticated takeover of file-transfer servers, application firewalls, load balancers, and widely-deployed CMS sites—assets that often sit deep inside corporate networks—providing ransomware operators and APT groups with direct footholds for lateral movement and data theft.

## Active Exploitation Details

### Wing FTP Server Remote Code Execution
- **Description**: A maximum-severity flaw in Wing FTP Server allows unauthenticated attackers to send crafted HTTP requests that bypass input validation and execute arbitrary commands with the privileges of the service account.  
- **Impact**: Full system compromise, arbitrary file upload, data theft, lateral movement into internal networks.  
- **Status**: Exploits observed in the wild less than 24 hours after disclosure; official patches released by WingFTP.  
- **CVE ID**: CVE-2025-47812  

### Fortinet FortiWeb Pre-Auth SQL Injection to RCE
- **Description**: A critical SQL injection in FortiWeb’s web interface lets unauthenticated users inject SQL payloads that cascade into operating-system command execution.  
- **Impact**: Gaining root‐level access on the application firewall, interception or alteration of inbound/outbound web traffic, credential harvesting.  
- **Status**: Proof-of-concept exploit code publicly available; Fortinet issued emergency firmware updates.  
- **CVE ID**: CVE-2025-25257  

### Citrix NetScaler “CitrixBleed 2”
- **Description**: An input-handling flaw in NetScaler ADC and Gateway permits disclosure of session tokens that can be repurposed to hijack authenticated sessions and ultimately execute code.  
- **Impact**: Session hijacking, privilege escalation to appliance admin, pivot into internal Citrix-published applications.  
- **Status**: Confirmed active exploitation; CISA added to KEV catalogue and mandated federal patching. Fixes available from Citrix.  
- **CVE ID**: CVE-2025-5777  

### Laravel APP_KEY Leakage Remote Code Execution
- **Description**: Attackers weaponise leaked Laravel APP_KEY values (often exposed in public GitHub repos) to forge encrypted cookies and trigger the framework’s deserialisation routines, resulting in arbitrary code execution.  
- **Impact**: Complete takeover of affected Laravel applications, database exfiltration, deployment of web shells.  
- **Status**: Mass-exploitation evident against at least 600 Internet-facing apps; mitigation requires key rotation and code updates.  

### WordPress Gravity Forms Supply-Chain Backdoor
- **Description**: The developer’s download infrastructure for the Gravity Forms plugin was compromised; manual installers obtained from the site contained an obfuscated PHP backdoor executed during plugin activation.  
- **Impact**: Remote command execution under web-server context, creation of rogue admin accounts, SEO spam or malware distribution.  
- **Status**: Malicious packages pulled; defenders must verify hashes and replace infected copies.  

## Affected Systems and Products

- **Wing FTP Server**: v7.4.0 and earlier on Windows, Linux, macOS  
- **Fortinet FortiWeb**: Physical and virtual appliances prior to fixed firmware (FortiWeb 7.0.x, 6.4.x)  
- **Citrix NetScaler ADC/Gateway**: 13.1 before 13.1-55.15 and 14.1 before 14.1-16.7  
- **Laravel Applications**: Any deployment where the APP_KEY has leaked publicly; PHP-based web servers (Apache, Nginx)  
- **WordPress Gravity Forms**: Manual installation packages downloaded during the compromise window, affecting any WordPress site where installed  

## Attack Vectors and Techniques

- **Unauthenticated HTTP RCE**  
  - **Vector**: Crafted HTTP requests exploiting input-validation flaws (Wing FTP Server)  

- **Pre-Auth SQL Injection Chain**  
  - **Vector**: Malicious SQL payloads in web parameters leading to OS-level command execution (FortiWeb)  

- **Session Token Leakage / Replay**  
  - **Vector**: Malformed requests cause memory disclosure of valid session tokens, used to hijack sessions (CitrixBleed 2)  

- **Cryptographic Key Forgery**  
  - **Vector**: Using leaked Laravel APP_KEY to create signed cookies, triggering unsafe PHP object deserialisation  

- **Supply-Chain Package Tampering**  
  - **Vector**: Compromised distribution server served backdoored plugin ZIPs (Gravity Forms)  

## Threat Actor Activities

- **Unknown Crimeware Operators**  
  - **Campaign**: Mass scanning and exploitation of Wing FTP Server CVE-2025-47812 to deploy reverse shells and file exfiltration tools.  

- **Unattributed Threat Actors**  
  - **Campaign**: Automated exploitation of FortiWeb appliances following public PoC release; observed dropping web shells named “fwiup.php.”  

- **Multiple APT and Cyber-Criminal Groups**  
  - **Campaign**: Leveraging CitrixBleed 2 for initial access before ransomware deployment; CISA notes targeting of federal civilian agencies.  

- **GitHub Reconnaissance Actors**  
  - **Campaign**: Scraping public repositories for Laravel .env files containing APP_KEY values, then executing remote commands to plant cryptominers.  

- **Supply-Chain Intruder (unidentified)**  
  - **Campaign**: Breached Gravity Forms infrastructure; objective appears to be long-term installation of backdoors across high-traffic WordPress sites.  

