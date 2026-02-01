# Exploitation Report

Recent security incidents reveal a significant increase in zero-day exploitation and sophisticated attack campaigns targeting critical infrastructure and enterprise systems. Two critical zero-day vulnerabilities in Ivanti Endpoint Manager Mobile (EPMM) are being actively exploited in the wild, with CVE-2026-1340 added to CISA's Known Exploited Vulnerabilities Catalog. Chinese state-aligned threat actors continue their aggressive campaigns, with UAT-8099 deploying BadIIS SEO malware against IIS servers across Asia, while the RedKitten campaign targets human rights organizations. Additionally, SmarterMail has patched a critical unauthenticated remote code execution vulnerability, and malicious Chrome extensions are being used to steal authentication tokens and hijack affiliate links.

## Active Exploitation Details

### Ivanti EPMM Zero-Day Remote Code Execution Vulnerabilities
- **Description**: Two critical security flaws in Ivanti Endpoint Manager Mobile that enable remote code execution
- **Impact**: Attackers can execute arbitrary code remotely on affected EPMM systems without authentication
- **Status**: Currently being exploited in zero-day attacks; security updates have been released by Ivanti
- **CVE ID**: CVE-2026-1281, CVE-2026-1340

### SmarterMail Unauthenticated Remote Code Execution Vulnerability
- **Description**: Critical security flaw in SmarterMail email software allowing unauthenticated remote code execution
- **Impact**: Attackers can execute arbitrary code without authentication, potentially compromising email infrastructure
- **Status**: Fixed by SmarterTools; CVSS score of 9.3 indicates critical severity
- **CVE ID**: CVE information mentioned but specific number not provided in source

### BadIIS SEO Malware Campaign
- **Description**: China-linked UAT-8099 threat actor targeting IIS servers in Asia with specialized SEO manipulation malware
- **Impact**: Compromise of web server infrastructure and potential SEO poisoning attacks
- **Status**: Active campaign discovered between late 2025 and early 2026

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Multiple versions affected by zero-day remote code execution vulnerabilities
- **SmarterMail Email Software**: Critical unauthenticated RCE vulnerability with CVSS 9.3 score
- **Microsoft IIS Servers**: Targeted by BadIIS SEO malware in Asia-Pacific region
- **Google Chrome Extensions**: Malicious extensions targeting affiliate links and ChatGPT authentication
- **Android Devices**: Thousands of malware variants distributed through Hugging Face platform
- **Instagram Private Accounts**: Photo links exposed to unauthenticated visitors (subsequently fixed)
- **Wind and Solar Energy Farms**: Over 30 renewable energy facilities in Poland targeted in coordinated attacks

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched Ivanti EPMM vulnerabilities for remote code execution
- **Voice Phishing (Vishing)**: ShinyHunters using targeted voice calls to steal SSO credentials and bypass MFA
- **Company-Branded Phishing Sites**: Sophisticated phishing infrastructure mimicking legitimate SSO login pages
- **Malware Distribution via AI Platforms**: Abuse of Hugging Face repository to host thousands of Android malware variants
- **Chrome Extension Abuse**: Malicious browser extensions hijacking affiliate links and stealing authentication tokens
- **SEO Manipulation**: BadIIS malware specifically designed for search engine optimization poisoning
- **Cloud Storage Subscription Scams**: Large-scale email campaigns targeting users with fake renewal notifications

## Threat Actor Activities

- **UAT-8099 (China-linked)**: Conducting campaign against IIS servers in Asia using BadIIS SEO malware between late 2025 and early 2026
- **RedKitten (Iran-aligned)**: Targeting human rights NGOs and activists documenting recent humanitarian crises with Farsi-speaking operations
- **ShinyHunters-Style Groups**: Escalating vishing attacks and SaaS platform breaches to steal multi-factor authentication credentials
- **Unknown Chrome Extension Attackers**: Deploying malicious browser extensions for affiliate link hijacking and ChatGPT token theft
- **Polish Energy Sector Attackers**: Coordinated cyber attacks against over 30 wind and photovoltaic farms plus manufacturing sector targets
- **Android Malware Distributors**: Leveraging Hugging Face platform to distribute thousands of financial credential-stealing malware variants