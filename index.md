# Exploitation Report  

A surge of high-impact vulnerabilities is driving active exploitation across infrastructure, developer ecosystems, and endpoint devices. The most critical activity centers on a maximum-severity flaw in AMI MegaRAC BMC firmware that CISA confirms is being used to hijack and even brick servers. Critical, unauthenticated remote-code-execution bugs in Cisco Identity Services Engine (ISE) raise parallel concerns for network access control environments, while an unpatchable Brother printer weakness exposes hundreds of models to remote takeover via predictably generated admin passwords. Meanwhile, a supply-chain flaw in the Open VSX registry threatens millions of developers, and multiple campaigns—ranging from Microsoft 365 “Direct Send” abuse to ScreenConnect Authenticode stuffing—illustrate how attackers pair new tactics with exploitable bugs to bypass defenses.

---

## Active Exploitation Details  

### AMI MegaRAC BMC Remote Hijack Vulnerability  
- **Description**: A maximum-severity flaw in the MegaRAC Baseboard Management Controller firmware allows remote, unauthenticated access, enabling full takeover of server management functions.  
- **Impact**: Attackers can power-cycle or brick servers, deploy persistent implants at the firmware layer, steal credentials, and move laterally inside data-center networks.  
- **Status**: CISA added the bug to its Known Exploited Vulnerabilities (KEV) catalog and reports in-the-wild exploitation; vendors are releasing firmware updates, but many servers remain unpatched.  

### Cisco ISE / ISE-PIC Unauthenticated RCE Flaws  
- **Description**: Two critical vulnerabilities in Cisco Identity Services Engine and Passive Identity Connector allow unauthenticated remote code execution with root privileges via crafted HTTP requests.  
- **Impact**: Complete compromise of the NAC platform, letting attackers manipulate authentication policies, harvest credentials, and pivot deeper into enterprise networks.  
- **Status**: Actively weaponized proof-of-concept code is circulating; Cisco has issued patches and recommends immediate upgrades.  

### Brother Printer Default-Password Generation Weakness  
- **Description**: 689 Brother printers (plus dozens from Fujifilm, Toshiba, Konica Minolta) ship with admin passwords that can be derived remotely from publicly exposed device details.  
- **Impact**: Remote attackers can obtain administrator access, change firmware, install malicious payloads, reroute print jobs, or pivot onto corporate LANs.  
- **Status**: No firmware fix is available; Brother advises network isolation and password changes where possible.  

### Open VSX Registry Critical Takeover Vulnerability  
- **Description**: A flaw in the “open-vsx.org” extension registry could let attackers seize control of the service’s backend, replacing or adding malicious Visual Studio Code extensions.  
- **Impact**: Mass supply-chain compromise of developer workstations, CI/CD pipelines, and downstream applications.  
- **Status**: Researchers disclosed the issue; the Open VSX maintainers have deployed mitigations, but users must re-verify extension integrity.  

### Microsoft 365 “Direct Send” Abuse  
- **Description**: Attackers leverage the seldom-monitored “Direct Send” feature to inject phishing emails that appear to originate from legitimate internal accounts.  
- **Impact**: Credential theft, initial-access establishment, and lateral movement while evading standard email-security gateways.  
- **Status**: Ongoing campaign; Microsoft recommends disabling or monitoring “Direct Send” and enforcing MFA.  

### ScreenConnect Authenticode-Stuffing Technique  
- **Description**: Threat actors modify hidden parameters inside the ConnectWise ScreenConnect installer, preserving a valid Authenticode signature while embedding custom remote-access malware.  
- **Impact**: Signed malware bypasses application-whitelisting controls, enabling stealthy persistence and remote surveillance.  
- **Status**: Observed in active attacks; defenders should verify file hashes rather than signatures alone.  

---

## Affected Systems and Products  

- **AMI MegaRAC BMC Firmware**: Servers from multiple OEMs using vulnerable MegaRAC versions  
- **Cisco Identity Services Engine / ISE-PIC**: All 3.x/4.x branches before latest security release  
- **Brother Printers**: 689 models across color/mono laser, inkjet, label, and scanner lines  
- **Fujifilm/Toshiba/Konica Minolta Printers**: 53 additional models sharing the same password algorithm  
- **Open VSX Registry**: Public extension repository used by Eclipse Theia-based IDEs and VS Code derivatives  
- **Microsoft 365 Tenants**: Any organization with “Direct Send” (SMTP submission) enabled  
- **ConnectWise ScreenConnect**: Windows installers abused for Authenticode stuffing attacks  

---

## Attack Vectors and Techniques  

- **BMC Exploitation via Out-of-Band Management Ports**  
  - **Vector**: Internet-exposed IPMI/Redfish interfaces; credentials not required  
- **Unauthenticated REST API Calls**  
  - **Vector**: Crafted HTTP requests exploit Cisco ISE parsing flaws for RCE  
- **Predictable Default Credentials**  
  - **Vector**: Algorithmically derived printer admin passwords from serial/MAC data  
- **Registry Compromise for Supply-Chain Injection**  
  - **Vector**: Manipulating Open VSX backend to push trojanized extensions  
- **Internal Phishing with Direct Send**  
  - **Vector**: SMTP relay sending spoofed messages that bypass SPF/DKIM checks  
- **Authenticode Stuffing**  
  - **Vector**: Alter PE sections after signature block, maintaining valid signature hashes  
- **Fake CAPTCHA / ClickFix Social Engineering**  
  - **Vector**: Browser overlays trigger malicious downloads as users attempt to verify human status  
- **Microsoft ClickOnce & AWS S3 Hosting**  
  - **Vector**: Side-loading Golang backdoors via trusted cloud storage to energy-sector targets  

---

## Threat Actor Activities  

- **Scattered Spider**  
  - **Campaign**: Pivoted from retail to U.S. insurance providers, leveraging SIM-swapping and social-engineering to breach identity platforms.  
- **APT35 / Charming Kitten (Iran)**  
  - **Campaign**: AI-assisted spear-phishing against Israeli tech and cybersecurity experts; malicious links deliver credential-harvesting pages.  
- **North Korean “Contagious Interview” Operators**  
  - **Campaign**: 35 malicious npm packages masquerading as coding tests; drop infostealers/backdoors on developers.  
- **OneClik Group**  
  - **Campaign**: Targeting energy sector with ClickOnce-delivered Golang malware hosted on AWS infrastructure.  
- **Unidentified Actors Exploiting AMI MegaRAC**  
  - **Campaign**: Server hijacking and bricking attacks observed worldwide; motives range from ransomware to destructive sabotage.  
- **Cyber-Criminal Syndicate in Africa**  
  - **Campaign**: Leveraging open-source tooling (Cobalt Strike, Metasploit) to breach financial institutions across the continent.  
- **ScreenConnect Abusers**  
  - **Campaign**: Weaponizing remote-access software installers to deliver fully signed malware for covert operations.  

---

**End of Report**