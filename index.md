# Exploitation Report

During the last week, defenders observed a diverse set of active exploitation campaigns ranging from protocol-level denial-of-service attacks to highly targeted intrusions against retail, telecom, and cryptocurrency organizations. The most damaging activity centred on the 7.3 Tbps HTTP/2 “Rapid Reset” denial-of-service event, large-scale supply-chain poisoning on GitHub, aggressive social-engineering intrusions by Scattered Spider, and the continued abuse of Android virtualization and overlay mechanisms by mobile-banking trojans. Multiple nation-state and financially motivated actors—including Lazarus, Salt Typhoon, Qilin, and Scattered Spider—were linked to these operations.

## Active Exploitation Details

### HTTP/2 Rapid Reset Protocol Abuse
- **Description**: Attackers exploit a weakness in the HTTP/2 protocol that allows them to flood servers with a high rate of stream-reset frames (“Rapid Reset”). The stateless nature of the resets forces back-end infrastructure to allocate resources repeatedly, leading to amplification.  
- **Impact**: Enabled the largest recorded DDoS attack (7.3 Tbps, 37.4 TB in 45 seconds) against a hosting provider; could knock large Internet properties offline.  
- **Status**: Actively exploited in the wild. Mitigations and rate-limiting rules have been deployed by Cloudflare and other CDN/WAF vendors; no protocol-level patch is yet standardized.  

### GitHub Repository Impersonation & Trojanization
- **Description**: Threat actors uploaded more than 200 malicious copy-cat repositories posing as popular hacking tools or game mods. The projects contained obfuscated malware loaders that execute on developer workstations.  
- **Impact**: Developer workstations become initial footholds for wider supply-chain compromise, credential theft, and token exfiltration.  
- **Status**: Repositories are being discovered and removed, but new ones continue to appear. GitHub users must manually validate repository provenance.  

### Android Virtualization & Overlay Abuse
- **Description**: Mobile malware families “Godfather” and “AntiDot” create isolated virtual environments and deceptive overlays on Android devices. This bypasses traditional sandboxing and grants malware full accessibility service privileges.  
- **Impact**: Theft of authentication codes, NFC-based transaction hijacking, and fraudulent wire transfers directly from infected devices.  
- **Status**: Active campaigns observed across 3,775 devices in 273 separate waves. Google Play Protect updates are rolling out, but sideloading channels remain at risk.  

### MFA Fatigue & Help-Desk Social Engineering (Scattered Spider)
- **Description**: The crew leverages repeated MFA push requests, convincing employees to approve logins, or calls help-desks impersonating staff to reset credentials. Once inside, they enumerate cloud privileges and deploy ransomware or exfiltrate data.  
- **Impact**: Combined attack on Marks & Spencer and Co-op caused up to $592 million in damages; insurance sector (Aflac) also breached, exposing personal data.  
- **Status**: Ongoing. Victims are tightening identity governance and adding phishing-resistant MFA—but the actor remains highly active.  

## Affected Systems and Products

- **Global Hosting Provider (undisclosed)**  
  - **Platform**: Public-facing HTTP/2 web services protected by Cloudflare  

- **GitHub**  
  - **Platform**: Open-source repositories; developers using Git, npm, pip, and direct `git clone` workflows  

- **Android Smartphones (Godfather & AntiDot campaigns)**  
  - **Platform**: Android 9–14; devices permitting sideloading or third-party app stores  

- **Marks & Spencer & Co-op Retail Networks**  
  - **Platform**: Azure AD, Okta, VPN gateways, and on-prem Windows/VMware infrastructure  

- **Aflac Insurance Environment**  
  - **Platform**: Cloud SaaS (email, identity providers) and internal claims systems  

- **Viasat Satellite & Telecom Infrastructure**  
  - **Platform**: Hybrid on-prem / cloud environment targeted by Salt Typhoon  

- **BitoPro Cryptocurrency Exchange**  
  - **Platform**: Web, mobile trading APIs, and backend wallets targeted by Lazarus  

## Attack Vectors and Techniques

- **HTTP/2 Stream Reset Flooding**  
  - **Vector**: Large botnets send crafted RST_STREAM frames at scale, over-consuming server resources.  

- **Supply-Chain Poisoning via GitHub**  
  - **Vector**: Malicious forks masquerade as legitimate repos; `setup.py` or `package.json` executes malware during build/install.  

- **Android Virtualization Hijack**  
  - **Vector**: Malware initiates a hidden virtual device instance, injects overlays that mimic banking apps, then intercepts credentials and NFC payments.  

- **MFA Push Bombing / Help-Desk Impersonation**  
  - **Vector**: Attackers repeatedly trigger MFA requests, or call IT support to reset accounts after harvesting employee PII.  

- **Hot-Wallet Credential Theft**  
  - **Vector**: Lazarus compromises exchange backend servers to drain wallets within minutes.  

## Threat Actor Activities

- **Scattered Spider**  
  - **Campaign**: Coordinated retail and insurance breaches using MFA fatigue, SIM-swapping, and cloud privilege escalation.  

- **Salt Typhoon**  
  - **Campaign**: Espionage operation against Viasat; living-off-the-land techniques and covert data collection with minimal disruption.  

- **Lazarus Group**  
  - **Campaign**: $11 million theft from BitoPro; rapid transfer to mixing services to launder funds.  

- **Qilin RaaS**  
  - **Campaign**: Introduced “Call Lawyer” extortion feature, offering legal coaching to pressure victims, observed in recent ransomware notes.  

- **Unknown Actors behind GitHub Trojanization**  
  - **Campaign**: At least 200 fake repos targeting gamers, security researchers, and Python developers to build a foothold in CI/CD pipelines.  

- **Botnet Operators (HTTP/2 Rapid Reset)**  
  - **Campaign**: Short-burst, high-bandwidth DDoS attacks testing provider thresholds; likely for-hire service.  

**Bold** vigilance and rapid patching or mitigation remain essential as these exploited weaknesses continue to evolve.