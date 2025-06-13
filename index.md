# Exploitation Report

The most critical exploitation activity observed this cycle centers on two sophisticated zero-click attack paths and one boot-level compromise that require no user interaction.  Researchers disclosed “EchoLeak,” a prompt-injection technique that silently siphons data from Microsoft 365 Copilot sessions, while forensic analysts tied Paragon’s “Graphite” spyware to an iOS zero-click exploit chain actively deployed against European journalists.  Simultaneously, malware operators continue to abuse a Windows Secure Boot bypass to install UEFI bootkits that survive OS re-installation, prompting Microsoft to rush emergency patches and public guidance.  These three issues collectively threaten cloud productivity suites, mobile devices, and desktop endpoints across all major platforms.

## Active Exploitation Details

### EchoLeak Zero-Click Copilot Prompt-Injection
- **Description**: A logic-flaw in Microsoft 365 Copilot that lets an attacker embed specially crafted “invisible” prompt fragments inside shared documents or emails. When Copilot processes the content in the victim’s context, the hidden prompt causes the LLM to echo sensitive tenant data to a remote channel without any clicks or visible cues.
- **Impact**: Theft of emails, Teams chat content, SharePoint documents, and other M365 tenant data; potential privilege escalation if harvested information is reused for spear-phishing or lateral movement.
- **Status**: Confirmed proof-of-concept exploitation by Aim Security researchers; Microsoft is reportedly working on a mitigation layer but no definitive patch has been released.
  
### iOS Zero-Click Exploit Chain Used by Graphite Spyware
- **Description**: A multi-stage exploit delivered via iMessage that triggers remote code execution and kernel privilege escalation on fully-patched iPhones.  The payload installs Paragon’s “Graphite” spyware, giving operators persistent access and full device surveillance capabilities.
- **Impact**: Complete device takeover, live microphone/camera activation, credential theft, and exfiltration of encrypted messenger content.
- **Status**: Actively deployed against at least two EU-based investigative journalists; Apple has issued security updates closing the exploit path, but un-patched devices remain vulnerable.

### Windows Secure Boot Bypass Leveraged by UEFI Bootkit Malware
- **Description**: A design flaw in the Windows boot chain that allows unsigned or maliciously signed bootloaders to execute before OS security controls. Threat actors weaponize the gap to drop UEFI bootkits that embed themselves in firmware.
- **Impact**: Persistent compromise that survives disk wipes, disables EDR agents, and grants kernel-level control for ransomware or espionage operations.
- **Status**: Exploited in active campaigns; Microsoft pushed an out-of-band update for Windows 11 24H2 and back-ported fixes to supported versions. Systems without the latest Secure Boot DBX revocation remain exposed.

## Affected Systems and Products

- **Microsoft 365 Copilot**: All tenants where Copilot is enabled; affects web, desktop, and mobile clients  
  **Platform**: Microsoft 365 cloud environment  
- **Apple iPhone / iPad**: iOS versions prior to Apple’s latest security update (16.x/17.x lines)  
  **Platform**: iOS / iPadOS mobile ecosystem  
- **Microsoft Windows PCs**: Windows 10, Windows 11, Windows Server editions lacking the most recent Secure Boot patches  
  **Platform**: x86-64 and ARM-based Windows with UEFI firmware  

## Attack Vectors and Techniques

- **Invisible Prompt Injection (EchoLeak)**  
  • **Vector**: Malicious Markdown, HTML, or text snippets embedded in M365 files, emails, or Teams messages automatically parsed by Copilot.

- **Zero-Click iMessage Exploitation (Graphite)**  
  • **Vector**: Specially crafted iMessage attachments that trigger the exploit chain upon receipt, no user action required.

- **UEFI Bootkit Deployment**  
  • **Vector**: Malicious bootloader dropped via spear-phishing, physical access, or chained post-exploitation tools; abuses Secure Boot bypass to execute during system start-up.

## Threat Actor Activities

- **Unattributed Operator Using EchoLeak**  
  • **Campaign**: Proof-of-concept demonstrations show data exfiltration from multiple tenant types; no public attribution yet.

- **Paragon Graphite Operators**  
  • **Campaign**: Targeted surveillance against European journalists; leverages zero-click iMessage payloads to implant Graphite spyware and harvest politically sensitive information.

- **UEFI Bootkit Malware Authors (BlackLotus-style)**  
  • **Campaign**: Ongoing ransomware and espionage operations deploying persistent firmware implants to evade reimaging and EDR detection; broad targeting of enterprise and consumer Windows devices.

