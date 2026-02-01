# Exploitation Report

Critical zero-day attacks are actively targeting enterprise infrastructure, with threat actors exploiting vulnerabilities in Ivanti Endpoint Manager Mobile (EPMM) and conducting sophisticated campaigns against cloud platforms and critical infrastructure. The most significant developments include two zero-day remote code execution flaws in Ivanti EPMM that have been actively exploited in the wild, along with coordinated attacks against renewable energy infrastructure in Poland. Additionally, multiple threat groups are leveraging advanced social engineering techniques to compromise single sign-on systems and steal multi-factor authentication credentials, while malicious actors are abusing legitimate platforms to distribute malware and conduct large-scale cybercriminal operations.

## Active Exploitation Details

### Ivanti EPMM Zero-Day Remote Code Execution Flaws
- **Description**: Two critical vulnerabilities in Ivanti Endpoint Manager Mobile allowing unauthenticated remote code execution
- **Impact**: Complete system compromise with the ability to execute arbitrary code without authentication
- **Status**: Actively exploited in zero-day attacks; security updates have been released by Ivanti
- **CVE ID**: CVE-2026-1281 and CVE-2026-1340

### SmarterMail Critical Unauthenticated RCE Vulnerability
- **Description**: Critical security flaw in SmarterMail email software allowing unauthenticated remote code execution
- **Impact**: Arbitrary code execution without authentication with a CVSS score of 9.3
- **Status**: Patched by SmarterTools with security updates released

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Critical vulnerabilities allowing remote code execution, actively exploited in zero-day attacks
- **SmarterMail Email Software**: Critical unauthenticated RCE vulnerability with CVSS 9.3 score
- **Windows 11 Systems**: Boot failures linked to failed December 2025 security updates
- **Microsoft 365/Outlook**: Encrypted email access issues affecting classic Outlook users
- **Polish Wind and Solar Farms**: Over 30 renewable energy facilities targeted in coordinated cyber attacks
- **Google Chrome Extensions**: Malicious extensions hijacking affiliate links and stealing ChatGPT authentication tokens
- **IIS Servers in Asia**: Targeted by China-linked threat actors with BadIIS SEO malware
- **Android Devices**: Thousands of malware variants distributed through Hugging Face platform
- **Instagram Private Profiles**: Photo links exposed to unauthenticated visitors

## Attack Vectors and Techniques

- **Voice Phishing (Vishing)**: ShinyHunters conducting targeted voice calls to steal SSO credentials and bypass MFA
- **Company-Branded Phishing Sites**: Fake websites mimicking legitimate company portals to harvest single sign-on credentials
- **Platform Abuse**: Exploitation of legitimate platforms like Hugging Face for malware distribution
- **Social Engineering**: Sophisticated campaigns targeting employees to gain initial access to cloud environments
- **SEO Poisoning**: BadIIS malware manipulating search engine optimization on compromised IIS servers
- **Affiliate Link Hijacking**: Chrome extensions redirecting users' clicks to attacker-controlled affiliate programs
- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in enterprise mobile management systems

## Threat Actor Activities

- **ShinyHunters**: Conducting extensive SaaS data-theft attacks using vishing techniques and SSO credential theft to breach cloud platforms
- **UAT-8099 (China-linked)**: Targeting IIS servers across Asia with BadIIS SEO malware in campaigns spanning late 2025 to early 2026
- **RedKitten (Iran-linked)**: Targeting human rights NGOs and activists documenting recent human rights violations
- **Polish Infrastructure Attackers**: Coordinated cyber attacks against 30+ wind and photovoltaic farms plus manufacturing sector targets
- **Android Malware Operators**: Large-scale campaign distributing thousands of APK payload variants through Hugging Face to collect financial service credentials
- **Chrome Extension Threat Actors**: Deploying malicious browser extensions to hijack affiliate revenue and steal ChatGPT access tokens