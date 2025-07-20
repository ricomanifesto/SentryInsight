# Exploitation Report

A wave of highly-critical zero-day exploitation is underway targeting widely-deployed enterprise platforms. Attackers are chaining remote-code-execution flaws in Microsoft SharePoint Server (CVE-2025-53770) and an authentication-bypass in CrushFTP (CVE-2025-54309) to gain footholds inside corporate networks. These intrusions are unfolding alongside supply-chain compromises of popular npm packages and Arch Linux AUR projects, advanced phishing operations that sidestep FIDO2 keys, and focused malware campaigns aimed at Web3 developers. Organizations running the affected products should treat these threats as an immediate incident-response priority and accelerate patching or compensating controls.

## Active Exploitation Details

### Microsoft SharePoint Server Remote Code Execution Zero-Day
- **Description**: A critical flaw in Microsoft SharePoint Server allows unauthenticated remote attackers to execute arbitrary code by sending crafted requests to the web services endpoint.  
- **Impact**: Full takeover of SharePoint, lateral movement into internal networks, theft of sensitive documents, and deployment of additional payloads.  
- **Status**: Actively exploited since at least 18 July; over 85 compromised servers confirmed. No official patch is available. Microsoft has published mitigations involving disabling the vulnerable endpoint and restricting external access.  
- **CVE ID**: CVE-2025-53770  

### CrushFTP Web Interface Authentication Bypass & Code Execution
- **Description**: A vulnerability in CrushFTP’s web interface permits attackers to bypass authentication, quickly escalate privileges to administrator, and upload or execute malicious files.  
- **Impact**: Complete server compromise, exfiltration of stored files, pivoting into adjacent systems, and potential ransomware deployment.  
- **Status**: Zero-day confirmed under active exploitation in the wild. Vendor has released updated builds and urges immediate upgrades and password rotation.  
- **CVE ID**: CVE-2025-54309  

## Affected Systems and Products

- **Microsoft SharePoint Server (on-premises)**  
  - **Platform**: Windows Server; versions currently supported (e.g., SharePoint Server Subscription Edition, 2019) exposed to the Internet or internal users.

- **CrushFTP Server (all editions prior to vendor-patched build)**  
  - **Platform**: Cross-platform Java application on Windows, Linux, macOS.

- **Aruba Instant On Access Points**  
  - **Platform**: Hardware access points running Aruba Instant On firmware containing hard-coded credentials (no exploitation observed yet, but remotely accessible).

- **npm Ecosystem – eslint-config-prettier, eslint-plugin-prettier, and 3 additional packages**  
  - **Platform**: Node.js supply chain; any project auto-upgrading to the trojanized versions.

- **Arch Linux AUR – three malicious packages (Chaos RAT)**  
  - **Platform**: Linux endpoints using affected AUR helpers or manual AUR installs.

## Attack Vectors and Techniques

- **Deserialization-Based RCE (SharePoint)**  
  - **Vector**: Crafted SOAP/REST calls trigger insecure deserialization leading to arbitrary code execution.

- **Web Interface Authentication Bypass (CrushFTP)**  
  - **Vector**: Manipulated request paths and session tokens skip login checks, granting admin access.

- **Hard-coded Credential Abuse (Aruba Instant On)**  
  - **Vector**: Attackers use embedded username/password to log in via HTTP/HTTPS management portal.

- **Token Theft & Package Hijack (npm / AUR)**  
  - **Vector**: Phishing emails harvest maintainer tokens; attackers publish back-doored package versions consumed by CI/CD pipelines.

- **FIDO2 MFA Downgrade (PoisonSeed)**  
  - **Vector**: Phishing sites force victims into cross-device WebAuthn flow, presenting QR codes that proxy authentication to attacker devices.

- **Malicious AI Landing Pages (EncryptHub)**  
  - **Vector**: Fake AI tooling sites deliver Fickle Stealer via disguised installers, specifically luring Web3 developers.

## Threat Actor Activities

- **EncryptHub (aka LARVA-208 / Water Gamayun)**  
  - **Campaign**: Fake AI coding platforms delivering Fickle Stealer to Web3 developer environments for credential and wallet exfiltration.

- **Unnamed SharePoint Exploitation Cluster**  
  - **Campaign**: Mass scanning of Internet-facing SharePoint servers; post-exploitation includes web shell deployment and data theft from at least 85 organizations.

- **Unknown Actors Exploiting CrushFTP**  
  - **Campaign**: Targeted attacks on file-transfer infrastructures, focusing on financial, healthcare, and technology firms with unpatched CrushFTP instances.

- **PoisonSeed Operators**  
  - **Campaign**: Phishing operations bypassing FIDO2 hardware keys, primarily aimed at enterprise Microsoft 365 tenants.

- **npm Supply-Chain Intruders**  
  - **Campaign**: Phished maintainers, hijacked five npm packages, injected information-stealing malware into development pipelines.

- **APT28 (Fancy Bear)**  
  - **Campaign**: “Authentic Antics” espionage malware harvesting Microsoft 365 credentials across diplomatic and defense sectors.

- **Arch Linux AUR Malicious Maintainers**  
  - **Campaign**: Uploaded packages installing Chaos RAT for remote control of Linux workstations, now pulled by Arch security team.

Stay vigilant, apply vendor guidance immediately, and monitor for post-exploitation indicators associated with these threats.