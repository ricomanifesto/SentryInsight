# Exploitation Report

A sharp uptick in server-side and network appliance compromises dominates recent threat activity. The most urgent issues center on a maximum-severity flaw in AMI’s MegaRAC BMC firmware that lets intruders fully hijack or permanently brick servers, and two different NetScaler ADC/Gateway weaknesses—one (CVE-2025-6543) already weaponized for denial-of-service attacks and another, dubbed “CitrixBleed 2,” allowing unauthenticated session hijacking. CISA has fast-tracked these issues, together with exploited bugs in D-Link DIR-859 home routers and Fortinet FortiOS, into its Known Exploited Vulnerabilities catalog, underscoring the breadth of devices at risk. Simultaneously, newly patched software flaws such as WinRAR’s CVE-2025-6218 show how commodity applications can be turned into launchpads for post-extraction malware, while diverse threat actors—including Iran’s APT35, North Korea’s Lazarus-linked developers, and financially-motivated groups operating in Africa—leverage open-source tooling, AI-assisted phishing, and software-supply-chain attacks to extend their reach. Urgent patching, firmware updates, and hardening of remote-management interfaces remain critical for defenders.  

## Active Exploitation Details

### AMI MegaRAC BMC Remote Code Execution / Device Bricking
- **Description**: A maximum-severity vulnerability in AMI’s MegaRAC Baseboard Management Controller software permits unauthenticated remote code execution that can hand over full out-of-band management control to attackers. The flaw also allows adversaries to corrupt firmware images, effectively bricking affected servers.  
- **Impact**: Complete server takeover, firmware destruction, service interruption across entire data-center fleets.  
- **Status**: Actively exploited in the wild; AMI and OEM server vendors have issued patched firmware images, but exploitation continues while unpatched devices remain reachable.  

### Citrix NetScaler ADC/Gateway DoS
- **Description**: Buffer-handling weakness in request processing causes NetScaler appliances to crash or enter an unrecoverable state when sent specially crafted packets.  
- **Impact**: Remote attackers can force a denial-of-service that knocks portals offline, disrupting VPN and application-delivery services.  
- **Status**: Confirmed active exploitation; Citrix released emergency firmware updates.  
- **CVE ID**: CVE-2025-6543  

### Citrix NetScaler “CitrixBleed 2” Session Hijacking
- **Description**: Memory-handling issue similar to the original CitrixBleed allows unauthenticated actors to extract valid session tokens and impersonate legitimate users.  
- **Impact**: Full account takeover, lateral movement into internal networks, potential data theft.  
- **Status**: In-the-wild exploitation reported; mitigations and patches available from Citrix.  

### D-Link DIR-859 Router Command Injection
- **Description**: Improper input validation within the web-management interface enables attackers on the WAN side to inject system commands with root privileges.  
- **Impact**: Remote code execution, router hijacking for botnet creation or network eavesdropping.  
- **Status**: Added to CISA KEV after confirmed exploitation; unofficial third-party firmware or device replacement often required because vendor support is discontinued.  

### Fortinet FortiOS Heap/Buffer Overflow
- **Description**: Malformed IPSec or SSL-VPN packets trigger a heap overflow, granting code-execution in the FortiOS context.  
- **Impact**: Firewall compromise, traffic interception, and platform pivoting.  
- **Status**: Active exploitation prompted inclusion in CISA KEV; Fortinet has issued security updates for supported versions.  

### WinRAR Directory Traversal
- **Description**: CVE-2025-6218 permits crafted archive entries to write files outside the intended extraction path, enabling automatic execution of attacker-supplied binaries post-extraction.  
- **Impact**: Code execution on user workstations, initial access for further malware deployment.  
- **Status**: Patched in WinRAR 7.10 and later; exploitation viability demonstrated in the wild.  
- **CVE ID**: CVE-2025-6218  

## Affected Systems and Products

- **AMI MegaRAC BMC Firmware**: MegaRAC SP-X versions shipped in many OEM x86 servers (Dell, HPE, Lenovo, Supermicro).  
- **Citrix NetScaler ADC / Gateway**: Versions 14.1 ≤ 14.1-23.x, 13.1 ≤ 13.1-51.x, 13.0 ≤ 13.0-92.x, 12.1 (EoL).  
- **D-Link DIR-859 Router**: All firmware revisions; product is end-of-life.  
- **Fortinet FortiOS**: 7.4.x < 7.4.3, 7.2.x < 7.2.7, 7.0.x < 7.0.14, 6.4.x < 6.4.15 (plus long-term support trains).  
- **WinRAR**: Windows desktop versions prior to 7.10.  

## Attack Vectors and Techniques

- **Out-of-Band Management Takeover**: Leveraging MegaRAC BMC flaw via TCP/UDP management ports exposed to the Internet or internal networks.  
- **DoS Packet Flooding**: Sending crafted traffic to vulnerable NetScaler appliances to trigger crashes (CVE-2025-6543).  
- **Token Skimming (“CitrixBleed 2”)**: Memory scraping to extract session tokens and reuse them for authenticated access.  
- **Command Injection over HTTP**: Injecting shell commands through vulnerable CGI parameters on D-Link DIR-859 routers.  
- **Heap Overflow Exploitation**: Malformed VPN traffic to Fortinet FortiOS leading to remote code execution within security appliance.  
- **Archive Path Traversal**: Embedding “..\\” paths in RAR files so extracted payloads land in Startup folders (CVE-2025-6218).  

## Threat Actor Activities

- **APT35 / Charming Kitten (Iran)**  
  - **Campaign**: AI-assisted spear-phishing against Israeli journalists and cybersecurity experts, aiming to deliver malware implants and collect credentials.  

- **OneClik Campaign (Unknown Actor, likely state-aligned)**  
  - **Activities**: Abuses Microsoft ClickOnce and AWS S3/CloudFront to host payloads, targeting energy-sector organizations with Golang backdoors.  

- **North Korean “Contagious Interview” Operators**  
  - **Campaign**: Malicious npm packages and fake job interviews to infect developers with infostealers/backdoors; 35 new packages observed.  

- **African Financial-Sector Intrusions (Financially Motivated Group)**  
  - **Campaign**: Uses open-source post-exploitation frameworks (e.g., Sliver, Mythic) and commodity RATs to compromise banks across multiple African nations.  

- **Dire Wolf Ransomware Group**  
  - **Campaign**: Double-extortion ransomware hits 16 organizations in tech and manufacturing since May, leveraging stolen VPN credentials and unpatched edge devices (including NetScaler appliances).  

- **IntelBroker (Individual Actor)**  
  - **Activities**: Charged for multi-victim data-theft campaigns; leveraged previously compromised credentials and public exploit kits.  

- **BreachForums Operators**  
  - **Activities**: Arrested in France; forum leveraged to traffic data obtained through exploitation of KEV-listed vulnerabilities such as NetScaler and Fortinet flaws.  

---

Defenders should prioritize patching Internet-facing infrastructure—especially server BMC firmware, NetScaler ADCs/Gateways, Fortinet firewalls, and consumer-grade routers still deployed in small-office environments—and deploy network segmentation to mitigate post-exploitation lateral movement. Continuous monitoring for archive path traversal exploitation and phishing campaigns exploiting AI tooling remains equally critical.