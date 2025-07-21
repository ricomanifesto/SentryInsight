# Exploitation Report

A surge of high-impact exploitation activity is underway, led by weaponization of two Microsoft SharePoint Server remote-code-execution (RCE) zero-days (CVE-2025-53770 and CVE-2025-53771) that have already breached dozens of organizations worldwide. Simultaneously, attackers are abusing a critical path-traversal flaw in CrushFTP (CVE-2025-54309) to seize administrative control of unpatched file-transfer servers. Beyond direct software vulnerabilities, the PoisonSeed threat group is sidestepping FIDO2 hardware keys through a novel QR-code phishing downgrade, while large-scale cryptojacking and supply-chain compromise campaigns continue to erode trust in web infrastructure and developer ecosystems. Security teams should prioritize emergency patching, harden authentication workflows, and monitor for the techniques outlined below.

## Active Exploitation Details

### Microsoft SharePoint Server RCE Zero-Days
- **Description**: Two independent input-validation issues allow remote, unauthenticated attackers to upload malicious ASPX pages that execute with SharePoint service privileges.
- **Impact**: Full remote code execution, lateral movement into on-prem and cloud-connected Active Directory environments, data exfiltration, and potential ransomware deployment.
- **Status**: Actively exploited since at least 18 July 2025 in “ToolShell” campaigns; emergency out-of-band patches are now available from Microsoft.
- **CVE ID**: CVE-2025-53770  
- **CVE ID**: CVE-2025-53771  

### CrushFTP Path-Traversal RCE
- **Description**: A directory-traversal logic flaw lets authenticated or sometimes unauthenticated users break out of the virtual file system, overwrite configuration files, and trigger arbitrary code execution.
- **Impact**: Attackers gain administrative rights on the server, harvest stored credentials, and pivot to internal networks hosting sensitive data.
- **Status**: Under active exploitation in the wild; vendor has issued patched builds and advises immediate upgrade.
- **CVE ID**: CVE-2025-54309  

### FIDO2 / WebAuthn Cross-Device Sign-In Abuse
- **Description**: PoisonSeed leverages WebAuthn’s cross-device sign-in flow to downgrade strong FIDO2 hardware-key authentication. Victims are lured to scan a QR code that silently proxies authentication to the attacker.
- **Impact**: Account takeover of high-value cloud and SaaS assets even when hardware security keys are enforced.
- **Status**: Ongoing phishing campaign; no software patch required, but mitigations involve disabling cross-device sign-ins and enforcing origin checks.

### JavaScript Cryptojacking Mass-Injection
- **Description**: Over 3,500 legitimate websites were compromised to serve an obfuscated browser-based Monero miner that communicates via WebSockets to evade Content-Security-Policy controls.
- **Impact**: Visitor CPU hijacking, monetization for attackers, site-reputation damage, and possible follow-on malware delivery.
- **Status**: Campaign active; affected sites must remove injected scripts and harden CMS/plugin security.

### npm Package Hijacking via Token Theft
- **Description**: Phishing emails stole maintainer tokens, allowing adversaries to publish backdoored versions of popular linting packages (`eslint-config-prettier`, `eslint-plugin-prettier`, and others).
- **Impact**: Downstream developers unknowingly execute malware during build pipelines, leading to workstation infection and CI/CD compromise.
- **Status**: Malicious package versions have been yanked; developers should audit dependency trees and rotate stolen tokens.

## Affected Systems and Products

- **Microsoft SharePoint Server**: 2019, 2022, and Subscription Edition on Windows Server platforms  
- **CrushFTP**: Versions 10.3.0 and earlier on Windows, Linux, and macOS servers  
- **Enterprise Identity Platforms**: Any environment using WebAuthn cross-device sign-in with FIDO2 hardware keys (Chrome, Edge, Firefox across desktop/mobile)  
- **Compromised Websites**: Sites running vulnerable or poorly maintained CMS plugins/frameworks (WordPress, Magento, custom stacks)  
- **npm Ecosystem**: Projects importing hijacked packages—primarily JavaScript/TypeScript developer workstations and CI services  

## Attack Vectors and Techniques

- **Malicious ASPX Upload (SharePoint ToolShell)**  
  - **Vector**: Crafted API calls or SOAP requests upload a web shell page, then trigger execution via standard SharePoint endpoints.

- **Path Traversal to Config Overwrite (CrushFTP)**  
  - **Vector**: Manipulated file paths (`../../`) escape the virtual file system, enabling replacement of `users.xml` to escalate privileges.

- **QR Phishing Downgrade (PoisonSeed)**  
  - **Vector**: Victim scans attacker-controlled QR code; the session is proxied so that authentication occurs on the attacker’s device, not the legitimate origin.

- **WebSocket-Based Cryptojacking**  
  - **Vector**: Injected `<script>` downloads an obfuscated miner, opens a persistent WebSocket to mining pool, bypassing traditional HTTP inspection.

- **npm Token Phishing & Malicious Publish**  
  - **Vector**: Spear-phishing steals one-time passwords and tokens, adversary publishes sabotaged package versions that execute post-install scripts.

## Threat Actor Activities

- **ToolShell Group**  
  - **Campaign**: Exploiting SharePoint zero-days for foothold, dropping custom PowerShell payloads, targeting finance, healthcare, and government sectors.

- **PoisonSeed**  
  - **Campaign**: QR-code phishing against corporate Office 365 and Google Workspace tenants; primary objective is credential theft for BEC and data exfiltration.

- **Unknown Cryptojacking Collective**  
  - **Campaign**: Mass exploitation of weak CMS plugins to inject JavaScript miners; profits routed through privacy-centric cryptocurrency pools.

- **EncryptHub (LARVA-208 / Water Gamayun)**  
  - **Campaign**: Distributing “Fickle Stealer” malware to Web3 developers via spoofed AI SaaS platforms, harvesting browser wallets and SSH keys.

- **Supply-Chain Intruders (npm)**  
  - **Campaign**: Phishing maintainers, hijacking linting packages to deploy reconnaissance backdoors in developer environments.

Security teams should apply released patches immediately, disable risky authentication flows where possible, perform web-shell and miner scans, and validate integrity of all development dependencies.