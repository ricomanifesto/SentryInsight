# Exploitation Report

Critical exploitation activity continues to escalate with threat actors leveraging multiple attack vectors to compromise enterprise systems and mobile devices. The most significant developments include active exploitation of FortiClient EMS authentication bypass vulnerabilities (CVE-2026-35616) for credential theft, a zero-day remote code execution flaw in Gogs Git service affecting internet-facing instances, and sophisticated malware-as-a-service operations targeting Android and Windows platforms. Additionally, threat actors are increasingly incorporating AI-powered tools to enhance attack capabilities and reduce exploit development timelines.

## Active Exploitation Details

### FortiClient EMS Authentication Bypass
- **Description**: Authentication bypass vulnerability in FortiClient Enterprise Management Server allowing unauthorized access
- **Impact**: Attackers can deploy credential-stealing malware, specifically the undocumented EKZ stealer
- **Status**: Currently being exploited in active campaigns, patch available
- **CVE ID**: CVE-2026-35616

### Gogs Remote Code Execution Zero-Day
- **Description**: Unpatched zero-day vulnerability in Gogs self-hosted Git service enabling remote code execution
- **Impact**: Any authenticated user can execute arbitrary code under certain conditions on internet-facing instances
- **Status**: Active zero-day exploitation, no patch currently available

### BTMOB Android Remote Access Trojan
- **Description**: Android malware offered as a service with custom payload generation capabilities
- **Impact**: Complete device compromise, data theft, and remote control of infected Android devices
- **Status**: Actively distributed through malware-as-a-service model across Latin America

### Grandoreiro Banking Trojan
- **Description**: Banking trojan campaign targeting Windows systems in Latin America and Europe
- **Impact**: Financial data theft and unauthorized banking transactions
- **Status**: Active campaigns ongoing with sophisticated distribution methods

## Affected Systems and Products

- **FortiClient Enterprise Management Server**: Authentication bypass vulnerability affecting enterprise deployments
- **Gogs Git Service**: Self-hosted Git service instances exposed to the internet
- **Android Devices**: Targeted by BTMOB RAT through phishing and social engineering
- **Windows Systems**: Compromised by Grandoreiro banking trojan in Latin American and European campaigns
- **Cryptocurrency Organizations**: Targeted by JINX-0164 threat actor using macOS malware
- **High-Performance Computing Systems**: Infected with GPU mining malware through SEO poisoning
- **npm Registry**: Malicious packages targeting Claude AI user directories

## Attack Vectors and Techniques

- **Authentication Bypass**: Exploitation of FortiClient EMS flaws to gain unauthorized system access
- **Zero-Day Exploitation**: Direct exploitation of unpatched Gogs vulnerability for remote code execution
- **SEO Poisoning**: Manipulation of search engine results and AI chatbot recommendations to distribute cryptojacking malware
- **Social Engineering**: Fake recruiter lures targeting cryptocurrency firms with macOS malware
- **Malware-as-a-Service**: BTMOB RAT distributed through licensing model with no-code development interface
- **Supply Chain Attacks**: Malicious npm packages designed to steal files from Claude AI user directories
- **AI-Enhanced Attacks**: Use of ChatGPT and Gemini to generate convincing phishing lures and malware

## Threat Actor Activities

- **GreyVibe**: Russian threat cluster targeting Ukrainian entities using AI-generated lures and custom malware tools
- **JINX-0164**: Previously undocumented threat actor targeting cryptocurrency organizations with fake recruitment campaigns and macOS malware
- **Silent Ransom Group**: Ransomware operators conducting physical intrusions at law firm locations to steal data directly
- **ShinyHunters**: Extortion gang claiming responsibility for Carnival Corporation data breach affecting nearly 6 million people
- **Latin American Cybercriminals**: Groups targeting government agencies to monetize citizen data, including 5.8 million Uruguayan citizen records
- **BTMOB Operators**: Cybercriminals offering Android RAT through malware-as-a-service model across Brazil and Latin America