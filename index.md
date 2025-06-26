# Exploitation Report

Over the past week, defenders have observed a sharp uptick in real-world exploitation of critical infrastructure bugs.  Attackers are actively abusing a remote-code-execution flaw in AMI’s MegaRAC BMC firmware to hijack and even “brick” data-center servers, while two separate vulnerabilities in Citrix NetScaler appliances are being weaponized for denial-of-service and full session hijacking.  CISA has also confirmed in-the-wild exploitation of high-impact flaws affecting D-Link DIR-859 routers and Fortinet FortiOS, prompting emergency inclusion in the Known Exploited Vulnerabilities (KEV) catalogue.  These server-grade and edge-network weaknesses are being leveraged alongside sophisticated spear-phishing operations from Iran-aligned APT35, demonstrating coordinated efforts to gain persistent access across both enterprise cores and perimeters.

## Active Exploitation Details

### AMI MegaRAC BMC Remote Code-Execution Vulnerability
- **Description**: A maximum-severity flaw in AMI’s MegaRAC Baseboard Management Controller (BMC) software that allows unauthenticated attackers to execute arbitrary code in the out-of-band management interface.  
- **Impact**: Full takeover of server hardware, firmware tampering, and the ability to “brick” servers by corrupting system firmware or wiping disks.  
- **Status**: Confirmed active exploitation; CISA has added the issue to its KEV catalogue.  Firmware updates and OEM patches are available and should be applied immediately.  

### Citrix NetScaler ADC/Gateway Denial-of-Service Vulnerability
- **Description**: A flaw in NetScaler ADC and Gateway that enables remote attackers to force appliances into a persistent DoS state.  
- **Impact**: Legitimate users are locked out, and dependent applications experience prolonged outages; exploitation can also open follow-on opportunities for intrusion once services restart.  
- **Status**: Actively exploited in the wild.  Citrix issued emergency fixes and urges upgrading to the latest builds.  
- **CVE ID**: CVE-2025-6543  

### “CitrixBleed 2” Session Hijacking Vulnerability
- **Description**: A newly disclosed weakness similar to 2023’s CitrixBleed that allows unauthenticated actors to extract valid authentication tokens from NetScaler ADC/Gateway memory.  
- **Impact**: Attackers can replay stolen session tokens to gain privileged VPN access without credentials, pivot inside networks, and harvest sensitive data.  
- **Status**: Evidence of exploitation observed; patches are available and should be deployed immediately.  

### D-Link DIR-859 Router Remote Code-Execution Vulnerability
- **Description**: A critical flaw in the DIR-859 firmware permitting remote code execution through crafted HTTP requests to the device’s web interface.  
- **Impact**: Complete router compromise, traffic inspection/manipulation, and establishment of a foothold inside home or small-office networks.  
- **Status**: Added to CISA KEV, indicating confirmed exploitation.  D-Link has released updated firmware; unsupported devices remain vulnerable.  

### Fortinet FortiOS Critical Vulnerability
- **Description**: A high-severity FortiOS flaw (pre-authentication) that lets remote attackers execute code or commands on affected firewalls.  
- **Impact**: Full device takeover, creation of persistent tunnels, and visibility into all north-south traffic traversing the firewall.  
- **Status**: Actively exploited per CISA KEV entry.  Fortinet has issued fixed versions and security advisories.  

## Affected Systems and Products

- **AMI MegaRAC BMC**: Server-class motherboards from multiple OEM vendors running vulnerable MegaRAC firmware builds  
- **Citrix NetScaler ADC & Gateway**: Versions 12.x, 13.0, and 14.1 prior to the emergency updates for CVE-2025-6543 and “CitrixBleed 2” patches  
- **D-Link DIR-859 Router**: All firmware revisions prior to the latest security release  
- **Fortinet FortiOS**: Multiple branches (6.x and 7.x) below vendor-specified fixed builds  
- **Enterprise Servers**: VMware, Dell, HPE, Lenovo, and other platforms shipping AMI MegaRAC-based BMCs  

## Attack Vectors and Techniques

- **Out-of-Band Management Abuse**  
  - **Vector**: Direct access to exposed BMC management interfaces over TCP/IP (typically ports 443, 623, or IPMI).  

- **Session Token Extraction (“CitrixBleed 2”)**  
  - **Vector**: Malformed requests to NetScaler appliance endpoints leak authentication tokens that can be replayed.  

- **Denial-of-Service Flood**  
  - **Vector**: Crafted network packets trigger resource-exhaustion in NetScaler appliances, forcing reboot loops.  

- **Router Web-Interface Exploit**  
  - **Vector**: HTTP GET/POST requests with malicious payloads achieve command execution on D-Link DIR-859 devices.  

- **Phishing and Social Engineering (APT35)**  
  - **Technique**: AI-generated spear-phishing emails targeting Israeli tech experts to deliver credential-harvesting links or malware.  

## Threat Actor Activities

- **Actor/Group**: APT35 (“Charming Kitten”)  
  - **Campaign**: AI-powered phishing against Israeli cybersecurity professionals and journalists to obtain credentials and intelligence.  

- **Actor/Group**: Unattributed actors abusing MegaRAC**  
  - **Campaign**: Mass-scanning and exploitation of exposed BMC interfaces, leading to server hijack, firmware wiping, and ransomware deployment.  

- **Actor/Group**: Multiple financially motivated groups**  
  - **Campaign**: Leveraging D-Link and Fortinet exploits for foothold in SOHO and enterprise environments, often preceding data-exfiltration or ransomware operations.  

- **Actor/Group**: OneClik Operators**  
  - **Campaign**: Combining Microsoft ClickOnce abuse with AWS infrastructure for stealthy malware delivery to energy-sector targets; often use compromised edge devices (Citrix/FortiGate) for C2 redirection.  

- **Actor/Group**: North Korean “Contagious Interview” Crew**  
  - **Campaign**: Malicious npm packages in fake job-interview scenarios; relies on compromised edge routers and firewalls for staging C2 infrastructure observed exploiting FortiOS.  

**Bold** emphasis identifies critical items; organizations should patch immediately, monitor for indicators of compromise, and restrict exposure of management interfaces to mitigate the outlined threats.