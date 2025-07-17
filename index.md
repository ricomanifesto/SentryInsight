# Exploitation Report

Recent threat-hunting investigations highlight a critical exploitation wave against fully-patched SonicWall appliances, where an undisclosed zero-day is delivering the new “Overstep” backdoor in support of ransomware operations believed to be tied to the Abyss group. Concurrently, cyber-criminal operators have rolled out Matanbuchus 3.0, a heavily re-tooled malware loader now propagated through Microsoft Teams chats and enriched with EDR-evasion and DNS-tunneled C2, markedly increasing the success rate of targeted ransomware intrusions. While Oracle has rushed emergency fixes for a critical flaw in its Cloud Code Editor service, no public evidence of in-the-wild abuse is yet available; nonetheless, defenders should apply patches immediately due to the vulnerability’s trivial exploitation path.

## Active Exploitation Details

### SonicWall Zero-Day Leading to “Overstep” Backdoor
- **Description**: An unknown vulnerability in fully up-to-date SonicWall next-generation firewalls and Secure Remote Access (SRA) appliances is being leveraged to gain privileged access and deploy the custom “Overstep” backdoor.  
- **Impact**: Remote code execution on the appliance, network persistence, lateral movement, and eventual ransomware deployment.  
- **Status**: Confirmed in-the-wild exploitation; no public patch. SonicWall has issued temporary hardening steps while the root-cause analysis continues.

### Microsoft Teams Abuse Delivering Matanbuchus 3.0 Loader
- **Description**: Attackers drop weaponized archive files in Microsoft Teams chats, abusing native file-sharing to sidestep secure-email gateways and perimeter defenses. The payload installs Matanbuchus 3.0, which features encrypted DNS-based command-and-control, EDR process discovery, and reflective PE injection.  
- **Impact**: Initial access, payload staging, and seamless handoff to ransomware frameworks or data-stealers.  
- **Status**: Actively observed in multiple targeted enterprise intrusions. No vulnerability patch required (misuse of legitimate functionality); mitigations focus on Teams security policies and attachment controls.

## Affected Systems and Products

- **SonicWall Next-Generation Firewalls & SRA Appliances**  
  - **Platform**: Physical and virtual devices running the latest firmware streams; exploitation reported across enterprise and MSP environments.  

- **Microsoft Teams (Desktop and Web clients)**  
  - **Platform**: Microsoft 365 tenants with default file-sharing permissions; all operating systems hosting Teams.  

## Attack Vectors and Techniques

- **Zero-Day Appliance Exploit**  
  - **Vector**: Direct exploitation of an as-yet-unidentified flaw reachable over HTTPS management or VPN services on SonicWall gear, followed by Overstep backdoor deployment.

- **Malicious Teams File Drop**  
  - **Vector**: Social-engineering of individual users or Teams channels to accept and open weaponized ZIPs/CABs, launching the Matanbuchus 3.0 installer.

- **DNS-Tunneled C2 (Matanbuchus 3.0)**  
  - **Technique**: Encodes beacon traffic within TXT queries to attacker-controlled domains, blending exfiltration into normal DNS noise.

- **EDR-Awareness & Process Injection (Matanbuchus 3.0)**  
  - **Technique**: Scans for >15 common EDR/AV processes; if present, switches to memory-only reflective DLL injection to evade user-mode hooks.

## Threat Actor Activities

- **Abyss Ransomware-Linked Actor**  
  - **Campaign**: Exploiting SonicWall zero-day to install Overstep, harvest domain credentials, and stage double-extortion ransomware payloads against manufacturing and healthcare victims.

- **Matanbuchus 3.0 Operator (“BelialDemon” Affiliate Service)**  
  - **Campaign**: Loader offered as malware-as-a-service (MaaS) to multiple criminal crews; current wave targets professional-services and technology firms via Teams spear-phishing, aiming to monetize access through ransomware partnerships.

- **ShinyHunters**  
  - **Campaign**: Credited with the intrusion that exposed customer data across multiple Louis Vuitton regions; while specific vulnerabilities remain unconfirmed, stolen credentials and dark-web resale activity are ongoing.

- **LockBit-Styled Supply-Chain Actor**  
  - **Campaign**: Breach of UK retailer Co-op leading to personal data theft of 6.5 million members, with signs of ransomware-enabled extortion after lateral movement through third-party systems.

Defenders are urged to apply SonicWall interim mitigations, harden Teams file-sharing policies (e.g., disable external file exchange, enforce Safe Attachments), and expedite Oracle Cloud Infrastructure patch deployments to stay ahead of current exploitation trends.