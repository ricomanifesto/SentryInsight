# Exploitation Report

During the past week, defenders observed a sharp rise in active exploitation and supply-chain compromise. The most critical activity centres on a zero-day authentication bypass in CrushFTP (CVE-2025-54309) that grants full administrative control of vulnerable servers. Simultaneously, new, still-unnamed zero-days in Ivanti Connect Secure/Policy Secure are being chained to drop the MDifyLoader malware and execute in-memory Cobalt Strike beacons. On the trade-craft side, the “PoisonSeed” campaign is sidestepping FIDO2 hardware keys by abusing WebAuthn’s cross-device sign-in, while separate threat groups hijacked two of the most-used npm linter packages and several Arch Linux AUR packages to distribute remote-access malware. Russia-linked APT28 (“Fancy Bear”) is running stealthy credential-theft operations against Microsoft 365 tenants, and espionage cluster UNG0002 is leveraging LNK files to implant RATs across East Asia. Collectively, these events highlight escalating attacker focus on identity-based attacks, developer ecosystems, and edge-device zero-days.

## Active Exploitation Details

### CrushFTP Web Interface Authentication Bypass  
- **Description**: A logic flaw lets remote, unauthenticated users craft a rogue session and elevate it to administrator level through the web interface.  
- **Impact**: Attackers can create admin accounts, upload arbitrary plug-ins, execute system commands, and fully hijack the underlying server.  
- **Status**: Actively exploited in the wild. Vendor released fixed builds (latest 11.x/10.x/9.x) and urges immediate upgrade.  
- **CVE ID**: CVE-2025-54309  

### Ivanti Connect Secure / Policy Secure Zero-Day Chain  
- **Description**: A pair of newly discovered flaws—one granting authentication bypass and another enabling command injection—allow remote actors to deliver the MDifyLoader downloader, followed by in-memory Cobalt Strike payloads.  
- **Impact**: Full device compromise, lateral movement into internal networks, and persistent access for follow-on operations.  
- **Status**: Exploits observed before public disclosure; Ivanti has released hot-fixes and mitigations while preparing full patches.  

### FIDO2 MFA Downgrade via WebAuthn Cross-Device Abuse (PoisonSeed)  
- **Description**: Attackers trigger the “cross-device sign-in” flow, surfacing a QR code that convinces victims to approve a login on a secondary device, silently downgrading from hardware-bound FIDO2 to less-secure push approval.  
- **Impact**: Session takeover of accounts protected by security-key-based MFA, enabling email and cloud-service access.  
- **Status**: Ongoing phishing waves; no vendor patch required, but security-key policy hardening is advised.  

### npm Package Maintainer Account Takeover (eslint-config-prettier & eslint-plugin-prettier)  
- **Description**: Phishing emails stole maintainer credentials, after which malicious versions with obfuscated post-install scripts were published to npm, turning the libraries into malware droppers.  
- **Impact**: Developers who installed the tainted packages received info-stealing malware capable of exfiltrating tokens and environment secrets.  
- **Status**: Malicious versions yanked; legitimate packages republished. Users must audit build environments and rotate credentials.  

### Arch Linux AUR Chaos RAT Supply-Chain Infection  
- **Description**: Three community AUR packages were replaced with code that fetched and launched Chaos RAT, giving attackers shell access and persistence on Linux hosts.  
- **Impact**: Remote command execution, data exfiltration, and potential lateral movement on developer workstations and servers.  
- **Status**: Packages removed from AUR; impacted users instructed to rebuild systems from trusted sources and revoke compromised keys.  

### Microsoft 365 “Authentic Antics” Credential-Stealing Malware  
- **Description**: APT28 deployed a bespoke malware framework that impersonates legitimate add-ins to capture authentication cookies, tokens, and mailbox contents from Microsoft 365 tenants.  
- **Impact**: Long-term espionage through email collection, document theft, and potential spread via internal contact lists.  
- **Status**: Active; Microsoft & UK NCSC released indicators and recommend conditional-access hardening and add-in governance.  

## Affected Systems and Products

- **CrushFTP Server 9, 10, 11**: All platforms (Windows, Linux, macOS) prior to patched builds  
- **Ivanti Connect Secure / Policy Secure**: All supported hardware and virtual gateways on unpatched firmware  
- **npm packages**: eslint-config-prettier v9.1.0 – v9.1.1, eslint-plugin-prettier v5.1.0 – v5.1.1  
- **Arch Linux AUR**: `ruby-filemagic`, `libarchive`, and `nodejs-webpack` (malicious uploads)  
- **Microsoft 365 Tenants**: Organisations allowing unmanaged add-ins or lacking strict identity governance  
- **Enterprise MFA Deployments**: Any service relying on WebAuthn cross-device flows without strict security-key enforcement  

## Attack Vectors and Techniques

- **Authentication Bypass via Session Forging**  
  - *Vector*: Crafted HTTP requests manipulate CrushFTP session tokens to gain admin privileges.  

- **Zero-Day Command Injection on VPN Gateways**  
  - *Vector*: Chained auth bypass and shell command injection on Ivanti edge devices deliver MDifyLoader.  

- **QR-Code Phishing for MFA Downgrade**  
  - *Vector*: PoisonSeed emails redirect to fake login portals that generate WebAuthn QR codes, tricking users into approving rogue logins.  

- **Package Maintainer Phishing & Malicious Post-Install Scripts**  
  - *Vector*: Stolen npm credentials publish trojanised packages; scripts execute `curl | bash` logic to drop malware.  

- **Repository Poisoning in AUR**  
  - *Vector*: Attackers upload altered PKGBUILDs containing `curl` commands that fetch Chaos RAT binaries during package compilation.  

- **Malicious Microsoft 365 Add-in Installation**  
  - *Vector*: Spear-phishing or OAuth consent grants install add-ins that exfiltrate tokens and mailbox data.  

## Threat Actor Activities

- **Unknown (CrushFTP Exploits)**  
  - *Campaign*: Opportunistic mass scanning and exploitation to build botnets or gain footholds in enterprise networks.  

- **Unidentified Threat Cluster (Ivanti Zero-Day)**  
  - *Campaign*: Targeted intrusion sets against government and telecom sectors, delivering MDifyLoader → Cobalt Strike.  

- **PoisonSeed**  
  - *Campaign*: Global phishing operation focusing on finance and tech employees, bypassing hardware MFA controls.  

- **Supply-Chain Intruder(s)**  
  - *Campaign*: Credential-phishing of open-source maintainers, weaponising popular npm packages to infect developer environments.  

- **APT28 (Fancy Bear / Russian GRU)**  
  - *Campaign*: “Authentic Antics” espionage, harvesting Microsoft 365 credentials and data from government and defence entities.  

- **UNG0002**  
  - *Campaign*: Dual operations in China, Hong Kong, and Pakistan using LNK files and RATs for cyber-espionage.  

