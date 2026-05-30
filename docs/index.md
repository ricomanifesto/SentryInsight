# Exploitation Report

Current threat activity reveals several critical exploitation campaigns targeting enterprise infrastructure and AI systems. Attackers are actively exploiting vulnerabilities in FortiClient Enterprise Management Server to deploy credential stealing malware, while a new vulnerability in the Marimo platform is being leveraged for post-exploitation activities using AI agents. Additionally, threat actors are abusing legitimate AI services like ChatGPT for phishing operations and malware distribution. The emergence of state-sponsored groups like GREYVIBE using AI-powered attack techniques represents a significant evolution in cyber warfare tactics, particularly targeting Ukrainian entities with sophisticated AI-generated lures and custom malware arsenals.

## Active Exploitation Details

### FortiClient EMS Authentication Bypass Vulnerability
- **Description**: Authentication bypass vulnerability in FortiClient Enterprise Management Server allowing unauthorized access to enterprise systems
- **Impact**: Attackers can deploy credential stealing malware, specifically the undocumented EKZ infostealer, compromising enterprise credentials and sensitive data
- **Status**: Actively exploited in the wild with ongoing campaign activity
- **CVE ID**: CVE-2026-35616

### Marimo Platform Remote Code Execution
- **Description**: Vulnerability in publicly-accessible Marimo platform installations allowing initial access and exploitation
- **Impact**: Enables threat actors to gain initial system access and conduct post-compromise activities using large language model agents for automated exploitation
- **Status**: Actively exploited with confirmed post-exploitation LLM agent usage
- **CVE ID**: CVE-2026-39987

### Gogs Git Service Remote Code Execution
- **Description**: Critical security vulnerability in Gogs open-source self-hosted Git service allowing authenticated users to execute arbitrary code
- **Impact**: Any authenticated user can execute arbitrary code on the system under certain conditions, leading to complete system compromise
- **Status**: Critical vulnerability disclosed, patch status unknown

### ChatGPT Content Sharing Abuse
- **Description**: Abuse of ChatGPT's content-sharing feature and web summary functionality to host malicious content and phishing pages
- **Impact**: Users directed to download malware disguised as legitimate ChatGPT desktop applications through fake outage pages and markdown link manipulation
- **Status**: Ongoing abuse of legitimate AI service features for malware distribution

## Affected Systems and Products

- **FortiClient Enterprise Management Server**: Enterprise endpoint management deployments vulnerable to authentication bypass attacks
- **Marimo Platform**: Publicly-accessible installations used for data science and analytics workflows
- **Gogs Git Service**: Open-source self-hosted Git service installations across various environments
- **ChatGPT Platform**: AI assistant service being abused through content-sharing and web summary features
- **Android Devices**: Targeted by BTMOB malware service with custom phishing payloads
- **NuGet Package Ecosystem**: C# development environments targeted by malicious Sicoob SDK packages
- **npm Package Registry**: Cloud environments with exposed secrets targeted through malicious packages

## Attack Vectors and Techniques

- **Authentication Bypass**: Exploitation of FortiClient EMS vulnerability to bypass security controls and deploy malware
- **AI-Powered Social Engineering**: Use of ChatGPT and Google Gemini to generate convincing phishing lures and attack content
- **Supply Chain Poisoning**: Injection of malicious packages into NuGet and npm repositories to target developers and cloud infrastructure
- **Legitimate Service Abuse**: Manipulation of ChatGPT sharing features and markdown rendering to host malicious content
- **Post-Exploitation Automation**: Deployment of LLM agents for automated post-compromise activities and lateral movement
- **Custom Malware Generation**: BTMOB service providing tailored Android malware payloads for specific phishing campaigns

## Threat Actor Activities

- **GREYVIBE (Russia-linked)**: Conducting persistent attacks against Ukraine and Ukraine-related entities since August 2025, utilizing AI-generated lures and sophisticated custom malware including HTTPSpy backdoors
- **Kimsuky (North Korean APT)**: Expanding arsenal with HTTPSpy, HelloDoor, and VS Code tunnels to target South Korean military and corporate entities
- **ShinyHunters Extortion Gang**: Successfully breached Charter Communications, compromising 4.9 million customer accounts in April attack
- **Unknown Threat Actors**: Actively exploiting FortiClient EMS vulnerability (CVE-2026-35616) to deploy EKZ credential stealer across enterprise environments
- **The Com Criminal Gang**: Neo-Nazi-affiliated cybercriminal organization using cyber attack proceeds to support violent crimes and exploitation activities
- **BTMOB Operators**: Providing Android malware-as-a-service with custom payload generation capabilities for targeted phishing operations