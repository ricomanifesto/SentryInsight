# Exploitation Report

Over the last week, defenders have observed a surge in real-world exploitation that spans cloud infrastructure, open-source supply chains, mobile platforms, and large-scale denial-of-service activity. The most critical events include record-breaking HTTP/2 “Rapid Reset” attacks used to generate a 7.3 Tbps DDoS flood against a hosting provider, widespread seeding of malicious GitHub repositories to compromise developers, and active mobile banking fraud campaigns abusing virtualization and overlay techniques on Android devices. Nation-state and financially motivated groups—including Lazarus, Salt Typhoon, Qilin ransomware affiliates, and Scattered Spider—are leveraging these vectors to steal cryptocurrency, exfiltrate sensitive data, and extort victims.

## Active Exploitation Details

### HTTP/2 “Rapid Reset” Abuse
- **Description**: Attackers abuse a design weakness in the HTTP/2 protocol that allows them to send a rapid sequence of stream reset frames, forcing servers to allocate disproportionate resources and amplifying traffic volume.  
- **Impact**: Enables terabit-scale Layer 7 DDoS attacks capable of knocking large hosting providers offline; observed peak at 7.3 Tbps delivering 37.4 TB in 45 seconds.  
- **Status**: Actively exploited in the wild; mitigations are available from major CDN and web-server vendors, but many self-hosted deployments remain vulnerable.

### Malicious Copycat Repositories on GitHub
- **Description**: Threat actors clone popular open-source projects or publish look-alike repos laced with malware, often masquerading as developer utilities or Python hacking tools.  
- **Impact**: Developers who pull the code trigger remote access Trojans that steal credentials, implant backdoors, or exfiltrate crypto-wallet data.  
- **Status**: Ongoing campaign with dozens of repos discovered and removed; no upstream patch—developers must validate repo authenticity.

### Trojanized GitHub Repositories Targeting Gamers and Developers
- **Description**: Separate but related campaign seeding more than 200 repositories delivering weaponized binaries under the guise of gaming mods or cheat utilities.  
- **Impact**: Installation grants attackers full system control, credential theft, and potential lateral movement inside corporate networks where the infected workstation resides.  
- **Status**: Still active; GitHub security teams are taking takedown actions while indicators of compromise (IoCs) circulate among defenders.

### Godfather Android Malware Virtualization Hijack
- **Description**: New Godfather variant spins up isolated virtual environments on Android phones, injects legitimate banking apps, and intercepts user input to hijack accounts.  
- **Impact**: Allows unauthorized fund transfers, credential theft, and full session hijacking without rooting the device.  
- **Status**: In-the-wild infections rising; Google Play Protect updates released, but sideloaded apps remain a threat.

### AntiDot Android Malware (Overlays, Virtualization Fraud, NFC Theft)
- **Description**: AntiDot leverages Accessibility Service overlays and virtualization to spoof legitimate app interfaces, steal NFC-based payment data, and execute unauthorized transactions.  
- **Impact**: Direct financial loss, credential compromise, and potential device takeover.  
- **Status**: Active across 3,775 confirmed devices; no single patch—requires user removal and MDM enforcement.

### Salt Typhoon Cloud Intrusions
- **Description**: Chinese state-aligned actor “Salt Typhoon” breached Viasat by exploiting undisclosed cloud service weaknesses and misconfigurations to obtain privileged access.  
- **Impact**: Potential espionage, disruption of satellite communications, and intelligence gathering.  
- **Status**: Investigation ongoing; hardening guidance shared with government partners.

### Qilin Ransomware Initial-Access Exploits
- **Description**: Qilin RaaS affiliates employ recently patched remote-code-execution flaws in Internet-facing software to drop double-extortion payloads, then escalate pressure with an in-portal “Call Lawyer” feature.  
- **Impact**: Complete encryption of corporate data, public leak threats, and increased ransom demands.  
- **Status**: Actively exploiting unpatched systems; vendors have released fixes for the underlying RCE flaws.

