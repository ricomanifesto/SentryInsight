# Exploitation Report

Over the past week, multiple critical enterprise-grade vulnerabilities have moved from disclosure to active weaponisation. The most urgent activity centres on Microsoft SharePoint servers, where the China-linked group **Storm-2603** is chaining freshly patched flaws (known collectively as the “ToolShell” zero-day exploit chain) to drop the new Warlock ransomware family. At the same time, long-standing remote-code-execution bugs in **Ivanti Connect Secure** remain a favoured foothold for Chinese operators hitting Japanese organisations six months after fixes were released. SonicWall has also rushed out an emergency update for SMA 100 VPN gateways to close an authenticated file-upload bug that can yield full appliance takeover. Parallel campaigns show attackers abusing WordPress “mu-plugin” mechanics for covert persistence and weaponising Windows UI Automation in the new Coyote banking trojan. These trends reinforce the need for rapid patch management, continuous monitoring of edge devices, and layered ransomware defences.

## Active Exploitation Details

### SharePoint “ToolShell” Zero-Day Chain
- **Description**: A pair of SharePoint flaws that allow unauthenticated attackers to craft specially formatted API or SOAP requests, bypass normal security checks, and execute code via malicious DLL uploads (“ToolShell” implant).
- **Impact**: Full remote code execution on SharePoint servers, lateral movement into Microsoft 365 tenants, and deployment of Warlock ransomware.
- **Status**: Widely exploited in the wild by Storm-2603; Microsoft patches available.

### SonicWall SMA 100 Authenticated File Upload RCE
- **Description**: A critical weakness in the SMA 100 firmware that lets a logged-in user upload arbitrary files outside the intended path, leading to command injection and root-level code execution.
- **Impact**: Complete compromise of the VPN gateway, credential theft, and network pivoting.
- **Status**: Patch released; SonicWall warns that exploitation is “expected imminently” and urges immediate updates.

### Ivanti Connect Secure / Policy Secure RCE Vulnerabilities
- **Description**: Previously disclosed remote-code-execution bugs affecting the web component of Ivanti’s SSL-VPN appliances; exploit chain combines an authentication bypass with command injection over the management interface.
- **Impact**: Device takeover, session hijacking, and persistent network access.
- **Status**: Exploited continuously since last year; fixes available but many Japanese organisations remain unpatched.

### WordPress Mu-Plugin Backdoor Abuse
- **Description**: Attackers with initial admin access place a stealth plugin in the rarely inspected “/wp-content/mu-plugins/” directory, granting persistent administrative control that survives core updates.
- **Impact**: Arbitrary PHP execution, site defacement, credential theft, and payload staging.
- **Status**: Active campaign; no core WordPress patch required but hardening and file-integrity monitoring advised.

### Windows UI Automation Abuse (Coyote Banking Trojan)
- **Description**: First documented malware that leverages the Windows UIA framework to interact programmatically with banking portals, bypassing browser-based anti-fraud controls.
- **Impact**: Automated fund transfers and credential harvesting against Brazilian banks and crypto exchanges.
- **Status**: Active; no underlying Windows patch, mitigation relies on endpoint detection and browser hardening.

## Affected Systems and Products

- **Microsoft SharePoint Server**: 2016, 2019, Subscription Edition on Windows Server  
  **Platform**: On-premises Windows environments
- **SonicWall SMA 100 Series**: SMA 200/210/400/410/500v running 10.x firmware  
  **Platform**: Hardened Linux-based VPN appliances
- **Ivanti Connect Secure / Policy Secure**: 9.x and 22.x branch gateways prior to fixed builds  
  **Platform**: Purpose-built VPN/zero-trust appliances
- **WordPress Sites**: Any version where attackers obtain admin credentials  
  **Platform**: PHP-based CMS on Linux/Windows hosting
- **Windows 10 / 11 Endpoints**: Systems targeted by Coyote trojan  
  **Platform**: Desktop Windows with UI Automation framework enabled

## Attack Vectors and Techniques

- **Deserialization & DLL Upload (SharePoint)**  
  Vector: Crafted API requests bypassing authentication to upload malicious DLLs.

- **Authenticated Arbitrary File Upload (SonicWall)**  
  Vector: Web interface allows attacker-supplied archives to escape intended directories and execute.

- **Auth Bypass + Command Injection (Ivanti)**  
  Vector: Chained web requests manipulate CGI components to run system commands.

- **Mu-Plugin Persistence (WordPress)**  
  Vector: Implant placed in `/mu-plugins/` auto-loaded on every page request, evading plugin listings.

- **UI Automation Scripting (Coyote Trojan)**  
  Vector: Malware leverages Microsoft UIA to simulate user actions inside banking sessions.

## Threat Actor Activities

- **Storm-2603 (China-linked)**  
  Campaign: Exploits SharePoint ToolShell chain, dropping Warlock ransomware on unpatched servers across multiple sectors.

- **Unnamed Chinese APT Targeting Tibet**  
  Campaign: Distributes fake Dalai Lama mobile apps with embedded spyware to surveil Tibetan activists.

- **Chinese Operators Exploiting Ivanti**  
  Campaign: Ongoing intrusion wave against Japanese critical infrastructure via unpatched Ivanti VPN appliances.

- **Coyote Banking Trojan Operators**  
  Campaign: Conduct dozens of financially motivated attacks against Brazilian banks and crypto exchanges by scripting UI interactions.

- **XSS.is Marketplace Takedown**  
  Campaign: Arrest of forum administrator disrupts a major hub for buying exploits and stolen data, likely altering underground supply chains.

