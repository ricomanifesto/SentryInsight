# Exploitation Report

The cybersecurity landscape is currently experiencing significant exploitation activity across multiple fronts. Microsoft addressed three zero-day vulnerabilities in its January 2026 Patch Tuesday, with one being actively exploited in the wild. A critical AI platform vulnerability in ServiceNow has been identified as potentially the most severe AI-related security flaw to date. The CISA has warned of active exploitation of a Gogs vulnerability enabling remote code execution. Additionally, sophisticated malware campaigns are targeting diverse environments, from Ukraine's defense forces with PluggyApe backdoor malware to Linux cloud servers through the advanced VoidLink framework. North Korean APT groups are actively conducting quishing attacks against government agencies, while web skimming campaigns continue to steal credit card information from online checkout pages.

## Active Exploitation Details

### Microsoft Zero-Day Vulnerabilities
- **Description**: Three zero-day vulnerabilities patched in Microsoft's January 2026 Patch Tuesday, with one being actively exploited in the wild
- **Impact**: Active exploitation allowing attackers to compromise Windows systems
- **Status**: Patches available through KB5073724 extended security update and cumulative updates KB5074109 and KB5073455

### Gogs Code Execution Vulnerability
- **Description**: High-severity security flaw in Gogs (Go Git Service) that enables remote code execution
- **Impact**: Attackers can execute arbitrary code on vulnerable Gogs installations
- **Status**: Actively exploited in the wild according to CISA warning, added to Known Exploited Vulnerabilities catalog

### ServiceNow AI Platform Critical Flaw
- **Description**: Critical security vulnerability in ServiceNow's AI Platform that allows unauthenticated user impersonation
- **Impact**: Unauthorized access to customer data and connected systems through unguarded legacy chatbot infrastructure
- **Status**: Patched by ServiceNow, described as "most severe AI vulnerability to date"

## Affected Systems and Products

- **Microsoft Windows Systems**: Windows 10, Windows 11 versions 23H2, 24H2, and 25H2 affected by zero-day vulnerabilities
- **Gogs Git Service**: Self-hosted Git service vulnerable to remote code execution
- **ServiceNow AI Platform**: AI-enabled chatbot systems exposed customer data and connected infrastructure
- **Linux Cloud Servers**: Targeted by VoidLink malware framework in containerized environments
- **Ukraine Defense Forces**: Officials targeted by PluggyApe backdoor through charity-themed campaigns
- **MEXC Cryptocurrency Exchange**: API keys stolen through malicious Chrome extensions
- **Web Payment Systems**: American Express, Diners Club, Discover payment networks targeted by skimming campaigns

## Attack Vectors and Techniques

- **Charity-Themed Social Engineering**: Malicious campaigns targeting Ukraine's army using humanitarian themes to deliver PluggyApe backdoor
- **Multi-Stage Malware Delivery**: SHADOW#REACTOR campaign using text-only files to deliver Remcos RAT while bypassing security tools
- **Malicious Browser Extensions**: Chrome extensions masquerading as trading tools to steal cryptocurrency API keys
- **QR Code Phishing (Quishing)**: North Korean APT Kimsuky using QR codes in phishing emails targeting government agencies
- **Web Skimming**: Long-running campaign since January 2022 targeting online checkout pages to steal credit card data
- **LinkedIn Social Engineering**: Fake comment-reply tactics using spoofed platform notifications for phishing
- **Python and Cloudflare Abuse**: Legitimate cloud services weaponized to deliver AsyncRAT malware
- **Brute Force Attacks**: GoBruteforcer botnet targeting over 50,000 Linux servers with weak credentials

## Threat Actor Activities

- **North Korean APT Kimsuky**: Conducting quishing attacks against US and foreign government agencies, NGOs, and academic institutions using QR code-filled phishing emails
- **SHADOW#REACTOR Operators**: Deploying sophisticated multi-stage attack chains using text files to deliver Remcos RAT and evade detection
- **VoidLink Developers**: Creating advanced cloud-native malware framework with custom loaders, implants, rootkits, and plugins for Linux environments
- **Ukrainian-Targeting Groups**: Conducting charity-themed campaigns against Ukraine's Defense Forces to deliver PluggyApe backdoor malware
- **Web Skimming Groups**: Operating long-term campaigns since 2022 targeting major payment networks and online retailers
- **Cryptocurrency Threat Actors**: Developing malicious Chrome extensions to steal MEXC exchange API keys from traders
- **GoBruteforcer Operators**: Managing botnet infrastructure targeting Linux servers with enhanced AI-generated configurations