# Exploitation Report

Critical exploitation activity is currently focused on FortiClient Enterprise Management Server vulnerabilities and zero-day flaws in open-source Git services. Threat actors are actively exploiting an authentication bypass vulnerability in FortiClient EMS to deploy credential-stealing malware, while a newly discovered zero-day vulnerability in Gogs Git service allows authenticated users to achieve remote code execution. These attacks represent immediate threats to enterprise infrastructure and development environments. Additionally, sophisticated malware campaigns are targeting cryptocurrency organizations and leveraging AI tools to enhance attack effectiveness, while ransomware groups are evolving their tactics to include physical infiltration of target facilities.

## Active Exploitation Details

### FortiClient EMS Authentication Bypass
- **Description**: Authentication bypass vulnerability in FortiClient Enterprise Management Server that allows attackers to circumvent security controls
- **Impact**: Successful exploitation enables deployment of credential-stealing malware, specifically an undocumented infostealer called EKZ
- **Status**: Vulnerability is now patched, but active exploitation campaigns continue against unpatched systems
- **CVE ID**: CVE-2026-35616

### Gogs Remote Code Execution Zero-Day
- **Description**: Unpatched zero-day vulnerability in the Gogs self-hosted Git service that affects Internet-facing instances
- **Impact**: Allows any authenticated user to execute arbitrary code on the target system under certain conditions
- **Status**: Currently unpatched zero-day with active exploitation potential

## Affected Systems and Products

- **FortiClient Enterprise Management Server**: All unpatched versions vulnerable to authentication bypass attacks
- **Gogs Git Service**: Self-hosted instances exposed to the internet are at risk from the zero-day vulnerability
- **Android Devices**: Targeted by BTMOB remote access trojan through malware-as-a-service operations
- **Windows Systems**: Affected by Grandoreiro banking trojan campaigns targeting Latin America and Europe
- **macOS Systems**: Targeted by JINX-0164 threat actor using fake recruiter lures against cryptocurrency firms
- **High-Performance GPU Systems**: Targeted by cryptojacking campaigns using SEO poisoning and AI chatbot manipulation

## Attack Vectors and Techniques

- **Authentication Bypass**: Exploitation of FortiClient EMS flaws to deploy credential stealers
- **Zero-Day Exploitation**: Direct exploitation of unpatched Gogs vulnerabilities for code execution
- **Social Engineering**: Fake recruiter lures targeting cryptocurrency organizations with macOS malware
- **SEO Poisoning**: Coordinated campaigns manipulating search results and AI chatbot recommendations to spread GPU mining malware
- **Physical Infiltration**: Ransomware groups conducting in-person attacks against law firm facilities
- **AI-Enhanced Attacks**: Threat actors using ChatGPT and Gemini to generate attack lures and improve malware effectiveness
- **Supply Chain Attacks**: Malicious npm packages targeting Claude AI user directories

## Threat Actor Activities

- **GreyVibe**: Russian threat cluster targeting Ukrainian entities using AI-generated lures and custom malware tools powered by ChatGPT and Gemini
- **Silent Ransom Group**: Ransomware actors physically infiltrating law firm facilities to steal data directly from servers and databases
- **JINX-0164**: Previously undocumented threat actor conducting recruitment-themed social engineering campaigns against cryptocurrency organizations
- **ShinyHunters**: Extortion gang responsible for the Carnival Corporation data breach affecting nearly 6 million people
- **BTMOB Operators**: Cybercriminals offering Android RAT services through a malware-as-a-service model with no-code development interfaces
- **Latin American Cybercriminals**: Groups targeting government agencies across Latin America to monetize citizen data, including a leak of 5.8 million Uruguayan citizen records