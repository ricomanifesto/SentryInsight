# Exploitation Report

Recent security articles highlight ongoing exploitation of critical vulnerabilities, with attackers leveraging public exploit code, social engineering, and malicious packages to penetrate enterprise networks. Cisco has addressed serious flaws in its Identity Services Engine and Customer Collaboration Platform, while Qualcomm has patched three security flaws that malicious actors have already exploited in the wild. Threat groups continue to innovate their tactics with ransomware, vishing campaigns, supply chain attacks on open-source repositories, and phishing techniques targeting corporate authentication flows.

## Active Exploitation Details

### Cisco Identity Services Engine and Customer Collaboration Platform Vulnerabilities
- **Description**: Multiple vulnerabilities in Cisco’s Identity Services Engine (ISE) and Customer Collaboration Platform (CCP) that can be exploited using publicly available code. Attackers can potentially gain escalated privileges or unauthorized access.  
- **Impact**: Unauthenticated remote access, enabling lateral movement and compromise of sensitive data.  
- **Status**: Cisco has released patches to address these vulnerabilities.  
 
### Qualcomm Exploited Security Flaws
- **Description**: Three critical flaws in Qualcomm components used in various devices have been actively exploited to compromise systems, potentially granting attackers full control.  
- **Impact**: Device takeover, data exfiltration, and possible hardware-level compromise.  
- **Status**: Qualcomm has issued fixes, but end users remain at risk until device manufacturers apply the updates.  

## Affected Systems and Products

- **Cisco Identity Services Engine (ISE) and Customer Collaboration Platform (CCP)**: Vulnerable deployments prior to the patched versions  
- **Qualcomm-based Devices**: Smartphones and other hardware reliant on Qualcomm chipsets or components  
- **Asus Routers**: Multiple models compromised as part of emerging botnet operations  
- **HPE StoreOnce**: Subject to recently addressed vulnerabilities that could allow authentication bypass  
- **Salesforce Implementations**: Potentially targeted by vishing and credential-harvesting campaigns  
- **Ruby/PyPI/npm Package Users**: At risk from malicious supply chain packages designed to exfiltrate sensitive data  
- **Android Devices**: Impacted by emerging malware such as “Crocodilus” targeting users globally  
- **Kerberos-Based Environments**: Prone to AS-REP roasting attacks if best practices and strong passwords are not enforced  

## Attack Vectors and Techniques

- **Malicious Open-Source Packages**: Attackers upload trojanized libraries to PyPI, npm, and RubyGems to exfiltrate data or compromise systems.  
  • **Vector**: Users install the packages believing them to be legitimate, enabling backdoors and malware execution.

- **Device Code Phishing**: Exploits trusted authentication flows (e.g., Microsoft Teams, IoT logins) to bypass MFA by tricking users into providing codes.  
  • **Vector**: Malicious links or prompts lure users into entering their authentication codes, granting attackers unauthorized access.

- **Vishing (Voice Phishing) Campaigns**: Threat actors impersonate legitimate services (e.g., Salesforce, financial institutions) to steal user credentials or data.  
  • **Vector**: Phone calls or voice messages urging victims to install malicious apps or provide personal information.

- **Replay Attacks on Deepfake Detection**: Criminals re-record deepfake audio or video to bypass AI detection systems.  
  • **Vector**: Authentic acoustic environment recordings that confuse standard deepfake detection models.

- **Kerberos AS-REP Roasting**: Exploits weak encryption or misconfigurations in Kerberos, allowing attackers to crack hashes offline.  
  • **Vector**: An attacker requests a Kerberos ticket for accounts marked “Do not require pre-authentication,” then brute-forces the returned hashed credentials.

- **Chaos RAT Deployment**: Uses fake network tool installers on Windows and Linux to deliver a remote access trojan.  
  • **Vector**: Users tricked into downloading disguised software that executes malicious payloads.

- **Botnet Infiltration of Routers**: Threat actors compromise routers (e.g., Asus models) to build large-scale botnets.  
  • **Vector**: Exploitation of insecure configurations or outdated firmware to gain persistent control over the device.

- **Backdoored GitHub Code**: Attackers insert hidden backdoors into commonly sought-after exploits, bots, or game cheats on GitHub, targeting other hackers or curious users.  
  • **Vector**: Cloned source code with malicious modifications that execute remote commands upon installation.

## Threat Actor Activities

- **Actor/Group**: UNC6040  
  - **Campaign**: Vishing attacks targeting Salesforce apps, tricking users into installing fake data loaders to exfiltrate information.

- **Actor/Group**: Play Ransomware  
  - **Campaign**: Large-scale ransomware attacks breaching approximately 900 victims worldwide, including critical service providers.

- **Actor/Group**: Hacker Targeting 5,000 Hosting Accounts  
  - **Campaign**: Illegally accessed hosting accounts to mine cryptocurrency, causing millions in damages.

- **Actor/Group**: ShinyHunters (Impersonators)  
  - **Campaign**: Purporting to be “ShinyHunters” to extort data from organizations’ Salesforce instances via social engineering.

- **Actor/Group**: Developer of Malicious Supply Chain Packages  
  - **Campaign**: Creating trojanized libraries on npm, PyPI, and RubyGems to compromise user systems and steal crypto, credentials, or source code.

- **Actor/Group**: “Crocodilus” Malware Operators  
  - **Campaign**: Targeting Android devices to steal personal data, initially in Turkey and now expanding globally.

- **Actor/Group**: Ukrainian GUR Offensive  
  - **Campaign**: Claimed hack of Tupolev, a major Russian aerospace and defense entity, potentially disrupting strategic bomber development.

- **Actor/Group**: Botnet Operators Compromising Asus Routers  
  - **Campaign**: Seizing control of thousands of consumer routers, possibly building a botnet for future large-scale attacks.