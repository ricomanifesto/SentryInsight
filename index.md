# Exploitation Report

Critical zero-day vulnerabilities and active exploitation campaigns are currently targeting enterprise systems and development environments. Attackers are leveraging sophisticated techniques including AI-assisted exploit development, supply chain attacks, and in-person data theft operations. The most concerning activities include the exploitation of a zero-day vulnerability in KnowledgeDeliver learning management systems for web shell deployment, active attacks against LiteSpeed cPanel plugins, and large-scale supply chain compromises affecting thousands of GitHub repositories. Threat actors are increasingly using AI chatbots and SEO poisoning to distribute malware, while ransomware groups have evolved to conduct physical infiltration attacks against law firms.

## Active Exploitation Details

### KnowledgeDeliver Zero-Day Vulnerability
- **Description**: Critical zero-day vulnerability in KnowledgeDeliver learning management system (LMS) allowing unauthorized access
- **Impact**: Attackers can deploy Godzilla web shells on compromised servers, providing persistent backdoor access
- **Status**: Actively exploited in the wild as zero-day; patch status unknown

### LiteSpeed cPanel Plugin Vulnerability
- **Description**: Critical vulnerability in LiteSpeed cPanel user-end plugin affecting web hosting control panels
- **Impact**: Enables unauthorized access and potential server compromise
- **Status**: Actively exploited; CISA issued emergency directive requiring federal agencies to patch within 4 days

### Gitea Container Registry Vulnerability
- **Description**: Authentication bypass vulnerability in Gitea's self-hosted version control platform
- **Impact**: Allows unauthenticated remote attackers to pull private container images without authorization
- **Status**: Vulnerability disclosed; exploitation status in wild unclear

## Affected Systems and Products

- **KnowledgeDeliver LMS**: Learning management system servers running vulnerable versions
- **LiteSpeed cPanel Plugin**: Web hosting servers using the affected plugin component
- **Gitea Platforms**: Self-hosted version control instances with container registry functionality
- **GitHub Repositories**: Over 5,500 repositories infected with Megalodon malware in coordinated supply chain attack
- **npm Registry**: JavaScript package ecosystem targeted with malicious packages stealing Claude AI user data
- **Windows and Android Systems**: Targeted by Grandoreiro and BTMOB banking trojans in Latin America and Europe
- **macOS Systems**: Cryptocurrency firms targeted by JINX-0164 malware through fake recruiter campaigns
- **High-Performance Computing Systems**: GPU mining systems targeted through SEO poisoning and AI chatbot manipulation

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in enterprise systems
- **AI-Assisted Exploit Development**: Attackers using artificial intelligence to dramatically reduce exploit development timelines
- **Supply Chain Attacks**: Mass compromise of software repositories and package managers
- **SEO Poisoning**: Manipulation of search engine results to redirect users to malicious sites
- **AI Chatbot Manipulation**: Exploiting AI chatbot recommendations to surface cryptojacking malware
- **Social Engineering**: Fake recruitment campaigns targeting cryptocurrency organizations
- **Physical Infiltration**: In-person attacks by ransomware groups targeting law firm data
- **Blockchain-Based C2**: Resilient command and control infrastructure using Solana blockchain technology

## Threat Actor Activities

- **Silent Ransom Group (SRG)**: Conducting physical infiltration attacks against U.S. law firms, combining social engineering with in-person data theft operations
- **JINX-0164**: Previously undocumented threat actor targeting cryptocurrency firms with macOS malware distributed through fake recruitment campaigns
- **ShinyHunters**: Extortion group conducting data breach operations against telecommunications companies like Charter Communications
- **TeamPCP**: Cybercrime group behind Shai-Hulud worm campaigns causing significant damage to open source ecosystems
- **GlassWorm Operators**: Sophisticated supply chain attackers using blockchain-based infrastructure before recent takedown by CrowdStrike, Google, and Shadowserver Foundation
- **Latin American Banking Trojans**: Multiple groups deploying Grandoreiro and BTMOB malware across Europe and Latin America
- **Megalodon Campaign**: Coordinated attack compromising over 5,500 GitHub repositories in just six hours to steal developer credentials and secrets