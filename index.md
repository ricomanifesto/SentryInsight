# Exploitation Report

Critical exploitation activity is currently targeting enterprise systems with particular focus on SAP S/4HANA environments and emerging malware campaigns. The most significant threat involves active exploitation of a critical command injection vulnerability in SAP S/4HANA systems (CVE-2025-42957), which allows attackers to execute arbitrary commands on vulnerable servers. Additionally, threat actors are expanding their operations with new malware variants including CastleRAT, while sophisticated phishing campaigns are leveraging SVG files to bypass security detection. A newly discovered Sitecore zero-day vulnerability is also being weaponized for ViewState-based attacks, highlighting the continued evolution of web application exploitation techniques.

## Active Exploitation Details

### SAP S/4HANA Command Injection Vulnerability
- **Description**: A critical command injection vulnerability affecting SAP S/4HANA Enterprise Resource Planning (ERP) software that allows remote code execution
- **Impact**: Attackers can execute arbitrary commands on vulnerable SAP servers, potentially leading to complete system compromise and data breach
- **Status**: Currently being exploited in the wild against exposed servers
- **CVE ID**: CVE-2025-42957

### Sitecore Zero-Day Vulnerability
- **Description**: A zero-day vulnerability in Sitecore content management systems that enables ViewState-based attacks through exposed ASP.NET machine keys
- **Impact**: Remote injection and deserialization attacks leading to potential system compromise
- **Status**: Active exploitation reported with weaponization of ASP.NET machine keys

## Affected Systems and Products

- **SAP S/4HANA**: Enterprise Resource Planning software systems with exposed servers at highest risk
- **Sitecore CMS**: Content management systems with exposed ASP.NET machine keys vulnerable to ViewState attacks
- **ASP.NET Applications**: Web applications with improperly configured machine keys susceptible to deserialization attacks

## Attack Vectors and Techniques

- **Command Injection**: Direct exploitation of input validation flaws in SAP S/4HANA to execute system commands
- **ViewState Manipulation**: Weaponization of exposed ASP.NET machine keys for remote injection and deserialization attacks
- **SVG-Based Phishing**: Use of Scalable Vector Graphics files containing Base64-encoded phishing pages to evade detection
- **Malware-as-a-Service**: Deployment of CastleRAT remote access trojans through CastleLoader framework

## Threat Actor Activities

- **TAG-150**: Expanding CastleLoader malware operations with development of CastleRAT remote access trojan available in both Python and C variants, operating as malware-as-a-service framework
- **Colombian Judicial System Impersonators**: Conducting phishing campaigns using SVG files with Base64-encoded content to target victims while evading traditional security detection mechanisms
- **Enterprise-Focused Attackers**: Actively targeting SAP S/4HANA installations and Sitecore deployments for initial access and system compromise