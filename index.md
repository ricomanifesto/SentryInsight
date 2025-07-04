# Exploitation Report

Over the last week, multiple high-impact zero-day exploits have come to light. A newly identified threat group dubbed **NightEagle (APT-Q-95)** is actively weaponizing an undisclosed Microsoft Exchange Server flaw to breach organizations in China’s military and technology sectors. Simultaneously, Chinese-aligned actors are abusing two separate zero-day vulnerabilities in **Ivanti Connect Secure Appliances (CSA)**, compromising French government and critical-infrastructure entities. An additional China-nexus initial-access broker was observed exploiting the same Ivanti bugs and then “self-patching” victims’ appliances to monopolize access. These campaigns collectively enable full remote code execution, credential theft, and long-term persistence in enterprise environments.

## Active Exploitation Details

### Microsoft Exchange Server Zero-Day (NightEagle)
- **Description**: An undisclosed remote code execution flaw in on-premises Microsoft Exchange Server exploited via crafted HTTP requests that ultimately allow web-shell deployment and command execution under SYSTEM privileges.  
- **Impact**: Full compromise of corporate email, lateral movement inside the network, exfiltration of sensitive military and proprietary technology data.  
- **Status**: Being actively exploited as a zero-day; Microsoft has not yet released a security update. Mitigations currently revolve around disabling exposed Exchange web services and applying strict perimeter filtering.  

### Ivanti Connect Secure Appliance Zero-Days
- **Description**: Two independent vulnerabilities in Ivanti’s VPN gateway (CSA) enable unauthenticated attackers to bypass authentication controls and execute arbitrary commands on the underlying OS.  
- **Impact**: Remote code execution, credential harvesting, backdoor installation, and network pivoting into sensitive French government, telecom, media, finance, and transport networks.  
- **Status**: Exploitation confirmed in the wild by Chinese threat actors; emergency patches and mitigations have been released by Ivanti and the French CERT.  

### Ivanti Zero-Day “Self-Patch” Abuse (Initial-Access Broker)
- **Description**: The same Ivanti zero-days above are leveraged by a likely China-nexus initial-access broker who, after exploitation, installs their own hot-fix to prevent other attackers from exploiting the appliance, ensuring exclusive foothold.  
- **Impact**: Maintains sole persistence for subsequent resale of access to ransomware crews or espionage units while evading defensive scanning for known vulnerable versions.  
- **Status**: Ongoing; defenders must verify appliance integrity as patched versions may still be compromised.  

## Affected Systems and Products

- **Microsoft Exchange Server 2019 / 2016 (on-premises)**  
  - **Platform**: Windows Server deployments exposed to the Internet via Outlook Web Access / Exchange Control Panel  
- **Ivanti Connect Secure Appliance (formerly Pulse Secure VPN) – All 9.x / 22.x lines**  
  - **Platform**: Hardened Linux-based VPN gateways used in enterprise and government remote-access deployments  

## Attack Vectors and Techniques

- **Web-Shell Implantation via Exchange HTTP Abuse**  
  - **Vector**: Crafted HTTP POST/GET requests targeting the vulnerable Exchange endpoint, followed by drop-in of China Chopper-style web shells.  

- **Authentication Bypass & Command Injection on Ivanti CSA**  
  - **Vector**: Unauthenticated REST calls chaining the auth-bypass bug with a subsequent command injection to run arbitrary shell commands as root.  

- **Self-Patching Post-Exploitation**  
  - **Vector**: Attackers upload vendor-style hot-fix packages after initial compromise, closing exploitable endpoints to lock out competitors while keeping their own backdoors.  

## Threat Actor Activities

- **NightEagle (APT-Q-95)**  
  - **Campaign**: Targeting Chinese military research institutes and semiconductor firms; establishes web-shells on Exchange, uses custom backdoors for data exfiltration.  

- **Chinese State-Aligned Intrusion Set**  
  - **Campaign**: Widespread exploitation of Ivanti CSA zero-days against French government, telecom, transport, media, and finance sectors; focuses on credential theft and long-term espionage.  

- **Unnamed China-Nexus Initial-Access Broker**  
  - **Campaign**: Monetizes compromised Ivanti appliances by selling persistent access on dark-web markets; employs “self-patching” to retain exclusivity and frustrate rival crews.  

---

**Analyst Note**: Organizations running on-premises Exchange or Ivanti Connect Secure should treat these issues as critical, initiate out-of-band patching or apply vendor-recommended mitigations immediately, and perform comprehensive compromise assessments focusing on web-shell artifacts and unauthorized administrative accounts.