# Exploitation Report

Recent security intelligence highlights active exploitation of a critical Roundcube webmail vulnerability and a ConnectWise flaw, illustrating attackers’ continued focus on remote code execution and unauthorized access routes. Meanwhile, threat actors deploy advanced malware such as PathWiper and BADBOX 2.0, targeting everything from critical infrastructure to large pools of consumer devices. Several APT groups have also intensified their campaigns, employing sophisticated tactics and expanding their geographic reach.

## Active Exploitation Details

### Critical Roundcube Webmail Exploit
- **Description**: A severe remote code execution bug in Roundcube webmail software allowing attackers to run arbitrary commands on the server.  
- **Impact**: Successful exploitation grants complete access to email data and potentially enables lateral movement within the compromised environment.  
- **Status**: Actively exploited in the wild; patches are available in recent releases of Roundcube.  
- **CVE ID**: CVE-2025-49113  

### ConnectWise ScreenConnect Flaw
- **Description**: An undisclosed vulnerability in ConnectWise ScreenConnect (formerly ScreenConnect) used by attackers to gain unauthorized access to remote support sessions.  
- **Impact**: Adversaries can potentially compromise managed service provider (MSP) infrastructure or customer endpoints connected via ScreenConnect.  
- **Status**: Under active exploitation; a vendor patch has been released.  

## Affected Systems and Products

- **Roundcube Webmail**: Older versions prior to the latest patched releases (1.5.4, 1.6.7, and 1.7.2)  
- **ConnectWise ScreenConnect**: Deployments not yet updated to the most recent patched version  

## Attack Vectors and Techniques

- **Remote Code Execution (RCE)**: Exploiting Roundcube’s critical bug to inject and execute arbitrary commands on the webmail server  
- **Unauthorized Remote Access**: Leveraging an as-yet-undisclosed ConnectWise flaw to take over remote sessions  
- **Data Exfiltration via Malware**: Using campaigns like PathWiper and BADBOX 2.0 to steal or destroy sensitive information  
- **Misconfigurations & API Key Leakage**: Popular Chrome extensions that transmit data over HTTP or embed sensitive secrets, enabling interception or misuse  

## Threat Actor Activities

- **Actor/Group**: Operators behind PathWiper  
  - **Campaign**: Deployed a destructive wiping attack against a Ukrainian critical infrastructure entity  
- **Actor/Group**: FBI-tracked operators behind BADBOX 2.0  
  - **Campaign**: Infected millions of Android devices, converting them into malicious proxy hosts  
- **Actor/Group**: Bitter APT  
  - **Campaign**: Broadened geographic targeting using evolved tactics aligned with state-sponsored objectives  
- **Actor/Group**: BladedFeline  
  - **Campaign**: Persisted for years in Iraqi and Kurdish government networks, employing specialized malware  
- **Actor/Group**: ViLE gang  
  - **Campaign**: Engaged in extortion by breaching a federal law enforcement portal and demanding payoff  