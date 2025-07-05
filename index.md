# Exploitation Report

Over the last week, security researchers observed two high-impact zero-day exploit chains actively leveraged in the wild.  The NightEagle APT is weaponising an undisclosed Microsoft Exchange Server flaw to gain initial access to government and defence-adjacent networks, while a separate Chinese state-aligned cluster is abusing multiple zero-days in Ivanti Connect Secure Appliances (CSA) to infiltrate French government, telecom, media, finance and transport organisations.  Both attacks deliver web-shells for persistent remote code execution (RCE), enable credential harvesting, and pivot laterally into on-premises and cloud resources.  Rapid patching and robust monitoring of edge devices are therefore critical.

## Active Exploitation Details

### Microsoft Exchange Server Zero-Day RCE
- **Description**: A previously undocumented vulnerability in Microsoft Exchange that allows remote, unauthenticated attackers to execute arbitrary code on vulnerable servers by abusing the Outlook Web Access (OWA) endpoint.  
- **Impact**: Complete takeover of on-prem Exchange, deployment of web-shells, email exfiltration, lateral movement into adjacent Windows infrastructure.  
- **Status**: Being actively exploited by the NightEagle APT; Microsoft has not yet released public patches, making this a live zero-day.  

### Ivanti Connect Secure Appliance Zero-Days (Auth Bypass & Command Injection)
- **Description**: A chain of authentication-bypass and command-injection flaws in Ivanti CSA that lets remote attackers bypass login controls and execute system-level commands on the underlying OS.  
- **Impact**: Full VPN appliance compromise, credential theft, network reconnaissance, and installation of persistent backdoors.  
- **Status**: Actively exploited by a Chinese state-sponsored group against French critical sectors; mitigation guidance and emergency fixes are available from Ivanti pending a comprehensive firmware update.  

## Affected Systems and Products

- **Microsoft Exchange Server**: On-premises versions 2016 and 2019 (all cumulative updates)  
  - **Platform**: Windows Server deployments running Exchange in government, defence, manufacturing and technology environments  
- **Ivanti Connect Secure Appliance (CSA)**: All firmware builds prior to the out-of-band July 2025 hotfix  
  - **Platform**: Physical and virtual VPN gateways used across French governmental, telecom, media, finance and transport networks  

## Attack Vectors and Techniques

- **Web-Shell Deployment via OWA**  
  - **Vector**: Crafted HTTPS requests to OWA endpoint exploit the Exchange zero-day, writing ChinaChopper-style web-shells to the `/owa/auth` directory.  

- **Authentication Bypass on Ivanti CSA**  
  - **Vector**: Malicious REST API calls manipulate session tokens to bypass login, followed by command injection in appliance management scripts.  

- **Credential Dumping & Lateral Movement**  
  - **Vector**: Post-exploitation use of Mimikatz, WMI and remote PowerShell to harvest credentials and pivot inside Windows AD domains.  

- **Encrypted C2 Over TLS**  
  - **Vector**: Attackers tunnel commands through HTTPS ports 443/8443 to evade network inspection and blend with legitimate traffic.  

## Threat Actor Activities

- **NightEagle (APT-Q-95)**  
  - **Campaign**: Targeting China’s military and high-tech sectors since June 2025; drops memory-resident web-shells, deploys custom backdoor “SkyWing,” and exfiltrates mailbox data.  

- **Unattributed Chinese State-Aligned Group**  
  - **Campaign**: Multi-sector intrusion wave across France leveraging Ivanti CSA zero-days; establishes persistence via modified `/data/runtime/tmp` scripts and siphons VPN credentials to access internal networks.