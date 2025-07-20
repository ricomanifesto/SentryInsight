# Exploitation Report

A surge of active exploitation is underway against enterprise collaboration and file-transfer infrastructure, with threat actors weaponizing two critical zero-day vulnerabilities—one in Microsoft SharePoint Server (CVE-2025-53770) and another in the CrushFTP managed file-transfer platform (CVE-2025-54309). Both flaws allow unauthenticated attackers to gain full administrative control, and together they have already compromised dozens of corporate environments worldwide. Simultaneously, supply-chain compromises in the JavaScript ecosystem, malicious Arch Linux AUR uploads, and an advanced MFA-downgrade phishing operation (“PoisonSeed”) illustrate the expanding breadth of attacker innovation across authentication, developer tooling, and open-source software distribution channels.

## Active Exploitation Details

### Microsoft SharePoint Server CVE-2025-53770 Zero-Day
- **Description**: A critical, pre-authentication remote code execution flaw in Microsoft SharePoint Server that lets attackers upload arbitrary ASPX payloads and execute them with SYSTEM privileges.
- **Impact**: Full server takeover, lateral movement into on-prem and hybrid Microsoft 365 environments, theft of sensitive documents, and deployment of web shells for persistent access.
- **Status**: Unpatched zero-day; Microsoft has not released fixes. At least 75 organizations have been breached in an ongoing campaign.
- **CVE ID**: CVE-2025-53770

### CrushFTP Web Interface Authentication Bypass (CVE-2025-54309)
- **Description**: A logic flaw in session handling within CrushFTP’s web management interface enabling unauthenticated users to escalate to administrator sessions.
- **Impact**: Attackers gain administrative rights, allowing creation of new user accounts, modification of server configuration, exfiltration or tampering with hosted files, and potential pivoting to internal networks.
- **Status**: Actively exploited in the wild; vendor has issued updated builds mitigating the issue. Administrators must apply the latest patch immediately.
- **CVE ID**: CVE-2025-54309

### npm Maintainer Token Compromise & Package Injection
- **Description**: Phishing emails stole npm access tokens from maintainers of five popular packages. Attackers published trojanized updates that install information-stealing malware during package installation.
- **Impact**: Downstream developers inherit malicious code, enabling credential theft and potential supply-chain propagation into production applications.
- **Status**: Malicious versions removed; maintainers are rotating tokens and publishing clean releases, but clones may persist on mirrors.

### Arch Linux AUR Malicious Package Upload (CHAOS RAT)
- **Description**: Three packages uploaded to the Arch User Repository contained obfuscated install scripts that fetched the CHAOS remote-access trojan.
- **Impact**: Full user compromise on affected Linux workstations, including keylogging, file exfiltration, and command execution.
- **Status**: Packages delisted; users must audit systems for RAT remnants and rotate credentials.

### WebAuthn Cross-Device MFA Downgrade (“PoisonSeed”)
- **Description**: Attackers trigger the WebAuthn cross-device sign-in flow, serving QR codes that trick victims into approving a lower-assurance push-notification on their mobile authenticator, bypassing FIDO2 security-key requirements.
- **Impact**: Account takeover on enterprise SSO platforms despite hardware-key policies, enabling email and cloud resource compromise.
- **Status**: Campaign active; no vendor patch because the weakness abuses legitimate UX. Mitigations include disabling cross-device sign-in and enforcing device-bound passkeys.

## Affected Systems and Products

- **Microsoft SharePoint Server**: All on-prem versions currently supported by mainstream support; particularly internet-facing deployments.  
- **CrushFTP Server**: Versions prior to the vendor’s out-of-band hotfix (10.x and 11.x branches).  
- **npm Packages**: eslint-config-prettier, eslint-plugin-prettier, and three additional unnamed packages trojanized in July 2025.  
- **Arch Linux AUR Packages**: Three packages (names withheld in the advisory) uploaded between 7–12 July 2025.  
- **Enterprise SSO / IdPs**: Any platform supporting WebAuthn cross-device sign-in (Azure AD, Okta, Duo, etc.) is susceptible to “PoisonSeed” phishing abuse.

## Attack Vectors and Techniques

- **Pre-Auth RCE via Malicious ASPX Upload (SharePoint)**  
  • Vector: Crafted HTTP POST requests exploiting inadequate validation in file-upload handler.  

- **Session Fixation / Token Replay (CrushFTP)**  
  • Vector: Manipulated session identifiers in the web interface to hijack admin privileges.  

- **Phishing-Driven Token Theft**  
  • Vector: Spear-phishing messages impersonating npm staff, harvesting maintainer access tokens.  

- **Trojanized Package Installation Scripts**  
  • Vector: Post-install hooks downloading secondary payloads (npm & AUR ecosystems).  

- **MFA Downgrade / QR-Code Phishing (“Quishing”)**  
  • Vector: Fake login portals generating WebAuthn QR codes that reroute authentication to attacker-controlled sessions.  

## Threat Actor Activities

- **Unnamed SharePoint Exploitation Cluster**  
  • Campaign: Large-scale scanning of public SharePoint endpoints, deployment of China-Chopper-style web shells, and data theft from 75+ organizations.  

- **CrushFTP Exploitation Group**  
  • Campaign: Rapid weaponization within 24 hours of disclosure; targets include finance and healthcare sectors to harvest sensitive files.  

- **“PoisonSeed” Phishing Operator**  
  • Campaign: Focused on technology and government users, leveraging QR-code lures to bypass hardware MFA.  

- **APT28 (Fancy Bear)**  
  • Campaign: “Authentic Antics” malware used for Microsoft 365 credential harvesting, aligning with overlapping infrastructure seen in prior GRU operations.  

- **UNG0002**  
  • Campaign: LNK-file spear-phishing against entities in China, Hong Kong, and Pakistan, delivering RATs for espionage.  

