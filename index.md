# Exploitation Report

Current threat landscape shows intense exploitation activity across multiple attack vectors, with critical authentication bypass vulnerabilities in WordPress themes being actively exploited alongside sophisticated social engineering campaigns. Threat actors are leveraging legitimate cloud services like AWS for data theft operations, while ransomware groups are forming strategic alliances to enhance their collective impact. Notable campaigns include authentication bypass exploits in WordPress Service Finder themes, FileFix cache smuggling attacks, and widespread credential stuffing operations targeting major platforms.

## Active Exploitation Details

### Service Finder WordPress Theme Authentication Bypass
- **Description**: Critical vulnerability allowing threat actors to bypass authentication mechanisms in the Service Finder WordPress theme
- **Impact**: Attackers can gain unauthorized access to any account, including administrator-level access, potentially leading to complete website compromise
- **Status**: Actively exploited in the wild with ongoing attacks targeting vulnerable installations

### Figma MCP Server Remote Code Execution
- **Description**: Severe vulnerability in the figma-developer-mcp Model Context Protocol server that enables remote code execution
- **Impact**: Attackers can execute arbitrary code remotely, potentially compromising entire systems running the vulnerable MCP server
- **Status**: Now patched, but organizations need immediate updates to prevent exploitation
- **CVE ID**: CVE-2025-53967

### FileFix Cache Smuggling Attack
- **Description**: New variant of FileFix social engineering attack utilizing cache smuggling techniques to secretly download malicious ZIP archives
- **Impact**: Bypasses security software detection while delivering malicious payloads to victim systems
- **Status**: Active campaign with evolving techniques to evade detection

### WordPress Sites JavaScript Injection
- **Description**: Malicious JavaScript injections targeting WordPress sites to redirect users to malicious destinations
- **Impact**: Site visitors are redirected to sketchy sites as part of next-generation ClickFix phishing campaigns
- **Status**: Ongoing campaign targeting multiple WordPress installations

## Affected Systems and Products

- **Service Finder WordPress Theme**: Critical authentication bypass affecting all installations
- **Discord Zendesk Support System**: Alleged breach exposing data of 5.5 million users including government IDs
- **Figma MCP Server**: Organizations using figma-developer-mcp Model Context Protocol server
- **WordPress Sites**: Multiple installations targeted for malicious JavaScript injection campaigns
- **AWS Cloud Instances**: Crimson Collective targeting Amazon Web Services environments for data theft
- **Asahi Brewery Systems**: Japanese beer manufacturer hit by Qilin ransomware affecting operations
- **Red Hat GitLab Instance**: Crimson Collective breach of Red Hat Consulting GitLab systems
- **DraftKings User Accounts**: Sports betting platform targeted in credential stuffing attacks
- **Salesforce Customer Systems**: Widespread data theft attacks affecting multiple customer accounts

## Attack Vectors and Techniques

- **Authentication Bypass**: Exploiting critical flaws in WordPress themes to gain unauthorized administrative access
- **Cache Smuggling**: Using cache manipulation to secretly download malicious archives while bypassing security software
- **JavaScript Injection**: Injecting malicious code into WordPress sites for redirection attacks
- **Voice Phishing (Vishing)**: ShinyHunters using voice-based social engineering to access Salesforce customer data
- **Credential Stuffing**: Automated attacks using previously compromised credentials against multiple platforms
- **Cloud Instance Targeting**: Direct attacks against AWS cloud environments for data exfiltration
- **Ransomware Deployment**: Traditional encryption-based extortion with data theft components
- **Social Engineering**: Job-themed phishing campaigns targeting influencers with fake Tesla and Red Bull positions
- **RMM Tool Weaponization**: Chinese threat actors using legitimate Nezha monitoring tool for malicious purposes

## Threat Actor Activities

- **ShinyHunters**: Conducting broad corporate extortion campaigns, launched website threatening to publish stolen data from multiple organizations, previously siphoned over a billion records from Salesforce customers
- **Crimson Collective**: Partnering with Scattered Lapsus$ hunters, targeting AWS cloud instances for data theft, recently breached Red Hat Consulting GitLab instance
- **Qilin Ransomware Group**: Claimed responsibility for Asahi brewery attack, leaked company data on dark web extortion page, formed strategic alliance with LockBit and DragonForce
- **LockBit, DragonForce Alliance**: Three major ransomware groups formed strategic coalition sharing attack information and resources, released LockBit 5.0 and invited other cybercriminals to join collaboration
- **BatShadow Group**: Vietnamese cybercrime group behind Vampire Bot malware campaign targeting job hunters
- **Chinese-Nexus Actors**: Weaponizing legitimate Nezha open-source monitoring tool to deliver Gh0st RAT malware to targets
- **Russian, North Korean, Chinese State Actors**: Misusing ChatGPT AI tool for malware development and cyberattack facilitation before being disrupted by OpenAI