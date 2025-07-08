# Exploitation Report

Over the past week, defenders observed a notable uptick in active exploitation against edge devices, consumer IoT, and widely-deployed enterprise software.  The most critical activity centers on the release of proof-of-concept exploits for the new “CitrixBleed 2” vulnerability (CVE-2025-5777), aggressive botnet recruitment of vulnerable TBK DVRs and Four-Faith industrial routers, and fresh zero-day abuse of Google Chrome highlighted in multiple threat-intel briefings.  CISA simultaneously added four newly exploited flaws to its Known Exploited Vulnerabilities (KEV) catalog, underscoring the speed with which attackers weaponize recent disclosures.  Retail, manufacturing, and critical-infrastructure networks remain prime targets, with groups such as RondoDox, TAG-140, and nation-state actors leveraging a mix of credential abuse, supply-chain weaknesses, and outright remote-code-execution (RCE) exploits to gain persistent footholds.

## Active Exploitation Details

### CitrixBleed 2 in NetScaler ADC/Gateway
- **Description**: Memory-handling flaw in NetScaler Gateway and ADC allowing unauthenticated HTTP requests to read sensitive session tokens and credentials, leading to full device compromise and lateral movement.  
- **Impact**: Credential disclosure, session hijacking, remote code execution, and potential complete takeover of appliances servicing VPN and application delivery.  
- **Status**: Public proof-of-concept code released; active scanning observed. Patches are available from Citrix and must be applied immediately.  
- **CVE ID**: CVE-2025-5777  

### TBK Digital Video Recorder Flaw
- **Description**: Logic error in authentication routines of TBK DVR firmware enables attackers to bypass login controls and issue privileged API requests.  
- **Impact**: Remote execution of arbitrary system commands; integration of devices into DDoS botnets; live video feed hijacking.  
- **Status**: Exploited in the wild by the new RondoDox botnet. No official vendor patch; mitigations require network isolation and credential hardening.  

### Four-Faith Industrial Router Vulnerability
- **Description**: Improper input validation in the device’s web-management interface allows command-injection over HTTP.  
- **Impact**: Remote code execution, persistent malware installation, and use as DDoS amplifiers.  
- **Status**: Weaponized by RondoDox. Firmware updates are not yet publicly released; users must disable remote management and restrict inbound traffic.  

### Google Chrome Zero-Day
- **Description**: Type-confusion flaw in the V8 JavaScript engine enabling sandbox escape and full browser compromise when a victim visits a malicious page.  
- **Impact**: Arbitrary code execution in the context of the logged-in user, credential theft, and follow-on malware delivery.  
- **Status**: Actively exploited in the wild; Google issued an emergency update for all platforms.  

### CISA KEV Additions (Four Newly Exploited Flaws)
- **Description**: A set of four distinct vulnerabilities across multiple vendors and products, each confirmed to be exploited against U.S. networks.  
- **Impact**: Ranges from privilege escalation to remote code execution, depending on the specific product.  
- **Status**: Vendors have released patches; federal agencies must remediate by CISA-mandated deadlines.  

### Default-Password Abuse in Industrial Control Systems
- **Description**: Attackers leveraged unchanged factory credentials on PLCs to access and manipulate water-facility pressure stations.  
- **Impact**: Potential disruption of physical processes, safety-system override, and environmental damage.  
- **Status**: Exploitation confirmed; mitigations include enforced credential rotation and network segmentation.  

### Chrome Extension Supply-Chain Abuse (“Color Picker”)
- **Description**: Popular Chrome Web Store extension updated with malicious code that hijacks browser sessions and injects spyware.  
- **Impact**: Session theft, redirection to phishing pages, data exfiltration.  
- **Status**: Extension still available at time of reporting; Google review pending.  

## Affected Systems and Products

- **Citrix NetScaler ADC / Gateway**: Versions prior to patched build 14.1-22.47 and 13.1-51.19  
- **TBK DVRs**: Multiple models (e.g., DVRS-5004, DVRS-8008) running legacy firmware  
- **Four-Faith Routers**: F-G100, F-R200 series with remote-management enabled  
- **Google Chrome**: All desktop and Android builds prior to the July emergency release  
- **Industrial PLCs & SCADA Controllers**: Water-utility pressure-station equipment with default credentials  
- **Chrome “Color Picker” Extension**: Version 4.3.1 and derivatives still hosted in the Chrome Web Store  

## Attack Vectors and Techniques

- **HTTP Memory-Leak Exploit**  
  - **Vector**: Crafted unauthenticated requests to NetScaler `/vpn/` and `/cgi/` endpoints extract session tokens.  

- **Botnet Auto-Enrollment via Auth-Bypass**  
  - **Vector**: Mass-internet scanning for TBK DVR login pages; attackers send tampered cookies to skip authentication and push malware.  

- **Command-Injection over Web Interface**  
  - **Vector**: Malformed parameter in `ping` diagnostic page of Four-Faith routers executes shell commands.  

- **Drive-By Browser Exploitation**  
  - **Vector**: Malicious JavaScript triggers V8 type confusion, achieving RCE on unpatched Chrome.  

- **Default-Credential Login**  
  - **Vector**: Automated scripts attempt vendor-shipped usernames/passwords on exposed PLCs.  

- **Malicious Extension Update**  
  - **Vector**: Extension auto-updates via Chrome Web Store, granting spyware code the same permissions as the original add-on.  

## Threat Actor Activities

- **RondoDox Botnet Operators**  
  - **Campaign**: Large-scale DDoS infrastructure building, leveraging TBK DVR and Four-Faith router exploits to gain bandwidth and persistence.  

- **TAG-140**  
  - **Campaign**: “ClickFix-Style” spear-phishing against Indian government and rail sectors, using malicious scripts to deploy the BroaderAspect loader and DRAT v2 RAT, likely for long-term espionage.  

- **Iran-Linked Water-Facility Intrusion Set**  
  - **Campaign**: Targeted ICS compromise through default credentials, aiming to control municipal water pressure systems.  

- **Unknown Chrome 0-Day Broker**  
  - **Campaign**: Sale and deployment of exploit kit in drive-by attacks against high-value browser targets; observed in malvertising chains.  

- **Extension-Hijack Actors**  
  - **Campaign**: Supply-chain poisoning of popular Chrome add-ons to redirect web traffic and steal session cookies across >100,000 users.  

- **CISA-Highlighted Actors (Multiple)**  
  - **Campaign**: Active exploitation of four newly cataloged KEV vulnerabilities across federal and critical-infrastructure networks, specifics withheld by agency but confirmed in the wild.  

---

Security teams should prioritize patching **CVE-2025-5777**, update Chrome immediately, audit networks for vulnerable TBK / Four-Faith devices, revoke default credentials on all ICS assets, and monitor for malicious browser extensions in enterprise fleets.