# Exploitation Report

The most urgent exploitation activity observed in the recent news cycle is the active abuse of a critical SAP NetWeaver vulnerability (CVE-2025-31324) to gain pre-authentication remote code execution and implant the newly identified “Auto-Color” Linux malware inside a U.S.-based chemicals company. This single flaw enables full compromise of SAP application servers, a cornerstone of many enterprise resource-planning environments, and is being weaponized in real-world attacks. At the same time, ransomware operators behind the “Gunra” family have introduced a Linux variant, broadening their cross-platform reach, while supply-chain phishing against PyPI maintainers and disruptive cyber-operations hitting municipal and transportation sectors (Saint Paul, Aeroflot, Orange) highlight a rapidly evolving threat landscape.

## Active Exploitation Details

### SAP NetWeaver Pre-Auth Remote Code Execution
- **Description**: A directory-traversal and file-write flaw in SAP NetWeaver Application Server ABAP that allows unauthenticated attackers to upload malicious files and execute arbitrary code on the underlying host.  
- **Impact**: Full system takeover of SAP servers, lateral movement across enterprise networks, and deployment of custom malware (“Auto-Color”) that establishes persistence and exfiltrates data.  
- **Status**: Confirmed in-the-wild exploitation; SAP has issued security patches and customers are urged to apply them immediately.  
- **CVE ID**: CVE-2025-31324  

## Affected Systems and Products

- **SAP NetWeaver Application Server ABAP (AS ABAP)**  
  • Affected Versions: All releases prior to the vendor patch for CVE-2025-31324  
  • Platform: Linux/UNIX and Windows hosts running SAP NetWeaver

- **Enterprise Linux Servers**  
  • Impacted as secondary targets when Auto-Color backdoor is deployed  
  • Platform: Ubuntu, Red Hat, SUSE, and other common server distributions

- **Endpoints Targeted by Gunra Ransomware**  
  • Versions: Windows 10/11, Windows Server 2016-2022, plus new ELF binaries for major Linux distros  
  • Platform: Cross-platform (Windows & Linux) environments

- **PyPI Maintainers & Users**  
  • Scope: Developers receiving fake “account verification” emails  
  • Platform: Any OS accessing the Python Package Index

- **Municipal & Critical Infrastructure Networks**  
  • City of Saint Paul, Minnesota (government IT and public-safety systems)  
  • Platform: Mixed Windows/Linux environments

- **Transportation & Telecom Operators**  
  • Aeroflot airline reservation & flight-operation systems  
  • Orange telecom administrative network  
  • Platform: Highly heterogeneous enterprise stacks

## Attack Vectors and Techniques

- **SAP HTTP Directory Traversal (CVE-2025-31324)**  
  • Vector: Crafted HTTP requests to vulnerable NetWeaver endpoints write a malicious file to the application directory, then trigger execution.  

- **Malware Deployment – “Auto-Color”**  
  • Technique: Post-exploitation payload delivered via the compromised SAP server writes an ELF binary that opens a reverse shell and schedules persistence via cron.

- **Cross-Platform Ransomware (Gunra Linux Variant)**  
  • Technique: Multithreaded encryption routine compiled for ELF; actors pivot from initial Windows foothold to encrypt NFS-mounted Linux shares.

- **Supply-Chain Phishing Against PyPI**  
  • Vector: Look-alike domains (e.g., “pyp1[.]org”) and spoofed “verification” emails harvest credentials, redirecting victims to malicious package repositories.

- **Credential Compromise & Lateral Movement in Municipal Networks**  
  • Technique: Undisclosed exploit or stolen credentials used to disable critical city services, followed by ransomware-style encryption and data exfiltration.

## Threat Actor Activities

- **Unknown Threat Actors Exploiting SAP NetWeaver**  
  • Campaign: Single-stage intrusion delivering Auto-Color malware to a U.S. chemicals firm; focuses on intellectual-property theft and backdoor persistence.

- **Gunra Ransomware Group**  
  • Activities: Released a Linux build, enabling encryption of mixed-OS environments; observed targeting midsize organizations with multithreaded payloads.

- **Phishing Group Targeting PyPI Developers**  
  • Campaign: Ongoing credential-harvesting operation using fake verification emails; aims to poison the software-supply chain with malicious Python packages.

- **Saint Paul Cyberattack Actors**  
  • Activities: Disrupted municipal services, prompting activation of the National Guard; methods point to sophisticated ransomware or wiper operations.

- **Aeroflot Incident Actors**  
  • Activities: Caused cancellation of 60+ flights and extensive delays; attackers penetrated operational IT systems, indicating high operational-technology (OT) awareness.

- **Orange Telecom Attackers**  
  • Activities: Breached internal system; early containment reported, but investigation ongoing to determine scope and data exfiltration.