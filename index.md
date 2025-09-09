# Exploitation Report

The current threat landscape is dominated by sophisticated supply chain attacks targeting development platforms and repositories. Multiple high-impact campaigns have emerged, including the GhostAction GitHub attack that compromised 3,325 secrets and the largest supply chain attack in history affecting npm packages with over 2.6 billion weekly downloads. These incidents highlight the critical vulnerability of software development infrastructure, with attackers successfully stealing authentication tokens, API keys, and credentials that enable widespread downstream compromises. Additionally, advanced malware campaigns like MostereRAT and GPUGate are employing sophisticated evasion techniques, including EDR-killing capabilities and abuse of legitimate platforms like Google Ads and GitHub to deliver malicious payloads to targeted organizations.

## Active Exploitation Details

### GhostAction GitHub Supply Chain Attack
- **Description**: A sophisticated supply chain attack targeting GitHub repositories that successfully compromised 3,325 secrets including authentication tokens and API keys
- **Impact**: Attackers gained access to PyPI, npm, DockerHub, GitHub tokens, Cloudflare, and AWS keys, enabling widespread downstream attacks
- **Status**: Active exploitation confirmed with significant impact across multiple platforms and services

### npm Package Supply Chain Attack
- **Description**: The largest supply chain attack in history targeting npm packages with over 2.6 billion weekly downloads through compromised maintainer accounts
- **Impact**: Malware injection into widely-used packages affecting millions of downstream applications and users
- **Status**: Active exploitation with massive scale impact across the JavaScript ecosystem

### MostereRAT Malware Campaign
- **Description**: Sophisticated EDR-killing malware designed to maintain long-term persistent access on Windows systems
- **Impact**: Blocks security tools and establishes persistent backdoor access for threat actors
- **Status**: Active deployment in targeted campaigns against Windows environments

### GPUGate Malware Campaign
- **Description**: Advanced malware campaign leveraging Google Ads and fake GitHub commits to target IT firms
- **Impact**: Delivers malicious payloads to organizations searching for legitimate tools and software
- **Status**: Active exploitation using search engine advertising and repository manipulation

### Salesloft GitHub Account Compromise
- **Description**: GitHub repository breach that led to theft of Drift OAuth tokens and subsequent Salesforce data theft attacks
- **Impact**: Compromise of hundreds of Salesforce instances and data theft affecting 22 companies
- **Status**: Initial breach occurred in March, with downstream attacks continuing through August

## Affected Systems and Products

- **GitHub Repositories**: Widespread compromise of development repositories and associated secrets
- **npm Package Registry**: Over 2.6 billion weekly downloads affected by malicious package injections
- **Salesforce Instances**: Hundreds of instances compromised through stolen OAuth tokens
- **Windows Systems**: Targeted by MostereRAT for persistent access and security tool evasion
- **PyPI, DockerHub**: Authentication tokens and credentials compromised in GhostAction attack
- **AWS and Cloudflare**: API keys and access credentials stolen in supply chain attacks
- **IT Firms**: Specifically targeted by GPUGate campaign through malicious advertising

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Injection of malicious code into legitimate software packages and repositories
- **OAuth Token Theft**: Compromise of authentication tokens to gain unauthorized access to cloud services
- **Search Engine Advertising Abuse**: Use of paid Google Ads to deliver malware to users searching for legitimate tools
- **Repository Manipulation**: Creation of fake GitHub commits and repositories to appear legitimate
- **EDR Evasion**: Advanced techniques to disable and bypass endpoint detection and response systems
- **Credential Harvesting**: Large-scale theft of API keys, tokens, and authentication credentials
- **Maintainer Account Compromise**: Targeting of package maintainer accounts to inject malicious code

## Threat Actor Activities

- **GhostAction Campaign**: Sophisticated actors targeting GitHub infrastructure with focus on credential theft and supply chain compromise
- **npm Supply Chain Attackers**: Highly capable threat actors executing the largest recorded supply chain attack against JavaScript ecosystem
- **MostereRAT Operators**: Advanced persistent threat actors deploying EDR-killing malware for long-term access
- **GPUGate Campaign**: Targeted attacks against IT firms using multi-vector approach including advertising abuse and repository manipulation
- **Salesloft Attackers**: Threat actors conducting multi-stage attacks from initial GitHub compromise to widespread Salesforce data theft