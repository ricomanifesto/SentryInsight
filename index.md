# Exploitation Report

A coordinated wave of attacks is actively targeting Ivanti Connect Secure / Policy Secure VPN and Neurons for ZTA appliances through multiple zero-day flaws in the Configuration Service (CSA) component. French government agencies, telecom providers, media, finance, and transport organizations have already been compromised, while a China-nexus Initial Access Broker is systematically exploiting the same bugs, even “self-patching” victims’ gateways to lock out competitors. These intrusions grant remote code execution, implant persistent web shells, and enable full network take-over. Urgent patching or interim mitigations are critical.

## Active Exploitation Details

### Ivanti CSA Zero-Day Vulnerabilities
- **Description**: A chain of previously unknown flaws in the Configuration Service Authentication (CSA) module of Ivanti Connect Secure, Ivanti Policy Secure, and Ivanti Neurons for Zero Trust Access allows unauthenticated attackers to gain device-level access and execute arbitrary commands.
- **Impact**:  
  • Remote code execution on VPN gateways  
  • Credential harvesting and session hijacking  
  • Lateral movement into internal networks  
  • Deployment of web shells and backdoors
- **Status**:  
  • Actively exploited in the wild by state-sponsored and criminal actors  
  • Vendor has issued patches and mitigation guidance; systems remain widely unpatched in many environments
- **CVE ID**: *Not provided in the referenced articles*

## Affected Systems and Products

- **Ivanti Connect Secure**: All supported versions prior to the out-of-band July 2025 patches  
- **Ivanti Policy Secure**: Gateway builds using the vulnerable CSA component  
- **Ivanti Neurons for ZTA**: Appliances running the affected CSA module  
- **Platform**: Network-edge VPN and ZTA appliances deployed across on-premises, hybrid, and cloud infrastructures

## Attack Vectors and Techniques

- **Unauthenticated Remote Exploit**  
  • Vector: Direct HTTPS requests to the CSA API endpoints on vulnerable Ivanti gateways  
  • Technique: Crafted requests trigger logic flaws and command injection to obtain root-level shell access  

- **Self-Patching for Turf Control**  
  • Vector: After initial compromise, attackers upload modified CSA binaries or configuration files  
  • Technique: The adversary patches the zero-day on the victim appliance, blocking other threat actors while maintaining their own persistence  

- **Web-Shell Deployment & Persistence**  
  • Vector: File upload or config manipulation via CSA access  
  • Technique: Deploy lightweight web shells that survive reboots and firmware upgrades, enabling long-term foothold  

## Threat Actor Activities

- **Actor/Group**: China-nexus intrusion set (uncategorized)  
  • **Campaign**: Targeted French government, telecom, media, finance, and transport entities  
  • **Activities**: Leveraged Ivanti zero-days for initial compromise, installed backdoors, exfiltrated sensitive data, and pivoted laterally

- **Actor/Group**: Unnamed Initial Access Broker (IAB)  
  • **Campaign**: “Self-Patch” operation for exclusive access  
  • **Activities**: Mass-exploitation of the same Ivanti flaws, followed by on-the-fly patching of victim appliances to prevent other intruders, then selling privileged access on criminal marketplaces

