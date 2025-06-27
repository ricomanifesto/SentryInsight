# Exploitation Report

During the past week, defenders observed a significant surge in remote-code-execution activity against infrastructure devices and security appliances.  Three separate vulnerabilities are now confirmed as exploited in the wild: a maximum-severity flaw in AMI MegaRAC Baseboard Management Controllers (BMC) that lets intruders seize or brick entire servers; an unauthenticated bug in D-Link DIR-859 home/SMB routers that is being folded into botnets; and a high-impact Fortinet FortiOS vulnerability that adversaries are using for initial access to corporate networks.  These exploits highlight a continued trend of attackers favoring edge devices and out-of-band management interfaces where traditional endpoint security is absent.

## Active Exploitation Details

### AMI MegaRAC BMC Remote Code Execution  
- **Description**: A critical flaw in American Megatrends’ MegaRAC BMC firmware allows unauthenticated network access to the management interface, resulting in full remote code execution with BMC-level privileges.  
- **Impact**: Attackers can hijack, permanently brick, or stealth-monitor servers, bypassing the host operating system entirely.  
- **Status**: Confirmed active exploitation; CISA added the flaw to its Known Exploited Vulnerabilities (KEV) catalog. Firmware updates are available from affected OEM vendors but must be applied manually through out-of-band tools.

### D-Link DIR-859 Router Command Injection  
- **Description**: An input-validation error in the web-based management console of DIR-859 routers permits specially crafted HTTP requests that spawn a command shell with root privileges.  
- **Impact**: Remote attackers can fully take over routers, pivot into internal networks, or conscript devices into DDoS botnets.  
- **Status**: Actively exploited according to CISA KEV listing. D-Link has issued end-of-life notices for the model; no official patch is forthcoming, leaving mitigation to network segmentation or device replacement.

### Fortinet FortiOS / FortiProxy Heap Overflow  
- **Description**: A buffer-management flaw in the SSL-VPN component of FortiOS and FortiProxy allows a malformed packet sequence to overflow the heap and execute arbitrary code as root on affected appliances.  
- **Impact**: Successful exploitation grants full administrative control of the firewall/VPN, enabling lateral movement and data exfiltration across protected networks.  
- **Status**: Confirmed exploited in the wild; Fortinet released hotfix builds and strongly advises immediate upgrade or temporary disabling of the SSL-VPN service.

## Affected Systems and Products

- **AMI MegaRAC BMC-equipped Servers**: Multiple OEM server lines (Supermicro, Dell, HPE, Lenovo, ASUS, and others) running vulnerable MegaRAC firmware  
  - **Platform**: Out-of-band management controllers accessible over dedicated network interfaces  

- **D-Link DIR-859 Wireless AC1750 Routers** (all firmware revisions, product is end-of-life)  
  - **Platform**: SOHO hardware running D-Link’s embedded Linux-based firmware  

- **Fortinet FortiOS & FortiProxy**  
  - **Platform**: FortiGate NGFW appliances and FortiProxy web proxies with SSL-VPN exposed to the Internet  

## Attack Vectors and Techniques

- **Unauthenticated Management-Interface Access**  
  - **Vector**: Direct network access to BMC interfaces on port 623 (IPMI) or Redfish/HTTPS ports exploited to run code without credentials.  

- **Web-Admin Command Injection**  
  - **Vector**: Malicious HTTP/HTTPS requests sent to `/cgi-bin/` endpoints of DIR-859 routers trigger shell command execution.  

- **SSL-VPN Heap Overflow**  
  - **Vector**: Crafted SSL-VPN handshake packets delivered over the public Internet exploit heap mis-management in FortiOS/Proxy, leading to RCE.  

## Threat Actor Activities

- **Unknown Infrastructure-Focused Actors**  
  - **Campaign**: Leveraging the AMI MegaRAC flaw to implant persistent malware on data-center servers and, in some cases, to permanently disable systems (bricking). Target sectors include cloud providers and managed hosting firms.  

- **Botnet Operators**  
  - **Campaign**: Large-scale scanning for DIR-859 units, adding compromised routers to DDoS and proxy botnets used for anonymised malicious traffic.  

- **Multiple Intrusion Sets (State-sponsored and Cyber-criminal)**  
  - **Campaign**: Active exploitation of Fortinet appliances for initial foothold, followed by ransomware or espionage operations. Energy, manufacturing, and financial services are primary targets.  

- **APT35 (“Charming Kitten”)**  
  - **Campaign**: Parallel spear-phishing operations against Israeli technology experts using AI-generated lure content; while not tied to the above CVE-based exploits, the group increasingly chains VPN and edge-device vulnerabilities once inside a network.  

- **Scattered Spider**  
  - **Campaign**: Shifted focus from retail to U.S. insurance firms, abusing compromised VPN and IdP credentials to bypass MFA, often taking advantage of unpatched edge devices such as vulnerable Fortinet gear.  

Defense teams should prioritise patching of the highlighted device-level flaws, restrict exposure of management interfaces, and expand monitoring of outbound traffic from infrastructure components that traditionally fall outside the endpoint security stack.