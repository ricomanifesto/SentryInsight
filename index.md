# Exploitation Report

Threat hunters continue to observe a sharp uptick in high-impact exploitation against edge infrastructure and file-transfer software. The most pressing activity centers on two critical flaws: “CitrixBleed 2” in Citrix NetScaler ADC/Gateway and a command-injection bug in Wing FTP Server. Both vulnerabilities are under active attack, with government advisories and real-world post-exploitation telemetry confirming compromise attempts. Successful exploitation enables unauthenticated attackers to hijack VPN sessions, execute arbitrary code, and pivot deeper into corporate networks, making rapid patching imperative.

## Active Exploitation Details

### Citrix NetScaler ADC/Gateway – “CitrixBleed 2”
- **Description**: A memory-handling flaw that allows crafted requests to read sensitive heap data from the VPN service, exposing valid session tokens and credentials.  
- **Impact**: Enables session hijacking, authentication bypass, potential lateral movement, and data exfiltration without valid credentials.  
- **Status**: Confirmed widespread exploitation; CISA added the flaw to its KEV catalog and ordered U.S. federal agencies to patch within 24 hours. Vendor fixes are available in the latest NetScaler builds.  
- **CVE ID**: CVE-2025-5777  

### Wing FTP Server Remote Command Injection
- **Description**: An input-validation failure in the server’s administration interface allows attackers to inject operating-system commands via SQL-style payloads sent in unauthenticated HTTP requests.  
- **Impact**: Full remote code execution under the privileges of the Wing FTP service account, leading to complete server takeover and potential malware deployment.  
- **Status**: Actively exploited in the wild; security firm Huntress reported real-time intrusions. A patched release is available from WingFTP.  
- **CVE ID**: CVE-2025-47812  

## Affected Systems and Products

- **Citrix NetScaler ADC & Gateway**  
  - **Platform**: Physical and virtual appliances running vulnerable firmware prior to the latest 14.1, 13.1, and 13.0 builds.  

- **Wing FTP Server**  
  - **Platform**: Windows, Linux, macOS, and Solaris builds prior to the vendor’s fixed version (7.4.x).  

## Attack Vectors and Techniques

- **Session Token Memory-Leak (CitrixBleed 2)**  
  - **Vector**: Malformed HTTP/HTTPS requests to the VPN endpoint extract heap memory, revealing valid authentication artifacts.  

- **Unauthenticated Command Injection (Wing FTP)**  
  - **Vector**: Direct HTTP POST/GET requests with crafted SQL/OS-command payloads to administrative CGI endpoints.  

- **Rowhammer Bit-Flip Attacks**  
  - **Vector**: Rapid, repeated memory accesses on GDDR6 GPUs to induce bit flips and corrupt data structures, potentially leading to privilege escalation. NVIDIA advises enabling system-level ECC as mitigation.  

- **Supply-Chain Extension Takeover (OpenVSX Zero-Day)**  
  - **Vector**: Namespace-collision in the OpenVSX registry allowed attackers to publish malicious Visual Studio Code extensions under trusted names, hijacking developer environments before the flaw was patched.  

## Threat Actor Activities

- **Unknown Intrusion Sets (CitrixBleed 2)**  
  - **Campaign**: Broad, opportunistic scanning of internet-exposed NetScaler appliances; observed targeting of U.S. federal networks and large enterprises.  

- **Unattributed Actors (Wing FTP)**  
  - **Campaign**: Rapid weaponization of proof-of-concept code; attackers deploy web shells and remote management tools immediately after exploitation.  

- **Pay2Key Ransomware (Iran-Backed)**  
  - **Campaign**: Newly relaunched RaaS offering 80% revenue share; focuses on double-extortion attacks, likely to integrate fresh exploits such as CitrixBleed 2 for initial access.  

- **Scattered Spider (Arrest Action)**  
  - **Campaign**: Four suspected members arrested in the U.K. following high-profile retail and airline breaches; group previously leveraged VPN and help-desk social-engineering for access and may have exploited edge appliance flaws similar to CitrixBleed variants.  

**Bold, immediate patching of Citrix NetScaler and Wing FTP remains the highest priority to blunt ongoing exploitation campaigns.**