# Exploitation Report

Recent reports highlight critical vulnerabilities and exploitation campaigns targeting a broad range of systems and cloud-based products. Notably, attackers are actively exploiting a severe Roundcube webmail flaw that enables remote code execution, while Cisco has warned of a credential vulnerability impacting cloud-hosted Identity Services Engine (ISE) deployments. Researchers have also uncovered attacks leveraging unpatched ConnectWise software and compromised Asus routers. Collectively, these exploits pose high risks and underscore the importance of timely patching and threat awareness across organizations.

## Active Exploitation Details

### Roundcube Critical Remote Code Execution
- **Description**: A critical flaw in the popular Roundcube open-source webmail software that can be exploited to run arbitrary code on the server. Attackers are reportedly selling and using it for unauthorized access.
- **Impact**: Full remote compromise of the webmail system, allowing the attacker to steal emails, pivot within the network, and potentially gain further access to sensitive data.
- **Status**: Actively being exploited, with technical details disclosed. Administrators are urged to apply the vendor’s patches immediately.
- **CVE ID**: CVE-2025-49113

### Cisco Cloud Credential Vulnerability
- **Description**: A static credential vulnerability affecting Cisco Identity Services Engine (ISE) instances deployed on select cloud platforms, resulting in shared credentials across different deployments.
- **Impact**: Attackers with knowledge of these credentials could gain privileged access to ISE, potentially compromising authentication workflows and exposing sensitive information.
- **Status**: Cisco has issued warnings and recommends updating to a secure release or applying any available mitigations to eliminate the shared credentials problem.

### ConnectWise Flaw Used in Attacks
- **Description**: A recent unknown flaw in ConnectWise ScreenConnect software that attackers have leveraged to gain unauthorized access to customer environments. 
- **Impact**: Remote takeover of managed service provider or end-customer systems, allowing adversaries to install malware, steal data, or disrupt operations.
- **Status**: A patch has been released, but specific technical details remain undisclosed. Organizations using ScreenConnect should update immediately.

### Asus Router Vulnerability
- **Description**: Attackers are compromising Asus routers through undisclosed exploits or weak configurations, enrolling them in botnets.
- **Impact**: Compromised routers can be used as launchpads for large-scale attacks, eavesdropping on traffic, and enabling unauthorized remote access.
- **Status**: Users with affected routers are urged to update firmware and strengthen security settings. Additional steps include disabling remote administration if not required.

## Affected Systems and Products

- **Roundcube Webmail**: Critical remote code execution flaw in widely used open-source webmail software  
- **Cisco Identity Services Engine (ISE)**: Cloud-based ISE deployments on AWS, Azure, Oracle Cloud  
- **ConnectWise ScreenConnect**: Remote support and access software for managed service providers  
- **Asus Routers**: Various consumer-grade models vulnerable to compromise  

## Attack Vectors and Techniques

- **Remote Code Execution (RCE)**: Attackers exploit flaws in Roundcube to run malicious code on target servers  
- **Static Credentials**: Shared default credentials in Cisco cloud-based ISE deployments  
- **Software Supply Chain Attack**: Weaknesses in ConnectWise ScreenConnect enabling remote attacker entry  
- **Router Compromise**: Exploitation of Asus router vulnerabilities for botnet enrollment and network pivoting  

## Threat Actor Activities

- **BADBOX 2.0 Malware Operators**: Infecting Android devices at large scale, turning them into malicious proxies  
- **PathWiper Campaign**: Destructive wiper malware target­ing critical infrastructure in Ukraine  
- **Bitter APT**: Advanced persistent threat group expanding its scope, focusing on intelligence gathering  
- **BladedFeline**: An Iran-linked group involved in long-term espionage operations against Middle Eastern targets  
- **ViLE Gang**: Cybercriminals sentenced for breaching a federal law enforcement portal and conducting extortion  
- **Interlock Ransomware**: Claiming responsibility for healthcare data breaches and leaking stolen files  
- **RedLine Syndicates**: Associated with state-backed operations that harvest credentials and system data  