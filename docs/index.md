# Exploitation Report

Critical zero-day vulnerabilities in Ivanti Endpoint Manager Mobile (EPMM) are actively being exploited in the wild, posing immediate risks to enterprise mobile device management systems. Two zero-day remote code execution flaws (CVE-2026-1281 and CVE-2026-1340) have been confirmed as actively exploited, with one vulnerability earning inclusion in CISA's Known Exploited Vulnerabilities catalog. Additional critical security concerns include a newly patched unauthenticated remote code execution vulnerability in SmarterMail with a CVSS score of 9.3, Chrome extensions conducting credential theft operations, and coordinated infrastructure attacks by state-sponsored threat actors targeting renewable energy facilities and business environments across multiple regions.

## Active Exploitation Details

### Ivanti EPMM Zero-Day Vulnerabilities
- **Description**: Two critical remote code execution vulnerabilities in Ivanti Endpoint Manager Mobile (EPMM) software affecting enterprise mobile device management systems
- **Impact**: Attackers can achieve arbitrary code execution on vulnerable EPMM systems, potentially compromising entire mobile device management infrastructure
- **Status**: Actively exploited in zero-day attacks; security updates have been released by Ivanti
- **CVE ID**: CVE-2026-1281, CVE-2026-1340

### SmarterMail Unauthenticated RCE Vulnerability
- **Description**: Critical unauthenticated remote code execution flaw in SmarterMail email software that allows attackers to execute arbitrary code without authentication
- **Impact**: Complete compromise of email servers, potential access to sensitive communications and user credentials
- **Status**: Patched by SmarterTools; vulnerability carried a CVSS score of 9.3
- **CVE ID**: Not specified in source material

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Enterprise mobile device management systems vulnerable to zero-day RCE attacks
- **SmarterMail Email Software**: Email servers running vulnerable versions prior to security updates
- **Google Chrome Extensions**: Browser environments with malicious extensions capable of affiliate link hijacking and ChatGPT token theft
- **IIS Servers in Asia**: Microsoft Internet Information Services servers targeted by China-linked UAT-8099 group with BadIIS SEO malware
- **Wind and Solar Farms**: Over 30 renewable energy facilities in Poland targeted in coordinated cyber attacks
- **SaaS Platforms**: Cloud-based software-as-a-service platforms targeted through vishing attacks and multi-factor authentication bypass techniques

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in enterprise mobile management systems before patches were available
- **Vishing (Voice Phishing)**: Social engineering attacks combining phone calls with technical manipulation to steal multi-factor authentication credentials
- **Malicious Browser Extensions**: Chrome extensions designed to hijack affiliate links, steal user data, and collect OpenAI ChatGPT authentication tokens
- **SEO Malware Deployment**: BadIIS malware installed on compromised IIS servers to manipulate search engine optimization and maintain persistent access
- **Coordinated Infrastructure Attacks**: Synchronized cyber operations targeting critical energy infrastructure across multiple facilities simultaneously

## Threat Actor Activities

- **Iran-Linked RedKitten**: Farsi-speaking threat actor aligned with Iranian state interests conducting campaigns against human rights NGOs and activists documenting recent humanitarian issues
- **ShinyHunters-Style Operations**: Financially motivated hacking groups using advanced vishing techniques to breach SaaS platforms and steal sensitive data through MFA bypass methods
- **China-Linked UAT-8099**: Chinese state-sponsored threat group conducting campaigns between late 2025 and early 2026, targeting IIS servers across Asia with specialized BadIIS SEO malware
- **Polish Infrastructure Attackers**: Unidentified threat actors behind coordinated attacks on over 30 wind and photovoltaic farms, plus manufacturing sector targets in Poland during December operations