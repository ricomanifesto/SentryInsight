# Exploitation Report

A surge of active exploitation is underway against two critical server-side zero-day vulnerabilities—one in Microsoft SharePoint (CVE-2025-53770) and another in CrushFTP (CVE-2025-54309). Both flaws allow remote, unauthenticated compromise of high-value infrastructure and are being leveraged in broad campaigns that have already breached more than 85 on-premises SharePoint servers and numerous unsecured CrushFTP instances. In parallel, threat actors are innovating around identity protections: the “PoisonSeed” phishing operation is bypassing FIDO2 multi-factor authentication (MFA) by abusing WebAuthn’s cross-device sign-in flow. These exploits, coupled with aggressive supply-chain compromises targeting npm and Arch Linux AUR repositories, underscore a rapidly evolving threat landscape that blends zero-day weaponization with novel social-engineering techniques.

## Active Exploitation Details

### Microsoft SharePoint Server RCE Zero-Day
- **Description**: A critical remote code-execution flaw in Microsoft SharePoint Server that allows unauthenticated attackers to upload and execute arbitrary code through crafted API calls.  
- **Impact**: Complete takeover of SharePoint servers, lateral movement inside corporate networks, data theft, and deployment of ransomware.  
- **Status**: Actively exploited since at least 18 July; no official patch available. Microsoft has published temporary mitigation guidance.  
- **CVE ID**: CVE-2025-53770  

### CrushFTP Web Interface Authentication Bypass
- **Description**: An authentication-bypass vulnerability in the CrushFTP file-transfer platform’s web interface enabling attackers to obtain administrator privileges via crafted requests.  
- **Impact**: Full administrative control, exfiltration or deletion of hosted files, creation of rogue user accounts, and pivoting to internal assets.  
- **Status**: Zero-day is under active exploitation; a vendor hot-fix is available and users are urged to upgrade immediately.  
- **CVE ID**: CVE-2025-54309  

### WebAuthn Cross-Device MFA Downgrade (PoisonSeed)
- **Description**: A phishing-driven downgrade attack where adversaries trick users into approving malicious login requests by exploiting WebAuthn’s cross-device sign-in feature, effectively bypassing FIDO2 security-key protections.  
- **Impact**: Account takeover of cloud and corporate services protected by hardware-based MFA, leading to potential business-email compromise (BEC) and data breaches.  
- **Status**: Ongoing campaign; no vendor patch required, but security-key workflows and user training must be reinforced.  

## Affected Systems and Products

- **Microsoft SharePoint Server 2019/2022 (on-prem)**  
  - **Platform**: Windows Server deployments, including hybrid environments  

- **CrushFTP (all versions prior to vendor hot-fix 11.x/10.x)**  
  - **Platform**: Cross-platform Java application on Windows, Linux, macOS, and Solaris  

- **WebAuthn / FIDO2 Implementations (cross-device sign-in feature)**  
  - **Platform**: Modern browsers and identity providers supporting passkeys and security-key login workflows  

## Attack Vectors and Techniques

- **Malicious SOAP/API Requests (SharePoint)**  
  - **Vector**: Unauthenticated HTTP(S) requests to vulnerable SharePoint endpoints upload payloads that are later executed by the server process.  

- **Forged Web Interface Calls (CrushFTP)**  
  - **Vector**: Crafted HTTP requests bypass login checks, granting direct access to administrative dashboards.  

- **MFA Downgrade via QR-Code Phishing (PoisonSeed)**  
  - **Vector**: Victims scan a QR code or click a link that initiates cross-device WebAuthn authentication, unknowingly authorizing the attacker’s session.  

## Threat Actor Activities

- **EncryptHub / LARVA-208 (Water Gamayun)**  
  - **Campaign**: Distributing “Fickle Stealer” malware through fake AI development platforms aimed at Web3 developers to harvest credentials and cryptocurrency wallets.  

- **Unnamed Campaign Operators (SharePoint CVE-2025-53770)**  
  - **Activities**: Mass-exploitation spree compromising 75 + corporate SharePoint servers for data theft and potential ransomware staging.  

- **Unknown Threat Groups (CrushFTP CVE-2025-54309)**  
  - **Activities**: Targeting unpatched CrushFTP servers globally for administrative takeover and file exfiltration.  

- **PoisonSeed Phishing Group**  
  - **Campaign**: Actively leveraging WebAuthn MFA downgrade to infiltrate enterprise accounts and bypass FIDO2 protections.  

- **Supply-Chain Attackers (npm / AUR)**  
  - **Campaign**: Hijacked eslint-config-prettier, eslint-plugin-prettier, and other npm packages plus three Arch Linux AUR packages to deliver malware via compromised maintainer tokens.  

- **APT28 (Fancy Bear)**  
  - **Activities**: Operating “Authentic Antics” credential-stealing malware targeting Microsoft 365 tenants for espionage.  

## End of Report