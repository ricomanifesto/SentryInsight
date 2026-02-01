# Exploitation Report

Critical zero-day exploitation activity has been identified across multiple enterprise systems, with attackers actively targeting Ivanti Endpoint Manager Mobile (EPMM) infrastructure and leveraging sophisticated social engineering campaigns. The most urgent threats include two critical remote code execution vulnerabilities in Ivanti EPMM (CVE-2026-1281 and CVE-2026-1340) being actively exploited in the wild, alongside a high-severity unauthenticated RCE flaw in SmarterMail email software (CVE-2026-20331). Threat actors are also deploying advanced malware campaigns targeting Asian organizations through compromised IIS servers and conducting large-scale credential harvesting operations through malicious Chrome extensions and voice phishing attacks.

## Active Exploitation Details

### Ivanti EPMM Zero-Day Vulnerabilities
- **Description**: Two critical remote code execution vulnerabilities in Ivanti Endpoint Manager Mobile affecting enterprise mobile device management infrastructure
- **Impact**: Complete system compromise allowing attackers to execute arbitrary code and potentially gain control over managed mobile devices across organizations
- **Status**: Actively exploited in zero-day attacks; security updates have been released by Ivanti
- **CVE ID**: CVE-2026-1281, CVE-2026-1340

### SmarterMail Unauthenticated RCE Vulnerability
- **Description**: Critical unauthenticated remote code execution flaw in SmarterMail email software with a CVSS score of 9.3
- **Impact**: Attackers can execute arbitrary code without authentication, potentially compromising entire email infrastructure
- **Status**: Security patches released by SmarterTools; exploitation potential remains high
- **CVE ID**: CVE-2026-20331

### BadIIS SEO Malware Campaign
- **Description**: Sophisticated malware targeting Microsoft IIS servers across Asia, deployed by China-linked threat actors
- **Impact**: Server compromise leading to SEO manipulation, data theft, and potential lateral movement within networks
- **Status**: Active campaign identified between late 2025 and early 2026

### Malicious Chrome Extensions
- **Description**: Browser extensions designed to hijack affiliate links, steal user data, and collect OpenAI ChatGPT authentication tokens
- **Impact**: Financial fraud through affiliate link manipulation and unauthorized access to AI services
- **Status**: Active distribution through Chrome Web Store

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Critical vulnerabilities affecting mobile device management infrastructure
- **SmarterMail Email Software**: Unauthenticated RCE vulnerability with CVSS 9.3 score
- **Microsoft IIS Servers**: Targeted by BadIIS malware campaign across Asian organizations
- **Google Chrome Browser**: Extensions stealing authentication tokens and manipulating affiliate links
- **Android Devices**: Malware variants distributed through Hugging Face platform targeting financial applications
- **Wind and Solar Energy Facilities**: Over 30 renewable energy farms targeted in coordinated Polish cyber attacks
- **Single Sign-On (SSO) Systems**: Targeted through vishing attacks and company-branded phishing sites

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in Ivanti EPMM and SmarterMail systems
- **Voice Phishing (Vishing)**: Sophisticated social engineering campaigns targeting SSO credentials
- **Malicious Browser Extensions**: Chrome extensions with hidden malicious functionality for credential theft
- **SEO Poisoning**: BadIIS malware manipulating search engine optimization on compromised IIS servers
- **Mobile App Repository Abuse**: Hugging Face platform used to host thousands of Android malware variants
- **Company-Branded Phishing**: Legitimate-appearing websites designed to steal single sign-on credentials
- **Infrastructure Targeting**: Coordinated attacks against critical energy infrastructure in Poland

## Threat Actor Activities

- **China-Linked UAT-8099**: Deploying BadIIS SEO malware against Asian IIS servers in sophisticated campaign
- **ShinyHunters-Style Groups**: Conducting vishing attacks to steal MFA credentials and breach SaaS platforms
- **Iranian RedKitten Campaign**: Targeting human rights NGOs and activists with state-aligned cyber operations
- **Financial Crime Groups**: Distributing Android malware through legitimate AI platforms to target banking applications
- **Unknown Threat Actors**: Exploiting Ivanti EPMM zero-days and conducting coordinated attacks on Polish energy infrastructure