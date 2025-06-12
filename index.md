# Exploitation Report

Over the last week, threat actors have intensified exploitation of multiple high-impact flaws. The most critical activity centers on a Windows WebDAV remote-code-execution zero-day abused by the Stealth Falcon APT since March, and a newly weaponized vulnerability in the Wazuh security platform now fueling Mirai botnet growth. Researchers also disclosed “EchoLeak,” the first publicly documented zero-click AI flaw that leaks Microsoft 365 Copilot data without user interaction, while Google quietly fixed a weakness in its password-recovery workflow that allowed mass enumeration of users’ phone numbers. Parallel campaigns continue to brute-force Apache Tomcat management consoles, and ransomware and infostealer crews are actively leveraging open-source toolsets to accelerate compromise timelines.

## Active Exploitation Details

### Windows WebDAV Remote-Code-Execution Zero-Day
- **Description**: A previously unknown flaw in Windows WebDAV allows crafted network requests to trigger arbitrary code execution on targeted hosts.  
- **Impact**: Stealth Falcon uses the vulnerability to deploy malware on government and defense networks in Turkey, Qatar, Egypt, and the UAE. Successful exploitation grants full system compromise.  
- **Status**: Actively exploited since March 2025; Microsoft has not yet released a formal patch. Work-around guidance focuses on disabling the WebDAV service where possible.  

### Wazuh Security Platform Vulnerability Exploited by Mirai Botnets
- **Description**: Recently published Wazuh flaw (specific component not specified in the article) is being probed by Mirai botnets minutes after disclosure, highlighting shrinking time-to-exploit windows.  
- **Impact**: Remote attackers gain execution on vulnerable Wazuh deployments, allowing them to conscript servers into DDoS botnets and launch further lateral movement.  
- **Status**: Patch is available from Wazuh; exploitation in the wild is ongoing while many instances remain unpatched.  

### EchoLeak Zero-Click AI Vulnerability in Microsoft 365 Copilot
- **Description**: “EchoLeak” abuses system messages to silently extract the user’s Copilot context, enabling data exfiltration without clicks or social-engineering prompts.  
- **Impact**: Attackers can harvest sensitive emails, files, and chat content processed by Copilot directly from the AI interface.  
- **Status**: Publicly disclosed proof-of-concept; no evidence of widespread malicious use yet. Microsoft is investigating mitigations.  

### Google Account-Recovery Phone Number Enumeration Bug
- **Description**: A logic weakness on Google’s password-recovery page let attackers brute-force any account and confirm associated phone numbers.  
- **Impact**: Exposure of private contact information facilitates phishing, SIM-swapping, and targeted social-engineering attacks.  
- **Status**: Google has remediated the flaw following responsible disclosure; no user action required.  

### Weak Authentication Exposure on Apache Tomcat Manager
- **Description**: Hundreds of IP addresses are coordinating large-scale brute-force attempts against publicly exposed Tomcat Manager panels, exploiting default or weak credentials.  
- **Impact**: Successful logins allow attackers to deploy web shells, manipulate applications, or pivot deeper into corporate networks.  
- **Status**: Ongoing offensive activity; mitigation requires credential hardening and network segmentation.  

## Affected Systems and Products

- **Microsoft Windows (WebDAV Service)**  
  - **Platform**: Windows client and server editions with WebDAV enabled  

- **Wazuh Open-Source Security Platform**  
  - **Platform**: Linux servers running vulnerable Wazuh versions (all architectures)  

- **Microsoft 365 Copilot / Office 365 Tenants**  
  - **Platform**: Cloud-hosted Microsoft 365 environments with Copilot enabled  

- **Google Account Recovery Portal**  
  - **Platform**: Web service affecting all Google accounts prior to the recent fix  

- **Apache Tomcat (Manager Application)**  
  - **Platform**: Apache Tomcat servers exposing /manager/html on Internet-facing hosts  

## Attack Vectors and Techniques

- **WebDAV RCE Payloads**  
  - **Vector**: Malicious WebDAV requests delivered over HTTP(S) to vulnerable Windows services.  

- **Botnet Automated Exploit Modules**  
  - **Vector**: Mirai scripts scanning for Wazuh endpoints and pushing shell commands to join botnets.  

- **Zero-Click AI Prompt Injection (“EchoLeak”)**  
  - **Vector**: Crafted AI instructions embedded in emails or shared documents automatically processed by Copilot.  

- **Credential Enumeration via Recovery Workflow**  
  - **Vector**: Automated requests to Google’s password-reset API to confirm valid phone numbers.  

- **Brute-Force Login on Tomcat Manager**  
  - **Vector**: Distributed password spraying from 295+ unique IP addresses targeting weak/default credentials.  

- **Ultrasonic Covert Channel (“SmartAttack”)**  
  - **Vector**: Air-gapped data encoded as inaudible ultrasonic signals received by nearby smartwatches.  

- **TeamFiltration Framework Abuse**  
  - **Vector**: Phishing-obtained tokens used with open-source tool to enumerate and exfiltrate Microsoft Entra ID data.  

## Threat Actor Activities

- **Stealth Falcon (APT)**  
  - **Campaign**: Zero-day WebDAV exploitation delivering bespoke malware to Middle-East government and defense entities.  

- **Mirai Botnet Operators**  
  - **Campaign**: Rapid weaponization of the Wazuh flaw to expand DDoS botnet infrastructure worldwide.  

- **GreyNoise-Tracked Cluster**  
  - **Campaign**: Coordinated brute-force operation against Apache Tomcat Manager from 295 IPs, aiming at mass web-shell deployment.  

- **Former Black Basta Affiliates**  
  - **Campaign**: Microsoft Teams phishing combined with Python automation to maintain persistent enterprise access in 2025 attacks.  

- **Fog Ransomware Group**  
  - **Campaign**: Uses Syteca employee-monitoring software and open-source pentest tools for defense evasion and data exfiltration.  

- **Operation Secure (International Law Enforcement)**  
  - **Campaign**: Seized 117 C2 servers and 20,000 malicious IPs, arresting 32 individuals tied to infostealer-as-a-service rings.  

- **TeamFiltration Actors**  
  - **Campaign**: Targeted over 80,000 Microsoft Entra ID accounts, leveraging stolen credentials for large-scale account takeover.  

---

**Prepared by:** Cybersecurity Threat Hunting & Vulnerability Exploitation Analysis Team  
**Date:** 2025-06-XX