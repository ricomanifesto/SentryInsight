# Exploitation Report

A China-nexus threat actor is actively leveraging multiple zero-day vulnerabilities in Ivanti Connect Secure Appliances to compromise French government agencies, telecom providers, media companies, financial institutions, and transport operators. Once inside, the intruders pivot laterally, exfiltrate data, and—in some cases—apply their own “self-patch” to the devices to lock out competing attackers. The campaign combines sophisticated exploitation of the unpatched flaws with supply-chain-style persistence techniques and highlights the urgent need for immediate mitigation across all exposed Ivanti Secure Access infrastructure.

## Active Exploitation Details

### Ivanti Connect Secure Appliance Zero-Day Vulnerabilities
- **Description**: Previously unknown flaws in Ivanti Connect Secure (formerly Pulse Secure) and related Ivanti Policy Secure / Neurons for ZTA gateways allow unauthenticated remote attackers to run arbitrary commands on the underlying operating system. The bugs enable full device takeover, credential harvesting, and installation of additional malware or persistence scripts.
- **Impact**: Attackers obtain root-level control of the VPN appliance, intercept enterprise traffic, harvest credentials, move laterally into internal networks, and exfiltrate sensitive data.
- **Status**: Actively exploited in the wild by China-linked APT operators and at least one Initial Access Broker (IAB) that “self-patches” the devices post-compromise. Ivanti has released emergency mitigations and out-of-band security updates; comprehensive patches are now available and must be applied immediately across all affected appliances.

## Affected Systems and Products

- **Ivanti Connect Secure (ICS)**: All currently supported versions of the SSL-VPN gateway  
  **Platform**: Hardware and virtual appliances on enterprise perimeter
- **Ivanti Policy Secure / Unified Access Gateway / Neurons for ZTA**: Corresponding firmware branches that share the vulnerable codebase  
  **Platform**: On-premises access-control appliances deployed in government and corporate networks
- **French Government Ministries & Agencies**: Production ICS clusters providing remote access for civil servants  
  **Platform**: Mixed on-premises hardware deployments
- **Telecom, Media, Finance, Transport Sectors in France**: Enterprise VPN concentrators used by critical infrastructure operators  
  **Platform**: Hybrid hardware / virtual gateway environments

## Attack Vectors and Techniques

- **Unauthenticated Remote Command Execution**  
  - **Vector**: Direct exploitation of the zero-day flaw via crafted HTTPS requests to the VPN appliance’s web interface, bypassing authentication and triggering OS-level commands.
- **Credential Harvesting & Session Hijacking**  
  - **Vector**: Post-exploitation interception of VPN sessions and scraping of cached credentials/pass-through authentication tokens.
- **Self-Patching / Turf-Control**  
  - **Vector**: After gaining root access, the threat actor uploads a patched binary that closes the exploited flaw, preventing competing intrusions while maintaining their own backdoor.
- **Lateral Movement via VPN Pivot**  
  - **Vector**: Leveraging compromised appliance trust to access internal subnets, RDP/SMB shares, and administrative interfaces.

## Threat Actor Activities

- **Actor/Group**: Unnamed China-aligned Advanced Persistent Threat (APT) and an affiliated Initial Access Broker  
  - **Activities**:  
    • Coordinated exploitation of Ivanti zero-days against French government and critical-sector targets  
    • Deployment of custom payloads for persistence and data exfiltration  
    • Post- compromise “self-patching” to monopolize access and sell footholds to downstream ransomware or espionage crews
- **Campaign**: Ongoing 2025 operation targeting Western European organizations  
  - **Impacts**: Government data theft, industrial espionage, and potential staging for disruptive follow-on attacks against telecom and transport infrastructure