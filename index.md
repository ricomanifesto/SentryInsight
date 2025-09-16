# Exploitation Report

The security landscape reveals several concerning exploitation activities, with threat actors actively targeting healthcare infrastructure, cloud platforms, and enterprise systems. Notable incidents include the KillSec ransomware group successfully breaching a Brazilian healthcare software provider and compromising sensitive patient data. Additionally, sophisticated threat actors have created fraudulent accounts in Google's Law Enforcement Request System, while Chinese-aligned Mustang Panda has deployed advanced malware including the SnakeDisk USB worm and updated TONESHELL backdoor variants. The FBI has issued warnings about coordinated attacks against Salesforce customers by threat groups UNC6040 and UNC6395, and researchers have demonstrated new memory-based attacks that bypass modern DDR5 security protections.

## Active Exploitation Details

### KillSec Ransomware Attack
- **Description**: Ransomware attack targeting Brazilian healthcare technology infrastructure
- **Impact**: Breach of healthcare technology supply chain with theft of sensitive patient data
- **Status**: Active ongoing investigation, compromised healthcare software provider systems

### Google Law Enforcement Portal Compromise
- **Description**: Creation of fraudulent accounts within Google's Law Enforcement Request System (LERS)
- **Impact**: Potential unauthorized access to user data through abuse of legitimate law enforcement channels
- **Status**: Confirmed by Google, fraudulent account identified and addressed

### Mustang Panda Malware Campaign
- **Description**: Advanced persistent threat campaign using updated TONESHELL backdoor and new SnakeDisk USB worm
- **Impact**: Lateral movement through USB propagation and persistent backdoor access on Thai IP addresses
- **Status**: Active campaign with newly documented malware variants

### Phoenix Rowhammer Attack
- **Description**: New variant of Rowhammer attacks targeting DDR5 memory systems
- **Impact**: Bypasses latest memory protection mechanisms on SK Hynix DDR5 chips
- **Status**: Academic proof-of-concept demonstrated, affects current DDR5 implementations

## Affected Systems and Products

- **Brazilian Healthcare Software**: Major healthcare technology provider compromised by KillSec ransomware
- **Google LERS Platform**: Law enforcement data request system targeted by fraudulent account creation
- **Salesforce Customers**: Multiple organizations targeted by coordinated threat actor campaigns
- **DDR5 Memory Systems**: SK Hynix DDR5 memory chips vulnerable to Phoenix Rowhammer attacks
- **FinWise Bank Systems**: Corporate customer data accessed through insider threat
- **Thai Network Infrastructure**: Systems targeted by Mustang Panda USB worm propagation

## Attack Vectors and Techniques

- **Ransomware Deployment**: KillSec group targeting healthcare supply chain infrastructure
- **Social Engineering**: Fraudulent law enforcement account creation for data access
- **USB Worm Propagation**: SnakeDisk malware spreading through removable media
- **Memory Exploitation**: Phoenix attack bypassing DDR5 Rowhammer protections
- **Insider Threats**: Former employee unauthorized access to sensitive financial data
- **Cloud Platform Targeting**: Coordinated attacks against Salesforce customer environments

## Threat Actor Activities

- **KillSec Ransomware Group**: Actively targeting healthcare technology providers in Brazil with focus on patient data theft
- **Unknown Threat Actors**: Sophisticated actors creating fraudulent law enforcement accounts to abuse legitimate data request systems
- **Mustang Panda (Chinese APT)**: Deploying updated malware toolkit including TONESHELL backdoor and SnakeDisk USB worm against Thai infrastructure
- **UNC6040 and UNC6395**: FBI-identified threat groups conducting coordinated campaigns against Salesforce customers, operating both separately and in collaboration
- **Insider Threats**: Former FinWise Bank employee conducting unauthorized data access affecting 689,000 American First Finance customers