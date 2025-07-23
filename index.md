# Exploitation Report

Recent reporting highlights a significant surge in exploitation activity against enterprise collaboration and network-access infrastructure. Chinese state-sponsored groups are chaining newly disclosed Microsoft SharePoint Server vulnerabilities to obtain initial footholds in corporate environments, while threat actors are simultaneously leveraging three critical remote-code-execution flaws in Cisco Identity Services Engine (ISE) to disable network-access controls and pivot deeper into victim networks. Both exploit campaigns are confirmed active in the wild, with vendors having issued patches that organizations must deploy immediately to reduce risk.

## Active Exploitation Details

### Microsoft SharePoint Server Vulnerabilities
- **Description**: A set of newly revealed bugs in on-premises SharePoint Server that allow unauthenticated attackers to bypass authentication, upload malicious files, and ultimately execute arbitrary code under the SharePoint service account.  
- **Impact**: Full compromise of the SharePoint farm, credential theft, web-shell deployment, lateral movement, and persistent access to sensitive corporate data and intellectual property.  
- **Status**: Actively exploited by at least three China-based nation-state groups; security updates have been released by Microsoft and should be applied urgently.  

### Cisco Identity Services Engine (ISE) Critical RCE Flaws
- **Description**: Three maximum-severity vulnerabilities in Cisco ISE that enable remote, unauthenticated attackers to execute commands with root privileges via crafted web or CLI requests.  
- **Impact**: Complete takeover of the ISE appliance, ability to modify or disable network-access policies, harvest user credentials, and pivot into protected segments of the enterprise network.  
- **Status**: Cisco issued patches and public advisories; exploitation has been confirmed in active attacks targeting both enterprise and critical-infrastructure environments.  

## Affected Systems and Products

- **Microsoft SharePoint Server (2016, 2019, Subscription Edition)**  
  - **Platform**: Windows Server installations running on-premises or in self-hosted cloud IaaS

- **Cisco Identity Services Engine (ISE) ≤ 3.x prior to current fixed releases**  
  - **Platform**: Dedicated physical and virtual appliances (Linux-based underlying OS)

## Attack Vectors and Techniques

- **Web-Shell Deployment via SharePoint HTTP Requests**  
  - **Vector**: Malicious HTTP POST requests to vulnerable SharePoint endpoints that bypass authentication checks, allowing file upload and code execution.

- **Remote Command Injection on Cisco ISE**  
  - **Vector**: Specially crafted REST or CLI packets sent to the ISE administrative interface, triggering root-level command execution without valid credentials.

- **Credential Harvesting & Lateral Movement**  
  - **Vector**: Post-exploitation use of harvested NTLM hashes (SharePoint) or TACACS/RADIUS secrets (ISE) to move laterally and escalate privileges.

## Threat Actor Activities

- **Linen Typhoon, Violet Typhoon, and a third unnamed China-based group**  
  - **Campaign**: Coordinated exploitation of vulnerable SharePoint servers since early July; objectives include espionage, intellectual-property theft, and establishing long-term persistence.

- **Unattributed Crimeware Operators**  
  - **Campaign**: Opportunistic scanning for vulnerable Cisco ISE instances, followed by double-extortion ransomware or data-theft operations against compromised organizations.

- **Interlock Ransomware Operators**  
  - **Campaign**: Leveraging compromised network-access devices—including newly exploited ISE appliances—to deploy ransomware payloads and exfiltrate sensitive data for extortion.

---

Organizations running the affected software should prioritize patch deployment, validate that exposed management interfaces are properly segmented, and perform immediate compromise assessments for signs of web shells, unauthorized administrative sessions, or unexpected policy changes.