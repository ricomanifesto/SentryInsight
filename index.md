# Exploitation Report

Critical exploitation activity is currently dominated by zero-day attacks and supply chain compromises targeting high-value systems. The most significant incidents include a zero-day vulnerability in KnowledgeDeliver learning management systems being exploited to deploy Godzilla web shells, and CISA's emergency directive requiring federal agencies to patch an actively exploited cPanel plugin flaw within four days. Additionally, sophisticated supply chain attacks are proliferating, with the GlassWorm botnet targeting developers through blockchain-based infrastructure and the Megalodon malware campaign compromising over 5,500 GitHub repositories in just six hours. Threat actors are also employing novel attack vectors, including AI chatbot manipulation for cryptojacking campaigns and in-person data theft operations by the Silent Ransom Group.

## Active Exploitation Details

### KnowledgeDeliver Zero-Day Web Shell Deployment
- **Description**: Critical zero-day vulnerability in KnowledgeDeliver learning management system allowing remote code execution
- **Impact**: Attackers can deploy Godzilla web shells for persistent system access and data exfiltration
- **Status**: Actively exploited as zero-day vulnerability; patch status unknown

### LiteSpeed cPanel Plugin Critical Vulnerability
- **Description**: Critical vulnerability in LiteSpeed cPanel user-end plugin allowing unauthorized access
- **Impact**: Complete system compromise and unauthorized administrative access to web hosting infrastructure
- **Status**: CISA mandates federal agencies patch within 4 days due to active exploitation

### Gitea Container Image Exposure
- **Description**: Security flaw allowing unauthenticated remote attackers to access private container images
- **Impact**: Unauthorized access to sensitive container configurations, source code, and proprietary applications
- **Status**: Vulnerability disclosed; exploitation capability confirmed

## Affected Systems and Products

- **KnowledgeDeliver LMS**: Learning management systems running vulnerable server configurations
- **LiteSpeed cPanel Plugin**: Web hosting control panels with the vulnerable LiteSpeed plugin installed
- **Gitea Platforms**: Self-hosted version control platforms exposing private container repositories
- **GitHub Repositories**: Over 5,500 repositories compromised by Megalodon malware campaign
- **Windows and Android Devices**: Targeted by Grandoreiro and BTMOB banking trojans
- **macOS Systems**: Targeted by JINX-0164 threat actor using recruitment-themed social engineering
- **npm Registry**: Malicious packages targeting Claude AI user directories
- **High-Performance Computing Systems**: Targeted by GPU mining malware campaigns

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in web applications and management systems
- **Supply Chain Poisoning**: Malicious commits to GitHub repositories and compromised npm packages
- **SEO Poisoning**: Manipulated search results redirecting to cryptojacking malware sites
- **AI Chatbot Manipulation**: Exploitation of AI recommendation systems to distribute malicious downloads
- **Social Engineering**: Recruitment-themed lures targeting cryptocurrency organizations
- **In-Person Data Theft**: Physical infiltration by extortion groups to access law firm servers
- **Blockchain-Based C2**: Resilient command and control infrastructure using Solana blockchain technology

## Threat Actor Activities

- **Silent Ransom Group**: Conducting in-person data theft attacks against U.S. law firms with social engineering tactics to access servers and databases
- **JINX-0164**: Previously undocumented threat actor targeting cryptocurrency firms with macOS malware using fake recruiter lures
- **ShinyHunters**: Extortion gang responsible for data breaches affecting Carnival Corporation (6 million records) and Charter Communications
- **GlassWorm Operators**: Sophisticated botnet targeting developers through supply chain attacks with blockchain-based infrastructure
- **Megalodon Campaign**: Massive GitHub repository compromise affecting 5,500+ repositories in six-hour timeframe
- **Latin American Cybercriminals**: Targeting government agencies for citizen data monetization, including 5.8 million Uruguayan citizen records
- **Grandoreiro and BTMOB Operators**: Banking trojan campaigns targeting Latin America and Europe across Windows and Android platforms