# Exploitation Report

During the last 48 hours multiple high-impact vulnerabilities moved from disclosure to active exploitation. Threat actors are weaponizing critical remote-code-execution issues in Wing FTP Server, Fortinet FortiWeb, and Citrix NetScaler (“CitrixBleed 2”) while simultaneously abusing supply-chain weaknesses (Gravity Forms, OpenVSX) and novel attack surfaces such as Google Gemini prompt-injection, Bluetooth “PerfektBlue,” and GPU-level RowHammer (GPUHammer). The breadth of affected technologies—ranging from enterprise ADCs and web firewalls to AI assistants, vehicle infotainment units, and NVIDIA GPUs—demonstrates an urgent need for immediate patching, defense-in-depth, and enhanced monitoring.

---

## Active Exploitation Details

### Wing FTP Server Remote Code Execution
- **Description**: A critical flaw in Wing FTP Server allows unauthenticated attackers to execute arbitrary code by sending specially crafted commands that bypass input validation.  
- **Impact**: Full system compromise, data exfiltration, deployment of ransomware or web-shells.  
- **Status**: Actively exploited in the wild; vendor issued patches and mitigation guidance.  
- **CVE ID**: CVE-2025-47812  

### Fortinet FortiWeb Pre-Auth SQL Injection / RCE
- **Description**: A pre-authentication SQL injection in the FortiWeb management interface enables attackers to run arbitrary database commands and pivot to remote code execution.  
- **Impact**: Complete takeover of FortiWeb appliances, lateral movement into protected web infrastructure.  
- **Status**: Proof-of-concept exploits publicly released; patches available and strongly advised.  
- **CVE ID**: CVE-2025-25257  

### Citrix NetScaler “CitrixBleed 2”
- **Description**: Memory handling flaw in NetScaler ADC and Gateway permits attackers to leak session tokens and credentials through crafted requests.  
- **Impact**: Session hijacking, privilege escalation, potential VPN gateway takeover.  
- **Status**: Confirmed active exploitation; CISA added to KEV catalog and mandated immediate patching for federal agencies.  
- **CVE ID**: CVE-2025-5777  

### Google Gemini Email Summary Manipulation
- **Description**: Prompt-injection style weakness in Gemini for Workspace lets attackers craft emails that trigger malicious summaries containing phishing links or fraudulent instructions.  
- **Impact**: Social-engineering at scale, credential theft, internal BEC-style fraud.  
- **Status**: Technique observed in real-world phishing campaigns; Google working on mitigations.  

### WordPress Gravity Forms Supply-Chain Backdoor
- **Description**: The developer website distributing manual installers was compromised; trojanized plugin versions include a PHP backdoor executed upon activation.  
- **Impact**: Arbitrary code execution on WordPress sites, data theft, site defacement, malware staging.  
- **Status**: Malicious packages pulled; users must verify hashes and reinstall clean builds.  

### OpenVSX Extension Marketplace Hijack
- **Description**: Previously unknown flaw in OpenVSX allowed attackers to overwrite legitimate extensions, enabling malicious updates for IDEs such as Cursor and Windsurf.  
- **Impact**: Developer workstation takeover, supply-chain contamination of software projects.  
- **Status**: Zero-day now patched; users urged to refresh all affected extensions.  

### Laravel APP_KEY Leakage RCE
- **Description**: Hundreds of public GitHub repositories exposed their Laravel APP_KEY, permitting attackers to craft signed requests that lead to remote code execution.  
- **Impact**: Full application compromise, database access, credential dumping.  
- **Status**: Keys observed in the wild; maintainers advised to rotate APP_KEYs and audit code.  

### PerfektBlue Bluetooth Stack Vulnerabilities
- **Description**: Four flaws in OpenSynergy’s BlueSDK enable a one-click Bluetooth attack chain dubbed “PerfektBlue,” yielding code execution in IVI, medical, industrial, and mobile devices.  
- **Impact**: Remote takeover of 350 million cars and over 1 billion devices, potential physical safety risks.  
- **Status**: No patches yet; vendors (Mercedes, Skoda, Volkswagen, etc.) coordinating fixes, mitigation guidance issued.  

