# Exploitation Report

Critical AI framework vulnerabilities are currently under active exploitation, with CISA warning about hackers targeting the Langflow platform through CVE-2026-33017. This critical code injection vulnerability demonstrates how quickly threat actors respond to new disclosures, with attacks beginning within hours of public disclosure. Meanwhile, sophisticated espionage campaigns continue with the China-linked Red Menshen group using stealthy BPFDoor implants to spy on government networks through telecom infrastructure. The threat landscape also includes evolution of iOS exploit frameworks, with the Coruna kit reusing code from the 2023 Operation Triangulation attacks for mass targeting campaigns. Additionally, widespread attacks against e-commerce platforms continue with PolyShell targeting over half of all vulnerable Magento stores and new payment skimmers using WebRTC channels to bypass security controls.

## Active Exploitation Details

### Langflow AI Framework Vulnerability
- **Description**: A critical code injection vulnerability affecting the Langflow framework that enables attackers to hijack AI workflows
- **Impact**: Attackers can execute arbitrary code and take control of AI workflow systems
- **Status**: Currently being actively exploited in the wild, with attacks starting within hours of disclosure
- **CVE ID**: CVE-2026-33017

### PolyShell Magento Vulnerability
- **Description**: A critical vulnerability affecting Magento Open Source and Adobe Commerce version 2 installations
- **Impact**: Allows attackers to compromise e-commerce platforms and potentially steal customer data and payment information
- **Status**: Actively exploited, targeting 56% of all vulnerable Magento stores

### Operation Triangulation iOS Exploits
- **Description**: Evolved exploit framework called Coruna that reuses kernel exploit code from the 2023 Operation Triangulation campaign
- **Impact**: Zero-click iMessage exploits targeting iPhones for espionage purposes
- **Status**: Recently discovered mass attack campaigns using updated versions of 2023 exploit code

### Claude Chrome Extension Vulnerability
- **Description**: A zero-click XSS prompt injection vulnerability in Anthropic's Claude Google Chrome Extension
- **Impact**: Malicious prompts could be triggered simply by visiting a compromised web page
- **Status**: Vulnerability disclosed and patched, previously exploitable for zero-click attacks

## Affected Systems and Products

- **Langflow Framework**: AI workflow management platform actively targeted by attackers
- **Magento Open Source v2**: E-commerce platform with over half of vulnerable installations under attack
- **Adobe Commerce v2**: Enterprise e-commerce solution affected by PolyShell attacks
- **Apple iOS Devices**: iPhones targeted by evolved Triangulation exploit framework
- **Claude Chrome Extension**: AI assistant browser extension vulnerable to prompt injection
- **Telecom Network Infrastructure**: Government and telecom networks infiltrated by BPFDoor implants
- **E-commerce Websites**: Payment systems targeted by WebRTC-based skimmer malware
- **Ajax Football Club Systems**: IT infrastructure compromised exposing fan data and enabling ticket hijacking
- **LangChain/LangGraph**: AI frameworks with disclosed vulnerabilities exposing files and secrets

## Attack Vectors and Techniques

- **Code Injection**: Critical vulnerability in Langflow enabling arbitrary code execution
- **Zero-Click Exploits**: iMessage-based attacks requiring no user interaction on iOS devices
- **Prompt Injection**: XSS-based attacks against AI assistant browser extensions
- **WebRTC Data Channels**: Payment skimmers using WebRTC to bypass Content Security Policy controls
- **Phishing Campaigns**: Multi-stage attacks targeting TikTok Business accounts and Microsoft credentials
- **Network Infiltration**: Long-term embedding in telecom infrastructure for espionage
- **E-commerce Compromise**: Mass targeting of vulnerable Magento installations
- **Browser Extension Abuse**: Bubble platform misused to host malicious phishing applications

## Threat Actor Activities

- **Red Menshen (China-linked)**: Conducting long-term espionage campaign using BPFDoor implants embedded in telecom networks to spy on government systems
- **PolyShell Attackers**: Mass exploitation campaign targeting 56% of vulnerable Magento stores for e-commerce compromise
- **Coruna Kit Operators**: iOS exploit framework distributors conducting mass attacks using evolved Triangulation exploit code
- **WebRTC Skimmer Groups**: E-commerce payment data theft using novel WebRTC bypass techniques
- **AI Platform Attackers**: Rapid exploitation of Langflow vulnerability within hours of disclosure
- **TikTok Phishers**: Business account targeting campaign with anti-bot detection evasion
- **Microsoft Credential Harvesters**: Bubble platform abuse for phishing campaign infrastructure