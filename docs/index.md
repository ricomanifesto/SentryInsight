# Exploitation Report

Current threat landscapes reveal critical active exploitation across multiple high-impact vulnerabilities. The most significant ongoing exploitation involves a zero-day vulnerability in Gogs Git service enabling remote code execution for authenticated users, and the active exploitation of CVE-2026-35616 in FortiClient Enterprise Management Server being leveraged to deploy credential-stealing malware. Advanced threat actors including North Korean Kimsuky group and Russian-affiliated GreyVibe cluster are deploying sophisticated new tools and AI-powered attack campaigns targeting military, corporate, and cryptocurrency organizations across multiple regions.

## Active Exploitation Details

### FortiClient EMS Authentication Bypass Vulnerability
- **Description**: Critical authentication bypass vulnerability in FortiClient Enterprise Management Server allowing unauthorized access to enterprise management functions
- **Impact**: Attackers can bypass authentication mechanisms and deploy credential-stealing malware, specifically an undocumented infostealer called EKZ
- **Status**: Actively exploited in the wild, patch available
- **CVE ID**: CVE-2026-35616

### Gogs Git Service Zero-Day Vulnerability
- **Description**: Critical zero-day remote code execution vulnerability in Gogs self-hosted Git service affecting authenticated users under certain conditions
- **Impact**: Any authenticated user can execute arbitrary code on vulnerable Gogs instances, leading to complete system compromise
- **Status**: Unpatched zero-day actively being exploited on Internet-facing instances

## Affected Systems and Products

- **FortiClient Enterprise Management Server**: All vulnerable versions affected by authentication bypass allowing credential theft
- **Gogs Git Service**: Self-hosted Git service instances exposed to Internet facing critical RCE risk
- **Android Devices**: Targeted by BTMOB RAT and Grandoreiro banking trojan campaigns across Latin America and Europe
- **Windows Systems**: Affected by Grandoreiro banking malware and GPU mining malware campaigns
- **macOS Platforms**: Targeted by JINX-0164 threat actor using fake recruiter lures against cryptocurrency firms
- **South Korean Military and Corporate Systems**: Targeted by Kimsuky group using HTTPSpy, HelloDoor, and VS Code tunnels

## Attack Vectors and Techniques

- **Authentication Bypass Exploitation**: FortiClient EMS vulnerability leveraged to deploy credential stealers without proper authentication
- **Zero-Day Remote Code Execution**: Gogs Git service compromise enabling arbitrary code execution for authenticated attackers
- **Social Engineering with AI-Generated Content**: GreyVibe actors using ChatGPT and Gemini to create convincing phishing lures and campaign materials
- **Fake Recruitment Campaigns**: JINX-0164 targeting cryptocurrency firms with macOS malware delivered through fraudulent job opportunities
- **SEO Poisoning and AI Chatbot Manipulation**: GPU mining malware distributed through coordinated search engine optimization attacks and manipulated AI recommendations
- **Physical Infiltration**: Silent Ransom Group conducting in-person social engineering attacks against law firms to access servers and databases
- **MaaS Distribution Models**: BTMOB RAT offered through malware-as-a-service with builder interfaces for custom payload generation

## Threat Actor Activities

- **Kimsuky (Velvet Chollima)**: North Korean state-sponsored group expanding arsenal with HTTPSpy backdoor, HelloDoor malware, and Visual Studio Code tunnels for persistence against South Korean targets
- **GreyVibe**: Russian-affiliated threat cluster leveraging AI tools including ChatGPT and Gemini to enhance cyberattack effectiveness against Ukrainian entities with custom malware toolkit
- **JINX-0164**: Previously undocumented threat actor conducting targeted campaigns against cryptocurrency organizations using recruitment-themed social engineering and macOS malware for digital asset theft
- **Silent Ransom Group**: Ransomware operation conducting physical infiltration attacks against law firms, combining traditional extortion with in-person social engineering tactics
- **ShinyHunters**: Extortion gang claiming responsibility for Carnival Corporation breach affecting nearly 6 million people
- **Latin American Cybercriminal Groups**: Multiple actors targeting government agencies across Latin America to monetize citizen data, including recent 5.8 million record exposure from Uruguay