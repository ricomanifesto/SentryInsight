# Exploitation Report

Recent reporting underscores a surge in critical infrastructure-level exploitation, with attackers zeroing in on management interfaces and edge appliances that provide deep footholds inside enterprise networks.  The most pressing activity involves a maximum-severity flaw in AMI’s MegaRAC BMC firmware that is already being weaponized to hijack and permanently brick servers, together with an actively exploited denial-of-service vulnerability (CVE-2025-6543) in Citrix NetScaler ADC/Gateway appliances.  CISA has added related MegaRAC, D-Link DIR-859, and Fortinet FortiOS issues to its Known Exploited Vulnerabilities (KEV) catalog, confirming in-the-wild abuse.  Concurrently, new “CitrixBleed 2” session-hijacking research, sophisticated supply-chain tactics (malicious npm packages and ClickOnce abuse), and ransomware operations such as Dire Wolf illustrate how adversaries are chaining these weaknesses with stealthy delivery techniques to maximize impact.

## Active Exploitation Details

### AMI MegaRAC BMC Maximum-Severity Vulnerability
- **Description**: A critical flaw in AMI’s MegaRAC Baseboard Management Controller firmware allows unauthenticated remote attackers to gain full control over out-of-band server management, enabling malicious firmware uploads or destructive commands.  
- **Impact**: Complete server takeover or permanent “bricking,” leading to widespread infrastructure outages.  
- **Status**: Confirmed active exploitation; CISA added the issue to the KEV catalog.  Firmware patches are available from server OEMs and should be applied immediately.  

### Citrix NetScaler ADC/Gateway DoS Vulnerability
- **Description**: Resource-exhaustion flaw in NetScaler ADC and Gateway lets a remote attacker send crafted packets that push the appliance into a crash/denial-of-service state.  
- **Impact**: Disruption of all load-balancing and VPN services, potentially forcing companies offline.  
- **Status**: Citrix has released emergency fixes and warns the bug is being exploited in the wild.  
- **CVE ID**: CVE-2025-6543  

### D-Link DIR-859 Router Remote Code-Execution Vulnerability
- **Description**: An unauthenticated RCE bug in the DIR-859 router’s web interface allows attackers to run arbitrary commands with root privileges.  
- **Impact**: Full takeover of home or small-office networks, enabling traffic interception or pivoting into corporate environments used by remote workers.  
- **Status**: Listed by CISA as actively exploited; model is officially end-of-life with no vendor patch, leaving mitigation to network segmentation or device replacement.  

### Fortinet FortiOS SSL-VPN Vulnerability
- **Description**: A flaw in FortiOS SSL-VPN permits an unauthenticated attacker to execute code or commands on the firewall, often via specially crafted HTTP requests.  
- **Impact**: Direct firewall compromise, credential theft, and lateral movement into protected networks.  
- **Status**: Added to CISA KEV catalog; Fortinet has provided updates and work-arounds.  

### CitrixBleed 2 Session-Hijacking Vulnerability
- **Description**: Newly disclosed weakness in NetScaler ADC/Gateway that leaks session tokens, echoing 2023’s CitrixBleed but affecting a different code path.  
- **Impact**: Allows attackers to hijack authenticated sessions without credentials, enabling stealthy access to internal applications.  
- **Status**: Researchers observed exploitation attempts; defenders should apply the latest firmware and revoke active sessions.  

## Affected Systems and Products

- **AMI MegaRAC BMC (multiple server OEMs)**  
  - **Platform**: Data-center and on-prem servers using MegaRAC firmware versions prior to vendor-specific fixes  

- **Citrix NetScaler ADC & Gateway**  
  - **Platform**: All supported hardware, VPX, and SDX appliances prior to 14.2-9.56 / 13.1-51.17 / 13.0-92.24 hotfixes  

- **D-Link DIR-859 Wireless AC 1750 Router**  
  - **Platform**: Home/SOHO router firmware latest build (end-of-life, no patches)  

- **Fortinet FortiOS**  
  - **Platform**: FortiGate firewalls running vulnerable FortiOS branches pre-hotfix (versions vary by model)  

## Attack Vectors and Techniques

- **Out-Of-Band Management Abuse**  
  - **Vector**: Remote access to BMC management port on TCP 623/664/5900; malicious Redfish or IPMI requests hijack MegaRAC.  

- **Edge-Appliance DoS**  
  - **Vector**: Crafted HTTP/SSL requests aimed at NetScaler Gateway trigger resource exhaustion, forcing reboot loops.  

- **Session Token Leakage (CitrixBleed 2)**  
  - **Vector**: Exploits improper memory handling to read sensitive session data over TLS, allowing replay without MFA.  

- **Router RCE via Web UI**  
  - **Vector**: Unauthenticated POST requests inject system commands in DIR-859 CGI scripts.  

- **SSL-VPN Command Injection**  
  - **Vector**: Manipulated parameters in FortiOS login requests execute shell commands on the firewall.  

## Threat Actor Activities

- **APT35 / Charming Kitten (Iran)**  
  - **Campaign**: AI-powered spear-phishing against Israeli cybersecurity experts; leverages compromised infrastructure for C2, potentially using NetScaler exploits for persistence.  

- **Unknown Financial Threat Group (Africa)**  
  - **Campaign**: Combines open-source red-team tools with FortiOS and router exploits to breach banks across multiple African nations.  

- **OneClik Campaign**  
  - **Actor/Group**: Undisclosed sophisticated operators targeting the energy sector.  
  - **Activities**: Abuse of Microsoft ClickOnce and AWS S3 presigned URLs to deliver Golang backdoors, often following exploitation of edge devices for initial access.  

- **North Korean “Contagious Interview” Operators**  
  - **Campaign**: Spreads malicious npm packages during fake job interviews, then pivots via VPN and router vulnerabilities to corporate networks.  

- **Dire Wolf Ransomware Group**  
  - **Campaign**: Double-extortion attacks against manufacturing and technology firms; observed using stolen VPN credentials (possible FortiOS exploit) for ingress.  

- **ScreenConnect Abuse Actors**  
  - **Campaign**: Weaponize modified ConnectWise ScreenConnect installers with Authenticode stuffing to maintain signed malware, often deployed post-exploitation of BMCs or VPN devices.  

By prioritizing patches on MegaRAC BMCs, Citrix NetScaler appliances (especially CVE-2025-6543), Fortinet firewalls, and vulnerable D-Link routers—and by revoking / re-issuing session tokens—defenders can blunt the most urgent exploitation waves now coursing through enterprise environments.