# Exploitation Report

Critical zero-day vulnerabilities are being actively exploited across multiple enterprise platforms, with Ivanti Endpoint Manager Mobile (EPMM) suffering from two critical remote code execution flaws being exploited in the wild. Additional concerning activity includes a China-linked threat actor campaign targeting IIS servers across Asia with specialized SEO malware, massive Android malware distribution through the Hugging Face platform, and record-breaking DDoS attacks reaching 31.4 Tbps. Organizations face increased risk from unpatched SmarterMail vulnerabilities, n8n automation platform flaws, and Chrome extension-based attacks targeting affiliate links and authentication tokens.

## Active Exploitation Details

### Ivanti EPMM Zero-Day Remote Code Execution Flaws
- **Description**: Two critical security vulnerabilities in Ivanti Endpoint Manager Mobile (EPMM) allowing remote code execution
- **Impact**: Complete system compromise and unauthorized access to mobile device management infrastructure
- **Status**: Actively exploited in zero-day attacks, security updates now available
- **CVE ID**: CVE-2026-1281 and CVE-2026-1340

### SmarterMail Unauthenticated Remote Code Execution
- **Description**: Critical unauthenticated remote code execution vulnerability in SmarterMail email software
- **Impact**: Arbitrary code execution without authentication, complete email server compromise
- **Status**: Patches available, critical vulnerability with CVSS 9.3 score

### n8n AI Automation Platform Remote Code Execution
- **Description**: Multiple critical remote code execution vulnerabilities in the popular AI automation platform
- **Impact**: Server hijacking, credential theft, and full system takeover
- **Status**: Second round of critical RCE bugs discovered, patches available

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Zero-day vulnerabilities actively exploited
- **SmarterMail Email Software**: Critical unauthenticated RCE flaw
- **n8n AI Automation Platform**: Multiple critical RCE vulnerabilities
- **Microsoft Windows IIS Servers**: Targeted by China-linked BadIIS SEO malware campaign
- **Google Chrome Extensions**: Malicious extensions hijacking affiliate links and stealing ChatGPT tokens
- **Android Devices**: Thousands of malware variants distributed via Hugging Face platform
- **Ollama AI Servers**: 175,000 publicly exposed servers across 130 countries
- **Match Group Dating Services**: Data breach affecting Tinder, Hinge, OkCupid, and Match
- **SonicWall Cloud Backup**: Exploited in ransomware attack against Marquis Software Solutions

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Targeting Ivanti EPMM vulnerabilities for immediate system compromise
- **Unauthenticated Remote Code Execution**: SmarterMail vulnerabilities allowing direct server compromise
- **SEO Poisoning Malware**: BadIIS malware targeting IIS servers for search engine manipulation
- **Malicious Browser Extensions**: Chrome extensions abusing affiliate links and stealing authentication tokens
- **AI Platform Abuse**: Hugging Face platform used to distribute thousands of Android malware variants
- **DDoS Record Breaking**: Aisuru botnet achieving 31.4 Tbps attack volume
- **Supply Chain Compromise**: Roblox game modifications containing infostealer malware
- **Cloud Infrastructure Attacks**: SonicWall cloud backup systems compromised for ransomware deployment

## Threat Actor Activities

- **UAT-8099 (China-linked)**: Targeting IIS servers across Asia with BadIIS SEO malware between late 2025 and early 2026
- **Chrome Extension Attackers**: Deploying malicious extensions to hijack affiliate revenue and steal OpenAI authentication credentials
- **Android Malware Campaign**: Using Hugging Face platform to distribute financial credential-stealing malware across thousands of variants
- **Aisuru/Kimwolf Botnet**: Conducting record-breaking DDoS attacks reaching 31.4 Tbps in December 2025
- **IPIDEA Proxy Network**: Operating large-scale residential proxy networks fueled by malware before Google disruption
- **Ransomware Groups**: Exploiting SonicWall cloud backup vulnerabilities to compromise financial services providers