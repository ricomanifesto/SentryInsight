# Exploitation Report

Over the past week, multiple critical vulnerabilities moved from disclosure to widespread, real-world exploitation. Threat actors are weaponising fresh remote-code-execution flaws in Wing FTP Server, Fortinet FortiWeb and Citrix NetScaler appliances while also abusing leaked Laravel APP_KEYs and a supply-chain compromise of the WordPress Gravity Forms plugin. At the same time, researchers unveiled GPUHammer—an alarming RowHammer variant that corrupts NVIDIA GDDR6 memory—and “PerfektBlue” Bluetooth flaws that could let attackers remotely seize control of millions of vehicles. Immediate patching, key rotation and supply-chain integrity checks are imperative.

## Active Exploitation Details

### Wing FTP Server Remote Code Execution  
- **Description**: A critical vulnerability allows unauthenticated attackers to send specially crafted requests that trigger memory corruption, resulting in execution of arbitrary code with the privileges of the Wing FTP Server process.  
- **Impact**: Full system takeover, deployment of malware or ransomware, data exfiltration, lateral movement inside the network.  
- **Status**: Confirmed in-the-wild exploitation began within 24 hours of public technical write-ups. Fixed versions are available from the vendor.  
- **CVE ID**: CVE-2025-47812  

### Citrix NetScaler “CitrixBleed 2” Information Disclosure / RCE  
- **Description**: A flaw in request handling leaks session tokens and other sensitive data, enabling attackers to hijack authenticated sessions and execute administrative actions remotely.  
- **Impact**: Compromise of VPN gateways, credential harvesting, potential deployment of post-exploitation tooling leading to RCE.  
- **Status**: Added to CISA’s Known Exploited Vulnerabilities catalogue; active exploitation observed against federal and enterprise environments. Patches released by Citrix.  
- **CVE ID**: CVE-2025-5777  

### Fortinet FortiWeb Pre-Auth SQL Injection to RCE  
- **Description**: A pre-authentication SQL injection in FortiWeb’s web interface lets an attacker run arbitrary database commands and pivot to remote code execution on the underlying OS.  
- **Impact**: Complete compromise of web-application-firewall appliances, interception or alteration of protected traffic.  
- **Status**: Proof-of-concept exploits published; exploitation attempts observed in the wild. Fixes issued in July 2025 firmware updates.  
- **CVE ID**: CVE-2025-25257  

### GPUHammer RowHammer Variant on NVIDIA GPUs  
- **Description**: Researchers showed that rapid hammering of specific GDDR6 rows on NVIDIA GPUs induces bit flips, degrading AI model accuracy and potentially allowing data corruption or extraction.  
- **Impact**: Integrity loss of AI workloads, model poisoning, possible escalation if GPU memory holds sensitive data.  
- **Status**: Demonstrated under lab conditions; NVIDIA urges enabling system-level ECC or upgrading hardware/firmware.  

### Laravel APP_KEY Leakage Leading to Remote Code Execution  
- **Description**: Hundreds of repositories on GitHub exposed Laravel APP_KEY environment variables. Attackers can craft maliciously signed cookies to trigger PHP object deserialization and execute code on the target application server.  
- **Impact**: Remote code execution, credential theft, full database compromise across more than 600 identified apps.  
- **Status**: Keys are actively harvested; mass exploitation underway. Mitigation requires regenerating APP_KEY, rotating cookies and auditing repos.  

### WordPress Gravity Forms Supply-Chain Backdoor  
- **Description**: The official Gravity Forms website was breached, and manual installer ZIP files were trojanised with a PHP backdoor that phones home for commands.  
- **Impact**: Remote code execution on any WordPress site that installed the infected package, leading to web-shell deployment and potential site defacement or data theft.  
- **Status**: Malicious downloads detected; clean packages now available. Administrators must verify plugin hashes and reinstall.  

### OpenVSX Extension Marketplace Zero-Day  
- **Description**: A logic flaw in namespace ownership allowed attackers to hijack existing extensions, poison updates and execute arbitrary code on developers’ machines using Cursor and Windsurf IDEs.  
- **Impact**: Supply-chain compromise of developer workstations, credential theft, insertion of malicious code into software builds.  
- **Status**: Zero-day patched; no large-scale abuse reported post-fix, but vulnerable versions existed for months.  

### PerfektBlue Bluetooth Vulnerabilities in OpenSynergy BlueSDK  
- **Description**: Four distinct issues (heap overflows and logic errors) in the Bluetooth stack used by multiple car manufacturers allow attackers within Bluetooth range to achieve code execution on in-vehicle infotainment systems.  
- **Impact**: Potential pivot to critical vehicular subsystems, unauthorised access to driver data, possible safety impact.  
- **Status**: Patches provided to OEMs; exploitation not yet observed publicly but considered high risk for proximity attacks.  

### mcp-remote Command Injection  
- **Description**: Unsanitised parameters are passed directly to the `exec` function in the popular open-source mcp-remote project, enabling arbitrary OS command execution.  
- **Impact**: Compromise of CI/CD pipelines or servers where the package is used (437 k+ downloads).  
- **Status**: Patched in the latest release; users must upgrade immediately.  

