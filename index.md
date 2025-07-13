# Exploitation Report

Since the start of July 2025, defenders have been confronted with a wave of live exploitation campaigns that cut across network appliances, file-transfer servers, web frameworks, Bluetooth stacks, and even graphics cards. The most urgent issues are the critical remote-code-execution flaws in Citrix NetScaler (Citrix Bleed 2), Wing FTP Server, and Fortinet FortiWeb, all of which are already weaponised in the wild and have proof-of-concept (PoC) code circulating publicly. At the same time, researchers have demonstrated new hardware-level attacks such as GPUHammer against NVIDIA GDDR6 GPUs and PerfektBlue against automotive Bluetooth implementations, underscoring that attackers are probing ever-lower layers of the stack. Supply-chain compromises (Gravity Forms) and misconfigurations (Laravel APP_KEY leakage, McHire’s “123456” password) round out a threat landscape that is both technically diverse and highly active.

## Active Exploitation Details

### Citrix Bleed 2 – NetScaler ADC & Gateway Information Disclosure/RCE
- **Description**: A critical flaw in Citrix NetScaler ADC and Gateway allows unauthenticated attackers to hijack sessions and potentially execute arbitrary code or harvest credentials.  
- **Impact**: Enables complete takeover of VPN gateways, lateral movement, and data exfiltration across enterprise environments.  
- **Status**: Confirmed in active exploitation; CISA has added the bug to the KEV catalogue and ordered U.S. federal agencies to patch within 24 hours. Fixed builds are already available from Citrix.  
- **CVE ID**: CVE-2025-5777  

### Wing FTP Server Remote Code Execution
- **Description**: A maximum-severity vulnerability permits remote, unauthenticated code execution on Wing FTP Server by sending a crafted request that abuses the server’s request-handling logic.  
- **Impact**: Full system compromise, data theft, and deployment of ransomware or cryptominers.  
- **Status**: Exploitation observed one day after technical details were published; security firm Huntress is tracking multiple live intrusions. Patches are available from Wing FTP.  
- **CVE ID**: CVE-2025-47812  

### Fortinet FortiWeb Pre-Auth SQL Injection to RCE
- **Description**: A pre-authentication SQL injection flaw in the FortiWeb management interface can be chained to execute system commands as root.  
- **Impact**: Allows attackers to bypass authentication, dump databases, and run arbitrary code on web-application-firewall appliances that often sit in front of business-critical portals.  
- **Status**: Multiple public PoCs released; Fortinet has shipped hotfixes and full firmware updates. Mass scanning activity has begun.  
- **CVE ID**: CVE-2025-25257  

### GPUHammer – RowHammer Variant on NVIDIA GDDR6 GPUs
- **Description**: Researchers flipped bits within GDDR6 memory by rapidly activating adjacent rows (“RowHammer”), degrading AI model accuracy and opening the door to data corruption or privilege escalation.  
- **Impact**: Integrity attacks on AI workloads, potential hypervisor escape in GPU-accelerated cloud instances, and tampering with confidential computations.  
- **Status**: Lab-demonstrated but practical; NVIDIA urges customers to enable system-level ECC and firmware mitigations.  

### PerfektBlue Bluetooth RCE Chain
- **Description**: Four vulnerabilities in OpenSynergy’s BlueSDK allow 1-click remote code execution over Bluetooth on cars (Mercedes, Volkswagen, Škoda) and on industrial, medical, and consumer devices using the same stack.  
- **Impact**: Attacker can remotely execute code, disable safety features, and pivot into vehicular CAN networks or IoT back-ends.  
- **Status**: No patches shipped yet for many affected vendors; proof-of-concept exploits demonstrated at a security conference, raising likelihood of imminent in-the-wild attacks.  

### Laravel APP_KEY Leakage Leading to RCE
- **Description**: Hundreds of Laravel projects on GitHub inadvertently exposed their APP_KEY, enabling attackers to craft signed payloads that trigger PHP object deserialization and remote code execution.  
- **Impact**: Full takeover of exposed web applications, data theft, and lateral movement into associated cloud resources.  
- **Status**: Active reconnaissance scripts are harvesting keys; developers must rotate keys and regenerate application secrets.  

