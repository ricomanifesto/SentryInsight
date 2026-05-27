# Exploitation Report

The cybersecurity landscape is experiencing significant exploitation activity across multiple fronts, with critical vulnerabilities being actively targeted by threat actors. CISA has issued urgent patching directives for a critical cPanel plugin vulnerability that is under active exploitation, giving federal agencies only four days to secure their systems. Meanwhile, multiple zero-day vulnerabilities have been discovered and exploited, including a critical flaw in the KnowledgeDeliver learning management system that was used to install web shells. The threat landscape is further complicated by sophisticated malware campaigns like GlassWorm targeting software supply chains, and the emergence of AI-assisted cryptojacking operations that leverage chatbot interactions to redirect users to malicious sites.

## Active Exploitation Details

### LiteSpeed cPanel User-End Plugin Vulnerability
- **Description**: A critical vulnerability in the LiteSpeed cPanel user-end plugin that is being actively exploited in the wild
- **Impact**: Allows attackers to compromise servers running the vulnerable plugin
- **Status**: CISA has mandated federal agencies patch within 4 days due to active exploitation

### KnowledgeDeliver Learning Management System Zero-Day
- **Description**: A critical zero-day vulnerability in the KnowledgeDeliver learning management system that was exploited before patches were available
- **Impact**: Attackers successfully deployed Godzilla web shells on compromised servers
- **Status**: Previously unknown vulnerability that has been exploited to install web shells

### SharePoint Remote Code Execution Vulnerability
- **Description**: A remote code execution vulnerability in SharePoint that can be exploited without specialized conditions
- **Impact**: Allows attackers to execute arbitrary code on SharePoint servers
- **Status**: Microsoft has released patches across multiple SharePoint server versions
- **CVE ID**: CVE-2026-45659

### Gitea Private Container Image Exposure
- **Description**: A security flaw in Gitea that allows unauthenticated remote attackers to access private container images
- **Impact**: Unauthorized access to private container repositories without authentication
- **Status**: Disclosed vulnerability affecting self-hosted Git repositories

## Affected Systems and Products

- **LiteSpeed cPanel Plugin**: User-end plugin component with critical security flaw under active exploitation
- **KnowledgeDeliver LMS**: Learning management system servers vulnerable to web shell installation
- **Microsoft SharePoint**: Multiple server versions affected by remote code execution vulnerability
- **Gitea Platforms**: Self-hosted Git repository systems exposing private container images
- **GitHub Repositories**: Over 5,500 repositories infected by Megalodon malware in coordinated supply chain attack
- **Developer Environments**: Software development infrastructure targeted by GlassWorm botnet operations

## Attack Vectors and Techniques

- **Web Shell Deployment**: Exploitation of KnowledgeDeliver zero-day to install Godzilla web shells for persistent access
- **Supply Chain Compromise**: Megalodon malware campaign infected thousands of GitHub repositories in coordinated attack
- **Blockchain C2 Infrastructure**: GlassWorm botnet utilized Solana blockchain for resilient command and control operations
- **AI Chatbot Manipulation**: Cryptojacking campaigns using AI chatbot interactions to redirect users to malicious download sites
- **DLL Side-Loading**: Advanced technique employed by MuddyWater group in espionage operations across multiple countries
- **Unauthenticated Access**: Direct exploitation of Gitea vulnerability to access private container images without credentials
- **In-Person Data Theft**: Silent Ransom Group conducting physical attacks on law firm premises to steal sensitive data

## Threat Actor Activities

- **Silent Ransom Group (SRG)**: Conducting in-person data theft attacks specifically targeting U.S.-based law firms with physical breach tactics
- **MuddyWater APT**: Iranian state-sponsored group conducting espionage campaign using DLL side-loading techniques across nine countries and four continents
- **ShinyHunters**: Extortion group responsible for Charter Communications data breach with ransom demands
- **TeamPCP**: Cybercrime group behind Shai-Hulud worm campaigns causing significant damage to open source ecosystem
- **GlassWorm Operators**: Sophisticated actors targeting software developers in supply chain attacks using blockchain-based infrastructure
- **Megalodon Campaign**: Coordinated malware distribution affecting thousands of GitHub repositories to steal developer credentials and secrets
- **Cryptojacking Groups**: Leveraging AI chatbot technologies to distribute cryptocurrency mining malware through social engineering