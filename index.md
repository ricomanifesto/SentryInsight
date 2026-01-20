# Exploitation Report

The current threat landscape reveals several critical security vulnerabilities being actively exploited across multiple platforms and technologies. Most notable are prompt injection attacks against Google Gemini AI that allow bypassing privacy controls through malicious calendar invites, serious vulnerabilities in AI Model Context Protocol servers enabling remote code execution and cloud takeovers, a new hardware flaw affecting AMD processors that breaks security protections, and sophisticated malware campaigns using fake browser extensions and LinkedIn messages to deploy remote access trojans. These attacks demonstrate the evolving threat landscape where traditional security boundaries are being circumvented through AI manipulation, supply chain compromises, and social engineering techniques.

## Active Exploitation Details

### Google Gemini Indirect Prompt Injection
- **Description**: A prompt injection vulnerability in Google Gemini AI assistant that can be exploited through malicious Google Calendar invites to bypass authorization guardrails
- **Impact**: Attackers can access private calendar data, circumvent Google's privacy controls, and potentially extract sensitive information from user accounts
- **Status**: Vulnerability disclosed by researchers, current patch status unclear

### Anthropic MCP Git Server Vulnerabilities
- **Description**: Three security vulnerabilities in mcp-server-git, the official Git Model Context Protocol server maintained by Anthropic
- **Impact**: Attackers can read or delete arbitrary files, achieve remote code execution, and potentially take over cloud environments
- **Status**: Actively exploitable vulnerabilities affecting popular AI service components

### StackWarp Hardware Vulnerability
- **Description**: A hardware-level security flaw affecting AMD processors from Zen 1 through Zen 5 architectures that breaks AMD SEV-SNP (Secure Encrypted Virtualization-Secure Nested Paging) protections
- **Impact**: Attackers can bypass hardware-level security protections designed to isolate sensitive workloads in virtualized environments
- **Status**: Hardware vulnerability affecting multiple generations of AMD CPUs, requiring potential firmware updates

### Cloudflare ACME Validation Bug
- **Description**: A security vulnerability in Cloudflare's Automatic Certificate Management Environment validation logic
- **Impact**: Allows attackers to bypass Web Application Firewall (WAF) controls and directly access origin servers
- **Status**: Fixed by Cloudflare, but previously exploitable

## Affected Systems and Products

- **Google Gemini AI Assistant**: Vulnerable to prompt injection attacks through calendar integration
- **Anthropic MCP Servers**: Git Model Context Protocol servers with file access and code execution vulnerabilities
- **AMD Processors**: Zen 1 through Zen 5 CPU architectures affected by StackWarp hardware flaw
- **Microsoft PowerToys**: New version 0.97 released with CursorWrap utility (no vulnerabilities reported)
- **Google Chrome/Edge Browsers**: Targeted by fake NexShield ad blocker extension in malvertising campaigns
- **Microsoft Visual Studio Code**: Abused by Evelyn Stealer malware through weaponized extensions
- **Cloudflare ACME Services**: Previously vulnerable validation logic allowing WAF bypass
- **StealC Malware Panel**: Contains cross-site scripting vulnerability in web-based control panel

## Attack Vectors and Techniques

- **Prompt Injection**: Natural language attacks against AI systems using malicious calendar invites to bypass security controls
- **Malicious Browser Extensions**: Fake ad blockers like NexShield that deliberately crash browsers for ClickFix attacks
- **DLL Sideloading**: LinkedIn-based phishing campaigns deploying remote access trojans through malicious DLL files
- **Social Engineering**: LinkedIn private messages used to distribute malware payloads
- **Supply Chain Attacks**: Weaponization of legitimate development tools like VS Code extensions
- **Hardware-Level Exploitation**: StackWarp attacks targeting AMD processor security features
- **Certificate Validation Bypass**: Exploiting ACME validation flaws to circumvent web security controls
- **Cross-Site Scripting**: XSS vulnerabilities in malware control panels allowing researcher infiltration

## Threat Actor Activities

### KongTuke Campaign
- **Actor/Group**: Cybercriminals operating malvertising campaigns using fake Chrome extensions
- **Campaign**: Distribution of ModeloRAT malware through NexShield fake ad blocker that crashes browsers to facilitate ClickFix-style attacks

### Russian-Aligned Hacktivist Groups
- **Actor/Group**: Multiple Russian hacktivist organizations targeting UK infrastructure
- **Campaign**: Ongoing attacks against critical infrastructure and local government organizations in the United Kingdom, as warned by UK government authorities

### LinkedIn-Based RAT Distributors
- **Actor/Group**: Cybercriminals using social media platforms for malware distribution
- **Campaign**: Phishing operations through LinkedIn private messages to deploy remote access trojans via DLL sideloading techniques

### Evelyn Stealer Operators
- **Actor/Group**: Malware developers targeting software developers and cryptocurrency users
- **Campaign**: Information stealing operations using weaponized Visual Studio Code extensions to harvest credentials and cryptocurrency wallet data

### Supreme Court Hacker
- **Actor/Group**: Individual threat actor from Tennessee who targeted US government systems
- **Campaign**: Successful breaches of US Supreme Court electronic filing system, AmeriCorps, and Department of Veterans Affairs, with stolen data leaked on Instagram

### Access Broker Operations
- **Actor/Group**: Jordanian national operating as network access broker
- **Campaign**: Selling unauthorized access to computer networks of at least 50 companies to other cybercriminals