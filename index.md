# Exploitation Report

During the last week, security researchers and vendors reported a surge in real-world exploitation activity ranging from large-scale supply-chain abuse on GitHub and Android virtualization attacks to protocol-level DDoS events and state-sponsored network intrusions. Threat actors such as **Lazarus**, **Salt Typhoon**, **Scattered Spider**, and the **Qilin** ransomware group are actively abusing these weaknesses to steal millions in cryptocurrency, exfiltrate corporate data, and disrupt critical services. Development environments, telecom infrastructure, cloud hosting providers, and mobile users are all being targeted simultaneously, underscoring the breadth of today’s exploitation landscape.

## Active Exploitation Details

### Malicious Copycat Repositories on GitHub  
- **Description**: Attackers create counterfeit repositories that mimic popular open-source projects, embedding backdoors or infostealers inside seemingly legitimate code.  
- **Impact**: Developers who clone or `pip/npm install` these projects silently execute malware, enabling credential theft, remote access, and subsequent supply-chain poisoning of downstream applications.  
- **Status**: Ongoing campaign with dozens (200+ observed) of repos still appearing; GitHub’s security team is removing them as they surface. No traditional vendor patch—defense relies on repository takedown and developer vigilance.  

### HTTP/2 “Rapid Reset” Amplification (7.3 Tbps DDoS)  
- **Description**: Adversaries abuse the HTTP/2 protocol feature that allows streams to be rapidly reset, overwhelming edge servers with a flood of low-cost requests that consume disproportionate resources.  
- **Impact**: Record-breaking volumetric DDoS (7.3 Tbps, 37.4 TB in 45 seconds) caused severe service degradation at a hosting provider before Cloudflare mitigation kicked in.  
- **Status**: Actively exploited in the wild; leading CDN and web-server vendors have issued mitigation guidance and updated rate-limiting rules.  

### Android Virtualization Abuse by “Godfather” Malware  
- **Description**: The latest Godfather variant spins up isolated virtual environments on compromised phones, sideloads banking apps, then hijacks sessions and intercepts MFA tokens without rooting the device.  
- **Impact**: Complete account takeover of mobile banking, e-wallets, and cryptocurrency applications; enables fraudulent transactions and credential exfiltration.  
- **Status**: Active infections across Europe and North America. Google Play Protect updates are rolling out; no OS patch required, but app updates and EDR rules are advised.  

### Overlay, Virtualization, and NFC Theft in “AntiDot” Android Malware  
- **Description**: AntiDot leverages Android overlay permissions and creates fake login screens, while also abusing NFC APIs to skim contactless payment card data.  
- **Impact**: Theft of banking credentials, payment card information, and direct unauthorized NFC transactions.  
- **Status**: 3,775 confirmed device compromises across 273 campaigns; mitigation via Google Play Protect updates and revocation of malicious developer certificates.  

### Network Edge Device Exploit by Salt Typhoon  
- **Description**: The China-nexus group compromises internet-facing edge appliances at global telecoms—Viasat being the latest victim—using a still-undisclosed zero-day in networking gear to gain persistent access.  
- **Impact**: Initial access for espionage, lateral movement into satellite ground-station networks, and potential disruption of customer connectivity.  
- **Status**: Active exploitation; vendor patches or IOC details have not yet been publicly released. Organizations are urged to increase monitoring of edge devices and apply firmware updates as they become available.  

## Affected Systems and Products

- **GitHub-hosted Open-Source Repositories**  
  - **Platform**: Any OS / DevOps pipeline that pulls code via GitHub, Python `pip`, Node `npm`, or similar package managers  

- **HTTP/2-capable Web & API Servers (NGINX, Apache, Envoy, Cloudflare edge)**  
  - **Platform**: Linux-based web infrastructure, cloud load balancers, and CDNs  

- **Android Banking, Crypto-Wallet, and FinTech Apps**  
  - **Platform**: Android 11–14, especially devices allowing virtualization or Accessibility overlays  

- **Telecom Edge Appliances (undisclosed vendor, satellite ground infrastructure)**  
  - **Platform**: Proprietary network OS running on ISP / satellite gateways  

## Attack Vectors and Techniques

- **Typosquatting / Repojacking**  
  - **Vector**: Adversaries register repository names similar to legitimate projects; developers unknowingly pull malicious code.  

- **HTTP/2 Rapid Reset Flood**  
  - **Vector**: Massive parallel HTTP/2 stream creations followed by immediate resets cause amplification and resource exhaustion.  

- **Android Accessibility & Virtualization Abuse**  
  - **Vector**: Malware requests accessibility privileges, deploys virtual containers, and invisibly proxies legitimate app traffic.  

- **Overlay Phishing & NFC Skimming**  
  - **Vector**: Fake UI overlays capture credentials; NFC interfaces are accessed via malicious apps to read contactless card data.  

- **Zero-Day Edge Device Compromise**  
  - **Vector**: Remote code execution via undisclosed flaw in network appliance firmware, enabling credential harvesting and persistent backdoors.  

## Threat Actor Activities

- **Lazarus Group**  
  - **Campaign**: $11 million cryptocurrency theft from BitoPro exchange on May 8 2025 using spear-phishing and post-exploitation tunneling.  

- **Salt Typhoon**  
  - **Campaign**: Ongoing intrusions into telecoms (Viasat latest) leveraging a zero-day in network edge devices for intelligence gathering.  

- **Scattered Spider (aka UNC3944/0ktapus)**  
  - **Campaign**: Coordinated attacks on U.S. insurance companies—including Aflac—leveraging social-engineering and SIM-swap tactics to infiltrate Okta and cloud environments.  

- **Qilin Ransomware-as-a-Service**  
  - **Campaign**: Introduced a “Call Lawyer” negotiation feature, providing legal scripts to affiliates to intensify ransom pressure on victims.  

- **GitHub Supply-Chain Actors (unattributed)**  
  - **Campaign**: 200+ trojanized repositories pushing infostealers and RATs to developers and gamers worldwide.  

- **Botnet Operators (HTTP/2 DDoS)**  
  - **Campaign**: Coordinated botnet leveraging Rapid Reset technique to launch record-setting 7.3 Tbps attack against a hosting provider.  

Stay vigilant for patch releases on network edge devices, enforce strict code-import policies, and deploy updated DDoS mitigation rules to counter these evolving threats.