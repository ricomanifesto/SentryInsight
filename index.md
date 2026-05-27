# Exploitation Report

Critical exploitation activity is currently centered around multiple zero-day vulnerabilities and ongoing malware campaigns targeting diverse systems. Most concerning are the active zero-day exploits against KnowledgeDeliver learning management systems and LiteSpeed cPanel plugins, which are being used to install web shells and compromise server infrastructure. Simultaneously, sophisticated supply chain attacks are targeting developers through npm packages and GitHub repositories, while banking trojans continue to plague Windows and Android users across Latin America and Europe. These activities represent a significant escalation in both the sophistication and scope of current cyber threats.

## Active Exploitation Details

### KnowledgeDeliver Zero-Day Vulnerability
- **Description**: A critical zero-day vulnerability in the KnowledgeDeliver learning management system (LMS) that allows remote code execution
- **Impact**: Attackers can deploy the Godzilla web shell to maintain persistent access and execute arbitrary commands on compromised servers
- **Status**: Actively exploited in the wild as a zero-day; patch status unknown

### LiteSpeed cPanel Plugin Critical Vulnerability
- **Description**: A critical vulnerability in the LiteSpeed cPanel user-end plugin that enables unauthorized access
- **Impact**: Allows attackers to compromise web hosting control panels and potentially gain administrative access to hosted websites
- **Status**: Actively exploited; CISA has mandated federal agencies patch within 4 days

### Gitea Container Registry Authentication Bypass
- **Description**: A security flaw in Gitea's self-hosted version control platform that bypasses authentication for container registries
- **Impact**: Unauthenticated remote attackers can pull private container images, potentially exposing sensitive source code and credentials
- **Status**: Recently disclosed vulnerability affecting organizations using Gitea for container management

## Affected Systems and Products

- **KnowledgeDeliver LMS**: Learning management systems running vulnerable versions
- **LiteSpeed cPanel Plugin**: Web hosting environments using the affected plugin
- **Gitea Platform**: Self-hosted Git services with container registry functionality
- **Windows Systems**: Targets of Grandoreiro banking trojan and Megalodon malware campaigns
- **Android Devices**: Infected with BTMOB RAT through targeted campaigns
- **GitHub Repositories**: Over 5,500 repositories compromised in Megalodon supply chain attack
- **npm Registry**: Developers using mouse5212-super package and other malicious packages
- **Claude AI Users**: Directory theft via malicious npm packages
- **SharePoint Servers**: Microsoft issued out-of-band patches for critical vulnerabilities

## Attack Vectors and Techniques

- **Web Shell Deployment**: Godzilla web shell installation through KnowledgeDeliver zero-day exploitation
- **Supply Chain Poisoning**: Malicious npm packages targeting Claude AI user directories and developer environments
- **Repository Compromise**: Mass GitHub repository infection with credential-stealing malware
- **DLL Side-Loading**: MuddyWater espionage group using legitimate executables to load malicious libraries
- **AI Chatbot Manipulation**: Cryptojacking campaigns leveraging AI chatbot recommendations to redirect users to malicious sites
- **In-Person Data Theft**: Silent Ransom Group conducting physical breaches of law firm offices
- **Blockchain C2 Infrastructure**: GlassWorm botnet utilizing Solana blockchain for resilient command and control

## Threat Actor Activities

- **MuddyWater (Iranian APT)**: Conducting espionage campaigns across nine countries using DLL side-loading techniques targeting government and critical infrastructure
- **Silent Ransom Group (SRG)**: Escalating to in-person data theft attacks against U.S. law firms, representing a significant tactical evolution
- **ShinyHunters**: Extorting Charter Communications after successful data breach, continuing their pattern of high-profile corporate targeting
- **TeamPCP**: Orchestrating the Shai-Hulud worm campaigns affecting open-source ecosystems through repository poisoning
- **Latin American Cybercriminals**: Systematically targeting government agencies to monetize citizen data, with recent focus on Uruguayan government systems
- **Grandoreiro Operators**: Deploying banking trojans across Latin America and Europe targeting both Windows and Android platforms
- **GlassWorm Campaign**: Sophisticated supply chain attacks targeting developers before recent infrastructure takedown by security researchers