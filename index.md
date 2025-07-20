# Exploitation Report

Over the past week, threat actors have ramped up attacks that blend zero-day exploitation with clever social-engineering and software-supply-chain compromise. The most critical activity centers on the active exploitation of a new CrushFTP zero-day (CVE-2025-54309) that grants unauthenticated administrative control of file-transfer servers. Concurrently, attackers are abusing unpatched flaws in Ivanti Connect Secure/Policy Secure appliances to implant the in-memory “MDifyLoader” malware, while other groups are bypassing FIDO2 security-key protections through a PoisonSeed phishing campaign. Supply-chain defenders also face renewed pressure after popular npm linter packages and Arch Linux AUR packages were hijacked to distribute malware. Nation-state and financially motivated actors—including APT28, UNG0002, and an unidentified group behind the npm incident—are leveraging these weaknesses for espionage, credential theft, and large-scale access operations.

---

## Active Exploitation Details

### CrushFTP Web Interface Authentication Bypass
- **Description**: A zero-day flaw in CrushFTP allows remote attackers to elevate privileges by creating or hijacking an administrative session through crafted web-interface requests.  
- **Impact**: Full administrative control of affected servers, enabling data theft, configuration changes, and arbitrary code execution.  
- **Status**: Actively exploited in the wild. CrushFTP has issued mitigations and updated builds; administrators are urged to patch immediately.  
- **CVE ID**: CVE-2025-54309  

### Ivanti Connect Secure / Policy Secure Unpatched Remote-Code Flaws
- **Description**: Multiple previously unknown vulnerabilities in Ivanti’s VPN and NAC gateways are being chained to drop the “MDifyLoader” malware and execute Cobalt Strike beacons purely in memory.  
- **Impact**: Remote code execution, persistent access to corporate networks, and facilitation of follow-on ransomware or espionage activity.  
- **Status**: Zero-day exploitation observed; Ivanti has released security advisories and fixes, but many appliances remain unpatched in production.  

### PoisonSeed FIDO2 MFA Downgrade Attack
- **Description**: Phishing campaign abuses WebAuthn’s cross-device sign-in feature. Victims scan a QR code that silently downgrades FIDO2 hardware-key authentication to a less secure method, tricking users into approving malicious sessions.  
- **Impact**: Account takeover despite hardware security-key protections, leading to email or cloud-service compromise.  
- **Status**: Ongoing; no vendor patch required—mitigations include disabling cross-device sign-in and strengthening user awareness.  

### npm Package Hijacking (eslint-config-prettier & eslint-plugin-prettier)
- **Description**: Attackers phished maintainers’ npm credentials, published malicious versions that execute preinstall scripts to fetch additional payloads.  
- **Impact**: Supply-chain infection of developer machines, credential theft, and potential lateral movement into CI/CD environments.  
- **Status**: Malicious releases detected and removed; maintainers re-claimed control and published clean updates.  

### Arch Linux AUR Malicious Packages
- **Description**: Three AUR packages were seeded with post-install scripts that retrieved the CHAOS Remote Access Trojan.  
- **Impact**: Full remote access to affected Linux hosts, data exfiltration, and use in botnet activity.  
- **Status**: Packages pulled from AUR and flagged; users must audit and cleanse compromised systems.  

### Authentic Antics Microsoft 365 Credential-Stealing Malware
- **Description**: Stealthy malware framework attributed to APT28 leverages malicious OAuth applications and phishing pages to harvest Microsoft 365 credentials without triggering MFA alerts.  
- **Impact**: Long-term espionage access to government and defense-sector mailboxes and documents.  
- **Status**: Active campaign; Microsoft and NCSC issued guidance to audit OAuth app permissions and logins.  

### UNG0002 LNK & RAT Campaigns
- **Description**: The UNG0002 cluster delivers weaponized LNK files that side-load remote-access trojans in attacks on entities in China, Hong Kong, and Pakistan.  
- **Impact**: Initial access, surveillance, and data theft across public and private sector networks.  
- **Status**: Ongoing espionage activity; defenders advised to block LNK execution and tighten attachment controls.  

