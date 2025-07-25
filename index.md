# Exploitation Report

Over the past week, threat actors have ramped up exploitation of enterprise collaboration and virtualization platforms while simultaneously introducing novel malware delivery methods. Ongoing ransomware campaigns are abusing multiple Microsoft SharePoint vulnerabilities collectively tracked as “ToolShell,” Chinese-linked espionage operators (“Fire Ant”) are chaining VMware flaws to gain hypervisor-level access, and critical authentication bypass weaknesses in Mitel’s MiVoice MX-ONE are drawing immediate attention from defenders. At the same time, new Linux malware (“Koske”) and supply-chain style compromises in the Steam gaming ecosystem illustrate attackers’ continued creativity in initial access. Law-enforcement takedowns (BlackSuit, XSS) have disrupted some criminal infrastructure, yet active exploitation of the vulnerabilities listed below remains widespread.

## Active Exploitation Details

### Microsoft SharePoint “ToolShell” Vulnerabilities  
- **Description**: A set of SharePoint bugs that allow remote, unauthenticated attackers to upload malicious DLLs and execute arbitrary PowerShell (“ToolShell”) in the context of the SharePoint server.  
- **Impact**: Facilitates initial access for ransomware deployment, lateral movement, and data exfiltration. Compromised servers serve as launch pads for domain-wide encryption.  
- **Status**: Confirmed in-the-wild exploitation by Storm-2603 for ransomware operations; Microsoft patches available.  
- **CVE ID**: CVE-2023-29385, CVE-2023-24955  

### VMware ESXi & vCenter Remote Code-Execution Chain  
- **Description**: Multiple flaws in VMware ESXi hypervisors and vCenter that allow guest-to-host escape and unauthenticated code execution on management interfaces, enabling attackers to compromise entire virtualization clusters.  
- **Impact**: Full control of virtual machines, access to memory of co-resident workloads, credential theft, and long-term espionage footholds.  
- **Status**: Active exploitation by the Fire Ant espionage group; patches and mitigations released by VMware.  
- **CVE ID**: CVE-2023-34048, CVE-2023-20867  

### Mitel MiVoice MX-ONE Authentication Bypass  
- **Description**: A critical flaw that lets remote attackers bypass login mechanisms on MiVoice MX-ONE call-control systems through crafted HTTP requests.  
- **Impact**: Complete administrative takeover of enterprise telephony infrastructure, call interception, and potential pivoting inside voice/data networks.  
- **Status**: Security update issued by Mitel; exploitation proof-of-concepts are circulating.  

### “Koske” Linux Loader (Image Steganography Exploit)  
- **Description**: Malware leverages benign-looking Panda JPEGs to hide and side-load malicious shellcode directly into memory, enabling execution without touching disk.  
- **Impact**: Stealthy persistence on Linux servers, evasion of traditional file-based AV and EDR, follow-on deployment of crypto-miners and credential stealers.  
- **Status**: Actively observed in the wild; no vendor patch (behavioral mitigation required).  

### Steam Early-Access Supply-Chain Compromise  
- **Description**: Threat actor “EncryptHub” replaced legitimate game binaries inside an early-access Steam title with an info-stealer, abusing Steam’s content distribution.  
- **Impact**: Theft of browser cookies, crypto-wallets, and platform credentials from gamers; potential lateral spread through Steam friend-networks.  
- **Status**: Malware removed by Valve; investigation ongoing.  

## Affected Systems and Products

- **Microsoft SharePoint Server 2019 / Subscription Edition**  
  - Platform: Windows Server on-prem & hybrid cloud deployments  

- **VMware ESXi 6.7, 7.x, 8.x and vCenter Server 7.x / 8.x**  
  - Platform: Bare-metal hypervisors and vSphere management appliances  

- **Mitel MiVoice MX-ONE (all branches ≤ latest pre-patch build)**  
  - Platform: Linux-based PBX and call-control appliances  

- **Linux Distributions (Ubuntu, Debian, CentOS, Rocky, etc.) hosting public-facing services**  
  - Platform: x86_64 cloud & on-prem servers targeted by Koske  

- **Steam Early-Access Game “(Title Withheld)”**  
  - Platform: Windows gaming PCs using the Steam client  

## Attack Vectors and Techniques

- **DLL Upload via SharePoint API (“ToolShell”)**  
  - Vector: Crafted SOAP/REST requests bypassing permission checks to drop and invoke malicious DLLs.  

- **Guest-to-Host Escape & vCenter API Abuse**  
  - Vector: Chained VMware flaws allowing code execution from a compromised VM or via TCP/443 against vCenter.  

- **HTTP Authentication Bypass**  
  - Vector: Manipulated path traversal in MiVoice web interface, skipping session validation routines.  

- **Steganography-Based Payload Injection**  
  - Vector: Decoding of encrypted shellcode embedded in JPEG images, executed in-memory via LD_PRELOAD.  

- **Software-Supply-Chain Poisoning (Steam CDN)**  
  - Vector: Upload of trojanized game builds to the official content delivery network, automatically pushed to users.  

## Threat Actor Activities

- **Storm-2603 (China-nexus)**  
  - Campaign: Ransomware deployment leveraging SharePoint “ToolShell” bugs for rapid domain encryption across North American and European enterprises.  

- **Fire Ant**  
  - Campaign: Long-term espionage targeting telecom and government clouds; implants on ESXi hosts harvest credentials and virtual disk images.  

- **BlackSuit Ransomware**  
  - Campaign: Infrastructure disrupted by Operation Checkmate; previously exploited unpatched VPN and software vulnerabilities to breach “hundreds” of organizations.  

- **EncryptHub**  
  - Campaign: Trojanized Steam early-access title to distribute info-stealer malware, focusing on the gaming community.  

- **Koske Developers (Unattributed)**  
  - Campaign: Broad opportunistic scanning of Linux servers, believed to be AI-assisted in malware generation and payload packing.