# Exploitation Report

During the last week, multiple high-impact campaigns have demonstrated that threat actors are successfully combining social-engineering, supply-chain abuse, and exploitation of mobile and edge-device weaknesses to achieve wide-scale compromise.  Scattered Spider continued its financially motivated intrusions against large retailers, Salt Typhoon expanded its espionage foothold into satellite communications, and Lazarus monetized compromised infrastructure in an $11 million crypto heist.  Parallel to these human-operated attacks, record-breaking 7.3 Tbps DDoS traffic and hundreds of weaponized GitHub repositories revealed how adversaries are abusing ubiquitous Internet services for both disruption and initial access.  Android users were also hit hard, with the “Godfather” and “AntiDot” malware strains exploiting virtualization and overlay capabilities to hijack banking sessions and NFC payments.  The activity shows a clear trend toward multi-vector operations that blend traditional vulnerability exploitation with identity compromise and supply-chain poisoning.

## Active Exploitation Details

### Scattered Spider Retail & Insurance Intrusions
- **Description**: Social-engineering and MFA-fatigue attacks used to seize privileged identities in Marks & Spencer, Co-op, and U.S. insurance firms (including Aflac), followed by data theft and ransomware deployment.  
- **Impact**: Operational disruption, theft of payment data and PII, and estimated losses up to $592 million.  
- **Status**: Ongoing; organizations are hardening identity providers and enforcing phishing-resistant MFA.

### Malicious GitHub Copycat Repositories
- **Description**: Threat actors uploaded dozens of repositories masquerading as popular projects, embedding backdoors and infostealers to compromise developer environments.  
- **Impact**: Supply-chain infection leading to credential theft and downstream compromise of any application compiled with the Trojanized code.  
- **Status**: Active; GitHub is removing reported repos but new ones continue to appear.

### Trojanized “Python Hacking Tools” Campaign
- **Description**: Over 200 fake GitHub repositories advertised as offensive security utilities but delivered malware via malicious setup.py and obfuscated binaries.  
- **Impact**: Remote code execution on developer machines, credential harvesting, and C2 beaconing.  
- **Status**: Live; researchers are issuing takedowns and IoC lists.

### Salt Typhoon (Volt Typhoon) Edge-Device Exploitation
- **Description**: Chinese state actor leveraged vulnerabilities in edge devices and living-off-the-land tooling to infiltrate Viasat’s satellite communications network.  
- **Impact**: Long-term espionage access into critical telecom infrastructure with potential to disrupt global connectivity.  
- **Status**: Confirmed compromise; hardening and firmware patching underway.

### Lazarus Group Exchange Breach
- **Description**: Compromise of hot wallets at BitoPro through exploitation of web-server and back-office weaknesses, followed by rapid laundering of $11 million in cryptocurrency.  
- **Impact**: Direct financial loss, reputational damage, and heightened regulatory scrutiny.  
- **Status**: Funds moved through mixing services; investigation in cooperation with global law-enforcement continues.

### Record 7.3 Tbps HTTP/2 DDoS
- **Description**: Botnet abused flaws in HTTP/2 connection management to launch the largest recorded distributed-denial-of-service attack (7.3 Tbps, 37.4 TB in 45 seconds) against a hosting provider.  
- **Impact**: Temporary service exhaustion and threat of collateral damage across shared infrastructure.  
- **Status**: Mitigated by Cloudflare; technique remains available to botnet operators.

### Android “Godfather” Virtualization Abuse
- **Description**: Malware spins up isolated virtual environments on devices, sideloads fraudulent banking apps, and intercepts transactions outside normal OS protections.  
- **Impact**: Account hijacking, unauthorized fund transfers, and credential theft.  
- **Status**: Active; no patch required on Android OS, but removal depends on AV/EDR detection updates.

### Android “AntiDot” Overlay & NFC Exploitation
- **Description**: Campaign uses overlay screens, virtualization fraud, and malicious NFC interactions to steal credentials from 3,775+ devices across 273 campaigns.  
- **Impact**: Theft of online-banking and contactless-payment data, device takeover.  
- **Status**: Ongoing; users advised to disable sideloading and review NFC settings.

