# Exploitation Report

During the past week, threat activity largely centered on supply-chain manipulation, large-scale credential exposure, and the weaponization of network and application-layer weaknesses. Chinese state-aligned actors (Salt Typhoon) continued leveraging zero-day flaws in edge devices to infiltrate telecom providers, while financially motivated groups (e.g., Lazarus, Scattered Spider, Qilin) pursued ransomware, credential theft, and cryptocurrency raids. Simultaneously, a record 7.3 Tbps DDoS assault exploited the HTTP/2 Rapid Reset weakness, and multiple Android banking Trojans abused virtualization and overlay techniques to bypass mobile defenses. Developers were also targeted through dozens of malicious copy-cat GitHub repositories, underscoring the growing risk to the software supply chain.

## Active Exploitation Details

### Salt Typhoon Zero-Day on Remote Management Appliances
- **Description**: A still-undisclosed zero-day flaw in remote edge appliances that allows unauthenticated access and persistent foothold inside telecom and satellite networks.  
- **Impact**: Full network compromise, credential theft, and long-term espionage against satellite communications infrastructure.  
- **Status**: Actively exploited; no public patch details released. Viasat confirmed compromise, investigations ongoing.

### HTTP/2 Rapid Reset Amplification
- **Description**: Abuse of the HTTP/2 protocol’s stream-cancellation feature (“Rapid Reset”) to trigger massive amplification in volumetric DDoS attacks.  
- **Impact**: Generated the largest recorded DDoS event (7.3 Tbps, 37.4 TB in 45 seconds), capable of knocking high-bandwidth hosting providers offline.  
- **Status**: Exploitation in the wild; Cloudflare deployed protocol-level mitigations, other vendors urged to adopt similar filters.

### GitHub Supply-Chain Poisoning via Malicious Copycat Repositories
- **Description**: Threat actors cloned popular open-source projects, injected malware, and reposted them under look-alike names to compromise unsuspecting developers. Over 200 weaponized repos were discovered.  
- **Impact**: Remote code execution on developer systems, credential theft, and potential downstream contamination of enterprise software.  
- **Status**: Ongoing takedowns by GitHub; attackers continue re-uploading variants.

### Android Virtualization Hijack (Godfather Trojan)
- **Description**: The latest Godfather variant spins up isolated virtual environments on Android devices, sideloads victim banking apps, and intercepts traffic and credentials within the sandbox.  
- **Impact**: Real-time hijacking of banking sessions, unauthorized money transfers, and MFA bypass.  
- **Status**: Active infections observed across multiple regions; no OS-level patch (mitigation relies on mobile AV and Google Play Protect).

### AntiDot Android Overlay & NFC Exploit
- **Description**: “AntiDot” malware pushes dynamic overlays to steal credentials, abuses virtualization fraud similar to Godfather, and skims contactless payments through NFC emulation.  
- **Impact**: Credential harvesting, unauthorized NFC transactions, and full device surveillance.  
- **Status**: 3,775 confirmed infections across 273 campaigns; threat intelligence feeds now blacklisting C2 nodes.

### Scattered Spider Social-Engineering Intrusions
- **Description**: Extensive MFA-bypass and SIM-swap social-engineering playbook used to gain access to retailer and insurance networks (M&S, Co-op, Aflac).  
- **Impact**: Up to $592 M in damages, data exfiltration, and extortion.  
- **Status**: Campaign still active; victims urged to harden identity platforms and enforce phishing-resistant MFA.

### Qilin Ransomware “Call Lawyer” Pressureware
- **Description**: Ransomware-as-a-Service group now offers built-in legal counsel to affiliates and victims, escalating psychological pressure to pay.  
- **Impact**: Double-extortion, operational disruption, and reputational damage.  
- **Status**: Active; no decryptor publicly available.

### Lazarus Exchange Breach
- **Description**: Compromise of Taiwanese exchange BitoPro, attributed to the North-Korean Lazarus group, leveraging unknown network intrusion vector to siphon crypto assets.  
- **Impact**: $11 M in cryptocurrency theft, potential follow-on laundering.  
- **Status**: Incident contained, law-enforcement investigation in progress.

## Affected Systems and Products

- **Viasat Satellite & Telecom Infrastructure**  
  - **Platform**: Remote management/VPN appliances, Windows & Linux internal servers.

- **Global HTTP/2-Enabled Web Services**  
  - **Platform**: Any cloud provider or on-prem load balancer supporting HTTP/2.

- **GitHub Open-Source Ecosystem**  
  - **Platform**: Developers on Windows, macOS, and Linux pulling trojanized repos.

- **Android Banking Applications (Godfather / AntiDot Victims)**  
  - **Platform**: Android 8–14 smartphones; apps from official and third-party stores.

- **Retail & Insurance Enterprises (Scattered Spider victims)**  
  - **Platform**: Identity providers (Okta/Azure AD), internal Windows AD domains.

- **Enterprise Environments Targeted by Qilin RaaS**  
  - **Platform**: Windows Server & Desktop, VMware vSphere, Hyper-V infrastructures.

- **BitoPro Cryptocurrency Exchange**  
  - **Platform**: Hybrid cloud servers running exchange hot-wallet infrastructure.

## Attack Vectors and Techniques

- **Zero-Day Appliance Exploitation**  
  - **Vector**: Unauthenticated network access to edge device management interfaces.  

- **HTTP/2 Rapid Reset**  
  - **Vector**: Flood of RST_STREAM frames to amplify traffic toward targets.  

- **Malicious Repository Cloning**  
  - **Vector**: Typosquatting popular GitHub projects; developers `git clone` malicious forks.  

- **Android Virtualization Fraud**  
  - **Vector**: Malware creates an isolated VM, installs victim’s banking app inside, intercepts UI and network calls.  

- **Dynamic Overlay Phishing (Mobile)**  
  - **Vector**: Real-time overlay of legitimate app screens to capture credentials and OTPs.  

- **SIM-Swap & MFA Fatigue**  
  - **Vector**: Social-engineered carrier interactions and repeated push-notification prompts.  

- **Double-Extortion Ransomware**  
  - **Vector**: Initial foothold via RDP or phishing, data exfiltration, then encryption.  

- **Hot-Wallet Compromise**  
  - **Vector**: Lateral movement to crypto wallet servers, private-key theft, on-chain laundering.

## Threat Actor Activities

- **Salt Typhoon (China-nexus)**  
  - **Campaign**: Multi-year telecom espionage; latest victim Viasat. Focus on zero-days in edge appliances and living-off-the-land post-exploitation.

- **Scattered Spider (UNC3944/Muddled Libra)**  
  - **Campaign**: Coordinated April-May 2025 attacks on UK retailers & US insurers using social engineering and SIM swapping for MFA bypass.

- **Lazarus Group (North Korea)**  
  - **Campaign**: May 2025 BitoPro heist, $11 M stolen; part of broader crypto-funding operations.

- **Qilin RaaS**  
  - **Campaign**: Offering “Call Lawyer” feature to affiliates, increasing ransom leverage and professionalization of negotiations.

- **Unknown DDoS Botnet Operator**  
  - **Campaign**: 7.3 Tbps HTTP/2 attack; infrastructure suggests automated botnet with global IoT and cloud nodes.

- **Supply-Chain Malware Actors (GitHub Copycat Ops)**  
  - **Campaign**: Over 200 malicious repos targeting developers and gamers to implant info-stealers and RATs.

**Bold emphasis** and markdown hierarchy have been applied per instructions.