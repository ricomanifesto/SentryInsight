# Exploitation Report

Critical zero-day vulnerabilities are currently being exploited in the wild, most notably affecting Ivanti Endpoint Manager Mobile (EPMM) systems with two remote code execution flaws (CVE-2026-1281 and CVE-2026-1340) that have been actively targeted by threat actors. Additionally, SmarterMail email software faces a severe unauthenticated remote code execution vulnerability with a CVSS score of 9.3. Chinese APT groups, particularly UAT-8099, are conducting sophisticated campaigns targeting IIS servers across Asia using the BadIIS SEO malware, while malicious Chrome extensions are stealing ChatGPT authentication tokens and hijacking affiliate links. The threat landscape is further complicated by massive DDoS attacks from the Aisuru botnet reaching record-breaking 31.4 Tbps volumes, and widespread Android malware distribution through the Hugging Face platform.

## Active Exploitation Details

### Ivanti EPMM Zero-Day Remote Code Execution Vulnerabilities
- **Description**: Two critical security flaws in Ivanti Endpoint Manager Mobile that allow remote code execution without authentication
- **Impact**: Complete system compromise, unauthorized access to enterprise mobile device management infrastructure
- **Status**: Actively exploited in zero-day attacks; security updates have been released
- **CVE ID**: CVE-2026-1281 and CVE-2026-1340

### SmarterMail Unauthenticated RCE Vulnerability
- **Description**: Critical security flaw in SmarterMail email software allowing arbitrary code execution without authentication
- **Impact**: Complete server compromise, email system takeover, potential data exfiltration
- **Status**: Recently patched; CVSS score of 9.3 indicating critical severity

### BadIIS SEO Malware Campaign
- **Description**: Sophisticated malware targeting IIS servers in Asia for SEO manipulation and system compromise
- **Impact**: Website defacement, search engine ranking manipulation, potential backdoor installation
- **Status**: Active campaign attributed to China-linked UAT-8099 threat group

### n8n AI Platform Critical Vulnerabilities
- **Description**: Second round of critical remote code execution vulnerabilities in the popular AI automation platform
- **Impact**: Server hijacking, credential theft, complete system takeover in corporate environments
- **Status**: Recently disclosed; patches available

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Enterprise mobile device management systems vulnerable to zero-day RCE attacks
- **SmarterMail Email Software**: Email servers running vulnerable versions susceptible to unauthenticated RCE
- **Microsoft Internet Information Services (IIS)**: Web servers in Asia targeted by BadIIS malware campaign
- **n8n AI Automation Platform**: Corporate deployments at risk of compromise through RCE vulnerabilities
- **Google Chrome Extensions**: Browser users affected by malicious extensions stealing authentication tokens
- **Android Devices**: Mobile platforms targeted through malware distributed via Hugging Face repository
- **Hugging Face Platform**: AI model repository abused to host thousands of Android malware variants
- **Match Group Services**: Dating platforms including Tinder, Match.com, OkCupid, and Hinge affected by data breach

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct targeting of unpatched Ivanti EPMM systems through known vulnerabilities
- **Unauthenticated Remote Code Execution**: SmarterMail attacks requiring no prior authentication or credentials
- **Malicious Browser Extensions**: Chrome extensions hijacking affiliate links and stealing ChatGPT authentication tokens
- **Platform Abuse**: Legitimate Hugging Face repository used to distribute thousands of Android malware variants
- **SEO Malware Injection**: IIS servers compromised to manipulate search engine rankings through BadIIS malware
- **DDoS Amplification**: Record-breaking 31.4 Tbps attacks using Aisuru/Kimwolf botnet infrastructure
- **Game Modification Trojans**: Roblox mods containing infostealer malware targeting corporate environments
- **AI Platform Exploitation**: Targeting of n8n automation systems for credential theft and server compromise

## Threat Actor Activities

- **UAT-8099 (China-linked APT)**: Conducting sophisticated campaigns against Asian IIS servers using BadIIS SEO malware between late 2025 and early 2026
- **Unknown Threat Actors**: Actively exploiting Ivanti EPMM zero-day vulnerabilities in targeted attacks
- **Cybercriminal Groups**: Leveraging Hugging Face platform to distribute thousands of Android malware variants targeting financial and payment services
- **Aisuru Botnet Operators**: Launching record-breaking DDoS attacks reaching 31.4 Tbps and 200 million requests per second
- **Chrome Extension Attackers**: Deploying malicious browser extensions to steal ChatGPT tokens and hijack affiliate marketing revenue
- **IPIDEA Proxy Network**: Large-scale residential proxy network disrupted by Google after being used extensively by threat actors for malicious activities