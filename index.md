# Exploitation Report

Critical zero-day vulnerabilities are currently being exploited in the wild, with threat actors targeting Sitecore content management systems and TP-Link routers. The Sitecore zero-day has enabled attackers to deploy WeepSteel reconnaissance malware and backdoors through ViewState deserialization attacks. Meanwhile, Russian state-sponsored group APT28 has deployed the NotDoor Outlook backdoor against NATO countries, and the GhostRedirector threat cluster has compromised at least 65 Windows servers using sophisticated IIS modules and backdoors. These active exploitation campaigns demonstrate the ongoing threat landscape targeting enterprise infrastructure and network devices.

## Active Exploitation Details

### Sitecore Zero-Day Vulnerability
- **Description**: A zero-day vulnerability in legacy Sitecore deployments that allows threat actors to exploit exposed ASP.NET machine keys for remote injection and deserialization attacks
- **Impact**: Attackers can deploy WeepSteel reconnaissance malware and backdoors, enabling persistent access to compromised systems
- **Status**: Currently being actively exploited in the wild; represents the latest example of ViewState-based attacks

### TP-Link Router Zero-Day
- **Description**: An unpatched zero-day vulnerability affecting multiple TP-Link router models
- **Impact**: Enables unauthorized access and control of network infrastructure devices
- **Status**: Confirmed by TP-Link as unpatched; CISA has warned that other router flaws are being exploited in attacks

### NotDoor Outlook Backdoor
- **Description**: A sophisticated Microsoft Outlook backdoor deployed by Russian APT28 group targeting companies in NATO countries
- **Impact**: Provides persistent access to corporate email systems and enables espionage activities
- **Status**: Active deployment against multiple companies across different sectors

## Affected Systems and Products

- **Sitecore Content Management Systems**: Legacy deployments vulnerable to ViewState deserialization attacks
- **TP-Link Routers**: Multiple router models affected by unconfirmed zero-day vulnerability
- **Microsoft Outlook**: Targeted by NotDoor backdoor in NATO country organizations
- **Windows Servers**: At least 65 servers compromised by GhostRedirector, primarily in Brazil
- **PowerSchool Education Software**: 62 million students affected by massive data breach
- **Chess.com Platform**: Data breach via compromised third-party file transfer application
- **Salesloft Drift**: Supply chain attack affecting multiple high-profile customers

## Attack Vectors and Techniques

- **ViewState Deserialization**: Exploitation of exposed ASP.NET machine keys for remote code execution
- **IIS Module Injection**: GhostRedirector uses malicious Gamshen IIS module to inject links for SEO manipulation
- **Backdoor Deployment**: Rungan backdoor used alongside IIS modules for persistent access
- **Email System Compromise**: NotDoor backdoor specifically targets Microsoft Outlook installations
- **Supply Chain Attacks**: Targeting third-party services to compromise downstream customers
- **SEO Poisoning**: Artificial boosting of gambling site search engine rankings through compromised servers

## Threat Actor Activities

- **APT28 (Russian State-Sponsored)**: Deploying NotDoor Outlook backdoors against NATO country organizations across multiple sectors for espionage purposes
- **GhostRedirector**: Previously undocumented threat cluster that has compromised at least 65 Windows servers, primarily located in Brazil, using Rungan backdoors and Gamshen IIS modules for SEO manipulation
- **Sitecore Attackers**: Unidentified threat actors exploiting zero-day vulnerability to deploy WeepSteel reconnaissance malware in ViewState-based attacks
- **TP-Link Exploiters**: Unknown attackers leveraging zero-day vulnerabilities in router infrastructure as warned by CISA