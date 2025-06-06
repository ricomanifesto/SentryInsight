# Exploitation Report

Recent reporting highlights two significant active exploit campaigns. Attackers are targeting a critical remote code execution flaw in Roundcube Webmail and an undisclosed ConnectWise ScreenConnect vulnerability. Both exploits pose serious risks of unauthorized remote access and compromise of sensitive data. Additionally, multiple threat groups, including Bitter APT and BladedFeline, are conducting aggressive campaigns against various targets, underscoring a broad and evolving threat landscape.

## Active Exploitation Details

### Roundcube Webmail Remote Code Execution
- **Description**: A severe flaw in Roundcube’s open-source webmail application allows attackers to remotely execute malicious code by passing specially crafted requests and payloads.  
- **Impact**: Successful attacks grant full control of the underlying server, enabling data exfiltration and potential lateral movement throughout the network.  
- **Status**: Actively exploited in the wild with a patch available from Roundcube’s development team.  
- **CVE ID**: CVE-2025-49113  

### ConnectWise ScreenConnect Flaw
- **Description**: An undisclosed vulnerability in ConnectWise ScreenConnect (formerly known as ScreenConnect) permits attackers to gain unauthorized access to remote support environments.  
- **Impact**: Exploitation can lead to control over remote systems, unauthorized data retrieval, and further compromise of enterprise networks.  
- **Status**: Actively used in attacks; ConnectWise has released a patch to mitigate ongoing exploitation.  

## Affected Systems and Products

- **Roundcube Webmail**: A widely used open-source webmail platform susceptible to remote code execution attacks.  
- **ConnectWise ScreenConnect**: Remote support and remote access product used by MSPs and IT teams, affected by an actively exploited flaw.  

## Attack Vectors and Techniques

- **Remote Code Execution (RCE)**: Attackers exploit web-based functionality in Roundcube to send specially crafted payloads that trigger arbitrary code execution on the server.  
- **Unauthorized Remote Access**: Adversaries leverage a vulnerability in ConnectWise ScreenConnect to plant backdoors or misuse privileged remote support sessions.  

## Threat Actor Activities

- **Bitter APT**: Increasingly active espionage campaigns with evolving tactics, targeting organizations across new geographic regions.  
- **BladedFeline**: An Iran-linked group deploying Whisper and Spearal malware against Iraqi and Kurdish government officials.  
- **Play Ransomware**: Responsible for breaching hundreds of organizations, including critical infrastructure targets.  
- **ViLE Gang**: Involved in extortion and unauthorized access to a federal law enforcement portal, leveraging stolen data for intimidation.  
- **Interlock Ransomware**: Allegedly behind the breach of Kettering Health, leaking sensitive data to pressure victims into payment.  
- **RedLine Malware Operators**: Under investigation by authorities; threats include information-stealing campaigns sponsored by alleged state actors.  