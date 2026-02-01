# Exploitation Report

Critical exploitation activity is currently focused on zero-day vulnerabilities in enterprise infrastructure and sophisticated social engineering campaigns targeting cloud services. Two zero-day remote code execution vulnerabilities in Ivanti Endpoint Manager Mobile (EPMM) are being actively exploited in the wild, with CVE-2026-1281 and CVE-2026-1340 allowing attackers to achieve complete system compromise. Meanwhile, the ShinyHunters threat group has escalated their SaaS platform attacks through advanced voice phishing campaigns that bypass multi-factor authentication, targeting organizations across multiple industries. Chinese state-aligned threat actors continue coordinated campaigns, including UAT-8099's targeting of IIS servers across Asia and RedKitten's focused attacks on human rights organizations and activists.

## Active Exploitation Details

### Ivanti EPMM Zero-Day Vulnerabilities
- **Description**: Two critical remote code execution flaws in Ivanti Endpoint Manager Mobile allowing unauthenticated attackers to execute arbitrary code on vulnerable systems
- **Impact**: Complete system compromise, unauthorized access to enterprise mobile device management infrastructure, potential lateral movement within corporate networks
- **Status**: Actively exploited in zero-day attacks, security updates have been released by Ivanti
- **CVE ID**: CVE-2026-1281, CVE-2026-1340

### SmarterMail Unauthenticated RCE Vulnerability
- **Description**: Critical unauthenticated remote code execution flaw in SmarterMail email software with a CVSS score of 9.3
- **Impact**: Arbitrary code execution on mail servers, potential compromise of email infrastructure and sensitive communications
- **Status**: Patches have been released by SmarterTools to address the vulnerability

### Instagram Private Profile Photo Exposure
- **Description**: Vulnerability allowing unauthenticated visitors to access photo links from private Instagram accounts
- **Impact**: Unauthorized access to private user content, privacy violations
- **Status**: Issue has been fixed by Meta, but the company closed the security report as not applicable

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Critical zero-day vulnerabilities affecting mobile device management systems
- **SmarterMail Email Software**: Critical RCE vulnerability requiring immediate patching
- **Microsoft IIS Servers**: Targeted by BadIIS SEO malware in coordinated Chinese campaigns across Asia
- **Google Chrome Extensions**: Malicious extensions stealing ChatGPT tokens and hijacking affiliate links
- **n8n AI Automation Platform**: Multiple critical RCE vulnerabilities exposing corporate automation workflows
- **Android Mobile Devices**: Thousands of malware variants distributed through compromised Hugging Face platform
- **Cloud Storage Services**: Target of large-scale subscription scam campaigns worldwide
- **Wind and Solar Energy Facilities**: Over 30 renewable energy farms targeted in coordinated cyber attacks in Poland

## Attack Vectors and Techniques

- **Voice Phishing (Vishing)**: ShinyHunters using targeted phone calls combined with company-branded phishing sites to steal SSO credentials and bypass MFA
- **Zero-Day Exploitation**: Active exploitation of unpatched Ivanti EPMM vulnerabilities for initial access and system compromise
- **Malware Distribution**: BadIIS SEO malware deployment on compromised IIS servers for search engine manipulation
- **Browser Extension Abuse**: Malicious Chrome extensions collecting authentication tokens and manipulating affiliate links
- **Platform Abuse**: Hugging Face repository used to host thousands of Android malware variants targeting financial services
- **Email-Based Scams**: Large-scale cloud storage subscription scam campaigns using fake renewal notifications
- **Proxy Network Exploitation**: IPIDEA residential proxy networks fueled by malware for anonymizing malicious traffic

## Threat Actor Activities

- **ShinyHunters**: Conducting sophisticated vishing campaigns targeting SaaS platforms, stealing SSO credentials through company-branded phishing sites and voice calls to bypass multi-factor authentication
- **UAT-8099 (China-linked)**: Active campaign between late 2025 and early 2026 targeting IIS servers across Asia with BadIIS SEO malware for search engine manipulation and persistent access
- **RedKitten (Iran-linked)**: Farsi-speaking threat actor conducting targeted campaigns against human rights NGOs and activists documenting recent human rights violations
- **Unknown Threat Actors**: Coordinated attacks on over 30 wind and photovoltaic farms in Poland, plus manufacturing sector and public administration targets
- **Financial Crime Groups**: Operating large-scale Android malware campaigns through Hugging Face platform, targeting banking and payment service credentials