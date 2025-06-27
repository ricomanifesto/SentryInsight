# Exploitation Report

The past week revealed a sharp rise in real-world exploitation of infrastructure-level vulnerabilities, led by active attacks on AMI’s MegaRAC BMC firmware that enable full server takeover, and newly confirmed weaponization of flaws in Fortinet FortiOS and D-Link consumer routers now added to CISA’s Known Exploited Vulnerabilities (KEV) catalog. Simultaneously, critical unauthenticated RCE bugs in Cisco Identity Services Engine were patched, while large-scale social-engineering campaigns such as “OneClik” and Microsoft 365 “Direct Send” abuse demonstrate attackers’ continued pivot toward living-off-the-land techniques. Nation-state actors—most notably Iran’s APT35/Charming Kitten—leveraged AI-powered spear-phishing, and financially motivated groups like Scattered Spider shifted targeting to U.S. insurance firms. Taken together, these developments underscore an urgent need for rapid patching of exposed infrastructure components, continuous monitoring for credential-abuse vectors, and reinforced user-centric defenses.

## Active Exploitation Details

### AMI MegaRAC BMC Firmware Remote Code Execution  
- **Description**: A maximum-severity vulnerability in American Megatrends’ MegaRAC Baseboard Management Controller allows unauthenticated attackers to execute arbitrary code on the BMC via crafted network requests, leading to complete control of underlying servers.  
- **Impact**: Full server hijack, device bricking, deployment of persistent implants, lateral movement across data-center networks.  
- **Status**: Confirmed active exploitation; CISA issued an alert and added the flaw to the KEV catalog. Patches are available from server OEMs but adoption remains uneven.  
- **CVE ID**: CVE-2023-34329  

### D-Link DIR-859 Router Command Injection  
- **Description**: A remote command-injection flaw in the DIR-859 AC1750 router’s management interface permits execution of system commands without authentication.  
- **Impact**: Remote takeover of consumer or small-office routers, DNS manipulation, and foothold for residential proxy networks.  
- **Status**: Actively exploited in the wild; listed by CISA in KEV. Firmware updates are released, though many devices are end-of-life and remain unpatched.  

### Fortinet FortiOS SSL-VPN Heap Buffer Overflow  
- **Description**: Vulnerability in the SSL-VPN component of FortiOS that allows a specially crafted request to trigger a heap overflow and attain code execution with root privileges.  
- **Impact**: Network perimeter breach, credential theft, deployment of ransomware, and broader compromise of OT/IT environments.  
- **Status**: Under active exploitation per CISA KEV. Patches released; Fortinet urges immediate upgrade or VPN disablement.  

### Cisco Identity Services Engine (ISE) and ISE-PIC Unauthenticated RCE  
- **Description**: Two unrelated but similar flaws in the web-based administrative interface of Cisco ISE and Passive Identity Connector permit unauthenticated attackers to upload arbitrary files and gain root shell access.  
- **Impact**: Complete compromise of NAC infrastructure, manipulation of identity policies, and potential credential harvesting across enterprise AD/LDAP sources.  
- **Status**: No confirmed exploitation yet, but proof-of-concept code is publicly circulating. Fixed versions are available; Cisco rates both as maximum-severity.  

### Open VSX Registry Namespace Takeover  
- **Description**: A misconfiguration in the Open VSX package registry allowed attackers to overwrite any extension, leading to supply-chain compromise of Visual Studio Code extensions.  
- **Impact**: Mass downstream infection of developer workstations, CI/CD pipelines, and potential insertion of malicious code into production apps.  
- **Status**: Vulnerability disclosed and patched; researchers demonstrated exploitability but no public evidence of mass exploitation at time of report.  

### Brother / Fujifilm / Toshiba / Konica Minolta Default Admin Password Exposure  
- **Description**: 689 Brother printer models (plus 53 from other vendors) ship with predictable administrator passwords that can be regenerated remotely via a published algorithm.  
- **Impact**: Unauthorized configuration changes, proxying of malicious traffic, exfiltration of scanned documents.  
- **Status**: In the wild exploitation detected on internet-exposed devices. Vendor guidance recommends disabling remote management and changing credentials immediately.

## Affected Systems and Products

