# Exploitation Report

Current exploitation activity reveals a concerning landscape of active zero-day attacks, sophisticated threat campaigns, and critical vulnerabilities being exploited in the wild. Most notably, Ivanti Endpoint Manager Mobile (EPMM) has been targeted with two zero-day remote code execution vulnerabilities (CVE-2026-1281 and CVE-2026-1340) that attackers are actively exploiting. Additionally, SmarterMail email software contains a critical unauthenticated RCE flaw with a CVSS score of 9.3, while Chinese APT groups are deploying advanced malware campaigns targeting Asian organizations. The threat landscape is further complicated by sophisticated social engineering attacks from groups like ShinyHunters, who are leveraging voice phishing and SSO credential theft to breach cloud platforms, and widespread abuse of legitimate platforms like Hugging Face for malware distribution.

## Active Exploitation Details

### Ivanti EPMM Zero-Day RCE Vulnerabilities
- **Description**: Two critical remote code execution flaws in Ivanti Endpoint Manager Mobile that allow attackers to execute arbitrary code on vulnerable systems
- **Impact**: Complete system compromise, unauthorized access to managed mobile devices, potential lateral movement within enterprise networks
- **Status**: Actively exploited in zero-day attacks; security updates have been released by Ivanti
- **CVE ID**: CVE-2026-1281 and CVE-2026-1340

### SmarterMail Unauthenticated RCE Vulnerability
- **Description**: Critical security flaw in SmarterMail email software allowing unauthenticated remote code execution
- **Impact**: Arbitrary code execution without authentication, complete email server compromise
- **Status**: Patched by SmarterTools; vulnerability carried CVSS 9.3 score indicating critical severity
- **CVE ID**: CVE-2026-1334

### Instagram Private Profile Photo Exposure
- **Description**: Vulnerability allowing unauthenticated visitors to access photo links from private Instagram accounts
- **Impact**: Privacy breach exposing private user content to unauthorized parties
- **Status**: Fixed by Meta, though report was closed as "not applicable" by the company

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Mobile device management platform experiencing active zero-day exploitation
- **SmarterMail Email Software**: Email server platform with critical RCE vulnerability
- **Instagram Platform**: Social media platform with privacy exposure vulnerability affecting private accounts
- **IIS Servers in Asia**: Microsoft web servers targeted by China-linked UAT-8099 group with BadIIS SEO malware
- **Wind and Solar Farms**: 30+ renewable energy facilities in Poland targeted in coordinated cyber attacks
- **Google Chrome Extensions**: Browser extensions abusing affiliate links and stealing ChatGPT authentication tokens
- **n8n AI Automation Platform**: Workflow automation tool with multiple critical RCE vulnerabilities
- **Ollama AI Servers**: 175,000 publicly exposed AI deployment servers across 130 countries

## Attack Vectors and Techniques

- **Voice Phishing (Vishing)**: ShinyHunters group using targeted phone-based social engineering to steal SSO credentials
- **Company-Branded Phishing Sites**: Sophisticated phishing infrastructure mimicking legitimate company login portals
- **Zero-Day Exploitation**: Active exploitation of unpatched vulnerabilities in enterprise mobile management systems
- **Malware Repository Abuse**: Using Hugging Face platform to distribute thousands of Android malware variants targeting financial services
- **Chrome Extension Hijacking**: Malicious browser extensions intercepting affiliate links and stealing authentication tokens
- **SEO Poisoning**: BadIIS malware deployment for search engine optimization manipulation
- **Residential Proxy Network Abuse**: IPIDEA proxy networks compromised through malware infections for threat actor operations

## Threat Actor Activities

- **ShinyHunters**: Financially motivated group conducting SaaS data theft through vishing attacks and SSO credential compromise targeting cloud platforms
- **RedKitten (Iran-linked)**: Farsi-speaking threat actor targeting human rights NGOs and activists documenting recent events
- **UAT-8099 (China-linked)**: Advanced persistent threat group deploying BadIIS SEO malware against IIS servers across Asia
- **Unknown Polish Campaign Actors**: Coordinated attacks against renewable energy infrastructure including wind and photovoltaic farms
- **Android Malware Operators**: Campaign utilizing Hugging Face platform for credential harvesting targeting financial and payment services
- **Chrome Extension Threat Actors**: Cybercriminals deploying malicious browser extensions for affiliate fraud and authentication token theft
- **IPIDEA Proxy Network Operators**: Large-scale residential proxy operation disrupted by Google, used extensively by various threat actors for malicious activities