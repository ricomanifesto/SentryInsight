# Exploitation Report

The current threat landscape reveals several critical zero-day exploitations and sophisticated attack campaigns targeting diverse systems and platforms. Most notably, Ivanti Endpoint Manager Mobile (EPMM) systems are under active zero-day exploitation with two critical remote code execution vulnerabilities being exploited in the wild. Simultaneously, threat actors are leveraging advanced social engineering techniques, particularly vishing attacks by groups like ShinyHunters to compromise single sign-on credentials and breach SaaS platforms. Additionally, state-sponsored activities from China-linked groups are targeting critical infrastructure including renewable energy facilities and Asian organizations with sophisticated malware campaigns.

## Active Exploitation Details

### Ivanti EPMM Zero-Day Vulnerabilities
- **Description**: Two critical remote code execution flaws in Ivanti Endpoint Manager Mobile that allow attackers to execute arbitrary code without authentication
- **Impact**: Complete system compromise, unauthorized access to mobile device management infrastructure, and potential lateral movement within enterprise networks
- **Status**: Actively exploited in zero-day attacks; security updates have been released
- **CVE ID**: CVE-2026-1281 and CVE-2026-1340

### SmarterMail Remote Code Execution Flaw
- **Description**: Critical unauthenticated remote code execution vulnerability in SmarterMail email software with a CVSS score of 9.3
- **Impact**: Arbitrary code execution on mail servers, potential compromise of email infrastructure and sensitive communications
- **Status**: Patched by SmarterTools; vulnerability details indicate critical severity requiring immediate attention

### Chrome Extensions Malicious Activity
- **Description**: Malicious Google Chrome extensions designed to hijack affiliate links, steal user data, and collect OpenAI ChatGPT authentication tokens
- **Impact**: Data theft, unauthorized access to ChatGPT accounts, financial fraud through affiliate link manipulation
- **Status**: Active campaign identified by researchers; extensions likely still in circulation

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: All versions affected by zero-day vulnerabilities requiring immediate patching
- **SmarterMail Email Software**: Critical vulnerability with unauthenticated RCE capabilities
- **Google Chrome**: Malicious extensions targeting users with data theft and authentication token collection
- **Windows IIS Servers**: Targeted by China-linked UAT-8099 group with BadIIS SEO malware, particularly in Asian regions
- **Wind and Solar Farms**: Over 30 renewable energy facilities in Poland targeted in coordinated cyber attacks
- **Instagram Private Accounts**: Evidence of photo links being exposed to unauthenticated visitors
- **SaaS Platforms**: Widespread targeting through SSO credential theft campaigns

## Attack Vectors and Techniques

- **Voice Phishing (Vishing)**: ShinyHunters group using targeted phone calls combined with branded phishing sites to steal SSO credentials
- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in Ivanti EPMM systems for immediate system compromise
- **Malicious Browser Extensions**: Chrome extensions abusing user trust to steal authentication tokens and hijack affiliate links
- **SEO Malware**: BadIIS malware targeting IIS servers to manipulate search engine optimization and maintain persistence
- **Social Engineering**: Company-branded phishing sites designed to steal multi-factor authentication credentials
- **Android Malware Distribution**: Using Hugging Face platform as repository for thousands of malware variants targeting financial applications

## Threat Actor Activities

- **ShinyHunters**: Conducting large-scale vishing campaigns to steal SSO credentials for SaaS platform breaches, expanding their tradecraft to include voice-based social engineering
- **UAT-8099 (China-linked)**: Targeting IIS servers across Asia with BadIIS SEO malware in campaigns spanning late 2025 to early 2026
- **RedKitten (Iran-linked)**: Conducting cyber espionage campaign targeting human rights NGOs and activists documenting recent events in Iran
- **Unknown APT Groups**: Coordinated attacks against Polish critical infrastructure including over 30 wind and photovoltaic farms plus manufacturing sector entities
- **Financial Cybercriminals**: Distributing Android malware through Hugging Face platform targeting credentials for popular financial and payment services