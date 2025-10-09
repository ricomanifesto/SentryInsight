# Exploitation Report

Current cybersecurity threat landscape shows significant active exploitation across multiple attack vectors, with threat actors targeting cloud environments, WordPress platforms, and leveraging social engineering techniques. Notable activities include the Crimson Collective's AWS cloud targeting operations, active exploitation of WordPress authentication bypasses, ransomware cartel formations, and sophisticated phishing campaigns targeting job seekers and influencers. CVE-2025-53967 has been identified in the Figma MCP server enabling remote code execution, while various groups are weaponizing legitimate tools like Nezha for malicious purposes.

## Active Exploitation Details

### Service Finder WordPress Theme Authentication Bypass
- **Description**: Critical vulnerability allowing threat actors to bypass authentication mechanisms and gain administrative access to WordPress sites
- **Impact**: Complete administrative control over affected WordPress installations, enabling malicious code injection and site takeover
- **Status**: Actively exploited in the wild by multiple threat actors

### Figma MCP Server Remote Code Execution
- **Description**: Severe vulnerability in the figma-developer-mcp Model Context Protocol server allowing attackers to achieve code execution
- **Impact**: Remote code execution capabilities that can lead to complete system compromise
- **Status**: Patched vulnerability that was actively exploited
- **CVE ID**: CVE-2025-53967

### WordPress Theme Malicious JavaScript Injection
- **Description**: Campaign targeting WordPress sites with malicious JavaScript injections designed to redirect users to malicious sites
- **Impact**: Site visitors redirected to sketchy sites, potential for credential harvesting and malware distribution
- **Status**: Ongoing active campaign affecting WordPress installations

### FileFix Cache Smuggling Attack
- **Description**: New variant of FileFix social engineering attack using cache smuggling techniques to secretly download malicious ZIP archives
- **Impact**: Bypasses security software detection and delivers malware payload to victim systems
- **Status**: Newly discovered attack method being actively deployed

## Affected Systems and Products

- **WordPress Sites**: Service Finder theme and various other WordPress installations targeted for authentication bypass and malicious code injection
- **AWS Cloud Instances**: Amazon Web Services environments targeted by Crimson Collective for data theft and extortion
- **Figma MCP Server**: Third-party Model Context Protocol server for connecting Figma to agentic AI systems
- **Discord Zendesk**: Support system compromised affecting 5.5 million users with government IDs exposed
- **Asahi Brewery Systems**: Japanese beer manufacturer hit by Qilin ransomware affecting production and order systems
- **DraftKings Accounts**: Sports betting platform accounts compromised through credential stuffing attacks

## Attack Vectors and Techniques

- **Authentication Bypass**: Exploiting vulnerabilities in WordPress themes to gain unauthorized administrative access
- **Cache Smuggling**: Using browser cache manipulation to bypass security software and deliver malicious payloads
- **Voice Phishing (Vishing)**: ShinyHunters group using voice-based social engineering to steal Salesforce customer data
- **Credential Stuffing**: Automated attacks using previously compromised credentials against multiple platforms
- **Social Engineering**: Job-themed phishing campaigns targeting influencers with fake Tesla and Red Bull job offers
- **JavaScript Injection**: Compromising WordPress sites to inject malicious scripts for traffic redirection
- **Tool Weaponization**: Converting legitimate monitoring tools like Nezha into attack infrastructure

## Threat Actor Activities

- **Crimson Collective**: Targeting AWS cloud environments for data theft and extortion, recently partnered with Scattered Spider/Lapsus$ group and breached Red Hat Consulting GitLab instance
- **Qilin Ransomware Group**: Claimed responsibility for Asahi brewery attack, leaked company data, and formed strategic alliance with LockBit and DragonForce
- **LockBit, Qilin & DragonForce Alliance**: Three major ransomware groups formed collaborative "cartel" to share attack information and resources, coinciding with LockBit 5.0 release
- **BatShadow**: Vietnamese cybercrime group behind Vampire Bot malware campaign targeting job seekers
- **ShinyHunters**: Conducting broad corporate extortion spree after stealing over a billion records from Salesforce customers through voice phishing
- **Chinese-Nexus Actors**: Weaponizing legitimate Nezha open-source monitoring tool to deliver Gh0st RAT malware to targets
- **State-Sponsored Groups**: Russian, North Korean, and Chinese threat actors disrupted by OpenAI for misusing ChatGPT to facilitate malware development