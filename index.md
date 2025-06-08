# Exploitation Report

A surge of cyber threats has emerged across multiple platforms, with attackers targeting DVR devices, open-source software repositories, and critical infrastructure. Notable campaigns include a Mirai botnet variant exploiting command injection in TBK DVR devices, widespread malware infiltrations in npm and PyPI, malicious npm packages acting as data wipers, and ransomware groups taking advantage of critical Fortinet flaws. These exploits emphasize the ongoing need for vigilant patching, supply chain security, and proactive threat hunting.

## Active Exploitation Details

### Command Injection in TBK DVR Devices
- **Description**: A Mirai malware variant uses a command injection flaw in TBK DVR-4104 and DVR-4216 devices, allowing attackers to run arbitrary code and add the devices to a botnet.  
- **Impact**: Compromised DVRs can be hijacked for large-scale DDoS attacks and additional malicious activities.  
- **Status**: Actively exploited, with no specific patch details publicly disclosed.  

### Supply Chain Malware in npm and PyPI
- **Description**: Threat actors introduced malicious code into multiple popular packages in both the npm and PyPI ecosystems, infecting unsuspecting users’ projects.  
- **Impact**: Attackers can execute remote commands, install backdoors, and potentially steal sensitive data from infected systems.  
- **Status**: Several packages have been taken down or updated; users are advised to review dependencies and apply updated releases.  

### Malicious Browser Extensions
- **Description**: A malicious extension campaign targeting Chromium-based browsers infected over 700 users in Latin America, secretly siphoning data.  
- **Impact**: Stolen credentials, surveillance of user activity, and potential lateral movement across additional platforms.  
- **Status**: Ongoing; users are encouraged to remove untrusted extensions and apply security best practices.  

### Gluestack npm Package Attack
- **Description**: Over a dozen popular Gluestack packages in npm were altered to include malicious code, acting as a remote access trojan (RAT).  
- **Impact**: Threat actors gain unauthorized control over infected systems, enabling data theft and execution of further attacks.  
- **Status**: Compromised packages have been taken down or cleaned; users must audit dependencies and update to safe versions.  

### Malicious npm Packages as Data Wipers
- **Description**: Two recently identified npm packages posing as utilities instead serve as destructive wipers, deleting project directories.  
- **Impact**: Loss of critical application data and potential disruption of the development lifecycle.  
- **Status**: Packages have been removed; developers should verify installed modules and maintain version control backups.  

### Critical Fortinet Flaws Exploited by Qilin Ransomware
- **Description**: Qilin ransomware operators are leveraging unpatched security flaws on Fortinet devices, bypassing authentication and executing code remotely.  
- **Impact**: Full compromise of network appliances, enabling ransomware encryption of systems across the targeted organization.  
- **Status**: Actively exploited; Fortinet has released updates, and organizations must apply patches or mitigations immediately.  

## Affected Systems and Products
- **TBK DVR-4104 and DVR-4216**: Vulnerable to command injection, exploited by Mirai.  
- **npm Packages**: Various malicious or compromised modules posing as legitimate libraries.  
- **PyPI Packages**: Multiple infected Python packages harboring backdoors and malware.  
- **Fortinet Appliances**: Affected by critical flaws used by Qilin ransomware.  
- **Chromium-Based Browsers**: Targeted by malicious extensions stealing user data.  

## Attack Vectors and Techniques
- **Command Injection**: Exploiting insecure input handling in DVR devices to run arbitrary code.  
- **Supply Chain Attacks**: Inserting malicious code into popular open-source repositories (npm, PyPI) to compromise downstream users.  
- **Malicious Extensions**: Luring browser users into installing fraudulent add-ons that collect sensitive information.  
- **Remote Access Trojan (RAT)**: Gluestack package compromise granting full attacker control over infected systems.  
- **Data Wiping**: Npm modules that delete critical files, causing disruption to development processes.  
- **Ransomware Deployment**: Targeted exploitation of unpatched Fortinet devices for unauthorized encryption of enterprise networks.  

## Threat Actor Activities
- **Mirai Botnet Operators**: Expanding infection to vulnerable TBK DVRs for large-scale DDoS campaigns.  
- **Supply Chain Attackers**: Compromising npm and PyPI packages to deliver backdoors and data-wiping malware.  
- **Malicious Extension Campaign**: Focused spying operation targeting Latin American Chrome-based browser users.  
- **Qilin Ransomware Group**: Leveraging Fortinet flaws to breach victims, encrypt data, and extort organizations.  
- **PathWiper Actors**: Deploying wiper malware to disrupt Ukrainian critical infrastructure.  
- **ClickFix Phishers**: Using sophisticated social engineering to spread malware, including an Atomic macOS Stealer variant.  