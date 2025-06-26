# Exploitation Report

Over the past week, security researchers and vendors have confirmed highly-targeted exploitation of multiple enterprise-grade remote-access products, with Citrix NetScaler appliances and ConnectWise ScreenConnect endpoints drawing the heaviest fire.  The newly disclosed CVE-2025-6543 denial-of-service flaw is already being weaponized to knock NetScaler gateways offline, while a separate “CitrixBleed 2” session-hijacking bug is enabling theft of authenticated tokens.  Simultaneously, threat actors are chaining the February 2024 ScreenConnect authentication-bypass/RCE flaws with trojanized installers to obtain persistent remote footholds.  These exploits are surfacing in espionage, hack-tivist and financially motivated campaigns, highlighting the continued attacker focus on edge devices and software-distribution supply chains.

## Active Exploitation Details

### Citrix NetScaler ADC/Gateway DoS Vulnerability
- **Description**: A flaw in the HTTP/3 request-handling logic of NetScaler ADC and Gateway causes memory exhaustion that forces the appliance into an unrecoverable reboot loop.  
- **Impact**: Unauthenticated attackers can remotely crash impacted gateways, triggering denial of service that blocks all VPN and application delivery traffic.  
- **Status**: Confirmed in-the-wild exploitation; Citrix released emergency patches and urges immediate upgrade or traffic-filtering mitigations.  
- **CVE ID**: CVE-2025-6543  

### “CitrixBleed 2” Session-Hijacking Vulnerability  
- **Description**: A newly discovered information-disclosure flaw allows leakage of session tokens stored in appliance memory, echoing the 2023 “CitrixBleed” weakness.  
- **Impact**: Attackers can replay stolen cookies to hijack authenticated sessions and pivot into internal networks without valid credentials.  
- **Status**: Observed weaponised in limited attacks; fixes are available in the latest NetScaler firmware releases.  

### ConnectWise ScreenConnect Authentication-Bypass / RCE Chain  
- **Description**: A pair of issues—an authentication bypass that creates arbitrary users with admin privileges and a path-traversal leading to remote code execution—enable full takeover of on-prem ScreenConnect servers.  
- **Impact**: Complete compromise of remote-support infrastructure, lateral movement, malware deployment and data theft.  
- **Status**: Actively exploited both via direct attacks on unpatched servers and through trojanized ScreenConnect installers signed with “Authenticode stuffing.”  
- **CVE ID**: CVE-2024-1709 (auth bypass & RCE)  
- **CVE ID**: CVE-2024-1708 (path traversal)  

### WinRAR Directory-Traversal Execution Vulnerability  
- **Description**: Crafted archive paths escape the intended extraction directory, enabling dropped files to launch automatically on user log-on through Windows shortcut abuse.  
- **Impact**: Allows malware authors to achieve code execution immediately after extraction, bypassing many user-interface security prompts.  
- **Status**: Patched by RARLAB; malware samples abusing the flaw have been observed in the wild.  
- **CVE ID**: CVE-2025-6218  

## Affected Systems and Products

- **Citrix NetScaler ADC/Gateway**: Versions 13.1, 13.0, 12.1 and earlier builds prior to the June 2025 hotfixes  
- **ConnectWise ScreenConnect**: Self-hosted builds before 23.9.8; compromised “signed” installers circulated via phishing sites  
- **RARLAB WinRAR**: Windows editions prior to 7.11  
- **Brother Printers / MFC / Label printers**: Hundreds of models shipped 2010–2024 vulnerable to default-password generation flaw (unpatchable)  
- **SAP GUI for Windows & Java**: Versions prior to June 2025 cumulative update contain input-history data-exfiltration bugs  
- **Microsoft Entra ID SaaS Applications**: 9 % of third-party apps still mis-configured against the nOAuth token-validation weakness  
- **SonicWall NetExtender**: Trojanized installers impersonating legitimate VPN client  
- **AWS & Microsoft ClickOnce-served Apps**: Targets in the energy sector running OneClik-delivered payloads  
- **npm Ecosystem**: Developers pulling 35 malicious packages in the “Contagious Interview” campaign  

## Attack Vectors and Techniques

- **Denial-of-Service Flood**: Exploit of CVE-2025-6543 with crafted HTTP/3 packets to exhaust NetScaler resources  
- **Session Token Theft**: Memory scraping of NetScaler appliances to replay authentication cookies (“CitrixBleed 2”)  
- **Authenticode Stuffing**: Injecting malicious binaries into ScreenConnect MSI’s signature table to bypass SmartScreen  
- **Auth Bypass & RCE**: Direct exploitation of CVE-2024-1709/1708 on exposed ScreenConnect servers  
- **Directory Traversal in Archives**: Malicious WinRAR files place LNKs in Startup folders (CVE-2025-6218)  
- **ClickOnce Abuse**: Weaponised .application manifests sideloading Golang backdoors hosted on AWS S3  
- **Spear-Phishing**: Charming Kitten emails with lure documents targeting Israeli cyber professionals  
- **Malicious npm Packages**: Post-install scripts dropping Infostealers during fake job-interview process  
- **Default-Credential Generation**: Exploitation of Brother firmware flaw to derive admin passwords from device serial numbers  

## Threat Actor Activities

- **Charming Kitten (Iran)**  
  • Conducting spear-phishing against Israeli cybersecurity experts to deploy backdoors and gather intelligence.  

- **Unknown Crimeware Group (ScreenConnect/NetExtender)**  
  • Distributing trojanized SonicWall VPN clients and leveraging unpatched ScreenConnect RCEs for persistence.  

- **OneClik Campaign Operators**  
  • Targeting energy-sector firms with ClickOnce-based loaders and AWS-hosted payload infrastructure.  

- **North Korean “Contagious Interview” Operators**  
  • Spreading 35 malicious npm packages that install infostealers on developers’ machines.  

- **Cyber Fattah (Pro-Iranian Hacktivists)**  
  • Leaked thousands of personal records from the 2024 Saudi Games, likely obtained via opportunistic web-application compromise.  

- **Dire Wolf Ransomware Group**  
  • Double-extortion attacks against technology and manufacturing firms in 11 countries since May.  

- **IntelBroker (Individual Actor)**  
  • Charged for the sale of stolen data ($25 M damages) sourced through multiple breaches and dark-web operations.  

- **Unknown Actors Exploiting NetScaler DoS**  
  • Automating mass scans to crash exposed ADC/Gateway instances worldwide within hours of PoC release.  

---

Security teams are advised to prioritize patching of NetScaler appliances, ScreenConnect deployments and WinRAR installations, while closely monitoring for malicious ClickOnce manifests, npm package anomalies and trojanized remote-access software.