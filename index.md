# Exploitation Report

Recent threat intelligence indicates a surge in sophisticated malicious activity involving botnets, supply chain compromises, ransomware infections, and data wipers. Notably, threat actors have leveraged critical security flaws in Fortinet solutions to facilitate ransomware deployment, while multiple campaigns utilize phishing tactics, malicious browser extensions, and fraudulent npm packages. These incidents underscore the evolving tactics used by attackers to compromise business and personal environments.

## Active Exploitation Details

### Critical Fortinet Flaws Exploited by Qilin Ransomware
- **Description**: Attackers exploit authentication-bypass and remote code execution weaknesses in Fortinet devices to infiltrate networks.  
- **Impact**: Once inside, threat actors install ransomware, disrupt business operations, and demand payment under threat of data theft and encryption.  
- **Status**: Attacks are actively targeting unpatched or outdated Fortinet devices; patches are available from the vendor.

## Affected Systems and Products

- **Chromium-Based Browsers**: Targeted by malicious extensions, primarily affecting users across Latin America.  
- **Gluestack npm Packages**: Supply chain compromise impacting 15 packages with widespread downloads.  
- **Malicious npm Utilities**: Packages disguised as helpful tools but actually destructive wipers.  
- **Fortinet Devices**: Subject to critical exploits enabling remote code execution and authentication bypass.  
- **Android Devices**: BADBOX 2.0 botnet leveraging infected home networks.  
- **macOS Systems**: Atomic macOS Stealer campaign exploiting phishing tactics (ClickFix).  
- **Ukrainian Critical Infrastructure**: Targeted by the new PathWiper data wiper malware.  
- **Healthcare Organizations**: Multiple ransomware campaigns targeting sensitive data.

## Attack Vectors and Techniques

- **Malicious Browser Extensions**: Users tricked into installing add-ons that steal credentials or inject malware.  
- **Supply Chain Attacks**: Compromise of legitimate npm packages (Gluestack, other utilities) to distribute malicious code.  
- **Data Wiper Malware (PathWiper)**: Erases or corrupts data to disrupt critical infrastructure operations.  
- **Ransomware Infections**: Qilin, Chaos, and Interlock strains leveraging vulnerabilities or social engineering to gain initial access.  
- **Phishing via ClickFix**: Social engineering method prompting users to click disguised links leading to malware downloads.  
- **Botnet Campaign (BADBOX 2.0)**: Infects Android devices to form large-scale networks for malicious activities.

## Threat Actor Activities

- **Qilin Ransomware**: Deploys payloads through critical Fortinet flaws, encrypts systems, and extorts victims.  
- **Interlock Ransomware Group**: Responsible for a healthcare breach, stealing data and demanding payment.  
- **Chaos Ransomware Actors**: Attacked a tax resolution firm, leaking sensitive client information.  
- **Malicious npm Package Operators**: Insert destructive or Trojanized code into widely used JavaScript libraries.  
- **BADBOX 2.0 Botnet**: Continues to propagate across home networks, focusing on Android devices.  
- **Atomic macOS Stealer Campaign**: Employs phishing via ClickFix to compromise Apple users.  
- **PathWiper Operators**: Target Ukrainian infrastructure to disrupt operations and cause data loss.  