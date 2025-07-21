# Exploitation Report

A surge of high-impact zero-day activity is dominating the threat landscape. Attackers are chaining two Microsoft SharePoint Server remote-code-execution flaws (CVE-2025-53770 and CVE-2025-53771) in widespread “ToolShell” intrusions that have already breached more than 80 organizations. Simultaneously, a critical authentication-bypass flaw in CrushFTP (CVE-2025-54309) is being weaponized to seize full administrative control of file-transfer servers. Both vendors have now issued out-of-band patches, but exploitation continues against unpatched assets. Parallel campaigns involving large-scale cryptojacking of 3,500 websites, supply-chain attacks on npm packages, and advanced phishing operations highlight a rapidly evolving ecosystem of techniques that circumvent MFA, poison development pipelines, and monetize compromised infrastructure.

## Active Exploitation Details

### Microsoft SharePoint Server RCE – CVE-2025-53770  
- **Description**: A zero-day remote code execution flaw in SharePoint’s web services layer, triggered by specially crafted API requests that bypass normal validation and allow arbitrary code upload/execution under the SharePoint service context.  
- **Impact**: Full takeover of the SharePoint server, deployment of web shells, credential theft, and lateral movement inside corporate networks.  
- **Status**: Actively exploited since 18 July 2025; emergency patches released by Microsoft.  
- **CVE ID**: CVE-2025-53770  

### Microsoft SharePoint Server RCE – CVE-2025-53771  
- **Description**: Companion zero-day in SharePoint that permits privilege escalation and code execution through improper authentication handling, often chained with CVE-2025-53770 in “ToolShell” attacks.  
- **Impact**: Enables attackers to achieve SYSTEM-level execution, persistent access, and data exfiltration.  
- **Status**: Exploited in the same campaign; fixed via out-of-band updates issued concurrently with CVE-2025-53770.  
- **CVE ID**: CVE-2025-53771  

### CrushFTP Authentication Bypass – CVE-2025-54309  
- **Description**: A path-traversal logic flaw in CrushFTP that lets unauthenticated users craft requests to hijack valid admin sessions and gain full control of the web interface.  
- **Impact**: Attackers obtain administrative privileges, exfiltrate stored files, create backdoor accounts, and pivot to internal networks.  
- **Status**: Under active exploitation in the wild; vendor released patched builds (10.7.1/11.1) and hot-fixes.  
- **CVE ID**: CVE-2025-54309  

## Affected Systems and Products

- **Microsoft SharePoint Server 2016 / 2019 / Subscription Edition**  
  - **Platform**: Windows Server deployments (on-premises and hybrid)
  
- **CrushFTP 10.x and earlier (all platforms)**  
  - **Platform**: Cross-platform Java application on Windows, Linux, macOS

- **Compromised Websites (3,500+ sites running various CMS stacks)**  
  - **Platform**: Public-facing web servers using JavaScript-enabled browsers

- **npm Ecosystem – eslint-config-prettier, eslint-plugin-prettier, and additional hijacked packages**  
  - **Platform**: Node.js development environments on all operating systems

## Attack Vectors and Techniques

- **ToolShell Exploit Chain**  
  - **Vector**: Malicious SOAP/REST requests upload weaponized .aspx payloads to SharePoint, spawning web shells and reverse shells.

- **CrushFTP Session Hijack**  
  - **Vector**: Crafted URL path traversal forces server to treat attacker as an authenticated admin session.

- **Stealth Cryptojacking Injection**  
  - **Vector**: Obfuscated JavaScript loaded from compromised CDN domain leverages WebSocket tunneling to mine cryptocurrency in visitors’ browsers.

- **npm Supply-Chain Poisoning**  
  - **Vector**: Stolen maintainer tokens used to push trojanized package versions that execute post-install scripts to drop malware.

- **PoisonSeed MFA Downgrade Phishing**  
  - **Vector**: Abuse of WebAuthn cross-device sign-in prompts victims to approve fraudulent FIDO2 requests, bypassing hardware-key enforcement.

- **Fake AI Platform Malware Delivery**  
  - **Vector**: Lure websites offering “AI coding assistants” trick Web3 developers into downloading installers that deploy Fickle Stealer.

## Threat Actor Activities

- **ToolShell Cluster**  
  - **Campaign**: Coordinated exploitation of SharePoint zero-days to deploy proprietary “ToolShell” backdoor; targets government, finance, and manufacturing sectors worldwide.

- **Unidentified Threat Actors Targeting CrushFTP**  
  - **Campaign**: Mass scanning and automated exploitation of CVE-2025-54309 to create rogue admin accounts and exfiltrate sensitive archives.

- **Cryptojacking Collective (unnamed)**  
  - **Campaign**: Compromise of 3,500 legitimate sites; monetization via browser-based Monero mining leveraging stealth WebSocket channels.

- **EncryptHub (aka LARVA-208 / Water Gamayun)**  
  - **Campaign**: Social-engineering Web3 developers with fake AI tools, delivering Fickle Stealer to harvest wallets, browser data, and IDE credentials.

- **PoisonSeed Phishing Group**  
  - **Campaign**: Bypass of FIDO2 MFA through cross-device prompts; focuses on enterprise email and cloud-service accounts for initial access.

- **npm Supply-Chain Attacker (unknown)**  
  - **Campaign**: Phishing of open-source maintainers, hijacking popular linter packages to propagate malware inside CI/CD pipelines.

