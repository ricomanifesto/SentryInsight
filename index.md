# Exploitation Report

Critical exploitation activity is currently underway across multiple platforms, with several high-severity vulnerabilities being actively targeted by threat actors. The most significant incidents include a zero-day vulnerability in Samsung Android devices that has been exploited in active attacks, a critical remote code execution flaw in Dassault manufacturing systems being exploited in the wild, and sophisticated spyware campaigns targeting Apple device users in France. Additionally, threat groups UNC6040 and UNC6395 are conducting data theft operations against Salesforce platforms, while a new ransomware strain has demonstrated capabilities to bypass UEFI Secure Boot protections. These exploitation activities span consumer devices, enterprise platforms, and critical infrastructure systems.

## Active Exploitation Details

### Samsung Android Zero-Day Vulnerability
- **Description**: A critical security vulnerability in Samsung Android devices that has been exploited in zero-day attacks
- **Impact**: Allows attackers to compromise Samsung Android devices through active exploitation
- **Status**: Fixed in Samsung's monthly security updates
- **CVE ID**: CVE-2025-21043

### Dassault DELMIA Apriso Remote Code Execution
- **Description**: Critical remote code execution flaw in DELMIA Apriso manufacturing operations management software
- **Impact**: Enables attackers to execute arbitrary code remotely on affected manufacturing systems
- **Status**: Actively exploited in the wild, CISA warning issued

### Apple Spyware Campaign
- **Description**: Fourth spyware campaign in 2025 targeting Apple device users in France
- **Impact**: Sophisticated surveillance operations targeting specific individuals
- **Status**: Active campaign confirmed by CERT-FR and Apple user notifications

### HybridPetya Ransomware UEFI Bypass
- **Description**: New ransomware strain capable of bypassing UEFI Secure Boot protections
- **Impact**: Can install malicious applications on the EFI System Partition, compromising boot security
- **Status**: Recently discovered active threat

### Cursor IDE Security Flaw
- **Description**: Critical security vulnerability in Cursor IDE that could expose user code to malware
- **Impact**: Automatic command execution vulnerability that could compromise development environments
- **Status**: Security flaw identified with mitigation guidance available

## Affected Systems and Products

- **Samsung Android Devices**: All Samsung Android devices prior to latest security updates
- **DELMIA Apriso**: Manufacturing operations management software used in industrial environments
- **Apple Devices**: iPhones and other Apple devices used by targeted individuals in France
- **UEFI Systems**: Systems with UEFI Secure Boot that may be vulnerable to HybridPetya ransomware
- **Cursor IDE**: Development environment used by software developers
- **Salesforce Platforms**: Enterprise customer relationship management systems

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched Samsung Android vulnerability
- **Remote Code Execution**: Network-based attacks against Dassault manufacturing systems
- **Spyware Deployment**: Sophisticated surveillance software targeting high-value individuals
- **UEFI Bypass**: Advanced ransomware technique circumventing boot-level security protections
- **Social Engineering**: Targeting of Salesforce platforms through credential theft and unauthorized access
- **Supply Chain Compromise**: Potential risks from undocumented radios in solar-powered infrastructure devices

## Threat Actor Activities

- **UNC6040**: Cybercriminal group targeting Salesforce platforms for data theft operations
- **UNC6395**: Second cybercriminal group conducting similar Salesforce-focused attacks with data exfiltration capabilities
- **HybridPetya Operators**: Ransomware group deploying advanced UEFI bypass techniques for system compromise
- **State-Sponsored Actors**: Sophisticated spyware campaigns targeting specific individuals in France, likely nation-state activity
- **Samsung Zero-Day Exploiters**: Unknown threat actors conducting active exploitation of Android devices