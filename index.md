# Exploitation Report

Critical zero-day vulnerabilities are currently being actively exploited in the wild, with Ivanti Endpoint Manager Mobile (EPMM) suffering from two confirmed zero-day remote code execution flaws tracked as CVE-2026-1281 and CVE-2026-1340. Additionally, SolarWinds Web Help Desk has disclosed four critical vulnerabilities enabling unauthenticated remote code execution and authentication bypass, while SmarterMail addressed a critical unauthenticated RCE flaw with a CVSS score of 9.3. Chinese threat actors continue their aggressive campaigns, with UAT-8099 deploying BadIIS malware against IIS servers across Asia and multiple APT groups utilizing sophisticated malware against regional targets. The threat landscape is further complicated by large-scale infrastructure compromises, including the disruption of IPIDEA's massive residential proxy network used by cybercriminals and the discovery of 175,000 publicly exposed Ollama AI servers worldwide.

## Active Exploitation Details

### Ivanti EPMM Zero-Day Vulnerabilities
- **Description**: Two critical remote code execution vulnerabilities affecting Ivanti Endpoint Manager Mobile that have been exploited in zero-day attacks
- **Impact**: Attackers can achieve remote code execution on affected EPMM systems, potentially compromising mobile device management infrastructure
- **Status**: Actively exploited in the wild with security updates released by Ivanti
- **CVE ID**: CVE-2026-1281 and CVE-2026-1340

### SolarWinds Web Help Desk Critical Flaws
- **Description**: Four critical vulnerabilities in SolarWinds Web Help Desk including unauthenticated remote code execution and authentication bypass flaws
- **Impact**: Unauthenticated attackers can execute arbitrary code and bypass authentication mechanisms
- **Status**: Security updates released by SolarWinds to address the vulnerabilities
- **CVE ID**: Not specified in the articles

### SmarterMail Critical RCE Vulnerability
- **Description**: Critical unauthenticated remote code execution flaw in SmarterMail email software with CVSS score of 9.3
- **Impact**: Attackers can execute arbitrary code without authentication on affected email servers
- **Status**: Patched by SmarterTools along with additional security flaws
- **CVE ID**: Not fully specified in the articles (referenced as "CVE-...")

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Critical zero-day vulnerabilities enabling remote code execution
- **SolarWinds Web Help Desk**: Four critical flaws including RCE and authentication bypass capabilities
- **SmarterMail Email Software**: Critical unauthenticated RCE vulnerability with CVSS 9.3 score
- **Microsoft IIS Servers**: Targeted by China-linked UAT-8099 group with BadIIS SEO malware in Asia
- **Windows 11 Systems**: Boot failures linked to failed December 2025 update installations
- **Android Devices**: Thousands of malware variants distributed through Hugging Face platform targeting financial services
- **n8n AI Automation Platform**: Critical vulnerabilities that could compromise customer security
- **Ollama AI Servers**: 175,000 publicly exposed servers across 130 countries

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched Ivanti EPMM vulnerabilities before public disclosure
- **Unauthenticated Remote Code Execution**: Multiple products affected by RCE flaws requiring no authentication
- **Supply Chain Abuse**: Hugging Face platform misused to distribute thousands of Android malware variants
- **SEO Malware Deployment**: BadIIS malware targeting IIS servers for search engine optimization manipulation
- **Residential Proxy Networks**: IPIDEA network infrastructure used by threat actors for malicious activities
- **Authentication Bypass**: Critical flaws in SolarWinds Web Help Desk allowing unauthorized access
- **AI Platform Exploitation**: Semantic chaining jailbreak techniques targeting large language models like Gemini and Grok

## Threat Actor Activities

- **UAT-8099 (China-linked)**: Conducting campaigns against IIS servers in Asia using BadIIS SEO malware between late 2025 and early 2026
- **Chinese APT Groups**: Deploying sophisticated malware against various Asian organizations with high-end attack tools
- **TA584 Initial Access Broker**: Switching to Tsundere Bot alongside XWorm remote access trojan for ransomware preparation attacks
- **Aisuru/Kimwolf Botnet Operators**: Launched record-breaking 31.4 Tbps DDoS attack in December 2025 with 200 million requests per second
- **Android Malware Campaign**: Operators using Hugging Face to distribute credential-stealing malware targeting financial and payment services
- **IPIDEA Network Operators**: Maintained one of the world's largest residential proxy networks before Google-led disruption efforts