# Exploitation Report

During the past week, security researchers and government agencies have confirmed a surge in active exploitation of multiple high-impact vulnerabilities across enterprise appliances, developer ecosystems, IoT/automotive stacks, and AI tooling. Critical remote-code-execution (RCE) bugs in Wing FTP Server (CVE-2025-47812), Fortinet FortiWeb (CVE-2025-25257), and Citrix NetScaler ADC/Gateway (CVE-2025-5777) are being mass-scanned and weaponised within hours of public disclosure, prompting urgent patch mandates from CISA. Concurrently, attackers are abusing supply-chain weak points—backdooring Gravity Forms plugin installers, hijacking OpenVSX extensions, and leveraging leaked Laravel APP_KEYs—to obtain server-side execution. New attack surfaces have also emerged: “PerfektBlue” Bluetooth flaws allow one-click RCE against 350 million vehicles and one billion devices, GPUHammer undermines NVIDIA GDDR6 GPUs via RowHammer-style bit flips, and a Google Gemini logic flaw lets phishers smuggle malicious links inside trusted AI-generated email summaries. Organisations should prioritise patching, network segmentation, and threat-hunting for post-exploitation artefacts immediately.

---

## Active Exploitation Details

### Wing FTP Server Remote Code Execution  
- **Description**: A critical bug in Wing FTP Server allows unauthenticated attackers to execute arbitrary OS commands by sending crafted input to the server’s administration interface.  
- **Impact**: Full system takeover, file exfiltration, creation of back-door accounts, and lateral movement across the corporate network.  
- **Status**: Exploits observed in the wild less than 24 hours after technical details were published; vendor patch available.  
- **CVE ID**: CVE-2025-47812  

### Fortinet FortiWeb Pre-Auth SQL Injection → RCE  
- **Description**: Input validation flaws in FortiWeb’s web interface permit unauthenticated SQL injection, which can be pivoted into remote code execution.  
- **Impact**: Attackers gain root-level access to the underlying appliance, allowing web-shell deployment and traffic interception.  
- **Status**: Proof-of-concept exploit released publicly; active exploitation reported; patches issued in FortiWeb security update.  
- **CVE ID**: CVE-2025-25257  

### Citrix NetScaler “Citrix Bleed 2”  
- **Description**: Memory-handling weakness in NetScaler ADC/Gateway exposes session data that can be replayed to hijack authenticated sessions and execute arbitrary code.  
- **Impact**: Network gateway compromise, credential theft, and potential lateral spread to domain controllers and SaaS applications.  
- **Status**: Confirmed active exploitation; CISA added to KEV catalog with 24-hour patch deadline for U.S. federal networks.  
- **CVE ID**: CVE-2025-5777  

### Google Gemini for Workspace Email Summary Abuse  
- **Description**: Logic flaw lets attackers craft emails whose AI-generated “summaries” contain hidden malicious instructions or phishing URLs while the original message appears benign.  
- **Impact**: High-success phishing without attachments or obvious links, boosting click-through rates and credential theft.  
- **Status**: Technique observed in the wild; Google is rolling out mitigations server-side—no customer patch available.  

### “PerfektBlue” – OpenSynergy BlueSDK Bluetooth RCE Chain  
- **Description**: Four vulnerabilities in the BlueSDK stack enable a remote attacker within Bluetooth range to trigger heap corruption and execute code with the privileges of the Bluetooth daemon.  
- **Impact**: One-click takeover of infotainment units, telematics gateways, medical devices, industrial controllers, and smartphones; potential for physical safety impact in vehicles.  
- **Status**: No official patches from many downstream vendors; mitigations include disabling Bluetooth discovery and applying firmware updates when released.  

### GPUHammer (RowHammer Variant on NVIDIA GPUs)  
- **Description**: Rapid, repeated memory access patterns flip bits in GDDR6 VRAM, corrupting data used by AI models or sensitive computations.  
- **Impact**: Model poisoning, data integrity loss, potential privilege escalation when GPU memory is shared with CPUs.  
- **Status**: Demonstrated in laboratory conditions; NVIDIA advises enabling system-level ECC and memory refresh mitigations.  

### Laravel APP_KEY Leakage → Remote Code Execution  
- **Description**: Exposed APP_KEY values on public GitHub repos allow attackers to forge signed cookies and achieve code execution via Laravel’s encrypted session mechanism.  
- **Impact**: Complete compromise of more than 600 publicly reachable Laravel applications, data theft, and deployment of ransomware loaders.  
- **Status**: Active mass-exploitation reported; remediation requires key rotation and secret management hygiene.  

### McHire Chatbot Weak Password Exposure  
- **Description**: Administrative interface for McDonald’s recruiting chatbot protected by the password “123456,” enabling unauthorised access to 64 million application chats.  
- **Impact**: Exposure of PII, employment history, and potential social-engineering fodder.  
- **Status**: Password changed and access restricted, but data already scraped by researchers; unknown if threat actors accessed.  

### OpenVSX Extension Supply-Chain Zero-Day  
- **Description**: A flaw in OpenVSX’s namespace validation allowed attackers to publish malicious extensions under trusted namespaces, potentially auto-updating IDEs such as Cursor and Windsurf.  
- **Impact**: Execution of attacker-controlled code on millions of developer workstations, credential theft, and CI/CD compromise.  
- **Status**: Patched on the OpenVSX service; users must audit installed extensions for tampering.  

