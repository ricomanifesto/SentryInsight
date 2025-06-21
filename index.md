# Exploitation Report  

During the last week, defenders observed a surge in high-impact attacks that mix classic vulnerability exploitation with sophisticated social-engineering and supply-chain abuse. The largest DDoS event ever recorded (7.3 Tbps) relied on the still-exploited HTTP/2 “Rapid Reset” flaw, while threat actors such as Scattered Spider and Salt Typhoon continued cloud-and-identity-centric intrusions that sidestep perimeter controls. Simultaneously, hundreds of trojanized GitHub repositories and new Android malware strains demonstrate that attackers are exploiting trust in developer ecosystems and mobile platforms, expanding the threat surface well beyond traditional CVE-driven issues.  

## Active Exploitation Details  

### HTTP/2 “Rapid Reset” Amplification Attack  
- **Description**: Exploits a weakness in the HTTP/2 protocol that allows an attacker to repeatedly open and immediately cancel streams, overwhelming servers by triggering excessive state changes.  
- **Impact**: Enabled the 7.3 Tbps distributed denial-of-service attack that pushed 37.4 TB of traffic in 45 seconds against a hosting provider, threatening availability of large web infrastructures.  
- **Status**: Actively exploited in the wild; major CDN and web-server vendors have issued patches and mitigations.  
- **CVE ID**: CVE-2023-44487  

### GitHub Copycat / Trojanized Repository Abuse  
- **Description**: Adversaries upload malicious repositories that masquerade as popular open-source projects, embedding credential stealers, backdoors, and cryptocurrency miners. Over 200 rogue repos were identified targeting developers and gamers.  
- **Impact**: Developers who clone or include these projects inherit malicious code, leading to supply-chain compromise, lateral movement, and data exfiltration.  
- **Status**: Campaign is ongoing; GitHub is removing repos and issuing DMCA takedowns, but new copies continue to appear.  

### Scattered Spider Retail & Insurance Intrusions  
- **Description**: The group leverages SIM-swapping, MFA-fatigue, and social-engineering of help desks to seize privileged Okta and Azure AD sessions, then deploys ransomware and data-extortion tools.  
- **Impact**: Attacks on Marks & Spencer, Co-op, and multiple U.S. insurers caused an estimated $592 million in combined damages, including downtime, data theft, and ransom payments.  
- **Status**: Actively conducting campaigns; no specific vendor patch because exploitation relies on identity abuse rather than a software flaw.  

### Salt Typhoon (Chinese APT) Cloud Intrusions  
- **Description**: Targets telecom and satellite providers (most recently Viasat) by harvesting Azure service-principal credentials, abusing OAuth application permissions, and pivoting across multicloud environments.  
- **Impact**: Potential access to sensitive customer traffic and internal tooling; espionage motivation suspected.  
- **Status**: Active; mitigations focus on credential hygiene, conditional access, and continuous token revocation.  

### Godfather & AntiDot Android Virtualization Exploits  
- **Description**: New malware builds hidden virtual containers on Android devices to run overlaid banking apps, intercept NFC payment data, and bypass OS permission prompts.  
- **Impact**: Real-time theft of banking credentials, fraudulent transfers, and contact-less payment abuse.  
- **Status**: Spreading in 273 distinct campaigns; no OS-level patch yet, though Google Play Protect signatures have been updated.  

## Affected Systems and Products  

- **HTTP/2-Enabled Web Servers**: NGINX, Apache, IIS, Envoy, and any custom servers that accept HTTP/2 traffic  
- **Cloudflare, AWS ALB, Google Cloud Load Balancers**: Front-end infrastructure susceptible to HTTP/2 Rapid Reset floods  
- **GitHub Ecosystem**: Developers using Python-based hacking tools, game cheats, and “security-utilities” repos published during May–June 2025  
- **Retail & Insurance Firms**: Okta-integrated SaaS, Microsoft 365, and Azure AD tenants targeted by Scattered Spider  
- **Viasat & Satellite/Telecom Providers**: Azure, GCP, and on-prem hybrid cloud assets leveraged by Salt Typhoon  
- **Android Devices (Android 10+)**: Particularly those that permit side-loading of apps from third-party stores infected with Godfather or AntiDot  

## Attack Vectors and Techniques  

- **HTTP/2 Rapid Reset Flood**  
  - **Vector**: Massive botnets send parallel RST frames to exhaust server resources.  

- **Supply-Chain Repo Poisoning**  
  - **Vector**: Typo-squatted or copy-pasted GitHub repositories distributed via social media and developer forums.  

- **MFA Fatigue & SIM-Swapping**  
  - **Vector**: Continuous push notifications and stolen SMS codes trick employees into approving rogue logins (Scattered Spider).  

- **Cloud Token Hijacking**  
  - **Vector**: Theft of OAuth refresh tokens and abuse of service-principal secrets for persistent Azure access (Salt Typhoon).  

- **Android Virtualization Overlay**  
  - **Vector**: Malware deploys a hidden work profile, runs cloned banking apps inside a virtual space, captures credentials, and tampers with NFC transactions.  

## Threat Actor Activities  

- **Scattered Spider (a.k.a. Octo Tempest)**  
  - **Campaign**: Retail and insurance extortion; combines social-engineering with lateral movement into SaaS platforms; ransom plus data-leak pressure tactics.  

- **Salt Typhoon**  
  - **Campaign**: Espionage-oriented cloud intrusions on telecoms; shares TTPs with previous Storm-0558 style token-forging operations.  

- **Lazarus Group**  
  - **Campaign**: $11 million cryptocurrency theft from BitoPro exchange; leveraged spear-phishing and chain-swapped stolen coins through mixers.  

- **Qilin Ransomware-as-a-Service**  
  - **Campaign**: Added “Call Lawyer” negotiation feature to coerce higher payments; provides affiliates with legal scripts to intimidate victims.  

- **Unknown Developer-Focused Threat Cluster**  
  - **Campaign**: 200+ malicious GitHub repos delivering trojanized hacking tools, credential stealers, and crypto miners; infrastructure overlaps with prior gamer-targeting operations.  

- **Godfather & AntiDot Operators (Financially Motivated)**  
  - **Campaign**: 273 mobile campaigns using virtualization, overlays, and NFC theft aimed at European banking customers.  

Defenders should prioritize HTTP/2 Rapid Reset mitigations, tighten identity and token protections in SaaS clouds, scan developer environments for malicious dependencies, and enforce mobile application control to blunt these active exploitation waves.