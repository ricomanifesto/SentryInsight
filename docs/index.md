# Exploitation Report

Critical exploitation activity is currently targeting infrastructure components and popular software packages across multiple sectors. The most severe active threats include a zero-day vulnerability in TrueConf video conferencing software being exploited against Southeast Asian government networks, a memory corruption flaw in Citrix NetScaler appliances under active attack, and an F5 BIG-IP vulnerability that has been reclassified as remote code execution. Additionally, supply chain attacks have compromised the popular Axios npm package and the Trivy security scanner, while threat actors continue to leverage social engineering tactics like ClickFix to deploy sophisticated malware. These incidents demonstrate ongoing targeting of both enterprise infrastructure and open-source ecosystems.

## Active Exploitation Details

### TrueConf Zero-Day Vulnerability
- **Description**: High-severity security flaw in TrueConf client video conferencing software being exploited as a zero-day
- **Impact**: Enables attackers to compromise video conferencing systems in government environments
- **Status**: Currently under active exploitation targeting Southeast Asian government entities

### Citrix NetScaler Memory Corruption Flaw
- **Description**: Critical severity memory vulnerability in Citrix NetScaler ADC and NetScaler Gateway appliances
- **Impact**: Allows attackers to obtain sensitive data from affected systems
- **Status**: Actively exploited in attacks, CISA has ordered federal agencies to patch by Thursday
- **CVE ID**: CVE-2026-3055

### F5 BIG-IP Remote Code Execution Vulnerability
- **Description**: Originally disclosed as a denial-of-service flaw but reclassified as remote code execution vulnerability
- **Impact**: Enables attackers to execute arbitrary code on affected F5 BIG-IP systems
- **Status**: Under active exploitation, severity upgraded from high to critical
- **CVE ID**: CVE-2025-53521

### Axios npm Package Supply Chain Attack
- **Description**: Compromise of the Axios HTTP client npm package with over 100 million weekly downloads
- **Impact**: Cross-platform remote access trojan deployment to Linux, Windows, and macOS systems
- **Status**: Malicious versions published through compromised npm account

### DeepLoad Malware Campaign
- **Description**: AI-powered malware using ClickFix social engineering tactics and WMI persistence
- **Impact**: Steals browser credentials and evades detection through AI-generated obfuscation
- **Status**: Active campaign targeting users through social engineering

## Affected Systems and Products

- **TrueConf Client**: Video conferencing software used by government entities in Southeast Asia
- **Citrix NetScaler ADC/Gateway**: Network appliances used for application delivery and secure remote access
- **F5 BIG-IP**: Application delivery controllers and load balancers
- **Axios npm Package**: JavaScript HTTP client library with massive developer adoption
- **Trivy Security Scanner**: Container and code vulnerability scanner used in CI/CD pipelines
- **Google Cloud Vertex AI**: Machine learning platform with potential data exposure vulnerabilities
- **OpenAI ChatGPT**: Conversational AI platform with data exfiltration vulnerabilities
- **Telegram Messaging App**: Communication platform with reported critical vulnerability

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in enterprise software
- **Supply Chain Compromise**: Injection of malicious code into trusted software packages and development tools
- **ClickFix Social Engineering**: Deceptive tactics tricking users into executing malicious commands
- **Memory Corruption Attacks**: Exploitation of buffer overflows and memory management flaws
- **Credential Theft**: Targeting of stored authentication data in browsers and applications
- **Cross-Platform Deployment**: Malware designed to operate across Windows, Linux, and macOS environments
- **AI-Assisted Obfuscation**: Use of artificial intelligence to generate evasive malware code

## Threat Actor Activities

- **Silver Fox Group**: Expanding Asia-focused cyber campaign using AtlasCross RAT and typosquatted domains targeting Chinese-speaking users
- **Iranian APT Groups**: Deploying pseudo-ransomware and reviving Pay2Key operations targeting high-impact US organizations
- **Southeast Asian Campaign**: Unknown threat actors exploiting TrueConf zero-day against government networks
- **Supply Chain Attackers**: Sophisticated actors compromising popular open-source packages like Axios and Trivy
- **Cryptocurrency Thieves**: Hackers stealing over $53 million from Uranium Finance crypto exchange
- **Government Network Infiltrators**: Attackers breaching Dutch Finance Ministry systems and taking treasury banking portals offline