### McHire Chatbot Weak Credential Exposure  
- **Description**: A hard-coded administrator password “123456” allowed unauthenticated access to backend chat data for 64 million job applications.  
- **Impact**: Massive PII exposure, reputational damage, potential follow-on phishing attacks.  
- **Status**: Vendor remediated the issue; exposed data may already be in circulation.  

## Affected Systems and Products

- **Wing FTP Server**: All versions prior to patched build (vendor advisory)  
- **Citrix NetScaler ADC & Gateway**: 14.1 before 14.1-12.x; 13.1 before 13.1-55.x; 13.0 before 13.0-93.x (on-prem and cloud)  
- **Fortinet FortiWeb**: 7.4.0; 7.2.0-7.2.2; 7.0.0-7.0.7; 6.3.0-6.3.24  
- **NVIDIA GPUs**: All GDDR6-based consumer, workstation and data-centre cards with ECC disabled  
- **Laravel Applications**: Projects whose APP_KEY leaked in public GitHub repositories  
- **WordPress Sites**: Installations that manually downloaded Gravity Forms ZIPs between 1 July – 12 July 2025  
- **OpenVSX Ecosystem**: Cursor, Windsurf and any IDEs pulling extensions from OpenVSX prior to July 2025 patch  
- **Automotive Platforms**: Mercedes-Benz, Volkswagen, Škoda and other OEMs shipping OpenSynergy BlueSDK ≤ v3.7  
- **mcp-remote NPM Package**: Versions < 1.2.4 (patched) across Linux, macOS and Windows  
- **McHire (Paradox/Olivia) Platform**: U.S.-hosted instances used by McDonald’s recruiting teams  

## Attack Vectors and Techniques

- **RowHammer (GPUHammer)**  
  - Vector: High-frequency memory row access on GDDR6 to induce bit flips  
- **Pre-Auth SQL Injection → RCE (FortiWeb)**  
  - Vector: Crafted HTTP POST to vulnerable parameter triggers stacked SQL queries and command execution  
- **Memory Corruption Overflows (Wing FTP)**  
  - Vector: Malformed FTP command or HTTP request exceeds buffer limits  
- **Session Token Harvesting (CitrixBleed 2)**  
  - Vector: Manipulated requests leak memory containing valid authentication tokens  
- **Deserialization via Forged Cookies (Laravel)**  
  - Vector: Attackers use leaked APP_KEY to sign malicious payloads, triggering PHP object deserialisation  
- **Trojanised Plugin Installation (Gravity Forms)**  
  - Vector: Users download a backdoored ZIP from compromised vendor website  
- **Namespace Takeover (OpenVSX)**  
  - Vector: Adversary deletes and re-registers extension namespace, pushing malicious update  
- **Bluetooth Heap Overflow (PerfektBlue)**  
  - Vector: Malicious L2CAP/AVCTP packets sent over proximity Bluetooth link  
- **Command Injection in CLI (mcp-remote)**  
  - Vector: Unsanitised CLI argument passed to `exec`  
- **Default / Weak Credentials (McHire)**  
  - Vector: Direct web login using hard-coded password  

## Threat Actor Activities

- **Unnamed Wing FTP Exploiters**  
  - Campaign: Rapid mass scanning and deployment of web-shells & coin-miners on publicly exposed servers immediately after PoC release.  

- **Multiple APT & Cyber-Crime Groups (CitrixBleed 2)**  
  - Campaign: Credential-harvesting operations against U.S. federal agencies and large enterprises, leveraging stolen NetScaler sessions for persistent VPN access.  

- **Grey-Hat Researchers & Opportunistic Attackers (FortiWeb)**  
  - Campaign: Automated exploitation attempts observed in honeypots within 48 hours of PoC publication.  

- **Supply-Chain Intrusion Operator (Gravity Forms)**  
  - Campaign: Compromised vendor infrastructure to deliver PHP backdoors; objective appears to be building a foothold on high-traffic WordPress sites.  

- **GitHub Secret-Harvesting Bots**  
  - Campaign: Continuous scraping of public repos for Laravel APP_KEYs, followed by automated exploitation and cryptojacking deployments.  

- **Pay2Key Ransomware-as-a-Service (Iranian-Backed)**  
  - Campaign: Relaunched RaaS platform offering an 80% cut to affiliates; likely to integrate fresh RCE exploits (e.g., Wing FTP, FortiWeb) into intrusion playbooks.  

- **Scattered Spider (Arrests Reported)**  
  - Campaign: Historically leveraged social engineering and VPN exploits similar to CitrixBleed; recent law-enforcement action may disrupt but not dismantle operations.  

- **Vehicle-focused Researchers (PerfektBlue)**  
  - Campaign: Coordinated disclosure to OEMs; no malicious exploitation tracked yet, but POC tools expected to surface on automotive-security forums.  

---

**Action Items:**  
1. Patch Citrix NetScaler, FortiWeb and Wing FTP immediately; revoke and recreate active sessions.  
2. Audit GitHub repositories for secret leakage and rotate Laravel APP_KEYs.  
3. Verify integrity of Gravity Forms installations and replace with verified clean builds.  
4. Enable ECC on NVIDIA GPUs or migrate workloads to ECC-capable hardware.  
5. Apply vendor firmware updates for vehicles and Bluetooth devices using BlueSDK.  
6. Upgrade open-source dependencies (mcp-remote, affected extensions) and monitor supply-chain channels.