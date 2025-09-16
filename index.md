# Exploitation Report

Critical exploitation activity has been identified across multiple fronts, with sophisticated spyware campaigns leveraging Apple vulnerabilities, advanced memory-based attacks bypassing modern protections, and widespread supply chain compromises. The most significant threat involves CVE-2025-43300, an out-of-bounds vulnerability in Apple systems that has been actively exploited in sophisticated spyware attacks, prompting Apple to backport security fixes. Additionally, a new RowHammer attack variant called Phoenix has demonstrated the ability to bypass DDR5 memory protections in just 109 seconds, while supply chain attackers have compromised over 40 npm packages to steal credentials through malicious bundle.js files.

## Active Exploitation Details

### Apple Spyware Vulnerability
- **Description**: An out-of-bounds vulnerability in Apple systems that allows sophisticated spyware attacks
- **Impact**: Enables remote code execution and system compromise through spyware deployment
- **Status**: Actively exploited in the wild; Apple has backported fixes to address the vulnerability
- **CVE ID**: CVE-2025-43300

### Phoenix RowHammer Attack
- **Description**: Advanced RowHammer attack variant targeting DDR5 memory chips from SK Hynix that bypasses modern memory protections
- **Impact**: Can compromise system integrity by manipulating memory contents, potentially leading to privilege escalation and system takeover
- **Status**: Proof-of-concept demonstrated; affects modern DDR5 memory systems with advanced protections

### npm Supply Chain Attack
- **Description**: Coordinated supply chain attack targeting the npm registry through compromised packages containing malicious bundle.js files
- **Impact**: Credential theft and potential system compromise for developers and applications using affected packages
- **Status**: Over 40 packages compromised across multiple maintainers; ongoing threat to JavaScript development ecosystem

## Affected Systems and Products

- **Apple iOS/macOS Systems**: Devices vulnerable to CVE-2025-43300 spyware exploitation
- **DDR5 Memory Systems**: SK Hynix DDR5 memory chips susceptible to Phoenix RowHammer attacks
- **npm Registry**: Over 40 compromised packages affecting JavaScript developers and applications
- **Salesforce Platform**: Customer environments targeted by UNC6040 and UNC6395 threat actors
- **FinWise Bank Systems**: Corporate customer data exposed through insider breach affecting 689,000 individuals
- **Google Law Enforcement Portal**: LERS platform compromised through fraudulent account creation
- **Brazilian Healthcare Software**: Systems impacted by KillSec ransomware affecting healthcare supply chain

## Attack Vectors and Techniques

- **Spyware Deployment**: Exploitation of CVE-2025-43300 to deliver sophisticated spyware payloads to Apple devices
- **Memory Manipulation**: Phoenix RowHammer technique bypassing DDR5 protections in 109 seconds through precise memory hammering
- **Supply Chain Poisoning**: Injection of malicious bundle.js files into legitimate npm packages for credential harvesting
- **USB Worm Propagation**: SnakeDisk USB worm deployment for lateral movement and backdoor delivery
- **Insider Threats**: Former employee access to sensitive systems post-employment termination
- **Social Engineering**: Fraudulent account creation in law enforcement portals to bypass security controls

## Threat Actor Activities

- **Mustang Panda**: China-aligned group deploying updated TONESHELL backdoor and SnakeDisk USB worm targeting Thailand IP addresses with Yokai backdoor delivery
- **UNC6040 and UNC6395**: Threat actors specifically targeting Salesforce customers, operating both separately and in coordinated campaigns
- **KillSec Ransomware Group**: Targeting Brazilian healthcare software providers, compromising critical healthcare technology supply chain infrastructure
- **npm Supply Chain Attackers**: Coordinated group compromising multiple npm package maintainers for widespread credential theft operations