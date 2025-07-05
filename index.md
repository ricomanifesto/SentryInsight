# Exploitation Report

Recent threat-intelligence disclosures highlight two concurrent zero-day campaigns of exceptional severity.  NightEagle (APT-Q-95) is leveraging an unpatched Microsoft Exchange Server flaw to compromise mail servers inside Chinese military and technology organizations, while a separate China-nexus cluster is abusing two fresh Ivanti Connect Secure Appliance (CSA) vulnerabilities against French government, telecom, media, finance, and transport networks.  Both operations enable full remote code execution, credential theft, and long-term persistence, emphasizing the ongoing risk posed by internet-facing infrastructure that cannot be patched immediately.

## Active Exploitation Details

### Microsoft Exchange Server Zero-Day (NightEagle Campaign)
- **Description**: A previously unknown vulnerability in Microsoft Exchange Server that allows remote, unauthenticated attackers to execute code by abusing the server’s web services component.  
- **Impact**: Full system compromise, lateral movement into Windows domains, email exfiltration, and potential deployment of additional malware.  
- **Status**: Confirmed in-the-wild exploitation; Microsoft has not yet issued a patch or mitigation guidance at the time of reporting.  

### Ivanti Connect Secure Appliance Zero-Days
- **Description**: Two distinct vulnerabilities in Ivanti CSA (and related Policy Secure / NZA products) enabling remote code execution and device takeover when specially crafted HTTPS requests are sent to the VPN gateway.  
- **Impact**: Theft of VPN credentials, session hijacking, installation of web-shells, and pivoting into protected internal networks.  
- **Status**: Actively exploited; Ivanti has released temporary mitigations and urges customers to apply forthcoming firmware updates as soon as available.  

## Affected Systems and Products

- **Microsoft Exchange Server**: Internet-facing on-premise deployments across all supported versions (2019, 2016, 2013)  
  - **Platform**: Windows Server environments in enterprise and governmental data centers  

- **Ivanti Connect Secure / Policy Secure / Neurons for Zero Trust Access**: Appliances running default or out-of-date firmware versions  
  - **Platform**: Hardened Linux-based VPN gateways used in government, telecom, finance, media, and transportation sectors  

## Attack Vectors and Techniques

- **Server-Side Request Forgery & Authentication Bypass (Exchange)**  
  - **Vector**: Crafted HTTP/HTTPS requests to `/owa/` and related endpoints bypass authentication controls, allowing arbitrary PowerShell or operating-system commands.  

- **Malicious HTTPS Configuration Payload (Ivanti CSA)**  
  - **Vector**: Custom SSL request chains exploit input-validation flaws in device web management, injecting system commands and dropping web-shells.  

- **Credential Dumping & Privilege Escalation (Post-Exploit)**  
  - **Vector**: Use of built-in tooling (eg, `ntdsutil`, LSASS memory scraping) once initial foothold is achieved, followed by lateral movement via SMB and WMI.  

## Threat Actor Activities

- **Actor/Group**: NightEagle (aka APT-Q-95)  
  - **Campaign**: Targets Chinese military R&D institutes and high-tech firms; observed deploying custom backdoors and exfiltrating sensitive engineering documents via compromised Exchange servers.  

- **Actor/Group**: Unnamed China-nexus threat cluster (linked to prior state-sponsored activity)  
  - **Campaign**: Multi-sector intrusions in France using Ivanti zero-days; objectives include long-term espionage, collection of government communications, and reconnaissance within telecom infrastructure.