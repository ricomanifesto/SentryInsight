# Exploitation Report

Based on the analysis of recent security articles, the current threat landscape shows several significant exploitation activities. The most critical incidents include the KillSec ransomware targeting Brazilian healthcare infrastructure, advanced threat actors UNC6040 and UNC6395 conducting sophisticated attacks against Salesforce customers, and the Mustang Panda group deploying new malware variants including the SnakeDisk USB worm. Additionally, researchers have demonstrated a new Phoenix attack that bypasses DDR5 memory protections, while insider threats and fraudulent law enforcement portal access highlight ongoing vulnerabilities in trusted systems.

## Active Exploitation Details

### KillSec Ransomware Campaign
- **Description**: Ransomware attack targeting Brazilian healthcare software providers
- **Impact**: Breach of healthcare technology supply chain with theft of sensitive patient data
- **Status**: Active exploitation affecting healthcare infrastructure

### UNC6040 and UNC6395 Threat Actor Campaign
- **Description**: Sophisticated threat actors targeting Salesforce customers through coordinated attacks
- **Impact**: Compromise of customer relationship management systems and associated data
- **Status**: Active FBI warning issued for ongoing threat activity

### Mustang Panda Operations
- **Description**: China-aligned threat actor deploying updated TONESHELL backdoor and new SnakeDisk USB worm
- **Impact**: Malware delivery targeting Thailand IP addresses with worm propagation capabilities
- **Status**: Active deployment of new malware variants including Yokai backdoor

### Phoenix Rowhammer Attack
- **Description**: New variant of Rowhammer attacks bypassing DDR5 memory protection mechanisms
- **Impact**: Memory corruption attacks against SK Hynix DDR5 chips
- **Status**: Academic research demonstrating successful bypass of latest memory defenses

### Law Enforcement Portal Compromise
- **Description**: Fraudulent account creation in Google's Law Enforcement Request System
- **Impact**: Unauthorized access to law enforcement data request platform
- **Status**: Google confirmed fraudulent account compromise

## Affected Systems and Products

- **Brazilian Healthcare Software**: Healthcare technology supply chain infrastructure compromised by ransomware
- **Salesforce Platform**: Customer relationship management systems targeted by threat actors
- **DDR5 Memory Systems**: SK Hynix DDR5 memory chips vulnerable to Phoenix Rowhammer attacks
- **Google LERS Platform**: Law Enforcement Request System compromised through fraudulent account creation
- **FinWise Bank Systems**: Internal systems accessed by former employee affecting American First Finance customers
- **Microsoft Exchange**: Exchange 2016 and 2019 reaching end of support creating potential security gaps

## Attack Vectors and Techniques

- **Ransomware Deployment**: Healthcare infrastructure targeting with data exfiltration capabilities
- **Supply Chain Attacks**: Targeting healthcare technology providers to access downstream customers
- **USB Worm Propagation**: SnakeDisk worm using removable media for malware distribution
- **Memory Exploitation**: Phoenix attack leveraging hardware vulnerabilities in DDR5 memory
- **Social Engineering**: Fraudulent law enforcement portal account creation
- **Insider Threats**: Former employee accessing sensitive customer data after employment termination

## Threat Actor Activities

- **KillSec Ransomware Group**: Targeting Brazilian healthcare sector with supply chain focus and patient data theft
- **UNC6040 and UNC6395**: Coordinated Salesforce customer targeting with FBI issuing active warnings
- **Mustang Panda**: China-aligned group deploying updated backdoors and USB worms targeting Thailand infrastructure
- **Academic Researchers**: Demonstrating new hardware attack vectors against modern memory protection systems