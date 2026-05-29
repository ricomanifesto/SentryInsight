# Exploitation Report

Critical exploitation activity continues to escalate with multiple vulnerabilities being actively exploited in the wild. The most significant threats include an authentication bypass vulnerability in FortiClient Enterprise Management Server being exploited to deploy credential-stealing malware, and an unpatched zero-day vulnerability in the Gogs self-hosted Git service allowing remote code execution. Additionally, sophisticated threat actors are leveraging AI-powered tools and custom malware arsenals to target financial institutions, cryptocurrency firms, and government networks across multiple regions.

## Active Exploitation Details

### FortiClient EMS Authentication Bypass Vulnerability
- **Description**: Authentication bypass vulnerability in FortiClient Enterprise Management Server that allows unauthorized access to enterprise systems
- **Impact**: Threat actors can deploy credential-stealing malware and gain unauthorized access to enterprise networks
- **Status**: Patched, but actively being exploited in ongoing campaigns
- **CVE ID**: CVE-2026-35616

### Gogs Remote Code Execution Zero-Day
- **Description**: Unpatched zero-day vulnerability in Gogs self-hosted Git service that allows authenticated users to execute arbitrary code
- **Impact**: Attackers can achieve remote code execution on Internet-facing Gogs instances under certain conditions
- **Status**: Zero-day vulnerability with no patch available, actively exploitable

## Affected Systems and Products

- **FortiClient Enterprise Management Server (EMS)**: All versions affected by the authentication bypass vulnerability
- **Gogs Self-Hosted Git Service**: Internet-facing instances vulnerable to zero-day RCE exploit
- **Charter Communications**: 4.9 million customer accounts compromised in data breach
- **Carnival Corporation**: Nearly 6 million people affected by confirmed data breach
- **Android Devices**: Targeted by BTMOB remote access trojan through phishing campaigns
- **macOS Systems**: Cryptocurrency firms targeted with fake recruiter lures and custom malware
- **Ukrainian Organizations**: Military and corporate entities targeted by Kimsuky threat actor
- **Brazilian Financial Systems**: Sicoob cooperative banking customers targeted through malicious NuGet packages

## Attack Vectors and Techniques

- **Social Engineering**: Fake recruitment campaigns targeting cryptocurrency firms with macOS malware
- **Phishing**: Custom Android malware payloads delivered through BTMOB builder interface
- **Supply Chain Attacks**: Malicious NuGet packages masquerading as legitimate banking SDKs
- **SEO Poisoning**: GPU mining malware spread through manipulated search results and AI chatbot recommendations
- **AI-Generated Content**: GreyVibe threat cluster using ChatGPT and Gemini to create convincing lures
- **Package Repository Abuse**: npm packages targeting cloud secrets and credentials
- **Authentication Bypass**: Direct exploitation of FortiClient EMS vulnerabilities to deploy malware
- **Zero-Day Exploitation**: Remote code execution attacks against unpatched Gogs instances

## Threat Actor Activities

- **Kimsuky (Velvet Chollima)**: North Korean state-sponsored group deploying HTTPSpy malware, HelloDoor backdoor, and abusing VS Code tunnels to target South Korean military and corporate entities
- **ShinyHunters Extortion Gang**: Responsible for major data breaches affecting Charter Communications (4.9M accounts) and Carnival Corporation (6M people)
- **GreyVibe**: Likely Russian threat cluster using AI-generated lures and custom malware tools to target Ukrainian entities
- **JINX-0164**: Previously undocumented threat actor targeting cryptocurrency organizations with recruitment-themed social engineering and digital asset theft
- **Silent Ransom Group**: Ransomware actors physically infiltrating law firm premises to steal data and social-engineer access to servers and databases
- **EKZ Operators**: Deploying undocumented credential stealer malware through FortiClient EMS exploitation
- **BTMOB Operators**: Running Android malware-as-a-service targeting Brazilian and Latin American users with custom phishing payloads