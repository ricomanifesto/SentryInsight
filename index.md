# Exploitation Report

Critical vulnerabilities are currently being actively exploited across multiple platforms, with CISA issuing urgent patching directives for federal agencies. The most significant threats include a zero-day vulnerability in the KnowledgeDeliver learning management system being exploited to install web shells, a critical LiteSpeed cPanel plugin flaw requiring immediate patching, an actively exploited Drupal SQL injection vulnerability, and a SharePoint remote code execution vulnerability addressed by Microsoft's out-of-band patch. Additionally, threat actors are leveraging AI chatbots for cryptojacking campaigns and conducting supply chain attacks through GitHub repository compromises.

## Active Exploitation Details

### KnowledgeDeliver Zero-Day Vulnerability
- **Description**: A critical zero-day vulnerability in the KnowledgeDeliver learning management system (LMS) that allows unauthorized access to servers
- **Impact**: Attackers can deploy web shells, including the Godzilla web shell, providing persistent remote access to compromised systems
- **Status**: Actively exploited in the wild as a zero-day attack

### LiteSpeed cPanel Plugin Vulnerability
- **Description**: A critical security flaw in the LiteSpeed cPanel user-end plugin that affects server security
- **Impact**: Allows attackers to compromise servers and potentially gain administrative access
- **Status**: Actively exploited - CISA has ordered federal agencies to patch within 4 days

### Drupal SQL Injection Vulnerability
- **Description**: An SQL injection vulnerability in the Drupal content management system that affects database security
- **Impact**: Enables attackers to execute unauthorized database queries and potentially extract sensitive information
- **Status**: Actively exploited - CISA has mandated federal agencies patch by Wednesday evening

### SharePoint Remote Code Execution Vulnerability
- **Description**: A remote code execution flaw in Microsoft SharePoint that can be exploited without specialized conditions
- **Impact**: Allows attackers to execute arbitrary code on affected SharePoint servers
- **Status**: Patched by Microsoft in an out-of-band update
- **CVE ID**: CVE-2026-45659

### Gitea Container Image Exposure
- **Description**: A security flaw in Gitea that allows unauthenticated remote attackers to access private container images
- **Impact**: Unauthorized access to private container images without authentication
- **Status**: Disclosed vulnerability requiring immediate attention

## Affected Systems and Products

- **KnowledgeDeliver Learning Management System**: Servers running this LMS platform vulnerable to zero-day exploitation
- **LiteSpeed cPanel Plugin**: Web hosting environments using the LiteSpeed cPanel user-end plugin
- **Drupal CMS**: Websites and applications built on the Drupal content management system
- **Microsoft SharePoint**: SharePoint servers across multiple versions affected by RCE vulnerability
- **Gitea**: Self-hosted Git service platforms running vulnerable versions
- **GitHub Repositories**: Over 5,500 repositories infected by the Megalodon malware campaign
- **AI Chatbot Platforms**: Various AI chatbot services being exploited for cryptojacking redirects

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in KnowledgeDeliver systems
- **Web Shell Deployment**: Installation of Godzilla and other web shells for persistent access
- **SQL Injection**: Database compromise through Drupal vulnerability exploitation
- **AI Chatbot Manipulation**: Using AI chatbot recommendations to redirect users to cryptojacking sites
- **Supply Chain Attacks**: Malicious commits pushed to GitHub repositories for credential theft
- **DLL Side-Loading**: Advanced technique used by MuddyWater group in espionage campaigns
- **Phishing and SEO Poisoning**: Iranian threat actors using these methods to deploy malware
- **In-Person Data Theft**: Physical attacks by Silent Ransom Group targeting law firms

## Threat Actor Activities

- **Silent Ransom Group (SRG)**: Conducting in-person data theft attacks targeting U.S. law firms with physical infiltration tactics
- **ShinyHunters**: Extortion group threatening Charter Communications with data leak unless ransom is paid
- **MuddyWater**: Iranian hacking group conducting espionage campaigns across 9 countries using DLL side-loading techniques
- **Nimbus Manticore**: Iranian state-sponsored actor deploying MiniFast and MiniJunk V2 malware via phishing
- **TeamPCP**: Cybercrime group behind the Shai-Hulud worm causing significant damage to open source ecosystem
- **GlassWorm Operators**: Persistent malware campaign disrupted by CrowdStrike, Google, and Shadowserver Foundation
- **Megalodon Campaign Actors**: Attackers who compromised over 5,500 GitHub repositories in just six hours
- **Ajax Football Club Hackers**: Cybercriminals who compromised the professional football club's systems