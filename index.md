# Exploitation Report

Current threat landscape reveals significant active exploitation targeting multiple critical systems and platforms. Two high-severity Ivanti EPMM vulnerabilities are being actively exploited with custom malware strains discovered in organizational networks. Google has patched its sixth Chrome zero-day vulnerability exploited in attacks this year, specifically **CVE-2025-10585** affecting the V8 JavaScript engine. Threat actors are leveraging sophisticated techniques including AI-generated scripts for malware deployment, collaborative operations between Russian APT groups, and large-scale supply chain attacks. Notable incidents include data breaches affecting major platforms and the compromise of cloud backup systems, highlighting the expanding attack surface across enterprise environments.

## Active Exploitation Details

### Ivanti EPMM Vulnerabilities
- **Description**: Two critical vulnerabilities in Ivanti Endpoint Manager Mobile (EPMM) are being actively exploited by threat actors who have developed custom malware strains
- **Impact**: Attackers can deploy specialized malware within compromised organizational networks, enabling persistent access and data exfiltration
- **Status**: CISA has released detailed analysis of discovered malware strains following active exploitation in unnamed organizations
- **CVE ID**: CVE-2025-4427 and CVE-2025-4428

### Chrome V8 Zero-Day Vulnerability
- **Description**: High-severity vulnerability in Chrome's V8 JavaScript engine that allows remote code execution
- **Impact**: Attackers can execute arbitrary code on victim systems running vulnerable Chrome browsers, potentially compromising millions of users
- **Status**: Google has released emergency security updates; this represents the sixth Chrome zero-day exploited in attacks this year
- **CVE ID**: CVE-2025-10585

### WatchGuard Firebox Critical Vulnerability
- **Description**: Remote code execution vulnerability affecting WatchGuard Firebox firewalls
- **Impact**: Attackers can potentially gain administrative access to network security infrastructure
- **Status**: WatchGuard has released security updates to address the vulnerability

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Enterprise mobile device management systems vulnerable to custom malware deployment
- **Google Chrome**: Web browsers running vulnerable versions of V8 JavaScript engine affecting millions of users
- **WatchGuard Firebox Firewalls**: Network security appliances vulnerable to remote code execution
- **SonicWall MySonicWall Service**: Cloud backup service compromising firewall configuration files for under 5% of customer base
- **PyPI Package Repository**: Python package index targeted in GhostAction supply chain attack with token theft
- **Salesforce Platform**: Claims of 1.5 billion records stolen from 760 companies via compromised Drift OAuth tokens
- **Transport for London Systems**: Public transportation infrastructure targeted in August 2024 cyberattack

## Attack Vectors and Techniques

- **AI-Generated Malicious Scripts**: TA558 threat actor using artificially generated scripts to deploy Venom RAT targeting Brazilian hotels
- **Supply Chain Compromise**: GhostAction attack targeting PyPI tokens and malicious packages like SilentSync RAT delivered via fake Python packages
- **OAuth Token Abuse**: Exploitation of compromised Salesloft Drift OAuth tokens to access Salesforce data
- **Multi-Stage Malware Deployment**: CountLoader malware serving as delivery mechanism for Cobalt Strike and other post-exploitation tools
- **Proxy Botnet Operations**: SystemBC malware converting infected VPS systems into proxy infrastructure for malicious traffic routing
- **Collaborative APT Operations**: Russian groups Gamaredon and Turla working together to deploy Kazuar backdoor against Ukrainian targets
- **Phishing-as-a-Service**: RaccoonO365 PhaaS platform disrupted by Microsoft, targeting Microsoft 365 environments

## Threat Actor Activities

- **TA558**: Targeting hotels in Brazil and Spanish-speaking markets using AI-generated scripts to deploy Venom RAT and other remote access trojans
- **Russian APT Groups (Gamaredon & Turla)**: Collaborative operations deploying Kazuar backdoor specifically targeting Ukrainian entities
- **Scattered Spider**: Two teenagers arrested in UK connection with August 2024 Transport for London cyberattack, highlighting youth involvement in major cybercriminal operations
- **ShinyHunters**: Extortion group claiming theft of 1.5 billion Salesforce records through exploitation of compromised OAuth tokens
- **SystemBC Operators**: Maintaining average of 1,500 proxy bots daily by targeting vulnerable commercial VPS systems
- **CountLoader Operators**: Russian ransomware gangs using new malware loader for post-exploitation tool delivery including Cobalt Strike