### McHire Chatbot Default Password Exposure
- **Description**: The McHire recruitment chatbot was protected with the trivial password “123456,” allowing unauthenticated access to backend chat logs and personal data for 64 million job applicants.  
- **Impact**: Large-scale PII exposure, compliance violations, and potential follow-on phishing attacks.  
- **Status**: Vulnerability discovered by researchers; McDonald’s has reset credentials and is notifying impacted users.  

### Gravity Forms Supply-Chain Backdoor
- **Description**: The developer portal for the Gravity Forms WordPress plugin was breached, and backdoored ZIP packages were distributed to customers performing manual installs.  
- **Impact**: Web-server compromise, credential theft, and the planting of additional malware on high-traffic WordPress sites.  
- **Status**: Malicious files have been withdrawn; users are urged to verify checksums and reinstall from clean builds.  

## Affected Systems and Products

- **Citrix NetScaler ADC & Gateway**: Multiple firmware branches prior to patched builds (13.1, 13.0, 12.1)  
- **Wing FTP Server**: Windows, Linux, and macOS builds before the July 2025 security update  
- **Fortinet FortiWeb**: Versions 7.4.1 and earlier, 7.2.3 and earlier, 7.0.7 and earlier  
- **NVIDIA GPUs**: All GDDR6-based consumer and data-center cards where ECC is disabled  
- **Vehicles Using BlueSDK**: Mercedes-Benz, Volkswagen, Škoda models 2020–2025; industrial/medical devices using OpenSynergy BlueSDK v3.x  
- **Laravel Applications**: Any deployment that has leaked its `.env` file or APP_KEY to public repositories  
- **McHire Chatbot Platform**: U.S. job-application portal across McDonald’s franchise network  
- **WordPress Gravity Forms Plugin**: Manual ZIP installs downloaded between 1–4 July 2025  

## Attack Vectors and Techniques

- **Pre-Auth SQL Injection**: Direct injection of SQL commands to achieve code execution on FortiWeb appliances.  
- **Session Token Hijacking**: Theft and replay of authentication tokens against NetScaler gateways (Citrix Bleed 2).  
- **Crafted Protocol Payload**: Malformed Wing FTP requests that trigger unsafe deserialization leading to RCE.  
- **RowHammer Bit Flips (GPUHammer)**: High-frequency row activations on GDDR6 memory to corrupt data and models.  
- **Bluetooth L2CAP Exploitation (PerfektBlue)**: Single-click delivery of malicious L2CAP packets to trigger stack overflow.  
- **Signed Payload Forgery**: Using leaked Laravel APP_KEY to sign malicious encrypted strings for deserialization attacks.  
- **Default/Weak Credentials**: Abuse of the “123456” password to access McHire backend services.  
- **Supply-Chain Replacement**: Distribution of backdoored Gravity Forms plugin packages from a compromised developer portal.  

## Threat Actor Activities

- **Unknown Exploit Kits**  
  - **Campaign**: Mass scanning and exploitation of Wing FTP Server and FortiWeb appliances immediately after PoC release. Targets include healthcare and education sectors.

- **Unattributed APT Targeting Citrix Appliances**  
  - **Campaign**: Live exploitation of Citrix Bleed 2 to obtain footholds inside large enterprise networks, confirmed by CISA telemetry.

- **Pay2Key Ransomware-as-a-Service (Iranian-linked)**  
  - **Campaign**: Relaunched with an 80 % revenue share for affiliates attacking U.S. and Israeli entities, leveraging any fresh RCE for initial access.

- **Gravity Forms Supply-Chain Actor**  
  - **Campaign**: Compromised plugin distribution infrastructure to implant PHP backdoors on thousands of WordPress sites.

- **Scattered Spider**  
  - **Activity**: Four suspected members arrested in the UK; group previously relied on social-engineering and identity-provider exploitation for high-profile breaches.

- **Automotive-Focused Researchers (PerfektBlue)**  
  - **Campaign**: Public disclosure of Bluetooth RCE flaws, sparking interest among both white-hat and criminal actors poised to weaponise the research.

