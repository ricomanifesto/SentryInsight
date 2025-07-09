# Exploitation Report

Threat activity over the last week highlights a sharp uptick in real-world exploitation of both newly disclosed and long-standing vulnerabilities. The most critical events include active weaponisation of a publicly disclosed Microsoft SQL Server zero-day that was patched only this week, large-scale abuse of unpatched flaws in TBK digital video recorders (DVRs) and Four-Faith industrial routers to fuel the emerging “RondoDox” DDoS botnet, and a novel “TapTrap” technique that bypasses Android’s permission model through invisible UI overlays. In parallel, supply-chain attacks are expanding—most notably the compromise of the Ethcode VS Code extension and the use of malicious Chrome extensions with 1.7 million installations—while nation-state groups such as North Korea’s Andariel and China-linked Silk Typhoon continue to leverage exploited weaknesses for espionage, fraud, and ransomware operations.

## Active Exploitation Details

### Microsoft SQL Server Zero-Day Remote Code Execution
- **Description**: A vulnerability in the query processing component of Microsoft SQL Server allows authenticated attackers—or unauthenticated attackers who can leverage linked‐server scenarios—to execute arbitrary code with SQL Server service-account privileges.  
- **Impact**: Complete takeover of the database instance, lateral movement into connected Windows hosts, data theft, and potential deployment of ransomware.  
- **Status**: Publicly disclosed prior to patch release; now patched in July 2025 Patch Tuesday, but in-the-wild exploitation observed before fixes became broadly available.  

### TBK DVR Command Injection & Auth-Bypass Flaws
- **Description**: Multiple input-validation weaknesses in TBK digital video recorders enable unauthenticated attackers to execute shell commands or bypass login controls via crafted HTTP requests.  
- **Impact**: Attackers gain root-level control of DVRs, integrate devices into botnets, pivot into internal CCTV networks, or exfiltrate video streams.  
- **Status**: Actively exploited by the RondoDox botnet; no vendor patch confirmed at reporting time.  

### Four-Faith Industrial Router Vulnerabilities
- **Description**: Stack-based buffer overflows and weak default credential mechanisms in Four-Faith F-series cellular routers permit remote takeover over cellular or wired WAN links.  
- **Impact**: Full device compromise, disruption of industrial connectivity, and enlistment of routers into DDoS botnets.  
- **Status**: Exploited in the wild by RondoDox operators; remediation guidance limited to disabling remote management and changing defaults.  

### Android “TapTrap” UI-Animation Permission Bypass
- **Description**: A tapjacking-style flaw abuses Android’s animation stack to display invisible overlay elements on top of legitimate prompts, tricking users into approving dangerous permissions or actions.  
- **Impact**: Silent enabling of SMS read/send, accessibility services, or remote-admin modules, leading to data theft and potential full device control.  
- **Status**: Technique observed in active campaigns; no OS-level patch yet, mitigation requires user awareness and Play Protect detection updates.  

### Ethcode VS Code Extension Supply-Chain Compromise
- **Description**: Attackers submitted a malicious pull request that injected back-doored dependencies into the open-source Ethcode extension, subsequently pushed to the Visual Studio Code marketplace.  
- **Impact**: Compromised developer workstations receive remote‐access payloads capable of credential theft and code exfiltration.  
- **Status**: Malicious version live for several days; maintainers have pulled the tainted release, but over 6,000 installations remain at risk until manually updated.  

### Malicious Chrome Extensions Campaign
- **Description**: Eleven extensions hosted on the Chrome Web Store embedded obfuscated JavaScript that tracks browsing activity, harvests authentication cookies, and redirects victims to phishing domains.  
- **Impact**: Session hijacking, profile-wide credential theft, and large-scale user tracking across 1.7 million installs.  
- **Status**: Extensions removed by Google after disclosure, but compromised browsers remain vulnerable until users uninstall.  

### Shellter Tool Misuse for Stealer Delivery
- **Description**: Leaked license keys for the Shellter red-team framework are being reused by threat actors to wrap Lumma Stealer and SectopRAT binaries in legitimate-looking payloads that bypass AV/EDR.  
- **Impact**: Stealthy deployment of infostealers, leading to credential, crypto-wallet, and session cookie exfiltration.  
- **Status**: Ongoing; no inherent vulnerability in Shellter, but exploitation of trust in signed payloads is widespread.  

