# Exploitation Report

During the past week threat actors focused on opportunistic, high-impact attacks rather than sophisticated zero-day exploitation.  The most critical activity included a nation-state–sized DDoS event that abused weaknesses in the HTTP/2 protocol to generate a record-breaking 7.3 Tbps flood, large-scale supply-chain poisoning on GitHub via trojanized repositories, continued retailer and insurance intrusions by the Scattered Spider social-engineering crew, and financially motivated breaches by Lazarus Group against cryptocurrency infrastructure.  Parallel campaigns on Android are leveraging virtualization and overlay techniques to hijack banking applications, while new credential compilations are fueling wide-scale account-takeover attempts.  Collectively, the activity underscores growing attacker emphasis on abusing misconfigurations, protocol flaws, and social-engineering gaps that sit outside traditional patch cycles.

## Active Exploitation Details

### HTTP/2 Rapid Reset Denial-of-Service Weakness
- **Description**: Abuse of the HTTP/2 “stream cancel” feature (RST_STREAM) to bombard servers with rapid, concurrent resets, forcing them to allocate resources far beyond normal limits.
- **Impact**: Enables terabit-scale DDoS that can overwhelm backbone links; recent peak measured at 7.3 Tbps delivering 37.4 TB in 45 seconds.
- **Status**: Exploitation is ongoing in the wild; mitigation guidance issued by major CDN and cloud vendors.  No traditional patch—requires rate-limiting and protocol hardening.

### Malicious Copycat & Trojanized GitHub Repositories
- **Description**: Adversaries clone popular open-source projects, inject malicious code or payload downloaders, and repost them to GitHub under look-alike names.
- **Impact**: Developers who install the tainted packages inherit backdoors that can steal credentials, open reverse shells, or exfiltrate cloud secrets, propagating further through CI/CD pipelines.
- **Status**: Dozens of live repos observed; GitHub is removing offenders but new copies appear daily.  No vendor patch—requires supply-chain controls by users.

### Android “Godfather” Virtualization Abuse
- **Description**: Latest Godfather banking Trojan spins up isolated virtual containers on the device, running cloned versions of legitimate banking apps under attacker control to intercept credentials and two-factor codes.
- **Impact**: Full account hijack, fraudulent transfers, and potential NFC-based contactless payment theft.
- **Status**: Active distribution through sideloaded APKs and malicious ads; Google Play Protect updates available but device patching is user-driven.

### Android “AntiDot” Overlay & NFC Attack Suite
- **Description**: Multi-stage malware that deploys phishing overlays atop legitimate apps, abuses virtualization for stealth, and captures NFC payment data during tap-to-pay transactions.
- **Impact**: Theft of banking credentials, credit-card data, and real-time transaction manipulation.
- **Status**: 3,775 devices confirmed compromised across 273 campaigns; no OS-level patch— mitigations depend on mobile AV and user permission hygiene.

### Scattered Spider Social-Engineering Intrusions
- **Description**: Highly organized English-speaking crew uses voice phishing, MFA fatigue, and stolen employee credentials to obtain initial access, followed by remote management tools and ransomware deployment.
- **Impact**: Operational outages, point-of-sale disruptions, data exfiltration; estimated damages up to $592 million for M&S and Co-op alone.
- **Status**: Attacks continue against retail and insurance sectors; no single technical patch—requires improved identity, MFA, and help-desk verification procedures.

### Lazarus Group Breach of BitoPro Exchange
- **Description**: North-Korean APT compromised back-end infrastructure of Taiwanese exchange, siphoning private keys and draining wallets.
- **Impact**: $11 million in cryptocurrency theft; potential secondary victimization if stolen credentials reused elsewhere.
- **Status**: Exchange implemented emergency wallet rotations; investigation ongoing.  No vendor patch disclosed.

### Salt Typhoon (aka Volt Typhoon) Espionage Against Viasat
- **Description**: China-nexus operators leveraged exposed edge devices and living-off-the-land techniques to burrow into satellite-communications networks.
- **Impact**: Intelligence gathering on critical telecom infrastructure; risk of latent disruption capability.
- **Status**: Activity confirmed; remediation steps shared with government partners, but specific fixes remain undisclosed for operational security.

## Affected Systems and Products

- **HTTP/2 Web Servers & Reverse Proxies**  
  Platform: All major OS and cloud platforms supporting HTTP/2.

- **GitHub Software Supply Chain**  
  Platform: Developer workstations, CI/CD pipelines, and any environment that pulls code from public GitHub repositories.

- **Android Mobile Devices (Godfather variant)**  
  Platform: Android 8 – 14; especially devices permitting sideloading or lacking Google Play Protect.

- **Android Mobile Devices (AntiDot campaigns)**  
  Platform: Same as above, with focus on users enabling NFC payments.

- **Retailer & Insurance Corporate Networks (Scattered Spider)**  
  Platform: Windows and macOS endpoints, Okta identity deployments, and RMM tools.

- **BitoPro Cryptocurrency Exchange Infrastructure**  
  Platform: Linux-based wallet servers, web applications, and internal admin portals.

- **Viasat Satellite & Edge Networking Gear**  
  Platform: Routers, firewalls, and IoT devices exposed to the public Internet.

## Attack Vectors and Techniques

- **HTTP/2 Rapid Reset Flooding**  
  Vector: Layer-7 DDoS using massive parallel stream cancellations.

- **Repository Typosquatting & Code Poisoning**  
  Vector: Users unknowingly `git clone` or `pip install` malicious repos/packages.

- **Virtualized App Cloning (Android)**  
  Vector: Malware-created containers masquerading as legitimate banking apps.

- **Overlay Phishing (Android)**  
  Vector: Draw-over-other-apps permission to capture credentials in real time.

- **Voice Phishing & MFA Fatigue (Scattered Spider)**  
  Vector: Call-center–style social engineering to trick employees into sharing one-time codes.

- **Remote Management Tool Abuse**  
  Vector: Legitimate RMM agents (e.g., AnyDesk, ScreenConnect) executed post-compromise.

- **Seed Phrase / Private-Key Exfiltration (Lazarus)**  
  Vector: Server-side wallet-management scripts modified to log keys.

- **Living off the Land (Salt Typhoon)**  
  Vector: PowerShell, WMI, and native network utilities to avoid detection.

## Threat Actor Activities

- **Scattered Spider**  
  Campaign: Concurrent attacks on Marks & Spencer, Co-op, and U.S. insurers (Aflac).  Emphasizes social engineering, identity compromise, and extortion.

- **Lazarus Group**  
  Campaign: BitoPro exchange breach netting $11 M in crypto; aligns with historical financially motivated operations funding DPRK.

- **Salt Typhoon (Volt Typhoon)**  
  Campaign: Long-term espionage in telecom sector; now confirmed impact on Viasat satellite networks.

- **Financially Motivated Android Crews**  
  Campaign: Godfather and AntiDot malware waves targeting over 3,700 devices for credential theft and fraudulent transactions.

- **Unknown Botnet Operators**  
  Campaign: Record-breaking 7.3 Tbps DDoS leveraging HTTP/2 weakness against a hosting provider; demonstrates increased botnet firepower and protocol abuse.

- **Malware Repository Builders**  
  Campaign: Ongoing publication of malicious copycat repositories (200+ detected) aiming at developers and gamers to seed wider compromises.

