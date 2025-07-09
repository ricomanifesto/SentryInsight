# Exploitation Report

Recent reporting highlights active exploitation of a newly-disclosed Microsoft SQL Server zero-day, widespread real-time phishing operations that bypass legacy MFA, and novel mobile techniques such as Android “TapTrap” that undermine the operating system’s permission model.  In parallel, critical business platforms are being scrutinised for logic flaws (e.g., ServiceNow “Count(er) Strike”) that adversaries could weaponise for data harvesting.  State-sponsored groups including North Korea’s Andariel and India-linked DoNot APT continue to leverage malware and social-engineering to compromise organisations, while financially-motivated actors use red-team tooling (Shellter) to distribute stealers at scale.

## Active Exploitation Details

### Microsoft SQL Server Privilege-Escalation Zero-Day
- **Description**: A flaw in Microsoft SQL Server allows authenticated users to escalate privileges, execute arbitrary code, or move laterally by abusing database-level permissions.
- **Impact**: Full takeover of SQL instances, potential access to sensitive business data, opportunity for domain-level compromise when SQL runs with elevated service accounts.
- **Status**: Publicly disclosed and observed in‐the-wild prior to the July 2025 Patch Tuesday release; fixes are available via Windows Update.

### Legacy MFA Real-Time Phishing Bypass (Adversary-in-the-Middle)
- **Description**: Attackers proxy login pages through look-alike sites, capture session cookies and OTP codes in real time, and relay them to genuine IdPs, effectively nullifying app-based or SMS-based MFA.
- **Impact**: Account takeover despite MFA, enabling email rule manipulation, BEC, cloud resource abuse, and privilege escalation.
- **Status**: Actively exploited across multiple sectors; mitigations require phishing-resistant factors (FIDO2, hardware tokens, biometrically-bound devices).

### Android “TapTrap” Permission-Bypass Technique
- **Description**: Exploits rapid UI animation overlays to trick users into granting permissions or executing destructive actions; leverages invisible tapjacking to mask true intent.
- **Impact**: Steals SMS, contact data, installs additional payloads, or initiates fraudulent transactions without user awareness.
- **Status**: Proof-of-concept observed in the wild on devices running unpatched Android custom ROMs and older security patch levels; no official OS fix yet.

### ServiceNow “Count(er) Strike” Data Enumeration Flaw
- **Description**: Logic flaw in the ServiceNow platform enables low-privileged users to enumerate and extract records from restricted tables via manipulated “counter” API calls.
- **Impact**: Exposure of PII, financial records, and proprietary data stored in ServiceNow instances; possible escalation to further cloud compromise.
- **Status**: Disclosure accompanied by technical details and PoC; exploitation already reported by security researchers against misconfigured instances.  ServiceNow has shipped mitigations and guidance, full patch forthcoming.

## Affected Systems and Products

- **Microsoft SQL Server (multiple supported builds)**  
  Platform: Windows Server, Azure SQL Managed Instances

- **Enterprise Identity Platforms using legacy MFA (Microsoft 365, Okta, Duo, generic TOTP/SMS)**  
  Platform: Web & cloud SSO environments

- **Android Smartphones & Tablets (Android 11 → 14 with vulnerable UI components)**  
  Platform: Stock Android and OEM skins lacking latest security patches

- **ServiceNow SaaS Instances (all releases prior to vendor mitigation)**  
  Platform: Cloud-hosted ITSM/HR/CRM environments

## Attack Vectors and Techniques

- **Adversary-in-the-Middle (AiTM) Phishing**  
  Vector: Malicious reverse-proxy sites (evilginx, Modlishka) capturing live authentication traffic.

- **SQL Server Privilege Escalation**  
  Vector: Authenticated database connections abusing the zero-day to obtain elevated rights.

- **TapJacking / Invisible Overlay**  
  Vector: Rapid animation overlays intercepting user taps to grant hidden permissions.

- **ServiceNow Counter API Abuse**  
  Vector: Crafted API calls that manipulate “sysparm_view” and “sys_id” parameters to enumerate restricted tables.

- **Red-Team Tool Re-Packing (Shellter)**  
  Vector: Embedding stealers (Lumma, SectopRAT) into benign executables to evade AV/EDR.

## Threat Actor Activities

- **Andariel (North Korea)**  
  Campaign: Revenue-generation via fraudulent IT worker personas, deployment of custom malware inside victim networks, sanctioned by U.S. Treasury.

- **DoNot APT (suspected India‐linked)**  
  Campaign: Targeting European foreign ministries with “LoptikMod” data-harvesting malware, utilising spear-phishing and DLL hijacking.

- **Lumma Stealer & SectopRAT Operators**  
  Campaign: Using a leaked Shellter license to obfuscate payloads, distributing via malvertising and phishing to exfiltrate credentials and crypto-wallet data.

- **DragonForce Ransomware**  
  Campaign: Breached M&S through sophisticated impersonation and social engineering, leading to large-scale data exfiltration and encryption.

- **Silk Typhoon (China)**  
  Campaign: Arrest of suspected member Xu Zewei linked to U.S. network intrusions leveraging custom implants and stolen credentials.

- **SatanLock Ransomware**  
  Campaign: Group shutting down operations yet threatening final data leaks, indicating increased law-enforcement pressure on ransomware operators.

