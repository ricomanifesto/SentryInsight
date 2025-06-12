# Exploitation Report

Over the past week, threat hunters observed a surge in high-impact exploitation activity spanning Microsoft Windows, Microsoft 365 Copilot, and identity-management infrastructure.  The most serious developments include a zero-day remote-code-execution flaw in Windows WebDAV that Stealth Falcon has weaponized against Middle-Eastern defense and government organizations, a newly disclosed zero-click “EchoLeak” vulnerability that can silently extract sensitive content from Microsoft 365 Copilot, and an actively abused Secure Boot bypass leveraged by bootkit malware.  Parallel brute-force campaigns are hammering Microsoft Entra ID and Apache Tomcat portals, while ransomware and infostealer crews continue to mix open-source and living-off-the-land tools for post-exploitation.  Organizations should prioritize patching, deploy compensating controls, and harden external authentication surfaces immediately.

## Active Exploitation Details

### Windows WebDAV Remote-Code-Execution Zero-Day
- **Description**: A previously unknown flaw in the WebDAV service of Windows allows crafted requests to trigger remote code execution with SYSTEM privileges.  
- **Impact**: Full takeover of the target host, enabling malware deployment, persistence, and lateral movement.  
- **Status**: Actively exploited in the wild since March 2025 by Stealth Falcon; no official patch released at publication time, mitigations limited to disabling WebDAV or blocking affected ports.  

### EchoLeak Zero-Click Data-Exfiltration Vulnerability (Microsoft 365 Copilot)
- **Description**: “EchoLeak” abuses the Copilot context-sharing mechanism to siphon conversation data without any end-user interaction.  Malicious prompts or messages silently trigger the leak.  
- **Impact**: Disclosure of privileged corporate data processed by Copilot—including emails, documents, and chat history—potentially leading to espionage or compliance violations.  
- **Status**: Newly uncovered zero-click flaw; proof-of-concept code demonstrated, no patch yet available.  Microsoft is investigating and recommends restricting Copilot access until remediated.  

### Windows Secure Boot Bypass Exploited by Bootkit Malware
- **Description**: A boot-time vulnerability in Windows Boot Manager permits unsigned or maliciously signed EFI components to load, undermining Secure Boot protections.  
- **Impact**: Attackers install persistent bootkits that survive OS reinstalls, disable security tools, and provide deep system control.  
- **Status**: Actively exploited by in-the-wild malware; Microsoft has shipped an emergency update and updated revocation lists.  Systems must apply the patch and enable the new Secure Boot policy.  

## Affected Systems and Products

- **Microsoft Windows (WebDAV Service)**  
  - **Platform**: Windows 10/11 and Windows Server versions with WebDAV enabled.

- **Microsoft 365 Copilot**  
  - **Platform**: Cloud-based Microsoft 365 tenants using Copilot AI assistance.

- **Windows Boot Manager / Secure Boot**  
  - **Platform**: All Secure-Boot-capable Windows PCs and servers prior to the latest emergency update.

- **Microsoft Entra ID (formerly Azure AD)**  
  - **Platform**: Cloud identity platform targeted by large-scale password-spraying.

- **Apache Tomcat Manager**  
  - **Platform**: Internet-exposed Tomcat servers with default or weak credentials.

## Attack Vectors and Techniques

- **Password Spraying Against Entra ID**  
  - **Vector**: TeamFiltration framework automates low-and-slow authentication attempts against over 80,000 accounts, evading lockout thresholds.

- **WebDAV Zero-Day Exploitation**  
  - **Vector**: Malicious documents or network requests trigger RCE through vulnerable WebDAV parsing.

- **Zero-Click AI Data Exfiltration (EchoLeak)**  
  - **Vector**: Crafted Copilot prompt embedded in emails or Teams chats automatically releases contextual data.

- **Secure Boot Bypass / Bootkit Implantation**  
  - **Vector**: Malicious EFI loader sidesteps signature checks, installing a persistent bootkit before the OS initializes.

- **Brute-Force Attacks on Apache Tomcat**  
  - **Vector**: Distributed botnet enumerates default credentials against /manager/html endpoints from hundreds of IP addresses.

- **Ultrasonic Smartwatch Exfiltration (SmartAttack)**  
  - **Vector**: Compromised workstation’s speaker emits inaudible ultrasonic signals captured by nearby smartwatches to steal data from air-gapped systems.

## Threat Actor Activities

- **Stealth Falcon**  
  - **Campaign**: Leveraging the WebDAV zero-day to deploy custom backdoors and credential-dumping tools against defense ministries in Turkey, Qatar, Egypt, and Jordan.  

- **TeamFiltration Operators**  
  - **Campaign**: Global account-takeover operation targeting Microsoft Entra ID tenants across multiple verticals; aims to harvest email and SharePoint data post-compromise.  

- **Former Black Basta Affiliates**  
  - **Campaign**: 2025 phishing wave using Microsoft Teams lures and Python automation to maintain persistent presence and stage ransomware.  

- **Fog Ransomware Group**  
  - **Campaign**: Combines open-source pentest utilities with legitimate employee-monitoring software (Syteca) to escalate privileges and exfiltrate files before encryption.  

- **Unidentified Botnet (Tomcat Brute-Force)**  
  - **Campaign**: Large-scale distributed authentication attacks on Apache Tomcat management panels; objective likely web-shell deployment for later monetization.  

- **Global Infostealer Networks (Operation Secure)**  
  - **Campaign**: Recently disrupted infrastructure previously used for phishing, BEC, and credential theft; 117 C2 servers seized and 32 suspects arrested.  

---

Organizations should immediately deploy Microsoft’s Secure Boot update, disable or restrict WebDAV where possible, audit Copilot usage, enforce strong MFA across Entra ID, and harden exposed Tomcat interfaces to reduce current threat exposure.