# Exploitation Report

The current threat landscape reveals several critical vulnerabilities under active exploitation, with threat actors leveraging both zero-day flaws and recently patched vulnerabilities to conduct sophisticated attacks. Most concerning is the ongoing exploitation of FortiClient EMS systems through an authentication bypass vulnerability, enabling widespread deployment of credential-stealing malware. Additionally, a critical zero-day vulnerability in the Gogs Git service allows authenticated users to execute arbitrary code, presenting immediate risks to organizations using this self-hosted platform. Cybercriminal operations are increasingly sophisticated, with threat actors like GreyVibe utilizing AI-generated lures and JINX-0164 targeting cryptocurrency firms through social engineering campaigns.

## Active Exploitation Details

### FortiClient EMS Authentication Bypass
- **Description**: A critical authentication bypass vulnerability in FortiClient Enterprise Management Server (EMS) that allows unauthorized access to management functions
- **Impact**: Attackers can deliver credential-stealing malware, specifically an undocumented stealer called EKZ, compromising enterprise security management infrastructure
- **Status**: Vulnerability is patched but continues to be actively exploited in ongoing campaigns
- **CVE ID**: CVE-2026-35616

### Gogs Remote Code Execution
- **Description**: An unpatched zero-day vulnerability in the Gogs self-hosted Git service that enables remote code execution
- **Impact**: Any authenticated user can execute arbitrary code under certain conditions, potentially leading to complete system compromise
- **Status**: Zero-day vulnerability with no patch currently available, actively being exploited
- **CVE ID**: Not provided in source articles

### GPU Mining Malware Campaign
- **Description**: Cryptojacking malware specifically targeting high-performance computing systems with powerful GPUs
- **Impact**: Unauthorized cryptocurrency mining operations that degrade system performance and increase operational costs
- **Status**: Active campaign spreading through SEO poisoning and AI chatbot manipulation

## Affected Systems and Products

- **FortiClient Enterprise Management Server (EMS)**: Authentication bypass vulnerability affecting enterprise deployments
- **Gogs Self-hosted Git Service**: Zero-day RCE vulnerability affecting Internet-facing instances
- **Windows Systems**: Targeted by Grandoreiro banking trojan campaigns across Latin America and Europe
- **Android Devices**: Affected by BTMOB RAT malware-as-a-service operations
- **macOS Systems**: Targeted by JINX-0164 threat actor using recruitment-themed social engineering
- **High-Performance Computing Systems**: GPU mining malware targeting systems with powerful graphics cards
- **npm Registry**: Malicious packages stealing files from Claude AI user directories

## Attack Vectors and Techniques

- **Authentication Bypass**: Exploitation of FortiClient EMS vulnerability to bypass security controls
- **Zero-day Exploitation**: Active exploitation of unpatched Gogs vulnerability for remote code execution
- **AI-Generated Social Engineering**: GreyVibe threat actors using ChatGPT and Gemini to create convincing phishing lures
- **Fake Recruitment Campaigns**: JINX-0164 targeting cryptocurrency firms with fraudulent job opportunities
- **SEO Poisoning**: Manipulation of search results to distribute cryptojacking malware
- **AI Chatbot Manipulation**: Corrupting AI chatbot recommendations to spread malicious content
- **Supply Chain Attacks**: Malicious npm packages targeting developer environments
- **Physical Social Engineering**: Silent Ransom Group conducting in-person attacks on law firms

## Threat Actor Activities

- **GreyVibe**: Russian threat cluster targeting Ukrainian entities with AI-generated lures and custom malware tools, leveraging ChatGPT and Gemini for campaign enhancement
- **JINX-0164**: Previously undocumented threat actor conducting sophisticated social engineering campaigns against cryptocurrency organizations using fake recruiter personas
- **Silent Ransom Group**: Ransomware operators physically infiltrating law firm premises to steal data and access servers
- **ShinyHunters**: Extortion gang responsible for Carnival Corporation data breach affecting nearly 6 million people
- **BTMOB Operators**: Cybercriminals offering malware-as-a-service with custom payload generation capabilities targeting Android users
- **Latin American Cybercriminals**: Groups targeting government data across Latin America, with recent focus on Uruguayan citizen records