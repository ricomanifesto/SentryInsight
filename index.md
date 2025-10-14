# Exploitation Report

Critical exploitation activity is currently targeting multiple high-value systems across enterprises and individuals. Microsoft has restricted Internet Explorer mode in Edge browser following credible reports of zero-day exploits targeting the Chakra JavaScript engine. Oracle issued emergency patches for E-Business Suite vulnerabilities being actively exploited for unauthorized data access. AMD's SEV-SNP confidential computing has been compromised through the RMPocalypse attack, while Android devices face a novel Pixnapping side-channel attack stealing 2FA codes. The RondoDox botnet has expanded to weaponize over 50 vulnerabilities across 30+ vendors, and widespread credential-based attacks are compromising SonicWall VPN accounts. Meanwhile, threat actors are leveraging legitimate tools like Velociraptor in LockBit ransomware operations and using Discord as command-and-control infrastructure.

## Active Exploitation Details

### Microsoft Edge Internet Explorer Mode Zero-Day
- **Description**: Zero-day vulnerabilities in the Chakra JavaScript engine within Internet Explorer mode in Microsoft Edge browser
- **Impact**: Attackers can gain unauthorized access to target devices and potentially execute malicious code
- **Status**: Microsoft has implemented restrictions on IE mode access after receiving credible exploitation reports in August 2025

### Oracle E-Business Suite Vulnerability
- **Description**: Security flaw in Oracle E-Business Suite allowing remote exploitation without authentication
- **Impact**: Unauthorized access to sensitive data and potential full system compromise
- **Status**: Oracle issued emergency security patch over the weekend; vulnerability being actively exploited

### RMPocalypse AMD SEV-SNP Attack
- **Description**: Single 8-byte write vulnerability that undermines AMD's Secure Encrypted Virtualization with Secure Nested Paging (SEV-SNP) confidential computing guarantees
- **Impact**: Complete compromise of confidential computing protections, allowing attackers to access encrypted virtual machine data
- **Status**: AMD has released fixes to address the vulnerability

### Pixnapping Android Side-Channel Attack
- **Description**: Side-channel attack targeting Android devices from Google and Samsung that exploits visual inference techniques
- **Impact**: Covert theft of two-factor authentication codes, Google Maps timelines, and other sensitive information without requiring app permissions
- **Status**: Newly discovered vulnerability affecting current Android devices

### Oracle Zero-Day Exploited by Clop Ransomware
- **Description**: Recently disclosed zero-day vulnerability in Oracle systems being exploited in targeted attacks
- **Impact**: Data exfiltration and potential ransomware deployment
- **Status**: Active exploitation by Clop ransomware gang, with Harvard University among confirmed victims

## Affected Systems and Products

- **Microsoft Edge Browser**: Internet Explorer mode functionality compromised through Chakra JavaScript engine vulnerabilities
- **Oracle E-Business Suite**: Multiple versions affected by authentication bypass vulnerability
- **AMD Processors**: SEV-SNP enabled processors vulnerable to RMPocalypse attack
- **Android Devices**: Google and Samsung Android devices susceptible to Pixnapping attack
- **SonicWall SSL VPN**: Over 100 accounts compromised through credential-based attacks
- **Various Network Devices**: 50+ vulnerabilities across 30+ vendors being exploited by RondoDox botnet
- **Velociraptor DFIR Tool**: Legitimate forensics tool being weaponized for ransomware attacks

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in Microsoft Edge and Oracle systems
- **Side-Channel Attacks**: Visual inference techniques used in Pixnapping to steal sensitive data without permissions
- **Credential Stuffing**: Widespread use of stolen valid credentials to compromise SonicWall VPN accounts
- **Supply Chain Compromise**: Malicious packages in npm, PyPI, and RubyGems repositories sending data to Discord channels
- **Legitimate Tool Abuse**: Weaponization of Velociraptor DFIR tool for malicious reconnaissance and data collection
- **Discord C2**: Use of Discord channels as command-and-control infrastructure for multiple malware families
- **GitHub Infrastructure Abuse**: Astaroth banking trojan using GitHub repositories for operational resilience

## Threat Actor Activities

- **Clop Ransomware Gang**: Actively exploiting Oracle zero-day vulnerabilities to breach high-profile targets including Harvard University
- **Storm-2603 (CL-CRI-1040)**: Orchestrating LockBit ransomware attacks using weaponized Velociraptor DFIR tools
- **TA585**: Delivering MonsterV2 malware through sophisticated phishing campaigns with multi-stage attack chains
- **RondoDox Operators**: Expanding botnet operations to exploit vulnerabilities across 30+ vendors in "exploit shopping spree" fashion
- **GXC Team**: Dismantled cybercrime syndicate led by Brazilian actor "GoogleXcoder" specializing in various cyber criminal activities
- **Multi-National Botnet**: Large-scale credential-based attacks targeting RDP services in the United States from 100,000+ IP addresses
- **Discord-Based Threat Actors**: Multiple groups leveraging Discord infrastructure for C2 communications and data exfiltration across different malware families