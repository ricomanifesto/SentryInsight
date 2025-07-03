# Exploitation Report

Chinese state-aligned operators are actively leveraging multiple zero-day vulnerabilities in Ivanti Connect Secure Appliances (CSA) to compromise French government, telecom, finance, media, and transport networks. Concurrently, a new in-the-wild Google Chrome vulnerability is being weaponised to deliver malware before users can patch. These incidents underscore an elevated risk to perimeter VPN infrastructure and ubiquitous client-side software, with threat actors ranging from sophisticated nation-state groups to criminal initial-access brokers racing to obtain footholds and privilege before defenders react.

## Active Exploitation Details

### Ivanti Connect Secure (CSA) Zero-Days
- **Description**: Multiple previously unknown flaws in Ivanti’s VPN/CSA devices allow remote unauthenticated attackers to gain system-level access, pivot internally, and establish persistent tunnels.  
- **Impact**: Full network compromise, credential theft, deployment of further implants, and the ability to self-patch devices to lock out competing actors.  
- **Status**: Confirmed exploitation in the wild by Chinese threat groups; emergency mitigations and patches released.  
- **CVE ID**: *[No CVE IDs explicitly provided in the source articles]*  

### Google Chrome In-the-Wild Vulnerability
- **Description**: A high-severity security hole in the Chrome browser enabling arbitrary code execution following drive-by visits to malicious or compromised sites.  
- **Impact**: Attackers can escape the browser sandbox, implant malware, and steal data under the current user context.  
- **Status**: Actively exploited before disclosure; Google has issued an update for all desktop platforms.  
- **CVE ID**: *[None explicitly provided in the referenced article]*  

### Cisco Unified Communications Manager Static Root Credential Flaw
- **Description**: A hard-coded SSH account with static credentials shipped in Unified CM and Unified CM Session Management Edition, effectively acting as a backdoor.  
- **Impact**: Remote unauthenticated root-level access, allowing takeover of call-processing infrastructure and lateral movement.  
- **Status**: Patched by Cisco; no confirmed exploitation reports yet, but proof-of-concept knowledge is public.  

## Affected Systems and Products

- **Ivanti Connect Secure Appliance (CSA)**  
  - **Platform**: All supported hardware and virtual appliances prior to the emergency security update  
- **Google Chrome Browser**  
  - **Platform**: Windows, macOS, Linux versions prior to the most recent stable channel release  
- **Cisco Unified Communications Manager / Session Management Edition**  
  - **Platform**: On-premises deployments running vulnerable firmware images shipped with static root credentials  

## Attack Vectors and Techniques

- **VPN Zero-Day Exploitation**  
  - **Vector**: Direct HTTPS requests to vulnerable CSA endpoints, chaining logic/command-injection flaws to drop web-shells and modify system packages.  

- **Drive-By Browser Exploit**  
  - **Vector**: Malicious websites or malvertising deliver crafted JavaScript and WebAssembly to trigger the Chrome vulnerability, leading to remote code execution on user machines.  

- **Static Credential Abuse**  
  - **Vector**: Automated scanning for exposed Cisco Unified CM SSH services, followed by login using published hard-coded credentials to obtain root shells.  

## Threat Actor Activities

- **Actor/Group**: Unnamed Chinese state-sponsored intrusion set  
  - **Campaign**: Targeted compromise of French government, telecom, media, finance, and transport organisations via Ivanti CSA zero-days; post-exploitation activities include credential dumping and tunnel creation.  

- **Actor/Group**: China-nexus Initial-Access Broker (IAB)  
  - **Campaign**: Mass exploitation of the same Ivanti zero-days to gain foothold, followed by self-patching appliances to monopolise access and sell it to downstream ransomware affiliates.  

- **Actor/Group**: Crimeware ecosystem (various)  
  - **Campaign**: Rapid incorporation of the new Chrome exploit into malvertising and phishing chains aimed at broad consumer and enterprise audiences, seeking to install info-stealers and loaders.  

- **Actor/Group**: Unknown (potential insider)  
  - **Campaign**: Monitoring of Cisco Unified CM installations for devices that remain unpatched and reachable from the Internet, presumably for future voice-network espionage or toll fraud.  

