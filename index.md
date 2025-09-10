# Exploitation Report

Based on the provided security articles, current exploitation activity centers primarily around Microsoft's September 2025 Patch Tuesday release, which addressed 81 vulnerabilities including two zero-day vulnerabilities that were publicly disclosed. Additionally, significant cybercriminal activities have been documented involving major supply chain attacks against NPM packages, ransomware operations, and large-scale cybercrime marketplaces. The threat landscape also includes ongoing attacks against exposed Docker APIs and substantial sanctions against Southeast Asian cyber scam networks that have stolen over $10 billion from Americans.

## Active Exploitation Details

### Microsoft Zero-Day Vulnerabilities
- **Description**: Two publicly disclosed zero-day vulnerabilities were included in Microsoft's September 2025 Patch Tuesday release
- **Impact**: Attackers could exploit these vulnerabilities before patches were available, potentially allowing for system compromise and unauthorized access
- **Status**: Patches released as part of Microsoft's September 2025 security update addressing 81 total flaws

### Escalation of Privilege Vulnerabilities
- **Description**: Nearly half of the vulnerabilities disclosed in Microsoft's September security update enable escalation of privileges, including one publicly known bug
- **Impact**: Attackers can elevate their access permissions within compromised systems, potentially gaining administrative control
- **Status**: Patches available through Microsoft's September 2025 security updates

### NPM Supply Chain Attack
- **Description**: Threat actors compromised the NPM account of developer "Qix" through phishing, then published poisoned versions of 18 popular open-source packages
- **Impact**: Affected packages account for more than 2 billion weekly downloads, creating massive potential for widespread compromise of applications using these packages
- **Status**: Attack has been contained but demonstrated the significant risk to software supply chains

### Docker API Exploitation
- **Description**: Threat actors are actively targeting exposed Docker APIs with updated malicious tooling that includes more dangerous functionality
- **Impact**: Could establish complex botnets and compromise containerized environments
- **Status**: Ongoing attacks with attackers using Tor networks to hide their activities

## Affected Systems and Products

- **Microsoft Windows Operating Systems**: Windows 10 and Windows 11 versions affected by 81 vulnerabilities in September 2025 Patch Tuesday
- **Microsoft Software Products**: Various Microsoft applications and services covered in the security update
- **NPM Package Ecosystem**: 18 popular open-source packages with over 2 billion weekly downloads compromised
- **Docker Environments**: Systems with exposed Docker APIs vulnerable to botnet deployment and compromise
- **Third-party Platforms**: Qantas customers affected through compromise of third-party platform used by the airline

## Attack Vectors and Techniques

- **Phishing Attacks**: Used to compromise developer accounts, specifically targeting NPM package maintainers
- **Supply Chain Poisoning**: Injection of malicious code into legitimate software packages distributed through NPM
- **API Exploitation**: Direct targeting of exposed Docker APIs to deploy malicious payloads
- **Privilege Escalation**: Exploitation of elevation of privilege vulnerabilities to gain higher system access
- **Tor Network Obfuscation**: Use of Tor networks to hide attacker infrastructure and maintain anonymity

## Threat Actor Activities

- **Southeast Asian Cyber Scam Networks**: Operations that stole over $10 billion from Americans, now subject to U.S. Treasury sanctions
- **NPM Supply Chain Attackers**: Sophisticated threat actors capable of compromising developer accounts and poisoning widely-used software packages
- **Docker API Threat Actors**: Groups developing advanced botnet infrastructure through exploitation of containerized environments
- **Ransomware Operations**: Ukrainian national Volodymyr Viktorovich Tymoshchuk charged for administering LockerGoga, MegaCortex, and Nefilim ransomware operations
- **BlackDB Cybercrime Marketplace**: Kosovo national Liridon Masurica pleaded guilty to operating this cybercrime marketplace active since 2018