# Exploitation Report

Over the past week, threat actors have intensified exploitation of enterprise-grade remote-access and business-critical software. Token-theft attacks against **Citrix NetScaler (dubbed “Citrix Bleed 2”)** and in-the-wild abuse of **ConnectWise ScreenConnect** authentication-bypass flaws continue to provide direct access to internal networks. Simultaneously, newly disclosed weaknesses in **SAP GUI** expose sensitive ERP data, while a dangerous **access-control gap in Microsoft Entra ID** is already being weaponized for privilege escalation. Supply-chain compromises remain prominent: a trojanized **SonicWall NetExtender** installer is circulating, and North-Korea-linked operators are again seeding malicious **npm** packages. The China-nexus “LapDogs” operation is also expanding its ORB relay mesh through backdoored SOHO devices, underscoring the breadth of current exploitation activity.

---

## Active Exploitation Details

### Citrix Bleed 2 Token-Theft Vulnerability  
- **Description**: Memory-scraping flaw in Citrix NetScaler ADC and Gateway appliances that leaks session tokens during client requests, enabling hijacking of authenticated sessions.  
- **Impact**: Allows unauthenticated attackers to impersonate legitimate users (including administrators) and pivot laterally.  
- **Status**: Actively exploited. Citrix has released patches and urges immediate appliance upgrades and token revocation.  

### SAP GUI Input-History XOR Flaws  
- **Description**: Two vulnerabilities in SAP GUI for Windows and Java where the “input history” feature stores user entries with weak XOR obfuscation, enabling local or remote attackers to decrypt and exfiltrate credentials or sensitive ERP data.  
- **Impact**: Theft of usernames, passwords, and confidential business information, potentially leading to SAP system compromise.  
- **Status**: Patched by SAP. Exploit proofs were demonstrated publicly and are being weaponized in penetration-testing toolkits.  

### ConnectWise ScreenConnect Auth-Bypass & Path-Traversal  
- **Description**: Combined flaws in on-prem ScreenConnect servers enabling unauthenticated takeover through crafted URL requests that bypass login and allow file manipulation.  
- **Impact**: Full remote-code execution, deployment of ransomware, and data theft from managed endpoints.  
- **Status**: Widely exploited since disclosure; security updates available.  
- **CVE ID**: CVE-2024-1709, CVE-2024-1708  

### Microsoft Entra ID Guest-Subscription Access-Control Gap  
- **Description**: Logic flaw in Entra ID subscription handling permits invited guest accounts to self-assign higher-privilege roles across tenants.  
- **Impact**: Elevation of privilege, unauthorized resource access, and cross-tenant data exposure.  
- **Status**: Under active investigation; mitigations exist (restrict guest invitations, conditional access), no formal patch yet.  

### Trojanized SonicWall NetExtender Installer  
- **Description**: Supply-chain attack delivering a backdoored build of the NetExtender SSL-VPN client that covertly exfiltrates credentials to attacker-controlled C2 servers.  
- **Impact**: Harvests VPN usernames, passwords, and one-time tokens, facilitating network intrusion.  
- **Status**: Malware distributed via phishing sites and third-party mirrors; SonicWall has issued integrity hashes and takedown efforts are ongoing.  

### Malicious npm Packages – “Contagious Interview” Operation  
- **Description**: Thirty-five npm packages masquerading as developer utilities contain obfuscated code that downloads secondary payloads and steals environment variables and SSH keys.  
- **Impact**: Compromise of developer workstations, credential theft, and pipeline poisoning of downstream applications.  
- **Status**: Packages removed from npm registry, but clones persist on alternate repositories; active monitoring advised.  

### LapDogs ORB Network – Backdoored SOHO Firmware  
- **Description**: Chinese threat cluster implants custom backdoors into outdated SOHO router firmware, enrolling devices into an “Operational Relay Box” (ORB) proxy mesh.  
- **Impact**: Stealth C2 relay, staging of espionage traffic, and anonymized launching pads for further intrusions.  
- **Status**: Ongoing; infected devices observed in the US and Southeast Asia. Vendors have released firmware updates for affected models.  

---

## Affected Systems and Products

- **Citrix NetScaler ADC & Gateway**  
  - Versions prior to latest June 2025 maintenance release  
  - Platform: On-prem and cloud-hosted appliances  

- **SAP GUI for Windows 7.80 and SAP GUI for Java 7.70**  
  - Platform: Windows and cross-platform Java environments  

- **ConnectWise ScreenConnect (on-prem)**  
  - Versions ≤ 23.9.4  
  - Platform: Windows & Linux server deployments  

- **Microsoft Entra ID (Azure AD)**  
  - All tenants that enable guest invitations  
  - Platform: Microsoft Azure cloud  

- **SonicWall NetExtender SSL-VPN Client**  
  - Trojanized build (ver. 10.2.337 and clones) distributed via rogue sites  
  - Platform: Windows endpoints  

- **npm JavaScript Packages** (e.g., @dev-uart/cli-toolkit, fs-extra-sync)  
  - Platform: Node.js developer environments on Windows, macOS, Linux  

- **SOHO Routers (LapDogs campaign)**  
  - Multiple brands; models running outdated firmware (notably in US, SG, MY)  
  - Platform: Embedded Linux-based router OS  

---

## Attack Vectors and Techniques

- **Session-Token Memory Scraping**  
  - Vector: Crafted HTTPS requests to vulnerable Citrix appliances extract tokens from process memory.  

- **Input-History Decryption**  
  - Vector: Local file access or remote share exposure of SAP GUI history files; XOR de-obfuscation retrieves plaintext inputs.  

- **Authentication Bypass via Crafted URL**  
  - Vector: `SetupWizard.aspx` endpoint manipulation in ScreenConnect grants admin session without credentials.  

- **Guest Role Escalation**  
  - Vector: Abuse of subscription migration workflow in Entra ID to assign privileged roles to guest accounts.  

- **Trojanized Software Distribution**  
  - Vector: Phishing emails and SEO-poisoned sites offering backdoored NetExtender installer.  

- **Malicious Package Typosquatting**  
  - Vector: npm installs of similarly-named packages execute post-install scripts that fetch backdoors.  

- **SOHO Firmware Backdooring**  
  - Vector: Exploitation of unpatched router vulnerabilities followed by firmware replacement, creating ORB relay nodes.  

---

## Threat Actor Activities

- **Unknown Crimeware Operators (Citrix Bleed 2)**  
  - Campaign: Mass scanning and token harvesting targeting exposed NetScaler appliances across finance and healthcare sectors.  

- **Multiple Ransomware Gangs (ScreenConnect)**  
  - Campaign: Post-exploitation deployment of ransomware and data-exfil tools after CVE-2024-1709 exploitation.  

- **China-Nexus “LapDogs” Group**  
  - Campaign: Building ORB relay infrastructure via backdoored SOHO devices for espionage operations in the US and Southeast Asia.  

- **Cyber Fattah (Pro-Iranian Hacktivists)**  
  - Activity: Data-leak operations leveraging compromised SAP environments; published personal records from 2024 Saudi Games.  

- **North-Korea-Linked “Contagious Interview” Operators**  
  - Campaign: Ongoing supply-chain attack delivering malicious npm packages to developers to aid intelligence gathering.  

- **Unattributed Threat Actor (SonicWall Trojans)**  
  - Campaign: Credential-theft operation distributing trojanized NetExtender instances, likely for resale on dark-web markets.  

---

**End of Report**