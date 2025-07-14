# Exploitation Report

The most critical exploitation activity observed this cycle centres on three server-side vulnerabilities already weaponised in the wild: a pre-authentication RCE in Wing FTP Server (CVE-2025-47812), the “Citrix Bleed 2” session hijacking flaw in NetScaler ADC/Gateway (CVE-2025-5777), and a critical SQL-injection-to-RCE chain in Fortinet FortiWeb (CVE-2025-25257). Active attacks against these products are progressing rapidly—Wing FTP exploitation began less than 24 hours after disclosure, while CitrixBleed 2 has been added to CISA’s KEV list with confirmed compromise of U.S. federal networks. Proof-of-concept (PoC) code for the FortiWeb flaw is public, accelerating mass-exploitation attempts. In parallel, new research exposes potentially devastating attack surfaces across eSIM management, Bluetooth stacks in 350 million cars, NVIDIA GPUs (RowHammer), Google Workspace’s Gemini summaries, and hundreds of Laravel applications with leaked APP_KEYs—underscoring a diverse and expanding exploitation landscape.

## Active Exploitation Details

### Wing FTP Server Remote Code Execution  
- **Description**: A maximum-severity vulnerability allowing unauthenticated attackers to send crafted requests that execute arbitrary commands with the privileges of the Wing FTP service.  
- **Impact**: Full server takeover, data theft, malware deployment, lateral movement.  
- **Status**: Confirmed in-the-wild exploitation; vendor has released patches and admins are urged to upgrade immediately.  
- **CVE ID**: CVE-2025-47812  

### Citrix NetScaler “CitrixBleed 2”  
- **Description**: Memory-handling flaw in NetScaler ADC and Gateway enabling extraction of session tokens and credentials over the network.  
- **Impact**: Session hijacking, post-authentication RCE, VPN gateway compromise, lateral intrusion into internal networks.  
- **Status**: Actively exploited; CISA added to KEV catalogue and mandated federal patching within 24 hours. Fixes available from Citrix.  
- **CVE ID**: CVE-2025-5777  

### Fortinet FortiWeb SQLi → RCE  
- **Description**: Pre-authentication SQL-injection in the management interface that can be escalated to remote code execution.  
- **Impact**: Complete device compromise, web-application firewall bypass, network pivoting.  
- **Status**: PoC exploit publicly released; Fortinet issued security update. Mass-scanning already observed.  
- **CVE ID**: CVE-2025-25257  

### Kigen eUICC / eSIM Weakness  
- **Description**: Logic flaw in eSIM profile download and authentication flow allowing SIM cloning and remote manipulation.  
- **Impact**: Device hijacking, persistent eavesdropping, fraudulent cellular billing, IoT botnet expansion.  
- **Status**: Research disclosure; no patch yet—mitigations limited to carrier-side monitoring.  

### PerfektBlue Bluetooth RCE Chain  
- **Description**: Four vulnerabilities in OpenSynergy BlueSDK enabling 1-click or proximity-based remote code execution via malformed Bluetooth packets.  
- **Impact**: Takeover of infotainment units, remote unlocking/start, compromise of industrial and medical devices.  
- **Status**: Vendors (Mercedes, Skoda, Volkswagen, among others) are releasing firmware updates; no confirmed exploitation but high risk with PoC demonstrations.  

### GPUHammer (RowHammer on NVIDIA GPUs)  
- **Description**: GPU memory disturbance attack flipping bits in GDDR6, degrading AI model accuracy or enabling data corruption.  
- **Impact**: Model poisoning, data integrity loss, potential privilege escalation when GPU memory is shared with the CPU.  
- **Status**: Lab demonstration; NVIDIA advises enabling system-level ECC and updating drivers.  

### Google Gemini Email Summary Prompt-Injection  
- **Description**: Prompt-injection flaw allowing attackers to embed malicious instructions that Gemini forwards to users as seemingly benign email summaries.  
- **Impact**: High-credibility phishing, credential harvesting, potential malware delivery without attachments.  
- **Status**: Google rolling out mitigations; abuse already spotted in phishing campaigns.  

### Laravel APP_KEY Remote Code Execution  
- **Description**: Leaked APP_KEYs on GitHub permit forging of signed cookies/session data, leading to deserialization and arbitrary code execution.  
- **Impact**: Full application compromise, database exfiltration, supply-chain attacks on dependent users.  
- **Status**: Hundreds of vulnerable deployments discovered; exploitation observed in opportunistic scanning.  

