# Exploitation Report

During the past week, defenders observed a surge in high-impact exploitation targeting edge appliances, widely-deployed server software, and embedded Bluetooth stacks. Proof-of-concept code is circulating for an unauthenticated remote-code-execution flaw in Fortinet FortiWeb, while Citrix “Bleed 2” is being weaponised in the wild against NetScaler ADC and Gateway devices, prompting an emergency CISA directive. Concurrently, active attacks have begun against a maximum-severity vulnerability in Wing FTP Server, and a supply-chain compromise of the popular Gravity Forms WordPress plugin is distributing backdoored packages. Researchers also disclosed “PerfektBlue,” a 1-click Bluetooth attack chain that could impact hundreds of millions of vehicles and IoT devices. Ransomware operators such as the Iranian-linked Pay2Key are incentivising affiliates with higher profit shares, signalling that the freshly exposed remote-code-execution paths will likely be folded into forthcoming campaigns.

## Active Exploitation Details

### Fortinet FortiWeb SQL Injection Leading to Pre-Auth RCE
- **Description**: A critical SQL-injection flaw in FortiWeb’s web interface allows unauthenticated attackers to execute arbitrary database commands that can be chained to full remote-code-execution on the underlying appliance.  
- **Impact**: Full takeover of FortiWeb WAF instances, lateral movement into protected networks, data interception/modification.  
- **Status**: Proof-of-concept exploits publicly released; researchers report scanning and opportunistic exploitation. Fortinet has issued security updates.  
- **CVE ID**: CVE-2025-25257  

### Citrix NetScaler “CitrixBleed 2”
- **Description**: A memory-handling flaw in NetScaler ADC and Gateway exposes sensitive session data that can be leveraged for unauthenticated session hijacking and code execution.  
- **Impact**: Credential/session theft, complete device compromise, access to internal VPN-exposed assets.  
- **Status**: Confirmed active exploitation; CISA added the flaw to its Known Exploited Vulnerabilities (KEV) catalogue and mandated immediate federal patching. Fixes are available from Citrix.  
- **CVE ID**: CVE-2025-5777  

### Wing FTP Server Directory Traversal / RCE
- **Description**: An input-validation weakness permits crafted requests to escape intended directories and execute arbitrary OS commands under the Wing FTP service context.  
- **Impact**: Remote takeover of FTP servers, data exfiltration, malware staging.  
- **Status**: Huntress has observed in-the-wild exploitation. Vendor patches released for all supported branches.  
- **CVE ID**: CVE-2025-47812  

### “PerfektBlue” Bluetooth Attack Chain
- **Description**: Four vulnerabilities in OpenSynergy’s BlueSDK allow a single malicious Bluetooth packet sequence to corrupt memory and attain code execution without user interaction.  
- **Impact**: Remote hijacking of infotainment systems, telematics modules, industrial controllers, phones, and medical devices.  
- **Status**: No widespread exploitation reported yet, but the attack is 1-click and affects an estimated 350 million vehicles and 1 billion devices. Patches and mitigations are being rolled out by OEMs.  

### Gravity Forms Supply-Chain Backdoor
- **Description**: Attackers breached the developer’s infrastructure and replaced manual installer ZIPs with a PHP backdoor that phones home and enables remote commands on WordPress sites.  
- **Impact**: Site defacement, credential theft, malware distribution via compromised WordPress instances.  
- **Status**: Malicious packages were briefly served from the official site; integrity-checked versions have now been re-uploaded and users are urged to reinstall.  

### OpenVSX Marketplace Zero-Day
- **Description**: A flaw in OpenVSX’s extension-signing workflow allowed attackers to publish trojanised extensions capable of arbitrary code execution on development machines using Cursor and Windsurf IDEs.  
- **Impact**: Developer workstation compromise, credential harvesting, CI/CD pipeline intrusion.  
- **Status**: Patched; no confirmed exploitation prior to disclosure, but the window for supply-chain attacks was significant.  

### McHire Chatbot Weak Credential Exposure
- **Description**: Use of the trivial password “123456” on a backend database exposed chat histories for 64 million job applicants.  
- **Impact**: Leakage of personal information, potential phishing and identity-theft vectors.  
- **Status**: Vulnerability reported and secured; evidence suggests data was openly accessible rather than actively exploited by threat actors.  

