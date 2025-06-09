# Exploitation Report

A wave of active exploits is targeting multiple technology ecosystems and devices, ranging from IoT products to open-source package repositories. Cybercriminals are increasingly using sophisticated techniques, like supply chain compromises and command injection vulnerabilities, to compromise thousands of victims globally. Notable campaigns include Mirai botnet infections of DVR devices, malicious npm and PyPI packages impacting development environments, data-wiping browser extensions, ClickFix-based phishing attacks, and ransomware groups exploiting critical Fortinet flaws.

## Active Exploitation Details

### TBK DVR Command Injection
- **Description**: A command injection vulnerability in TBK DVR-4104 and DVR-4216 digital video recorders exploited by a new Mirai botnet variant.  
- **Impact**: Attackers can hijack exposed DVR devices, incorporating them into the botnet for malicious activities such as DDoS attacks.  
- **Status**: Confirmed exploitation in the wild; device owners are urged to apply fixes or mitigations as soon as possible.  

### Supply Chain Attacks on npm and PyPI Ecosystems
- **Description**: Attackers introduced malicious code in multiple npm and PyPI packages, infecting a significant user base through compromised components.  
- **Impact**: Potential for remote access trojans and data exfiltration on developer machines and production servers.  
- **Status**: Ongoing threat; users and DevOps teams should inspect and remove compromised packages.  

### Malicious Browser Extensions
- **Description**: Trojanized extensions for Chromium-based browsers targeting users, primarily in Latin America, to siphon sensitive data.  
- **Impact**: Unauthorized access to browsing data, including credentials and other personal information.  
- **Status**: Active; users are advised to uninstall suspicious browser extensions and implement strict extension policies.  

### Malicious npm Packages (Gluestack)
- **Description**: Around 15 popular Gluestack packages in npm were backdoored with malware acting as a remote access trojan (RAT).  
- **Impact**: Compromise of application integrity, remote control of systems, and potential data exfiltration.  
- **Status**: Malicious implants discovered; developers should replace affected packages and rotate compromised credentials.  

### Malicious npm Utility Packages
- **Description**: Packages posing as legitimate utilities but containing destructive data-wiping functions that delete entire project directories.  
- **Impact**: Severe data loss and operational disruption for impacted projects.  
- **Status**: Identified and removed; users must audit dependencies to prevent further damage.  

### ClickFix-based Phishing
- **Description**: Sophisticated phishing campaigns employing ClickFix social engineering tactics to lure targets into downloading malware such as the Atomic macOS Stealer.  
- **Impact**: System compromise, credential theft, and unauthorized access to corporate or personal information.  
- **Status**: Ongoing phishing waves; end users should be trained to spot suspicious links and attachments.  

### BADBOX 2.0 Botnet
- **Description**: A persistent botnet targeting home networks, especially connected Android devices, to carry out illicit activities.  
- **Impact**: Devices fall under adversary control, enabling large-scale malicious operations.  
- **Status**: Remains active despite partial disruption; the FBI warns users to secure IoT and mobile devices with up-to-date firmware.  

### Critical Fortinet Flaws in Qilin Ransomware Attacks
- **Description**: The Qilin ransomware group exploits critical authentication bypass and remote code execution flaws in Fortinet products to infiltrate networks.  
- **Impact**: Unauthorized system access, encryption of critical data, and extortion demands.  
- **Status**: Confirmed attacks targeting unpatched devices; Fortinet has released patches and users should apply them immediately.  

## Affected Systems and Products

- **TBK DVR digital video recorders**: Models DVR-4104 and DVR-4216  
- **Open-source ecosystem**: npm (JavaScript) and PyPI (Python) packages  
- **Chromium-based browsers**: Various versions used in Latin America and beyond  
- **Gluestack npm packages**: Popular modules embedded with RAT functionality  
- **Android devices**: Actively targeted in home networks by BADBOX 2.0  
- **Fortinet devices**: With critical authentication bypass and remote code execution flaws  

## Attack Vectors and Techniques

- **Command Injection**: Used by Mirai botnet to compromise DVR devices  
- **Supply Chain Hijacking**: Malicious implants in npm and PyPI packages  
- **Malicious Browser Extensions**: Trojanized add-ons that exfiltrate user data  
- **Phishing with ClickFix**: Advanced social engineering campaigns leading to malware installation  
- **Ransomware Exploit**: Qilin ransomware leveraging critical Fortinet flaws  

## Threat Actor Activities

- **Mirai Operators**: Compromising DVR devices through command injection  
- **Unknown Supply Chain Attackers**: Injecting backdoors in npm and PyPI ecosystems  
- **Malware Creators**: Distributing destructive browser extensions and npm utilities  
- **Qilin Ransomware Group**: Utilizing Fortinet vulnerabilities to deploy ransomware  
- **BADBOX 2.0 Crew**: Sustaining a botnet campaign against home networks and Android devices  
- **Phishing Actors**: Employing ClickFix tactics to spread malware, including the Atomic macOS Stealer  