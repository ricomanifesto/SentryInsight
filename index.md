# Exploitation Report

An ongoing wave of intrusions is leveraging a previously unknown zero-day in SonicWall Secure Mobile Access (SMA) appliances to deploy a custom rootkit dubbed **“OVERSTEP.”**  The flaw is being exploited against fully patched – but end-of-life – SMA 100-series devices, providing attackers with persistent, pre-boot control, credential theft, and subsequent ransomware deployment.  Concurrently, the upgraded **Matanbuchus 3.0** loader is being pushed through social-engineering lures in Microsoft Teams chats, streamlining ransomware delivery and evading EDR solutions.  Taken together, the activity highlights a heightened threat to remote-access infrastructure and collaboration platforms that many organizations still regard as “trusted” entry points.

## Active Exploitation Details

### SonicWall Secure Mobile Access Zero-Day (OVERSTEP Campaign)
- **Description**: Unknown pre-authentication flaw in SonicWall SMA 100-series appliances lets attackers gain root access and implant the OVERSTEP boot-level rootkit, which tampers with the `/sbin/init` process and multiple system libraries to guarantee execution before the operating system fully loads.  
- **Impact**: Full device takeover, credential harvesting (including LDAP and local admin hashes), complete network entry, and the ability to stage further payloads such as ransomware.  
- **Status**: Actively exploited in the wild against fully patched but legacy (end-of-support) devices; no vendor patch is currently available.  Mitigations are limited to device isolation, replacement with supported hardware, and complete re-imaging.  

### Microsoft Teams Abuse Delivering Matanbuchus 3.0 Loader
- **Description**: Threat actors initiate targeted Microsoft Teams chats that persuade recipients to execute a malicious archive or shortcut.  The lure drops Matanbuchus 3.0, a loader with new DNS-based C2, built-in EDR process discovery, and file-less execution upgrades.  
- **Impact**: Initial foothold on user workstations, lateral movement, and simplified deployment of ransomware or additional post-exploitation frameworks.  
- **Status**: Ongoing campaigns observed; no underlying Microsoft Teams vulnerability is required, so no patch applies.  Protection hinges on conditional access, attachment filtering, and user awareness.  

## Affected Systems and Products

- **SonicWall SMA 100-Series Appliances**  
  - Affected Versions: SMA 200, 210, 400, 410 (end-of-life but widely deployed)  
  - Platform: Hardened Linux-based firmware used for SSL-VPN and secure remote access  

- **Microsoft Teams (Desktop and Web)**  
  - Platform: Windows & macOS endpoints connected to Microsoft 365 tenants  
  - Component: Chat and file-sharing functionality abused for malware delivery  

## Attack Vectors and Techniques

- **Zero-Day Remote Code Execution on VPN Gateway**  
  - Vector: Unidentified flaw reachable via the SMA web interface enables unauthenticated compromise, followed by rootkit installation in the device boot chain.  

- **Boot-Level Rootkit (OVERSTEP)**  
  - Technique: Modifies critical startup files (`/sbin/init`, `/usr/lib/...`) so malicious libraries load before the OS, ensuring persistence and disabling security controls.  

- **Phishing via Collaboration Platform**  
  - Vector: Social-engineering messages in Microsoft Teams deliver malicious ZIP/LNK files; execution launches the Matanbuchus 3.0 loader without raising traditional email-security alarms.  

- **DNS-Based Command-and-Control**  
  - Technique: Matanbuchus 3.0 beacons and retrieves payloads over DNS queries to avoid HTTP inspection and blend with normal traffic.  

## Threat Actor Activities

- **Unnamed Threat Actor Linked to Abyss Ransomware**  
  - Campaign: Exploiting SonicWall zero-day to implant OVERSTEP, harvest credentials, and stage ransomware operations against enterprises relying on outdated SMA appliances.  
  - Targeting: Organizations using SMA 100-series for remote workforce connectivity.  

- **Matanbuchus 3.0 Operators**  
  - Campaign: Spear-phishing via Microsoft Teams to distribute enhanced loader that automatically profiles endpoints, disables security tooling, and hands off control to ransomware affiliates.  
  - Targeting: Technology, legal, and manufacturing firms with high reliance on Teams collaboration.  

