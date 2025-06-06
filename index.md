# Exploitation Report

Recent security news highlights a surge in exploit activity targeting widely used platforms, with special focus on a critical Roundcube webmail vulnerability enabling remote code execution and a ConnectWise ScreenConnect flaw actively abused in the wild. Meanwhile, threat actors continue to evolve tactics, launching destructive wiper attacks against critical infrastructure and leveraging advanced malware, such as BADBOX 2.0, to compromise millions of devices.

## Active Exploitation Details

### Roundcube Webmail Remote Code Execution
- **Description**: A critical vulnerability that allows remote attackers to execute malicious code on Roundcube servers. Attackers are reportedly selling a functional exploit, increasing the risk of widespread compromise.  
- **Impact**: Successful exploitation can grant full system access, enabling data theft, email manipulation, and pivot attacks within affected networks.  
- **Status**: Actively exploited in the wild, with public details circulating. Patches are available, and administrators are urged to update immediately.  
- **CVE ID**: CVE-2025-49113

### ConnectWise ScreenConnect Vulnerability
- **Description**: An undisclosed flaw in ConnectWise ScreenConnect software has been leveraged by attackers to gain unauthorized access to remote support sessions and customer environments.  
- **Impact**: Compromised systems can facilitate privilege escalation, data theft, or lateral movement across multiple endpoints.  
- **Status**: Confirmed attacks are ongoing. ConnectWise has issued a patch, though details on the vulnerability remain partially undisclosed.

## Affected Systems and Products

- **Roundcube Webmail**: Versions susceptible to the remote code execution flaw.  
- **ConnectWise ScreenConnect**: Remote support installations vulnerable to targeted attacks in unpatched environments.

## Attack Vectors and Techniques

- **Remote Code Execution (RCE)**: Exploit scripts target unpatched Roundcube installations, allowing attackers to run arbitrary code.  
- **Remote Session Hijacking**: Threat actors exploit the ConnectWise ScreenConnect flaw to take over remote connections and gain elevated privileges.

## Threat Actor Activities

- **PathWiper Attack**: Deployed destructive wiper malware against critical infrastructure in Ukraine.  
- **BADBOX 2.0**: A massive Android malware campaign infecting millions of devices to facilitate malicious proxy usage.  
- **Bitter APT**: Expanding geopolitical cyber-espionage operations, demonstrated by sophisticated infiltration of multiple regional targets.  
- **BladedFeline (Iran-Linked)**: Hidden in victim networks for extended periods, conducting espionage and reconnaissance.  
- **BidenCash Marketplace**: Illicit carding platform targeted by a global takedown; associated domains seized by law enforcement.  
- **ViLE Gang**: Responsible for compromising a law enforcement portal in an extortion scheme.  
- **Interlock Ransomware**: Claims healthcare sector breaches and leaks stolen data.  
- **RedLine Infostealer**: Continues to pose a global data-exfiltration threat, with the U.S. offering rewards for information on state-sponsored operators.  