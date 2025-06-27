# Exploitation Report

During the past week defenders observed a marked resurgence in mass scanning and active exploitation of several high-impact vulnerabilities. Progress MOVEit Transfer instances are again being probed at scale, Cisco’s Identity Services Engine (ISE) faces in-the-wild remote-code-execution attempts only days after patches shipped, and CISA’s addition of flaws in AMI MegaRAC, Fortinet FortiOS, and D-Link routers to the Known Exploited Vulnerabilities (KEV) catalog confirms that threat actors are weaponising these weaknesses in real-world attacks. Concurrently, ransomware crews (e.g., CLOP) and financially-motivated groups (e.g., Scattered Spider) continue to leverage these and other vectors to steal data and gain persistence, while state-sponsored adversaries such as Iran’s APT35 intensify spear-phishing operations using AI-generated lures.  

## Active Exploitation Details

### Progress MOVEit Transfer SQL-Injection Chain
- **Description**: A chain of SQL-injection flaws in the MOVEit Transfer secure-file-transfer product allows unauthenticated attackers to access the back-end database and upload arbitrary web shells.  
- **Impact**: Full system compromise, data theft of any files moved through the platform, pivoting into internal networks, and large-scale extortion.  
- **Status**: GreyNoise reports a new spike in automated scanning beginning 27 May 2025; exploits are publicly available and patches were released by Progress.  
- **CVE ID**: CVE-2023-34362, CVE-2023-35036, CVE-2023-35708  

### Cisco ISE / ISE-PIC Remote-Code-Execution Vulnerabilities
- **Description**: Input-validation flaws in the web-based management interface of Cisco Identity Services Engine (ISE) and Passive Identity Connector (ISE-PIC) enable crafted network requests to execute OS commands with root privileges.  
- **Impact**: Unauthenticated remote attackers can gain full root access, create rogue network-access policies, harvest credentials, and disable security controls.  
- **Status**: Actively exploited according to Cisco’s advisory; fixed versions are available and admins are urged to upgrade immediately.  
- **CVE ID**: CVE-2025-20302, CVE-2025-20303  

### AMI MegaRAC BMC Vulnerability
- **Description**: A flaw in the MegaRAC Baseboard Management Controller firmware permits remote execution of arbitrary code over the management network.  
- **Impact**: Attackers can overwrite firmware, implant persistent backdoors at the hardware layer, or perform remote wipe/brick operations on servers.  
- **Status**: Added to CISA KEV, indicating confirmed exploitation; firmware updates have been published by OEM vendors.  
- **CVE ID**: CVE-2022-40258  

### D-Link DIR-859 Router Command-Injection
- **Description**: Improper sanitisation of HTTP parameters in the router’s web UI leads to command injection.  
- **Impact**: Remote takeover of consumer or SOHO routers, enabling traffic interception or botnet enlistment.  
- **Status**: Listed in CISA KEV as exploited; firmware is end-of-life and no official patch exists, making mitigation reliant on device replacement.  
- **CVE ID**: CVE-2021-45382  

### Fortinet FortiOS Path-Traversal / RCE
- **Description**: A path-traversal flaw in FortiOS SSL-VPN allows arbitrary file creation followed by code execution.  
- **Impact**: Obtaining VPN credentials, lateral movement, and potential full takeover of perimeter firewalls.  
- **Status**: Exploitation observed in the wild; Fortinet issued patches and IPS signatures.  
- **CVE ID**: CVE-2023-27997  

### Brother & Other Printer Default-Password Exposure
- **Description**: 689 Brother printer models (plus Fujifilm, Toshiba, Konica Minolta) ship with deterministic default admin passwords derivable from the device’s MAC address.  
- **Impact**: Remote attackers can achieve administrative access, alter firmware, and use printers as staging points for internal attacks.  
- **Status**: Public disclosure prompted active reconnaissance on Shodan; mitigations include immediate credential change and firmware update.  

### Microsoft 365 “Direct Send” Abuse
- **Description**: Attackers leverage the “Direct Send” feature in Microsoft 365 to relay phishing e-mails as if they originate from internal addresses, bypassing SPF/DKIM checks.  
- **Impact**: Credential theft, session hijacking, and downstream BEC (Business Email Compromise).  
- **Status**: Ongoing campaign; Microsoft recommends conditional-access hardening and transport-rule restrictions.  

## Affected Systems and Products

- **Progress MOVEit Transfer**: All versions prior to the June 2023 and subsequent cumulative security hotfixes  
- **Cisco Identity Services Engine / ISE-PIC**: 3.0, 3.1, 3.2, and 3.3 releases prior to patched builds  
- **AMI MegaRAC BMC**: Multiple server OEM implementations across x86 and ARM platforms  
- **D-Link DIR-859**: Firmware v1.06 and earlier (end-of-support)  
- **Fortinet FortiOS**: 7.2.x < 7.2.5 and 7.0.x < 7.0.12 (SSL-VPN enabled)  
- **Brother Printers**: HL-, MFC-, and DCP- series (see vendor advisory for full list)  
- **Microsoft 365 Tenants**: Organisations that allow “Direct Send” via Exchange Online  

## Attack Vectors and Techniques

- **SQL Injection to Web-Shell Upload**  
  Vector: Crafted HTTP POST requests to /api/v1/users in MOVEit portals.  

- **Unauthenticated Command Injection (HTTP POST)**  
  Vector: Malformed JSON payloads against Cisco ISE REST endpoints.  

- **Out-of-Band BMC Exploitation**  
  Vector: TCP/UDP access to IPMI/Redfish services on MegaRAC controllers.  

- **Router Web UI Command Injection**  
  Vector: GET requests with shell metacharacters in the “cmd” parameter on DIR-859.  

- **SSL-VPN Path Traversal**  
  Vector: HTTPS requests containing “../../..” sequences against FortiOS /remote/fgt_lang parameter.  

- **Default Credential Enumeration**  
  Vector: MAC-based password generation for Brother printer admin login over port 80/443.  

- **Email Spoofing via Direct Send**  
  Vector: Authenticated SMTP submission (port 25) from compromised M365 accounts, bypassing outbound protections.  

## Threat Actor Activities

- **CLOP Ransomware**  
  Campaign: Renewed exploitation of MOVEit Transfer; large-scale data theft and double-extortion against retail and finance.  

- **Scattered Spider (UNC3944/Octo Tempest)**  
  Campaign: Pivot from retail to U.S. insurance firms, leveraging SIM-swapping, social engineering, and cloud-token theft for initial access.  

- **OneClik Operators**  
  Campaign: Targeting global energy companies with malicious Microsoft ClickOnce installers and Golang backdoors; post-exploitation privilege escalation on domain controllers.  

- **APT35 / Charming Kitten**  
  Campaign: AI-generated spear-phishing against Israeli journalists and cybersecurity experts to deploy browser-based credential stealers.  

- **Cyber Fattah Hacktivists**  
  Campaign: Exfiltrated and publicly leaked Saudi Games event data in retaliation for regional geopolitical tensions.  

- **Unknown Financial Threat Cluster**  
  Campaign: Utilised open-source remote-access frameworks (MeshAgent, Metasploit) to compromise African financial institutions, focusing on SWIFT workstations and core banking servers.  

## End of Report