# Exploitation Report

Critical zero-day vulnerabilities are currently being exploited in the wild, with threat actors targeting Sitecore content management systems and TP-Link routers. The Sitecore zero-day has enabled attackers to deploy WeepSteel reconnaissance malware and backdoors through ViewState deserialization attacks. Meanwhile, Russian state-sponsored group APT28 has deployed the NotDoor Outlook backdoor against NATO countries, and the GhostRedirector threat cluster has compromised at least 65 Windows servers using sophisticated IIS modules and backdoors. Additionally, CISA has warned of active exploitation of multiple TP-Link router vulnerabilities, highlighting the ongoing threat to network infrastructure.

## Active Exploitation Details

### Sitecore Zero-Day Vulnerability
- **Description**: A zero-day vulnerability in legacy Sitecore deployments that allows threat actors to exploit exposed ASP.NET machine keys for remote injection and deserialization attacks
- **Impact**: Attackers can deploy WeepSteel reconnaissance malware and establish persistent backdoors on compromised systems
- **Status**: Currently being exploited in the wild; represents the latest example of ViewState-based attacks

### TP-Link Router Zero-Day
- **Description**: An unpatched zero-day vulnerability affecting multiple TP-Link router models
- **Impact**: Enables unauthorized access and control of network infrastructure
- **Status**: Confirmed by TP-Link as unpatched; CISA has warned of active exploitation of other TP-Link router flaws

### NotDoor Outlook Backdoor
- **Description**: A sophisticated Microsoft Outlook backdoor deployed by Russian APT28 group
- **Impact**: Provides persistent access to corporate email systems and enables data exfiltration
- **Status**: Actively deployed against companies in NATO countries across multiple sectors

## Affected Systems and Products

- **Sitecore Content Management Systems**: Legacy deployments vulnerable to ViewState deserialization attacks
- **TP-Link Routers**: Multiple router models affected by zero-day and other exploited vulnerabilities
- **Microsoft Outlook**: Targeted by NotDoor backdoor in corporate environments
- **Windows Servers**: At least 65 servers compromised by GhostRedirector, primarily in Brazil
- **IIS Web Servers**: Targeted by malicious Gamshen IIS modules for SEO manipulation
- **PowerSchool Education Platform**: 62 million students affected by data breach, including 880,000 Texans
- **Chess.com Platform**: Breached via third-party file transfer application
- **Salesloft Drift Customers**: Multiple high-profile organizations affected by supply chain attack

## Attack Vectors and Techniques

- **ViewState Deserialization**: Exploitation of exposed ASP.NET machine keys for remote code execution
- **Zero-Day Exploitation**: Active targeting of unpatched vulnerabilities in Sitecore and TP-Link systems
- **Backdoor Deployment**: Installation of persistent access tools like NotDoor and WeepSteel malware
- **IIS Module Injection**: Use of malicious Gamshen modules to manipulate search engine rankings
- **Supply Chain Attacks**: Compromise of third-party services affecting multiple downstream customers
- **Phishing-as-a-Service**: Global enterprise using cloaking techniques on public cloud infrastructure
- **SEO Manipulation**: Injection of gambling site links to artificially boost search rankings

## Threat Actor Activities

- **APT28 (Russian State-Sponsored)**: Deploying NotDoor Outlook backdoors against NATO country organizations across multiple sectors
- **GhostRedirector**: Previously undocumented threat cluster that compromised 65+ Windows servers using Rungan backdoor and Gamshen IIS modules, primarily targeting Brazilian infrastructure
- **Chinese Threat Actors**: Operating SEO manipulation campaigns to boost gambling sites through malicious IIS modules and search engine gaming
- **WeepSteel Operators**: Deploying reconnaissance malware through Sitecore zero-day exploitation
- **Phishing-as-a-Service Groups**: Running undetected operations on Google and Cloudflare infrastructure for over 3 years using advanced cloaking techniques