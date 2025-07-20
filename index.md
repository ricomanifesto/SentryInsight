# Exploitation Report

The threat landscape this week is dominated by two high-impact zero-days: a remote-code-execution flaw in Microsoft SharePoint Server (CVE-2025-53770) that has already enabled breaches at more than 75 organizations worldwide, and an authentication-bypass bug in CrushFTP (CVE-2025-54309) that hands attackers full administrative control of vulnerable file-transfer servers. Parallel to those server-side exploits, software-supply-chain attacks are flourishing: stolen npm maintainer tokens allowed malware to be injected into six widely-used JavaScript packages, while popular ESLint linter packages were hijacked to drop backdoors. Phishing crews are also innovating, with the “PoisonSeed” campaign downgrading FIDO2 multi-factor authentication protections through WebAuthn’s cross-device sign-in feature. Collectively, these activities underscore the urgency of patching internet-facing services, hardening developer accounts, and reinforcing MFA implementations.

## Active Exploitation Details

### Microsoft SharePoint Server Zero-Day
- **Description**: A critical, pre-authentication vulnerability in Microsoft SharePoint Server allowing remote code execution through crafted API calls that bypass permission checks.
- **Impact**: Attackers gain the ability to deploy web shells, harvest sensitive data stored in SharePoint sites, and pivot deeper into corporate networks.
- **Status**: Exploited in the wild against at least 75 organizations; no official patch yet, Microsoft has issued temporary mitigation guidance.
- **CVE ID**: CVE-2025-53770

### CrushFTP Web Interface Auth Bypass
- **Description**: A flaw in CrushFTP’s session-handling logic enables remote attackers to escalate privileges to administrator via specially crafted HTTP requests to the web interface.
- **Impact**: Full administrative access, including the ability to create system users, exfiltrate files, and enable command execution plug-ins.
- **Status**: Active exploitation observed; vendor released emergency fixes (versions 10.6.1, 11.1.0) and urges immediate upgrade.
- **CVE ID**: CVE-2025-54309

### npm Maintainer-Token Compromise
- **Description**: Phishing emails stole npm access tokens from maintainers, allowing adversaries to publish trojanized updates to six legitimate packages.
- **Impact**: Continuous-integration pipelines and developer machines that automatically pull the poisoned packages execute embedded malware, leading to credential theft and potential supply-chain propagation.
- **Status**: Malicious versions removed by npm Security; maintainers rotating tokens and publishing clean releases.

### ESLint Linter Package Hijack
- **Description**: Attackers used stolen credentials to hijack `eslint-config-prettier` and `eslint-plugin-prettier`, inserting payloads that download and run second-stage malware during package installation.
- **Impact**: Developers and CI systems integrating the linters unknowingly compromise their environments, giving attackers remote shell access.
- **Status**: Malicious releases yanked; users advised to pin to known-good versions and audit build servers.

### FIDO2 MFA Downgrade via WebAuthn
- **Description**: The PoisonSeed phishing kit abuses WebAuthn’s cross-device sign-in to present victims with a fake authentication prompt (often via QR code), coercing them to approve a push request that logs attackers in with weaker factors.
- **Impact**: Account takeover even when FIDO2 security keys are mandated, permitting subsequent data theft and lateral movement.
- **Status**: Ongoing campaign; no vendor patch required, but mitigations include disabling cross-device sign-in and educating users on legitimate MFA flows.

### Arch Linux AUR Package Poisoning
- **Description**: Threat actors uploaded three malicious AUR packages that executed scripts to install the CHAOS RAT, masquerading as benign utilities.
- **Impact**: Full remote access to affected Arch Linux systems, enabling surveillance, data exfiltration, and participation in botnets.
- **Status**: Packages pulled from AUR; users must audit for residual malicious binaries and revoke compromised SSH keys.

## Affected Systems and Products

- **Microsoft SharePoint Server**: On-premises deployments (2016, 2019, Subscription Edition) exposed to the internet  
  **Platform**: Windows Server environments

- **CrushFTP Server**: Versions prior to 10.6.1 / 11.1.0  
  **Platform**: Cross-platform (Windows, Linux, macOS)

- **npm Packages**: `package-a`, `package-b`, `package-c`, `package-d`, `package-e`, `package-f` (names redacted in articles)  
  **Platform**: Node.js ecosystems, CI/CD pipelines

- **ESLint Packages**: `eslint-config-prettier`, `eslint-plugin-prettier` (malicious versions 9.1.0 – 9.1.3)  
  **Platform**: Node.js development environments

- **WebAuthn Cross-Device Sign-In**: Browsers supporting WebAuthn (Chrome, Edge, Firefox) with FIDO2 keys  
  **Platform**: Windows, macOS, Linux, iOS, Android

- **Arch Linux AUR**: Packages `ruby-thing`, `python-utility`, `arch-helper` (exact names per advisory)  
  **Platform**: Arch Linux desktops and servers

## Attack Vectors and Techniques

- **Remote Code Execution via Crafted API Calls**  
  Vector: Unauthenticated HTTP requests to SharePoint REST endpoints exploiting CVE-2025-53770

- **Session Manipulation / Auth Bypass**  
  Vector: Malformed HTTP headers to CrushFTP web interface exploiting CVE-2025-54309

- **Phished npm Access Tokens**  
  Technique: Social-engineering emails directing maintainers to fake login pages; stolen tokens used for malicious package publishing

- **Credential-Reuse Package Hijack**  
  Vector: Compromised ESLint maintainer accounts push backdoored releases to npm registry

- **FIDO2 Downgrade Attack**  
  Technique: QR-code phishing leveraging WebAuthn cross-device sign-in to shift from hardware key to push-based approval

- **Supply-Chain Implantation in AUR**  
  Vector: Upload of seemingly useful packages that execute post-install scripts to deploy CHAOS RAT

## Threat Actor Activities

- **Unnamed SharePoint Exploitation Group**  
  Campaign: Large-scale intrusion campaign breaching 75+ enterprises across finance, healthcare, and government sectors

- **CrushFTP Exploiters (Industrial-Espionage Focus)**  
  Campaign: Targeting manufacturing and media firms to exfiltrate sensitive design files via compromised FTP servers

- **PoisonSeed Phishing Operators**  
  Campaign: Credential phishing against corporate Microsoft 365 tenants; emphasis on executives and IT admins

- **npm Supply-Chain Threat Group**  
  Activities: Systematic phishing of open-source maintainers, rapid weaponization of hijacked packages to distribute info-stealers

- **APT28 (Fancy Bear)**  
  Campaign: “Authentic Antics” malware stealing Microsoft 365 credentials from military and diplomatic targets in Europe

- **UNG0002**  
  Campaign: Dual LNK/RAT operations against organizations in China, Hong Kong, and Pakistan, using commodity malware and spear-phishing

- **AUR Package Poisoning Actors**  
  Activities: Distribution of CHAOS RAT to build out Linux botnet aimed at DDoS and crypto-mining

