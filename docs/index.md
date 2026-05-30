# Exploitation Report

Recent security intelligence reveals significant exploitation activity across multiple attack vectors, with threat actors leveraging both known vulnerabilities and novel techniques. Critical exploitation activity centers around FortiClient EMS authentication bypass vulnerabilities being actively exploited to deliver credential-stealing malware, alongside the discovery of a severe remote code execution flaw in the Gogs Git service. Additionally, threat actors are increasingly utilizing AI platforms like ChatGPT for sophisticated phishing campaigns and post-exploitation activities, while the Marimo framework has been targeted through newly identified vulnerabilities. The landscape also shows continued supply chain attacks through malicious NuGet and npm packages, and the emergence of AI-powered threat groups conducting sustained campaigns against critical infrastructure.

## Active Exploitation Details

### FortiClient EMS Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in FortiClient Enterprise Management Server allowing unauthorized access
- **Impact**: Attackers can deploy credential-stealing malware and gain unauthorized access to enterprise management systems
- **Status**: Actively exploited in the wild with documented campaigns deploying EKZ credential stealer
- **CVE ID**: CVE-2026-35616

### Gogs Remote Code Execution
- **Description**: Critical vulnerability in Gogs open-source self-hosted Git service allowing authenticated users to execute arbitrary code
- **Impact**: Any authenticated user can achieve full system compromise and execute arbitrary commands
- **Status**: Recently disclosed vulnerability with high severity rating

### Marimo Framework Vulnerability
- **Description**: Publicly accessible vulnerability in the Marimo framework being exploited for initial access
- **Impact**: Enables threat actors to gain initial foothold for subsequent AI-powered post-exploitation activities
- **Status**: Actively exploited by unknown threat actors using LLM agents for post-compromise operations
- **CVE ID**: CVE-2026-39987

### ChatGPT Content Sharing Abuse (ChatGPhish)
- **Description**: Vulnerability leveraging ChatGPT's implicit trust in Markdown links and web summary features for phishing
- **Impact**: Enables sophisticated phishing campaigns using trusted AI platforms as attack vectors
- **Status**: Active exploitation through fake outage pages and malicious content hosting

## Affected Systems and Products

- **FortiClient Enterprise Management Server**: All versions prior to security update addressing CVE-2026-35616
- **Gogs Git Service**: Open-source self-hosted Git installations allowing authenticated user access
- **Marimo Framework**: Publicly accessible instances vulnerable to exploitation
- **ChatGPT Platform**: Content sharing and web summary features being abused for phishing
- **NuGet Package Repository**: Malicious packages targeting Brazilian banking credentials
- **npm Package Repository**: Supply chain attacks targeting cloud secrets and credentials
- **Android Devices**: BTMOB malware targeting mobile platforms with custom payloads

## Attack Vectors and Techniques

- **Authentication Bypass**: Exploitation of FortiClient EMS to circumvent security controls
- **Supply Chain Poisoning**: Malicious packages in NuGet and npm repositories masquerading as legitimate SDKs
- **AI-Powered Phishing**: Leveraging ChatGPT and Google Gemini for content generation and social engineering
- **Mobile Malware Distribution**: Custom Android trojan builders creating targeted phishing payloads
- **Post-Exploitation Automation**: LLM agents conducting automated post-compromise activities
- **Markdown Link Manipulation**: Abuse of trusted AI platforms for hosting malicious content

## Threat Actor Activities

- **GREYVIBE Group**: Russian-linked threat actor conducting AI-powered cyberattacks against Ukrainian entities since August 2025, utilizing ChatGPT and Google Gemini for attack automation
- **Kimsuky (Velvet Chollima)**: North Korean state-sponsored group deploying HTTPSpy malware and expanding arsenal with HelloDoor tools and VS Code tunnels targeting South Korean military and corporate entities
- **ShinyHunters**: Extortion gang responsible for Charter Communications breach affecting 4.9 million accounts
- **Unknown LLM-Using Actors**: Threat actors leveraging large language models for post-exploitation activities following Marimo framework compromises
- **Supply Chain Attackers**: Multiple groups targeting NuGet and npm repositories with banking credential theft and cloud secret extraction capabilities