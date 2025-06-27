# Exploitation Report

During this reporting period, the most critical exploitation activity involves remote code-execution flaws in widely deployed infrastructure components. A maximum-severity vulnerability in AMI’s MegaRAC Baseboard Management Controller (BMC) firmware is being weaponized to hijack and permanently disable servers, while separate in-the-wild attacks are leveraging unpatched flaws in D-Link DIR-859 routers and Fortinet FortiOS. These issues provide unauthenticated attackers with root-level access, drive-by implants, or complete denial-of-service capabilities, placing data-center hardware, branch networks, and VPN gateways at immediate risk. The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has added all three vulnerabilities to its Known Exploited Vulnerabilities (KEV) catalog, underscoring their active exploitation and urging accelerated patching.

## Active Exploitation Details

### AMI MegaRAC BMC Remote Code Execution
- **Description**: A maximum-severity flaw in AMI’s MegaRAC BMC firmware allows remote, unauthenticated attackers to execute arbitrary code as the BMC super-user over the management interface. Successful exploitation grants full server control, enabling firmware overwrites or “bricking” of hardware.
- **Impact**: Complete takeover of server out-of-band management, potential permanent denial of service, credential theft, lateral movement into production networks.
- **Status**: Confirmed active exploitation; CISA placed the bug in the KEV catalog. Firmware updates have been released by impacted OEMs, but patch adoption remains low.
  
### D-Link DIR-859 Router Command Injection
- **Description**: A command-injection vulnerability in the DIR-859 wireless router’s web interface lets remote attackers run shell commands with elevated privileges through crafted HTTP requests.
- **Impact**: Remote code execution, network pivoting, installation of botnet malware, and interception of traffic.
- **Status**: Added to CISA’s KEV list due to observed exploitation in the wild. D-Link no longer provides security updates for this end-of-life model, leaving many devices unpatched.

### Fortinet FortiOS SSL-VPN Heap Overflow
- **Description**: A heap-based buffer-overflow flaw in FortiOS SSL-VPN portals can be triggered by specially crafted requests, leading to arbitrary code execution or device crash.
- **Impact**: Full compromise of FortiGate firewalls, unauthorized access to internal networks, data exfiltration, or denial of service.
- **Status**: Exploitation detected and tracked by CISA. Fortinet has issued patched firmware; organizations are urged to upgrade immediately.

## Affected Systems and Products

- **AMI MegaRAC BMC firmware**  
  - **Platform**: Server motherboards and blade systems across major OEMs (Dell EMC iDRAC, HPE iLO variants, Lenovo XClarity, etc.) running vulnerable MegaRAC versions.

- **D-Link DIR-859 Wireless AC1750 Router**  
  - **Platform**: SOHO/SMB networking equipment, firmware still in circulation despite end-of-life status.

- **Fortinet FortiGate appliances running FortiOS (SSL-VPN enabled)**  
  - **Platform**: Enterprise firewalls and secure SD-WAN devices; vulnerable across multiple FortiOS 7.x and 6.x branches prior to vendor-supplied hotfixes.

## Attack Vectors and Techniques

- **Out-of-Band Management Exploitation**  
  - **Vector**: Direct access to BMC management ports (e.g., Redfish/IPMI over TCP 623 or 443) to deliver malicious payloads exploiting the MegaRAC bug.

- **HTTP Command Injection**  
  - **Vector**: Crafted GET/POST requests to `/command.php` and similar endpoints on DIR-859 web UI, embedding shell metacharacters to gain root access.

- **Malicious SSL-VPN Requests**  
  - **Vector**: Specially crafted packets to FortiOS SSL-VPN portal triggering heap overflow before authentication.

- **Authenticode Stuffing on ScreenConnect Installers**  
  - **Vector**: Tampering with installer’s digital-signature padding to embed malicious payloads while maintaining a valid signature, enabling stealthy remote-access malware delivery.

- **ClickFix/ FileFix Social Engineering**  
  - **Vector**: Fake CAPTCHA “ClickFix” pages convincing users to download trojanized documents that sideload backdoors.

- **Microsoft 365 “Direct Send” Phishing**  
  - **Vector**: Abuse of the SMTP “Direct Send” feature to push credential-harvesting emails appearing as internal traffic, bypassing filtering.

## Threat Actor Activities

- **IntelBroker**  
  - **Campaign**: Widespread data-theft operations targeting multinational corporations and government entities; sales of stolen data on dark-web forums resulted in estimated $25 million in damages.

- **Scattered Spider (a.k.a. UNC3944/Octo Tempest)**  
  - **Campaign**: Shifted focus from retail to U.S. insurance firms, employing SIM-swapping, OctoBot social engineering, and help-desk MFA bypass to breach cloud and on-prem networks.

- **APT35 / Charming Kitten (Iran)**  
  - **Campaign**: AI-powered spear-phishing against Israeli tech and cybersecurity experts, using fabricated job offers and malicious OneDrive links to deploy bespoke malware.

- **Unknown Threat Actors Exploiting MegaRAC**  
  - **Activities**: Targeting data-center and cloud-service providers’ BMC interfaces to gain persistent access and, in some cases, render hardware inoperable.

- **Financial-Sector Intrusions in Africa**  
  - **Actor/Group**: Unnamed criminal syndicate leveraging open-source tools (Sliver, Mythic, Cobalt Strike) to exfiltrate SWIFT credentials and customer data since July 2023.

- **OneClik Campaign Operators**  
  - **Activities**: Compromising energy-sector organizations via Microsoft ClickOnce and AWS S3-hosted stagers, followed by deployment of custom Golang backdoors.

- **Former WSU Student (Individual Actor)**  
  - **Campaign**: Local privilege abuse within university systems to obtain discounted parking and exfiltrate personal data of students and staff.

- **Freelance “Pen-Tester” Turned Hacker**  
  - **Activities**: Gained unauthorized access to multiple corporate networks to advertise paid “security services,” leading to federal charges.

## End of Report