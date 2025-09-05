# Exploitation Report

Based on the analyzed security articles, several critical exploitation activities are currently underway. Most notably, threat actors have been actively exploiting a zero-day vulnerability in legacy Sitecore deployments to deploy WeepSteel reconnaissance malware. Additionally, TP-Link has confirmed an unpatched zero-day vulnerability affecting multiple router models, while CISA has warned that other router flaws are being exploited in attacks. Russian state-sponsored group APT28 has deployed a new Microsoft Outlook backdoor called NotDoor in targeted campaigns against NATO countries, and the GhostRedirector threat cluster has compromised at least 65 Windows servers using sophisticated backdoor techniques.

## Active Exploitation Details

### Sitecore Zero-Day Vulnerability
- **Description**: An unpatched zero-day vulnerability affecting legacy Sitecore deployments
- **Impact**: Allows threat actors to deploy WeepSteel reconnaissance malware for data collection and system reconnaissance
- **Status**: Currently being exploited in the wild, patch status unknown

### TP-Link Router Zero-Day
- **Description**: An unpatched zero-day vulnerability impacting multiple TP-Link router models
- **Impact**: Enables unauthorized access and potential network compromise
- **Status**: Confirmed by TP-Link as unpatched, actively being exploited according to CISA warnings

### NotDoor Outlook Backdoor
- **Description**: A sophisticated Microsoft Outlook backdoor deployed by Russian APT28 group
- **Impact**: Provides persistent access to corporate email systems and enables data exfiltration
- **Status**: Active deployment in targeted campaigns against NATO country organizations

## Affected Systems and Products

- **Sitecore CMS**: Legacy deployments vulnerable to zero-day exploitation
- **TP-Link Routers**: Multiple router models affected by unpatched zero-day vulnerability
- **Microsoft Outlook**: Targeted by NotDoor backdoor in corporate environments
- **Windows Servers**: At least 65 servers compromised by GhostRedirector cluster, primarily in Brazil
- **PowerSchool Systems**: Education software platform suffered massive breach affecting 62 million students
- **Chess.com Platform**: Compromised via third-party file transfer application
- **Salesloft Drift**: Supply chain attack affecting multiple high-profile customers

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched vulnerabilities in Sitecore and TP-Link systems
- **Backdoor Deployment**: Installation of WeepSteel malware and NotDoor Outlook backdoors for persistent access
- **Supply Chain Attacks**: Compromise of third-party services affecting downstream customers
- **Phishing-as-a-Service**: Global enterprise using cloaking techniques on public cloud infrastructure
- **IIS Module Injection**: GhostRedirector using Gamshen IIS module and Rungan backdoor for server compromise
- **File Transfer Exploitation**: Unauthorized access through compromised file transfer applications

## Threat Actor Activities

- **APT28 (Russian State-Sponsored)**: Deploying NotDoor Outlook backdoor against companies in NATO countries across multiple sectors
- **GhostRedirector Cluster**: Previously undocumented threat group compromising Windows servers primarily in Brazil using sophisticated backdoor techniques
- **Phishing-as-a-Service Operators**: Running undetected operations on Google and Cloudflare infrastructure for over 3 years using advanced cloaking methods
- **Chinese Data Collection**: Czech cyber agency NÚKIB warning about products and software sending user data back to China
- **WeepSteel Operators**: Exploiting Sitecore zero-day to deploy reconnaissance malware for intelligence gathering