- **AMI MegaRAC BMC Firmware**: Multiple OEM server lines (Supermicro, Dell, HPE, Lenovo) across on-prem and cloud data centers  
- **D-Link DIR-859 Router**: All firmware versions prior to latest hotfix; home and SMB deployments  
- **Fortinet FortiOS**: FortiGate firewalls running vulnerable SSL-VPN builds (commonly 7.2.x and 7.0.x before patched releases)  
- **Cisco Identity Services Engine / ISE-PIC**: ISE ≤ 3.1 patch 7 and 3.2 patch 3; Passive Identity Connector ≤ 3.1  
- **Open VSX Registry (open-vsx.org)**: Public registry service and self-hosted mirrors used by Eclipse Theia and VS Code forks  
- **Brother, Fujifilm, Toshiba, Konica Minolta Printers**: Specific model list covering laser, inkjet, and multifunction devices shipped since 2015  
- **Microsoft 365 Tenants**: Organizations allowing “Direct Send” relay from printer/scanner IP ranges  
- **Energy-Sector Enterprises**: Victims of “OneClik” ClickOnce attacks on Windows endpoints  
- **Windows Endpoints Running ConnectWise ScreenConnect**: Targets of Authenticode-stuffed installers

## Attack Vectors and Techniques

- **Unauthenticated BMC HTTP/Redfish Access**  
  - **Vector**: Direct network exposure of port / firmware API enabling code injection in MegaRAC.  

- **HNAP/UPnP Command Injection**  
  - **Vector**: Malformed SOAP actions sent to D-Link router management endpoint.  

- **SSL-VPN Heap Overflow Exploit**  
  - **Vector**: Crafted HTTPS requests to FortiGate SSL-VPN portal.  

- **Arbitrary File Upload to Cisco ISE**  
  - **Vector**: Abuse of web UI endpoints to drop malicious TAR/zip bundles, triggering root shell.  

- **Namespace Takeover / Typosquatting**  
  - **Vector**: Claiming or replacing package names in Open VSX, propagating malicious extensions.  

- **Predictable Default Credentials**  
  - **Vector**: Algorithmically generating admin passwords for printer web consoles.  

- **Microsoft 365 “Direct Send” Abuse**  
  - **Vector**: SMTP relay via Exchange Online’s Direct Send feature to deliver internal-looking phishing emails.  

- **Authenticode Stuffing of ScreenConnect Installer**  
  - **Vector**: Injecting malicious payload into installer while retaining a valid signature section.  

- **ClickOnce + AWS S3 (“OneClik”)**  
  - **Vector**: Phishing link drops ClickOnce application referencing payloads hosted on attacker-controlled S3 buckets.  

- **ClickFix / FileFix CAPTCHA Lure**  
  - **Vector**: Fake CAPTCHA gates prompting users to sideload malicious browser extensions or documents.  

- **AI-Assisted Spear-Phishing**  
  - **Vector**: Generative-AI-crafted emails mimicking trusted contacts to deliver malicious links or collect Google Workspace tokens.

## Threat Actor Activities

- **IntelBroker**  
  - **Campaign**: Large-scale data-theft breaches against government agencies and corporations; actor arrested but data re-sale persists on dark markets.  

- **Scattered Spider (Octo Tempest/UNC3944)**  
  - **Campaign**: Shifted from retail to U.S. insurance verticals; techniques include SIM swapping, Okta session hijacking, and ransomware-as-extortion.  

- **APT35 / Charming Kitten (Iran)**  
  - **Campaign**: AI-enhanced spear-phishing targeting Israeli tech and cybersecurity experts; delivers custom backdoors via cloud-hosted lure documents.  

- **OneClik Operators**  
  - **Campaign**: Targeting energy-sector organizations with ClickOnce-delivered Golang backdoors and AWS infrastructure for C2.  

- **ScreenConnect Abusers (Unnamed financially motivated group)**  
  - **Campaign**: Transforming legitimately signed remote-support tools into malware for stealthy, persistent access to enterprise networks.  

- **ClickFix/FileFix Social-Engineering Syndicate**  
  - **Campaign**: 517% surge in CAPTCHA-lure attacks across Q4 2024–Q1 2025, aimed at initial access for info-stealing malware loaders.  

- **Unknown Actors Exploiting AMI MegaRAC & Fortinet FortiOS**  
  - **Campaign**: Opportunistic scanning and mass exploitation of internet-facing management interfaces and VPN appliances to establish footholds in data centers and corporate networks.