### Scattered Spider Insurance-Sector Breaches
- **Description**: Social-engineering-driven intrusion set uses SIM-swapping and legacy VPN weaknesses to compromise insurance firms, including Aflac, and extract personal data.  
- **Impact**: Large-scale PII theft, regulatory exposure, and financial losses.  
- **Status**: Campaign ongoing; MFA hardening and VPN upgrades recommended.

### Lazarus Group Exchange Heist
- **Description**: North Korean Lazarus operators penetrated BitoPro exchange through spear-phishing and exploited weak internal controls to siphon $11 million in crypto.  
- **Impact**: Direct financial loss and reputational damage; funds funneled into DPRK programs.  
- **Status**: Funds traced on-chain; no software patch applicable—focus on operational security controls.

## Affected Systems and Products

- **HTTP/2-Enabled Web Servers**: NGINX, Apache, Cloud-hosted reverse proxies supporting HTTP/2  
  - **Platform**: Linux, Windows, containerized microservices, CDN edge nodes

- **GitHub Repository Consumers**: Developers using Git, CI/CD pipelines, package managers (pip, npm)  
  - **Platform**: Windows, macOS, Linux development environments

- **Android Banking Users**: Devices running Android 8–14 with side-loaded apps or accessibility permissions granted  
  - **Platform**: Mobile phones and tablets, especially in EMEA & LATAM regions

- **Viasat Cloud & Satellite Infrastructure**: Proprietary network management portals and cloud workloads  
  - **Platform**: Hybrid cloud (Azure/AWS) and on-prem orchestration systems

- **Enterprise VPN & RDP Exposures**: Organizations running outdated remote-access gateways exploited by Qilin and Scattered Spider  
  - **Platform**: Windows Server, legacy SSL-VPN appliances

- **Cryptocurrency Exchanges**: Centralized exchanges with internet-facing admin panels and hot-wallet servers  
  - **Platform**: Linux backend servers, Kubernetes clusters

## Attack Vectors and Techniques

- **HTTP/2 Rapid Reset Flood**  
  - **Vector**: Layer 7 DDoS leveraging unlimited RST_STREAM frames to exhaust server resources

- **Supply-Chain Repo Poisoning**  
  - **Vector**: Deceptive GitHub projects cloned or typo-squatted to trick developers into executing malicious code

- **Accessibility Overlay Abuse**  
  - **Vector**: Android malware displays fake login screens over real apps, capturing credentials and MFA codes

- **Virtualization-Based App Cloning**  
  - **Vector**: Godfather creates sandboxed instances of real banking apps inside a controlled VM, intercepting traffic

- **NFC Data Skimming**  
  - **Vector**: AntiDot intercepts Near-Field Communication transactions to steal payment card data

- **Spear Phishing & Credential Theft**  
  - **Vector**: Email or social-media lures delivering malware loaders or harvesting login data (Lazarus, Scattered Spider)

- **Legacy VPN/Driver Exploits**  
  - **Vector**: Use of outdated VPN appliances or Windows drivers without recent patches to gain privileged access

## Threat Actor Activities

- **Lazarus Group**  
  - **Campaign**: $11 million BitoPro cryptocurrency theft leveraging spear phishing and exchange-side weaknesses

- **Salt Typhoon (UNC5221 / Storm-0588)**  
  - **Campaign**: Intrusions into Viasat’s satellite network for espionage; methodology includes cloud credential abuse

- **Qilin Ransomware-as-a-Service**  
  - **Campaign**: Double-extortion operations augmented with “Call Lawyer” bargaining feature; targets midsize enterprises

- **Scattered Spider (OctoTempest)**  
  - **Campaign**: Insurance-sector breaches via SIM-swapping, social engineering, and VPN compromise; Aflac confirmed victim

- **Anonymous GitHub Threat Actors**  
  - **Campaign**: Copycat repo poisoning (dozens of malicious projects) and 200+ trojanized repositories aimed at gamers and developers

- **Unknown Botnet Operators**  
  - **Campaign**: Record 7.3 Tbps HTTP/2 Rapid Reset DDoS attack against hosting provider; infrastructure likely rented botnets

**End of Report**