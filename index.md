# Exploitation Report

Recent intelligence highlights an aggressive campaign in which Chinese-linked threat actors are abusing multiple zero-day vulnerabilities in Ivanti Connect Secure Appliances (CSA) to breach French government, telecom, media, finance, and transport networks. The attackers rapidly weaponize the flaws for initial access, implant web shells, and—remarkably—“self-patch” compromised gateways to monopolize access and block other adversaries. This activity underscores the criticality of edge-device vulnerabilities and the growing sophistication of initial-access brokers working on behalf of APT and ransomware crews.

## Active Exploitation Details

### Ivanti Connect Secure Appliance Zero-Day Vulnerabilities
- **Description**: A cluster of previously unknown flaws in Ivanti CSA VPN gateways allows unauthenticated attackers to bypass authentication and execute arbitrary commands on the underlying OS.
- **Impact**: Full device compromise, enabling credential theft, network pivoting, web-shell deployment, and persistent remote access to internal resources.
- **Status**: Actively exploited in the wild. Ivanti has released emergency mitigations and out-of-band patches; exploitation continues against unpatched or partially mitigated appliances.

## Affected Systems and Products
- **Ivanti Connect Secure / Policy Secure VPN Gateways (CSA)**: All unpatched versions prior to the July 2025 emergency release  
  - **Platform**: Network edge devices deployed in government, telecom, media, finance, and transport environments worldwide

## Attack Vectors and Techniques
- **Zero-Day Auth Bypass & Command Injection**  
  - **Vector**: Crafted HTTP/HTTPS requests to the web-based management interface achieve authentication bypass, followed by command injection against internal scripts to obtain root-level access.
- **Self-Patching by Adversary**  
  - **Vector**: After exploitation, the threat actor uploads a malicious—but functionally corrective—package that closes the same vulnerabilities, preventing rival actors and defenders from re-exploiting the gateway.
- **Web-Shell Implantation**  
  - **Vector**: Post-exploitation, lightweight web shells are placed in legitimate directories, granting persistent backdoor access over HTTPS.

## Threat Actor Activities
- **Actor/Group**: Unnamed China-nexus Advanced Persistent Threat (APT) and associated Initial-Access Broker
  - **Campaign**:  
    - Targeting French government agencies, telecoms, finance, media, and transport sectors  
    - Utilizes Ivanti zero-days for stealthy foothold  
    - Performs “defensive” self-patching of the exploited devices to secure exclusive access  
    - Sells or leverages access for further espionage or ransomware operations  