### WordPress Gravity Forms Backdoored Installers  
- **Description**: Threat actors compromised the developer’s website and injected PHP backdoors into manual installer ZIP files.  
- **Impact**: Immediate remote access to any site where the tampered plugin was installed; installation of additional malware.  
- **Status**: Malicious downloads pulled; security-signed builds re-issued.  

### eSIM Oracle Vulnerability Re-Exposure  
- **Description**: A six-year-old Oracle vulnerability in eSIM provisioning components enables SIM profile cloning, location tracking, and remote device takeover.  
- **Impact**: Covert surveillance or SIM swap attacks across millions of phones globally.  
- **Status**: No universal fix; mitigation relies on carrier-side updates and secure eSIM management frameworks.  

---

## Affected Systems and Products

- **Wing FTP Server**: v7.3.0 and earlier on Windows, Linux, macOS  
- **Fortinet FortiWeb**: Versions 7.0.x, 7.2.x, 7.4.x prior to July 2025 hotfixes  
- **Citrix NetScaler ADC/Gateway**: 14.1, 13.1, 13.0, 12.1 (all appliance form factors)  
- **Google Workspace (Gemini)**: Gmail with AI Email Summaries enabled (all browsers, mobile)  
- **OpenSynergy BlueSDK**: Automotive and IoT firmware using BlueSDK 5.x/6.x (Mercedes, Škoda, Volkswagen, medical & industrial devices)  
- **NVIDIA GPUs**: GDDR6-based consumer and data-center cards lacking ECC (RTX 30-series, A4000, etc.)  
- **Laravel Applications**: Any app with APP_KEY leaked in public repositories; predominantly Laravel 8/9  
- **McHire Chatbot Platform**: U.S. recruitment instances hosted by third-party SaaS provider  
- **OpenVSX Consumers**: Cursor IDE, Windsurf, Eclipse-based IDEs auto-syncing extensions  
- **WordPress Sites**: Deployments that manually downloaded Gravity Forms installers between compromise window dates  
- **eSIM-Enabled Phones**: Devices using vulnerable Oracle SIM provisioning software across multiple OEMs  

---

## Attack Vectors and Techniques

- **Unauthenticated HTTP Request → Command Injection**  
  - Vector: Crafted POST requests to Wing FTP admin endpoints.  

- **Pre-Auth SQL Injection**  
  - Vector: Malformed URL parameters to FortiWeb login handlers leading to OS-level shell.  

- **Session Token Replay / Memory Disclosure**  
  - Vector: Exploit CitrixBleed 2 to dump and replay valid session data over HTTPS.  

- **AI Summary Manipulation**  
  - Vector: Embed hidden prompts in email body that Gemini summariser surfaces as actionable text.  

- **Bluetooth Heap Overflow (“PerfektBlue”)**  
  - Vector: Malicious Bluetooth L2CAP packets broadcast within pairing range.  

- **RowHammer Bit-Flip (GPUHammer)**  
  - Vector: High-frequency GPU shader operations targeting adjacent VRAM rows.  

- **Laravel Cookie Forgery**  
  - Vector: Use leaked APP_KEY to craft signed cookies and hit application endpoints.  

- **Credential Stuffing on Unsecured Admin Portals**  
  - Vector: Default/weak password (“123456”) on McHire admin interface.  

- **Namespace Collision Supply-Chain Attack**  
  - Vector: Publish extension with same name as trusted one before original maintainer on OpenVSX.  

- **Backdoored Software Distribution**  
  - Vector: Replace legitimate Gravity Forms ZIP download with backdoor-laden file.  

- **eSIM Profile Manipulation**  
  - Vector: Exploit Oracle flaw during remote SIM provisioning over telecom network.  

---

## Threat Actor Activities

- **Unknown Criminal Clusters (Wing FTP & FortiWeb)**  
  - Campaign: Mass-scanning of exposed servers; quick weaponisation of PoC releases to deploy web-shells and crypto-miners.  

- **Iranian-Linked Pay2Key Ransomware Group**  
  - Campaign: Relaunched RaaS with 80 % affiliate profit share to incentivise attacks on U.S. and Israeli targets, likely to leverage newly compromised Citrix/FortiWeb footholds.  

- **Supply-Chain Intruders (Gravity Forms Case)**  
  - Campaign: Compromised developer infrastructure to embed PHP backdoors, aiming at widescale WordPress ecosystem compromise.  

- **Phishing Operators Exploiting Google Gemini**  
  - Campaign: High-volume credential-harvesting using AI-generated summaries to bypass traditional email filters.  

- **Vehicle-Focused Researchers/Proof-of-Concept Authors (PerfektBlue)**  
  - Campaign: Public disclosure of one-click Bluetooth RCE with demonstrations against Mercedes and Volkswagen models; advisory released, no patch yet.  

- **Academic Security Researchers (GPUHammer & OpenVSX)**  
  - Campaign: Authored technical papers and proofs showing feasibility of bit-flip attacks on GPUs and extension namespace hijacking; disclosures coordinated with vendors.  

---