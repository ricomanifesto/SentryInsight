# Exploitation Report

Over the past week, threat-hunting teams have tracked a diverse set of active exploits ranging from supply-chain compromises in developer ecosystems to state-sponsored campaigns abusing network gear. The most critical activity includes North Korea’s “Contagious Interview” operation seeding 35 malicious npm packages, Chinese actors leveraging a Cisco flaw against global telecoms, and a trojanized SonicWall NetExtender client siphoning VPN credentials. Concurrently, attackers are abusing misconfigured Docker APIs for covert cryptocurrency mining via Tor, weaponizing Windows File Explorer through the new “FileFix” technique, injecting keyloggers into on-premises Microsoft Exchange login pages, and operating a China-nexus “LapDogs” relay network built on backdoored SOHO devices. All incidents are confirmed in-the-wild with active exploitation and, in several cases, no vendor patch yet available.

## Active Exploitation Details

### Malicious npm Package Supply-Chain Attack (“Contagious Interview”)
- **Description**: 35 malicious packages uploaded to npm impersonate legitimate developer utilities. Upon installation, post-install scripts fetch second-stage backdoors and beacon to attacker-controlled C2.
- **Impact**: Remote code execution on developer machines, credential theft, and lateral movement into corporate CI/CD pipelines.
- **Status**: Ongoing; packages removed as discovered, but new variants continue to appear.

### Trojanized SonicWall NetExtender VPN Client
- **Description**: A threat actor modified the official NetExtender SSL-VPN installer, adding credential-harvesting payloads while preserving full VPN functionality to avoid detection.
- **Impact**: Theft of corporate VPN usernames, passwords, and potential MFA tokens, granting direct network access.
- **Status**: Actively distributed through look-alike sites and unsolicited emails; no official SonicWall code-signing compromise reported. Legitimate installer remains safe—users must verify hashes.

### Cisco Network Gear Flaw Exploited by “Salt Typhoon”
- **Description**: Chinese state-sponsored group exploited an unspecified Cisco vulnerability to gain privileged access to telecom infrastructure in Canada, adding to a wider global campaign.
- **Impact**: Remote code execution and persistent foothold in carrier networks, enabling espionage and traffic manipulation.
- **Status**: Exploitation confirmed in February; Cisco guidance and mitigations released, patch availability status undisclosed in public reporting.

### Backdoored SOHO Devices (“LapDogs” ORB Network)
- **Description**: China-nexus operation compromises small office/home office routers and IoT devices, inserting custom backdoors that convert them into “Operational Relay Boxes” (ORBs) for proxying espionage traffic.
- **Impact**: Covert relay of malicious traffic, anonymization of attacker infrastructure, and staging for additional intrusions.
- **Status**: Campaign active across the US and Southeast Asia; remediation requires device firmware replacement or secure wipe.

### Misconfigured Docker API Abuse via Tor
- **Description**: Attackers scan for Docker daemons exposed on TCP, then use Tor exit nodes to deploy cryptomining containers, hindering attribution and blocking.
- **Impact**: Resource hijacking, increased cloud bills, possible lateral movement into connected services.
- **Status**: Active; no software patch—secure by disabling unauthenticated remote API and applying firewall rules.

### Microsoft Exchange Login Page Keylogger Injection
- **Description**: Threat actors compromise on-premises Exchange servers, injecting malicious JavaScript into OWA/Exchange Control Panel login pages to exfiltrate credentials in real time.
- **Impact**: Account takeover of email accounts, privilege escalation, and potential full domain compromise.
- **Status**: Over 70 publicly exposed servers impacted; mitigation requires full incident response and hardening of Internet-facing Exchange deployments.

### “FileFix” Social Engineering Exploit in Windows File Explorer
- **Description**: Variant of ClickFix that entices users to paste a crafted UNC path or double-click a lure, which executes hidden PowerShell commands via the Explorer address bar without prompting.
- **Impact**: Command execution under current user context, bypassing many application-control defenses.
- **Status**: Technique publicly released; no Microsoft patch (design abuse rather than software bug). Defense relies on user education and address-bar execution monitoring.

## Affected Systems and Products

- **npm Ecosystem / Node.js Developers**  
  Platform: Windows, macOS, Linux developer workstations running npm

- **SonicWall NetExtender SSL-VPN**  
  Platform: Windows and macOS clients; corporate networks using SonicWall firewalls

- **Cisco Network Devices (model unspecified in reporting)**  
  Platform: Carrier-grade routers/switches in telecom environments

- **Consumer & SOHO Routers/IoT Devices (LapDogs)**  
  Platform: Linux-based firmware across multiple hardware vendors in US and SE Asia

- **Docker Engine with Remote API Exposed (TCP :2375/2376)**  
  Platform: Linux and Windows hosts in cloud and on-prem

- **Microsoft Exchange Server (on-prem, OWA/ECP enabled)**  
  Platform: Windows Server running Exchange 2016/2019

- **Windows 10 & 11 File Explorer**  
  Platform: Desktop environments where users can access the Explorer address bar

## Attack Vectors and Techniques

- **Package Typosquatting & Dependency Confusion**  
  Vector: Malicious npm packages masquerading as popular libs.

- **Trojanized Installer Distribution**  
  Vector: Fake download portals and phishing emails supplying tampered NetExtender installers.

- **Network Device Exploitation**  
  Vector: Remote exploitation of a Cisco firmware/software flaw to gain privileged shell access.

- **Firmware Backdooring of SOHO Devices**  
  Vector: Exploiting weak/default credentials or legacy vulnerabilities, then flashing custom images.

- **Unauthenticated Docker API Access over Tor**  
  Vector: Mass-scanning from Tor exit nodes, followed by docker run to deploy cryptominers.

- **Web Page Script Injection (Credential Harvesting)**  
  Vector: Post-exploitation modification of Exchange login pages to embed keylogger JavaScript.

- **Address-Bar Command Injection (FileFix)**  
  Vector: Socially engineered UNC paths or clickable shortcuts triggering PowerShell via Explorer.

## Threat Actor Activities

- **North Korean “Contagious Interview” Operators**  
  Campaign: Ongoing supply-chain infiltration using npm to compromise developers, possibly to reach cryptocurrency or defense targets.

- **Unidentified Threat Actor (SonicWall Installer)**  
  Campaign: Credential theft aimed at organizations relying on SonicWall VPN infrastructures.

- **Chinese State-Sponsored “Salt Typhoon”**  
  Campaign: Multi-nation telecom intrusion spree exploiting Cisco gear to surveil network traffic.

- **China-Nexus “LapDogs” Group**  
  Campaign: Construction of a large ORB proxy network from backdoored SOHO devices for clandestine espionage routing.

- **Cryptocurrency Mining Actors (Tor Docker Campaign)**  
  Campaign: Monetization via XMR mining containers; hides source through Tor, targets cloud workloads.

- **Unknown Exchange Keylogger Operators**  
  Campaign: Harvesting corporate email credentials from over 70 servers, likely leading to further BEC or espionage.

- **Security Researcher (FileFix Proof-of-Concept)**  
  Campaign: Public PoC demonstrating new social-engineering vector; could be weaponized by threat actors imminently.

**End of Report**

