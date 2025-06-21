# Exploitation Report

During the last week, threat activity has centered on large-scale supply-chain tampering, credential-theft-driven intrusions, and abuse of protocol or platform weaknesses that remain largely unpatched in the field. Scattered Spider continued its high-impact social-engineering and identity-takeover assaults against U.K. retailers, while Salt Typhoon quietly compromised satellite-communications provider Viasat through an as-yet-undisclosed vulnerability. At the same time, threat actors weaponized GitHub as a delivery network for trojanized repositories, leveraged weaknesses in HTTP/2 to launch the largest 7.3 Tbps DDoS attack ever recorded, and exploited Android’s virtualization and overlay mechanisms to hijack banking and NFC transactions. Lazarus Group’s $11 million cryptocurrency theft underscores the ongoing risk of unaddressed security gaps in centralized exchanges. Collectively, these campaigns demonstrate attackers’ preference for identity abuse, software-supply-chain insertion, and protocol-level flaws that provide immediate, high-return access without relying on traditional endpoint exploits.

## Active Exploitation Details

### Scattered Spider Retail & Insurance Intrusions
- **Description**: Social-engineering and SIM-swapping tactics to seize employee credentials and cloud identity tokens, enabling lateral movement into Marks & Spencer, Co-op, and multiple U.S. insurance firms (including Aflac).  
- **Impact**: Data exfiltration, ransomware staging, and combined damages estimated at $592 million.  
- **Status**: Active; no specific vendor patch—mitigation hinges on hardening identity governance, MFA, and mobile carrier SIM-port protections.

### Salt Typhoon Satellite-Network Breach
- **Description**: Chinese state-aligned “Salt Typhoon” exploited an undisclosed vulnerability in Viasat’s enterprise environment to gain persistent access and conduct espionage.  
- **Impact**: Potential exposure of satellite customer telemetry, network designs, and partners’ communications.  
- **Status**: Confirmed in the wild; Viasat has implemented fixes but has not released technical indicators or a public patch.

### GitHub Trojanized Repository Campaign
- **Description**: Over 200 look-alike GitHub repositories were seeded with weaponized Python projects that deliver backdoors and infostealers to developers and gamers.  
- **Impact**: Remote code execution on developer endpoints, credential theft, and downstream supply-chain compromise of any software built with the infected code.  
- **Status**: Ongoing; GitHub is removing repos as they are discovered, but new copies continue to surface.

### Malicious Copycat Repos (Dark Reading Report)
- **Description**: Parallel campaign flooding GitHub with copycat versions of legitimate projects that embed malware in dependency chains.  
- **Impact**: Trust erosion in open-source ecosystems, automated CI/CD poisoning, and potential customer compromise when tainted code is shipped.  
- **Status**: Active; defenders must pin dependencies and use build-time validation.

### HTTP/2 Rapid-Reset Exploitation in 7.3 Tbps DDoS
- **Description**: Attackers abused the “rapid reset” weakness in the HTTP/2 protocol to generate an unprecedented volumetric DDoS wave peaking at 7.3 Tbps, delivering 37.4 TB in 45 seconds.  
- **Impact**: Service outages for the targeted hosting provider and collateral congestion across upstream networks.  
- **Status**: Exploit code widely available; no simple patch—mitigation requires rate-limiting and upgraded edge filtering rules.

### Android Virtualization & Overlay Abuse (Godfather/AntiDot)
- **Description**: Mobile malware families “Godfather” and “AntiDot” create isolated virtual containers and UI overlays that bypass standard app-sandbox boundaries to intercept banking credentials and NFC payment data.  
- **Impact**: Full account takeover, fraudulent transactions, and device hijacking on >3,700 confirmed Android handsets.  
- **Status**: Active; Google Play Protect updates shipped, but many third-party app stores remain exposed.

### Lazarus Group Exchange Exploit – BitoPro Heist
- **Description**: Lazarus compromised internal systems at Taiwanese exchange BitoPro, exploiting security gaps in hot-wallet management to siphon $11 million in crypto assets.  
- **Impact**: Direct financial theft, reputational damage, and regulatory scrutiny of regional crypto platforms.  
- **Status**: Incident contained; exchange implementing cold-storage segregation and additional key-management controls.

## Affected Systems and Products

- **Marks & Spencer & Co-op Retail Networks**  
  - **Platform**: Azure AD, Okta SSO, internal PoS infrastructure  
- **U.S. Insurance Sector (Aflac, others)**  
  - **Platform**: Cloud identity platforms, call-center VoIP systems  
- **Viasat Enterprise & Satellite Ops**  
  - **Platform**: Hybrid on-prem / cloud management networks  
- **GitHub Open-Source Repositories**  
  - **Platform**: Cross-platform developer environments (Windows, macOS, Linux)  
- **Global HTTP/2-Enabled Web Servers & CDNs**  
  - **Platform**: Nginx, Apache, IIS, Cloudflare edge nodes  
- **Android Devices (Pixel & OEM models running Android 10+)**  
  - **Platform**: Mobile OS with virtualization support & accessibility services  
- **BitoPro Cryptocurrency Exchange**  
  - **Platform**: Web wallets, hot-wallet key management, trading APIs  

## Attack Vectors and Techniques

- **SIM-Swap & Social Engineering**  
  - **Vector**: Phone-based impersonation of IT staff to port numbers and intercept MFA.  
- **OAuth Token Theft**  
  - **Vector**: Phishing links leading to malicious IdP consent screens.  
- **Trojanized Repository Insertion**  
  - **Vector**: Fork/clone of popular GitHub projects containing malicious setup.py or compiled binaries.  
- **HTTP/2 Rapid Reset Flood**  
  - **Vector**: Programmatically opening and immediately resetting streams to amplify request rates.  
- **Virtual Container Abuse on Android**  
  - **Vector**: Malware-instantiated VM keeps malicious app hidden while overlay captures user input.  
- **Hot-Wallet Key Extraction**  
  - **Vector**: Compromised backend server with access to decrypted wallet keys.

## Threat Actor Activities

- **Scattered Spider (a.k.a. Octo Tempest)**  
  - **Campaign**: Combined retail & insurance intrusions since April 2025, leveraging SIM-swap, vishing, and remote-desktop hijacking to stage ransomware.  

- **Salt Typhoon**  
  - **Campaign**: Covert espionage against satellite communications providers; Viasat confirmed victim, other telecoms suspected.  

- **Lazarus Group**  
  - **Campaign**: $11 million crypto theft from BitoPro; ongoing targeting of exchanges across East Asia.  

- **Unknown GitHub Supply-Chain Actor(s)**  
  - **Campaign**: Mass seeding of malicious copycat and “hacking-tool” repos to compromise developers and gamers globally.  

- **DDoS-as-a-Service Operators**  
  - **Campaign**: HTTP/2 rapid-reset botnet leveraged to generate record traffic volumes against hosting providers, indicating commoditization of protocol-level DoS.  

- **Godfather/AntiDot Operators**  
  - **Campaign**: 273 separate Android malware waves focusing on banking, e-wallet, and NFC theft, often delivered via third-party app stores and smishing links.  

**Bold** defensive focus should remain on identity protection, supply-chain code validation, HTTP/2 hardening, and rapid patching of satellite and mobile ecosystems to disrupt these active exploitation chains.