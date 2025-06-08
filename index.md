# Exploitation Report

Recent security reports highlight active exploitation of command injection flaws in TBK DVR devices, critical vulnerabilities in Fortinet products targeted by ransomware, and large-scale supply chain compromises affecting npm and PyPI ecosystems. Threat actors also continue to leverage advanced phishing and social engineering techniques to deliver malware, underscoring the growing sophistication of global cyber campaigns.

## Active Exploitation Details

### Command Injection in TBK DVR Devices
- **Description**: A command injection vulnerability in TBK DVR-4104 and DVR-4216 allows attackers to execute arbitrary commands remotely. Attackers have been deploying a new Mirai variant to hijack and co-opt these devices into a botnet.  
- **Impact**: Remote takeover of DVR devices, enabling large-scale botnet propagation and DDoS attacks.  
- **Status**: Actively exploited in the wild; patch status unknown.

### Critical Fortinet Flaws
- **Description**: Multiple critical Fortinet vulnerabilities permit unauthenticated attackers to bypass security controls and execute malicious code remotely.  
- **Impact**: Full compromise of affected devices, enabling ransomware operators to gain footholds in enterprise networks.  
- **Status**: Actively exploited by ransomware groups; patches available from Fortinet.

## Affected Systems and Products

- **TBK DVR-4104 & DVR-4216**: Command injection flaws used to deploy Mirai malware.  
- **Fortinet Security Devices**: Critical vulnerabilities exploited for unauthorized access and code execution.  
- **npm & PyPI Packages**: Supply chain attacks introduce malicious code affecting projects with high download volumes.  

## Attack Vectors and Techniques

- **Command Injection**: Exploiting improperly sanitized inputs in DVR devices to execute arbitrary system commands.  
- **Supply Chain Attacks**: Compromising legitimate package repositories (npm/PyPI) to distribute trojanized software.  
- **Ransomware Exploitation**: Leveraging critical vulnerabilities in infrastructure devices for rapid lateral movement and data encryption.  
- **Malicious Browser Extensions**: Disguising unauthorized add-ons to siphon sensitive information and maintain persistence.  
- **ClickFix Phishing**: Employing sophisticated social engineering to trick users into downloading malware or revealing credentials.

## Threat Actor Activities

- **Mirai Botnet**: Using command injection to hijack DVR devices and grow its DDoS network.  
- **Qilin Ransomware Operation**: Specifically targeting unpatched Fortinet devices and executing ransomware attacks.  
- **BADBOX 2.0**: Continuing botnet operations against home networks, focusing on Android-based devices.  
- **Chaos Ransomware Group**: Responsible for compromising data at Optima Tax Relief.  
- **Interlock Ransomware**: Behind the breach at Kettering Health.  
- **Unspecified Supply Chain Attackers**: Infiltrating npm and PyPI to plant malicious packages and gain remote access.