# Exploitation Report

The cybersecurity landscape reveals several critical exploitation activities currently impacting organizations worldwide. CISA has issued warnings about active exploitation of a critical remote code execution vulnerability in Dassault's DELMIA Apriso manufacturing operations management application. Concurrently, the FBI has released flash alerts regarding two sophisticated threat groups, UNC6040 and UNC6395, actively targeting Salesforce platforms for data theft operations. Additionally, malicious actors are leveraging software distribution channels, with WhiteCobra flooding VSCode marketplaces with cryptocurrency-stealing extensions, and Chinese-speaking threat actors employing SEO poisoning campaigns to distribute HiddenGh0st, Winos, and kkRAT malware. A new ransomware variant called HybridPetya has emerged with the capability to bypass UEFI Secure Boot protections, while VoidProxy, a newly discovered phishing-as-a-service platform, is targeting Microsoft 365 and Google accounts. The French CERT-FR has also highlighted ongoing Apple spyware activities following previous zero-day disclosures.

## Active Exploitation Details

### DELMIA Apriso Remote Code Execution Vulnerability
- **Description**: Critical remote code execution flaw affecting DELMIA Apriso, a manufacturing operations management (MOM) application developed by Dassault
- **Impact**: Attackers can execute arbitrary code remotely on vulnerable systems, potentially compromising entire manufacturing environments
- **Status**: Actively exploited in the wild, CISA has added this vulnerability to its Known Exploited Vulnerabilities catalog

### Apple Zero-Day Spyware Vulnerability
- **Description**: Sophisticated zero-day vulnerability previously disclosed by Apple, used in targeted spyware attacks
- **Impact**: Enables sophisticated surveillance and data collection against targeted individuals
- **Status**: Previously patched by Apple, but French CERT-FR advisory provides additional context on exploitation activities

## Affected Systems and Products

- **DELMIA Apriso**: Manufacturing operations management application vulnerable to remote code execution attacks
- **Salesforce Platforms**: Customer relationship management environments targeted by UNC6040 and UNC6395 threat groups
- **Visual Studio Code Extensions**: Development environment compromised through malicious extensions in VSCode, Cursor, and Windsurf marketplaces
- **Microsoft 365 and Google Accounts**: Cloud productivity platforms targeted by VoidProxy phishing-as-a-service operations
- **UEFI Systems**: Modern computers with Secure Boot functionality vulnerable to HybridPetya ransomware bypass techniques
- **Apple Devices**: iPhones and other Apple products previously targeted in sophisticated spyware campaigns
- **Chinese Software Distribution Sites**: Fake software repositories used to distribute malware through SEO manipulation

## Attack Vectors and Techniques

- **Remote Code Execution**: Direct exploitation of DELMIA Apriso vulnerability for system compromise
- **Phishing-as-a-Service**: VoidProxy platform providing turnkey phishing solutions targeting cloud accounts with SSO bypass capabilities
- **Supply Chain Compromise**: Malicious VSCode extensions distributed through official marketplaces to steal cryptocurrency
- **SEO Poisoning**: Manipulation of search engine rankings to direct users to malicious software download sites
- **UEFI Secure Boot Bypass**: HybridPetya ransomware technique to install malicious applications on EFI System Partition
- **Salesforce Environment Infiltration**: Direct targeting of customer relationship management platforms for data exfiltration
- **GitHub Pages Abuse**: Leveraging legitimate GitHub hosting for malware distribution infrastructure

## Threat Actor Activities

- **UNC6040 and UNC6395**: Sophisticated threat groups actively compromising Salesforce environments for data theft and extortion purposes, with FBI releasing specific indicators of compromise
- **WhiteCobra**: Malicious actor flooding development environment marketplaces with 24 cryptocurrency-stealing extensions targeting VSCode, Cursor, and Windsurf users
- **Chinese-Speaking Threat Groups**: Conducting SEO poisoning campaigns distributing HiddenGh0st, Winos, and kkRAT malware specifically targeting Chinese-speaking users through manipulated search results
- **HybridPetya Operators**: Ransomware group developing advanced techniques to bypass modern security features like UEFI Secure Boot for system-level compromise
- **VoidProxy Service Providers**: Cybercriminals offering phishing-as-a-service platform specifically designed to bypass third-party single sign-on protections
- **Apple-Targeting Spyware Groups**: Sophisticated actors previously engaged in zero-day exploitation for targeted surveillance operations against specific individuals