# Exploitation Report

The past week’s security coverage highlights a renewed surge in real-world exploitation of previously disclosed vulnerabilities, aggressive zero-day weaponization, and creative abuse of supply-chain trust relationships. Chinese state-sponsored operators (Salt Typhoon) continue to reuse the Barracuda ESG command-injection flaw against fresh targets such as Viasat, while large-scale DDoS crews are reviving the HTTP/2 Rapid-Reset weakness to deliver record-shattering 7.3 Tbps floods. At the same time, financially motivated gangs—including Scattered Spider, Lazarus, and the Qilin ransomware program—pivot to identity compromise, SIM-swapping, and legal coercion to maximize extortion. Developers and gamers are being lured into more than 200 trojanized GitHub repositories, underlining persistent supply-chain exposure. Mobile users are also in the crosshairs, with new Godfather and AntiDot variants abusing virtualization and overlay techniques to hijack banking sessions and NFC payments.

## Active Exploitation Details

### Barracuda Email Security Gateway Remote Command Injection
- **Description**: A command-injection flaw in Barracuda ESG appliances that allows unauthenticated remote execution of arbitrary code via crafted TAR file headers used during email attachment scanning.  
- **Impact**: Full device compromise, lateral movement into internal networks, exfiltration of email data, and installation of persistent backdoors.  
- **Status**: Actively exploited by Salt Typhoon against Viasat and other service providers. Barracuda has released fixes, but appliances compromised before patching remain at risk.  
- **CVE ID**: CVE-2023-2868  

### HTTP/2 Rapid-Reset Denial-of-Service Weakness
- **Description**: Abuse of the HTTP/2 RFC mechanism that allows an attacker to open a large number of streams and immediately cancel them, forcing servers and CDNs to allocate disproportionate resources.  
- **Impact**: Massive volumetric DDoS attacks; the latest peaked at 7.3 Tbps and 37.4 TB in 45 seconds against a hosting provider.  
- **Status**: Under active exploitation in the wild. Mitigations implemented by major CDNs; protocol-level hardening is still in progress.  

### GitHub Trojanized Repository Supply-Chain Abuse
- **Description**: Threat actors publish repositories mimicking popular hacking tools or gaming mods that conceal obfuscated Python, Go, and Bash droppers.  
- **Impact**: Developer workstation compromise, credential theft, and downstream propagation when malicious code is reused in production pipelines.  
- **Status**: Ongoing campaign; more than 200 malicious repos identified and taken down, but new ones continue to appear.  

### Scattered Spider SIM-Swap & Identity Federation Abuse
- **Description**: Adversaries perform SIM-swapping and social-engineering calls to service desks to hijack MFA tokens, then pivot through Okta and Microsoft Entra ID to obtain session cookies and cloud workloads.  
- **Impact**: Enterprise-wide account takeover, data theft, and retail service disruption costing up to $592 million at Marks & Spencer and Co-op.  
- **Status**: Live campaign; no software patch—requires hardened identity workflows and phishing-resistant MFA.  

### Android Virtualization & Overlay Exploits (Godfather / AntiDot)
- **Description**: Malware loads banking apps in isolated virtual containers or overlays fake login pages, intercepting credentials and manipulating transactions; AntiDot additionally abuses NFC interfaces for contactless theft.  
- **Impact**: Account takeover across hundreds of banking, crypto, and payment apps on more than 3,700 devices.  
- **Status**: Active; Google Play Protect updates deployed, but sideloaded apps remain vulnerable.  

### Qilin Ransomware “Call Lawyer” Extortion Enhancement
- **Description**: While not a software flaw, Qilin leverages double-extortion tactics by embedding in-portal access to legal advisors for affiliates, intensifying pressure on breached victims.  
- **Impact**: Increased ransom payments, legal intimidation, and accelerated decision-making by victim organizations.  
- **Status**: Feature live within the Qilin RaaS portals; ongoing use in active ransomware events.  

## Affected Systems and Products

- **Barracuda Email Security Gateway**: Hardware and virtual appliances running unpatched firmware prior to May 2023  
- **HTTP/2-enabled Web Servers/CDNs**: Cloudflare, AWS ALB, Nginx, Apache, and proprietary stacks that support multiplexed streams  
- **GitHub Users & CI/CD Pipelines**: Developers cloning falsely branded “hacking tools,” gaming mods, or Python packages  
- **Retail & Insurance Cloud Tenants**: Okta, Microsoft Entra ID, Azure AD, Snowflake, and Salesforce tenants targeted by Scattered Spider  
- **Android Banking & Crypto Apps**: Devices running Android 8–14, particularly those sideloading APKs outside Google Play  
- **Organizations Behind DDoS Mitigation Appliances**: Hosting providers and SaaS platforms reliant on HTTP/2 are primary DoS targets  

## Attack Vectors and Techniques

- **Remote Command Injection**: Malformed TAR headers delivered via email attachments to Barracuda ESG appliances  
- **Protocol Abuse (HTTP/2 Rapid-Reset)**: Flood of create-then-cancel stream frames to exhaust server resources  
- **Repository Typosquatting & Dependency Confusion**: Look-alike GitHub projects lure developers into executing trojanized scripts  
- **SIM-Swapping & Voice-Phishing (Vishing)**: Social engineering to transfer phone numbers and bypass MFA, then leveraging session token theft  
- **Virtual Container Hijacking**: Godfather malware spins up isolated work profiles to invisibly automate fraudulent banking sessions  
- **Overlay & NFC Abuse**: AntiDot places UI overlays on genuine apps and steals contactless payment tokens  
- **Double-Extortion with Legal Coercion**: Qilin’s built-in legal counsel messages threaten lawsuits and regulatory fines to amplify ransom pressure  

## Threat Actor Activities

- **Salt Typhoon (PRC-linked)**  
  - **Campaign**: Ongoing exploitation of Barracuda ESG CVE-2023-2868 across telecoms (Viasat) and critical infrastructure; deployment of custom backdoors and credential harvesting.  

- **Scattered Spider (UNC3944/Starfraud)**  
  - **Campaign**: Combined attacks against Marks & Spencer, Co-op, and U.S. insurers such as Aflac; relies on SIM-swapping, service-desk social engineering, and cloud identity abuse to exfiltrate data and extort victims.  

- **Lazarus Group (North Korea)**  
  - **Campaign**: $11 million cryptocurrency theft from BitoPro exchange on May 8 2025; leveraged spear-phishing and on-chain laundering techniques.  

- **Qilin RaaS**  
  - **Campaign**: Broad double-extortion ransomware operations; new “Call Lawyer” feature used to increase psychological pressure on breached organizations.  

- **Unattributed DDoS Threat Actor(s)**  
  - **Campaign**: Record 7.3 Tbps HTTP/2 Rapid-Reset flood against a hosting provider; infrastructure-agnostic botnet with short-burst, high-volume tactics.  

- **GitHub Supply-Chain Actor (Unnamed)**  
  - **Campaign**: Publication of 200+ malicious repositories targeting gamers and developers; distribution of info-stealers and RATs through cloned project names.  

- **Financially Motivated Android Operators (“Coper” lineage)**  
  - **Campaign**: AntiDot and Godfather malware waves across 273 campaigns, primarily in Europe and Latin America, aiming at bank credential theft and NFC-based fraud.  

Stay vigilant for continued exploitation, prioritize patching of edge email appliances, enforce phishing-resistant MFA, audit developer toolchains, and harden HTTP/2 deployments to mitigate the active threats outlined above.