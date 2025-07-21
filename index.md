# Exploitation Report

During the past week, security researchers observed multiple, large-scale exploitation waves against business-critical collaboration and file-transfer platforms. Two unpatched zero-day vulnerabilities—CVE-2025-53770/CVE-2025-53771 in Microsoft SharePoint Server and CVE-2025-54309 in CrushFTP—are being weaponized to gain remote code execution and full administrative control of on-prem environments. More than 75 organizations have already had SharePoint servers breached, while opportunistic attackers are scanning the Internet for vulnerable CrushFTP instances only hours after proof-of-concept details leaked. Concurrently, supply-chain attacks continue to plague developer ecosystems, with npm and Arch Linux AUR repositories hijacked to distribute information-stealers and RATs. Threat actors such as EncryptHub and APT28 are actively leveraging these vectors, demonstrating an ongoing pivot toward developer-focused social-engineering and MFA-bypass techniques.

## Active Exploitation Details

### Microsoft SharePoint Server Remote Code Execution Zero-Days
- **Description**: Two independent flaws allow authenticated users with basic permissions to upload malicious ASPX pages via “Add Web Part Page” and other API endpoints, bypassing validation controls and triggering server-side execution.  
- **Impact**: Attackers can run arbitrary commands under the SharePoint service account, implant web shells, harvest credentials, and move laterally inside corporate networks.  
- **Status**: Actively exploited since 18 July; Microsoft has not yet released official patches. Temporary mitigations involve disabling page creation and restricting Designer/Owner roles.  
- **CVE ID**: CVE-2025-53770  
- **CVE ID**: CVE-2025-53771  

### CrushFTP Administrative Bypass Zero-Day (Path Traversal)
- **Description**: A path-traversal flaw in the web interface lets remote, unauthenticated users read arbitrary system files—including the main configuration XML—which stores encrypted admin credentials that can be trivially decrypted.  
- **Impact**: Full administrative takeover of the CrushFTP instance, enabling file exfiltration, command execution, and potential pivoting to internal systems.  
- **Status**: Exploits observed in the wild; vendor released emergency hot-fix builds and urged immediate upgrade.  
- **CVE ID**: CVE-2025-54309  

## Affected Systems and Products

- **Microsoft SharePoint Server**: 2019, 2022, and Subscription Edition (on-prem deployments exposed to the Internet)  
- **CrushFTP**: All versions prior to the emergency patched build (10.x/11.x) released 24 July 2025  
- **npm Ecosystem**: Compromised packages “eslint-config-prettier,” “eslint-plugin-prettier,” and four additional libraries updated on 21 July  
- **Arch Linux AUR**: Malicious packages pulled on 23 July that installed Chaos RAT  
- **Aruba Instant On Access Points**: Models AP11-AP25 contain hard-coded credentials (no confirmed exploitation yet)  
- **Web3 Development Environments**: Targets using fake “AI code-assistant” sites operated by EncryptHub  

## Attack Vectors and Techniques

- **Malicious ASPX Upload (SharePoint RCE)**  
  - **Vector**: Authenticated POST requests to page-creation endpoints; payload executes under IIS worker process.  

- **Path Traversal & Config Theft (CrushFTP)**  
  - **Vector**: Crafted HTTP GET request with ../../ traversal to “/users/MainUsers/Main.xml”, followed by credential decryption.  

- **Supply-Chain Package Hijacking (npm)**  
  - **Vector**: Phished maintainer tokens used to push trojanized package updates containing preinstall scripts that fetch Windows executables.  

- **Malicious AUR Packages (Arch Linux)**  
  - **Vector**: Typosquatted packages executing install scripts to drop Chaos RAT binary.  

- **FIDO2 MFA Downgrade (PoisonSeed)**  
  - **Vector**: Abuse of WebAuthn cross-device sign-in to present push notifications that trick users into approving attacker sessions.  

- **Fake AI Platform Lures (EncryptHub)**  
  - **Vector**: Water-holed websites and Discord channels offering “AI smart-contract assistant” downloads that bundle Fickle Stealer.  

## Threat Actor Activities

- **EncryptHub (aka LARVA-208 / Water Gamayun)**  
  - **Campaign**: Targets Web3 developers via fake AI tools; delivers Fickle Stealer to siphon cryptocurrency wallets, browser cookies, and SSH keys.  

- **Unattributed SharePoint Exploitation Cluster**  
  - **Campaign**: Mass scanning and exploitation of CVE-2025-53770/53771; at least 75 companies compromised, with web shells observed under “/Style Library/”.  

- **CrushFTP Zero-Day Operators**  
  - **Campaign**: Rapid opportunistic attacks against Internet-facing CrushFTP; observed exfiltration of sensitive archives followed by ransomware deployment.  

- **PoisonSeed**  
  - **Campaign**: Spear-phishing targeting enterprise Office 365 tenants; downgrades FIDO2 MFA to weaker push approvals, facilitating business-email compromise.  

- **APT28 (Fancy Bear)**  
  - **Campaign**: “Authentic Antics” malware steals Microsoft 365 credentials from government and defense contractors; leverages custom OAuth abuse for persistence.  

