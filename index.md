# Exploitation Report

A wave of active exploitation campaigns is unfolding across enterprise, developer, and consumer environments. Threat actors are leveraging two critical zero-day vulnerabilities—one in Microsoft SharePoint Server (CVE-2025-53770) and another in CrushFTP (CVE-2025-54309)—to gain remote code execution and full administrative control on unpatched systems. Simultaneously, sophisticated social-engineering operations are hijacking software-supply chains (npm and Arch AUR) and defeating modern FIDO2 multifactor authentication through “downgrade” attacks. These incidents collectively compromise hundreds of organizations, highlighting the urgent need for immediate patching, token hygiene, and MFA hardening.

---

## Active Exploitation Details

### Microsoft SharePoint Server Remote Code Execution Zero-Day
- **Description**: A critical, currently unpatched flaw in Microsoft SharePoint allows remote attackers to execute arbitrary code via a crafted request to the SharePoint web services endpoint.  
- **Impact**: Full takeover of SharePoint servers, lateral movement into corporate networks, data theft, and deployment of additional payloads. Over 75 global organizations have reportedly been breached.  
- **Status**: Actively exploited in the wild; no official patch released at report time. Mitigations and intrusion-detection signatures are being circulated by security vendors.  
- **CVE ID**: CVE-2025-53770  

### CrushFTP Server Administrative Access Zero-Day
- **Description**: A vulnerability in CrushFTP’s web interface enables unauthenticated attackers to escalate privileges to administrator by abusing session handling and path-traversal logic.  
- **Impact**: Complete server compromise, exposure of stored files, credential theft, and potential ransomware deployment.  
- **Status**: Actively exploited; vendor has released patched builds and urges immediate upgrade.  
- **CVE ID**: CVE-2025-54309  

### WebAuthn Cross-Device MFA Downgrade (PoisonSeed Campaign)
- **Description**: Attackers coerce victims to approve rogue login requests by exploiting the WebAuthn cross-device sign-in feature, effectively downgrading FIDO2 security-key protection to weaker push-based approval.  
- **Impact**: Account takeover even when FIDO2 keys are enforced; enables business-email compromise and further intrusions.  
- **Status**: Ongoing phishing campaign; no vendor patch required, but hardened authentication flows and user education are recommended.  

### Compromised npm Packages via Maintainer-Token Theft
- **Description**: Phishing emails stole npm publisher tokens, allowing attackers to inject malware into six popular JavaScript packages, including eslint-config-prettier and eslint-plugin-prettier.  
- **Impact**: Downstream developers received trojanized updates that exfiltrate environment variables, credentials, and SSH keys.  
- **Status**: Malicious versions have been yanked; maintainers rotated tokens and published clean releases.  

### Malicious Arch Linux AUR Packages Installing Chaos RAT
- **Description**: Three community-supplied AUR packages were backdoored to fetch and execute the CHAOS remote-access trojan on installation.  
- **Impact**: Full user compromise on affected Linux systems, providing persistent remote access and data exfiltration capabilities.  
- **Status**: Packages removed from AUR; users must audit systems for residual malware.  

---

## Affected Systems and Products

- **Microsoft SharePoint Server (Subscription Edition, 2019, 2016)**  
  - **Platform**: On-premises Windows Server deployments  
- **CrushFTP (all unpatched versions prior to vendor-issued hotfix)**  
  - **Platform**: Cross-platform Java application on Windows, Linux, macOS  
- **eslint-config-prettier & eslint-plugin-prettier (compromised npm versions)**  
  - **Platform**: Node.js ecosystem, CI/CD pipelines, developer workstations  
- **Additional npm packages (total of six trojanized libraries)**  
  - **Platform**: Any application pulling affected versions from the npm registry  
- **Arch Linux AUR backdoored packages**  
  - **Platform**: Arch Linux desktops, servers using AUR helpers  
- **WebAuthn / FIDO2 implementations with cross-device sign-in enabled**  
  - **Platform**: Modern web browsers and SSO platforms supporting WebAuthn  

---

## Attack Vectors and Techniques

- **SOAP Endpoint RCE (SharePoint)**  
  - **Vector**: Crafted HTTP requests to vulnerable SharePoint web services bypass authentication checks.  
- **Session-Hijack & Path Traversal (CrushFTP)**  
  - **Vector**: Manipulated URL paths and cookies escalate privileges to admin.  
- **Token-Theft Phishing (npm Supply Chain)**  
  - **Vector**: Spear-phishing emails lure maintainers to credential-harvesting sites, stealing npm auth tokens.  
- **Malicious Package Injection (npm/AUR)**  
  - **Vector**: Compromised maintainer accounts upload trojanized code that executes during package installation.  
- **FIDO2 Downgrade via QR Code (PoisonSeed)**  
  - **Vector**: Victims scan attacker-controlled QR code that triggers cross-device WebAuthn approval flow.  
- **LNK File Spear-Phishing (UNG0002)**  
  - **Vector**: Weaponized shortcut files launch RATs once opened by targets.  

---

## Threat Actor Activities

- **Unknown SharePoint Exploitation Cluster**  
  - **Campaign**: Large-scale intrusion breaching more than 75 organizations worldwide; post-exploitation focuses on data exfiltration and ransomware staging.  

- **Unidentified Actors Exploiting CrushFTP**  
  - **Campaign**: Rapid “smash-and-grab” intrusions against internet-facing file-transfer servers to harvest sensitive documents.  

- **PoisonSeed**  
  - **Campaign**: Targeted phishing against enterprises with FIDO2 deployments; objectives include credential theft and business-email compromise.  

- **npm Supply-Chain Attackers**  
  - **Campaign**: Credential-phishing followed by malicious package publication to propagate malware throughout the JavaScript ecosystem.  

- **Arch Linux AUR Malicious Maintainer(s)**  
  - **Campaign**: Backdooring of niche packages to establish footholds on developer and server systems running Arch Linux.  

- **APT28 (Fancy Bear)**  
  - **Campaign**: “Authentic Antics” malware steals Microsoft 365 credentials; leveraged in espionage operations against UK entities (no linked CVE in current cycle but related to broader threat landscape).  

- **UNG0002**  
  - **Campaign**: Twin espionage operations against China, Hong Kong, and Pakistan using LNK files and multiple RAT families.  

---

**End of Report**