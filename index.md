# Exploitation Report

Over the last week, threat actors have intensified supply-chain and platform abuse, coupling novel attack vectors with tried-and-true social-engineering tactics. Malicious GitHub repositories are being weaponized at scale to deliver backdoors to developers, North Korea’s Lazarus Group continues high-value cryptocurrency raids, and a record-breaking 7.3 Tbps HTTP/2 “Rapid Reset” flood highlights the destructive potential of protocol-layer exploits. Concurrently, Android malware families such as Godfather and AntiDot are hijacking mobile banking applications by abusing virtualization and overlay techniques, while the Qilin ransomware-as-a-service (RaaS) outfit expands its legal-pressure extortion model. Telecommunications, cryptocurrency, insurance, and cloud-hosting sectors all saw direct impacts, underscoring the breadth of current exploitation activity.

## Active Exploitation Details

### Malicious Copycat GitHub Repositories
- **Description**: Threat actors cloned popular open-source projects and injected malicious code, then re-published them under look-alike names. Unsuspecting developers who cloned or forked the repos executed embedded installers that fetched remote payloads.  
- **Impact**: Remote code execution (RCE) on developer workstations, credential theft, and potential downstream supply-chain compromise of any software built with the tainted code.  
- **Status**: Actively circulating; dozens of repos reported and removed, but new ones continue to appear. No universal patch—mitigation depends on repository hygiene and sig-based detection.  

### Trojanized GitHub Repositories Campaign Targeting Gamers & Developers
- **Description**: More than 200 repositories advertised “Python hacking tools” that instead delivered multi-stage loaders, Discord token stealers, and cryptocurrency miners.  
- **Impact**: Theft of secrets, unauthorized cryptomining, and lateral movement into corporate environments when victims reused work devices.  
- **Status**: Ongoing; security researchers are coordinating takedowns with GitHub’s trust & safety team.  

### HTTP/2 Rapid Reset Denial-of-Service Exploit
- **Description**: Adversaries abused the HTTP/2 “Rapid Reset” weakness to generate a volumetric flood that peaked at 7.3 Tbps, overwhelming a hosting provider before Cloudflare’s automated mitigation triggered.  
- **Impact**: Complete service disruption with 37.4 TB of traffic in 45 seconds, demonstrating the ease with which modest botnets can weaponize protocol flaws for massive DDoS attacks.  
- **Status**: Continues to be exploited in the wild; most major CDNs have mitigations in place, but origin servers lacking rate-limit controls remain vulnerable.  

### Android Virtualization Abuse (Godfather Malware)
- **Description**: The latest Godfather variant spins up isolated virtual environments on a victim’s device to sideload rogue banking apps, bypass security controls, and exfiltrate credentials.  
- **Impact**: Full account takeover, fraudulent transactions, and interception of MFA tokens.  
- **Status**: Active infections observed across Europe and Latin America; no vendor patch because the malware abuses legitimate Android virtualization APIs.  

### AntiDot Android Overlay & NFC Theft Campaign
- **Description**: AntiDot deploys dynamic overlay windows to mimic legitimate banking app login screens and leverages near-field communication (NFC) to steal contactless payment data.  
- **Impact**: Credential harvesting, unauthorized NFC payments, and account siphoning.  
- **Status**: 3,775 devices confirmed compromised across 273 campaigns; Google Play Protect detections updated, but sideloaded apps remain a risk.  

### Qilin Ransomware RaaS Feature Expansion
- **Description**: Qilin now offers affiliates a “Call Lawyer” extortion toolkit—pre-written legal threat letters and access to legal counsel—to intensify payment pressure on victims post-encryption.  
- **Impact**: Accelerated ransom payments, reputational damage, potential legal fines for victims due to data-privacy exposure.  
- **Status**: Actively deployed in current Qilin intrusions; no single vulnerability—initial access often via phishing and unpatched VPN appliances.  

