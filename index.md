# Exploitation Report

Multiple high-impact, in-the-wild exploitation campaigns are converging on enterprise collaboration platforms, e-commerce frameworks, container infrastructure, and software-supply-chain components.  A trio of Microsoft SharePoint zero-days are being weaponized by several Chinese nation-state groups and have already enabled breaches of sensitive U.S. government networks, including the National Nuclear Security Administration.  Separately, the “Mimo” threat actor has shifted from Craft CMS to Magento deployments and open Docker daemons to deliver cryptominers and proxyware, while a compromise of the popular NPM package “is” planted a backdoor across millions of developer workstations.  These events underscore the urgency of rapid patching, hardened configurations, and vigilant supply-chain security.

## Active Exploitation Details

### Microsoft SharePoint Zero-Day Chain  
- **Description**: Three previously unknown SharePoint flaws that allow authenticated or chained unauthenticated attackers to achieve code execution and lateral movement across SharePoint farms.  
- **Impact**: Full takeover of SharePoint servers, data exfiltration, and pivoting into internal networks—confirmed intrusion into U.S. federal agencies.  
- **Status**: Actively exploited; Microsoft has issued patches and published mitigation guidance.  

### Magento CMS Remote Code Execution (Leveraged by “Mimo”)  
- **Description**: A template-injection vulnerability in Magento enabling arbitrary PHP execution when specially crafted payloads are submitted through web requests.  
- **Impact**: Attackers deploy XMRig miners and proxyware, monetize server resources, and can embed skimmers to harvest payment data.  
- **Status**: Exploitation ongoing; Adobe has released security updates for supported Magento/Adobe Commerce versions.  

### Misconfigured Docker Daemon API Exposure  
- **Description**: Internet-exposed Docker Engine APIs without authentication allow creation of rogue containers with elevated privileges.  
- **Impact**: Deployment of malicious containers running cryptominers or proxy tunnels; full host compromise possible via “--privileged” flag abuse.  
- **Status**: Active exploitation; no patch (configuration issue). Administrators must restrict API exposure and enforce TLS/authN.  

### NPM Package “is” Supply-Chain Backdoor  
- **Description**: The legitimate NPM library “is” (2.8 M weekly downloads) was hijacked and updated with obfuscated malware that executes post-install scripts to open reverse shells.  
- **Impact**: Compromised developer endpoints, credential theft, lateral movement into CI/CD pipelines, and potential insertion of malicious code into dependent applications.  
- **Status**: Malicious versions have been removed; developers must audit dependency trees and rotate credentials.  

### Craft CMS Prior Vulnerability Re-used in New Campaigns  
- **Description**: Legacy remote-code-execution flaw in Craft CMS previously abused by “Mimo,” still exploited on unpatched sites as the actor pivots to new targets.  
- **Impact**: Server hijacking for cryptomining infrastructure and staging of further attacks.  
- **Status**: Patch long available; exploitation continues against unmaintained instances.  

### SharePoint Human-Resource Protocol Abuse (Password-Reset Social Engineering)  
- **Description**: Help-desk identity-verification weakness exploited to reset a privileged employee password at Cognizant, enabling a large-scale ransomware attack on Clorox.  
- **Impact**: Initial access followed by disruptive ransomware, costing $380 M in damages.  
- **Status**: Process weakness; organizations must harden verification procedures and deploy MFA.  

## Affected Systems and Products

- **Microsoft SharePoint**: SharePoint Server 2019, Subscription Edition; Online tenants with on-prem hybrid connectors  
- **National Nuclear Security Administration (NNSA) Networks**: SharePoint-integrated systems within federal enclave  
- **Magento / Adobe Commerce**: All 2.x branches prior to the latest July 2025 security cumulative update  
- **Docker Engine**: Community and Enterprise editions with unauthenticated TCP API exposed (ports 2375/2376)  
- **NPM Package Ecosystem**: Projects directly or transitively importing the “is” library versions pushed during the compromise window  
- **Craft CMS**: Sites running outdated 4.x and earlier releases lacking the vendor-provided RCE patch  
- **Cognizant Help-Desk Workflow**: Password-reset procedures impacting Clorox’s Active Directory and M365 tenants  

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Weaponized SharePoint requests chaining multiple unpublished flaws for authenticated RCE.  
- **Template Injection**: Malformed Magento theme components trigger server-side PHP execution.  
- **Container API Abuse**: Remote creation of “--privileged” Docker containers via exposed REST endpoints.  
- **Software Supply-Chain Poisoning**: Malicious NPM release delivering post-install reverse-shell payloads.  
- **Phishing & Spoofing**: Fake Department of Education G5 portal harvesting credentials through look-alike domains and cloned UX.  
- **Help-Desk Social Engineering**: Voice phishing to bypass identity verification and initiate password resets.  

## Threat Actor Activities

- **Chinese Nation-State Clusters**  
  - **Campaign**: Coordinated espionage exploiting SharePoint zero-days to breach U.S. critical-infrastructure and government entities, exfiltrating sensitive documents.  

- **Threat Actor “Mimo”**  
  - **Campaign**: Pivot from Craft CMS to Magento and Docker targets; installs XMRig miners, “Proxyware” to monetize bandwidth, and persistence via crontab modifications.  

- **Unknown Supply-Chain Attacker**  
  - **Campaign**: Hijack of NPM package “is”; aimed at widespread developer compromise and downstream infiltration of SaaS platforms.  

- **Education-Themed Phishing Operators**  
  - **Campaign**: Ongoing credential-harvesting operation against academic grant applicants through cloned Department of Education portals.  

- **Clorox Intrusion Actors**  
  - **Campaign**: Social-engineering of Cognizant help desk followed by ransomware deployment; leveraged newly reset credentials for privileged access.  

---

Stay vigilant: prioritize SharePoint patch deployment, audit public Docker APIs, update Magento instances, scrutinize NPM dependencies, and reinforce human-centric security controls.