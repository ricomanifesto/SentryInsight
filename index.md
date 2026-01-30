# Exploitation Report

Current exploitation activity reveals several critical zero-day vulnerabilities and ongoing campaigns targeting enterprise systems. Two critical zero-day flaws in Ivanti Endpoint Manager Mobile (CVE-2026-1281 and CVE-2026-1340) are being actively exploited in the wild, allowing remote code execution on enterprise mobile management systems. Additionally, a critical unauthenticated remote code execution vulnerability in SmarterMail email software poses immediate risks to organizations. Chinese threat actors continue aggressive campaigns against Asian organizations using sophisticated malware, while malicious browser extensions and AI platform abuse present emerging attack vectors targeting both individual users and enterprise environments.

## Active Exploitation Details

### Ivanti EPMM Zero-Day Vulnerabilities
- **Description**: Two critical remote code execution vulnerabilities in Ivanti Endpoint Manager Mobile that allow attackers to compromise mobile device management systems
- **Impact**: Complete system compromise, unauthorized access to managed mobile devices, and potential lateral movement within enterprise networks
- **Status**: Actively exploited in zero-day attacks, security updates have been released
- **CVE ID**: CVE-2026-1281 and CVE-2026-1340

### SmarterMail Unauthenticated RCE Flaw
- **Description**: Critical unauthenticated remote code execution vulnerability in SmarterMail email software with a CVSS score of 9.3
- **Impact**: Arbitrary code execution without authentication, complete system compromise
- **Status**: Security patches released by SmarterTools

### n8n AI Automation Platform Vulnerabilities
- **Description**: Second round of critical remote code execution bugs in the popular AI automation platform n8n
- **Impact**: Server hijacking, credential theft, and full system takeover in corporate environments
- **Status**: Recently disclosed, increases corporate risk exposure

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Enterprise mobile device management systems vulnerable to zero-day attacks
- **SmarterMail Email Software**: Email servers running vulnerable versions face unauthenticated RCE attacks
- **n8n AI Automation Platform**: Corporate deployments at risk of server compromise and credential theft
- **Google Chrome Extensions**: Browser extensions abusing affiliate links and stealing ChatGPT authentication tokens
- **Microsoft IIS Servers**: Asian IIS servers targeted by China-linked UAT-8099 group with BadIIS SEO malware
- **Android Devices**: Thousands of malware variants distributed through Hugging Face platform targeting financial services
- **Ollama AI Servers**: 175,000 publicly exposed AI servers across 130 countries vulnerable to unauthorized access

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in enterprise mobile management systems
- **Unauthenticated Remote Code Execution**: Attackers gaining system access without valid credentials through email software vulnerabilities
- **Malicious Browser Extensions**: Chrome extensions hijacking affiliate links and stealing authentication tokens for AI services
- **SEO Malware Deployment**: BadIIS malware targeting IIS servers to manipulate search engine optimization
- **AI Platform Abuse**: Using Hugging Face as a distribution platform for Android malware variants
- **Residential Proxy Networks**: IPIDEA proxy network disrupted after being used by threat actors for malicious activities
- **Social Engineering via Gaming**: Roblox mods containing infostealer malware targeting home users to compromise corporate networks

## Threat Actor Activities

- **UAT-8099 (China-linked)**: Targeting Asian IIS servers with BadIIS SEO malware in campaigns spanning late 2025 to early 2026
- **Chinese APT Groups**: Deploying advanced malware against various Asian organizations using sophisticated cyber weapons
- **Android Malware Operators**: Distributing thousands of malware variants through Hugging Face platform targeting financial and payment services
- **Aisuru/Kimwolf Botnet**: Launched record-breaking 31.4 Tbps DDoS attack in December 2025, generating 200 million requests per second
- **Chrome Extension Attackers**: Developing malicious browser extensions to steal ChatGPT tokens and manipulate affiliate marketing
- **Corporate Espionage**: Ex-Google engineer convicted of stealing 2,000 AI trade secrets for China-based startup operations