### Salt Typhoon Intrusions into Viasat
- **Description**: The Chinese-aligned group “Salt Typhoon” compromised Viasat’s corporate network, likely via unpatched edge infrastructure, to conduct reconnaissance against satellite communications assets.  
- **Impact**: Potential espionage, service disruption risk to critical telecom infrastructure.  
- **Status**: Investigation ongoing; Viasat reports no operational impact but hardening and incident response measures are in progress.  

### Lazarus Group BitoPro Crypto-Exchange Heist
- **Description**: Lazarus used spearfishing and backdoored trading tools to infiltrate BitoPro’s hot-wallet infrastructure, stealing $11 million in digital assets.  
- **Impact**: Direct financial loss, market confidence erosion, and possible compliance penalties for the exchange.  
- **Status**: Funds rapidly laundered through mixer services; exchange implementing wallet segregation and threat hunting for residual implants.  

### Scattered Spider Insurance-Sector Breach
- **Description**: Social-engineering group Scattered Spider leveraged SIM swapping and Okta session token theft to penetrate multiple U.S. insurers, including Aflac.  
- **Impact**: Exposure of personal data, policy information, and potential follow-on fraud.  
- **Status**: Active; insurers bolstering identity verification and monitoring for stolen session tokens.  

## Affected Systems and Products

- **GitHub Repositories / Git Clients**  
  - Platform: Cross-platform developer environments (Windows, macOS, Linux)

- **HTTP/2-Enabled Web Servers & Proxies**  
  - Platform: Cloud and on-prem hosting providers, CDNs, reverse proxies

- **Android Banking Applications**  
  - Platform: Android 11–14, especially devices that allow side-loading or developer mode

- **Viasat Corporate & Satellite Networks**  
  - Platform: Hybrid on-prem/cloud infrastructure; satellite control systems

- **BitoPro Cryptocurrency Exchange**  
  - Platform: Hot-wallet Linux servers; trading desk endpoints

- **Insurance Enterprise Identity Platforms (Okta, Azure AD)**  
  - Platform: Windows & cloud-based IAM environments targeted by Scattered Spider

## Attack Vectors and Techniques

- **Supply-Chain Repository Poisoning**  
  - Vector: Clone legitimate open-source projects, inject backdoors, publish under typo-squatted names

- **Protocol Abuse – HTTP/2 Rapid Reset**  
  - Vector: Rapidly send and cancel HTTP/2 streams to amplify traffic volume against targets

- **Virtualization-Based App Hijack (Android)**  
  - Vector: Spawn isolated containers to bypass application sandboxing and inject rogue banking apps

- **Dynamic Overlay Phishing (Android)**  
  - Vector: Real-time overlays that capture credentials from legitimate application windows

- **Spear-Phishing & Backdoored Trading Tools**  
  - Vector: Weaponized documents and trojanized trading software delivered to exchange employees

- **SIM Swapping & Session Token Replay**  
  - Vector: Social-engineering telecom providers to hijack SMS/MFA, followed by token theft via device takeover

- **Ransomware Double-Extortion with Legal Pressure**  
  - Vector: Data exfiltration followed by encryption; legal threats used to coerce payment

## Threat Actor Activities

- **Lazarus Group (North Korea)**  
  - Campaign: BitoPro cryptocurrency theft ($11 M); leveraging backdoored trading applications and rapid laundering tactics.  

- **Salt Typhoon (China-aligned)**  
  - Campaign: Intrusion into Viasat corporate network for satellite comms reconnaissance.  

- **Qilin Ransomware-as-a-Service**  
  - Campaign: Global ransomware operations with new “Call Lawyer” extortion module to maximize ransom yields.  

- **Scattered Spider**  
  - Campaign: U.S. insurance-sector attacks, combining SIM swapping, Okta abuse, and data theft.  

- **Unattributed Actors** – GitHub Supply-Chain Poisoning  
  - Campaign: 200+ malicious repositories targeting developers and gamers with stealer malware and cryptominers.  

- **DDoS Botnet Operators**  
  - Campaign: Record 7.3 Tbps HTTP/2 “Rapid Reset” attack against hosting provider, showing continued growth in botnet capacity and protocol weaponization.  

