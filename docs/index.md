# Exploitation Report

Several critical vulnerabilities are being actively exploited in the wild, with threat actors leveraging authentication bypass flaws, remote code execution vulnerabilities, and sophisticated AI-powered attack techniques. The most concerning activities include the exploitation of FortiClient EMS authentication bypass vulnerability (CVE-2026-35616) to deploy credential-stealing malware, a critical remote code execution vulnerability in Gogs Git service, and the exploitation of Marimo vulnerability (CVE-2026-39987) where attackers are using LLM agents for post-exploitation activities. Additionally, threat actors are abusing ChatGPT features to host malicious content and deploy sophisticated malware campaigns targeting various sectors.

## Active Exploitation Details

### FortiClient EMS Authentication Bypass
- **Description**: Authentication bypass vulnerability in FortiClient Enterprise Management Server allowing unauthorized access to systems
- **Impact**: Attackers can deploy credential-stealing malware, specifically the undocumented EKZ infostealer
- **Status**: Currently being exploited in active campaigns, patch available
- **CVE ID**: CVE-2026-35616

### Marimo Post-Exploitation with LLM Agents
- **Description**: Vulnerability in Marimo platform being exploited for initial access, with attackers using large language model agents for post-compromise activities
- **Impact**: Enables sophisticated post-exploitation automation and lateral movement through AI-powered techniques
- **Status**: Active exploitation observed with novel AI-enhanced attack techniques
- **CVE ID**: CVE-2026-39987

### Gogs Remote Code Execution
- **Description**: Critical vulnerability in Gogs self-hosted Git service that allows authenticated users to execute arbitrary code
- **Impact**: Complete system compromise for any authenticated user under certain conditions
- **Status**: Critical vulnerability disclosed, exploitation potential confirmed

### ChatGPhish Vulnerability
- **Description**: Vulnerability in OpenAI ChatGPT that leverages the AI assistant's implicit trust in Markdown links and images
- **Impact**: Enables phishing attacks through ChatGPT web summaries and content sharing features
- **Status**: Active abuse of ChatGPT share links to host fake outage pages and deliver malware

## Affected Systems and Products

- **FortiClient Enterprise Management Server**: Authentication bypass vulnerability enabling credential theft
- **Marimo Platform**: Post-exploitation targets with LLM-enhanced attack capabilities
- **Gogs Git Service**: Self-hosted Git platforms vulnerable to remote code execution
- **OpenAI ChatGPT**: Content sharing features being abused for malware distribution
- **Android Devices**: BTMOB malware-as-a-service targeting mobile platforms with custom phishing payloads
- **NuGet/npm Packages**: Malicious packages targeting Brazilian banking credentials and cloud secrets

## Attack Vectors and Techniques

- **Authentication Bypass**: Exploitation of FortiClient EMS flaws to bypass security controls
- **AI-Powered Social Engineering**: Use of ChatGPT and Gemini to generate convincing phishing lures and attack content
- **Malware-as-a-Service**: BTMOB Android trojan offering custom payload generation for phishing campaigns
- **Supply Chain Attacks**: Malicious NuGet packages masquerading as legitimate Brazilian banking SDKs
- **LLM Agent Exploitation**: Novel technique using AI agents for automated post-compromise activities
- **Content Platform Abuse**: Leveraging ChatGPT's trusted platform to host malicious content

## Threat Actor Activities

- **GreyVibe (Russian-linked)**: Targeting Ukrainian entities with AI-generated lures and custom malware tools, using ChatGPT and Gemini for attack enhancement
- **Kimsuky (North Korean)**: Deploying HTTPSpy malware and expanding arsenal with HelloDoor backdoor and VS Code tunnels against South Korean military and corporate targets
- **ShinyHunters**: Extortion gang responsible for Charter Communications breach affecting 4.9 million accounts
- **Unknown Threat Actor**: Conducting sophisticated post-exploitation using LLM agents after Marimo vulnerability exploitation
- **The Com Criminal Gang**: Neo-Nazi-affiliated group conducting cyberattacks to support violence and exploitation activities
- **Multiple Cybercriminals**: Exploiting FortiClient EMS vulnerabilities in ongoing credential theft campaigns