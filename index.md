# Exploitation Report

A surge of zero-day exploitation activity is underway across enterprise collaboration and file-transfer infrastructure. Attackers are weaponizing two unpatched Microsoft SharePoint vulnerabilities (CVE-2025-53770, CVE-2025-53771) and a newly disclosed CrushFTP flaw (CVE-2025-54309) to gain remote code execution and full administrative control of servers. The SharePoint zero-days have already compromised more than 85 on-prem instances and breached data on at least 75 organizations, while the CrushFTP weakness is being leveraged to escape the virtual file-system sandbox and download sensitive configuration files containing credentials. In parallel, threat actors are innovating in supply-chain and social-engineering vectors: EncryptHub is luring Web3 developers with fake AI platforms, npm and Arch Linux repositories were hijacked to drop malware, and the “PoisonSeed” campaign sidesteps FIDO2 authentication by abusing WebAuthn’s cross-device sign-in feature. Russian APT28 continues credential-stealing operations against Microsoft 365 tenants. The combined activity underscores an urgent need for virtual patching, MFA hardening, and rigorous supply-chain security.

## Active Exploitation Details

### Microsoft SharePoint Server Remote Code Execution Zero-Day  
- **Description**: A critical flaw in the SharePoint workflow service allows unauthenticated attackers to craft specially-formed HTTP requests that trigger arbitrary code execution under the SharePoint service account.  
- **Impact**: Full takeover of SharePoint servers, lateral movement inside corporate networks, data exfiltration, and potential deployment of web-shells or ransomware.  
- **Status**: Actively exploited since 18 July 2025; no official patch or mitigations beyond IIS request blocking rules.  
- **CVE ID**: CVE-2025-53770  

### Microsoft SharePoint Server Privilege-Escalation / RCE Zero-Day  
- **Description**: Companion vulnerability to the above, enabling privilege escalation and reliable code execution when chained with CVE-2025-53770.  
- **Impact**: Elevates attacker privileges to install persistence mechanisms and execute system-level commands.  
- **Status**: Actively exploited in the same campaign; no vendor fix released.  
- **CVE ID**: CVE-2025-53771  

### CrushFTP Administrative Access Zero-Day  
- **Description**: A server-side logic flaw lets remote attackers escape the CrushFTP Virtual File System (VFS) sandbox, read arbitrary files—including ‘users.conf’—and hijack authenticated admin sessions through stolen session cookies.  
- **Impact**: Complete administrative control, file exfiltration, credential theft, and potential deployment of additional malware.  
- **Status**: Under active exploitation; vendor has issued out-of-band hot-fix builds while a full update is being finalized.  
- **CVE ID**: CVE-2025-54309  

## Affected Systems and Products

- **Microsoft SharePoint Server 2016 / 2019 / Subscription Edition**  
  - **Platform**: On-prem Windows Server deployments exposed to the Internet  

- **CrushFTP Server versions prior to the July 2025 hot-fix release**  
  - **Platform**: Cross-platform (Windows, Linux, macOS) systems with the web interface enabled  

## Attack Vectors and Techniques

- **Unauthenticated HTTP RCE (SharePoint)**  
  - **Vector**: Crafted HTTP/S POST requests exploiting workflow processing endpoints to run arbitrary commands.  

- **VFS Sandbox Escape (CrushFTP)**  
  - **Vector**: Malicious path traversal combined with session hijacking to reach configuration files and admin functions.  

- **Supply-Chain Token Hijack (npm)**  
  - **Vector**: Phishing emails stole maintainer tokens; modified eslint-config-prettier & eslint-plugin-prettier packages to drop malware.  

- **AUR Package Poisoning (Arch Linux)**  
  - **Vector**: Malicious packages (“chaotic-aur-helper” et al.) uploaded to Arch User Repository, installing Chaos RAT.  

- **Cross-Device WebAuthn Downgrade (PoisonSeed)**  
  - **Vector**: Victims scan a QR code, approving login via a secondary device, bypassing FIDO2 hardware-key enforcement.  

- **Fake AI Platform Malware Delivery (EncryptHub)**  
  - **Vector**: Impersonation of AI development services to trick Web3 developers into downloading “Fickle Stealer.”  

## Threat Actor Activities

- **EncryptHub / LARVA-208 (Water Gamayun)**  
  - **Campaign**: Fake AI platforms targeting Web3 developers; drops Fickle Stealer for crypto-wallet and browser-credential theft.  

- **Unknown Actor(s) exploiting SharePoint Zero-Days**  
  - **Campaign**: Large-scale mass scanning and breach of over 75 organizations, deploying web-shells and staging data exfiltration.  

- **Unknown Actor(s) exploiting CrushFTP**  
  - **Campaign**: Targeted intrusions against file-transfer servers in technology and healthcare sectors to steal sensitive data.  

- **PoisonSeed**  
  - **Campaign**: Phishing operations that bypass FIDO2 MFA by leveraging WebAuthn cross-device flows; focuses on financial services employees.  

- **APT28 (Fancy Bear)**  
  - **Campaign**: “Authentic Antics” malware steals Microsoft 365 credentials; activity linked to Russian GRU for espionage objectives.