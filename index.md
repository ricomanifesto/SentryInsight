# Exploitation Report

June’s threat landscape is dominated by active attacks on remote-access infrastructure and software supply chains. Citrix NetScaler appliances are under heavy fire from two distinct flaws—one (“CitrixBleed 2”) enabling session hijacking and another (CVE-2025-6543) already causing denial-of-service outages worldwide. At the same time, threat actors are leveraging recently disclosed ConnectWise ScreenConnect vulnerabilities (CVE-2024-1709 & CVE-2024-1708) in live campaigns, pairing them with a trojanized SonicWall NetExtender installer to obtain persistent remote access. Parallel campaigns showcase North Korea’s continued use of malicious npm packages (“Contagious Interview”) and the “OneClik” operation abusing Microsoft ClickOnce and AWS to infiltrate energy-sector targets. Collectively, these activities emphasize the critical need for rapid patching of internet-facing services and rigorous supply-chain controls.

## Active Exploitation Details

### CVE-2025-6543 NetScaler ADC/Gateway DoS
- **Description**: Boundary-check flaw in the request-handling component of Citrix NetScaler ADC and Gateway that can be triggered pre-authentication to exhaust system resources.  
- **Impact**: Remote attackers force appliances into a crash/reboot loop, disrupting all customer-facing and internal applications that rely on the load balancer/VPN.  
- **Status**: Confirmed in-the-wild exploitation; emergency patches released by Citrix.  
- **CVE ID**: CVE-2025-6543  

### “CitrixBleed 2” Session Hijacking in NetScaler
- **Description**: Memory-handling weakness similar to 2023’s CitrixBleed, allowing unauthenticated attackers to retrieve lingering session tokens from the appliance’s cache.  
- **Impact**: Full takeover of active administrator or user sessions, enabling lateral movement and data theft without credentials.  
- **Status**: Exploits observed; hotfixes available in the latest firmware builds.  

### CVE-2024-1709 ConnectWise ScreenConnect Authentication Bypass
- **Description**: Logic flaw in ScreenConnect’s web application that skips credential verification when a crafted URI containing encoded newline characters is supplied.  
- **Impact**: Unauthenticated remote code execution on the ScreenConnect server, delivering malware or further payloads to all connected endpoints.  
- **Status**: Weaponised in current attacks distributing trojanized SonicWall installers; patches provided in version 24.3.4.  
- **CVE ID**: CVE-2024-1709  

### CVE-2024-1708 ConnectWise ScreenConnect Path Traversal
- **Description**: Directory traversal via improperly sanitised path parameters, permitting reading or writing arbitrary files outside the web root.  
- **Impact**: File disclosure, web-shell planting, or privilege escalation on vulnerable servers.  
- **Status**: Exploited alongside CVE-2024-1709 in combined intrusion sets; fixed in version 24.3.4.  
- **CVE ID**: CVE-2024-1708  

## Affected Systems and Products

- **Citrix NetScaler ADC & Gateway**  
  - **Platform**: Physical and virtual appliances (13.1 / 14.1 and earlier maintenance builds) deployed on-prem and in cloud VPCs  
- **ConnectWise ScreenConnect (On-Premise)**  
  - **Platform**: Windows & Linux servers running versions prior to 24.3.4  
- **SonicWall NetExtender (Trojanized Build)**  
  - **Platform**: Windows endpoints downloading installers from rogue sites or phishing links  
- **Corporate Workstations / Servers (Energy Sector)**  
  - **Platform**: Windows systems with ClickOnce enabled, susceptible to “OneClik” infection chain  
- **Developer Workstations (npm Ecosystem)**  
  - **Platform**: macOS, Linux, Windows environments that automatically resolve and build malicious npm packages  

## Attack Vectors and Techniques

- **ClickOnce Abuse (OneClik)**  
  - **Vector**: Phishing e-mails deliver .appref-ms files signed by fraudulent certificates; execution pulls payloads from AWS S3, bypassing many controls.  

- **Session Token Extraction (CitrixBleed 2)**  
  - **Vector**: Crafted HTTPS requests read residual session memory, stealing valid authentication cookies.  

- **Denial-of-Service Flood (CVE-2025-6543)**  
  - **Vector**: Repeated malformed packets overwhelm NetScaler request processing, forcing watchdog reboots.  

- **Auth Bypass URI Manipulation (CVE-2024-1709)**  
  - **Vector**: Encoded newline payload in REST endpoint skips login checks, granting admin shell.  

- **Path Traversal Write (CVE-2024-1708)**  
  - **Vector**: “..\” sequences in file-management API calls drop web shells or read config files.  

- **Supply-Chain Poisoning (Contagious Interview)**  
  - **Vector**: Malicious npm packages auto-executing post-install scripts to deploy infostealers/backdoors.  

- **Trojanized Installer Delivery**  
  - **Vector**: Fake SonicWall NetExtender executable sideloaded via phishing; harvested credentials used for network penetration.  

## Threat Actor Activities

- **Unknown Operator (“OneClik” Campaign)**  
  - Compromises energy-sector organizations in North America and Europe; leverages AWS infrastructure for staging; post-exploitation uses custom Golang backdoors.  

- **North Korean Cluster (“Contagious Interview”)**  
  - Continues multi-year developer-targeting operation; publishes at least 35 poisoned npm packages; goal is theft of source code and corporate credentials.  

- **Unattributed Actors Exploiting CVE-2025-6543**  
  - Mass-scanning the internet, causing widespread NetScaler outages; activity observed within hours of PoC release.  

- **Unattributed Actors Leveraging CitrixBleed 2**  
  - Focus on technology and financial-services firms; objective appears to be session hijack for data exfiltration.  

- **Remote-Access Intrusion Set (ConnectWise/SonicWall)**  
  - Uses CVE-2024-1709 & 1708 for initial foothold, drops trojanized NetExtender to persist, steals VPN and domain credentials; victims span SMEs in healthcare, retail, and manufacturing.