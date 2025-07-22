# Exploitation Report

Recent intelligence shows a sharp uptick in real-world exploitation of enterprise collaboration software and targeted cyber-espionage.  A critical Microsoft SharePoint zero-day is being weaponized to steal authentication keys and maintain long-term footholds in victims’ networks, while China-backed APT41 has expanded its operations into Africa by chaining an undisclosed web-application vulnerability with sophisticated post-exploitation tooling.  Together, these campaigns highlight an urgent need for rapid patch deployment, continuous monitoring of cloud and on-prem collaboration suites, and heightened vigilance against state-sponsored actors pivoting into new geographic regions.

## Active Exploitation Details

### Microsoft SharePoint Zero-Day (July 2025)
- **Description**: A previously unknown flaw in Microsoft SharePoint allows remote, unauthenticated attackers to craft specially formed requests that bypass normal authentication checks, steal signing keys, and execute arbitrary code under the SharePoint service context.  
- **Impact**: Attackers gain the ability to extract OAuth and SAML tokens, create backdoors for persistent access, move laterally across Microsoft 365 workloads, and exfiltrate sensitive data hosted in SharePoint document libraries.  
- **Status**: Confirmed in-the-wild exploitation since 7 July 2025.  Microsoft has issued interim mitigations, with a full security update expected in the next Patch Tuesday release.  

### Unnamed Web-Application Zero-Day Leveraged by APT41
- **Description**: APT41 compromised an African IT services provider through an undisclosed vulnerability in a perimeter web service.  The flaw enabled direct server compromise and deployment of custom web shells followed by precision credential harvesting.  
- **Impact**: Full takeover of the provider’s network, theft of internal project data, and establishment of covert C2 channels for ongoing espionage on downstream government clients.  
- **Status**: Actively exploited; no vendor patch has been announced.  Network defenders are relying on signature-based detections for the group’s bespoke malware loader and web-shell naming conventions.  

### ExpressVPN Windows Client RDP Tunnel-Bypass Flaw
- **Description**: A logic error in the Windows client routing table caused Remote Desktop Protocol traffic to exit the physical interface instead of the encrypted VPN tunnel, revealing users’ real IP addresses.  
- **Impact**: Adversaries monitoring RDP gateways could correlate VPN users with their true locations, de-anonymize sessions, or launch targeted intrusion attempts.  
- **Status**: Patched in the latest ExpressVPN Windows release.  No confirmed malicious exploitation, but proof-of-concept testing shows the leak is easily reproducible.  

## Affected Systems and Products

- **Microsoft SharePoint Server**: On-prem deployments (2019, Subscription Edition) exposed to the Internet  
- **Microsoft 365 Tenants**: Hybrid environments federating on-prem SharePoint with cloud services  
- **Unnamed Custom Web Portal**: Public-facing application managed by the targeted African IT services firm  
- **Windows endpoints running ExpressVPN**: Versions prior to the most recent client update  

## Attack Vectors and Techniques

- **Unauthenticated RCE via Crafted SharePoint Requests**  
  - **Vector**: Malicious HTTP payloads to a vulnerable SharePoint API endpoint bypass authentication and trigger code execution.  

- **Web-Shell Deployment & Living-off-the-Land (APT41)**  
  - **Vector**: Upload of obfuscated ASPX web shells, followed by PowerShell and WMI for lateral movement.  

- **VPN Tunnel Bypass (Information Disclosure)**  
  - **Vector**: Manipulation of Windows routing tables during RDP session handshake causes traffic to circumvent the VPN tunnel.  

## Threat Actor Activities

- **Actor/Group**: APT41 (a.k.a. Winnti, Barium)  
  - **Campaign**: Targeted intrusion against an African IT services provider; used a zero-day in a web service, deployed custom loaders, and exfiltrated sensitive regional government data.  

- **Actor/Group**: Unattributed threat clusters abusing SharePoint zero-day  
  - **Campaign**: Global opportunistic attacks focusing on organizations with externally exposed SharePoint; objectives include credential theft, long-term persistence, and reconnaissance inside Microsoft 365 environments.  

- **Actor/Group**: Security researchers / proof-of-concept testers  
  - **Campaign**: Validated ExpressVPN RDP leak to demonstrate deanonymization risks; no public evidence of weaponization by criminal or state actors yet.