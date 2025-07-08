# Exploitation Report

During the past week, defenders observed a sharp uptick in live exploitation of both enterprise and consumer-grade technologies. The most urgent activity centers on the newly-disclosed CitrixBleed 2 flaw (CVE-2025-5777) in Citrix NetScaler appliances, whose proof-of-concept code is already circulating publicly and being folded into automated exploitation frameworks. Parallel campaigns are abusing unpatched remote-code-execution weaknesses in TBK digital video recorders and Four-Faith industrial routers to expand the RondoDox DDoS botnet. Supply-chain abuse remains a high-priority threat: a poisoned pull-request weaponized the vulnerable Ethcode Visual Studio Code extension, while nearly a dozen malicious Chrome extensions (1.7 million installs) and a trojanized “Color Picker” extension were discovered hijacking browser sessions. Finally, security services continue to flag an in-the-wild Chrome zero-day and ongoing exploitation of Ivanti VPN bugs, underscoring the need for rapid patching and layered defense.

## Active Exploitation Details

### CitrixBleed 2 – NetScaler Memory-Leak/RCE
- **Description**: Critical flaw in Citrix NetScaler ADC/Gateway that allows unauthenticated attackers to leak memory contents and potentially gain remote code execution.
- **Impact**: Credential theft, session hijacking, full device compromise, and lateral movement into internal networks.
- **Status**: Proof-of-concept exploits publicly released; exploitation attempts detected in the wild. Patches are available from Citrix and should be applied immediately.
- **CVE ID**: CVE-2025-5777

### TBK DVR Remote-Code-Execution Flaws
- **Description**: Multiple unauthenticated vulnerabilities in TBK brand digital video recorders enabling execution of arbitrary system commands.
- **Impact**: Attackers can fully take over DVRs, enlist them into botnets, pivot into surveillance networks, or launch outbound DDoS attacks.
- **Status**: Actively exploited by the RondoDox botnet; no universal firmware fix released, leaving owners dependent on network isolation and access-control lists.

### Four-Faith Router Command-Injection Flaws
- **Description**: Input-validation weaknesses in web-based management interfaces of Four-Faith industrial cellular routers permit command injection.
- **Impact**: Remote attackers obtain root shell access, modify routing tables, or deploy malware that weaponizes the router for DDoS or espionage.
- **Status**: Actively abused by RondoDox operators; patch availability varies by model and carrier firmware.

### Ethcode VS Code Extension Supply-Chain Compromise
- **Description**: Maintainer abuse of a vulnerable Ethcode extension allowed a malicious pull request to inject hostile code executed whenever the extension loads in Visual Studio Code.
- **Impact**: More than 6,000 developers risk credential theft and device takeover upon opening VS Code with the tainted extension.
- **Status**: Malicious version removed from the marketplace; users must uninstall, purge cached copies, and rotate affected secrets.

### Google Chrome Zero-Day (July 2025)
- **Description**: Unpatched, actively exploited security flaw in Google Chrome reported in security bulletins and weekly threat recaps.
- **Impact**: Enables remote attackers to achieve sandbox escape and arbitrary code execution on fully-patched Chrome browsers.
- **Status**: Google has begun staged roll-out of a stable-channel fix; exploitation continues against lagging endpoints.

### Ivanti Connect Secure / Policy Secure VPN Vulnerabilities
- **Description**: Recently patched authentication-bypass and command-injection issues in Ivanti remote-access appliances remain a favorite target of attackers.
- **Impact**: Credential harvesting, implant deployment, and persistent network access.
- **Status**: Patches released; threat actors still scanning for unpatched gateways.

### Malicious Chrome Web-Store Extensions
- **Description**: Eleven extensions (1.7 M installs) and a popular “Color Picker” add-on contained spyware code that activates on every navigation event.
- **Impact**: Browser session hijacking, cookie theft, search hijacking, and redirection to exploit-kit infrastructure.
- **Status**: Extensions removed from the Web Store, but sideloaded copies remain in circulation; no browser update required.

