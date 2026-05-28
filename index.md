# Exploitation Report

The current threat landscape is dominated by several critical vulnerabilities being actively exploited in the wild. Most notably, threat actors are leveraging an authentication bypass vulnerability in FortiClient Enterprise Management Server (CVE-2026-35616) to deploy the EKZ credential stealer malware. Additionally, a zero-day remote code execution vulnerability in Gogs self-hosted Git service remains unpatched and poses significant risks to organizations. CISA has issued urgent directives for federal agencies to address a critical vulnerability in the LiteSpeed cPanel plugin that is being actively exploited. Furthermore, a zero-day vulnerability in KnowledgeDeliver learning management system has been exploited to deploy Godzilla web shells, highlighting the expanding attack surface across enterprise applications.

## Active Exploitation Details

### FortiClient EMS Authentication Bypass Vulnerability
- **Description**: Authentication bypass vulnerability affecting FortiClient Enterprise Management Server deployments
- **Impact**: Allows threat actors to deploy credential-stealing malware, specifically the EKZ infostealer, compromising enterprise credentials and sensitive data
- **Status**: Patched by vendor, but exploitation campaigns continue against unpatched systems
- **CVE ID**: CVE-2026-35616

### Gogs Remote Code Execution Zero-Day
- **Description**: Critical remote code execution vulnerability in Gogs open-source self-hosted Git service allowing authenticated users to execute arbitrary code
- **Impact**: Complete system compromise, allowing attackers to execute arbitrary code on affected Git service instances
- **Status**: Zero-day vulnerability with no available patch, actively being exploited

### LiteSpeed cPanel Plugin Critical Vulnerability
- **Description**: Critical vulnerability in LiteSpeed cPanel user-end plugin
- **Impact**: Allows unauthorized access and potential system compromise on web hosting environments
- **Status**: CISA has mandated federal agencies patch within 4 days due to active exploitation

### KnowledgeDeliver Zero-Day Web Shell Deployment
- **Description**: Critical zero-day vulnerability in KnowledgeDeliver learning management system
- **Impact**: Enables deployment of Godzilla web shells providing persistent backdoor access to compromised systems
- **Status**: Zero-day vulnerability exploited in the wild to install web shells

## Affected Systems and Products

- **FortiClient Enterprise Management Server**: All unpatched deployments vulnerable to authentication bypass attacks
- **Gogs Git Service**: Internet-facing instances running the open-source self-hosted Git service
- **cPanel Hosting Environments**: Servers running LiteSpeed cPanel plugin components
- **KnowledgeDeliver LMS**: Learning management system deployments vulnerable to web shell installation
- **Gitea Platforms**: Container registry functionality exposing private container images without authentication
- **Windows and Android Devices**: Targeted by Grandoreiro and BTMOB banking trojan campaigns
- **macOS Systems**: Targeted by JINX-0164 threat group using fake recruiter lures
- **High-Performance GPU Systems**: Targeted by cryptojacking campaigns through SEO poisoning

## Attack Vectors and Techniques

- **Authentication Bypass Exploitation**: Leveraging CVE-2026-35616 to bypass FortiClient EMS authentication mechanisms
- **Zero-Day Remote Code Execution**: Exploiting unpatched Gogs vulnerability for system compromise
- **Web Shell Deployment**: Installing Godzilla web shells through KnowledgeDeliver vulnerabilities
- **SEO Poisoning**: Manipulating search engine results to redirect users to cryptojacking malware sites
- **AI Chatbot Manipulation**: Exploiting AI chatbot recommendations to surface malicious download sites
- **DLL Side-Loading**: Advanced technique used by MuddyWater group for stealth deployment
- **Social Engineering**: Fake recruiter lures targeting cryptocurrency organizations
- **Supply Chain Attacks**: Malicious npm packages stealing files from Claude AI user directories
- **In-Person Data Theft**: Physical attacks by Silent Ransom Group targeting law firms

## Threat Actor Activities

- **EKZ Campaign Operators**: Actively exploiting FortiClient EMS vulnerabilities to deploy credential-stealing malware across enterprise environments
- **JINX-0164**: Previously undocumented threat actor targeting cryptocurrency organizations with macOS malware using recruitment-themed social engineering
- **MuddyWater**: Iranian hacking group conducting espionage campaigns across nine countries using DLL side-loading techniques
- **Silent Ransom Group**: Extortion gang conducting in-person data theft attacks specifically targeting U.S. law firms
- **GlassWorm Operators**: Targeting developers in supply-chain attacks using Solana blockchain-based command and control infrastructure
- **Grandoreiro Campaign**: Banking trojan operators targeting Windows systems across Latin America and Europe
- **BTMOB RAT Campaign**: Android-focused banking malware targeting users in coordinated campaigns
- **Cryptojacking Groups**: Leveraging SEO poisoning and AI chatbot manipulation to distribute GPU mining malware