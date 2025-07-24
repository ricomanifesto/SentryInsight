# Exploitation Report

Over the past week, multiple enterprise-grade products have come under active attack, with threat actors ranging from financially-motivated ransomware crews to state-aligned espionage groups. The most critical activity centers on a new remote-code-execution flaw in SonicWall SMA 100 VPN appliances, a freshly patched zero-day chain in Microsoft SharePoint abused to deploy Warlock ransomware, and the continued real-world abuse of two high-severity Ivanti Connect Secure vulnerabilities that were disclosed last year. In parallel, website operators are facing stealthy persistence mechanisms embedded in WordPress *mu-plugins*, while novel tradecraft such as the Coyote banking trojan’s use of Windows UI Automation increases the overall threat surface. Immediate patching and layered defenses are strongly advised.

## Active Exploitation Details

### SonicWall SMA 100 Remote Code Execution
- **Description**: A critical, authenticated arbitrary file-upload flaw in SMA 100 series VPN appliances allows attackers to upload malicious packages and execute code as root on the underlying OS.  
- **Impact**: Full device takeover, lateral movement into protected networks, and potential deployment of malware or ransomware.  
- **Status**: SonicWall released fixed firmware and warns that exploitation attempts have already been observed in the wild. Administrators are urged to upgrade immediately.

### Microsoft SharePoint “ToolShell” Zero-Day Chain
- **Description**: An exploitation chain dubbed “ToolShell” targets two recently fixed SharePoint vulnerabilities, enabling an attacker to run PowerShell in the W3WP process, drop web shells, and gain system-level access.  
- **Impact**: Execution of Warlock ransomware, theft of SharePoint-hosted data, and rapid lateral movement across Windows domains.  
- **Status**: Patches are available through the latest Microsoft security updates, but Storm-2603 is actively exploiting unpatched servers.

### Ivanti Connect Secure / Policy Secure Auth Bypass & Command Injection
- **Description**: Attackers chain an authentication-bypass flaw with a post-auth command-injection bug to achieve pre-authentication remote code execution on Ivanti gateways.  
- **Impact**: Network-edge compromise, credential theft, and deployment of additional payloads inside corporate environments.  
- **Status**: Fixes were issued six months ago, yet Chinese threat actors continue to exploit unpatched devices, particularly in Japan.  
- **CVE ID**: CVE-2023-46805, CVE-2024-21887

### WordPress Mu-Plugins Stealth Backdoor
- **Description**: Threat actors insert malicious PHP scripts into the *mu-plugins* directory, which loads automatically on every page request. The backdoor provides persistent admin access, command execution, and data exfiltration.  
- **Impact**: Site defacement, database theft, malware hosting, and use of compromised sites in broader attack campaigns.  
- **Status**: No vendor patch is required; remediation involves file-system cleanup, credential rotation, and hardening of WordPress administration.

## Affected Systems and Products

- **SonicWall SMA 100 Series Appliances**: SMA 200, 210, 400, 410, and 500v running unpatched firmware  
- **Microsoft SharePoint**: SharePoint Server 2016, SharePoint Server 2019, and Subscription Edition prior to July 2025 security updates  
- **Ivanti Connect Secure / Policy Secure**: 9.x and 22.x branches that have not applied the January 2025 remedial firmware  
- **WordPress Sites**: Any version where attackers obtain administrative or file-write access to the *mu-plugins* directory

## Attack Vectors and Techniques

- **Authenticated File-Upload RCE**  
  - **Vector**: Crafted archive uploaded through SMA 100 management interface, executed via post-upload path traversal.

- **Web-Shell Injection via SharePoint**  
  - **Vector**: Chained SharePoint flaws deliver PowerShell payload (“ToolShell”) that writes an ASPX web shell into the *layouts* directory.

- **Auth Bypass + Command Injection (Ivanti)**  
  - **Vector**: Initial unauthenticated request bypasses login controls, followed by crafted parameters that trigger shell commands.

- **Mu-Plugin Persistence**  
  - **Vector**: Malicious PHP dropped into */wp-content/mu-plugins/*. WordPress auto-loads the file on every request, hiding it from typical plugin lists.

- **Windows UI Automation Abuse (Coyote Trojan)**  
  - **Vector**: Malware leverages the UIA framework to interact with banking sessions, bypassing browser protections and capturing credentials.

## Threat Actor Activities

- **Storm-2603 (China-nexus)**  
  - **Campaign**: Leveraging SharePoint “ToolShell” chain to push Warlock ransomware across unpatched servers in manufacturing, legal, and education sectors.

- **Unnamed Chinese Espionage Group**  
  - **Campaign**: Exploiting Ivanti Connect Secure flaws to maintain long-term access to Japanese corporate networks for data exfiltration.

- **WordPress Backdoor Operators (Undisclosed)**  
  - **Campaign**: Mass compromise of SMB and e-commerce sites, using *mu-plugins* backdoor to inject payment skimmers and SEO spam.

- **Coyote Banking-Trojan Operators**  
  - **Campaign**: Dozens of credential-theft attacks against Brazilian banks and crypto exchanges using UI Automation to hijack transactions.

- **Chinese APT Targeting Tibetan Community**  
  - **Campaign**: Distribution of fake Dalai-Lama mobile apps to implant spyware, coinciding with upcoming cultural events.

