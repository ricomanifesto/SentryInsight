# Exploitation Report

Over the last week, threat activity has centered on two critical zero-day vulnerabilities—one in Microsoft SharePoint Server (CVE-2025-53770 / CVE-2025-53771) and another in CrushFTP (CVE-2025-54309)—both of which are undergoing large-scale, in-the-wild exploitation that enables remote code execution or full administrative takeover of enterprise systems. Simultaneously, the ecosystem is being pressured by multiple supply-chain compromises (malicious npm and Arch AUR packages), advanced phishing operations that bypass FIDO2 MFA (PoisonSeed), and a financially-motivated campaign by EncryptHub targeting Web3 developers with the “Fickle Stealer” infostealer. These overlapping attack waves underscore an urgent need for rapid mitigation, continuous monitoring, and defense-in-depth across collaboration platforms, file-transfer services, developer supply chains, and authentication workflows.

## Active Exploitation Details

### Microsoft SharePoint Server Remote Code Execution Zero-Days
- **Description**: Two separate but related SharePoint Server flaws allow unauthenticated remote code execution through crafted requests that abuse the server-side deserialization logic exposed by vulnerable API endpoints.  
- **Impact**: Attackers gain SYSTEM-level command execution, steal SharePoint data, drop web-shells, and pivot deeper into corporate networks. Reports already cite breaches of 75+ company servers.  
- **Status**: Actively exploited since at least 18 July; no official patch yet. Microsoft has released mitigation guidance involving blocking specific endpoints and disabling preview features.  
- **CVE ID**: CVE-2025-53770  
- **CVE ID**: CVE-2025-53771  

### CrushFTP Server Administrative Access Zero-Day
- **Description**: A path-traversal and session-poisoning flaw in CrushFTP’s web interface lets unauthenticated users read arbitrary files, hijack live sessions, and escalate to full administrator control.  
- **Impact**: Complete compromise of file-transfer servers, exfiltration or tampering of hosted data, and deployment of additional malware.  
- **Status**: Confirmed active exploitation. Vendor released fixed builds (10.7.1 / 11.1.1 and later); admins must update immediately or deploy vendor-supplied hot-fix.  
- **CVE ID**: CVE-2025-54309  

## Affected Systems and Products

- **Microsoft SharePoint Server 2016/2019/Subscription Edition**  
  - **Platform**: Windows Server on-prem deployments (cloud SharePoint Online not affected)

- **CrushFTP Server 9.x – 11.1.0 (all editions)**  
  - **Platform**: Windows, Linux, macOS, and any JVM-capable OS

- **npm Ecosystem Packages** (`eslint-config-prettier`, `eslint-plugin-prettier`, plus five hijacked modules)  
  - **Platform**: Cross-platform Node.js development environments

- **Arch Linux AUR Packages** (three malicious uploads distributing Chaos RAT)  
  - **Platform**: Linux desktops/servers using AUR helpers

- **Aruba Instant On Access Points** (hard-coded credential issue—no exploitation observed yet)  
  - **Platform**: Hardware appliance running Aruba Instant On firmware

- **Web3 Development Workstations** targeted by EncryptHub  
  - **Platform**: Primarily Windows environments used for blockchain and smart-contract development

## Attack Vectors and Techniques

- **Deserialization RCE (SharePoint)**  
  - **Vector**: Crafted HTTP POST to vulnerable API triggers gadget chain execution under `w3wp.exe`.

- **Path Traversal & Session Poisoning (CrushFTP)**  
  - **Vector**: Manipulated URL parameters retrieve session files, then weaponize session IDs for admin takeover.

- **Supply-Chain Token Hijack (npm)**  
  - **Vector**: Phishing steals maintainer tokens → malicious package update pushes infostealer payloads to users.

- **Malicious AUR Upload**  
  - **Vector**: Trojanized PKGBUILD scripts download Chaos RAT during package build/install.

- **Fake AI Platform Malware Dropper (EncryptHub)**  
  - **Vector**: Social-engineering lures Web3 developers to “AI coding assistants” that sideload Fickle Stealer.

- **FIDO2 MFA Downgrade (PoisonSeed)**  
  - **Vector**: Phishing email → victim scans QR code → WebAuthn cross-device sign-in downgraded to approving push prompt on compromised device.

## Threat Actor Activities

- **EncryptHub / LARVA-208 / Water Gamayun**  
  - **Campaign**: Fake AI dev tools deliver Fickle Stealer to Web3 developers, harvesting wallets, browser cookies, and SSH keys.

- **Unidentified SharePoint Exploitation Cluster**  
  - **Campaign**: Mass scanning of Internet-exposed SharePoint servers; post-exploitation includes Cobalt Strike beacons and data theft.

- **Multiple Crimeware Crews (CrushFTP)**  
  - **Campaign**: Opportunistic exploitation for data exfiltration and ransomware staging on unpatched file-transfer servers.

- **PoisonSeed**  
  - **Campaign**: Large-scale phishing binge targeting enterprise employees, aiming to sidestep hardware security keys and hijack Microsoft 365 accounts.

- **APT28 / Fancy Bear (Authentic Antics)**  
  - **Campaign**: Credential-stealing malware targeting Microsoft 365 tenants for espionage, aligned with Russian GRU operations.

- **Unknown Actors (npm & AUR Supply Chain)**  
  - **Campaign**: Credential phishing of open-source maintainers followed by package hijacking to distribute RATs and info-stealers to downstream developers.

**End of Report**