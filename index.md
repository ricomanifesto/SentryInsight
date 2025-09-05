# Exploitation Report

Critical zero-day exploitation activity has been identified targeting Sitecore content management systems, with threat actors deploying WeepSteel reconnaissance malware and backdoors through ViewState deserialization attacks. Additionally, Russian state-sponsored group APT28 has been actively deploying the NotDoor Outlook backdoor against NATO country organizations, while the GhostRedirector threat cluster has compromised at least 65 Windows servers using sophisticated IIS modules and backdoors. These activities represent significant ongoing threats to enterprise infrastructure and government entities.

## Active Exploitation Details

### Sitecore Zero-Day Vulnerability
- **Description**: A zero-day vulnerability in legacy Sitecore deployments that allows threat actors to exploit exposed ASP.NET machine keys for remote injection and deserialization attacks
- **Impact**: Attackers can deploy WeepSteel reconnaissance malware and establish persistent backdoors on compromised systems
- **Status**: Actively exploited in the wild, represents the latest example of ViewState weaponization

### NotDoor Outlook Backdoor
- **Description**: A sophisticated Microsoft Outlook backdoor developed and deployed by Russian APT28 group targeting organizations in NATO countries
- **Impact**: Provides persistent access to corporate email systems and enables data exfiltration from multiple business sectors
- **Status**: Active campaign targeting companies across different sectors in NATO member states

### Windows Server Compromise via Rungan Backdoor
- **Description**: GhostRedirector threat cluster exploiting Windows servers using the Rungan backdoor in combination with the Gamshen IIS module
- **Impact**: Complete server compromise allowing for malicious redirections and search engine manipulation for gambling site promotion
- **Status**: At least 65 Windows servers confirmed compromised, primarily located in Brazil

## Affected Systems and Products

- **Sitecore CMS**: Legacy deployments vulnerable to ViewState deserialization attacks through exposed ASP.NET machine keys
- **Microsoft Outlook**: Corporate email systems targeted by APT28's NotDoor backdoor across NATO countries
- **Windows Servers**: At least 65 servers compromised by GhostRedirector, primarily running IIS web services
- **PowerSchool Education Platform**: 62 million students affected by data breach, including 880,000 Texas residents
- **Chess.com Platform**: User data compromised through third-party file transfer application breach
- **Bridgestone Americas**: Manufacturing operations disrupted by confirmed cyberattack

## Attack Vectors and Techniques

- **ViewState Deserialization**: Exploitation of exposed ASP.NET machine keys to achieve remote code execution and malware deployment
- **Email System Backdoors**: APT28 utilizing NotDoor to maintain persistent access to corporate Outlook environments
- **IIS Module Injection**: GhostRedirector deploying malicious Gamshen IIS modules to manipulate web traffic and boost gambling site rankings
- **Third-Party Application Compromise**: Attackers targeting file transfer applications to gain access to primary platforms
- **Search Engine Manipulation**: Injection of malicious links to artificially boost search rankings for target gambling sites

## Threat Actor Activities

- **APT28 (Russian State-Sponsored)**: Conducting targeted campaigns against NATO country organizations using the NotDoor Outlook backdoor across multiple business sectors
- **GhostRedirector**: Previously undocumented threat cluster focusing on Windows server compromise for search engine manipulation and gambling site promotion, with primary activity in Brazil
- **Sitecore Attackers**: Unidentified threat actors exploiting zero-day vulnerabilities to deploy WeepSteel reconnaissance malware and establish persistent access to content management systems
- **Phishing-as-a-Service Operations**: Global enterprise operating undetected on Google and Cloudflare infrastructure for over three years using advanced cloaking techniques