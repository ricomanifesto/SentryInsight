# Exploitation Report

A coordinated wave of intrusions is leveraging two previously unknown vulnerabilities in Ivanti Connect Secure (ICS) and Ivanti Policy Secure appliances. Security agencies in France report confirmed compromises across government, telecommunications, media, finance, and transport sectors, while separate research shows a China-linked Initial Access Broker (IAB) abusing the same bugs and then “self-patching” the devices to lock out competitors. The zero-days form an exploit chain that first bypasses authentication and then enables remote code execution (RCE), giving attackers full control of affected VPN gateways and downstream network access.

## Active Exploitation Details

### Ivanti Connect Secure / Policy Secure Authentication Bypass Zero-Day
- **Description**: A flaw in the web component of Ivanti ICS and Policy Secure allows unauthenticated users to craft specially-formed requests that bypass normal login flows.  
- **Impact**: Attackers gain administrative session tokens without credentials, permitting full appliance management and access to VPN session data.  
- **Status**: Actively exploited in France and elsewhere; no official patch at publication time, but Ivanti has issued mitigation guidance and an upcoming hotfix schedule.  

### Ivanti Connect Secure / Policy Secure Remote Code Execution Zero-Day
- **Description**: Following successful authentication bypass, a separate input-validation weakness enables command injection, letting adversaries write files or execute arbitrary code in the underlying OS.  
- **Impact**: Full remote code execution, deployment of web shells, credential harvesting, lateral movement into internal networks.  
- **Status**: Actively chained with the authentication bypass; mitigations available, final patches forthcoming from Ivanti.  

## Affected Systems and Products

- **Ivanti Connect Secure (formerly Pulse Secure VPN) appliances**  
  - **Platform**: Physical and virtual VPN gateways running all supported firmware versions prior to interim mitigations  
- **Ivanti Policy Secure NAC appliances**  
  - **Platform**: On-premises network access control gateways, similar firmware lineage to ICS  

## Attack Vectors and Techniques

- **Chained Zero-Day Exploitation**  
  - **Vector**: External attack surface on HTTPS portal; attacker sends crafted requests to bypass authentication, then executes commands for persistence and lateral movement.  

- **Self-Patching for Turf Control**  
  - **Vector**: After gaining root, the actor applies unofficial patches or disables vulnerable code paths, preventing other threat groups from exploiting the same flaws.  

- **Web-Shell Deployment & Credential Dumping**  
  - **Vector**: Web shells planted in appliance file system; session and credential stores exfiltrated for further intrusion into internal assets.  

## Threat Actor Activities

- **Actor/Group**: Unnamed China-nexus Initial Access Broker  
  - **Campaign**: Uses Ivanti zero-days to obtain footholds, patches devices post-compromise, and sells or uses access for follow-on operations.  

- **Actor/Group**: Chinese State-Backed Intrusion Set (per French CERT disclosure)  
  - **Campaign**: Targeted French government, telecom, media, finance, and transport entities; objectives include espionage and supply-chain positioning.