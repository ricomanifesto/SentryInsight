# Exploitation Report

During the last week, attackers focused on financially-motivated intrusions and high-visibility sabotage rather than chaining headline zero-day exploits.  North Korea’s Lazarus Group stole $11 million from BitoPro by breaching the exchange’s hot-wallet infrastructure, while China-nexus “Salt Typhoon” quietly penetrated satellite-communications provider Viasat.  Record-setting 7.3 Tbps DDoS traffic pummeled a hosting company in the largest attack ever observed, and the Scattered Spider syndicate continued abusing identity-management weaknesses to breach U.S. insurers, including Aflac.  Simultaneously, new Android malware families (Godfather, AntiDot) leveraged virtualization and overlay tricks to hijack mobile banking sessions.  Collectively, these campaigns illustrate the continued exploitation of cloud misconfigurations, weak identity controls, and emergent DDoS techniques that yield immediate financial and geopolitical payoff for well-resourced threat actors.

## Active Exploitation Details

### BitoPro Exchange Hot-Wallet Breach
- **Description**: Attackers infiltrated BitoPro’s cryptocurrency hot-wallet environment on 8 May 2025, siphoning digital assets directly from customer wallets.  
- **Impact**: Immediate theft of approximately $11 million in cryptocurrency, disruption of exchange operations, and loss of customer trust.  
- **Status**: Confirmed active exploitation.  BitoPro has paused withdrawals, rotated wallet keys, and is working with law enforcement; no vendor patch is applicable because compromise stemmed from operational infrastructure rather than a discrete software flaw.  

### Salt Typhoon Cloud Intrusion (Viasat)
- **Description**: China-linked Salt Typhoon gained unauthorized access to Viasat’s internal environment.  While public details are limited, the attack leveraged previously observed tactics that exploit cloud misconfigurations and stolen credentials to move laterally across SaaS and IaaS.  
- **Impact**: Potential access to sensitive satellite-communications data and disruption of a critical-infrastructure provider, although Viasat reports no service impact to customers.  
- **Status**: Ongoing investigation; attack is active in the wild.  No vendor patch—mitigation centers on identity hardening and log review.  

### Record-Breaking 7.3 Tbps DDoS Flood
- **Description**: Cloudflare mitigated the largest distributed-denial-of-service event on record, peaking at 7.3 Tbps and delivering 37.4 TB of traffic in 45 seconds against a hosting provider.  The flood relied on novel HTTP/2 abuse combined with botnet amplification.  
- **Impact**: Could have rendered the victim’s infrastructure inaccessible; demonstrates that attackers can overwhelm even well-provisioned bandwidth if defenses are absent.  
- **Status**: Active technique observed in May 2025.  Mitigation available through upstream DDoS scrubbing and protocol filtering.  

### Scattered Spider Identity-Misuse Attacks (Aflac)
- **Description**: The financially-motivated Scattered Spider group compromised Aflac by social-engineering service-desk personnel and abusing single-sign-on/OAuth functionality to pivot across insurance networks.  
- **Impact**: Theft of personal data of policyholders and employees; potential regulatory penalties.  
- **Status**: Campaign is active.  Mitigation requires stronger help-desk procedures and phishing-resistant MFA for privileged accounts.  

### Android Banking Malware Virtualization Exploit (Godfather / AntiDot)
- **Description**: New variants create isolated virtual containers on Android devices, sidestepping OS sandboxing to overlay fake login screens on legitimate banking apps and silently initiate fraudulent transactions.  
- **Impact**: Full account takeover, interception of 2FA codes, and unauthorized transfers.  
- **Status**: In-the-wild attacks ongoing.  Google Play Protect updates and app-store takedowns issued; users must update Play Services and avoid sideloading.  

## Affected Systems and Products

- **BitoPro Cryptocurrency Exchange**  
  - **Platform**: Web-based wallet infrastructure (hot wallets, custodian APIs)  

- **Viasat Corporate Network & Satellite Control Systems**  
  - **Platform**: Hybrid on-prem / Azure and Office 365 cloud tenants  

- **Unnamed European Hosting Provider**  
  - **Platform**: Public-facing HTTP/2 web-server clusters behind Cloudflare  

- **Aflac Insurance IT Environment**  
  - **Platform**: Okta SSO, Azure AD, and internal policy-administration portals  

- **Android Devices (godfather / AntiDot campaigns)**  
  - **Platform**: Android 9 – 14; exploits Accessibility API, virtualization features  

## Attack Vectors and Techniques

- **Hot-Wallet Compromise**  
  - **Vector**: Compromised administrative keys/API tokens; likely spear-phishing and lateral movement into wallet servers.  

- **Cloud Misconfiguration & Credential Abuse**  
  - **Vector**: Stolen or brute-forced Azure/O365 credentials; exploitation of excessive privileges to expand access (Salt Typhoon, Scattered Spider).  

- **HTTP/2 Flood Amplification**  
  - **Vector**: Massive botnet leveraging HTTP/2 protocol features to reset streams rapidly, multiplying request rate and overwhelming target.  

- **Help-Desk Social Engineering**  
  - **Vector**: Voice-phishing and SIM-swap techniques to impersonate employees and obtain password-reset tokens (Scattered Spider).  

- **Android Virtualization Overlay**  
  - **Vector**: Malicious APK launches a virtual container, installs legitimate banking app inside, and injects overlay screens to steal credentials (Godfather, AntiDot).  

## Threat Actor Activities

- **Lazarus Group (North Korea)**  
  - **Campaign**: $11 M BitoPro heist; continues to target crypto exchanges for sanctions-evasion funding.  

- **Salt Typhoon (China-Nexus)**  
  - **Campaign**: Stealthy intrusions into telecommunications and satellite providers; objective is espionage and pre-positioning.  

- **Scattered Spider (FIN8/Octo Tempest affiliate)**  
  - **Campaign**: Coordinated attacks on U.S. insurance sector, leveraging social engineering and identity-provider abuse to steal PII and extort victims.  

- **Unknown Botnet Operator(s)**  
  - **Campaign**: Coordinated 7.3 Tbps HTTP/2 DDoS assault; demonstrates commoditized DDoS-as-a-Service capabilities at unprecedented scale.  

- **Godfather & AntiDot Malware Operators**  
  - **Campaign**: 273 active Android campaigns targeting financial institutions; monetization via credential theft and fraudulent transactions.  

These events highlight that attackers continue to favor credential theft, misconfiguration abuse, and network-layer flooding over traditional exploit-code targeting newly disclosed CVEs—reinforcing the need for identity security, architectural hardening, and layered DDoS defense.