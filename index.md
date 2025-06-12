# Exploitation Report

Recent intelligence highlights a surge in targeted exploitation of high-impact vulnerabilities across Microsoft Windows and open-source security tooling. Most notably, an APT group (“Stealth Falcon”) is weaponizing a previously unknown Windows WebDAV remote-code-execution flaw to compromise Middle-Eastern government networks, while Mirai botnet operators have pivoted to an authentication bypass in the Wazuh security platform to conscript new devices. In parallel, bootkit operators continue to abuse Microsoft’s Secure Boot bypass to deploy BlackLotus malware, demonstrating that even fully patched endpoints can be subverted if firmware protections are not enforced. The breadth of affected products—ranging from core operating-system components to defensive security platforms—underscores the critical need for rapid patching, rigorous hardening, and continuous threat-hunting.

## Active Exploitation Details

### Windows WebDAV Remote Code Execution Zero-Day
- **Description**: A flaw in the WebDAV service allows specially crafted requests to trigger remote code execution with SYSTEM privileges on Windows endpoints. The vulnerability requires no prior authentication when WebDAV is exposed via IIS or other HTTP listeners.  
- **Impact**: Complete takeover of targeted hosts, malware implantation, lateral movement, and data exfiltration.  
- **Status**: Actively exploited in the wild since March 2025 by the “Stealth Falcon” APT. Microsoft is preparing a patch; temporary mitigations involve disabling the WebClient service or blocking WebDAV traffic.  

### Windows Secure Boot Bypass Used by BlackLotus Bootkit
- **Description**: A logic flaw in Secure Boot policy validation enables attackers with administrative privileges to install malicious bootloaders that execute before the OS kernel.  
- **Impact**: Persistence at the EFI level, evasion of OS-level security controls, and ability to load arbitrary kernel drivers or disable EDR solutions.  
- **Status**: Patched by Microsoft, but exploitation remains widespread as BlackLotus operators target un-patched or misconfigured systems.  
- **CVE ID**: CVE-2023-24932  

### Wazuh API Authentication Bypass (Mirai Campaign)
- **Description**: Improper session validation inside the Wazuh RESTful API permits unauthenticated remote attackers to create administrative accounts and execute arbitrary commands on managed endpoints.  
- **Impact**: Remote code execution, installation of Mirai variants, and enrollment of servers and IoT devices into DDoS botnets.  
- **Status**: Exploited within hours of disclosure by multiple Mirai botnet crews. A patch is available from Wazuh; administrators should upgrade immediately and rotate API credentials.  

## Affected Systems and Products

- **Microsoft Windows (Client & Server)**  
  - Versions exposing WebDAV services or running vulnerable Secure Boot policy (most Windows 10/11 and Server 2019/2022 builds)  
  - Platform: On-premises, cloud-hosted VMs, hybrid AD environments  

- **Wazuh Security Platform**  
  - Versions prior to the fixed release (as per vendor advisory) running the vulnerable REST API component  
  - Platform: Linux-based Wazuh managers, on-premises or cloud deployments  

## Attack Vectors and Techniques

- **Zero-Day WebDAV Exploit**  
  - **Vector**: Malicious HTTP PROPFIND/SEARCH requests sent to exposed WebDAV endpoints  
  - **Technique**: Crafted payload triggers buffer overflow leading to SYSTEM-level shell  

- **Secure Boot Policy Tampering**  
  - **Vector**: Delivery of signed, malicious bootloader via phishing or privilege-escalation chain  
  - **Technique**: Replacement of legitimate EFI files to bypass boot verification and load BlackLotus  

- **Wazuh API Takeover**  
  - **Vector**: Direct HTTPS requests to the Wazuh REST API using forged session tokens  
  - **Technique**: Creation of rogue admin users followed by remote command execution to deploy Mirai binaries  

## Threat Actor Activities

- **Stealth Falcon (Nation-State APT)**  
  - **Campaign**: Targeted defense and government entities in Turkey, Qatar, Egypt, and Jordan with spear-phishing that redirects victims to WebDAV exploits. Post-exploitation toolset includes custom backdoors and credential-dumping utilities.  

- **Mirai Botnet Operators (Multiple Crews)**  
  - **Campaign**: Automated scanning for vulnerable Wazuh instances, immediate infection with modified Mirai payloads, and use of newly compromised nodes for high-volume DDoS attacks against gaming and financial services.  

- **BlackLotus Affiliate Networks**  
  - **Campaign**: Ongoing distribution of BlackLotus bootkit through malvertising and cracked-software installers, focusing on consumer and SMB sectors where Secure Boot is disabled or outdated.  

