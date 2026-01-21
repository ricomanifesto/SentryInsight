# Exploitation Report

The security landscape reveals several critical active exploitation activities across multiple platforms and systems. A critical vulnerability in the Advanced Custom Fields: Extended WordPress plugin is being actively exploited to grant hackers administrative access on approximately 50,000 WordPress sites. Meanwhile, sophisticated attack campaigns are targeting developers through malicious Visual Studio Code projects, with North Korean threat actors deploying backdoors through the Contagious Interview campaign. Additional threats include AI-generated cloud malware frameworks, browser-crashing scams designed to deliver malware, and exploitation of AI assistant vulnerabilities to leak private data. Several vulnerabilities in AI frameworks and model context protocol servers are creating opportunities for remote code execution and cloud takeovers.

## Active Exploitation Details

### Advanced Custom Fields: Extended WordPress Plugin Vulnerability
- **Description**: A critical-severity vulnerability in the ACF Extended plugin for WordPress that allows remote exploitation by unauthenticated attackers
- **Impact**: Attackers can obtain administrative permissions on WordPress sites, giving them full control over affected websites
- **Status**: Currently being actively exploited against approximately 50,000 WordPress sites

### Cloudflare ACME Validation Vulnerability  
- **Description**: Security vulnerability in Cloudflare's Automatic Certificate Management Environment (ACME) validation logic
- **Impact**: Allows attackers to bypass security controls and access origin servers directly, circumventing Web Application Firewall protections
- **Status**: Recently fixed by Cloudflare, but previously exploitable

### Google Gemini Prompt Injection Vulnerability
- **Description**: Indirect prompt injection flaw that leverages malicious Google Calendar invites to bypass authorization guardrails
- **Impact**: Attackers can access private Calendar data and potentially other Google services by weaponizing calendar invites
- **Status**: Actively exploitable through natural language instructions and social engineering

### Anthropic MCP Git Server Vulnerabilities
- **Description**: Three security flaws in the official Git Model Context Protocol server maintained by Anthropic
- **Impact**: Enable file access, code execution, and potential cloud takeovers through remote code execution
- **Status**: Disclosed vulnerabilities with proof-of-concept available

## Affected Systems and Products

- **WordPress Sites**: Approximately 50,000 sites running the Advanced Custom Fields: Extended plugin
- **Cloudflare Protected Sites**: Origin servers behind Cloudflare's ACME validation system
- **Google Gemini Users**: Users with integrated Google Calendar access through Gemini AI assistant
- **Visual Studio Code**: Developers using VS Code projects, particularly targeted by North Korean threat actors
- **Anthropic MCP Servers**: AI services utilizing model context protocol servers from Microsoft and Anthropic
- **Chrome and Edge Browsers**: Users targeted by fake NexShield ad-blocking extensions
- **Chainlit AI Framework**: Open source framework for AI chatbots with multiple vulnerabilities
- **Fortune 100 Finance Firms**: Large financial organizations targeted with PDFSider malware

## Attack Vectors and Techniques

- **Social Engineering**: Fake browser crash scenarios followed by malicious "fix" downloads through ClickFix attacks
- **Malicious Extensions**: Deployment of fake ad-blocking Chrome extensions that intentionally crash browsers
- **Supply Chain Attacks**: Weaponized Visual Studio Code projects containing backdoors and information stealers
- **Prompt Injection**: Indirect prompt injection through calendar invites to bypass AI assistant security controls
- **DLL Sideloading**: LinkedIn message-based phishing campaigns using DLL sideloading to deploy RAT malware
- **AI-Generated Malware**: VoidLink cloud malware framework developed with artificial intelligence assistance
- **Certificate Validation Bypass**: Exploitation of ACME validation logic flaws to access protected origin servers

## Threat Actor Activities

- **North Korean Groups**: Continuing the Contagious Interview campaign targeting developers with malicious VS Code projects and backdoors
- **Evelyn Stealer Operators**: Targeting software developers through weaponized VS Code extensions to steal credentials and cryptocurrency
- **ClickFix Campaign Actors**: Using NexShield fake ad-blocker extensions to crash browsers and deliver malware payloads
- **Ransomware Groups**: Deploying new PDFSider malware against Fortune 100 companies in the financial sector
- **Spam Operations**: Mass exploitation of Zendesk instances for large-scale spam campaigns (not tied to software vulnerabilities)
- **AI-Assisted Threat Actors**: Single operators using AI to develop sophisticated cloud-focused malware frameworks like VoidLink