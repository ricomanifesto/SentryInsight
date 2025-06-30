# Exploitation Report

The most critical exploitation activity this cycle centers on two separate but closely-related vulnerabilities in Citrix NetScaler ADC and NetScaler Gateway appliances. A first authentication-bypass issue (“Citrix Bleed”) remains widely exploited on more than 1,200 Internet-facing devices, while a newer flaw (“Citrix Bleed 2”) is now also being leveraged in the wild, prompting emergency monitoring by multiple security vendors. At the same time, China-linked actors in the LapDogs campaign have compromised over a thousand SOHO routers through chained firmware weaknesses, and several other threat groups—including Blind Eagle and Scattered Spider—continue to pair social-engineering with existing exploits to expand their foothold across financial, transportation, and energy sectors.

## Active Exploitation Details

### Citrix NetScaler ADC/Gateway Authentication Bypass (“Citrix Bleed”)
- **Description**: A critical flaw that allows unauthenticated attackers to bypass login protections on NetScaler ADC and NetScaler Gateway, granting direct access to session data and enabling account hijacking.  
- **Impact**: Credential theft, session takeover, lateral movement into internal networks, and potential data exfiltration.  
- **Status**: Confirmed active exploitation; patches have been released, yet over 1,200 appliances remain unpatched and exposed.  

### Citrix NetScaler ADC/Gateway Heap Memory Disclosure (“Citrix Bleed 2”)
- **Description**: A newly disclosed vulnerability that leaks heap memory contents, enabling threat actors to harvest session tokens and other sensitive information without authentication.  
- **Impact**: Session hijacking, privilege escalation, and the groundwork for full network compromise.  
- **Status**: ReliaQuest telemetry indicates an uptick in live attacks; a security update is available, but widespread patching is still underway.  
- **CVE ID**: CVE-2025-5777  

### SOHO Router Multi-Vendor Firmware Weaknesses (LapDogs Campaign)
- **Description**: An array of unpatched or end-of-life firmware bugs across several SOHO router brands abused to gain persistent remote shell access, create proxy nodes, and build espionage infrastructure.  
- **Impact**: Full device takeover, covert C2 relay, and surveillance staging against downstream targets.  
- **Status**: Actively exploited in the wild with more than 1,000 devices confirmed compromised; no coordinated vendor patch cycle observed.  

## Affected Systems and Products

- **Citrix NetScaler ADC & NetScaler Gateway**  
  - **Platform**: All hardware or virtual appliances running vulnerable builds in the 12.1, 13.0, 14.1, and 13.1 branches.

- **Citrix NetScaler ADC & NetScaler Gateway (Bleed 2)**  
  - **Platform**: Latest 14.x and 13.x firmware prior to emergency hotfixes released in June 2025.

- **SOHO Routers (LapDogs infrastructure)**  
  - **Platform**: Mixed small-office/home-office devices from multiple vendors, primarily Linux-based firmware with outdated kernels and web-UI components.  

## Attack Vectors and Techniques

- **HTTP(S) Request Forgery**  
  - **Vector**: Crafted web requests exploit Citrix gateways to bypass authentication or dump heap memory.  

- **Remote Shell Deployment on SOHO Routers**  
  - **Vector**: Chained firmware flaws and default/weak credentials provide attackers with root shell, followed by installation of custom tunneling software.  

- **Phishing-Driven Malware Staging (Blind Eagle / OneClik)**  
  - **Vector**: Spear-phishing lures deliver malicious ClickOnce packages or bundled RATs hosted on bulletproof infrastructure.  

- **Social-Engineering and MFA Fatigue (Scattered Spider)**  
  - **Vector**: Voice, SMS, and push-notification flooding to coerce employees into granting session tokens, later paired with Citrix exploitation for lateral movement.  

## Threat Actor Activities

- **LapDogs (China-linked)**  
  - **Campaign**: Long-running cyber-espionage operation using a mesh of compromised SOHO routers to hide attacker traffic and stage intrusions against higher-value networks.  

- **Blind Eagle (APT-C-36)**  
  - **Campaign**: Targeting Colombian financial institutions via Proton66-hosted phishing pages, followed by RAT deployment for credential theft and wire-fraud facilitation.  

- **Scattered Spider**  
  - **Campaign**: Expanding from retail and insurance into airline and transportation sectors; combines social-engineering with exploitation of Citrix gateways for persistence.  

- **Unknown Crimeware Groups**  
  - **Campaign**: Opportunistic scanning and exploitation of unpatched Citrix appliances worldwide to establish footholds for ransomware or data-theft monetization.