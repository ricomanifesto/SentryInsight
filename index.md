# Exploitation Report

The current threat landscape reveals multiple active exploitation campaigns targeting critical enterprise infrastructure and developer ecosystems. Most notably, threat actors are conducting sophisticated phishing operations targeting Microsoft 365 environments using advanced techniques like Axios abuse and 2FA bypass kits. A major supply chain compromise affected 20 popular npm packages with 2 billion weekly downloads after a maintainer's account was compromised through phishing. Additionally, new Android malware variants are emerging with enhanced banking fraud capabilities, while cryptojacking campaigns continue to exploit misconfigured Docker APIs through TOR networks. Several critical vulnerabilities in enterprise software, including maximum severity flaws in SAP NetWeaver, are being actively addressed by vendors.

## Active Exploitation Details

### Microsoft 365 Phishing Campaign
- **Description**: Advanced phishing attacks leveraging HTTP client tools like Axios in conjunction with Microsoft's Direct Send feature to create highly efficient attack pipelines
- **Impact**: Threat actors can bypass 2FA protections and gain unauthorized access to Microsoft 365 environments
- **Status**: Active exploitation with Salty 2FA kits being used to circumvent multi-factor authentication

### npm Supply Chain Attack
- **Description**: Compromise of 20 popular npm packages affecting 2 billion weekly downloads through a maintainer account takeover
- **Impact**: Potential code injection and malicious payload distribution across countless downstream applications and systems
- **Status**: Active compromise following successful phishing attack against maintainer Josh Junon (Qix)

### SAP NetWeaver Command Execution Vulnerability
- **Description**: Maximum severity command execution flaw in SAP NetWeaver software solution
- **Impact**: Remote code execution capabilities allowing attackers to execute arbitrary commands on affected systems
- **Status**: Recently patched by SAP as part of 21 vulnerability fixes, including three critical severity issues

### RatOn Android Malware
- **Description**: Sophisticated Android malware that evolved from basic NFC relay attack tool to full remote access trojan with Automated Transfer System capabilities
- **Impact**: Banking fraud through NFC relay attacks and comprehensive device compromise with remote access capabilities
- **Status**: Active in the wild with enhanced fraud capabilities

## Affected Systems and Products

- **Microsoft 365**: Exchange Online and Microsoft Teams environments targeted by phishing campaigns
- **npm Ecosystem**: 20 compromised packages affecting 2 billion weekly downloads and countless downstream applications
- **SAP NetWeaver**: Enterprise software solution with maximum severity command execution vulnerability
- **Android Devices**: Mobile platforms targeted by RatOn malware for banking fraud and remote access
- **Docker APIs**: Misconfigured Docker APIs being exploited for cryptojacking operations
- **Microsoft Exchange Online**: Anti-spam service causing legitimate URL blocking and email quarantine

## Attack Vectors and Techniques

- **Phishing with 2FA Bypass**: Advanced phishing campaigns using Salty 2FA kits to circumvent multi-factor authentication protections
- **HTTP Client Abuse**: Exploitation of legitimate tools like Axios combined with Microsoft Direct Send for attack pipeline creation
- **Supply Chain Compromise**: Targeting of package maintainers through phishing to compromise widely-used software repositories
- **NFC Relay Attacks**: Android malware leveraging Near Field Communication for banking fraud operations
- **TOR-Based Cryptojacking**: Use of TOR networks to obfuscate cryptojacking operations targeting misconfigured Docker APIs
- **Social Engineering**: Sophisticated phishing targeting developers and maintainers of critical software packages

## Threat Actor Activities

- **Microsoft 365 Phishing Groups**: Conducting highly efficient phishing campaigns targeting enterprise Microsoft 365 environments with advanced 2FA bypass techniques
- **Supply Chain Attackers**: Successfully compromised maintainer accounts to inject malicious code into popular npm packages with massive reach
- **Android Banking Fraudsters**: Deploying RatOn malware with enhanced NFC relay capabilities for automated banking fraud operations
- **Cryptojacking Operators**: Expanding TOR-based cryptojacking campaigns targeting misconfigured Docker APIs across cloud infrastructure