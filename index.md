# Exploitation Report

Critical zero-day vulnerabilities are currently being actively exploited across multiple enterprise platforms, posing significant risks to organizations worldwide. Most notably, Ivanti Endpoint Manager Mobile (EPMM) systems are under active attack through two zero-day remote code execution flaws (CVE-2026-1281 and CVE-2026-1340), while SolarWinds Web Help Desk faces four critical vulnerabilities including unauthenticated RCE and authentication bypass issues. Additional high-severity threats include a critical unauthenticated RCE vulnerability in SmarterMail email software and multiple security flaws in the n8n AI automation platform. Meanwhile, threat actors are leveraging malicious Chrome extensions to steal credentials and ChatGPT tokens, while Chinese APT groups continue sophisticated campaigns targeting Asian organizations with advanced malware.

## Active Exploitation Details

### Ivanti EPMM Zero-Day Vulnerabilities
- **Description**: Two critical remote code execution vulnerabilities in Ivanti Endpoint Manager Mobile that allow attackers to execute arbitrary code on affected systems
- **Impact**: Complete system compromise, unauthorized access to mobile device management infrastructure, potential lateral movement within enterprise networks
- **Status**: Actively exploited in zero-day attacks, security updates released by Ivanti
- **CVE ID**: CVE-2026-1281 and CVE-2026-1340

### SolarWinds Web Help Desk Critical Flaws
- **Description**: Four critical security vulnerabilities including unauthenticated remote code execution and authentication bypass mechanisms
- **Impact**: Complete system takeover without authentication, unauthorized administrative access, potential data theft and system manipulation
- **Status**: Security updates released to address all four vulnerabilities

### SmarterMail Unauthenticated RCE Vulnerability
- **Description**: Critical security flaw in SmarterMail email software allowing arbitrary code execution without authentication
- **Impact**: Complete email server compromise, unauthorized access to email communications, potential data exfiltration
- **Status**: Patches available from SmarterTools with CVSS score of 9.3

### Malicious Chrome Extensions Campaign
- **Description**: Sophisticated browser extensions designed to hijack affiliate links, steal user data, and collect OpenAI ChatGPT authentication tokens
- **Impact**: Credential theft, unauthorized access to ChatGPT accounts, financial fraud through affiliate link manipulation
- **Status**: Ongoing campaign targeting Chrome browser users

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Enterprise mobile device management systems vulnerable to zero-day attacks
- **SolarWinds Web Help Desk**: IT service management platforms facing critical authentication and RCE vulnerabilities
- **SmarterMail Email Software**: Email servers at risk of unauthenticated remote code execution
- **Google Chrome Browser**: Users exposed through malicious extensions stealing credentials and tokens
- **n8n AI Automation Platform**: Workflow automation servers vulnerable to credential theft and server hijacking
- **Microsoft IIS Servers**: Asian organizations targeted by BadIIS SEO malware campaigns
- **Android Devices**: Thousands of malware variants distributed through Hugging Face platform
- **Ollama AI Servers**: 175,000 publicly exposed servers across 130 countries at risk

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct targeting of unpatched Ivanti EPMM systems through remote code execution vulnerabilities
- **Unauthenticated Remote Code Execution**: Attacks on SolarWinds and SmarterMail systems without requiring valid credentials
- **Malicious Browser Extensions**: Social engineering to install credential-stealing Chrome extensions
- **SEO Malware Injection**: BadIIS malware targeting IIS servers for search engine optimization manipulation
- **AI Platform Abuse**: Hugging Face repository exploitation to distribute Android malware variants
- **Residential Proxy Networks**: IPIDEA network leveraging malware-infected devices for proxy services
- **Supply Chain Targeting**: Roblox game modifications used as vectors for infostealer malware

## Threat Actor Activities

- **UAT-8099 (China-linked)**: Sophisticated campaign targeting Asian IIS servers with BadIIS SEO malware between late 2025 and early 2026
- **Chinese APT Groups**: Deployment of high-end malware against various Asian organizations using advanced persistent threat techniques
- **Credential Theft Operations**: Large-scale campaigns using malicious Chrome extensions to harvest authentication tokens and financial data
- **Android Malware Distributors**: Organized campaigns leveraging AI platforms to spread thousands of malware variants targeting financial services
- **IPIDEA Network Operators**: Large-scale residential proxy network facilitating cybercriminal activities before Google disruption
- **Aisuru/Kimwolf Botnet**: Record-breaking DDoS attacks reaching 31.4 Tbps and 200 million requests per second