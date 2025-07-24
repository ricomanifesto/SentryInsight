# Exploitation Report

A surge in large-scale exploitation campaigns is being observed across multiple enterprise-grade platforms. The most critical activity centers on three new Microsoft SharePoint zero-day flaws that have already enabled the compromise of a U.S. nuclear-research agency and other government targets. Simultaneously, legacy ― yet still unpatched ― Ivanti Connect Secure/VPN vulnerabilities continue to grant Chinese operators footholds inside Japanese networks six months after fixes were published. On the web-application front, attackers are covertly planting backdoors in WordPress “mu-plugins,” while the financially motivated group “Mimo” has pivoted from Craft CMS to vulnerable Magento sites and poorly secured Docker hosts to deliver crypto-miners and proxyware. Collectively, these campaigns underscore the urgency of rapid patching, hardening of cloud/container environments, and continuous monitoring for post-exploitation persistence mechanisms.  

## Active Exploitation Details

### WordPress Mu-Plugin Stealth Backdoor  
- **Description**: Threat actors upload a malicious “must-use” plugin that auto-executes on every page load, granting administrator-level capabilities and remote command execution. The backdoor is obfuscated to evade standard plugin listings and security scanners.  
- **Impact**: Full site takeover, database exfiltration, malware distribution, and use of the site as a launchpad for further attacks.  
- **Status**: Actively deployed in the wild; no vendor patch required (abuse is post-compromise), but file-system hardening and integrity monitoring are advised.  

### Ivanti Gateway Remote Code Execution Bugs  
- **Description**: Long-standing RCE vulnerabilities in Ivanti Connect Secure and Policy Secure gateways allow unauthenticated attackers to chain path traversal with command-injection to execute arbitrary code.  
- **Impact**: Device takeover, session hijacking, credential theft, and lateral movement into internal networks.  
- **Status**: Patches were released six months ago yet exploitation remains widespread due to complex upgrade paths and appliance downtime concerns.  

### Microsoft SharePoint Zero-Day Trio  
- **Description**: Three previously unknown SharePoint flaws enable authenticated and, in some attack chains, unauthenticated adversaries to perform RCE and privilege escalation. Microsoft attributes exploitation to multiple Chinese nation-state groups.  
- **Impact**: Initial access into on-prem and hybrid SharePoint environments, theft of sensitive data, deployment of web shells, and cross-tenant lateral movement into Microsoft 365.  
- **Status**: Emergency patches issued; exploitation remains ongoing against unpatched servers.  

### Magento CMS Vulnerability Leveraged by “Mimo”  
- **Description**: The attacker exploits a server-side template injection weakness in outdated Magento instances to upload a PHP web shell and execute miner payloads.  
- **Impact**: CPU-consuming crypto-mining, installation of proxyware for traffic resale, and risk of follow-on ransomware.  
- **Status**: Active exploitation; admin upgrade to latest Magento build and removal of obsolete extensions recommended.  

### Docker Daemon Misconfiguration Abuse  
- **Description**: “Mimo” scans for Docker daemons exposed with TCP remote API or weak TLS settings, then creates rogue containers that run Monero miners and proxy services.  
- **Impact**: Resource hijacking, potential container escape, and insertion of the host into a criminal proxy network.  
- **Status**: Ongoing; mitigation involves disabling unauthenticated remote APIs, enforcing TLS mutual auth, and using firewall policies.  

## Affected Systems and Products

- **WordPress Sites**: Any version where attackers gain write access to the /wp-content/mu-plugins/ directory  
- **Ivanti Connect Secure / Policy Secure**: Unpatched gateway firmware versions prior to the January 2025 security update  
- **Microsoft SharePoint**: On-prem versions 2019, Subscription Edition, and hybrid deployments lacking July 2025 cumulative updates  
- **Magento Commerce / Open Source**: Instances running outdated plugins or core versions prior to the latest 2.4.x security bundle  
- **Docker Engine Hosts**: Linux servers exposing the Docker TCP API (port 2375/2376) without proper authentication  

## Attack Vectors and Techniques

- **Malicious Mu-Plugin Drop-In**  
  - **Vector**: Upload via compromised admin credentials or vulnerable third-party plugin, followed by silent activation in the mu-plugins folder.  

- **Chained Ivanti Path Traversal & Command Injection**  
  - **Vector**: Crafted HTTP requests traverse directories to access internal scripts, then inject system-level commands.  

- **SharePoint Web Shell Deployment**  
  - **Vector**: Exploit zero-day to gain server-side execution, write aspx web shells to the _layouts or _catalogs directory.  

- **Server-Side Template Injection (SSTI) in Magento**  
  - **Vector**: Malformed template parameters evaluate arbitrary PHP within the Magento runtime.  

- **Abuse of Exposed Docker Remote API**  
  - **Vector**: Unauthorized ‘docker run’ command creates containers that pull mining images from attacker-controlled registries.  

## Threat Actor Activities

- **Unknown WordPress Intrusion Set**  
  - **Campaign**: Large-scale compromise of blogs and e-commerce sites to maintain persistent admin access and facilitate SEO spam.  

- **Chinese APT Clusters (Three distinct groups)**  
  - **Campaign**: Coordinated exploitation of SharePoint zero-days against government, nuclear-research, and defense contractors for espionage.  

- **Chinese Threat Operators (Ivanti)**  
  - **Campaign**: Continued harvesting of Japanese corporate and governmental networks leveraging unpatched Ivanti gateways.  

- **“Mimo” Threat Actor**  
  - **Campaign**: Monetization-focused attacks shifting from Craft CMS to Magento and Docker, aiming to deploy crypto-miners and proxyware for illicit revenue streams.  

