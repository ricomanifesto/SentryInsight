# Exploitation Report

Over the past week, security researchers have observed a surge in real-world exploitation focused on remote-access infrastructure and collaboration platforms. Chinese state-aligned groups continue to weaponize long-patched Ivanti Connect Secure remote-code-execution flaws against Japanese organizations, while three newly disclosed Microsoft SharePoint zero-days are being chained in espionage operations that breached even U.S. nuclear-sector networks. Concurrently, the threat actor “Mimo” has shifted from Craft CMS to Magento e-commerce sites and misconfigured Docker environments to mass-deploy crypto-miners and proxyware. These campaigns underscore the ongoing risk posed by unpatched perimeter systems, misconfigurations, and quickly weaponized zero-days.

## Active Exploitation Details

### Ivanti Connect Secure / Policy Secure RCE Vulnerabilities
- **Description**: A set of remote-code-execution flaws in Ivanti’s VPN and network-access gateways that allow unauthenticated attackers to execute arbitrary commands on the appliance.
- **Impact**: Full device compromise, credential theft, lateral movement into internal networks, and persistent access for follow-on espionage.
- **Status**: Actively exploited for at least six months after patches were released; many appliances remain unpatched in Japan, enabling continued intrusions by Chinese actors.
  
### Microsoft SharePoint Server Zero-Day Vulnerabilities
- **Description**: Three previously unknown SharePoint flaws used in combination to bypass authentication, elevate privileges, and achieve remote code execution on on-premises SharePoint servers.
- **Impact**: Attackers gain SharePoint farm-level privileges, exfiltrate sensitive documents, implant web shells, and pivot deeper into government and critical-infrastructure networks.
- **Status**: Microsoft has issued security updates; exploitation was observed in the wild before patches became available.

### Magento CMS Remote-Code-Execution Vulnerability
- **Description**: Server-side vulnerability in Magento that allows attackers to upload or modify template files, leading to arbitrary code execution.
- **Impact**: Deployment of crypto-mining malware, proxyware, and further compromise of e-commerce customer data.
- **Status**: Exploitation ongoing; defenders advised to apply latest Magento security patches and disable unnecessary admin endpoints.

### Docker Remote Management Misconfiguration
- **Description**: Exposed or weakly secured Docker APIs and daemon sockets enabling unauthenticated remote container creation.
- **Impact**: Attackers launch privileged containers that run cryptocurrency miners or proxyware, consuming compute resources and offering footholds for additional attacks.
- **Status**: Widespread opportunistic exploitation by the Mimo threat actor; hardening and access-control lists (ACLs) are recommended.

## Affected Systems and Products

- **Ivanti Connect Secure / Ivanti Policy Secure**: Appliances running out-of-date firmware across enterprise and government networks  
- **Microsoft SharePoint Server**: On-prem installations (multiple supported versions) not yet updated with the latest security fixes  
- **Adobe Magento Commerce / Open Source**: Self-hosted Magento 2.x instances lacking current patches  
- **Docker Engine & Docker API**: Linux hosts with remote TCP socket exposed or default configuration left unauthenticated  

## Attack Vectors and Techniques

- **VPN Gateway Exploitation**  
  - **Vector**: Direct HTTPS requests to vulnerable Ivanti endpoints trigger command-injection payloads that download web shells.  

- **SharePoint Auth-Bypass & Web-Shell Implantation**  
  - **Vector**: Crafted SOAP/REST requests exploit authentication logic flaws, followed by privilege-escalation and shell upload.  

- **Magento Template Injection**  
  - **Vector**: Malicious admin requests or abused API keys modify PHTML templates to include PHP backdoors.  

- **Container Hijacking via Exposed Docker API**  
  - **Vector**: Remote attacker connects to port 2375/2376, deploys privileged containers running XMRig miners and proxyware agents.  

## Threat Actor Activities

- **Chinese State-Aligned Groups (Unnamed in reporting)**  
  - **Campaign**: Targeting Japanese organizations by repeatedly exploiting unpatched Ivanti appliances to harvest credentials and conduct long-term espionage.  

- **Multiple Chinese Nation-State Actors (“Storm-xxx” designations)**  
  - **Campaign**: Concurrent exploitation of the three SharePoint zero-days against U.S. federal agencies, including a nuclear-sector entity, to exfiltrate sensitive documents.  

- **Mimo**  
  - **Campaign**: Transitioned from Craft CMS exploitation to a new wave targeting Magento sites and misconfigured Docker hosts to install crypto-miners and commercial proxyware, monetizing compromised infrastructure at scale.  

These incidents highlight the critical importance of timely patching, continuous monitoring of perimeter systems, and rigorous configuration management to reduce the window of exposure to rapidly weaponized vulnerabilities.