### Qilin Ransomware “Call Lawyer” Pressureware
- **Description**: RaaS operators added an in-portal legal-counsel feature, instructing affiliates how to threaten victims with regulatory penalties for non-payment.  
- **Impact**: Increased ransom payments, legal intimidation tactics.  
- **Status**: Active; no universal decryptor available.

## Affected Systems and Products

- **Marks & Spencer / Co-op Retail Networks**: Identity providers (Okta, Azure AD), Windows and Linux servers  
- **Aflac & Other U.S. Insurers**: Corporate VPNs, email platforms, file shares  
- **GitHub Ecosystem**: Developers using cloned or typo-squatted repositories; all OS platforms  
- **Viasat**: Satellite ground stations, edge routers, network-management appliances  
- **BitoPro Cryptocurrency Exchange**: Hot wallet infrastructure, web back-office servers  
- **Hosting Provider (unnamed)**: Web, API, and HTTP/2 front-end clusters  
- **Android Devices**: All versions supporting virtualization features; Pixel models highlighted  
- **Global Banking Apps**: Applications running on compromised Android devices  
- **Organizations Targeted by Qilin**: VMware ESXi, Windows Server, and NAS devices  

## Attack Vectors and Techniques

- **SIM-Swap & MFA Fatigue**: Hijacking phone numbers and spamming push notifications to capture session tokens (Scattered Spider)  
- **Repository Impersonation / Typosquatting**: Publishing look-alike GitHub projects that install backdoors during build or install scripts  
- **Living-off-the-Land**: Using built-in Windows utilities (PowerShell, WMI) to avoid detection (Salt Typhoon)  
- **Edge-Device Exploitation**: Targeting unpatched routers and firewalls to gain foothold into telecom networks  
- **HTTP/2 Rapid-Reset Flooding**: Forcing servers to create and immediately cancel streams at scale, saturating bandwidth (7.3 Tbps DDoS)  
- **Android Virtualization Escape**: Running malicious apps in hidden containers to bypass OS security checks (Godfather)  
- **Overlay Phishing & NFC Skimming**: Displaying fake login screens and intercepting contactless transactions (AntiDot)  
- **Ransomware Double Extortion**: Encrypting data while threatening legal exposure via built-in counsel features (Qilin)  

## Threat Actor Activities

- **Scattered Spider (UNC3944/ALPHV affiliate)**  
  - **Campaign**: Coordinated April 2025 attacks on M&S, Co-op; concurrent U.S. insurance breaches. Targeting help-desk workflows, SMS gateways, and identity providers.

- **Salt Typhoon (Volt Typhoon)**  
  - **Campaign**: Stealth espionage against critical communications (Viasat) using edge-device vulnerabilities and credential theft.

- **Lazarus Group (North Korea)**  
  - **Campaign**: $11 million BitoPro theft; funds laundered through mixers, leveraging global crypto infrastructure.

- **Unknown GitHub Supply-Chain Operator(s)**  
  - **Campaign**: Hundreds of malicious repositories aiming at developers and gaming modders; ongoing creation of new projects.

- **Qilin Ransomware-as-a-Service**  
  - **Campaign**: New “Call Lawyer” feature to escalate pressure; victims across healthcare, manufacturing, and local government.

- **Botnet Operators (Unnamed)**  
  - **Campaign**: HTTP/2-based DDoS peak of 7.3 Tbps against hosting provider; botnet likely built from vulnerable IoT devices and compromised servers.

- **Android Malware Operators (“Godfather” & “AntiDot”)**  
  - **Campaign**: 273 distinct Android campaigns focusing on banking and payment theft, leveraging virtualization and overlay abuse.

---

This report aggregates the most significant exploitation activity observed in the referenced articles and highlights the vulnerabilities, affected systems, attacking techniques, and threat-actor operations currently posing the highest risk.