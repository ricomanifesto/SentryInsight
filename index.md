# Exploitation Report

A surge of real-world exploitation is centered on Microsoft SharePoint zero-days, supply-chain abuse in the JavaScript ecosystem, and opportunistic attacks on web-application and container infrastructures. Government networks – including the U.S. National Nuclear Security Administration – were breached via an unpatched SharePoint vulnerability chain, while threat actor “Mimo” pivoted from Craft CMS to Magento and exposed Docker APIs to deploy cryptominers and proxyware. Simultaneously, the compromise of the hugely popular NPM package `is` highlights the growing risk of developer-focused supply-chain attacks. These campaigns illustrate a broad spectrum of attack surfaces: on-prem collaboration platforms, e-commerce software, container orchestration, and development pipelines.

## Active Exploitation Details

### Microsoft SharePoint Server Zero-Day Chain  
- **Description**: A pair of previously unknown SharePoint Server vulnerabilities being chained for initial access and privilege escalation. Attackers weaponize specially crafted HTTP requests to execute code or elevate privileges within SharePoint farms.  
- **Impact**: Full takeover of SharePoint sites, lateral movement into internal networks, and exfiltration of sensitive government data (confirmed breach of the National Nuclear Security Administration).  
- **Status**: At least one flaw has been patched; another remains under investigation with mitigations issued. Exploitation is ongoing in the wild.

### Magento CMS Remote-Code Execution (RCE) Exploit – “Mimo” Campaign  
- **Description**: Web-template and deserialization flaws in Magento CMS allow unauthenticated attackers to execute arbitrary PHP code. The “Mimo” threat actor uses automated scanners to identify outdated Magento instances.  
- **Impact**: Deployment of XMRig-based cryptominers, installation of proxyware for bandwidth resale, and footholds for additional payloads.  
- **Status**: Active exploitation; official patches exist but many Internet-facing stores remain unpatched.

### Docker API Exposure / Misconfiguration Abuse  
- **Description**: Unauthenticated or weakly authenticated Docker Engine APIs exposed to the Internet let attackers create rogue containers. “Mimo” spins up privileged containers that mount the host filesystem.  
- **Impact**: Host compromise, resource hijacking for cryptocurrency mining, proxy network enrollment, and possibility of lateral movement to neighboring hosts.  
- **Status**: No vendor patch required; remediation involves hardening (binding to localhost, enabling TLS, access-controls).

### Compromised NPM Package `is` (Supply-Chain Backdoor)  
- **Description**: The legitimate NPM package `is` (≈2.8 million weekly downloads) was hijacked and updated with malicious post-install scripts that download and execute obfuscated binaries.  
- **Impact**: Remote code execution on developer workstations, CI/CD servers, and production Node.js environments, granting attackers full device access and potential credential theft.  
- **Status**: Malicious versions were removed; developers must audit dependency trees and force-upgrade to a clean release.

### Craft CMS Exploitation (Legacy, Still Observed)  
- **Description**: Legacy template-injection flaws in Craft CMS continue to be scanned and exploited by the same “Mimo” actor now focusing on Magento.  
- **Impact**: Website defacement, cryptominer deployment, data theft.  
- **Status**: Patches available; exploitation persists against unmaintained sites.

### Kerberoasting Weakness in Active Directory  
- **Description**: Abuse of Kerberos service ticket encryption (RC4-HMAC) lets attackers request Service Principal Name (SPN) tickets and crack them offline to recover plaintext service-account passwords.  
- **Impact**: Lateral movement and privilege escalation inside Windows domains without generating noisy on-host alerts.  
- **Status**: Enduring technique; mitigations (AES-only tickets, strong passwords) recommended.

### Help-Desk Identity Verification Bypass (Clorox Breach)  
- **Description**: Attackers socially engineered Cognizant’s help desk into resetting a Clorox employee’s credentials without proper identity validation.  
- **Impact**: Initial foothold that led to a $380 million business disruption.  
- **Status**: No software patch; procedural controls and MFA enforcement required.

## Affected Systems and Products

- **Microsoft SharePoint Server 2016 / 2019 / Subscription Edition**  
  Platform: On-prem Windows Server environments, including federal networks.

- **Adobe Magento Open Source & Adobe Commerce (out-of-date instances)**  
  Platform: Linux/Unix web servers running PHP.

- **Docker Engine & Docker Desktop with exposed REST API (TCP 2375/2376)**  
  Platform: Linux, Windows, Cloud VMs.

- **Craft CMS versions prior to latest security release**  
  Platform: PHP-based CMS on Linux.

- **NPM package `is` (compromised versions)**  
  Platform: Node.js ecosystems – developer workstations, CI/CD, production servers.

- **Active Directory domains using RC4-encrypted Kerberos tickets and weak SPN passwords**  
  Platform: Windows Server.

## Attack Vectors and Techniques

- **Zero-Day Exploitation (SharePoint)**  
  Vector: Malicious HTTP requests to vulnerable SharePoint endpoints chain RCE and privilege escalation.

- **Web-Application RCE (Magento / Craft CMS)**  
  Vector: Unsanitized template injection and deserialization payloads delivered via public URL parameters.

- **Container API Hijacking (Docker)**  
  Vector: Unauthenticated calls to exposed Docker APIs to create privileged containers running cryptominers.

- **Supply-Chain Poisoning (NPM)**  
  Vector: Malicious post-install scripts executed automatically during `npm install`.

- **Kerberoasting**  
  Vector: LDAP enumeration of SPNs followed by offline cracking of service tickets.

- **Social Engineering / Help-Desk Impersonation**  
  Vector: Telephone or chat requests persuading support staff to reset credentials without MFA or secondary verification.

## Threat Actor Activities

- **Unknown Nation-State Actors (attributed to Chinese groups by Microsoft)**  
  Campaign: Targeted exploitation of SharePoint zero-days; confirmed intrusion into U.S. critical infrastructure (NNSA).

- **“Mimo” Threat Actor**  
  Campaign: Mass-scanning Magento sites and misconfigured Docker hosts; deployment of XMRig miners and proxyware since pivoting from Craft CMS.

- **Unidentified Supply-Chain Actor(s)**  
  Campaign: Compromised NPM package `is`, distributing backdoor malware through trusted open-source channels.

- **Unidentified Actors in Clorox Intrusion**  
  Campaign: Social-engineering Cognizant help desk, leading to major ransomware/business-disruption at Clorox.

