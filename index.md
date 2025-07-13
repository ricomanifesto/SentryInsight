# Exploitation Report

Over the last week, threat actors have accelerated their exploitation of multiple high-impact vulnerabilities across enterprise, cloud, and consumer technology stacks. Active attacks are now confirmed against Wing FTP Server, Citrix NetScaler ADC/Gateway, and Fortinet FortiWeb, while supply-chain compromises and cryptographic key leakage are enabling remote code execution in popular WordPress and Laravel deployments. In parallel, researchers have weaponized a new GPU-level RowHammer variant (“GPUHammer”) that corrupts AI workloads on NVIDIA hardware. Security teams should prioritise patching the documented CVEs, rotate exposed secrets, and harden systems handling GDDR6-based GPUs.

## Active Exploitation Details

### GPUHammer RowHammer Variant on NVIDIA GDDR6 GPUs
- **Description**: A hardware-fault RowHammer technique adapted to GDDR6 memory flips bits on NVIDIA GPUs, leading to silent corruption of AI model parameters.  
- **Impact**: Model degradation, potential data poisoning, denial-of-service, and integrity loss in AI pipelines relying on affected GPUs.  
- **Status**: Proof-of-concept demonstrated publicly; NVIDIA urges enabling system-level ECC as an immediate mitigation.  
- *No CVE ID referenced in the source material.*

---

### Wing FTP Server Remote Code Execution
- **Description**: Critical input-validation flaw in Wing FTP Server allows unauthenticated attackers to execute arbitrary code through crafted requests.  
- **Impact**: Full system compromise, data theft, lateral movement, and ransomware deployment on servers running Wing FTP.  
- **Status**: Active exploitation observed within 24 hours of disclosure; vendor patches available.  
- **CVE ID**: CVE-2025-47812

---

### Fortinet FortiWeb Pre-Auth SQL Injection Leading to RCE
- **Description**: A SQL injection in FortiWeb’s web interface allows execution of arbitrary database commands which can be chained to gain shell access.  
- **Impact**: Remote takeover of FortiWeb appliances, credential theft, and intrusion into network segments protected by the WAF.  
- **Status**: Proof-of-concept exploits released; patches published by Fortinet, with exploitation attempts beginning in the wild.  
- **CVE ID**: CVE-2025-25257

---

### Citrix NetScaler “CitrixBleed 2”
- **Description**: Memory-handling flaw in NetScaler ADC and Gateway enables attackers to leak session data or execute code without authentication.  
- **Impact**: Session hijacking, credential compromise, remote network access, and potential privilege escalation across enterprise environments.  
- **Status**: Confirmed by CISA as actively exploited; emergency directives issued to federal agencies to patch immediately.  
- **CVE ID**: CVE-2025-5777

---

### Laravel APP_KEY Exposure Abuse
- **Description**: Leaked Laravel APP_KEY secrets on public GitHub repositories let attackers forge cookies or encrypt payloads that trigger remote code execution.  
- **Impact**: Complete application compromise, database extraction, and shell access on over 600 publicly reachable Laravel instances.  
- **Status**: Ongoing mass exploitation reported; administrators must rotate APP_KEYs and audit repositories.  

---

### Gravity Forms Supply-Chain Backdoor
- **Description**: The official manual installer packages of the Gravity Forms WordPress plugin were replaced with versions containing a PHP backdoor.  
- **Impact**: Backdoored websites may allow remote command execution, data theft, SEO poisoning, and further supply-chain propagation.  
- **Status**: Malicious plug-ins distributed; legitimate versions restored, but infected sites remain exposed until manually cleaned.  

## Affected Systems and Products

- **NVIDIA GPUs with GDDR6 memory**: Data-centre and workstation cards lacking ECC protection  
- **Wing FTP Server**: All supported platforms; vulnerable versions prior to vendor’s July 2025 update  
- **Fortinet FortiWeb**: Physical and virtual appliances running vulnerable firmware branches prior to 7.4.x/7.2.x security release  
- **Citrix NetScaler ADC & Gateway**: Appliances running builds prior to fixed versions addressing CitrixBleed 2  
- **Laravel-based Web Applications**: Instances whose APP_KEY secrets have been exposed via public repositories  
- **WordPress Gravity Forms Plugin**: Websites that installed the compromised manual ZIP packages during the attack window  

## Attack Vectors and Techniques

- **GPU RowHammer (“GPUHammer”)**  
  - **Vector**: High-frequency memory row activations targeting GDDR6 to induce controlled bit flips and corrupt AI models.  

- **Unauthenticated HTTP RCE (Wing FTP)**  
  - **Vector**: Crafted HTTP requests exploiting input validation flaws, delivering shellcode or dropping web shells.  

- **Pre-Auth SQL Injection → OS Shell (FortiWeb)**  
  - **Vector**: Malformed SQL queries in HTTP parameters escalate to system-level command execution.  

- **Session Memory Leak / Code Execution (CitrixBleed 2)**  
  - **Vector**: Direct interaction with NetScaler services to dump sensitive memory and reuse tokens or inject payloads.  

- **Cryptographic Key Forgery (Laravel APP_KEY)**  
  - **Vector**: Publicly leaked APP_KEY allows forging signed cookies to inject PHP code or Laravel serialised payloads.  

- **Supply-Chain Backdoor (Gravity Forms)**  
  - **Vector**: Users download trojanised plugin ZIPs from a compromised developer website; backdoor activates on install.  

## Threat Actor Activities

- **Unknown Opportunistic Attackers (Wing FTP & FortiWeb)**  
  - **Campaign**: Mass internet scanning followed by automated exploitation, establishing reverse shells for follow-on ransomware or exfiltration.  

- **Iranian-Backed Pay2Key Ransomware Group**  
  - **Activities**: Relaunched RaaS platform with 80 % affiliate profit share, encouraging attacks on U.S. and Israeli entities; exploits CitrixBleed 2 and other edge-device flaws for initial access.  

- **Supply-Chain Intruder (Gravity Forms Incident)**  
  - **Activities**: Compromised plugin developer infrastructure to distribute backdoored packages, targeting WordPress administrators globally.  

- **Commodity Threat Actors (Laravel APP_KEY Abuse)**  
  - **Activities**: Automated GitHub scraping for APP_KEY secrets, followed by exploitation to deploy web shells and cryptominers.  

- **Researchers / Proof-of-Concept Authors (GPUHammer & FortiWeb)**  
  - **Activities**: Public release of technical papers and PoC code, inadvertently lowering barrier to entry for less-sophisticated adversaries.  

Security teams should deploy vendor patches immediately, harden GPU configurations with ECC, revoke exposed secrets, and monitor for indicators tied to the threat actor campaigns outlined above.