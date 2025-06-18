# Exploitation Report  

A surge of in-the-wild exploitation is affecting both endpoint and server-side environments. Threat actors are chaining high-impact bugs—ranging from a Linux kernel privilege-escalation now cataloged by CISA, to a Google Chrome zero-day weaponized by the “TaxOff” group—to gain initial access and elevate privileges. Server-side software is equally at risk: live attacks against the Langflow AI-workflow tool are seeding the Flodrix botnet, while legacy Roundcube flaws enabled the theft of more than one million Cock.li user records. These campaigns demonstrate a clear trend toward multi-stage intrusion paths that mix browser exploits, local privilege escalation, and supply-chain abuse in cloud-native and AI-centric stacks.

## Active Exploitation Details  

### Linux Kernel Privilege Escalation Vulnerability  
- **Description**: Memory-management flaw in the Linux kernel that permits use-after-free conditions when handling network packet tables.  
- **Impact**: Local attackers can elevate from any unprivileged account to full root, paving the way for complete host takeover and lateral movement across containers or VMs.  
- **Status**: Confirmed active exploitation; CISA has added the bug to its Known Exploited Vulnerabilities (KEV) catalog. Patches are available from upstream and all major Linux distributions.  

### Google Chrome Zero-Day (CVE-2025-2783)  
- **Description**: Type-confusion vulnerability in the V8 JavaScript engine, exploitable via crafted web content. TaxOff used the flaw in drive-by attacks to execute arbitrary code in the browser process.  
- **Impact**: Remote code execution on Windows, macOS, and Linux endpoints, enabling immediate deployment of the Trinper backdoor and subsequent system compromise.  
- **Status**: Exploited as a zero-day in mid-March 2025; Google has since released security updates for all supported Chrome channels.  
- **CVE ID**: CVE-2025-2783  

### Langflow Remote Code Execution Flaw  
- **Description**: Input-validation weakness in the open-source Langflow platform that lets unauthenticated users inject and run operating-system commands through malformed workflow components.  
- **Impact**: Full system compromise leading to installation of the Golang-based Flodrix botnet, allowing DDoS, data theft, and lateral movement within cloud environments.  
- **Status**: Actively exploited in the wild; maintainers have issued a patched release and urge immediate upgrades.  

### Roundcube Legacy Webmail Flaws (Cock.li Breach)  
- **Description**: Multiple unpatched vulnerabilities in deprecated versions of the Roundcube PHP webmail application, including SQL injection and arbitrary file inclusion.  
- **Impact**: Attackers stole over one million user records from Cock.li, exposing email addresses, hashed passwords, and account metadata.  
- **Status**: Exploited against an out-of-support Roundcube deployment; the affected service has retired the vulnerable platform, but no official vendor patch is expected for end-of-life code.  

## Affected Systems and Products  

- **Linux Kernel (multiple distros)**  
  - **Platform**: Servers, desktops, and container hosts running unpatched kernels shipped with Ubuntu, Debian, Fedora, RHEL, and derivatives  

- **Google Chrome prior to the June 2025 security update**  
  - **Platform**: Windows, macOS, Linux, ChromeOS  

- **Langflow AI Workflow Builder (versions prior to the patched release)**  
  - **Platform**: Python-based applications hosted on Linux or containerized environments  

- **Roundcube Webmail 1.4.x and earlier (legacy, end-of-life)**  
  - **Platform**: PHP web applications on Linux/Apache or Nginx stacks  

## Attack Vectors and Techniques  

- **Drive-By Browser Exploit**  
  - **Vector**: Malicious or compromised websites deliver JavaScript that triggers CVE-2025-2783, spawning a shell and downloading the Trinper backdoor.  

- **Local Privilege Escalation via Kernel Use-After-Free**  
  - **Vector**: Post-compromise payload executes crafted `nftables` operations to reach root on vulnerable Linux hosts.  

- **AI Workflow Supply-Chain Abuse**  
  - **Vector**: Remote HTTP/GraphQL requests inject malicious nodes into exposed Langflow instances, achieving unauthenticated RCE and botnet enrollment.  

- **Legacy Webmail RCE**  
  - **Vector**: Crafted email or HTTP request exploits outdated Roundcube code, allowing attackers to run SQL queries and write arbitrary PHP files on the server.  

## Threat Actor Activities  

- **TaxOff**  
  - **Campaign**: Leveraged Chrome CVE-2025-2783 zero-day to implant the Trinper backdoor, focusing on spear-phished corporate users and government agencies.  

- **Flodrix Botnet Operators**  
  - **Campaign**: Mass-scanning for vulnerable Langflow instances; compromised hosts added to a Golang botnet used for DDoS and cryptomining.  

- **Unknown Actors Abusing Linux Kernel LPE**  
  - **Campaign**: Broad exploitation observed across cloud service providers and on-prem data centers to secure persistence and privilege escalation after initial foothold.  

- **Cock.li Breach Hacker (unnamed)**  
  - **Campaign**: Targeted exploitation of Roundcube flaws to exfiltrate over one million user records, now offered in underground markets.  

- **Water Curse**  
  - **Campaign**: Utilized 76 hijacked GitHub accounts to distribute multi-stage malware; while not tied to a specific CVE, the operation demonstrates sophisticated supply-chain manipulation.  

- **Silver Fox APT**  
  - **Campaign**: Phishing operation against Taiwanese organizations using HoldingHands RAT and Gh0stCringe malware, aiming for long-term espionage.