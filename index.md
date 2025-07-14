# Exploitation Report

During the last week, security researchers and government agencies confirmed a surge of real-world exploitation against enterprise infrastructure and developer ecosystems. Attackers are chaining unauthenticated remote-code-execution flaws (Wing FTP Server, Fortinet FortiWeb) with session-hijacking bugs (Citrix Bleed 2) while simultaneously abusing software-supply-chain weaknesses in OpenVSX, Visual Studio Code extensions, and WordPress plugin distribution. These campaigns allow adversaries ranging from financially motivated crypto-thieves to advanced persistent threats to seize servers, implant persistent malware, steal credentials, and pivot deeper into corporate networks.

## Active Exploitation Details

### Wing FTP Server Remote Code Execution
- **Description**: A maximum-severity flaw in Wing FTP Server allows unauthenticated attackers to send crafted HTTP requests that trigger OS-level command execution in the context of the service account.  
- **Impact**: Full takeover of the file-transfer server, lateral movement, data theft, and malware deployment.  
- **Status**: Rapid in-the-wild exploitation observed one day after technical details were published; vendor has released fixed builds.  
- **CVE ID**: CVE-2025-47812  

### Citrix Bleed 2 Session Hijacking
- **Description**: Memory-leak vulnerability in NetScaler ADC and Gateway exposes session tokens that remain valid even after logout.  
- **Impact**: Threat actors can bypass multifactor authentication, hijack administrator sessions, and establish persistent VPN access.  
- **Status**: Confirmed active exploitation; CISA added the flaw to its KEV catalog and mandated federal patching. Patches and mitigations available from Citrix.  
- **CVE ID**: CVE-2025-5777  

### Fortinet FortiWeb Pre-Auth SQL Injection
- **Description**: Improper input sanitization in the web UI enables pre-authentication SQL injection, escalating to arbitrary command execution on underlying hosts.  
- **Impact**: Attackers gain root-level control over FortiWeb appliances, allowing web-application-firewall bypass and network intrusion.  
- **Status**: Vendor patches released; multiple proof-of-concept exploits publicly circulating and being weaponized in mass-scan campaigns.  
- **CVE ID**: CVE-2025-25257  

### OpenVSX Extension Marketplace Zero-Day
- **Description**: Logic flaw in OpenVSX’s namespace-ownership verification let attackers publish malicious updates that silently replace legitimate extensions.  
- **Impact**: Extension hijacking for arbitrary code execution on millions of Cursor and Windsurf developer workstations.  
- **Status**: Zero-day actively exploited before disclosure; patch applied to the marketplace backend and namespace controls tightened.  

### Malicious VSCode/“Darcula” Extension in Cursor IDE
- **Description**: A fake Visual Studio Code extension was distributed via Cursor’s side-loading mechanism, bundling RATs and infostealers.  
- **Impact**: Theft of SSH keys, browser cookies, and in one incident $500 000 in cryptocurrency; remote shell persistence.  
- **Status**: Campaign shut down; indicators published, but cloned extensions still circulating on unofficial mirrors.  

### Gravity Forms Supply-Chain Backdoor
- **Description**: Attackers compromised the developer’s infrastructure and inserted PHP backdoors into manually downloaded plugin installers.  
- **Impact**: WordPress site takeover, credential dumping, and potential web-shell deployment across thousands of sites.  
- **Status**: Malicious downloads pulled; clean installers released. Existing sites require manual integrity checks.  

### Google Gemini Workspace Prompt-Injection Abuse
- **Description**: Attackers craft email content that poisons Gemini’s summarization, injecting links and instructions that redirect users to phishing pages.  
- **Impact**: High-credibility phishing without attachments, leading to credential harvesting and malware downloads.  
- **Status**: Technique observed in active phishing waves; Google rolling out trust-boundary updates and user-interface warnings.  

## Affected Systems and Products

- **Wing FTP Server**: Versions prior to patched 7.x releases  
  - **Platform**: Windows, Linux, macOS server deployments  

- **Citrix NetScaler ADC / Gateway**: All appliance models running vulnerable firmware builds before July 2025 updates  
  - **Platform**: On-prem appliances and cloud instances  

- **Fortinet FortiWeb**: 7.0.x and 7.2.x before hotfixes 7.0.5 & 7.2.3  
  - **Platform**: Dedicated hardware, VM, and public-cloud images  

- **OpenVSX Marketplace**: All namespaces prior to backend fix (affects Cursor IDE, Windsurf IDE)  
  - **Platform**: Developer workstations on Windows, macOS, Linux  

- **Cursor IDE / Visual Studio Code**: Systems where the malicious “Darcula” or similarly trojanized extensions were installed  
  - **Platform**: Cross-platform desktop IDEs  

- **WordPress Gravity Forms**: Sites that installed plugin builds downloaded between 10–17 July 2025  
  - **Platform**: PHP-based WordPress CMS  

- **Google Workspace with Gemini**: Gmail users who enabled AI email summarization  
  - **Platform**: Web and mobile Gmail clients  

## Attack Vectors and Techniques

- **Unauthenticated HTTP RCE**: Crafted requests exploit Wing FTP Server’s input parsing to spawn system shells.  
  - **Vector**: Internet-facing FTP web interface on port 5466 (default)  

- **Session Token Leakage**: Citrix Bleed 2 returns residual memory blocks containing active session cookies.  
  - **Vector**: HTTPS requests to `/vpn/` endpoints  

- **Blind SQL Injection**: FortiWeb parameter manipulation injects SQL, pivoting to command execution via stacked queries.  
  - **Vector**: Web management interface before authentication  

- **Extension Namespace Takeover**: Upload of malicious package revision under hijacked namespace in OpenVSX.  
  - **Vector**: Supply-chain update mechanisms of Cursor/Windsurf  

- **Trojanized IDE Extension**: Obfuscated JavaScript binaries download secondary payloads after install.  
  - **Vector**: VSIX side-loading and auto-update routine  

- **Plugin Backdoor Implantation**: Compromised release pipeline embeds base64-encoded web-shell into Gravity Forms core file.  
  - **Vector**: Manual ZIP downloads from vendor portal  

- **Prompt Injection / LLM Abuse**: Hidden instructions in email bodies alter Gemini’s summary output.  
  - **Vector**: HTML email content displayed through AI summarization feature  

## Threat Actor Activities

- **Unidentified Botnet Operators**  
  - **Campaign**: Mass scanning and exploitation of Wing FTP Server CVE-2025-47812; observed installing Go-based miners and reverse shells.  

- **Nation-State & Ransomware Affiliates**  
  - **Campaign**: Leveraging Citrix Bleed 2 to gain footholds in federal and healthcare networks, followed by data theft and double-extortion.  

- **Crimeware Group “Darcula” Clone Authors**  
  - **Campaign**: Distributed malicious VSCode extension, stealing crypto wallets and developer credentials; at least $500 K confirmed loss.  

- **Supply-Chain Intruders (unknown)**  
  - **Campaign**: Compromised Gravity Forms build server to inject persistent PHP backdoors, aiming at MSP-hosted WordPress farms.  

- **Phishing Operators Using AI Hijack**  
  - **Campaign**: Crafting emails that manipulate Gemini summaries to drive victims to credential-harvesting sites impersonating Microsoft 365 login portals.  

- **Automated Exploit Kits on GitHub**  
  - **Campaign**: Weaponization of FortiWeb CVE-2025-25257 PoC; rapid integration into open-source offensive tooling for red-team and malicious use.  

**Bold** mitigation reminder: patch NetScaler, FortiWeb, and Wing FTP immediately, audit developer extensions, and disable Gemini summarization until fixes propagate.