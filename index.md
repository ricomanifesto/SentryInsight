# Exploitation Report

Current threat activity shows active exploitation of critical vulnerabilities across enterprise infrastructure and consumer applications. Attackers are leveraging authentication bypass flaws in FortiClient EMS (CVE-2026-35616) to deploy credential-stealing malware, while a zero-day remote code execution vulnerability in Gogs Git service poses immediate risk to self-hosted repositories. Additionally, threat actors are exploiting a Marimo vulnerability (CVE-2026-39987) and utilizing AI services for both offensive operations and as attack surfaces. Nation-state groups, particularly Russian-linked GREYVIBE, are incorporating AI tools into their attack campaigns, while cybercriminals are abusing legitimate platforms like ChatGPT for malware distribution and phishing operations.

## Active Exploitation Details

### FortiClient EMS Authentication Bypass Vulnerability
- **Description**: Critical authentication bypass flaw in FortiClient Enterprise Management Server allowing unauthorized access to enterprise endpoint management systems
- **Impact**: Attackers can deploy credential-stealing malware (EKZ infostealer) and gain unauthorized access to enterprise endpoints
- **Status**: Actively exploited in the wild with ongoing campaigns observed
- **CVE ID**: CVE-2026-35616

### Gogs Remote Code Execution Zero-Day
- **Description**: Unpatched zero-day vulnerability in the Gogs self-hosted Git service that allows authenticated users to execute arbitrary code under certain conditions
- **Impact**: Complete compromise of Git repositories and underlying server infrastructure with remote code execution capabilities
- **Status**: Zero-day vulnerability with no current patch available, actively being disclosed

### Marimo Post-Exploitation Vulnerability
- **Description**: Vulnerability in Marimo platform being exploited to gain initial access for subsequent LLM-powered post-compromise activities
- **Impact**: Initial access vector leading to AI-enhanced post-exploitation activities and lateral movement
- **Status**: Actively exploited with threat actors using LLM agents for post-compromise operations
- **CVE ID**: CVE-2026-39987

### ChatGPT Content-Sharing Abuse
- **Description**: Exploitation of ChatGPT's content-sharing feature to host fake outage pages and phishing content
- **Impact**: Malware distribution disguised as legitimate ChatGPT desktop applications and credential theft through fake service pages
- **Status**: Ongoing abuse of legitimate platform features for malicious purposes

## Affected Systems and Products

- **FortiClient Enterprise Management Server**: Enterprise endpoint management systems vulnerable to authentication bypass
- **Gogs Git Service**: Self-hosted Git repositories exposed to remote code execution
- **Marimo Platform**: Initial access vector for AI-enhanced attacks
- **ChatGPT Platform**: Legitimate service being abused for malware hosting and phishing
- **Android Devices**: Targeted by BTMOB remote access trojan with custom phishing payloads
- **NuGet Package Ecosystem**: Malicious Sicoob packages targeting Brazilian banking credentials
- **npm Package Registry**: Packages designed to steal cloud secrets and credentials

## Attack Vectors and Techniques

- **Authentication Bypass**: Exploitation of FortiClient EMS to bypass security controls and deploy malware
- **Zero-Day Exploitation**: Unpatched Gogs vulnerability providing immediate RCE capabilities
- **Platform Abuse**: Leveraging legitimate ChatGPT sharing features for malicious content hosting
- **AI-Powered Post-Exploitation**: Using LLM agents to conduct sophisticated post-compromise activities
- **Supply Chain Attacks**: Malicious packages in software repositories targeting developers and organizations
- **Phishing-as-a-Service**: BTMOB malware builder providing customized Android trojans for phishing campaigns

## Threat Actor Activities

- **GREYVIBE (Russian-linked)**: Targeting Ukrainian entities with AI-generated lures and custom malware tools since August 2025, incorporating ChatGPT and Gemini into attack workflows
- **Kimsuky (North Korean)**: Deploying HTTPSpy malware and expanding arsenal with HelloDoor and VS Code tunnels against South Korean military and corporate entities
- **Unknown Threat Actor**: Exploiting Marimo vulnerability and using LLM agents for post-exploitation activities
- **Cybercriminal Groups**: Operating BTMOB Android malware-as-a-service with builder interface for custom payload generation
- **ShinyHunters**: Extortion gang responsible for Charter Communications breach affecting 4.9 million accounts