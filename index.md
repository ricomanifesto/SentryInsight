# Exploitation Report

Current threat activity reveals a surge in sophisticated attacks targeting cloud infrastructures, WordPress platforms, and enterprise services. Critical vulnerabilities are being actively exploited across multiple sectors, with threat actors leveraging authentication bypasses, token theft, and social engineering techniques. Notably, the Service Finder WordPress theme vulnerability is under active exploitation, allowing unauthorized administrative access. Russian-backed groups are weaponizing AI for enhanced phishing campaigns, while major ransomware cartels are forming strategic alliances to amplify their impact. The emergence of novel attack techniques like cache smuggling and the weaponization of legitimate tools demonstrates the evolving threat landscape.

## Active Exploitation Details

### Service Finder WordPress Theme Authentication Bypass
- **Description**: Critical security flaw in the Service Finder WordPress theme that allows complete authentication bypass
- **Impact**: Threat actors can gain unauthorized access to any account, including administrator accounts, enabling complete site takeover
- **Status**: Actively exploited in the wild, patch available

### WordPress Site Injection Campaign
- **Description**: Malicious JavaScript injections targeting WordPress sites to redirect users to malicious destinations
- **Impact**: Site visitors are redirected to sketchy sites as part of ClickFix phishing attacks, compromising user credentials and data
- **Status**: Ongoing campaign affecting multiple WordPress installations

### Figma MCP Server Remote Code Execution
- **Description**: Severe vulnerability in the figma-developer-mcp Model Context Protocol server that enables remote code execution
- **Impact**: Attackers can achieve code execution on target systems through agentic AI compromise vectors
- **Status**: Patched, but organizations must update immediately
- **CVE ID**: CVE-2025-53967

### Nezha Tool Weaponization
- **Description**: Legitimate open-source monitoring tool Nezha being weaponized by Chinese threat actors
- **Impact**: Delivers Gh0st RAT malware to targets, providing persistent remote access and control
- **Status**: Active campaign leveraging legitimate tool for malicious purposes

## Affected Systems and Products

- **Service Finder WordPress Theme**: All versions prior to the recent security update
- **WordPress Sites**: Vulnerable to JavaScript injection campaigns affecting site integrity and visitor security
- **Figma MCP Servers**: Organizations using figma-developer-mcp Model Context Protocol servers
- **AWS Cloud Instances**: Targeted by Crimson Collective for data theft and extortion
- **Discord Zendesk Systems**: Alleged breach affecting 5.5 million users with government ID exposure
- **Microsoft 365 Services**: Azure Front Door CDN outages affecting Teams and Exchange Online
- **Asahi Brewery Systems**: Ransomware attack causing operational disruptions and beer shortages
- **Salesforce Customer Environments**: Widespread data theft attacks affecting multiple customers

## Attack Vectors and Techniques

- **Authentication Bypass**: Direct exploitation of WordPress theme vulnerabilities for administrative access
- **Cache Smuggling**: FileFix attack variant using cache smuggling to secretly download malicious ZIP archives
- **Token Theft**: OAuth and API token compromise leading to SaaS environment breaches
- **Voice Phishing**: ShinyHunters using vishing attacks to compromise Salesforce customer data
- **JavaScript Injection**: Malicious code insertion into WordPress sites for traffic redirection
- **Social Engineering**: Fake job postings targeting influencers with Tesla and Red Bull impersonation
- **AI-Enhanced Phishing**: Russian actors using artificial intelligence to improve phishing campaign effectiveness
- **Legitimate Tool Abuse**: Weaponizing open-source Nezha monitoring tool for malware delivery

## Threat Actor Activities

- **Crimson Collective**: Targeting AWS cloud environments for data theft and extortion, recently breached Red Hat Consulting GitLab instance
- **TwoNet**: Pro-Russian hacktivist group pivoting from DDoS attacks to critical infrastructure targeting
- **ShinyHunters**: Conducting broad corporate extortion spree after stealing over billion records from Salesforce customers
- **BatShadow**: Vietnamese cybercrime group deploying Vampire Bot malware targeting job hunters
- **Chinese APT Groups**: Weaponizing Nezha tool and leveraging ChatGPT for malware development
- **Russian State Actors**: Implementing AI-enhanced cyber operations against Ukraine with improved phishing techniques
- **LockBit, Qilin, DragonForce Alliance**: Three major ransomware groups forming strategic cartel to share resources and attack information
- **Scattered Lapsus$ Collaborators**: Partnering with Crimson Collective for expanded attack capabilities