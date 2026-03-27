# Exploitation Report

Several critical vulnerabilities are currently under active exploitation, with the most concerning being a zero-day flaw in the Langflow AI framework (CVE-2026-33017) that CISA has warned is being actively exploited by threat actors to hijack AI workflows. Additionally, widespread attacks are targeting vulnerable Magento stores through the PolyShell vulnerability, affecting over 56% of all vulnerable installations. The cyberthreat landscape also includes sophisticated iOS exploit frameworks like Coruna, which reuses code from previous Triangulation campaigns, and new WebRTC-based payment skimmers that bypass Content Security Policy protections on e-commerce sites.

## Active Exploitation Details

### Langflow AI Framework Vulnerability
- **Description**: A critical code injection vulnerability in the Langflow framework that allows attackers to execute malicious code
- **Impact**: Complete hijacking of AI workflows and potential system compromise
- **Status**: Actively exploited in the wild, with threat actors pouncing on the vulnerability within hours of disclosure
- **CVE ID**: CVE-2026-33017

### PolyShell Magento Vulnerability
- **Description**: A vulnerability affecting Magento Open Source version 2 and Adobe Commerce installations
- **Impact**: Compromise of e-commerce stores and potential access to customer data and payment information
- **Status**: Active exploitation targeting 56% of all vulnerable Magento stores

### Coruna iOS Exploit Kit
- **Description**: An evolution of the framework used in Operation Triangulation, targeting iPhones via zero-click iMessage exploits
- **Impact**: Complete device compromise and espionage capabilities on iOS devices
- **Status**: Recently discovered exploit kit reusing 2023 Triangulation exploit code

### WebRTC Payment Skimmer
- **Description**: A sophisticated payment skimmer that uses WebRTC data channels to receive payloads and exfiltrate data
- **Impact**: Theft of payment card data from e-commerce websites while bypassing Content Security Policy protections
- **Status**: Active deployment on compromised e-commerce sites

### Ajax Football Club System Vulnerabilities
- **Description**: Unspecified vulnerabilities in Ajax Amsterdam's IT systems
- **Impact**: Exposure of fan data and enabling of ticket hijacking attacks
- **Status**: Successfully exploited, affecting hundreds of people

### Claude Chrome Extension Vulnerability
- **Description**: A zero-click XSS prompt injection vulnerability in Anthropic's Claude Google Chrome Extension
- **Impact**: Malicious prompt execution simply by visiting a web page
- **Status**: Vulnerability disclosed and patched

## Affected Systems and Products

- **Langflow Framework**: AI workflow platform vulnerable to code injection attacks
- **Magento Open Source v2**: E-commerce platform with over half of vulnerable installations under attack
- **Adobe Commerce**: Enterprise e-commerce solution affected by PolyShell vulnerability
- **iOS Devices**: iPhones targeted by Coruna exploit kit through iMessage
- **E-commerce Websites**: Sites using vulnerable payment processing systems targeted by WebRTC skimmers
- **Ajax Amsterdam IT Systems**: Football club infrastructure compromised through multiple vulnerabilities
- **Claude Chrome Extension**: Anthropic's AI assistant browser extension vulnerable to XSS attacks
- **NetScaler ADC and Gateway**: Citrix networking products with newly disclosed vulnerabilities requiring urgent patching

## Attack Vectors and Techniques

- **Code Injection**: Direct exploitation of vulnerable Langflow installations for workflow hijacking
- **Zero-Click Exploits**: Coruna framework delivers payloads through iMessage without user interaction
- **WebRTC Data Channels**: Novel technique bypassing CSP protections to exfiltrate payment data
- **XSS Prompt Injection**: Zero-click exploitation through malicious web page visits
- **Web Application Exploitation**: Direct targeting of vulnerable Magento installations
- **Social Engineering**: Phishing campaigns targeting TikTok for Business accounts with bot-resistant pages
- **Credential Stuffing**: Multi-stage fraud attacks using bots, proxies, and stolen credentials

## Threat Actor Activities

- **China-Linked Red Menshen**: Long-term espionage campaign embedding BPFDoor implants in telecom networks to spy on government networks
- **Unknown Langflow Attackers**: Rapid exploitation of CVE-2026-33017 within hours of disclosure
- **PolyShell Operators**: Systematic targeting of vulnerable Magento stores affecting majority of vulnerable installations
- **Payment Card Skimmer Groups**: Deployment of sophisticated WebRTC-based skimmers across multiple e-commerce sites
- **TikTok Phishing Operators**: Targeting business accounts with advanced bot-detection evasion techniques
- **RedLine Malware Administrators**: Continued operation of one of the most prolific infostealer malware families
- **Coruna Kit Operators**: Reuse and evolution of previous Triangulation campaign code for mass iOS attacks