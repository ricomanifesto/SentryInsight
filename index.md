# Exploitation Report

Current threat landscape shows significant exploitation activity across multiple platforms and services. Attackers are leveraging critical vulnerabilities in enterprise infrastructure software, particularly targeting FortiClient EMS with CVE-2026-35616 for credential theft operations. A new zero-day vulnerability CVE-2026-39987 in Marimo has been exploited by unknown threat actors who are innovatively using large language model agents for post-compromise activities. State-sponsored groups including GREYVIBE and Kimsuky are conducting sophisticated campaigns against Ukrainian and South Korean entities respectively, while cybercriminals are abusing legitimate AI platforms like ChatGPT for malware distribution and phishing operations. Enterprise software including Gogs Git service faces critical remote code execution vulnerabilities, and malware-as-a-service operations like BTMOB are providing customizable Android trojans to threat actors.

## Active Exploitation Details

### FortiClient EMS Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in FortiClient Enterprise Management Server allowing unauthorized access
- **Impact**: Attackers can deliver credential-stealing malware including the undocumented EKZ stealer
- **Status**: Currently being exploited in the wild, patch available
- **CVE ID**: CVE-2026-35616

### Marimo Zero-Day Vulnerability
- **Description**: Zero-day vulnerability in publicly-accessible Marimo instances being exploited for initial access
- **Impact**: Enables threat actors to gain system access and deploy LLM agents for post-exploitation activities
- **Status**: Actively exploited by unknown threat actor, patch status unclear
- **CVE ID**: CVE-2026-39987

### Gogs Git Service Remote Code Execution
- **Description**: Critical vulnerability in Gogs open-source self-hosted Git service allowing authenticated users to execute arbitrary code
- **Impact**: Any authenticated user can achieve remote code execution under certain conditions
- **Status**: Vulnerability disclosed, exploitation status being monitored

### ChatGPT Content Sharing Abuse
- **Description**: Threat actors abusing ChatGPT's content-sharing feature to host fake OpenAI outage pages
- **Impact**: Users directed to download malware disguised as ChatGPT desktop application
- **Status**: Ongoing abuse of legitimate platform features

### ChatGPhish Vulnerability
- **Description**: Vulnerability in ChatGPT web summaries leveraging AI assistant's trust in Markdown links and images
- **Impact**: Transforms ChatGPT into a phishing surface for malicious campaigns
- **Status**: Active vulnerability enabling phishing operations

## Affected Systems and Products

- **FortiClient Enterprise Management Server**: Authentication bypass vulnerability affecting enterprise deployments
- **Marimo Instances**: Publicly-accessible instances vulnerable to zero-day exploitation
- **Gogs Git Service**: Open-source self-hosted Git service with critical RCE vulnerability
- **OpenAI ChatGPT**: Content-sharing and web summary features being abused for malware distribution
- **Android Devices**: Targeted by BTMOB malware service with custom phishing payloads
- **NuGet Package Repository**: Malicious packages targeting Sicoob banking system users
- **npm Package Repository**: Malicious packages designed to steal cloud secrets and credentials

## Attack Vectors and Techniques

- **Authentication Bypass**: Exploiting CVE-2026-35616 to bypass FortiClient EMS authentication controls
- **LLM Agent Post-Exploitation**: Using large language models to conduct automated post-compromise activities
- **AI Platform Abuse**: Leveraging ChatGPT and Google Gemini for generating phishing lures and hosting malicious content
- **Supply Chain Attacks**: Distributing malicious NuGet and npm packages to target developers and banking users
- **Social Engineering**: Creating fake OpenAI outage pages and FIFA websites to steal credentials
- **Malware-as-a-Service**: BTMOB platform providing customizable Android trojans with builder interface
- **Remote Code Execution**: Exploiting Gogs vulnerability to achieve code execution on Git servers

## Threat Actor Activities

- **GREYVIBE**: Russian-linked threat actor conducting persistent attacks against Ukraine using AI-powered tools including ChatGPT and Google Gemini for generating attack materials
- **Kimsuky (Velvet Chollima)**: North Korean state-sponsored group targeting South Korean military and corporate entities with HTTPSpy malware, HelloDoor, and VS Code tunnels
- **ShinyHunters**: Extortion gang responsible for breaching Charter Communications and stealing data from 4.9 million accounts
- **Unknown LLM-Using Threat Actor**: Sophisticated group exploiting Marimo CVE-2026-39987 and deploying LLM agents for post-exploitation automation
- **EKZ Malware Operators**: Cybercriminals exploiting FortiClient EMS vulnerability to deploy undocumented credential stealer
- **BTMOB Service Operators**: Malware-as-a-service providers offering Android RAT with custom payload generation capabilities