# Exploitation Report

Current threat intelligence reveals significant exploitation activity across multiple attack vectors, with particular focus on infrastructure vulnerabilities and ransomware operations. Microsoft's August 2025 Patch Tuesday addressed 107 security flaws including one publicly disclosed zero-day vulnerability in Windows Kerberos that poses immediate risk to enterprise environments. Concurrently, threat actors are conducting coordinated brute-force campaigns against Fortinet SSL VPN devices while shifting tactics toward FortiManager exploitation. The cybercrime landscape shows increased collaboration between established groups, with ShinyHunters and Scattered Spider joining forces for sophisticated extortion campaigns targeting Salesforce customers. Additionally, over 3,300 Citrix NetScaler devices remain vulnerable to the CitrixBleed 2 authentication bypass vulnerability nearly two months after patches became available.

## Active Exploitation Details

### Windows Kerberos Zero-Day Vulnerability
- **Description**: A publicly disclosed zero-day vulnerability affecting Windows Kerberos authentication protocol
- **Impact**: Allows attackers to compromise authentication mechanisms and potentially gain unauthorized access to domain resources
- **Status**: Patched in Microsoft's August 2025 Patch Tuesday update addressing 107 total vulnerabilities

### CitrixBleed 2 Authentication Bypass
- **Description**: Critical vulnerability in Citrix NetScaler devices that allows attackers to bypass authentication mechanisms by hijacking user sessions
- **Impact**: Complete authentication bypass enabling unauthorized access to protected resources and potential lateral movement
- **Status**: Patches available but over 3,300 devices remain unpatched nearly two months after release

### Fortinet SSL VPN Vulnerabilities
- **Description**: Multiple vulnerabilities in Fortinet SSL VPN devices being targeted through coordinated brute-force attacks
- **Impact**: Successful exploitation provides remote access to corporate networks and potential for lateral movement
- **Status**: Active exploitation observed with attackers shifting focus to FortiManager devices

## Affected Systems and Products

- **Microsoft Windows**: Kerberos authentication protocol affected by zero-day vulnerability across Windows environments
- **Citrix NetScaler**: Over 3,300 devices remain vulnerable to CitrixBleed 2 authentication bypass
- **Fortinet SSL VPN**: Global brute-force campaign targeting SSL VPN devices with subsequent FortiManager exploitation
- **Salesforce Platforms**: Targeted by collaborative extortion campaigns from ShinyHunters and Scattered Spider
- **Middle Eastern Public Sector**: Aviation industry and government organizations targeted by Charon ransomware
- **Government Organizations**: Multiple agencies targeted by Curly COMrades cyber-espionage group using custom malware

## Attack Vectors and Techniques

- **Brute-Force Attacks**: Coordinated global campaign against Fortinet SSL VPN infrastructure with significant traffic spikes
- **Session Hijacking**: CitrixBleed 2 exploitation through user session manipulation to bypass authentication
- **Custom Malware Deployment**: Curly COMrades using specialized backdoor malware with persistent access through scheduled tasks
- **APT-Style Tactics**: Charon ransomware employing advanced persistent threat techniques in targeted campaigns
- **Data Extortion**: Combined ShinyHunters and Scattered Spider operations focusing on business data theft and extortion

## Threat Actor Activities

- **ShinyHunters & Scattered Spider**: Joint extortion campaign targeting Salesforce customers with plans to expand to financial services and technology providers
- **BlackSuit Ransomware Gang**: U.S. government seized over $1 million in cryptocurrency assets from this group's operations
- **Charon Ransomware Operators**: Deploying novel malware with APT-style tactics, potentially linked to China's state-sponsored Earth Baxia group
- **Curly COMrades**: New cyber-espionage group conducting targeted attacks against government organizations using custom backdoor malware
- **Earth Baxia**: Suspected Chinese state-sponsored actor potentially connected to Charon ransomware deployment in Middle Eastern campaigns