## Affected Systems and Products

- **Citrix NetScaler ADC & Gateway**: All firmware branches prior to patched build; appliance and VPX platforms  
- **TBK Digital Video Recorders**: Multiple DVR/NVR models running factory firmware (often internet-exposed)  
- **Four-Faith Industrial Routers (F-Series)**: Cellular and IoT gateway models used in critical infrastructure and remote telemetry  
- **Ethcode VS Code Extension**: Versions pulled from GitHub Marketplace (≈6,000 installations)  
- **Google Chrome Browser**: Stable channel on Windows, macOS, Linux prior to emergency zero-day update  
- **Ivanti Connect Secure / Policy Secure**: VPN appliances running vulnerable 9.x and 22.x code levels  
- **Malicious Chrome Extensions**: “Web Activity Time Tracker,” “Screenshot Master,” “Color Picker” and eight additional titles across Chrome desktop platforms  

## Attack Vectors and Techniques

- **HTTP Memory-Leak Exploit**  
  - **Vector**: Crafted requests to /vpn/* endpoints on vulnerable NetScaler appliances extract session tokens and memory objects.

- **Unauthenticated Command Injection**  
  - **Vector**: Direct POST requests to CGI scripts on TBK DVRs and Four-Faith routers inject shell commands executed with root privileges.

- **Supply-Chain Pull-Request Poisoning**  
  - **Vector**: Malicious contributor submits PR that adds obfuscated JavaScript to Ethcode source, auto-executed in developers’ IDEs.

- **Browser Extension Session Hijack**  
  - **Vector**: OnBeforeNavigate listener steals cookies and performs web-request redirection every time a page loads.

- **Drive-By Chrome 0-Day Delivery**  
  - **Vector**: Malicious websites exploit the undisclosed Chrome renderer bug, achieving sandbox escape and code execution.

- **VPN Web Interface Exploitation**  
  - **Vector**: Automated scanners locate Ivanti portals and trigger authentication bypass to drop web shells.

## Threat Actor Activities

- **RondoDox Botnet Operators**  
  - **Campaign**: Exploiting TBK DVRs and Four-Faith routers to amass a botnet used for volumetric DDoS attacks against gaming and financial services targets.

- **Unknown Exploit Developers (CitrixBleed 2)**  
  - **Activities**: Released public PoC on GitHub and integration into Metasploit, driving commodity scanning across enterprise IP ranges.

- **Malicious Extension Authors**  
  - **Campaign**: Planted spyware extensions in Chrome Web Store; monetized via affiliate redirects and sale of harvested credentials.

- **Supply-Chain Intruder Targeting Ethcode**  
  - **Activities**: Submitted poisoned pull request, likely aiming to reach developers in blockchain ecosystems using the extension.

- **TAG-140**  
  - **Campaign**: Spear-phishing Indian government entities with ClickFix-style lure delivering .NET loaders; leverages open-source tools for post-exploitation.

- **Silk Typhoon Affiliate**  
  - **Activities**: Arrested Chinese national allegedly involved in U.S. cyber-espionage; linked to exploitation of VPN and web-app flaws for initial access.

- **DPRK “NimDoor” Operators**  
  - **Campaign**: Social-engineering crypto workers via Zoom invites; deploy custom macOS backdoors and exploit unpatched third-party plugins.

- **Hunters International RaaS (retiring)**  
  - **Activities**: Announced shutdown/rebrand; historically capitalized on Citrix and VPN vulnerabilities for ransomware deployment.

---

Security teams should prioritize patching Citrix NetScaler appliances, isolate vulnerable DVRs/routers, remove malicious browser and IDE extensions, and accelerate Chrome and Ivanti updates. Continuous monitoring for unusual outbound traffic from edge devices and developer workstations remains critical to disrupt active threat campaigns.