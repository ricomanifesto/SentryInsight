# Exploitation Report

The past week’s security landscape was dominated by four distinct exploitation trends: (1) weaponisation of the HTTP/2 “Rapid Reset” flaw to generate the largest-ever 7.3 Tbps DDoS attack, (2) an aggressive supply-chain campaign flooding GitHub with weaponised “copy-cat” repositories, (3) large-scale abuse of Android’s overlay and virtualisation features by new banking-trojan families, and (4) highly-targeted identity-system intrusions led by the Scattered Spider group against retailers and insurers. Together these events highlight a shift toward abusing core internet protocols, developer ecosystems, mobile operating-system internals, and identity platforms—often in parallel—to maximise impact and monetisation.

## Active Exploitation Details

### HTTP/2 “Rapid Reset” Vulnerability  
- **Description**: A protocol-level weakness in HTTP/2 that allows an attacker to continuously open and immediately cancel streams (“RST_STREAM floods”), massively amplifying request volumes against servers and intermediary CDNs.  
- **Impact**: Enables hyper-volumetric DDoS attacks; Cloudflare recorded 7.3 Tbps and 37.4 TB of traffic in 45 seconds against a hosting provider.  
- **Status**: Actively exploited in the wild; mitigations available via vendor patches and configuration changes across major web-server and CDN stacks.

### Malicious Copy-Cat Repositories on GitHub  
- **Description**: Threat actors seeded dozens of repositories impersonating popular projects; the imposters contain obfuscated malware that activates at build or install time.  
- **Impact**: Compromises developer workstations and downstream applications, leading to credential theft, persistence, and potential supply-chain insertion.  
- **Status**: Ongoing campaign; GitHub has removed many repos but new ones continue to appear. No traditional patch—developers must rely on repository verification and signing.

### Android Overlay & Virtualisation Abuse (Godfather / AntiDot)  
- **Description**: Banking-trojan operators create isolated virtual environments on Android devices, then use overlay windows, NFC abuse, and accessibility-service hijacking to steal credentials and perform fraudulent transactions.  
- **Impact**: Full takeover of mobile banking sessions, interception of MFA codes, unauthorised fund transfers. Over 3,775 devices compromised across 273 campaigns (AntiDot); Godfather seen evolving similar tactics.  
- **Status**: Actively exploited zero-day technique; Google Play Protect updates distributed, but devices sideloading apps remain vulnerable.

### Okta Identity Session Compromise (Scattered Spider Operations)  
- **Description**: Scattered Spider leverages social-engineering, SIM-swapping, and MFA-prompt bombing to obtain Okta Super Admin sessions, pivoting into corporate SaaS and VPNs.  
- **Impact**: Exfiltration of customer PII, operational disruption, and reported $592 million in combined losses for Marks & Spencer and Co-op; follow-on breaches reported at Aflac.  
- **Status**: Campaign is currently active; Okta has issued hardening guidance and pushed new detection rules.

## Affected Systems and Products

- **HTTP/2-Enabled Web Servers & CDNs**: Apache httpd (2.4.x), NGINX (1.25.x), Envoy, Cloudflare edge infrastructure  
  - **Platform**: Linux, BSD, Windows hosts running HTTP/2 or fronted by supporting CDNs  

- **GitHub Projects & Developer Toolchains**: Python, JavaScript, Go modules cloned from public repos  
  - **Platform**: Cross-platform developer environments (Windows, macOS, Linux)  

- **Android Smartphones**: Devices running Android 11–14; Pixels and multiple OEM models targeted  
  - **Platform**: Google Play and sideloaded app ecosystems  

- **Okta Identity Cloud & Downstream SaaS**: Retail, insurance, and telecom tenants with Okta SSO deployments  
  - **Platform**: Cloud-based identity management integrated with on-prem AD and Azure-AD hybrids

## Attack Vectors and Techniques

- **RST_STREAM Flooding**  
  - **Vector**: Crafted HTTP/2 requests that instantly cancel streams to overwhelm target infrastructure.

- **Repository Typosquatting & Impersonation**  
  - **Vector**: Uploading look-alike project names or forks; malicious code executes during package install or build.

- **Android Accessibility & Virtual Machine Abuse**  
  - **Vector**: Malware requests AccessibilityService privileges, spins lightweight VMs, displays fraudulent overlays, and intercepts NFC-based transactions.

- **MFA Fatigue & SIM-Swap-Assisted Account Takeover**  
  - **Vector**: Repeated authentication push notifications combined with social-engineered telecom support calls to hijack Okta admin accounts.

## Threat Actor Activities

- **Scattered Spider (UNC3944 / Scatter Swine)**  
  - **Campaign**: Coordinated intrusions on U.K. retailers and U.S. insurers; leverages Okta session theft, data exfiltration, and extortion. Estimated losses up to $592 M.

- **Lazarus Group**  
  - **Campaign**: $11 M cryptocurrency theft from Taiwanese exchange BitoPro; ties to ongoing blockchain-targeted operations.

- **Salt Typhoon (China-nexus)**  
  - **Campaign**: Compromised Viasat through cloud-service footholds; intelligence-gathering focus, details shared with U.S. government partners.

- **Qilin Ransomware-as-a-Service**  
  - **Campaign**: Introduced “Call Lawyer” negotiation service to intensify pressure on victims; affiliates exploiting unpatched entry points for lateral movement.

- **Unattributed Threat Actors (GitHub Supply-Chain)**  
  - **Campaign**: Over 200 trojanised repositories targeting gamers and developers with information-stealing payloads.