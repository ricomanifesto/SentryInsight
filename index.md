# Exploitation Report

Threat actors are simultaneously leveraging multiple zero-day and recently patched flaws to gain initial access, elevate privileges, and establish long-term persistence in enterprise and cloud environments. The most critical activity observed this week includes the ongoing weaponisation of the CrushFTP authentication-bypass zero-day (CVE-2025-54309), mass Internet scanning for the TeleMessage SGNL credential-disclosure bug (CVE-2025-48927), and an active exploitation chain against un-patched Ivanti Connect Secure gateways that is dropping the new “MDifyLoader” payload to load Cobalt Strike beacons directly in memory. Parallel supply-chain attacks (malicious Arch Linux AUR packages) and sophisticated credential-theft campaigns from APT28 and the “PoisonSeed” actor illustrate a widening threat surface that combines vulnerability exploitation with social-engineering and software-supply-chain compromise.

## Active Exploitation Details

### CrushFTP Administrative Interface Authentication Bypass  
- **Description**: A zero-day flaw in CrushFTP’s web interface allows remote attackers to bypass authentication and obtain administrator privileges via crafted HTTP requests.  
- **Impact**: Full administrative control, leading to arbitrary file access, configuration changes, and potential code execution on the underlying server.  
- **Status**: Actively exploited in the wild. Vendor has released emergency patches and mitigation guidance.  
- **CVE ID**: CVE-2025-54309  

### TeleMessage SGNL Credential Disclosure Flaw  
- **Description**: An input-validation weakness in the SGNL enterprise-messaging application enables unauthenticated retrieval of configuration files that contain usernames, hashed passwords, and tokens.  
- **Impact**: Attackers can harvest credentials and pivot to internal messaging systems, enabling further lateral movement and data exfiltration.  
- **Status**: Exploitation attempts observed at scale; a security update has been issued and administrators are urged to patch immediately.  
- **CVE ID**: CVE-2025-48927  

### Ivanti Connect Secure Zero-Day Chain (MDifyLoader Deployment)  
- **Description**: A newly reported set of logic and path-traversal flaws in Ivanti Connect Secure / Policy Secure gateways is being chained to write files to disk and execute the in-memory “MDifyLoader,” which subsequently launches Cobalt Strike beacons.  
- **Impact**: Remote code execution on VPN appliances, credential theft, and establishment of covert command-and-control channels inside corporate networks.  
- **Status**: Confirmed in-the-wild exploitation; Ivanti has issued interim mitigations while permanent patches are being finalised.  

## Affected Systems and Products

- **CrushFTP Server**: Versions 9.x, 10.x, and early 11.x running on Windows, Linux, and macOS platforms  
- **TeleMessage SGNL Application**: On-prem and cloud deployments up to the vulnerable build identified in vendor advisory; affects Android, iOS, and web clients through back-end API exposure  
- **Ivanti Connect Secure / Policy Secure Gateways**: 9.x and 22.x firmware branches across physical and virtual appliances  
- **Arch Linux AUR Packages (`acroread-simple`, `postgresql-memo`, `jira-tools`)**: Malicious packages targeting Arch Linux systems via the AUR infrastructure  
- **Microsoft 365 Tenants** (Authentic Antics campaign): Cloud-based email and collaboration services across all platforms  

## Attack Vectors and Techniques

- **Web-Interface Authentication Bypass**  
  - **Vector**: Crafted HTTP requests manipulate session handling to skip login checks in CrushFTP.  

- **Unauthenticated API Enumeration**  
  - **Vector**: Direct GET requests to exposed endpoints retrieve `config.json` and credential stores in TeleMessage SGNL installations.  

- **Gateway Exploit Chain & In-Memory Loader**  
  - **Vector**: Chained path-traversal and command-injection on Ivanti VPN appliances writes MDifyLoader, which reflective-loads Cobalt Strike into memory to evade disk-based detection.  

- **Supply-Chain Package Poisoning**  
  - **Vector**: Malicious Arch Linux AUR packages execute install scripts that fetch and run CHAOS RAT from remote servers during package installation.  

- **QR-Code MFA Bypass (PoisonSeed)**  
  - **Vector**: Phishing pages display tampered QR codes that, when scanned, proxy authentication data and bypass FIDO-based MFA protections.  

- **Token Theft via Microsoft Graph (Authentic Antics / APT28)**  
  - **Vector**: PowerShell scripts and malicious OAuth applications steal OAuth refresh tokens and session cookies to maintain persistent Microsoft 365 access.  

## Threat Actor Activities

- **Unknown Criminal Actors**  
  - **Campaign**: Ongoing exploitation of CVE-2025-54309 to hijack CrushFTP servers, observed monetising access through data theft and initial-access-broker forums.  

- **Mass Opportunistic Scanners**  
  - **Campaign**: Internet-wide scanning for CVE-2025-48927 endpoints, likely preceding credential-stuffing and business-email-compromise operations.  

- **Unattributed Advanced Operator**  
  - **Campaign**: Deployment of MDifyLoader on un-patched Ivanti gateways; post-exploitation tooling indicates a highly skilled adversary focused on stealthy persistence and lateral movement.  

- **APT28 (Fancy Bear / Russian GRU)**  
  - **Campaign**: “Authentic Antics” malware used for Microsoft 365 credential harvesting in diplomatic and defence sectors across the UK and EU.  

- **PoisonSeed Actor**  
  - **Campaign**: Novel QR-code phishing operation targeting corporate users protected by FIDO hardware tokens, enabling session hijack and account takeover.  

- **UNG0002**  
  - **Campaign**: Parallel espionage campaigns in China, Hong Kong, and Pakistan leveraging malicious LNK files and RAT payloads for strategic intelligence collection.  

- **Unidentified AUR Package Maintainer(s)**  
  - **Campaign**: Supply-chain infiltration of Arch Linux AUR to distribute CHAOS RAT, targeting developers and power users in the Linux ecosystem.