### MCP Server Default-Auth Exposure
- **Description**: Nearly 2,000 MCP servers are deployed with optional (often disabled) authentication, allowing unfettered control to any remote user.  
- **Impact**: Complete server takeover, manipulation of agentic-AI workloads, and pivoting into connected infrastructure.  
- **Status**: Wide-scale exposure remains; remediation requires enabling authentication and network-level access controls.  

---

## Affected Systems and Products

- **CrushFTP**: Versions prior to emergency build 10.x/11.x hotfix on Windows, Linux, and macOS servers  
- **Ivanti Connect Secure & Policy Secure**: All unpatched appliance firmware versions globally deployed in VPN/NAC roles  
- **WebAuthn / FIDO2-enabled Web Services**: Any service allowing cross-device sign-in, notably enterprise SSO and cloud email platforms  
- **eslint-config-prettier / eslint-plugin-prettier (npm)**: Malicious versions 9.0.0 and 5.1.1 (respectively) published during attack window  
- **Arch Linux AUR**: Packages “initiate-systemd,” “ipp-usb-git,” and “onerng” (malicious revisions now removed)  
- **Microsoft 365 Tenants**: Organizations that permitted unverified OAuth apps or experienced phishing exposure  
- **Windows Desktops/Servers**: Targets that execute LNK attachments delivered by UNG0002 campaigns  
- **MCP Framework Servers**: Instances exposed to the internet without authentication across all supported OS platforms  

---

## Attack Vectors and Techniques

- **Cross-Device WebAuthn Abuse**  
  - **Vector**: QR codes in phishing emails redirect victims to attacker-controlled authentication sessions, downgrading FIDO2 protections.  

- **Supply-Chain Package Poisoning**  
  - **Vector**: Compromised npm / AUR accounts publish trojanized packages with pre/post-install scripts fetching remote malware.  

- **Zero-Day Remote Code Execution (RCE)**  
  - **Vector**: Exploit of CrushFTP and Ivanti web endpoints to create admin accounts or execute arbitrary commands on appliances.  

- **Malicious OAuth Application Registration**  
  - **Vector**: Attackers register rogue Azure AD apps and trick users into granting excessive permissions, bypassing MFA.  

- **Weaponized LNK Files & DLL Side-Loading**  
  - **Vector**: Email attachments containing crafted LNK shortcuts that load trojans from remote shares or temp directories.  

- **Unauthenticated Service Exposure**  
  - **Vector**: MCP servers shipped with authentication disabled, allowing direct HTTP API manipulation by external actors.  

---

## Threat Actor Activities

- **APT28 (Fancy Bear)**  
  - **Campaign**: “Authentic Antics” targeting government and defense entities for Microsoft 365 credential theft; uses stealthy malware and malicious OAuth apps.  

- **PoisonSeed Operators**  
  - **Campaign**: Global phishing effort focusing on enterprise email platforms, leveraging QR-code MFA downgrades to bypass FIDO2.  

- **Unnamed Supply-Chain Actor (npm Incident)**  
  - **Campaign**: Hijacked two high-profile linter packages to propagate infostealers into developer environments.  

- **UNG0002 (Unknown Group 0002)**  
  - **Campaign**: Twin espionage operations using LNK files and RATs against organizations in China, Hong Kong, and Pakistan.  

- **CrushFTP Exploiters**  
  - **Campaign**: Opportunistic and targeted attacks against file-transfer servers in multiple sectors; focus on data exfiltration and staging for ransomware.  

- **Ivanti Zero-Day Operators**  
  - **Campaign**: Use of MDifyLoader and in-memory Cobalt Strike to breach corporate VPN gateways, likely for initial-access brokering.  

- **Chaos RAT Distributors**  
  - **Campaign**: Malicious Arch Linux AUR maintainers seeding packages to conscript Linux workstations into remote-access botnets.  

- **Opportunistic Attackers on MCP Servers**  
  - **Campaign**: Automated scanning and exploitation of unauthenticated MCP endpoints for unrestricted server control.  

---

**End of Report**