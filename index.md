# Exploitation Report

A wave of coordinated intrusions is leveraging two previously unknown vulnerabilities in Ivanti Connect Secure and Policy Secure VPN appliances. The zero-days are being chained to gain unauthenticated access and execute system-level commands, which in turn enables attackers to pivot deeper into government, telecommunications, finance, media, and transport networks across France and other regions. Separate investigations confirm that a China-nexus initial-access broker is not only exploiting the flaws to install backdoors but also “self-patching” the devices to shut out competing threat groups, underscoring both the criticality and sophistication of the ongoing exploitation.

## Active Exploitation Details

### Ivanti Connect Secure / Policy Secure Authentication Bypass Zero-Day
- **Description**: A flaw in the web authentication flow allows remote attackers to craft requests that completely sidestep login controls, providing administrative-level access to the VPN appliance.  
- **Impact**: Unauthenticated attackers can extract configuration data, harvest credentials, and establish persistent footholds that grant wide lateral movement inside corporate and government networks.  
- **Status**: Actively exploited in multiple campaigns; Ivanti has released interim mitigations and subsequently pushed a full security update.  
- **CVE ID**: *not provided in source*  

### Ivanti Connect Secure / Policy Secure Command Injection Zero-Day
- **Description**: Following authentication bypass, adversaries leverage a second vulnerability that permits direct command injection in the underlying operating system, resulting in arbitrary code execution as root.  
- **Impact**: Complete compromise of the appliance, installation of web shells, credential dumping, and the ability to push malware into downstream environments.  
- **Status**: Confirmed in-the-wild exploitation alongside the authentication bypass; a vendor patch is now available, and emergency signatures have been issued by multiple security vendors.  
- **CVE ID**: *not provided in source*  

## Affected Systems and Products

- **Ivanti Connect Secure (formerly Pulse Secure) VPN Appliances**  
  - **Platform**: Hardware and virtual VPN gateways running all supported 22.x and earlier 21.x firmware versions prior to the out-of-band patch.

- **Ivanti Policy Secure Gateways & Ivanti Neurons for ZTA**  
  - **Platform**: On-premises policy-enforcement appliances and corresponding virtual images that share the same vulnerable code base as Connect Secure.

## Attack Vectors and Techniques

- **Auth-Bypass + Command-Injection Chain**  
  - **Vector**: Unauthenticated HTTPS requests to crafted endpoints trigger the bypass, followed by POST requests delivering OS commands in subsequent parameters.

- **Self-Patching (Turf Control)**  
  - **Vector**: After gaining root, the threat actor modifies vulnerable binaries and configuration files to close the holes they exploited, preventing other attackers from entering and hindering defenders’ forensic efforts.

- **Credential & Configuration Exfiltration**  
  - **Vector**: Using built-in system utilities, attackers export VPN configuration archives that contain plaintext passwords, certificates, and session data.

- **Web-Shell Deployment**  
  - **Vector**: Injected commands write custom CGI scripts or dropper binaries to persistent directories, providing long-term remote command execution.

## Threat Actor Activities

- **Actor/Group**: Unnamed China-linked APT (initial access broker)  
  - **Campaign**: Exploits Ivanti zero-days to gain foothold, immediately patches the devices to monopolize access, and then sells or leverages that access for follow-on intrusions.

- **Actor/Group**: Chinese State-Backed Operators (separate operation)  
  - **Campaign**: Targeted French governmental, telecom, media, finance, and transport sectors; deployed custom malware and conducted extensive data collection through the compromised VPN appliances.

- **Actor/Group**: Secondary Opportunistic Threat Actors** (blocked by self-patching)  
  - **Campaign**: Attempts to leverage the same Ivanti flaws were detected but thwarted due to the broker’s turf-control modifications, illustrating active competition among adversaries.

