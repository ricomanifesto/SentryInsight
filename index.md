# Exploitation Report

Critical exploitation activity is currently targeting multiple enterprise systems and technologies. Microsoft has restricted Internet Explorer mode access in Edge browser after discovering zero-day exploits in the Chakra JavaScript engine being leveraged by threat actors. Oracle has issued emergency patches for E-Business Suite vulnerabilities that allow unauthenticated remote access, with Harvard University investigating a breach linked to one such zero-day exploit. The RondoDox botnet is actively weaponizing over 50 vulnerabilities across 30+ vendors in widespread exploitation campaigns. Additionally, threat actors are conducting large-scale credential-based attacks against SonicWall VPN services, compromising over 100 accounts, while AMD's SEV-SNP confidential computing has been compromised through the RMPocalypse vulnerability.

## Active Exploitation Details

### Internet Explorer Mode Zero-Day Exploits
- **Description**: Zero-day vulnerabilities in the Chakra JavaScript engine within Internet Explorer mode of Microsoft Edge browser
- **Impact**: Allows attackers to gain unauthorized access to target devices through browser exploitation
- **Status**: Microsoft has implemented restrictions on IE mode access after receiving credible reports of active exploitation in August 2025

### Oracle E-Business Suite Vulnerabilities
- **Description**: Critical security flaws in Oracle E-Business Suite allowing unauthorized remote access without authentication
- **Impact**: Enables attackers to access sensitive data and potentially compromise enterprise systems
- **Status**: Oracle has released emergency security patches over the weekend; Harvard University breach investigation ongoing

### RMPocalypse AMD SEV-SNP Vulnerability
- **Description**: Security flaw in AMD's Secure Encrypted Virtualization with Secure Nested Paging (SEV-SNP) technology that can be exploited with a single 8-byte write operation
- **Impact**: Completely undermines confidential computing guarantees and security protections
- **Status**: AMD has released fixes to address the vulnerability

### RondoDox Botnet Multi-Vendor Exploitation
- **Description**: Widespread botnet campaign exploiting over 50 vulnerabilities across more than 30 different vendors
- **Impact**: Mass compromise of systems for botnet recruitment and malicious activities
- **Status**: Ongoing active exploitation campaign described as an "exploit shopping spree"

### Pixnapping Android Side-Channel Attack
- **Description**: Side-channel vulnerability affecting Android devices from Google and Samsung that allows unauthorized data extraction
- **Impact**: Enables covert theft of two-factor authentication codes, Google Maps timelines, and other sensitive information without requiring permissions
- **Status**: Newly discovered vulnerability affecting Android devices

## Affected Systems and Products

- **Microsoft Edge Browser**: Internet Explorer mode functionality specifically targeted through Chakra JavaScript engine exploits
- **Oracle E-Business Suite**: All versions vulnerable to unauthenticated remote access attacks
- **AMD Processors**: Systems using SEV-SNP confidential computing technology affected by RMPocalypse
- **Android Devices**: Google and Samsung devices vulnerable to Pixnapping side-channel attacks
- **SonicWall SSL VPN**: Over 100 accounts compromised through credential-based attacks
- **Multiple Vendor Systems**: Over 30 vendors with 50+ vulnerabilities being exploited by RondoDox botnet

## Attack Vectors and Techniques

- **Browser-Based Exploitation**: Zero-day attacks through Internet Explorer mode leveraging Chakra JavaScript engine vulnerabilities
- **Unauthenticated Remote Access**: Direct exploitation of Oracle E-Business Suite without requiring valid credentials
- **Memory Manipulation**: Single 8-byte write operations to compromise AMD's confidential computing protections
- **Side-Channel Attacks**: Pixel-based information leakage on Android devices to steal sensitive data
- **Credential-Based VPN Compromise**: Use of stolen valid credentials to access SonicWall VPN services
- **Multi-Vulnerability Exploitation**: Systematic exploitation of numerous vulnerabilities across multiple vendors
- **Discord C2 Communications**: Malware using Discord channels for command and control operations
- **Supply Chain Attacks**: Malicious packages in npm, PyPI, and RubyGems ecosystems transmitting data via Discord

## Threat Actor Activities

- **Unknown Threat Actors**: Actively exploiting Internet Explorer mode zero-days since August 2025, prompting Microsoft security restrictions
- **Clop Ransomware Gang**: Listed Harvard University on their data leak site following Oracle zero-day exploitation
- **RondoDox Operators**: Conducting massive exploitation campaigns across 30+ vendors with 50+ vulnerabilities
- **TA585**: Delivering MonsterV2 malware through phishing campaigns with sophisticated attack chains
- **Storm-2603**: Abusing legitimate DFIR tools like Velociraptor in LockBit ransomware attacks
- **SonicWall VPN Attackers**: Large-scale compromise of over 100 VPN accounts using stolen credentials
- **Android Malware Authors**: Developing side-channel attacks to bypass Android security permissions
- **Supply Chain Attackers**: Distributing malicious packages across multiple programming language ecosystems