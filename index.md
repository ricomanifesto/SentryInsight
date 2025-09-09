# Exploitation Report

The cybersecurity landscape is currently experiencing significant supply chain attacks targeting popular development platforms and code repositories. Multiple high-impact incidents have emerged involving compromised JavaScript packages with billions of weekly downloads, GitHub account breaches leading to widespread data theft, and sophisticated malware campaigns designed to evade security tools. These attacks demonstrate a concerning trend where threat actors are targeting the software development ecosystem to achieve maximum impact through supply chain compromise, affecting thousands of downstream users and organizations.

## Active Exploitation Details

### JavaScript Package Supply Chain Attack
- **Description**: Attackers compromised at least 18 popular JavaScript code packages through a phishing attack against a maintainer's account, injecting malicious software designed to steal cryptocurrency
- **Impact**: The compromised packages collectively receive over 2.6 billion weekly downloads, potentially affecting millions of users and applications that depend on these packages
- **Status**: Attack was detected and packages were secured, but the brief compromise window allowed widespread distribution of malicious code

### GhostAction GitHub Supply Chain Attack
- **Description**: A sophisticated supply chain attack targeting GitHub repositories that successfully compromised and stole 3,325 secrets including API keys, tokens, and credentials
- **Impact**: Stolen secrets include PyPI tokens, npm tokens, DockerHub credentials, GitHub tokens, Cloudflare keys, and AWS access keys, providing attackers with extensive access to cloud infrastructure and services
- **Status**: Attack has been identified and documented, but the full scope of compromised systems remains under investigation

### Salesloft GitHub Repository Breach
- **Description**: Attackers initially breached Salesloft's GitHub account in March, subsequently stealing Drift OAuth tokens that were later weaponized in August for widespread Salesforce data theft attacks
- **Impact**: The breach enabled attackers to access hundreds of Salesforce instances, leading to significant data theft across multiple organizations
- **Status**: Company has disclosed the incident and is working to remediate the impact of the compromised OAuth tokens

### MostereRAT Malware Campaign
- **Description**: A sophisticated remote access trojan designed to blend into legitimate system processes while actively blocking and disabling endpoint detection and response (EDR) security tools
- **Impact**: Provides threat actors with long-term, persistent access to Windows systems while evading detection by security software
- **Status**: Actively being used in ongoing campaigns targeting Windows environments

## Affected Systems and Products

- **JavaScript/Node.js Ecosystem**: Over 18 popular npm packages with collective downloads exceeding 2.6 billion per week
- **GitHub Repositories**: Thousands of repositories potentially affected by credential theft and unauthorized access
- **Salesforce Instances**: Hundreds of Salesforce environments compromised through stolen OAuth tokens
- **Windows Systems**: Targeted by MostereRAT malware for persistent access and EDR evasion
- **Cisco ASA Devices**: Experiencing increased network scanning activity suggesting potential upcoming exploitation
- **Lovesac Customer Data**: Personal information exposed in confirmed data breach following ransomware attack claims

## Attack Vectors and Techniques

- **Phishing Attacks**: Used to compromise maintainer accounts and gain access to popular code repositories
- **Supply Chain Injection**: Malicious code inserted into legitimate packages to reach maximum number of downstream users
- **OAuth Token Theft**: Stolen authentication tokens used to access cloud services and customer data
- **EDR Evasion**: Advanced techniques to disable and bypass endpoint security tools
- **Network Reconnaissance**: Large-scale scanning of network infrastructure to identify vulnerable devices
- **Social Engineering**: Targeting developers and maintainers with access to critical infrastructure

## Threat Actor Activities

- **Supply Chain Attackers**: Conducting coordinated campaigns against JavaScript package maintainers to inject cryptocurrency-stealing malware into widely-used code libraries
- **GitHub Credential Harvesters**: Operating sophisticated campaigns to steal thousands of API keys and access tokens from development repositories
- **Ransomware Groups**: Targeting furniture retailer Lovesac and potentially other organizations with data encryption and theft operations
- **Advanced Persistent Threat Groups**: Deploying MostereRAT malware for long-term access to Windows environments while evading security detection
- **Network Reconnaissance Actors**: Conducting large-scale scanning operations against Cisco ASA devices, potentially preparing for future exploitation campaigns