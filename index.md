# Exploitation Report

The current threat landscape reveals a surge in sophisticated exploitation activities spanning multiple attack vectors. Critical vulnerabilities are being actively exploited across WordPress themes, cloud infrastructure, and AI-integrated systems. Notable threat actors including Crimson Collective, LockBit, Qilin, and DragonForce are collaborating in unprecedented ways while leveraging both zero-day exploits and social engineering techniques. The formation of ransomware cartels and the weaponization of legitimate tools like Nezha demonstrate the evolving nature of modern cyber threats.

## Active Exploitation Details

### Service Finder WordPress Theme Authentication Bypass
- **Description**: A critical vulnerability in the Service Finder WordPress theme that allows authentication bypass
- **Impact**: Threat actors can bypass authentication mechanisms and log in as administrators, gaining full control over WordPress sites
- **Status**: Currently being actively exploited by threat actors

### Framelink Figma MCP Server Remote Code Execution
- **Description**: A severe vulnerability in the figma-developer-mcp Model Context Protocol server that enables remote code execution
- **Impact**: Attackers can achieve code execution on systems running the vulnerable MCP server, potentially leading to full system compromise
- **Status**: Vulnerability has been patched, but organizations need to update immediately
- **CVE ID**: CVE-2025-53967

### FileFix Cache Smuggling Attack
- **Description**: A new variant of the FileFix social engineering attack that uses cache smuggling techniques
- **Impact**: Secretly downloads malicious ZIP archives onto victim systems while evading security software detection
- **Status**: Active exploitation observed in the wild

### WordPress Site JavaScript Injection
- **Description**: Malicious JavaScript injections targeting WordPress sites to redirect users to malicious destinations
- **Impact**: Site visitors are redirected to sketchy sites as part of next-generation ClickFix phishing campaigns
- **Status**: Ongoing campaign with active exploitation

## Affected Systems and Products

- **Service Finder WordPress Theme**: Critical authentication bypass vulnerability allowing administrative access
- **Discord Zendesk Support System**: Breach affecting 5.5 million unique users with exposed government IDs
- **Figma MCP Server**: Remote code execution vulnerability in third-party AI integration
- **WordPress Sites**: Multiple sites compromised for JavaScript injection and redirection attacks
- **AWS Cloud Instances**: Targeted by Crimson Collective for data theft and extortion
- **Asahi Brewery Systems**: Hit by Qilin ransomware affecting order processing and delivery
- **Salesforce Customer Data**: Massive data theft affecting billions of records
- **DraftKings User Accounts**: Compromised through credential stuffing attacks

## Attack Vectors and Techniques

- **Cache Smuggling**: FileFix attacks use cache smuggling to bypass security software and deliver malicious payloads
- **JavaScript Injection**: WordPress sites compromised to inject malicious scripts for user redirection
- **Authentication Bypass**: Service Finder theme vulnerability exploited to gain administrative access
- **Voice Phishing (Vishing)**: ShinyHunters group uses voice phishing to steal Salesforce customer data
- **Credential Stuffing**: Automated attacks using stolen credentials against DraftKings accounts
- **Social Engineering**: Job-themed lures targeting influencers with fake Tesla and Red Bull positions
- **Weaponized Legitimate Tools**: Chinese actors using Nezha open-source monitoring tool to deliver Gh0st RAT

## Threat Actor Activities

- **Crimson Collective**: Actively targeting AWS cloud environments for data theft and extortion, recently collaborated with Scattered Spider/Lapsus$ group after breaching Red Hat Consulting's GitLab instance
- **BatShadow**: Vietnamese cybercrime group behind Vampire Bot malware campaign targeting job hunters
- **Qilin Ransomware Group**: Claimed responsibility for Asahi brewery attack, causing beer shortage and operational disruption
- **LockBit, Qilin & DragonForce**: Formed unprecedented ransomware cartel collaboration sharing attack information and resources, coinciding with LockBit 5.0 release
- **ShinyHunters**: Conducting broad corporate extortion spree, responsible for stealing over billion records from Salesforce customers through voice phishing
- **Chinese State-Nexus Actors**: Weaponizing legitimate Nezha open-source tool to deliver Gh0st RAT malware in sophisticated supply chain attacks
- **Russian, North Korean & Chinese Hackers**: Disrupted by OpenAI for misusing ChatGPT to facilitate malware development and cyberattacks