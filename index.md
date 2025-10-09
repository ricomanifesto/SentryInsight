# Exploitation Report

Current threat landscape shows active exploitation across multiple attack vectors, with threat actors targeting cloud environments, WordPress sites, and leveraging social engineering campaigns. Notable activities include Crimson Collective's targeting of AWS cloud instances, active exploitation of authentication bypass vulnerabilities in WordPress themes, and sophisticated ransomware cartel formations between major groups. Additionally, threat actors are weaponizing legitimate open-source tools and conducting widespread data theft campaigns against major platforms.

## Active Exploitation Details

### Service Finder WordPress Theme Authentication Bypass
- **Description**: Critical vulnerability allowing attackers to bypass authentication mechanisms and gain administrative access to WordPress sites
- **Impact**: Complete administrative takeover of affected WordPress installations, enabling malicious content injection and site compromise
- **Status**: Currently under active exploitation by threat actors

### Framelink Figma MCP Server Remote Code Execution
- **Description**: Vulnerability in the figma-developer-mcp Model Context Protocol server that enables remote code execution
- **Impact**: Attackers can achieve code execution on systems using the vulnerable MCP server, potentially compromising agentic AI implementations
- **Status**: Patched, but organizations need immediate updates
- **CVE ID**: CVE-2025-53967

### WordPress Site JavaScript Injection
- **Description**: Campaign targeting WordPress sites through malicious JavaScript injections via compromised themes
- **Impact**: Redirection of legitimate users to malicious sites, enabling ClickFix phishing attacks and credential theft
- **Status**: Ongoing active exploitation across multiple WordPress installations

## Affected Systems and Products

- **Discord Zendesk Support System**: Breach exposing data of 5.5 million users including government IDs
- **Red Hat Consulting GitLab Instance**: Compromised by Crimson Collective threat group
- **Asahi Brewery Systems**: Ransomware attack by Qilin group causing operational disruption and beer shortage
- **AWS Cloud Environments**: Targeted by Crimson Collective for data theft and extortion
- **WordPress Sites**: Multiple sites compromised through Service Finder theme vulnerabilities and JavaScript injection attacks
- **figma-developer-mcp Servers**: Systems using the vulnerable MCP server exposed to remote code execution
- **DraftKings User Accounts**: Compromised through credential stuffing attacks
- **Salesforce Customer Data**: Widespread data theft affecting multiple customers

## Attack Vectors and Techniques

- **Cache Smuggling**: FileFix variant using cache smuggling to secretly download malicious ZIP archives while evading security software
- **Social Engineering**: BatShadow group's Vampire Bot malware campaign targeting job seekers with fake employment opportunities
- **Credential Stuffing**: Large-scale automated attacks against user accounts using compromised credential lists
- **Authentication Bypass**: Exploitation of WordPress theme vulnerabilities to gain unauthorized administrative access
- **JavaScript Injection**: Malicious code injection into WordPress sites for traffic redirection and phishing campaigns
- **Cloud Environment Targeting**: Direct attacks on AWS instances for data exfiltration and extortion
- **Weaponized Legitimate Tools**: Chinese threat actors using Nezha open-source monitoring tool to deliver Gh0st RAT malware

## Threat Actor Activities

- **Crimson Collective**: Active targeting of AWS cloud environments and successful breach of Red Hat Consulting's GitLab instance, now collaborating with Scattered Spider/Lapsus$ group
- **BatShadow**: Vietnamese cybercrime group conducting sophisticated social engineering campaigns using Go-based Vampire Bot malware against job seekers
- **Qilin Ransomware Group**: Successful attack on Asahi brewery causing operational disruption, also part of new ransomware cartel alliance
- **LockBit-Qilin-DragonForce Cartel**: Formation of ransomware alliance sharing attack information and resources, inviting other cybercriminal groups to join
- **Chinese State-Nexus Actors**: Weaponization of Nezha open-source tool for remote monitoring and Gh0st RAT deployment
- **Discord Breach Actors**: Threat group claiming theft of 5.5 million user records from Discord's Zendesk support system
- **Russian, North Korean, and Chinese Hackers**: Groups disrupted by OpenAI for misusing ChatGPT to facilitate malware development and cyberattacks