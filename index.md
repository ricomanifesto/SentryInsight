# Exploitation Report

Over the past week, defenders observed a sharp rise in server-side compromise activity, led by the active exploitation of the newly disclosed CrushFTP zero-day (CVE-2025-54309) that grants full administrative control via the product’s web interface. Simultaneously, previously unknown flaws in Ivanti Connect Secure/Policy Secure have been weaponised to deploy the new “MDifyLoader” malware and in-memory Cobalt Strike beacons against remote-access gateways. Supply-chain risks also resurfaced as malicious Arch Linux AUR packages installed the CHAOS RAT on Linux workstations, while nearly 2,000 MCP (“Multi-Capability Processing”) servers were found exposed without any authentication, offering instant takeover to remote actors. Collectively, these campaigns highlight the continued effectiveness of zero-day exploitation, insecure default configurations, and software-repository poisoning, and they are being leveraged by both state-aligned groups (e.g., APT28/“Authentic Antics”) and financially-motivated operators.

---

## Active Exploitation Details

### CrushFTP Web Interface Authentication Bypass  
- **Description**: A logic flaw in CrushFTP’s web interface allows remote, unauthenticated attackers to escalate privileges and obtain full administrative access by abusing crafted HTTP requests.  
- **Impact**: Complete takeover of the file-transfer server, including file exfiltration, user impersonation, and deployment of additional payloads.  
- **Status**: Actively exploited in the wild; hot-fixes and updated builds have been released by the vendor.  
- **CVE ID**: CVE-2025-54309  

### Ivanti Connect Secure / Policy Secure Zero-Day Chain  
- **Description**: Unspecified vulnerabilities in the SSL-VPN and ZTNA gateways permit attackers to execute arbitrary code, inject “MDifyLoader,” and launch in-memory Cobalt Strike beacons. The flaws bypass existing authentication layers and device integrity checks.  
- **Impact**: Remote code execution on perimeter devices, credential theft, lateral movement, and persistent command-and-control.  
- **Status**: Under active exploitation; Ivanti has issued mitigation guidance and is expected to publish permanent patches imminently.  

### Malicious Arch Linux AUR Packages (“CHAOS RAT” Supply-Chain Attack)  
- **Description**: Three community-submitted AUR packages were trojanised to fetch and install the CHAOS remote-access trojan. The packages posed as legitimate utilities but executed post-install scripts that fetched the malware.  
- **Impact**: Backdoor installation, remote command execution, data exfiltration, and potential lateral movement on Linux desktops and servers.  
- **Status**: Packages have been removed from AUR; users must audit systems and replace compromised builds.  

### MCP Server Unauthenticated Access Exposure  
- **Description**: The MCP framework, widely used for “agentic AI” workloads, was deployed by ~2,000 organisations without enabling optional authentication. Any remote party can connect and issue privileged commands.  
- **Impact**: Full administrative control, data theft, workload manipulation, and system destruction.  
- **Status**: Actively abused; no vendor patch required—administrators must enable authentication immediately and rotate secrets.  

---

## Affected Systems and Products

- **CrushFTP (versions 10.x and earlier)**  
  - **Platform**: Windows, macOS, Linux server deployments  

- **Ivanti Connect Secure / Policy Secure gateways (multiple firmware builds)**  
  - **Platform**: Hardware and virtual appliances deployed as SSL-VPN or ZTNA portals  

- **Arch Linux systems installing AUR packages**  
  - **Platform**: Any x86_64 Linux device utilising the affected community repositories  

- **MCP (“Multi-Capability Processing”) servers**  
  - **Platform**: Cloud and on-premise instances running the MCP agentic-AI orchestration stack  

---

## Attack Vectors and Techniques

- **Web-Interface Zero-Day Exploit (CrushFTP)**  
  - **Vector**: Crafted HTTP/HTTPS requests that manipulate session state to obtain admin tokens.  

- **Perimeter-Device Exploitation (Ivanti)**  
  - **Vector**: Direct interaction with exposed management APIs to drop MDifyLoader and spawn in-memory Cobalt Strike payloads.  

- **Supply-Chain Poisoning (Arch Linux AUR)**  
  - **Vector**: Malicious `PKGBUILD` post-install scripts pulling CHAOS RAT from attacker-controlled domains.  

- **Unauthenticated Service Exposure (MCP)**  
  - **Vector**: Remote TCP connections to default MCP ports with no credential challenge, allowing administrative commands.  

- **QR Code MFA Phishing (“PoisonSeed”)**  
  - **Vector**: Social-engineering emails that present a QR code to capture FIDO-based MFA tokens and session cookies.  

---

## Threat Actor Activities

- **Unknown Threat Cluster (CrushFTP)**  
  - **Campaign**: Opportunistic mass scanning and exploitation for server hijacking and potential ransomware staging.  

- **Unidentified Advanced Operator (Ivanti/MDifyLoader)**  
  - **Campaign**: Targeted intrusions against organisations relying on Ivanti appliances, focusing on stealth persistence with in-memory tooling.  

- **AUR Package Threat Actors**  
  - **Campaign**: Supply-chain compromise aimed at Linux developers and enthusiasts, distributing CHAOS RAT for long-term access.  

- **APT28 (Fancy Bear) / “Authentic Antics”**  
  - **Activities**: Microsoft 365 credential harvesting via custom malware; leverages previously stolen tokens to maintain access across government and defence targets.  

- **“PoisonSeed” Phishing Group**  
  - **Activities**: Bypasses FIDO-based MFA using QR-code social-engineering lures, targeting remote workforce users in enterprise environments.  

- **UNG0002**  
  - **Campaign**: Espionage in China, Hong Kong, and Pakistan using malicious LNK files and RATs for data exfiltration and surveillance.  

---

**Defender Recommendations**  
1. Patch CrushFTP to the latest build immediately; rotate administrative credentials.  
2. Apply Ivanti interim mitigations, monitor for MDifyLoader indicators, and schedule appliance firmware updates once available.  
3. Audit Arch Linux endpoints for the removed AUR packages, replace binaries, and hunt for CHAOS RAT artefacts.  
4. Enable and enforce strong authentication on MCP servers; restrict exposure via firewall rules.  
5. Educate users on QR-code MFA phishing, enforce device-bound passkeys, and monitor for anomalous session creations.