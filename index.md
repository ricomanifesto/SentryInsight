# Exploitation Report

Critical exploitation activity is currently targeting multiple enterprise infrastructure components, with attackers leveraging both newly disclosed vulnerabilities and novel attack techniques. The most significant threats include active exploitation of Palo Alto Networks' GlobalProtect authentication bypass vulnerability and FortiClient EMS authentication flaws, alongside sophisticated campaigns using AI-powered tools by nation-state actors. Threat actors are also exploiting vulnerabilities in popular development platforms like Marimo and Gogs, while simultaneously abusing legitimate services such as ChatGPT for malware distribution and phishing campaigns.

## Active Exploitation Details

### PAN-OS GlobalProtect Authentication Bypass
- **Description**: A medium-severity authentication bypass vulnerability affecting PAN-OS and Prisma Access systems
- **Impact**: Attackers can bypass authentication mechanisms in GlobalProtect implementations
- **Status**: Under active exploitation in the wild
- **CVE ID**: CVE-2026-0257

### FortiClient EMS Authentication Bypass
- **Description**: An authentication bypass vulnerability in FortiClient Enterprise Management Server
- **Impact**: Allows hackers to deliver credential stealer malware, specifically the undocumented EKZ infostealer
- **Status**: Actively exploited to distribute malware
- **CVE ID**: CVE-2026-35616

### Marimo Post-Exploitation Vulnerability
- **Description**: A vulnerability in publicly-accessible Marimo instances that enables initial access
- **Impact**: Threat actors use this as an entry point for deploying LLM agents for post-compromise activities
- **Status**: Exploited for post-exploitation activities using AI agents
- **CVE ID**: CVE-2026-39987

### Gogs Remote Code Execution
- **Description**: A critical vulnerability in the popular open-source self-hosted Git service Gogs
- **Impact**: Any authenticated user can execute arbitrary code under certain conditions
- **Status**: Recently disclosed critical vulnerability
- **CVE ID**: Not explicitly mentioned in available article content

### ChatGPhish Vulnerability
- **Description**: A vulnerability in OpenAI ChatGPT that exploits the AI assistant's implicit trust in Markdown links and images
- **Impact**: Turns ChatGPT web summaries into a phishing surface for malicious activities
- **Status**: Disclosed vulnerability being used for phishing campaigns

## Affected Systems and Products

- **Palo Alto Networks PAN-OS**: GlobalProtect components and Prisma Access implementations
- **Fortinet FortiClient EMS**: Enterprise Management Server installations
- **Marimo**: Publicly-accessible instances of the platform
- **Gogs**: Self-hosted Git service installations
- **OpenAI ChatGPT**: Web summary and content-sharing features
- **Android Devices**: Targeted by BTMOB malware service with custom phishing payloads
- **NuGet Package Ecosystem**: Malicious packages targeting Brazilian banking credentials
- **npm Package Ecosystem**: Packages designed to steal cloud secrets

## Attack Vectors and Techniques

- **Authentication Bypass**: Exploiting authentication flaws in enterprise management systems
- **AI-Powered Phishing**: Using ChatGPT and Google Gemini to generate sophisticated lures and content
- **LLM Agent Post-Exploitation**: Deploying large language model agents for post-compromise activities
- **Supply Chain Attacks**: Injecting malicious packages into software repositories
- **Social Engineering**: Fake service outage pages and FIFA World Cup fraud schemes
- **Markdown Exploitation**: Abusing trusted markdown rendering in AI platforms
- **Custom Malware Builders**: BTMOB service providing tailored Android malware generation

## Threat Actor Activities

- **GreyVibe (Russia-linked)**: Targeting Ukrainian entities with AI-generated lures using ChatGPT and Gemini, active since August 2025
- **Kimsuky (North Korean APT)**: Deploying HTTPSpy malware and expanding arsenal with HelloDoor and VS Code tunnels against South Korean military and corporate entities
- **The Com Criminal Gang**: Neo-Nazi-affiliated group conducting cyberattacks to support violence and exploitation activities
- **ShinyHunters**: Extortion gang responsible for Charter Communications breach affecting 4.9 million accounts
- **Unknown Threat Actors**: Exploiting Marimo vulnerabilities and using LLM agents for post-exploitation activities
- **Brazilian Financial Threat Actors**: Targeting Sicoob banking system through malicious NuGet packages