### GPUHammer RowHammer Variant on NVIDIA GPUs
- **Description**: Researchers demonstrated “GPUHammer,” hammering GDDR6 rows to flip bits and degrade AI model accuracy or trigger code faults on NVIDIA GPUs without ECC.  
- **Impact**: Integrity attacks on AI workloads, potential escape from GPU sandboxes, data corruption.  
- **Status**: No reports of criminal abuse yet; NVIDIA urges enabling system-level ECC and firmware updates.  

---

## Affected Systems and Products

- **Wing FTP Server**: Versions prior to latest hotfix; all supported OS platforms  
- **Fortinet FortiWeb**: 7.x and 6.x branches prior to 7.4.2 / 6.4.9; hardware and VM appliances  
- **Citrix NetScaler ADC & Gateway**: All appliance models running vulnerable firmware before July 2025 patches  
- **Google Workspace (Gemini)**: Web and mobile Gmail clients with Gemini-enabled summaries  
- **Gravity Forms (WordPress)**: Manual installer packages downloaded from official site between compromise window  
- **OpenVSX Marketplace**: Extensions for Cursor, Windsurf, and other VS Code derivatives prior to patch rollout  
- **Laravel Applications**: Any deployments whose APP_KEY values were exposed in public repositories  
- **Vehicles & Devices Using OpenSynergy BlueSDK**: Mercedes, Skoda, Volkswagen infotainment; industrial, medical, consumer IoT on Bluetooth stacks pre-patch  
- **NVIDIA GPUs with GDDR6 (No ECC Enabled)**: RTX 20xx/30xx/40xx series, HGX servers, and comparable workstation cards  

---

## Attack Vectors and Techniques

- **Unauthenticated Command Injection (Wing FTP)**  
  • Vector: Crafted FTP commands leveraging input validation flaw to drop payloads.  

- **Pre-Auth SQL Injection to RCE (FortiWeb)**  
  • Vector: Malicious HTTP POST requests manipulating SQL queries, followed by OS-level command execution.  

- **Session Token Harvesting (CitrixBleed 2)**  
  • Vector: Specially crafted requests leak memory segments containing authenticated session cookies.  

- **Prompt Injection / Content Hijacking (Google Gemini)**  
  • Vector: Embedded linguistic triggers in email body steer Gemini summary generation toward malicious instructions.  

- **Trojanized Installer Delivery (Gravity Forms)**  
  • Vector: Supply-chain poisoning—downloaded ZIPs include hidden PHP backdoor executed on plugin activation.  

- **Extension Namespace Takeover (OpenVSX)**  
  • Vector: Exploiting publishing race condition to overwrite existing extension versions with malicious code.  

- **Secret Leakage Abuse (Laravel APP_KEY)**  
  • Vector: Publicly exposed APP_KEY lets attacker forge encrypted cookies/session tokens for code execution.  

- **One-Click Bluetooth RCE (PerfektBlue)**  
  • Vector: Malicious Bluetooth packet sequence exploiting buffer mismanagement in BlueSDK.  

- **GPU RowHammer (GPUHammer)**  
  • Vector: High-frequency memory row access on GDDR6 flips adjacent bits, undermining data integrity.  

---

## Threat Actor Activities

- **Unknown Crimeware Operators**  
  • Campaign: Mass exploitation of Wing FTP and FortiWeb RCEs to deploy web-shells and ransomware loaders.  

- **Adversaries Targeting Enterprises**  
  • Campaign: Ongoing CitrixBleed 2 attacks resulting in lateral movement inside corporate VPN environments.  

- **Supply-Chain Intruder (Unattributed)**  
  • Campaign: Compromise of Gravity Forms infrastructure to distribute backdoored plugins to WordPress admins.  

- **Phishing Actors Leveraging AI**  
  • Campaign: Crafting Gemini-optimized phishing emails that bypass user scrutiny and security filters.  

- **Pay2Key Ransomware-as-a-Service**  
  • Activities: Resurfaced with 80 % revenue share incentives for targeting US and Israeli organizations; likely to incorporate newly disclosed RCE vectors.  

- **Security Researchers (NVIDIA/GPUHammer, PerfektBlue)**  
  • Activities: Demonstrated novel RowHammer and Bluetooth attack chains, providing proof-of-concepts and responsible disclosure to vendors.  

---

**Organizations should immediately patch affected products, rotate exposed secrets, enable ECC where available, and monitor for indicators of compromise associated with the above attack vectors.**