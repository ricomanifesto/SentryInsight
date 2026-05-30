# Exploitation Report

Critical security vulnerabilities are under active exploitation across multiple platforms, with threat actors leveraging both technical vulnerabilities and social engineering techniques. The most concerning activities include authentication bypass vulnerabilities in enterprise security solutions, AI-powered attack campaigns, and sophisticated malware distribution through legitimate platforms. Notable threats include exploitation of FortiClient EMS authentication flaws, PAN-OS GlobalProtect bypasses, and innovative attacks leveraging AI tools for enhanced targeting and post-exploitation activities.

## Active Exploitation Details

### PAN-OS GlobalProtect Authentication Bypass
- **Description**: A medium-severity authentication bypass vulnerability affecting Palo Alto Networks PAN-OS and Prisma Access systems
- **Impact**: Allows attackers to bypass authentication mechanisms and gain unauthorized access to protected networks
- **Status**: Currently under active exploitation in the wild
- **CVE ID**: CVE-2026-0257

### FortiClient EMS Authentication Bypass
- **Description**: Authentication bypass vulnerability in FortiClient Enterprise Management Server allowing unauthorized access
- **Impact**: Enables attackers to deliver credential-stealing malware and compromise enterprise environments
- **Status**: Actively exploited to distribute EKZ infostealer malware
- **CVE ID**: CVE-2026-35616

### Marimo Code Execution Vulnerability
- **Description**: Vulnerability in publicly-accessible Marimo systems allowing initial access
- **Impact**: Provides attackers with initial foothold for advanced post-exploitation activities using AI agents
- **Status**: Exploited by unknown threat actors for sophisticated post-compromise operations
- **CVE ID**: CVE-2026-39987

### Gogs Remote Code Execution
- **Description**: Critical vulnerability in Gogs self-hosted Git service allowing authenticated users to execute arbitrary code
- **Impact**: Complete system compromise for any authenticated user under specific conditions
- **Status**: Recently disclosed critical vulnerability requiring immediate attention

### ChatGPhish Vulnerability
- **Description**: Vulnerability in OpenAI ChatGPT web summaries leveraging implicit trust in Markdown links and images
- **Impact**: Enables phishing attacks through ChatGPT's content-sharing features and web summary functionality
- **Status**: Actively abused by threat actors to host fake outage pages and deliver malware

## Affected Systems and Products

- **Palo Alto Networks PAN-OS**: GlobalProtect components affected by authentication bypass
- **Fortinet FortiClient EMS**: Enterprise Management Server vulnerable to authentication bypass
- **Marimo**: Publicly-accessible instances targeted for initial access
- **Gogs**: Self-hosted Git service installations with critical RCE vulnerability
- **OpenAI ChatGPT**: Content-sharing and web summary features exploited for phishing
- **Android Systems**: BTMOB malware targeting mobile devices with custom payloads
- **Cloud Infrastructure**: Over 2,000 AI-coded applications exposed in production environments
- **Charter Communications**: 4.9 million customer accounts compromised by ShinyHunters
- **23andMe**: Genetic and personal information exposed in 2023 breach under legal scrutiny

## Attack Vectors and Techniques

- **AI-Powered Campaigns**: GREYVIBE threat actors using ChatGPT and Gemini for enhanced attack operations
- **LLM Agent Post-Exploitation**: Advanced post-compromise activities using large language model agents for automated reconnaissance
- **Malicious Package Distribution**: Sicoob NuGet packages targeting banking credentials and npm packages stealing cloud secrets
- **Fake Application Distribution**: ChatGPT share links hosting fraudulent OpenAI outage pages to deliver malware
- **Mobile Malware-as-a-Service**: BTMOB Android RAT with builder interface for custom phishing payloads
- **Supply Chain Attacks**: Malicious packages in software repositories targeting developers and cloud environments
- **Social Engineering**: FIFA World Cup fraud schemes using fake websites to steal credentials and financial data

## Threat Actor Activities

- **GREYVIBE**: Russia-linked threat actor targeting Ukraine with AI-powered cyberattacks since August 2025, leveraging ChatGPT and Gemini for enhanced operations
- **Kimsuky**: North Korean state-sponsored group deploying HTTPSpy malware and expanding arsenal with HelloDoor and VS Code tunnels targeting South Korean entities
- **ShinyHunters**: Extortion gang responsible for Charter Communications breach affecting 4.9 million accounts
- **The Com**: Neo-Nazi-affiliated criminal gang using cyber proceeds to fund violent activities and exploitation operations
- **Unknown Threat Actors**: Sophisticated groups exploiting Marimo vulnerabilities and using AI agents for post-exploitation activities
- **Mobile Malware Operators**: Cybercriminals offering BTMOB Android RAT as a service with custom payload generation capabilities