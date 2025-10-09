# Exploitation Report

Critical exploitation activities are currently targeting WordPress themes, SaaS platforms, and cloud infrastructure. The most severe threats include active exploitation of the Service Finder WordPress theme authentication bypass vulnerability, widespread token-based attacks against SaaS platforms, and sophisticated ransomware operations by coordinated threat groups. Chinese-nexus actors are weaponizing legitimate tools like Nezha for remote access, while Russian hackers are leveraging AI for enhanced phishing and malware campaigns. Ransomware groups including LockBit, Qilin, and DragonForce have formed strategic alliances to dominate the threat landscape.

## Active Exploitation Details

### Service Finder WordPress Theme Authentication Bypass
- **Description**: Critical vulnerability in the Service Finder WordPress theme allowing complete authentication bypass
- **Impact**: Attackers can gain unauthorized access to any account, including administrator accounts, enabling complete site compromise
- **Status**: Actively being exploited in the wild by threat actors

### Figma MCP Server Remote Code Execution
- **Description**: Severe vulnerability in the figma-developer-mcp Model Context Protocol server enabling code execution
- **Impact**: Remote code execution capabilities that can compromise organizational agentic AI systems
- **Status**: Now patched, but organizations using this third-party integration remain at risk if unpatched
- **CVE ID**: CVE-2025-53967

### WordPress Theme Injection Attacks
- **Description**: Malicious JavaScript injections targeting WordPress sites to redirect users to malicious destinations
- **Impact**: Site visitors are redirected to sketchy sites as part of next-generation ClickFix phishing campaigns
- **Status**: Active campaign targeting WordPress installations

### Token-Based SaaS Platform Attacks
- **Description**: OAuth and API token theft targeting SaaS environments
- **Impact**: Complete compromise of SaaS platforms and access to sensitive organizational data
- **Status**: Leading cause of SaaS breaches with ongoing exploitation across multiple platforms

## Affected Systems and Products

- **WordPress**: Service Finder theme and various other themes vulnerable to injection attacks
- **Figma MCP Server**: Third-party Model Context Protocol integration vulnerable to RCE
- **Microsoft 365**: Services including Teams and Exchange Online affected by recent outages
- **Discord**: Zendesk support system compromised affecting 5.5 million users
- **AWS Cloud Instances**: Targeted by Crimson Collective for data theft operations
- **Salesforce**: Customer data affected by widespread data theft attacks
- **Asahi Brewery**: Production systems impacted by Qilin ransomware attack

## Attack Vectors and Techniques

- **Authentication Bypass**: Critical vulnerabilities in WordPress themes allowing direct admin access
- **Cache Smuggling**: FileFix attack variant using cache smuggling to bypass security software
- **Token Theft**: OAuth and API token compromise for SaaS platform access
- **Voice Phishing (Vishing)**: ShinyHunters using voice calls to extract credentials and data
- **AI-Enhanced Phishing**: Russian actors leveraging artificial intelligence for improved social engineering
- **Weaponized Legitimate Tools**: Chinese actors using Nezha open-source monitoring tool for malicious purposes
- **Infrastructure Targeting**: Pro-Russian groups pivoting to critical infrastructure attacks

## Threat Actor Activities

- **Crimson Collective**: Targeting AWS cloud environments for data theft and has partnered with Scattered Spider/Lapsus$ hunters
- **TwoNet**: Pro-Russian hacktivist group evolved from DDoS attacks to critical infrastructure targeting
- **ShinyHunters**: Operating broad corporate extortion campaigns after stealing over a billion records from Salesforce customers
- **Qilin Ransomware**: Successfully attacked Asahi brewery causing beer shortage and production disruptions
- **Chinese-Nexus Actors**: Weaponizing Nezha open-source tool to deliver Gh0st RAT malware
- **Russian State Actors**: Adopting AI technologies for enhanced cyber operations against Ukraine
- **BatShadow**: Vietnamese cybercrime group operating Vampire Bot malware targeting job hunters
- **Ransomware Cartel**: LockBit, Qilin, and DragonForce forming strategic alliance to share resources and attack information
- **Nation-State Groups**: Russian, North Korean, and Chinese hackers misusing ChatGPT for malware development and cyberattacks