# Exploitation Report

Critical exploitation activity has emerged across multiple attack vectors, with Apple backporting fixes for an actively exploited vulnerability with a CVSS score of 8.8 being used in sophisticated spyware campaigns. Simultaneously, threat actors are conducting large-scale supply chain attacks affecting over 40 npm packages to steal credentials, while advanced memory-based attacks are bypassing DDR5 protections in just over 100 seconds. Notable threat actor campaigns include Mustang Panda deploying USB worms targeting Thailand infrastructure and multiple groups targeting Salesforce customers with sophisticated attack techniques.

## Active Exploitation Details

### Apple Out-of-Bounds Vulnerability
- **Description**: A critical out-of-bounds vulnerability in Apple systems that has been actively exploited in sophisticated spyware attacks
- **Impact**: Enables attackers to conduct advanced spyware operations with high severity impact
- **Status**: Apple has backported fixes to address active exploitation
- **CVE ID**: CVE-2025-43300

### npm Supply Chain Compromise
- **Description**: Malicious code injection affecting over 40 npm packages across multiple maintainers using bundle.js for credential theft
- **Impact**: Allows attackers to steal developer credentials and potentially compromise downstream applications
- **Status**: Active exploitation targeting the npm registry ecosystem

### Phoenix RowHammer Memory Attack
- **Description**: Advanced RowHammer variant targeting DDR5 memory chips from SK Hynix, bypassing built-in protection mechanisms
- **Impact**: Can achieve memory corruption and potential privilege escalation in 109 seconds
- **Status**: Proof-of-concept demonstrated against advanced DDR5 protections

## Affected Systems and Products

- **Apple Devices**: Systems vulnerable to CVE-2025-43300 requiring backported security updates
- **npm Registry**: Over 40 compromised packages affecting multiple maintainers and downstream dependencies
- **DDR5 Memory**: SK Hynix DDR5 memory chips vulnerable to Phoenix RowHammer attacks
- **Google Law Enforcement Portal**: Fraudulent account creation in Law Enforcement Request System (LERS)
- **Salesforce Platform**: Multiple threat actors targeting customer environments
- **FinWise Bank**: Corporate customer data exposed through insider breach affecting 689,000 customers
- **Brazilian Healthcare Software**: Major healthcare technology supply chain element compromised by KillSec ransomware

## Attack Vectors and Techniques

- **Spyware Deployment**: Sophisticated spyware campaigns exploiting Apple vulnerabilities for advanced persistent access
- **Supply Chain Poisoning**: Injection of malicious bundle.js code into npm packages for credential harvesting
- **Memory Corruption**: Advanced RowHammer techniques bypassing DDR5 hardware protections in under two minutes
- **USB Worm Propagation**: SnakeDisk USB worm deployment for lateral movement and backdoor installation
- **Portal Impersonation**: Creation of fraudulent law enforcement accounts to bypass security controls
- **Insider Threats**: Former employee access to sensitive customer data after employment termination
- **Ransomware Operations**: Healthcare sector targeting with patient data exfiltration

## Threat Actor Activities

- **Mustang Panda**: China-aligned group deploying updated TONESHELL backdoor and SnakeDisk USB worm targeting Thailand IP addresses
- **UNC6040 and UNC6395**: Two distinct threat actors targeting Salesforce customers both separately and in coordinated tandem operations
- **KillSec Ransomware Group**: Targeting Brazilian healthcare software providers with patient data theft and encryption
- **npm Package Compromisers**: Unknown actors conducting widespread supply chain attacks across multiple package maintainers
- **Law Enforcement Portal Fraudsters**: Sophisticated actors creating fraudulent accounts in Google's law enforcement request system