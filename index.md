# Exploitation Report

Current exploitation activity reveals a significant surge in supply chain attacks, critical infrastructure vulnerabilities, and sophisticated social engineering campaigns. Notable incidents include North Korean threat actors successfully compromising the Axios npm package through targeted social engineering, resulting in a supply chain attack affecting potentially millions of developers. Additionally, attackers have exploited CVE-2025-55182 (React2Shell vulnerability) to compromise 766 Next.js hosts in a large-scale credential harvesting operation. Critical vulnerabilities in Cisco IMC systems and F5 BIG-IP APM instances are being actively exploited, with over 14,000 exposed instances remaining vulnerable to remote code execution attacks. The Drift Protocol suffered a devastating $285 million loss through a sophisticated attack where North Korean hackers gained Security Council administrative powers.

## Active Exploitation Details

### React2Shell Vulnerability in Next.js
- **Description**: Critical vulnerability allowing remote code execution in Next.js applications
- **Impact**: Large-scale credential harvesting, theft of database credentials, SSH private keys, and Amazon Web Services credentials
- **Status**: Actively exploited with 766 confirmed compromised hosts
- **CVE ID**: CVE-2025-55182

### Cisco Integrated Management Controller Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in Cisco IMC allowing unauthenticated remote access
- **Impact**: Attackers can gain administrative access to systems without authentication
- **Status**: Recently patched but exploitation ongoing
- **CVSS Score**: 9.8 (Critical)

### F5 BIG-IP APM Remote Code Execution
- **Description**: Critical vulnerability in F5 BIG-IP Application Policy Manager (APM) instances
- **Impact**: Remote code execution allowing complete system compromise
- **Status**: Over 14,000 instances remain exposed and vulnerable to ongoing attacks

### Progress ShareFile Pre-Authentication Chain
- **Description**: Two vulnerabilities that can be chained together for unauthenticated attacks
- **Impact**: Pre-authentication remote code execution and file exfiltration from enterprise environments
- **Status**: Recently disclosed with proof-of-concept available

## Affected Systems and Products

- **Next.js Applications**: 766 confirmed compromised hosts running vulnerable React implementations
- **Cisco IMC Systems**: Integrated Management Controllers across enterprise infrastructure
- **F5 BIG-IP APM**: Over 14,000 exposed instances vulnerable to remote code execution
- **Progress ShareFile**: Enterprise-grade secure file transfer solutions
- **npm Package Ecosystem**: Axios package and potentially other packages in supply chain attacks
- **iOS/Android Mobile Apps**: SparkCat malware variants targeting cryptocurrency wallet applications
- **Solana Blockchain Platform**: Drift Protocol losing $285 million through administrative takeover
- **European Commission Cloud Infrastructure**: Breach affecting 30 EU entities
- **Stryker Corporation Medical Systems**: Data-wiping attacks on medical technology infrastructure

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Social engineering of open-source maintainers to inject malicious code into popular packages
- **Social Engineering**: Highly targeted campaigns against software developers and administrators
- **Administrative Privilege Escalation**: Gaining Security Council or administrative powers through sophisticated attacks
- **Credential Harvesting**: Large-scale operations stealing database credentials, SSH keys, and cloud service credentials
- **Mobile App Store Infiltration**: Malicious applications bypassing Apple App Store and Google Play Store security controls
- **Authentication Bypass**: Exploiting critical flaws to gain unauthorized administrative access
- **Pre-Authentication Attacks**: Chaining vulnerabilities to achieve remote code execution without credentials
- **Residential Proxy Abuse**: Using legitimate residential IP addresses to evade detection in 78% of malicious sessions

## Threat Actor Activities

- **UNC1069 (North Korean)**: Orchestrated sophisticated social engineering campaign against Axios maintainer leading to npm supply chain compromise
- **DPRK-linked Groups**: Successfully executed $285 million theft from Drift Protocol through administrative takeover and durable nonce attacks
- **TeamPCP**: Attributed to European Commission cloud infrastructure breach affecting 30 EU entities
- **REF1695 Operation**: Financially motivated group using fake installers to deploy RATs and cryptocurrency miners since November 2023
- **Augmented Marauder**: Conducting multipronged banking trojan campaigns targeting Spanish-speaking users across Latin America
- **Iranian-linked Attackers**: Claimed responsibility for data-wiping attack against Stryker Corporation medical technology systems
- **Unknown Sophisticated Actors**: Exploiting Claude Code source code leak to distribute Vidar information-stealing malware through fake GitHub repositories