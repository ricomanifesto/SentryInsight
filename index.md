# Exploitation Report

Ongoing campaigns targeting **Ivanti Connect Secure Appliances** dominate the current exploitation landscape. Multiple China-nexus threat actors – including both state-sponsored groups and an Initial Access Broker (IAB) – are weaponizing a set of zero-day vulnerabilities to gain footholds in government, telecom, finance, media, and transportation networks, primarily in France. After compromising devices, one attacker cluster is even “self-patching” the flaws to monopolize access. These exploits enable full remote code execution, device persistence, and lateral movement inside victim environments, underscoring the urgency of rapid patching or mitigation.

## Active Exploitation Details

### Ivanti Connect Secure Appliance Zero-Day Chain
- **Description**: A group of unauthenticated flaws in Ivanti Connect Secure (ICS) / Policy Secure gateways that allow attackers to bypass authentication, write arbitrary files, and execute commands with elevated privileges directly on the underlying operating system.
- **Impact**: Remote code execution, credential theft, installation of web shells, persistence, and pivoting into internal networks.
- **Status**: Confirmed active exploitation in the wild by Chinese state-sponsored actors and a China-linked IAB; emergency mitigations and patches have been released by Ivanti and urged by national CERTs.
- **CVE ID**: *Not explicitly provided in the referenced articles*

## Affected Systems and Products
- **Ivanti Connect Secure (ICS)**: All vulnerable firmware versions prior to Ivanti’s out-of-band patch
- **Ivanti Policy Secure & Ivanti Neurons for ZTA**: Appliances sharing the same code base and vulnerability set
- **Enterprise Networks**: On-premises or cloud-hosted deployments servicing remote-access VPN for government, telecom, finance, media, and transportation sectors

## Attack Vectors and Techniques
- **Unauthenticated Web Exploitation**
  - **Vector**: Direct HTTPS requests to appliance portals leveraging auth-bypass and command-injection flaws.
- **Web Shell Deployment**
  - **Vector**: After gaining RCE, adversaries drop custom Perl/Python shells to maintain long-term access.
- **Self-Patching (Turf Control)**
  - **Vector**: Initial Access Broker uploads legitimate Ivanti hot-fix packages post-compromise to close the exploited holes, locking out rival attackers and complicating forensic efforts.
- **Credential Theft & Lateral Movement**
  - **Vector**: Extracted session tokens and cached credentials from the appliance are reused to move laterally into internal services (RDP, SMB, AD).

## Threat Actor Activities
- **Chinese State-Sponsored Group**
  - **Campaign**: Coordinated intrusions against French governmental, telecom, finance, media, and transport entities; objective appears to be espionage and long-term access.
- **China-Nexus Initial Access Broker (Unattributed)**
  - **Campaign**: “Self-patching” operations that exploit the Ivanti zero-days, deploy web shells, and then apply vendor hot-fixes to keep exclusive control; access likely sold to downstream ransomware or espionage groups.