# Exploitation Report

The current threat landscape reveals several critical exploitation activities targeting diverse systems and platforms. Most notably, CISA has issued warnings about active exploitation of a critical vulnerability in the Langflow AI framework (CVE-2026-33017), which threat actors began exploiting within hours of disclosure. Additionally, sophisticated attack campaigns are underway including the evolution of iOS exploitation frameworks linked to Operation Triangulation, mass attacks targeting Magento e-commerce platforms through PolyShell vulnerabilities, and advanced espionage operations by China-linked threat actors using stealthy BPFDoor implants in telecommunications networks. The exploitation landscape also includes novel attack techniques such as WebRTC-based payment skimmers that bypass content security policies and zero-click XSS attacks against AI browser extensions.

## Active Exploitation Details

### Langflow AI Framework Critical Vulnerability
- **Description**: A critical code injection vulnerability affecting the Langflow framework that allows attackers to hijack AI workflows
- **Impact**: Attackers can execute arbitrary code and take control of AI workflow systems
- **Status**: Actively exploited in the wild, with threat actors exploiting the vulnerability within hours of its disclosure
- **CVE ID**: CVE-2026-33017

### PolyShell Magento Vulnerability
- **Description**: A vulnerability affecting Magento Open Source version 2 and Adobe Commerce installations
- **Impact**: Allows attackers to compromise e-commerce stores and potentially access sensitive customer and payment data
- **Status**: Actively exploited, targeting 56% of all vulnerable Magento stores in ongoing campaigns

### iOS Zero-Click Exploits (Coruna Framework)
- **Description**: An evolution of the exploit framework used in Operation Triangulation, utilizing zero-click iMessage exploits targeting iOS devices
- **Impact**: Enables remote device compromise without user interaction, allowing for espionage and data theft
- **Status**: Active exploitation framework linked to recent mass attacks, reusing exploit code from 2023 Triangulation attacks

### Claude Chrome Extension XSS Vulnerability
- **Description**: A vulnerability in Anthropic's Claude Google Chrome Extension that enables zero-click cross-site scripting (XSS) and prompt injection attacks
- **Impact**: Attackers can trigger malicious prompts and potentially compromise user data simply by visiting a malicious webpage
- **Status**: Vulnerability disclosed and patched, but demonstrates active research into AI extension exploitation

### Ajax Football Club IT System Vulnerabilities
- **Description**: Unspecified vulnerabilities in Ajax Amsterdam's IT systems that allowed unauthorized access to fan data
- **Impact**: Exposure of personal data belonging to hundreds of fans and potential ticket hijacking capabilities
- **Status**: Exploited by attackers, with the club disclosing the breach and implementing remediation measures

## Affected Systems and Products

- **Langflow AI Framework**: Critical vulnerability enabling workflow hijacking and code injection
- **Magento Open Source v2 and Adobe Commerce**: PolyShell vulnerability affecting over half of vulnerable installations
- **iOS Devices**: Targeted by sophisticated zero-click exploit frameworks via iMessage
- **Chrome Browser Extensions**: Specifically Claude extension vulnerable to XSS and prompt injection
- **Ajax FC IT Infrastructure**: Web applications and databases containing fan registration and ticketing data
- **NetScaler ADC and Gateway**: Citrix networking products with newly patched vulnerabilities similar to previous CitrixBleed flaws
- **E-commerce Platforms**: Payment systems targeted by WebRTC-based skimmers that bypass content security policies
- **Telecommunications Networks**: Infrastructure compromised by China-linked threat actors using BPFDoor implants

## Attack Vectors and Techniques

- **Code Injection**: Exploitation of the Langflow framework vulnerability to execute arbitrary code in AI workflows
- **Zero-Click Exploitation**: iOS attacks requiring no user interaction through malicious iMessage payloads
- **Web Application Attacks**: PolyShell campaigns targeting vulnerable Magento installations through web-based vulnerabilities
- **WebRTC Data Channel Abuse**: Novel payment skimmer technique using WebRTC to bypass content security policies and exfiltrate payment data
- **Prompt Injection**: XSS attacks against AI browser extensions to manipulate AI model responses
- **Network Infrastructure Compromise**: Strategic positioning within telecommunications networks for long-term espionage
- **Social Engineering**: Phishing campaigns targeting TikTok for Business accounts with bot-resistant malicious pages
- **Credential Stuffing**: Multi-stage fraud attacks chaining bot signups with stolen credentials for account takeovers

## Threat Actor Activities

- **China-Linked Red Menshen Group**: Conducting long-term espionage campaigns through strategic positioning in telecommunications networks using stealthy BPFDoor implants to spy on government networks
- **iOS Exploit Kit Operators**: Deploying the Coruna framework in mass attack campaigns, leveraging updated versions of Operation Triangulation exploit code
- **PolyShell Campaign Actors**: Systematically targeting vulnerable Magento stores with automated attacks affecting majority of susceptible installations
- **Payment Skimmer Operators**: Developing sophisticated WebRTC-based skimmers to steal e-commerce payment data while evading security controls
- **AI Platform Attackers**: Rapidly exploiting newly disclosed Langflow vulnerabilities within hours of public disclosure for workflow hijacking
- **RedLine Malware Administrators**: Operating prolific infostealer malware campaigns with suspected administrator facing extradition to the United States
- **LeakBase Forum Operators**: Managing major cybercrime marketplace for stolen data and hacking tools until recent arrest by Russian authorities