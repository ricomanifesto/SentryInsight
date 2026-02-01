# Exploitation Report

Recent security incidents reveal a concerning landscape of active exploitation targeting critical infrastructure and enterprise systems. Most notably, two zero-day vulnerabilities in Ivanti Endpoint Manager Mobile (EPMM) are being actively exploited in the wild, with one already added to CISA's Known Exploited Vulnerabilities catalog. Additionally, threat actors are leveraging sophisticated social engineering campaigns, including ShinyHunters' vishing attacks that abuse single sign-on credentials to breach SaaS platforms. Chinese state-aligned groups continue their aggressive campaigns, with UAT-8099 deploying BadIIS SEO malware against IIS servers across Asia, while RedKitten targets human rights organizations and activists. The exploitation activity extends to mobile platforms, where malicious Chrome extensions are stealing ChatGPT authentication tokens and Android malware campaigns are abusing legitimate platforms like Hugging Face to distribute thousands of credential-stealing variants.

## Active Exploitation Details

### Ivanti EPMM Zero-Day Vulnerabilities
- **Description**: Two critical remote code execution flaws in Ivanti Endpoint Manager Mobile that allow unauthorized access and control
- **Impact**: Attackers can achieve arbitrary code execution on affected systems, potentially compromising mobile device management infrastructure
- **Status**: Actively exploited in zero-day attacks; security updates have been released
- **CVE ID**: CVE-2026-1281 and CVE-2026-1340

### SmarterMail Unauthenticated RCE Flaw
- **Description**: Critical unauthenticated remote code execution vulnerability in SmarterMail email software with a CVSS score of 9.3
- **Impact**: Allows attackers to execute arbitrary code without authentication, potentially compromising email infrastructure
- **Status**: Patches available from SmarterTools

### Instagram Private Profile Photo Exposure
- **Description**: Vulnerability allowing unauthorized access to private Instagram account photos through exposed photo links
- **Impact**: Privacy breach exposing private content to unauthenticated visitors
- **Status**: Issue has been fixed by Meta, though initially closed as not applicable

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Critical zero-day vulnerabilities affecting mobile device management systems
- **SmarterMail Email Software**: Critical RCE vulnerability with CVSS 9.3 score
- **Google Chrome Extensions**: Malicious extensions targeting affiliate links and ChatGPT access tokens
- **IIS Servers in Asia**: Targeted by BadIIS SEO malware from Chinese threat actors
- **Android Devices**: Targeted by malware variants distributed through Hugging Face platform
- **Wind and Solar Farms**: Over 30 renewable energy facilities in Poland targeted in coordinated attacks
- **Instagram Platform**: Private profile photo exposure affecting user privacy
- **Windows 11 Systems**: Boot failures linked to failed December 2025 updates

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched vulnerabilities in Ivanti EPMM systems
- **Voice Phishing (Vishing)**: ShinyHunters using targeted voice calls combined with company-branded phishing sites
- **Single Sign-On (SSO) Abuse**: Stealing SSO credentials to gain unauthorized access to SaaS platforms
- **Malicious Browser Extensions**: Chrome extensions hijacking affiliate links and stealing authentication tokens
- **SEO Poisoning Malware**: BadIIS malware manipulating search engine optimization on compromised IIS servers
- **Mobile Malware Distribution**: Using legitimate platforms like Hugging Face to host thousands of Android malware variants
- **Social Engineering**: Fake cloud storage renewal campaigns targeting users worldwide
- **Platform Abuse**: Leveraging trusted platforms and services to distribute malicious content

## Threat Actor Activities

- **ShinyHunters**: Conducting sophisticated vishing attacks to steal MFA tokens and breach SaaS platforms through SSO credential theft
- **UAT-8099 (China-linked)**: Deploying BadIIS SEO malware against IIS servers across Asia in campaigns running from late 2025 to early 2026
- **RedKitten (Iran-linked)**: Targeting human rights NGOs and activists documenting recent events, using Farsi-speaking operators aligned with Iranian state interests
- **Polish Infrastructure Attackers**: Coordinated cyber attacks against more than 30 wind and photovoltaic farms, plus manufacturing sector targets
- **Android Malware Operators**: Distributing thousands of credential-stealing malware variants targeting financial and payment services through Hugging Face platform
- **Chrome Extension Threat Actors**: Developing malicious browser extensions to hijack affiliate programs and steal ChatGPT authentication tokens