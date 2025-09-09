# Exploitation Report

The cybersecurity landscape is currently experiencing significant supply chain attacks targeting popular development platforms and packages. Most notably, a sophisticated campaign has compromised 20 popular npm packages with over 2 billion weekly downloads through a phishing attack against maintainer Josh Junon. Additionally, multiple organizations including Plex, Salesloft, and Lovesac have suffered data breaches, while threat actors are conducting widespread reconnaissance against Cisco ASA devices and leveraging advanced malware like MostereRAT to evade security tools.

## Active Exploitation Details

### npm Package Supply Chain Attack
- **Description**: A phishing attack compromised maintainer Josh Junon's account, leading to the injection of malicious code into 20 popular npm packages
- **Impact**: Attackers can steal cryptocurrency and potentially execute arbitrary code on systems using these packages
- **Status**: Packages were briefly compromised with malicious software designed to steal crypto assets

### Plex Data Breach
- **Description**: Media streaming platform suffered a data breach where attackers accessed customer authentication data from databases
- **Impact**: Customer authentication credentials were stolen, requiring password resets
- **Status**: Plex is warning customers to reset passwords following the breach

### Salesloft GitHub Account Compromise
- **Description**: Breach occurred through GitHub account compromise leading to a massive supply chain attack
- **Impact**: Hundreds of Salesforce instances were compromised through stolen OAuth tokens
- **Status**: Active breach with widespread impact on connected Salesforce environments

### GhostAction GitHub Supply Chain Attack
- **Description**: New supply chain attack targeting GitHub repositories and associated secrets
- **Impact**: 3,325 secrets stolen including PyPI, npm, DockerHub, GitHub tokens, Cloudflare, and AWS keys
- **Status**: Active campaign with significant credential theft

### MostereRAT Malware Campaign
- **Description**: Sophisticated malware designed to blend in with legitimate processes while blocking security tools
- **Impact**: Provides persistent access on Windows systems while evading endpoint detection and response (EDR) tools
- **Status**: Active threat actor campaign using EDR-killing capabilities

## Affected Systems and Products

- **npm Packages**: 20 popular JavaScript packages with 2+ billion weekly downloads compromised
- **Plex Platform**: Customer authentication databases breached
- **Salesloft**: GitHub repositories and connected Salesforce instances affected
- **GitHub Repositories**: Targeted in GhostAction campaign for secret extraction
- **Cisco ASA Devices**: Subject to increased network scanning activity
- **Windows Systems**: Targeted by MostereRAT malware for persistent access
- **Lovesac**: Customer data exposed in ransomware attack

## Attack Vectors and Techniques

- **Phishing Attacks**: Used to compromise maintainer accounts for supply chain attacks
- **Supply Chain Compromise**: Malicious code injection into popular software packages
- **GitHub Account Takeover**: Leveraged to access repositories and steal OAuth tokens
- **Network Reconnaissance**: Large-scale scanning of Cisco ASA devices
- **EDR Evasion**: MostereRAT uses sophisticated techniques to bypass security tools
- **Ransomware Operations**: Targeting furniture retailers and other businesses

## Threat Actor Activities

- **Salt Typhoon/UNC4841**: China-linked threat actors with 45 previously unreported domains dating back to May 2020, indicating long-term cyber espionage operations
- **npm Package Attackers**: Conducted targeted phishing against package maintainers to compromise supply chain
- **MostereRAT Operators**: Deploying sophisticated malware for persistent Windows system access
- **GhostAction Campaign**: Systematic targeting of GitHub repositories to extract sensitive credentials and tokens
- **Cisco ASA Scanners**: Conducting widespread reconnaissance that may indicate preparation for future exploitation