### mcp-remote Command-Injection Flaw
- **Description**: Unsanitised parameters in the open-source mcp-remote project allow attackers to inject shell commands when remote RC files are processed.  
- **Impact**: Arbitrary OS command execution in environments that embed the library (over 437 k downloads).  
- **Status**: Security advisory and patch issued; exploitation proof-of-concepts exist.  

## Affected Systems and Products

- **Fortinet FortiWeb WAF**: Multiple 6.x and 7.x branches prior to vendor-specified fixed builds  
  - **Platform**: Hardware and virtual FortiWeb appliances  
- **Citrix NetScaler ADC & Gateway**: All supported versions prior to the July 2025 security update  
  - **Platform**: On-prem and cloud deployments, often fronting VPN and gateway services  
- **Wing FTP Server**: Versions before 7.5.1 (Windows, Linux, macOS)  
  - **Platform**: Enterprise and SMB file-transfer environments  
- **OpenSynergy BlueSDK (PerfektBlue)**: Implementations in Mercedes, Volkswagen, Škoda, and numerous mobile/IoT devices  
  - **Platform**: Embedded Linux, Android, QNX, and proprietary automotive OSes  
- **Gravity Forms WordPress Plugin**: Manual installer packages downloaded between July 3 – July 5 2025  
  - **Platform**: Self-hosted WordPress sites on PHP 7/8  
- **OpenVSX Extension Marketplace**: Cursor, Windsurf, and other IDEs pulling unsigned extensions prior to patch  
  - **Platform**: Developer workstations (Windows, macOS, Linux)  
- **mcp-remote Library**: All releases before 1.3.4  
  - **Platform**: Applications integrating the Node.js package  

## Attack Vectors and Techniques

- **Pre-Auth SQL Injection**  
  - **Vector**: Crafted HTTP POST to FortiWeb login endpoint injects SQL, pivoting to shell access.  

- **Session Bleed / Memory Disclosure**  
  - **Vector**: Malformed requests to NetScaler gateways leak session tokens enabling hijack and RCE.  

- **Directory Traversal + Command Injection**  
  - **Vector**: Encoded path segments sent to Wing FTP trigger traversal and `exec` of attacker-supplied commands.  

- **Bluetooth L2CAP Heap Corruption (“PerfektBlue”)**  
  - **Vector**: Single Bluetooth packet with malformed headers causes heap overflow and RCE on BlueSDK stack.  

- **Supply-Chain Backdoor Delivery**  
  - **Vector**: Compromised Gravity Forms ZIP contains obfuscated PHP that contacts C2 on install.  

- **Extension Marketplace Hijack**  
  - **Vector**: Rogue OpenVSX publisher pushes malicious versions that IDEs auto-update.  

- **Hard-Coded Weak Credentials**  
  - **Vector**: Publicly accessible McHire instance protected only by “123456” exposes applicant data.  

- **Node.js Command Injection**  
  - **Vector**: Unsanitised arguments in mcp-remote allow execution via shell metacharacters.  

## Threat Actor Activities

- **Unknown Opportunistic Actors**  
  - **Campaign**: Mass scanning and exploitation of Fortinet FortiWeb and Wing FTP instances to establish footholds and deploy webshells.  

- **Unattributed Actors Targeting Citrix Appliances**  
  - **Campaign**: Active weaponisation of CitrixBleed 2 against U.S. government and enterprise networks; rapid post-exploitation tunnelling observed.  

- **Iranian-Linked Pay2Key Ransomware**  
  - **Campaign**: Relaunched RaaS offering 80 % profit for attacks on U.S. and Israeli organisations; expected to leverage newly disclosed RCE paths for initial access.  

- **Gravity Forms Supply-Chain Intruders**  
  - **Campaign**: Short-lived compromise of vendor infrastructure used to distribute backdoored plugins, suggesting a focused supply-chain operation similar to previous Magecart tactics.  

- **Scattered Spider (Arrests)**  
  - **Campaign**: Law-enforcement disruption following high-profile breaches; residual operators may seek new RCE vectors detailed above.  

- **Huntress Incident-Response Teams**  
  - **Campaign**: Confirmed exploitation telemetry for Wing FTP; providing IOCs and remediation guidance to affected MSPs.  

**Bold** remediation recommendation: organisations should prioritise patching FortiWeb, NetScaler, and Wing FTP; audit WordPress installations for malicious Gravity Forms payloads; update Bluetooth firmware where available; and monitor for connections to known Pay2Key and supply-chain C2 infrastructure.