# Exploitation Report

A coordinated wave of attacks is leveraging multiple zero-day vulnerabilities in Ivanti Connect Secure (ICS) and Policy Secure gateway appliances, providing Chinese-linked adversaries and an identified initial-access broker with full device takeover, credential harvesting, and sustained network footholds across French government agencies, telecom firms, media, finance, and transport sectors. Attackers are chaining an authentication-bypass flaw with a remote command-execution flaw, quickly moving to implant web shells, harvest session cookies, and even “self-patch” appliances to lock out competing threat actors while maintaining persistence. Emergency mitigations and vendor hotfixes are available, but widespread scanning and exploitation continue in the wild.

## Active Exploitation Details

### Ivanti Connect Secure / Policy Secure Authentication-Bypass Zero-Day
- **Description**: A flaw in the authentication logic of ICS and Policy Secure gateways allows remote, unauthenticated attackers to craft specially crafted HTTP requests that bypass login controls and gain administrative access.  
- **Impact**: Full administrative access to the VPN appliance, exposure of configuration files, credential theft, session hijacking, and lateral movement into internal networks.  
- **Status**: Actively exploited by Chinese state-aligned actors and an initial-access broker. Ivanti has released emergency hotfixes and mitigation guidance; patching is strongly urged.  

### Ivanti Connect Secure / Policy Secure Command-Injection Zero-Day
- **Description**: Post-authentication command-injection vulnerability that lets attackers execute arbitrary commands on the underlying OS once an initial foothold is obtained (often via the authentication-bypass flaw).  
- **Impact**: Remote code execution as root on the appliance, installation of web shells, creation of backdoor accounts, and deployment of custom patches that prevent other adversaries from exploiting the same flaw.  
- **Status**: Confirmed in-the-wild exploitation. Ivanti has issued hotfixes; administrators must apply patches or implement the vendor-supplied XML mitigation file immediately.  

## Affected Systems and Products

- **Ivanti Connect Secure (formerly Pulse Secure VPN)**: All supported hardware and virtual appliances prior to the July 2025 emergency hotfix build.  
- **Ivanti Policy Secure**: All versions sharing the vulnerable code base with ICS.  
- **Government and Critical Infrastructure Networks (France)**: Agencies in governmental, telecom, finance, media, and transport sectors confirmed compromised.  
- **Enterprise Environments Worldwide**: Any organization exposing vulnerable ICS/Policy Secure gateways to the Internet.  

## Attack Vectors and Techniques

- **Chained Zero-Day Exploitation**  
  - **Vector**: Remote attackers send crafted HTTP/HTTPS requests to public-facing VPN portals, first triggering the authentication-bypass flaw and then the command-injection to gain root shell access.  

- **Web-Shell Implantation & Session Hijacking**  
  - **Vector**: After code execution, attackers deploy bespoke web shells in appliance file systems and harvest active VPN session cookies to pivot inside networks without valid credentials.  

- **Self-Patching / Turf-Control**  
  - **Vector**: An initial-access broker exploits the zero-days, then installs unofficial patches to close the same vulnerabilities, effectively monopolizing access and blocking rival threat actors and incident responders.  

## Threat Actor Activities

- **Actor/Group**: Unnamed China-nexus Advanced Persistent Threat  
  - **Campaign**: Targeted French government and critical infrastructure networks, using ICS zero-days for initial compromise, followed by data exfiltration and persistent access.  

- **Actor/Group**: Unidentified Initial Access Broker (IAB)  
  - **Campaign**: Mass-exploitation of global ICS deployments, harvesting credentials and selling footholds on dark-web marketplaces; observed “self-patching” appliances post-intrusion to retain exclusive control.

