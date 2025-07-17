# Exploitation Report

Recent threat-hunting findings highlight an aggressive wave of exploitation targeting edge appliances and collaboration platforms. The most critical activity centres on a previously unknown flaw in SonicWall Secure Mobile Access (SMA) appliances that adversaries are abusing to deploy a boot-level rootkit dubbed **OVERSTEP**. The intrusion set, believed to be related to the Abyss ransomware group, is successfully compromising fully patched yet end-of-support devices and maintaining persistence even across firmware upgrades. At the same time, an upgraded **Matanbuchus 3.0** loader is being mass-distributed through Microsoft Teams chats, giving ransomware operators turnkey initial access inside corporate environments. These simultaneous campaigns demonstrate an attacker focus on supply-chain touchpoints and ubiquitous SaaS collaboration tools to sidestep traditional perimeter defences.

## Active Exploitation Details

### SonicWall SMA Zero-Day (OVERSTEP)
- **Description**: An unpatched, previously unknown vulnerability in SonicWall Secure Mobile Access appliances allows remote attackers to gain root access, disable signature verification in the bootloader, and inject the persistent OVERSTEP rootkit into the firmware image.  
- **Impact**: Full device takeover, stealth persistence across reboots and firmware upgrades, covert command-and-control, and facilitation of lateral movement for ransomware deployment.  
- **Status**: Actively exploited in the wild against fully updated but end-of-support SMA hardware. No vendor patch is currently available; SonicWall is investigating mitigation options.  

### Microsoft Teams File Delivery Abuse Enabling Matanbuchus 3.0
- **Description**: Attackers exploit Microsoft Teams’ external messaging capabilities to deliver malicious MSI packages that sideload the Matanbuchus 3.0 loader. The loader incorporates EDR evasion, DNS-tunneled C2, and plug-and-play ransomware deployment features.  
- **Impact**: Initial foothold within enterprise Microsoft 365 tenants, stealth payload execution, follow-on ransomware or data-exfiltration modules.  
- **Status**: Ongoing campaign observed; no underlying Teams software vulnerability is required, so standard patching does not mitigate the threat.  

## Affected Systems and Products

- **SonicWall Secure Mobile Access appliances**: SMA 1000 series and out-of-support SMA 200/210/400/410 devices running the latest available firmware  
  - **Platform**: On-premises VPN/remote-access gateways deployed in corporate DMZs  

- **Microsoft Teams (Microsoft 365)**: Desktop and web clients capable of receiving external chat invitations and file attachments  
  - **Platform**: Windows, macOS, and browser-based clients in enterprise and education tenants  

## Attack Vectors and Techniques

- **Remote Device Exploitation**  
  - **Vector**: Directly targeting publicly exposed SonicWall SMA management interfaces to execute the zero-day, overwrite boot components, and install OVERSTEP.  

- **Bootloader Manipulation / Bootkit Deployment**  
  - **Vector**: Modifies `grub.cfg` and embedded kernel modules to disable signature checks, ensuring rootkit persistence across firmware flashes.  

- **SaaS Chat Malware Delivery**  
  - **Vector**: Sending malicious MSI installers via Microsoft Teams chats or channel file shares; leveraging user trust and default file-handling behaviour to trigger Matanbuchus 3.0 execution.  

- **DNS-Based Command-and-Control**  
  - **Vector**: Matanbuchus 3.0 resolves C2 instructions through DNS TXT records, reducing reliance on blocked IP endpoints and blending with legitimate traffic.  

## Threat Actor Activities

- **Abyss Ransomware-Linked Operators**  
  - **Campaign**: Deployment of OVERSTEP on SonicWall SMA appliances to establish covert persistence, followed by staged ransomware encryption inside victim networks. Targets include midsize enterprises reliant on legacy SMA hardware.  

- **Matanbuchus 3.0 Affiliates**  
  - **Campaign**: Mass social-engineering via Microsoft Teams to deliver the upgraded loader, enabling rapid pivot to ransomware payloads. Focused on technology, finance, and professional-services firms with high Microsoft 365 usage.  

- **ShinyHunters (Related Data-Breach Activity)**  
  - **Campaign**: While not exploiting a newly disclosed vulnerability, the group is credited with the coordinated breaches of Louis Vuitton’s regional sites, illustrating continued focus on retail/luxury targets for data-theft monetisation.  

**Bold, multi-layered defence—encompassing strict patch management, end-of-support hardware retirement, and SaaS collaboration hardening—is essential to counter these rapidly evolving exploitation trends.**