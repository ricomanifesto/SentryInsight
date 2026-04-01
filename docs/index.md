# Exploitation Report

Critical exploitation activity is currently targeting enterprise infrastructure, with multiple zero-day vulnerabilities and supply chain attacks posing immediate threats to organizations worldwide. The most severe incidents include active exploitation of a zero-day vulnerability in TrueConf video conferencing software targeting Southeast Asian government networks, a critical Citrix NetScaler memory flaw being exploited in the wild, and a major supply chain attack compromising the Axios npm package affecting over 100 million weekly downloads. Additionally, threat actors have successfully breached Google's Vertex AI platform, Cisco development environments through the Trivy supply chain attack, and multiple government and healthcare systems. Iranian state-sponsored groups have escalated their operations using pseudo-ransomware tactics, while various APT groups continue targeting critical infrastructure across multiple sectors.

## Active Exploitation Details

### TrueConf Zero-Day Vulnerability
- **Description**: High-severity security flaw in TrueConf client video conferencing software being exploited as a zero-day
- **Impact**: Enables attackers to compromise government networks and potentially access sensitive communications
- **Status**: Actively exploited in targeted campaigns against Southeast Asian government entities

### Citrix NetScaler Memory Vulnerability
- **Description**: Critical severity memory flaw in Citrix NetScaler ADC and NetScaler Gateway appliances
- **Impact**: Allows attackers to obtain sensitive data from affected systems
- **Status**: Under active exploitation; CISA has ordered federal agencies to patch by Thursday
- **CVE ID**: CVE-2026-3055

### F5 BIG-IP Remote Code Execution Flaw
- **Description**: Vulnerability initially classified as denial-of-service but reclassified as remote code execution after exploitation evidence emerged
- **Impact**: Enables attackers to execute arbitrary code on affected F5 BIG-IP systems
- **Status**: Under active exploitation in the wild
- **CVE ID**: CVE-2025-53521

### Google Vertex AI Security Blind Spot
- **Description**: Security vulnerability in Google Cloud's Vertex AI platform allowing AI agents to be weaponized
- **Impact**: Attackers can gain unauthorized access to cloud data and private artifacts through compromised AI agents
- **Status**: Disclosed by researchers; exploitation potential demonstrated

### OpenAI ChatGPT Data Exfiltration Vulnerability
- **Description**: Previously unknown vulnerability allowing sensitive conversation data to be extracted without user consent
- **Impact**: Enables attackers to steal private ChatGPT conversations and potentially GitHub tokens through Codex
- **Status**: Patched by OpenAI after disclosure by Check Point researchers

## Affected Systems and Products

- **TrueConf Client**: Video conferencing software used by government entities in Southeast Asia
- **Citrix NetScaler ADC/Gateway**: Network appliances widely deployed in enterprise environments
- **F5 BIG-IP**: Application delivery controllers and load balancers
- **Google Vertex AI**: Machine learning platform and AI development environment
- **Axios npm Package**: JavaScript HTTP client library with 100+ million weekly downloads
- **OpenAI ChatGPT**: AI chatbot platform and associated Codex development tools
- **Cisco Development Environment**: Internal development systems accessed through Trivy compromise
- **AWS and Azure Cloud Instances**: Cloud infrastructure targeted by TeamPCP threat group
- **Dutch Finance Ministry Systems**: Government treasury banking portal and related infrastructure
- **CareCloud Healthcare Platform**: Healthcare IT systems containing patient data

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in TrueConf and initially F5 systems
- **Supply Chain Attacks**: Compromise of Axios npm package and Trivy affecting downstream users
- **Credential Theft and Reuse**: TeamPCP group using stolen credentials for rapid cloud environment compromise
- **AI Agent Weaponization**: Exploitation of over-privileged AI agents in Google Vertex AI platform
- **ClickFix Social Engineering**: DeepLoad malware campaign using fake error prompts to trick users
- **Typosquatting Domains**: Silver Fox group using fake domains impersonating trusted software brands
- **Pseudo-Ransomware Operations**: Iranian APTs blending state-sponsored and cybercriminal tactics
- **WebSocket Implant Deployment**: RoadK1ll malware enabling lateral movement across compromised networks

## Threat Actor Activities

- **Silver Fox Group**: Chinese-speaking threat actors expanding Asia campaign using AtlasCross RAT and typosquatted domains targeting software users
- **TeamPCP**: Cybercriminal group conducting rapid attacks on AWS, Azure, and SaaS instances using stolen credentials
- **Iranian APT Groups**: State-sponsored actors deploying pseudo-ransomware and reviving Pay2Key operations against US organizations
- **Government-Targeting Attackers**: Unknown threat actors exploiting TrueConf zero-day against Southeast Asian government networks
- **Supply Chain Attackers**: Multiple groups compromising popular development tools including Axios npm package and Trivy scanner
- **DeepLoad Campaign Operators**: Threat actors using AI-assisted obfuscation and WMI persistence for credential theft operations
- **Cisco Environment Attackers**: Threat actors leveraging Trivy compromise to breach Cisco development environments and steal source code
- **Healthcare Sector Attackers**: Groups targeting CareCloud and other healthcare IT firms for patient data theft