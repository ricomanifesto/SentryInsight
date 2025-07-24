# Exploitation Report

Over the past week, defenders have grappled with multiple, simultaneously active exploitation waves.  Chinese state-aligned groups are abusing recently disclosed Microsoft SharePoint zero-days to compromise U.S. government networks (including a nuclear agency), while separate Chinese operators continue to leverage months-old Ivanti Connect Secure remote-code-execution bugs that many organizations still have not fully remediated.  A financially motivated actor dubbed “Mimo” has shifted from CraftCMS to Magento and exposed Docker APIs to drop crypto-miners, and the newly observed “Coyote” banking trojan is abusing the Windows UI Automation framework in dozens of attacks against Brazilian financial institutions.  Taken together, the campaigns underline how quickly zero-days are operationalized, how long patched flaws remain useful to attackers, and how novel abuse of legitimate features can bypass traditional defenses.

## Active Exploitation Details

### Ivanti Connect Secure / Ivanti Policy Secure RCE Vulnerabilities
- **Description**: Chain of remote-code-execution flaws in the Ivanti Secure VPN appliances that allow unauthenticated attackers to bypass authentication, inject commands, and take full control of gateways.  
- **Impact**: Complete device takeover, credential theft, lateral movement into internal networks, and installation of webshells for persistent access.  
- **Status**: Widely exploited in the wild for at least six months; official patches and mitigation guidance are available, yet many appliances remain unpatched or incompletely remediated, especially in Japan.  

### Microsoft SharePoint Server Zero-Day Trio
- **Description**: Three distinct zero-day vulnerabilities in Microsoft SharePoint enabling authentication bypass, privilege escalation, and remote code execution when specially crafted requests are sent to vulnerable servers.  
- **Impact**: Attackers can execute arbitrary code under the SharePoint service account, exfiltrate sensitive documents, pivot internally, and gain long-term footholds.  The flaws have been weaponized in espionage campaigns.  
- **Status**: Microsoft has released fixes for two of the three vulnerabilities; the third received temporary mitigations while a final patch is prepared.  Active exploitation by at least three Chinese nation-state actors is confirmed.  

### Magento CMS Remote Code Execution Vulnerability
- **Description**: A server-side vulnerability in Magento’s template processing that allows attackers to run arbitrary PHP code through crafted payloads sent to vulnerable endpoints.  
- **Impact**: Full compromise of e-commerce sites, card-skimming injection, crypto-mining installation, and resale of database contents.  
- **Status**: Exploited in the wild by the “Mimo” threat actor; patches exist, but many Internet-facing Magento instances remain outdated.  

### Docker Remote API Exposure (Misconfiguration)
- **Description**: Docker daemons left exposed on TCP/2375 or 2376 without authentication let remote attackers deploy malicious containers.  
- **Impact**: Deployment of cryptocurrency miners and proxyware containers, resource hijacking, internal network pivoting, and possible host escape attempts.  
- **Status**: No vendor patch required (design is secure when properly configured); exploitation continues against misconfigured hosts.  

### Windows UI Automation Abuse (Coyote Trojan)
- **Description**: The Coyote banking trojan weaponizes the Windows UI Automation (UIA) framework to interact with banking websites invisibly, bypassing traditional web-injection defenses.  
- **Impact**: Automated theft of banking and cryptocurrency credentials, unauthorized fund transfers, and account takeover.  
- **Status**: Actively used in targeted campaigns across Brazil; no software vulnerability is patched because the attack abuses a legitimate Windows feature.  Mitigations rely on behavioral detection and hardening of endpoint protections.  

## Affected Systems and Products

- **Ivanti Connect Secure / Policy Secure VPN Gateways**: Versions prior to the January and subsequent cumulative security fixes  
- **Microsoft SharePoint Server**: On-prem 2019, Subscription Edition, and selected builds integrated with hybrid Microsoft 365 environments  
- **Magento CMS (Adobe Commerce)**: Self-hosted installations running outdated versions lacking the most recent security bundle  
- **Docker Engine**: Linux and Windows hosts with the Docker Remote API exposed over TCP without TLS or authentication  
- **Windows 10/11 Endpoints**: Systems targeted by the Coyote trojan, particularly those used to access Brazilian banking and crypto-exchange portals  

## Attack Vectors and Techniques

- **VPN Appliance Exploitation**: Unauthenticated HTTP requests chain authentication bypass with command injection to implant webshells on Ivanti gateways.  
- **Malicious SharePoint Requests**: Crafted SOAP/REST calls exploit auth bypass and RCE zero-days, followed by payload drop and privilege escalation.  
- **Template Injection (Magento)**: Attacker-controlled parameters in Magento’s template engine produce server-side PHP execution.  
- **Exposed Docker API Abuse**: Remote `docker run` commands pull attacker-created images, initiating crypto-mining and proxy-sharing processes.  
- **UI Automation Hijacking**: Malware scripts interact with banking application UI elements to perform hidden clicks and data entry, evading browser hooks.  

## Threat Actor Activities

- **Chinese State-Aligned Groups (Unnamed in reporting)**  
  - **Campaign**: Coordinated exploitation of the three SharePoint zero-days to compromise U.S. government (including a nuclear agency) and other Western targets for cyber-espionage.  

- **Chinese APT Targeting Japan (continuation of prior activity)**  
  - **Campaign**: Persistent exploitation of Ivanti Connect Secure RCE flaws to access Japanese corporate and government networks, followed by credential harvesting and lateral movement.  

- **Threat Actor “Mimo”**  
  - **Campaign**: Shifted focus from CraftCMS to Magento and misconfigured Docker hosts; deploys XMRig miners and proxyware, monetizing both CPU cycles and network bandwidth.  

- **Coyote Banking Trojan Operators**  
  - **Campaign**: Dozens of attacks against Brazilian banks and cryptocurrency exchanges; leverages spear-phishing and malicious installers to deliver the trojan that abuses Windows UI Automation for covert transactions.  