### OpenVSX Extension Repository Zero-Day  
- **Description**: Authentication bypass in OpenVSX allowed attackers to publish malicious Visual Studio Code extensions under any namespace.  
- **Impact**: Supply-chain takeover of developer environments, credential theft, code tampering.  
- **Status**: Patched; no confirmed mass exploitation but considered critical due to window of exposure.  

## Affected Systems and Products

- **Wing FTP Server (≤ version reported in advisory)**  
  - **Platform**: Windows, Linux, macOS server installations  

- **Citrix NetScaler ADC & Gateway (all builds prior to fixed release)**  
  - **Platform**: On-prem appliances, cloud images, VPX/MPX/SDX  

- **Fortinet FortiWeb (versions 7.x/6.x before 7.4.1, 6.3.24, 6.0.13)**  
  - **Platform**: Physical and virtual WAF appliances  

- **Kigen eUICC / eSIM cards (M2M & IoT form factors, multiple smartphone models)**  
  - **Platform**: Android, iOS, embedded Linux IoT devices  

- **OpenSynergy BlueSDK implementations in Mercedes, Skoda, Volkswagen, industrial/medical endpoints**  
  - **Platform**: Automotive ECUs, embedded RTOS, Android Automotive  

- **NVIDIA GPUs with GDDR6 memory (GeForce, RTX, data-centre A-series)**  
  - **Platform**: Windows, Linux workstations and servers with ECC disabled  

- **Google Workspace – Gemini AI Summarisation**  
  - **Platform**: Web Gmail, Android/iOS Gmail clients in Workspace domains  

- **Laravel Web Applications with exposed APP_KEYs**  
  - **Platform**: PHP 8.x on Linux/Windows hosts, containerised deployments  

- **OpenVSX Central Repository (prior to patch) / Extensions for Cursor & Windsurf IDEs**  
  - **Platform**: Developer machines (VS Code, VSCodium, Cursor, Windsurf)  

## Attack Vectors and Techniques

- **Unauthenticated HTTP RCE**  
  - **Vector**: Crafted POST/GET requests to vulnerable Wing FTP & FortiWeb endpoints.  

- **Session Token Bleeding**  
  - **Vector**: Memory scraping via malformed HTTP/HTTPS requests against NetScaler Gateway.  

- **Prompt Injection**  
  - **Vector**: Malicious text embedded in legitimate-looking emails to redirect Gemini summaries.  

- **Bluetooth L2CAP Packet Manipulation**  
  - **Vector**: Over-the-air 1-click pairing requests exploiting BlueSDK flaws (“PerfektBlue”).  

- **RowHammer Bit-Flipping**  
  - **Vector**: High-frequency GPU memory access patterns inducing electrical disturbance on adjacent cells.  

- **Signed Cookie Forgery**  
  - **Vector**: Use leaked Laravel APP_KEY to craft serialized payloads executed upon deserialization.  

- **Supply-Chain Extension Hijack**  
  - **Vector**: Abuse OpenVSX namespace control to distribute trojanised VS Code extensions.  

## Threat Actor Activities

- **Unknown Crimeware Groups (Wing FTP & FortiWeb)**  
  - **Campaign**: Mass-internet scanning followed by deployment of web-shells and coin-miners. Targets include SMBs and hosting providers.  

- **Unattributed APT/Crimeware (CitrixBleed 2)**  
  - **Campaign**: Credential/session harvesting against U.S. federal civilian agencies and critical infrastructure providers. Rapid exploitation post-patch release.  

- **Pay2Key Ransomware (Iran-linked)**  
  - **Campaign**: Re-launched RaaS platform offering 80 % affiliate share for attacks on U.S. and Israeli entities; likely to leverage fresh VPN/edge exploits such as CitrixBleed 2 for entry.  

- **Phishing Operators**  
  - **Campaign**: Using Gemini prompt-injection to craft convincing email summaries containing bogus “security notifications” with links to credential-harvesting pages.  

- **Automotive & IoT Researchers (PerfektBlue)**  
  - **Campaign**: Proof-of-concept releases driving manufacturer patch adoption; no malicious actor sightings yet but potential for car-theft crews to weaponise.  

- **GitHub Secret Hunters**  
  - **Campaign**: Automated scanning of public repos for Laravel APP_KEYs, followed by exploit to implant C2 beacons in affected web apps.  

- **Supply-Chain Attackers**  
  - **Campaign**: Attempted takeover of popular extension namespaces in OpenVSX to distribute spyware to developer workstations.  

