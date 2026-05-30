# Exploitation Report

The current threat landscape reveals several critical active exploitation campaigns, with threat actors leveraging both newly discovered vulnerabilities and sophisticated attack techniques. Most concerning is the active exploitation of FortiClient EMS authentication bypass vulnerability CVE-2026-35616, which attackers are using to deploy credential-stealing malware. Additionally, the Marimo vulnerability CVE-2026-39987 has been exploited in novel attacks where threat actors use large language model agents for post-compromise activities. Meanwhile, state-sponsored groups like the Russian-linked GreyVibe are conducting AI-powered cyberattacks against Ukrainian entities, and various malware-as-a-service operations are targeting banking credentials and cloud infrastructure through package repository attacks.

## Active Exploitation Details

### FortiClient EMS Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in FortiClient Enterprise Management Server (EMS) allowing unauthorized access
- **Impact**: Attackers can deploy credential-stealing malware, specifically an undocumented infostealer called EKZ
- **Status**: Currently being actively exploited; patch available
- **CVE ID**: CVE-2026-35616

### Marimo Post-Exploitation with LLM Agents
- **Description**: Vulnerability in publicly-accessible Marimo instances being exploited for initial access
- **Impact**: Unknown threat actors are using large language model agents to conduct sophisticated post-compromise activities
- **Status**: Active exploitation observed with novel post-exploitation techniques
- **CVE ID**: CVE-2026-39987

### Gogs Remote Code Execution
- **Description**: Critical vulnerability in Gogs self-hosted Git service allowing authenticated users to execute arbitrary code
- **Impact**: Any authenticated user can achieve remote code execution under certain conditions
- **Status**: Recently disclosed, potential for active exploitation

### ChatGPT Content Sharing Abuse
- **Description**: Abuse of ChatGPT's content-sharing feature to host fake OpenAI outage pages
- **Impact**: Users directed to download malware disguised as ChatGPT desktop application
- **Status**: Ongoing campaign using legitimate platform features for malicious purposes

### ChatGPhish Vulnerability in ChatGPT
- **Description**: Vulnerability leveraging ChatGPT's implicit trust in Markdown links and images
- **Impact**: Transforms ChatGPT web summaries into phishing surfaces for credential theft
- **Status**: Disclosed vulnerability with demonstrated exploitation potential

## Affected Systems and Products

- **FortiClient Enterprise Management Server (EMS)**: Authentication bypass vulnerability affecting enterprise deployments
- **Marimo**: Open-source data science platform with publicly accessible instances
- **Gogs**: Self-hosted Git service installations vulnerable to authenticated RCE
- **ChatGPT**: Content sharing and web summary features being abused for malicious purposes
- **NuGet Package Repository**: Malicious packages targeting Brazilian banking system (Sicoob)
- **npm Package Repository**: Malicious packages targeting cloud secrets and credentials
- **Android Platforms**: BTMOB malware targeting mobile devices with custom phishing payloads

## Attack Vectors and Techniques

- **Authentication Bypass**: Exploiting FortiClient EMS to gain unauthorized access and deploy malware
- **LLM Agent Post-Exploitation**: Novel use of AI agents for conducting post-compromise activities
- **Package Repository Poisoning**: Malicious NuGet and npm packages masquerading as legitimate SDKs
- **Social Engineering via AI Platforms**: Abusing trusted AI platforms to host fake pages and deliver malware
- **Mobile Malware-as-a-Service**: BTMOB builder interface for generating custom Android payloads
- **AI-Generated Phishing**: Use of ChatGPT and Gemini for creating sophisticated lure content
- **FIFA World Cup Impersonation**: Fake websites targeting 2026 World Cup anticipation for fraud

## Threat Actor Activities

- **GreyVibe (Russian-linked)**: Conducting AI-powered cyberattacks against Ukrainian entities since August 2025, using ChatGPT and Gemini for lure generation
- **Kimsuky (North Korean)**: Deploying HTTPSpy malware and expanding arsenal with HelloDoor and VS Code Tunnels against South Korean military and corporate targets
- **ShinyHunters**: Extortion gang responsible for Charter Communications breach affecting 4.9 million accounts
- **Unknown LLM-Using Actor**: Leveraging large language models for post-exploitation after Marimo CVE-2026-39987 exploit
- **The Com Criminal Gang**: Neo-Nazi-infested group using cyber winnings to support violent crimes and sexploitation
- **Dutch Botnet Operators**: 17 million device botnet disrupted by Dutch authorities with 200+ servers seized
- **BTMOB Operators**: Android malware service providers offering custom phishing payload generation