## Affected Systems and Products

- **Microsoft SQL Server 2014–2022 (all editions)**  
  - **Platform**: Windows Server 2016/2019/2022 and Azure SQL Managed Instance  

- **TBK DVR models DVS-AHD & DVS-IP**  
  - **Platform**: Embedded Linux-based CCTV recorders  

- **Four-Faith F3x/F8x Series Cellular Routers**  
  - **Platform**: ARM-based embedded Linux, industrial IoT deployments  

- **Android Smartphones/Tablets (Android 10-14)**  
  - **Platform**: All vendors; exploitation via malicious applications sideloaded or delivered through third-party stores  

- **Visual Studio Code “Ethcode” Extension (v1.3.0–1.3.2)**  
  - **Platform**: Windows, macOS, Linux developer workstations  

- **Google Chrome with Malicious Extensions (11 specific IDs, 1.7 M installs)**  
  - **Platform**: Windows, macOS, Linux, ChromeOS  

- **Shellter Framework (illicitly licensed builds)**  
  - **Platform**: Windows binaries used to generate AV-evasive payloads  

## Attack Vectors and Techniques

- **SQL Query Payload Injection**  
  - **Vector**: Crafted SQL statements delivered via compromised front-end apps or linked-server calls exploit the SQL Server RCE flaw.  

- **Unauthenticated HTTP API Abuse**  
  - **Vector**: Direct requests to `/cgi-bin/system` and similar endpoints on TBK DVRs and Four-Faith routers execute arbitrary shell commands.  

- **TapJacking via Invisible Animations**  
  - **Vector**: Malicious Android apps overlay zero-opacity views timed with UI animations, hijacking user taps to grant elevated permissions.  

- **Supply-Chain Pull Request Poisoning**  
  - **Vector**: Attackers contribute malicious code to open-source projects, which is then automatically built and published to official marketplaces.  

- **Malicious Extension Auto-Update**  
  - **Vector**: Chrome automatically updates installed extensions, silently deploying spyware code without user interaction.  

- **Shellter-Based Binary Repacking**  
  - **Vector**: Threat actors repackage stealers inside legitimate EXE files signed with Shellter, evading EDR through polymorphic shells.  

## Threat Actor Activities

- **Andariel (North Korea)**  
  - **Campaign**: Fraudulent IT-worker scheme and ransomware operations using stolen resumes and remote-infrastructure implants. Actively monetises access via cryptocurrency theft and extortion.  

- **Silk Typhoon (China-Linked)**  
  - **Campaign**: Multi-year espionage against US entities; recent arrest of Xu Zewei ties group to SQL Server exploitation for initial access.  

- **RondoDox Botnet Operators**  
  - **Campaign**: Mass scanning of port 37777 and cellular WAN IP ranges to compromise TBK DVRs and Four-Faith routers, assembling DDoS firepower for rent on illicit markets.  

- **TapTrap Campaign Actors (Unattributed)**  
  - **Campaign**: Distribute trojanised productivity and game apps on third-party Android stores, focusing on harvesting MFA codes and financial data.  

- **Shellter-Stealer Affiliates**  
  - **Campaign**: Use leaked Shellter licenses to re-sign Lumma Stealer, SectopRAT, Arechclient2, and Rhadamanthys, targeting gaming, crypto-trading, and developer communities.  

- **Anatsa Banking-Trojan Operators**  
  - **Campaign**: Published fake PDF-reader app on Google Play (>50 k installs), then pivoted victims to targeted overlay attacks against US banking apps.  

- **Malicious Chrome Extension Developers (Unknown Group)**  
  - **Campaign**: SEO-poisoned landing pages lured users to install “productivity” add-ons that exfiltrate browsing data and redirect to credential-harvesting sites.  

---

Security teams should prioritise patching SQL Server instances, isolate or retire vulnerable DVRs/routers, harden Android device policies to block sideloading, and audit development and browser extensions to mitigate the ongoing exploitation waves outlined above.