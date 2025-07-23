# Exploitation Report

The most critical exploitation activity observed this period centers on two enterprise-grade platforms: Cisco Identity Services Engine (ISE) and Microsoft SharePoint Server. Cisco confirmed that attackers are chaining three recently patched remote-code-execution flaws to gain unauthenticated root access on ISE appliances now seen in the wild, while Microsoft attributes ongoing SharePoint intrusions to multiple Chinese state-aligned groups exploiting unpatched internet-facing servers. Concurrently, new campaigns leveraging the Coyote banking trojan highlight an emerging technique that abuses the Windows UI Automation framework to harvest credentials from financial portals. These events underline a renewed focus on identity infrastructure, collaboration portals, and native OS components as high-value entry points for ransomware crews and nation-state actors alike.

## Active Exploitation Details

### Cisco ISE Remote Code Execution Flaws
- **Description**: A trio of critical vulnerabilities in Cisco Identity Services Engine and ISE-PIC allow unauthenticated attackers to upload malicious files and execute code with root privileges via exposed web services and API endpoints.  
- **Impact**: Full compromise of the network-access-control (NAC) appliance, enabling lateral movement, credential theft, and policy manipulation across enterprise environments.  
- **Status**: Actively exploited in the wild; Cisco has released fixed versions and updated its advisory to note confirmed exploitation.  
- **CVE ID**: *Not explicitly provided in the source articles*

### Microsoft SharePoint Server Vulnerabilities
- **Description**: Multiple security flaws in on-premises SharePoint Server instances are being leveraged to achieve arbitrary code execution and privilege escalation. Attackers target servers exposed to the internet without the latest cumulative updates.  
- **Impact**: Remote code execution under the SharePoint service account, leading to data theft, web-shell deployment, and potential domain compromise.  
- **Status**: Exploitation ongoing since early July; patches are available through Microsoft’s regular security releases.  
- **CVE ID**: *Not explicitly provided in the source articles*

### Windows UI Automation Framework Abuse (Coyote Malware)
- **Description**: The newest variant of the Coyote banking trojan hooks Microsoft’s UI Automation accessibility APIs to fingerprint active browser windows, detect visits to banking or cryptocurrency sites, and trigger credential-stealing modules.  
- **Impact**: Real-time theft of banking credentials, session cookies, and potential account takeover for financial fraud.  
- **Status**: Active in the wild; no vendor patch required as the malware abuses legitimate functionality, but Microsoft has issued detection guidance.  

## Affected Systems and Products

- **Cisco Identity Services Engine (ISE)**  
  - Versions prior to the fixed releases specified in Cisco’s July advisory  
  - **Platform**: Appliance-based or virtual ISE deployments in enterprise and critical-infrastructure networks  

- **Cisco ISE Passive Identity Connector (ISE-PIC)**  
  - Companion component vulnerable through the same RCE chain  
  - **Platform**: Windows Server and Linux hosts running ISE-PIC  

- **Microsoft SharePoint Server**  
  - Internet-facing on-prem versions lacking the latest cumulative updates  
  - **Platform**: Windows Server environments (SharePoint 2019, 2016, and earlier still in support)  

- **Windows 10 / Windows 11 Endpoints**  
  - Systems where users interact with online banking and cryptocurrency portals  
  - **Platform**: Desktop and laptop endpoints susceptible to Coyote malware infection  

## Attack Vectors and Techniques

- **Unauthenticated Web Service Exploit (Cisco ISE)**  
  - **Vector**: Crafted HTTP(S) packets to vulnerable ISE REST endpoints upload a malicious tar-archive leading to code execution as root.  

- **SharePoint Pre-Auth Exploit Chain**  
  - **Vector**: Attackers send specially crafted SOAP/REST requests or manipulate ViewState data to bypass authentication and drop web shells.  

- **UI Automation Credential Harvesting (Coyote)**  
  - **Vector**: Malware injects into the browser, leverages UI Automation API calls to enumerate on-screen elements, detect login fields, and exfiltrate entered credentials.  

- **Double-Extortion Ransomware Deployment (Interlock)**  
  - **Vector**: Post-exploitation tools (PowerShell, RDP, Cobalt Strike) combined with data theft prior to encryption for additional leverage.  

## Threat Actor Activities

- **Linen Typhoon, Violet Typhoon, and a third Chinese state-aligned group**  
  - **Campaign**: Coordinated exploitation of SharePoint Server flaws since 7 July, targeting government, energy, and telecom sectors to gain long-term footholds and exfiltrate sensitive data.  

- **Unknown Threat Actors Exploiting Cisco ISE**  
  - **Campaign**: Mass scanning of corporate perimeters for vulnerable ISE appliances followed by rapid deployment of custom payloads achieving root persistence.  

- **Interlock Ransomware Operators**  
  - **Campaign**: Escalating double-extortion attacks on businesses and critical infrastructure, often leveraging compromised identity appliances or unpatched edge services for initial access.  

- **Coyote Malware Distributors**  
  - **Campaign**: Phishing and malicious advertising campaigns aimed at end-users in Latin America and Europe, focusing on financial gain through banking and crypto theft.  

**Bold action is urged**: organizations should apply vendor patches immediately, harden exposure of collaboration/NAC platforms, monitor for abnormal UI Automation API usage, and update detections for Interlock-related ransomware tooling.