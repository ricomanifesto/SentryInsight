# Exploitation Report

Over the last week threat hunters observed a sharp rise in real-world exploitation of critical vulnerabilities across Microsoft, open-source security tooling, and AI productivity platforms. The most urgent activity involves Stealth Falcon’s weaponization of an unpatched Windows WebDAV remote code-execution flaw, Mirai botnet operators mass-exploiting a newly disclosed Wazuh platform weakness hours after public release, and the discovery of “EchoLeak,” the first documented zero-click data-exfiltration technique targeting Microsoft 365 Copilot. In parallel, active Secure Boot bypass attacks leveraging a bootkit-related flaw continue despite Microsoft’s recent out-of-band patch. Organizations should prioritize mitigations, monitoring, and patch deployment for the vulnerabilities detailed below.

## Active Exploitation Details

### Windows WebDAV Remote Code Execution Zero-Day
- **Description**: A logic flaw in the Windows WebDAV service allows a malicious server to trigger arbitrary code execution on a client system when the victim accesses a crafted WebDAV share.
- **Impact**: Full compromise of Windows endpoints, malware deployment, and lateral movement inside the victim network.
- **Status**: Actively exploited in the wild by Stealth Falcon since March 2025; Microsoft has not yet issued a permanent fix but mitigations are circulating.

### EchoLeak Zero-Click AI Data-Exfiltration Vulnerability (Microsoft 365 Copilot)  
- **Description**: “EchoLeak” abuses the Copilot context window to inject malicious prompts that silently force the AI assistant to stream sensitive tenant data to an attacker-controlled channel—no user interaction required.
- **Impact**: Leakage of emails, documents, Teams chats, and SharePoint content; potential compliance violations and intellectual-property loss.
- **Status**: Proof-of-concept code publicly demonstrated; Microsoft is investigating and has issued interim guidance but no formal patch is available.

### Wazuh Security Platform Injection Flaw Exploited by Mirai Botnets  
- **Description**: An input-validation weakness in the Wazuh API permits unauthenticated command injection via crafted HTTP requests, granting remote shell access.
- **Impact**: Attackers enlist vulnerable servers into Mirai-based DDoS botnets or deploy additional malware.
- **Status**: Patch released by Wazuh; exploitation observed within 24 hours of disclosure as two distinct Mirai campaigns scan and compromise exposed hosts.

### Windows Secure Boot Bypass Used for Bootkit Deployment  
- **Description**: A Secure Boot security feature bypass enables threat actors to load a maliciously signed bootloader during the boot sequence, establishing a persistent bootkit.
- **Impact**: Root-level persistence, evasion of EDR/AV, and the ability to tamper with operating-system security controls before they start.
- **Status**: Exploited in the wild; Microsoft shipped an emergency patch and accompanying revocation list. Administrators must deploy the update and enable revocation to be fully protected.
- **CVE ID**: CVE-2023-24932

## Affected Systems and Products

- **Windows Client & Server**: All supported versions vulnerable to the WebDAV RCE zero-day  
- **Microsoft 365 Copilot**: Tenant-wide exposure across Windows, macOS, and web clients  
- **Wazuh (open-source SIEM/EDR)**: Versions prior to the latest hotfix across Linux deployments  
- **Windows PCs with Secure Boot enabled**: Systems lacking the May 2025 Secure Boot patch and revocation list  

## Attack Vectors and Techniques

- **Malicious WebDAV Share**: Spear-phishing emails or watering-hole sites lure targets into mounting attacker-controlled WebDAV paths that execute code automatically.
- **Zero-Click Prompt Injection**: Crafted system prompts sent through collaborative documents or Teams chats trigger EchoLeak without user awareness.
- **Automated API Exploit Scanning**: Mirai operators mass-scan IPv4 space for vulnerable Wazuh endpoints and deliver command-injection payloads.
- **Bootloader Signature Forgery**: Attackers sign rogue bootloaders that bypass legacy Secure Boot policies to implant bootkits.
- **Brute-Force Credential Stuffing**: 295 coordinated IPs attempt to force Apache Tomcat Manager passwords, emphasizing the need for MFA and network filtering.

## Threat Actor Activities

- **Stealth Falcon (APT)**  
  - Targeting defense and government networks in Turkey, Qatar, Egypt, and Jordan  
  - Delivers malicious links triggering the Windows WebDAV zero-day to establish implants

- **Mirai Botnet Operators**  
  - Running two separate campaigns to compromise Wazuh servers for DDoS horsepower  
  - Rapid weaponization demonstrates shrinking vulnerability-to-exploit timelines

- **Former Black Basta Affiliates**  
  - Using Microsoft Teams phishing and Python loaders to maintain footholds for ransomware deployment; leverage Secure Boot bypass to harden persistence

- **GreyNoise-Observed Cluster**  
  - 295 distinct IP addresses coordinating brute-force attacks on Apache Tomcat Manager interfaces worldwide

- **Fog Ransomware Group**  
  - Combines legitimate monitoring software (Syteca) with open-source pentest tools to evade detection during lateral movement and data staging

Organizations should apply the referenced patches immediately, harden exposed services, and monitor for the listed tactics to reduce risk from ongoing exploitation campaigns.