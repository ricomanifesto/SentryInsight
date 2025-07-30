# Exploitation Report

Over the last week, security researchers tracked coordinated exploitation of a critical command-injection flaw in SAP NetWeaver (CVE-2025-31324), which attackers weaponized to drop the new “Auto-Color” Linux malware inside a U.S. chemicals company. At the same time, ransomware operations such as the rapidly evolving **Gunra** crew expanded to Linux targets, and disruptive intrusions forced the City of Saint Paul to call in the National Guard and grounded more than 60 Aeroflot flights. Parallel campaigns leveraged sophisticated social-engineering—“choicejacking” on mobile devices and large-scale phishing against PyPI maintainers—to steal credentials and gain initial access. The activity underscores growing pressure on enterprise software supply chains and critical-infrastructure providers from both financially-motivated and opportunistic threat actors.

## Active Exploitation Details

### SAP NetWeaver Remote Command Injection Leading to Auto-Color Implant
- **Description**: A critical command-injection vulnerability in SAP NetWeaver’s Internet Communication Manager (ICM) allows unauthenticated attackers to craft specially-formatted HTTP requests that force the underlying OS to execute arbitrary shell commands.  
- **Impact**: Full remote code execution, deployment of persistent malware (Auto-Color), lateral movement across SAP and non-SAP hosts, theft of proprietary data, and potential sabotage of production systems.  
- **Status**: Actively exploited in the wild; SAP has released patches and customers are urged to apply them immediately and monitor for ICM log anomalies.  
- **CVE ID**: CVE-2025-31324  

## Affected Systems and Products

- **SAP NetWeaver Application Server (ICM component)**  
  - **Platform**: On-premises and cloud deployments running on Linux/UNIX and Windows prior to the July 2025 security update  

- **U.S. Chemicals Company (name withheld)**  
  - **Platform**: Hybrid SAP landscape with Linux application servers targeted for Auto-Color malware deployment  

- **Broader SAP Install Base**  
  - **Platform**: Any organization that has not yet applied the vendor patch for CVE-2025-31324  

## Attack Vectors and Techniques

- **HTTP Command Injection (CVE-2025-31324)**  
  - **Vector**: Malformed HTTP requests to the SAP NetWeaver ICM service trigger OS-level shell execution, providing an initial foothold.  

- **Malware Deployment – Auto-Color**  
  - **Vector**: Post-exploitation script fetches and installs a bespoke Linux payload that establishes persistence, exfiltrates environment data, and awaits follow-on commands.  

- **Cross-Platform Ransomware (Gunra Linux Variant)**  
  - **Vector**: Utilises multithreaded file encryption after initial access (credentials, exposed services, or bought access) to accelerate impact on both Windows and Linux servers.  

- **Choicejacking (Mobile Social-Engineering)**  
  - **Vector**: Malicious websites or rogue mobile apps overlay deceptive UI elements atop legitimate system dialogs to hijack user consent, enabling installation of unwanted configuration profiles or spyware.  

- **Supply-Chain Phishing Against PyPI Maintainers**  
  - **Vector**: Look-alike “pypi-verification[.]org” domain sends fake verification emails prompting maintainers to re-authenticate, harvesting credentials and session cookies for package hijacking.  

## Threat Actor Activities

- **Unknown APT/Crimeware Group (SAP Auto-Color Operators)**  
  - **Campaign**: Targeted breach of a U.S. chemicals firm by exploiting CVE-2025-31324; dropped Auto-Color implant, harvested proprietary formulas, and attempted lateral movement into OT networks.  

- **Gunra Ransomware Gang**  
  - **Campaign**: Rolled out a Linux build with multithreaded encryption, aiming at VMware, Hyper-V, and bare-metal servers to broaden ransom reach and disrupt mixed-platform environments.  

- **PyPI Phishing Operators**  
  - **Campaign**: Ongoing credential-harvesting wave impersonating official PyPI staff to compromise developer accounts and inject malicious code into popular Python packages.  

- **Unknown Actors – City of Saint Paul Intrusion**  
  - **Campaign**: Large-scale cyberattack crippled municipal IT systems, prompting National Guard cyber-response teams; initial vector under investigation, ransomware suspected.  

- **Unknown Actors – Aeroflot Disruption**  
  - **Campaign**: Cyberattack on the airline’s IT backbone led to flight cancellations and delays; early indicators suggest network intrusion aimed at operational disruption rather than data theft.  

- **Orange S.A. Incident Response Team**  
  - **Campaign**: Detected and isolated a breached internal system; scope and perpetrators not yet disclosed, but investigation centres on potential credential compromise within supplier access.  

---

Regular, timely patching of SAP NetWeaver, strict network segmentation, and continuous monitoring for anomalous outbound connections remain critical to mitigating the current wave of post-exploitation malware and ransomware activity.