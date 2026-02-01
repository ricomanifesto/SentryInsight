# Exploitation Report

Critical zero-day exploitation activity has been identified targeting Ivanti Endpoint Manager Mobile systems, with two severe vulnerabilities being actively exploited in the wild. Additionally, significant threat actor campaigns are underway, including ShinyHunters conducting sophisticated SaaS platform breaches through voice phishing and SSO abuse, while Chinese APT groups are deploying advanced malware against Asian infrastructure targets. The security landscape is further complicated by widespread malicious Chrome extension campaigns stealing ChatGPT credentials and hijacking affiliate links, alongside coordinated attacks against critical infrastructure including wind and solar farms.

## Active Exploitation Details

### Ivanti EPMM Zero-Day Remote Code Execution Flaws
- **Description**: Two critical security vulnerabilities in Ivanti Endpoint Manager Mobile that enable remote code execution
- **Impact**: Attackers can achieve arbitrary code execution on affected systems, potentially compromising entire endpoint management infrastructure
- **Status**: Actively exploited in zero-day attacks; security updates have been released by Ivanti
- **CVE ID**: CVE-2026-1281 and CVE-2026-1340

### SmarterMail Unauthenticated Remote Code Execution
- **Description**: Critical security flaw in SmarterMail email software allowing unauthenticated remote code execution
- **Impact**: Attackers can execute arbitrary code without authentication, with a CVSS score of 9.3
- **Status**: Security patches have been released by SmarterTools

### BadIIS SEO Malware Campaign
- **Description**: China-linked UAT-8099 threat actor targeting IIS servers across Asia with specialized malware
- **Impact**: Compromise of web servers for SEO manipulation and potential data theft
- **Status**: Active campaign identified between late 2025 and early 2026

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Multiple versions affected by zero-day remote code execution vulnerabilities
- **SmarterMail Email Software**: Critical unauthenticated RCE vulnerability with CVSS 9.3 score
- **IIS Servers in Asia**: Targeted by China-linked UAT-8099 group with BadIIS malware
- **Google Chrome Browser**: Malicious extensions compromising user credentials and hijacking affiliate links
- **Wind and Solar Farms**: Over 30 renewable energy facilities in Poland targeted in coordinated attacks
- **SaaS Platforms**: Multiple cloud services compromised through SSO credential theft
- **Android Devices**: Thousands of malware variants distributed via Hugging Face platform
- **Instagram Platform**: Private account photo exposure vulnerability affecting user privacy

## Attack Vectors and Techniques

- **Voice Phishing (Vishing)**: ShinyHunters using targeted voice phishing to steal SSO credentials for SaaS platform access
- **Company-Branded Phishing Sites**: Creation of legitimate-looking phishing pages to harvest single sign-on credentials
- **Malicious Browser Extensions**: Chrome extensions designed to steal ChatGPT authentication tokens and hijack affiliate links
- **Zero-Day Exploitation**: Active exploitation of unpatched Ivanti EPMM vulnerabilities for remote code execution
- **IIS Server Compromise**: Targeting of Internet Information Services servers with specialized SEO manipulation malware
- **Cloud Storage Scams**: Large-scale email campaigns with fake renewal notifications to steal credentials
- **Malware Repository Abuse**: Using Hugging Face platform to host and distribute thousands of Android malware variants

## Threat Actor Activities

- **ShinyHunters**: Conducting sophisticated vishing attacks and SSO credential theft campaigns targeting SaaS platforms with extortion-themed activities
- **UAT-8099 (China-linked)**: Deploying BadIIS SEO malware against IIS servers across Asia in coordinated campaign
- **RedKitten (Iran-aligned)**: Farsi-speaking threat actor targeting human rights NGOs and activists documenting recent activities
- **Android Malware Operators**: Leveraging Hugging Face platform to distribute thousands of financial credential-stealing malware variants
- **Chrome Extension Attackers**: Deploying malicious browser extensions to steal ChatGPT tokens and manipulate affiliate marketing systems
- **Infrastructure Attackers**: Coordinated targeting of over 30 wind and solar farms in Poland along with manufacturing sector organizations