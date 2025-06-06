# Exploitation Report

Recent security disclosures highlight a surge in malicious activity targeting critical infrastructure, popular webmail solutions, and remote management platforms. Of particular concern is the active remote code execution exploit in Roundcube webmail, high-impact vulnerabilities in Cisco Identity Services Engine (ISE) deployments on major cloud platforms, and an exploited flaw in ConnectWise ScreenConnect. Multiple threat actors, including APT groups, continue to capitalize on these exploits and sophisticated malware campaigns to expand their footprint and disrupt organizations worldwide.

## Active Exploitation Details

### Roundcube Webmail Vulnerability
- **Description**: A critical flaw in the Roundcube open-source webmail application that allows remote code execution on unpatched instances. Attackers can leverage it to gain unauthorized access to email data and potentially pivot further into the underlying server.
- **Impact**: Full compromise of the targeted webmail environment, with the potential to exfiltrate, modify, or delete sensitive data.
- **Status**: Actively exploited by cybercriminals. A patch is available from the Roundcube development team.
- **CVE ID**: CVE-2025-49113

### Cisco ISE Static Credential Vulnerability
- **Description**: A critical configuration issue in Cisco Identity Services Engine (ISE) software deployments on AWS, Azure, and Oracle Cloud. All instances using the same software release share identical credentials, allowing attackers to gain administrative access.
- **Impact**: Potential full administrative compromise of Cisco ISE systems, enabling lateral movement and unauthorized access to network resources.
- **Status**: Cisco has issued an alert and recommends immediate patching or reconfiguration to mitigate the threat.

### ConnectWise ScreenConnect Flaw
- **Description**: A remote management tool vulnerability in ConnectWise ScreenConnect that is being exploited in ongoing attacks. Malicious actors can abuse the flaw to take over ScreenConnect instances and potentially access client systems.
- **Impact**: Full remote takeover of managed endpoints, risk of data theft, and deployment of additional malware across multiple client networks.
- **Status**: ConnectWise has released a patch, but attacks continue to target unpatched deployments.

## Affected Systems and Products

- **Roundcube**: Versions affected prior to the latest security patch released for CVE-2025-49113  
- **Cisco Identity Services Engine (ISE)**: Deployments running vulnerable releases on AWS, Azure, or Oracle Cloud  
- **ConnectWise ScreenConnect**: Unpatched or outdated versions vulnerable to the disclosed flaw  

## Attack Vectors and Techniques

- **Remote Code Execution (RCE)**: Hackers exploit the Roundcube webmail software bug to achieve code execution on vulnerable servers.  
- **Unauthorized Administrative Access**: Exploiting static credentials in Cisco ISE or leveraging the ConnectWise ScreenConnect flaw to gain full control of administrative consoles.  
- **Malware Deployment**: Once inside, attackers install malicious binaries (including wiper malware) to disrupt systems, exfiltrate information, or further pivot within compromised networks.  

## Threat Actor Activities

- **Actor/Group**: Various unknown cybercriminals deploying attacks against Roundcube webmail; malicious parties selling the Roundcube exploit on underground forums.  
- **Campaign**: Increased exploitation of remote management platforms (e.g., ConnectWise ScreenConnect) to escalate privileges and move laterally.  

- **Actor/Group**: Bitter APT  
  - **Campaign**: Ongoing espionage operations with expanding geographic reach, focusing on government and critical infrastructure targets.  

- **Actor/Group**: BladedFeline (Iran-linked)  
  - **Campaign**: Targeting Iraqi and Kurdish entities with custom malware to gather intelligence and disrupt operations.  

- **Unknown Threat Actor**: Deployed PathWiper in destructive attacks on Ukrainian critical infrastructure, indicating a focus on sabotage and large-scale disruption.  