# Exploitation Report

Recent cybersecurity developments reveal several critical exploitation activities targeting diverse attack vectors. The most concerning incidents include a sophisticated supply chain attack compromising over 40 npm packages using malicious bundle.js files to steal developer credentials, advanced memory-based attacks bypassing DDR5 protection mechanisms, and coordinated threat actor campaigns targeting cloud platforms and healthcare infrastructure. Additionally, insider threats and fraudulent account creation in law enforcement systems highlight the evolving threat landscape facing organizations across multiple sectors.

## Active Exploitation Details

### Phoenix RowHammer Attack
- **Description**: A new variant of RowHammer attack targeting DDR5 memory chips from SK Hynix that bypasses advanced memory protections
- **Impact**: Successfully compromises DDR5 memory security mechanisms in 109 seconds, potentially allowing unauthorized memory access and system compromise
- **Status**: Recently discovered by researchers from ETH Zürich and Google; affects current DDR5 memory implementations

### NPM Supply Chain Attack
- **Description**: Malicious compromise of over 40 npm packages across multiple maintainer accounts using bundle.js to harvest credentials
- **Impact**: Credential theft from developers and potential compromise of downstream applications using these packages
- **Status**: Actively exploited; compromised packages identified and flagged by security researchers

### SnakeDisk USB Worm
- **Description**: Previously undocumented USB worm deployed by Mustang Panda threat group to deliver Yokai backdoor
- **Impact**: Lateral movement through USB devices and persistent backdoor installation on targeted systems
- **Status**: Active deployment targeting Thailand-based IP addresses

### Google Law Enforcement Portal Compromise
- **Description**: Fraudulent account creation in Google's Law Enforcement Request System (LERS) platform
- **Impact**: Unauthorized access to law enforcement data request systems, potentially compromising sensitive investigations
- **Status**: Confirmed by Google; fraudulent account has been identified and addressed

## Affected Systems and Products

- **DDR5 Memory Chips**: SK Hynix DDR5 memory modules vulnerable to Phoenix RowHammer attacks
- **NPM Registry**: Over 40 compromised packages affecting multiple maintainer accounts and downstream dependencies
- **Salesforce Platform**: UNC6040 and UNC6395 threat actors targeting Salesforce customers according to FBI warnings
- **Google LERS**: Law Enforcement Request System compromised through fraudulent account creation
- **FinWise Bank Systems**: Insider breach affecting 689,000 American First Finance customers
- **Brazilian Healthcare Software**: KillSec ransomware targeting healthcare technology supply chain providers

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Malicious bundle.js files injected into legitimate npm packages to steal developer credentials
- **Memory Exploitation**: Advanced RowHammer techniques bypassing modern DDR5 protection mechanisms within 109 seconds
- **USB Propagation**: SnakeDisk worm utilizing USB devices for lateral movement and payload delivery
- **Social Engineering**: Fraudulent account creation in legitimate law enforcement request portals
- **Insider Threats**: Former employees accessing sensitive data after employment termination
- **Ransomware Deployment**: KillSec ransomware targeting critical healthcare infrastructure and stealing patient data

## Threat Actor Activities

- **Mustang Panda**: China-aligned group deploying updated TONESHELL backdoor and new SnakeDisk USB worm targeting Thailand-based systems
- **UNC6040 and UNC6395**: Threat actors targeting Salesforce customers both separately and in coordinated campaigns, prompting FBI warnings
- **KillSec Ransomware Group**: Targeting Brazilian healthcare software providers, compromising major elements of the healthcare technology supply chain and stealing sensitive patient data
- **Supply Chain Attackers**: Coordinated compromise of multiple npm package maintainer accounts to distribute credential-stealing malware through bundle.js