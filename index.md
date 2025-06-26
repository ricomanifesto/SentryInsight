# Exploitation Report

A surge of exploitation activity is centering on Citrix NetScaler appliances, where two separate flaws are being weaponized for denial-of-service and session-hijacking attacks. Meanwhile, threat actors are innovating around software-supply-chain abuse, repurposing trusted installers (ScreenConnect, SonicWall NetExtender) and cloud delivery mechanisms (Microsoft ClickOnce, AWS) to deliver backdoors and steal credentials. North Korea-linked operators continue to seed malicious npm packages, and multiple ransomware and hacktivist groups are capitalizing on these vectors to expand their reach.

## Active Exploitation Details

### NetScaler ADC/Gateway DoS Vulnerability
- **Description**: A flaw in NetScaler ADC and Gateway allows remote, unauthenticated attackers to send crafted requests that place the appliance into a denial-of-service state.  
- **Impact**: Exhausts system resources, knocking out VPN and application-delivery functions and potentially forcing emergency fail-over.  
- **Status**: Actively exploited in the wild; Citrix has released emergency patches and mitigation guidance.  
- **CVE ID**: CVE-2025-6543  

### “CitrixBleed 2” Session-Hijacking Vulnerability
- **Description**: A newly disclosed flaw reminiscent of the original CitrixBleed enables theft of authentication tokens from memory, letting attackers hijack active user sessions on NetScaler ADC/Gateway.  
- **Impact**: Full session takeover, lateral movement inside corporate networks, data exfiltration, and potential privilege escalation.  
- **Status**: Exploitation observed; Citrix has issued fixes and urges immediate upgrade.  

### ScreenConnect Authenticode-Stuffing Abuse
- **Description**: Attackers modify hidden fields inside the ConnectWise ScreenConnect installer’s Authenticode signature, embedding malicious payloads while preserving the file’s valid digital signature.  
- **Impact**: Creation of fully signed remote-access malware that easily evades trust-based controls and endpoint defenses.  
- **Status**: Being used in active campaigns; no vendor patch is applicable because the abuse targets the signing process rather than a code flaw.  

### OneClik (Microsoft ClickOnce & AWS) Supply-Chain Attack
- **Description**: A multi-stage intrusion chain abuses Microsoft’s ClickOnce deployment technology to sideload custom Golang backdoors hosted on AWS infrastructure.  
- **Impact**: Stealthy remote code execution, persistent access, and data theft in targeted energy-sector organizations.  
- **Status**: Ongoing campaign observed in the wild; defenders must harden ClickOnce configurations and monitor outbound AWS traffic.  

### Trojanized SonicWall NetExtender Installer
- **Description**: A counterfeit version of the SonicWall NetExtender VPN client carries an infostealer that harvests credentials when users attempt legitimate log-ins.  
- **Impact**: Compromise of corporate VPN credentials, enabling subsequent unauthorized network access.  
- **Status**: Active distribution on look-alike websites and phishing lures; SonicWall advises checksum validation of installers.  

### Contagious Interview npm Package Implant
- **Description**: North Korea-linked operators publish malicious npm packages that masquerade as developer tools, planting backdoors during “fake job interview” lures.  
- **Impact**: Theft of source code, multi-platform persistence, and potential pivot into victim organizations’ CI/CD pipelines.  
- **Status**: Fresh wave of 35 malicious packages detected and removed, but ongoing uploads continue.  

## Affected Systems and Products

- **Citrix NetScaler ADC & Gateway**: All unsupported builds and supported versions prior to emergency patches for CVE-2025-6543 and “CitrixBleed 2”  
- **ConnectWise ScreenConnect**: Official Windows installer, when tampered with via Authenticode stuffing  
- **Microsoft ClickOnce Deployed Apps**: Any ClickOnce package fetched over HTTP(S) that points to attacker-controlled AWS S3 or CloudFront buckets  
- **SonicWall NetExtender**: Windows client installers obtained from unofficial sources  
- **npm Ecosystem**: Developers installing the 35 newly identified malicious packages tied to the Contagious Interview campaign  

## Attack Vectors and Techniques

- **Authenticode Stuffing**  
  - **Vector**: Injecting malicious DLLs into the signed section of ScreenConnect MSI packages, leaving the signature intact.  

- **ClickOnce Cloud Sideloading**  
  - **Vector**: Users launch a ClickOnce URL that silently downloads a malicious payload from attacker-controlled AWS infrastructure.  

- **Malicious Package Typosquatting**  
  - **Vector**: Publishing libraries with names visually similar to popular npm packages to poison the software-supply chain.  

- **Session Token Memory Scraping**  
  - **Vector**: Exploiting “CitrixBleed 2” to read sensitive memory regions and steal live authentication tokens.  

- **DoS Flood via Crafted Requests**  
  - **Vector**: Sending malformed HTTP(S) traffic to NetScaler endpoints, triggering CVE-2025-6543 and exhausting resources.  

- **Trojanized Installer Replacement**  
  - **Vector**: Hosting look-alike SonicWall installer download pages to trick users into replacing genuine VPN clients with credential-stealing versions.  

## Threat Actor Activities

- **IntelBroker**  
  - **Campaign**: Wide-ranging data-theft operations against multiple organizations, leveraging stolen credentials and underground-forum sales.  

- **Unknown ScreenConnect Abusers**  
  - **Campaign**: Weaponizing Authenticode stuffing to deliver stealth RATs under the guise of legitimate remote-support tools.  

- **OneClik Operators**  
  - **Campaign**: Targeting the energy sector with ClickOnce-delivered Golang backdoors, achieving long-term persistence and data exfiltration.  

- **North Korea-Linked “Contagious Interview” Group**  
  - **Campaign**: Continues to plant malicious npm packages and lure developers with fake job interviews, aiming for supply-chain infiltration.  

- **Dire Wolf Ransomware**  
  - **Campaign**: Double-extortion attacks against technology and manufacturing firms across 11 countries; leverages stolen credentials, possibly obtained from campaigns above.  

- **Cyber Fattah (Pro-Iranian Hacktivists)**  
  - **Campaign**: Data-leak operations, including the dump of Saudi Games records, using opportunistic exploitation and credential reuse.  

- **Citrix Exploitation Clusters (Multiple Unnamed Actors)**  
  - **Campaign**: Exploiting CVE-2025-6543 and “CitrixBleed 2” to disrupt services and hijack sessions, observable in both criminal and state-aligned intrusion sets.  

---

Defenders should prioritize patching NetScaler appliances, verify digital signatures against tampering, restrict ClickOnce deployments, and monitor developer environments for malicious npm package imports.