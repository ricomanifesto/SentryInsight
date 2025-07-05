# Exploitation Report  

A wave of zero-day exploitation is targeting widely-deployed enterprise infrastructure.  An emergent threat actor tracked as NightEagle is actively abusing an unpatched Microsoft Exchange Server flaw to gain a persistent foothold inside Chinese military and technology networks, while separate China-nexus operators are chaining two Ivanti Connect Secure Appliance (CSA) zero-days to breach French government, telecom, finance, and transport organizations.  Both exploit sets deliver full remote code execution, facilitate credential theft, and enable long-term espionage.  Security teams should prioritize defensive monitoring on public-facing Exchange and Ivanti gateways, implement vendor mitigations immediately, and hunt for post-compromise activity across email, VPN, and identity infrastructure.  

## Active Exploitation Details  

### Microsoft Exchange Server Zero-day Vulnerability  
- **Description**: A previously undocumented flaw in Microsoft Exchange that allows authenticated or low-authenticated attackers to execute arbitrary code on the underlying Windows host.  Exploitation bypasses existing mitigation guidance and directly targets on-premises Outlook Web Access (OWA) endpoints.  
- **Impact**: Remote code execution, email exfiltration, lateral movement, and possible domain compromise.  
- **Status**: Being exploited in the wild as a true zero-day; Microsoft has not yet released a patch.  

### Ivanti Connect Secure Appliance (CSA) Zero-days – Authentication Bypass & Command Injection  
- **Description**: A chained pair of critical vulnerabilities in Ivanti CSA that first allows an unauthenticated attacker to bypass authentication controls and then perform command injection within the underlying operating system.  
- **Impact**: Full device takeover, credential harvesting, network tunneling, and deployment of additional malware or web-shells.  
- **Status**: Actively exploited against multiple French government and commercial entities; Ivanti has issued emergency mitigations and security updates but widespread patching remains incomplete.  

## Affected Systems and Products  

- **Microsoft Exchange Server**: All supported on-premises versions; particularly internet-facing OWA services.  
- **Ivanti Connect Secure Appliance (CSA) / Policy Secure**: Gateway versions prior to the emergency hotfix release; devices often exposed directly to the internet for VPN access.  

## Attack Vectors and Techniques  

- **Server-Side Exploitation of Email Gateway**  
  - **Vector**: Direct HTTP/S requests against Outlook Web Access endpoints to trigger Exchange zero-day code execution.  
- **Chained Auth Bypass → Command Injection on VPN Gateway**  
  - **Vector**: Unauthenticated attacker exploits Ivanti CSA web interface, gains elevated shell, and installs persistence implants.  
- **Web-Shell Deployment & Credential Dumping**  
  - **Vector**: Post-exploitation technique observed on both Exchange and Ivanti appliances to maintain long-term access and pivot internally.  

## Threat Actor Activities  

- **Actor/Group**: NightEagle (aka APT-Q-95)  
  - **Campaign**: Targeting Chinese military and technology sectors via Exchange zero-day; focused on intelligence gathering and lateral movement using bespoke backdoors.  

- **Actor/Group**: Unnamed China-nexus operators & Initial Access Broker  
  - **Campaign**: Exploiting Ivanti CSA zero-days to compromise French government, telecommunications, media, finance, and transport organizations.  Observed “self-patching” devices post-intrusion to monopolize access and block rival attackers.