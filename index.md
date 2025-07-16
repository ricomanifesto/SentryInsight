# Exploitation Report

During the past week, threat actors have intensified exploitation of firmware- and AI-related weaknesses while broadening supply-chain attacks and novel malware delivery techniques. High-impact activity includes a Secure Boot–bypassing flaw in Gigabyte UEFI firmware that enables stealth bootkits, a prompt-injection bug in Google’s Gemini AI assistant that lets adversaries craft invisible but malicious “security alerts,” and a North-Korean campaign seeding 67 malicious npm packages carrying the new XORIndex loader. Ransomware operators are also weaponising a “FileFix” document-repair ruse to covertly drop PHP-based Interlock RAT payloads, and the Konfety Android malware is abusing malformed APKs to sidestep mobile defences. A state-backed group is simultaneously leveraging AWS Lambda for covert command-and-control via the HazyBeacon backdoor. The combination of firmware compromise, AI manipulation, cloud-based C2, and supply-chain poisoning underscores an urgent need for rapid patching, firmware updates, and heightened developer-ecosystem hygiene.

## Active Exploitation Details

### Gigabyte UEFI Secure Boot Bypass
- **Description**: Multiple Gigabyte motherboard models ship with UEFI firmware vulnerabilities that allow unsigned code execution during the boot sequence, bypassing Secure Boot protections.  
- **Impact**: Attackers can implant persistent bootkits that survive OS reinstallation, remain invisible to endpoint security, and gain kernel-level control.  
- **Status**: Exploitation observed in the wild. Gigabyte has issued firmware updates for several models, but many systems remain unpatched.  

### Google Gemini Invisible-Prompt Injection
- **Description**: A prompt-injection flaw in Google’s Gemini AI assistant enables adversaries to embed invisible (e.g., zero-width or white-on-white) instructions that masquerade as legitimate Google Security notifications.  
- **Impact**: Users can be tricked into following malicious links, divulging credentials, or executing unintended actions while believing the prompts originate from Google.  
- **Status**: Actively exploited in phishing campaigns. Google is rolling out mitigations; users should update Gemini-enabled applications and validate any security prompts.  

### npm Package Poisoning – XORIndex Loader
- **Description**: North Korean actors uploaded 67 trojanised packages to the Node Package Manager registry. Installing these packages deploys the XORIndex malware loader, which fetches follow-on payloads.  
- **Impact**: Compromised developer environments, credential theft, and potential lateral movement into corporate CI/CD pipelines.  
- **Status**: Packages were live and being downloaded before discovery; npm has begun removal, but mirrors and forks persist.  

### FileFix Document-Repair Attack (Interlock RAT)
- **Description**: The Interlock ransomware group adopted a “FileFix” technique that embeds malicious code into ostensibly repaired documents or archives. Opening the file executes a PHP-based Interlock RAT variant.  
- **Impact**: Initial foothold, remote control, and staging for encryption or double-extortion operations.  
- **Status**: Ongoing campaigns against multiple industries. No vendor patch (social-engineering vector); defensive controls and content disarm recommended.  

### Malformed-APK Evasion – Konfety Android Malware
- **Description**: Konfety now ships APKs with a deliberately malformed ZIP structure and layered obfuscation, circumventing static and dynamic analysis engines on Android security products.  
- **Impact**: Silent installation of spyware capable of SMS interception, keylogging, and exfiltration of device data.  
- **Status**: Active distribution through third-party app stores and smishing lures. Google Play services unaffected, but Android users side-loading apps are at risk.  

### HazyBeacon Cloud-Based Backdoor
- **Description**: A previously undocumented Windows backdoor (“HazyBeacon”) uses AWS Lambda, API Gateway, and S3 for covert C2 and data exfiltration, blending with legitimate cloud traffic.  
- **Impact**: Long-term espionage within Southeast-Asian government networks, enabling file theft and remote command execution without raising perimeter-filter alarms.  
- **Status**: Campaign ongoing; no specific software patch—mitigations focus on cloud traffic anomaly detection and IAM hardening.  

## Affected Systems and Products

- **Gigabyte Motherboards (multiple Z390, X570, B550, and newer models)**  
  - **Platform**: Windows/Linux systems relying on affected UEFI firmware  
- **Google Gemini AI Assistant (Workspace, Gmail, Chrome, Android integrations)**  
  - **Platform**: Web and mobile clients using Gemini Advanced or trial features  
- **Node.js Development Environments (npm registry consumers)**  
  - **Platform**: Cross-platform developer workstations and CI/CD pipelines  
- **Microsoft Windows Endpoints targeted by Interlock RAT**  
  - **Platform**: Office documents, PHP runtimes where FileFix payloads execute  
- **Android Devices (Android 10-14, side-loaded apps)**  
  - **Platform**: Mobile phones and tablets permitting installation from unknown sources  
- **Government and Enterprise Windows Hosts communicating via AWS**  
  - **Platform**: Environments where outbound AWS Lambda traffic is allowed  

## Attack Vectors and Techniques

- **Prompt Injection (Invisible Text)**  
  - **Vector**: Zero-width / white-on-white characters in Gemini dialogs to hide attacker commands.  
- **UEFI Bootkit Implantation**  
  - **Vector**: Flashing malicious firmware or exploiting vulnerable Gigabyte update mechanisms.  
- **Supply-Chain Poisoning (npm)**  
  - **Vector**: Publishing trojanised packages with familiar names to trick developers into installation.  
- **FileFix Document Abuse**  
  - **Vector**: Disguised “fixed” documents or archives that auto-execute embedded RAT code.  
- **Malformed ZIP/APK Packaging**  
  - **Vector**: Corrupt ZIP central directory entries that bypass antivirus and static scanners.  
- **Cloud-Native C2 via AWS Lambda**  
  - **Vector**: Leveraging legitimate AWS services (Lambda invoke, S3 PUT/GET) for encrypted C2 traffic.  

## Threat Actor Activities

- **North Korean Cluster (XORIndex Campaign)**  
  - **Campaign**: Continues “Contagious Interview” operations by flooding npm with 67 malicious packages, aiming at software-development supply chains.  
- **Interlock Ransomware Group**  
  - **Campaign**: Deploying new PHP-based RAT via FileFix to expand foothold before encryption; targeting finance, manufacturing, and healthcare.  
- **State-Backed Actor (HazyBeacon)**  
  - **Campaign**: Intelligence-gathering against Southeast-Asian governmental organisations, hiding C2 inside AWS cloud channels.  
- **Diskstation Ransomware Gang (Romania)**  
  - **Campaign**: Previously compromised NAS devices across Lombardy; recently disrupted by law enforcement, but tooling remains in the wild.  
- **AsyncRAT Ecosystem (Multiple Forks)**  
  - **Campaign**: Open-source variants proliferating on GitHub, enabling commodity attackers to build customised payloads for phishing and RAT delivery.  

