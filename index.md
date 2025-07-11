# Exploitation Report

The past week has seen a surge in high-impact exploitation activity targeting enterprise infrastructure. Attackers are chaining remote-code-execution flaws in Wing FTP Server (CVE-2025-47812) and Citrix NetScaler ADC/Gateway (CVE-2025-5777) while a still-unnamed zero-day in Microsoft Exchange is being weaponized by a North-American APT against Chinese organizations. These exploits provide initial access that is quickly leveraged for full system compromise, data exfiltration, and ransomware deployment. Security teams should fast-track patching, tighten perimeter controls, and increase monitoring for suspicious process spawning and outbound C2 traffic originating from these products.

## Active Exploitation Details

### Wing FTP Server Remote Code Execution
- **Description**: A maximum-severity flaw in Wing FTP Server allows unauthenticated attackers to send a crafted network request that triggers arbitrary command execution under the privileges of the service account.  
- **Impact**: Full server takeover, lateral movement, credential theft, and deployment of ransomware payloads.  
- **Status**: Confirmed active exploitation in the wild; vendor patch released and should be applied immediately.  
- **CVE ID**: CVE-2025-47812  

### Citrix NetScaler ADC/Gateway Critical Vulnerability
- **Description**: A critical input-validation error in Citrix NetScaler ADC and Gateway permits remote, unauthenticated exploitation via specially crafted HTTP requests, leading to code execution or session hijacking.  
- **Impact**: Device compromise, network foothold, session token theft, and potential pivoting into internal resources protected by the appliance.  
- **Status**: Actively exploited; added to CISA KEV catalog. Citrix has issued fixed builds and mitigation guidance.  
- **CVE ID**: CVE-2025-5777  

### Microsoft Exchange Server Zero-Day
- **Description**: An undisclosed vulnerability in on-premises Microsoft Exchange is being exploited to gain privileged access through crafted email or HTTP requests, bypassing authentication and executing code on the server.  
- **Impact**: Complete mailbox theft, credential dumping, installation of web shells, and persistent network access.  
- **Status**: In-the-wild exploitation by a North-American APT; no official patch yet (zero-day). Security advisories recommend disabling exposed Exchange services and increasing anomaly detection.  

## Affected Systems and Products

- **Wing FTP Server**: All supported versions prior to the vendor’s emergency fix  
  - **Platform**: Windows, Linux, macOS server deployments  
- **Citrix NetScaler ADC & Gateway**: Supported 13.x, 14.x builds before July 2025 security updates  
  - **Platform**: Hardware appliances, VPX virtual appliances, and cloud instances  
- **Microsoft Exchange Server**: 2019, 2016 on-prem installations exposed to the Internet  
  - **Platform**: Windows Server environments hosting Exchange services  

## Attack Vectors and Techniques

- **Unauthenticated HTTP/FTP Request Injection**  
  - **Vector**: Crafted network packets exploit Wing FTP Server’s command-handling logic to run OS commands.  

- **Web Interface Exploitation & Session Hijacking**  
  - **Vector**: Malformed HTTP requests to Citrix NetScaler’s management or authentication endpoints bypass input validation and execute arbitrary code or steal session cookies.  

- **Email/OWA Zero-Day Chain**  
  - **Vector**: Custom exploits aimed at Exchange’s IIS modules deliver web shells and elevate privileges without valid credentials.  

## Threat Actor Activities

- **Pay2Key Ransomware (Iranian-backed)**  
  - **Campaign**: Relaunched RaaS platform offering 80 % profit share; observed leveraging compromised enterprise footholds (including Citrix appliances) to deploy double-extortion ransomware across EMEA targets.  

- **Unnamed North-American APT**  
  - **Campaign**: Targeted Chinese entities using the Exchange zero-day for espionage, mailbox exfiltration, and long-term persistence.  

- **Scattered Spider (Arrests Reported)**  
  - **Campaign**: Although four members were arrested, prior operations abused remote-access software and MFA fatigue to infiltrate retailers; continued monitoring advised for copycat activity.  

**Bold** emphasis, clear sectioning, and actionable detail have been provided for rapid situational awareness and response.