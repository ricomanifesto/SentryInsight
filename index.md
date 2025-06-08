# Exploitation Report

Recent security intelligence points to a surge in malicious activity across multiple fronts, including supply chain attacks targeting widely used npm packages, critical vulnerabilities in Fortinet devices exploited to deploy ransomware, and newly identified data wiper strains. These campaigns highlight the evolving tactics of threat actors who leverage sophisticated social engineering (e.g., ClickFix phishing), malicious code injection, and aggressive ransomware strategies to compromise systems and exfiltrate or destroy data.

## Active Exploitation Details

### Gluestack NPM Supply Chain Attack
- **Description**: Threat actors injected malicious code into 15 popular Gluestack npm packages, allowing remote access trojan (RAT) functionality within legitimate projects.
- **Impact**: Attackers can execute arbitrary commands, steal data, and maintain persistence in development and production environments.
- **Status**: The affected packages were compromised and are under investigation to remove or replace the malicious components.

### Malicious npm Data Wiper Packages
- **Description**: Newly discovered npm packages masquerading as helpful utilities but programmed to delete project directories, leading to data loss.
- **Impact**: Automated or accidental installation of these packages can result in immediate destruction of application directories and loss of critical project files.
- **Status**: Security teams are actively removing these packages and advising users to review their dependency lists.

### Critical Fortinet Vulnerabilities
- **Description**: Multiple high-impact flaws in Fortinet products are being exploited to bypass authentication and enable remote code execution, allowing ransomware operators to gain privileged access.
- **Impact**: Threat actors can take full control of vulnerable devices, pivot through internal networks, and deploy ransomware payloads.
- **Status**: Fortinet has released patches, but attackers continue to target unpatched systems.

### Atomic macOS Stealer
- **Description**: A macOS-focused information stealer that arrives via phishing campaigns employing ClickFix tactics to trick users into opening malicious links.
- **Impact**: Capable of exfiltrating browser credentials, system information, and potentially sensitive files from Apple devices.
- **Status**: Active campaigns continue to distribute the malware, and heightened awareness of phishing tactics is advised.

### PathWiper Data Wiper
- **Description**: A destructive malware strain identified in attacks against critical infrastructure, leveraging lateral movement techniques to erase essential system files.
- **Impact**: Causes operational disruption and potential system outages by corrupting stored data and rendering systems unrecoverable.
- **Status**: Ongoing investigations confirm active use in targeted campaigns against high-value infrastructure.

## Affected Systems and Products

- **Gluestack npm packages**: Multiple compromised package repositories targeting JavaScript-based projects  
- **Fortinet devices**: Vulnerable Fortinet firewalls and VPN appliances  
- **macOS systems**: Endpoints susceptible to the Atomic macOS Stealer via phishing  
- **npm-based environments**: Projects affected by destructive data wiper packages  
- **Critical infrastructure in Ukraine**: Primary targets of the PathWiper malware  

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Injecting malicious code into legitimate npm packages to distribute malware downstream  
- **Destructive Data Wipers**: Planting npm packages that delete directories or overwrite critical system files  
- **Ransomware Leveraging Known Vulnerabilities**: Exploiting authentication bypass and remote code execution flaws in enterprise devices  
- **Advanced Phishing (ClickFix)**: Using sophisticated social engineering lures to trick users into executing stealer malware  

## Threat Actor Activities

- **Qilin Ransomware**: Deploys ransomware through exploitation of Fortinet vulnerabilities, focusing on unpatched enterprise appliances  
- **BADBOX 2.0**: A botnet campaign targeting home networks and Android devices, converting them into malicious proxy nodes  
- **Interlock Ransomware**: Responsible for breaching healthcare systems (e.g., Kettering Health) and stealing sensitive data  
- **Chaos Ransomware**: Used in attacks against tax resolution firms (e.g., Optima Tax Relief), leading to data leaks  
- **PathWiper Operators**: Conduct disruptive attacks on critical infrastructure in Ukraine, leveraging new data wiper capability  