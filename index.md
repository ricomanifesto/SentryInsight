# Exploitation Report

Security telemetry collected over the last week shows a sharp uptick in high-impact exploitation of enterprise software exposed to the Internet.  The most critical activity involves weaponisation of three recently patched remote-code-execution flaws in Cisco Identity Services Engine (ISE), now confirmed to be giving unauthenticated attackers ROOT access on network-access-control appliances.  In parallel, Microsoft has attributed ongoing intrusions against on-premises SharePoint Server to multiple Chinese state-aligned actors who are chaining still-unpatched SharePoint vulnerabilities for web-shell deployment and lateral movement.  While not exploiting a code defect, the new “Coyote” banking malware deserves mention for abusing Windows’ UI Automation framework in novel ways to harvest banking credentials.  Ransomware operators behind “Interlock” are also escalating double-extortion campaigns, frequently leveraging the above vulnerabilities for initial access before exfiltration and encryption.  Immediate patching, segmentation, and continuous monitoring are strongly advised.

## Active Exploitation Details

### Cisco Identity Services Engine (ISE) Remote-Code-Execution Vulnerabilities
- **Description**: A set of three critical flaws in the web-based administrative interface of Cisco ISE and ISE Passive Identity Connector allow unauthenticated attackers to send crafted requests that trigger deserialisation issues, resulting in full remote code execution as the root user.  
- **Impact**: Complete compromise of the NAC appliance, credential theft, pivoting to internal networks, manipulation of network-access policies.  
- **Status**: Patches were released by Cisco in the most recent ISE maintenance update; Cisco and multiple CERTs now confirm in-the-wild exploitation against unpatched systems.  

### Microsoft SharePoint Server Vulnerabilities
- **Description**: Multiple security flaws in Internet-facing SharePoint Server instances permit attackers to bypass authentication, upload malicious ASPX web shells, and achieve arbitrary code execution within the SharePoint application pool.  
- **Impact**: Initial foothold on corporate networks, privilege escalation, data exfiltration, and persistent command-and-control.  
- **Status**: Updates are available via Microsoft’s security channel.  Exploitation is active and attributed to at least three distinct Chinese APT groups.  

### Windows UI Automation Abuse by “Coyote” Banking Trojan
- **Description**: The latest Coyote variant hooks into the Microsoft UI Automation accessibility framework to detect when users browse specific banking or cryptocurrency sites, allowing screen content capture and credential theft without requiring browser exploits.  
- **Impact**: Real-time theft of online-banking credentials, cryptocurrency wallet information, and session tokens.  
- **Status**: No patch required (abuses legitimate OS feature).  Mitigations revolve around EDR detection of suspicious UI Automation calls and hardening of browser processes.  

### Interlock Ransomware Operational Technique
- **Description**: Interlock operators employ a double-extortion model, exploiting publicly exposed services (including Cisco ISE devices and unpatched VPN gateways) to gain access, exfiltrate sensitive data, and then encrypt on-premises infrastructure.  
- **Impact**: Business disruption, financial loss, public data leaks, and regulatory exposure.  
- **Status**: Active; no vendor patch (tactic).  Mitigation requires patching entry-point vulnerabilities and enforcing strong credential hygiene.  

## Affected Systems and Products

- **Cisco Identity Services Engine (ISE) & ISE Passive Identity Connector**  
  - Platform: Hardware or VM appliances running ISE 3.x (all builds prior to latest hotfix)

- **Microsoft SharePoint Server 2016, 2019, and Subscription Edition (on-premises)**  
  - Platform: Windows Server deployments exposed to the Internet

- **Windows 10/11 Endpoints**  
  - Platform: Any system where users run Chromium-based or Firefox browsers (targeted by Coyote malware’s UI Automation abuse)

- **Corporate Networks & Critical Infrastructure Organisations**  
  - Platform: Multi-OS environments reached via Interlock ransomware campaigns

## Attack Vectors and Techniques

- **Unauthenticated HTTP/HTTPS RCE**  
  - Vector: Crafted REST or SOAP requests to Cisco ISE management interface trigger deserialisation vulnerabilities.

- **SharePoint Web-Shell Upload**  
  - Vector: Abuse of SharePoint API endpoints to upload malicious ASPX files, followed by command execution.

- **UI Automation Framework Hijacking**  
  - Vector: Malware injects into browser processes and uses accessibility APIs to scrape window text and images.

- **Double-Extortion Ransomware Lifecycle**  
  - Vector: Initial exploitation of edge devices → privilege escalation → bulk data exfiltration → file encryption → ransom demand.

## Threat Actor Activities

- **Linen Typhoon, Violet Typhoon, and a third unnamed Chinese APT**  
  - Campaign: Coordinated exploitation of SharePoint Server to establish long-term footholds in government, defence, and manufacturing networks.  
  - Activities: Web-shell deployment, credential dumping, selective data exfiltration.

- **Interlock Ransomware Operators**  
  - Campaign: Surge in attacks on U.S. and EU critical-infrastructure entities; leveraging Cisco ISE and VPN device flaws for entry, followed by double extortion.  
  - Activities: Data theft, encryption, ransom negotiations, threat of public data release.

- **Financially Motivated Actors Distributing Coyote**  
  - Campaign: Targeted phishing against banking customers worldwide; leveraging loader malware that deploys the new UI-Automation-enabled Coyote variant.  
  - Activities: Credential harvesting, real-time session hijacking, cryptocurrency theft.

- **Unattributed Actors Exploiting Cisco ISE**  
  - Campaign: Opportunistic scanning of Internet-facing ISE appliances; goal appears to be initial network access for resale on underground markets.  

