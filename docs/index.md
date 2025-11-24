# Exploitation Report

Critical exploitation activity is currently underway across multiple enterprise systems, with threat actors actively targeting vulnerabilities in Oracle Identity Manager, Windows Server Update Services (WSUS), and Oracle E-Business Suite. The most concerning activity involves a zero-day vulnerability in Oracle Identity Manager that CISA has added to its Known Exploited Vulnerabilities catalog, alongside active ShadowPad malware campaigns exploiting WSUS infrastructure. Enterprise organizations face immediate risks from these ongoing attacks, with threat actors achieving full system access and deploying sophisticated malware payloads.

## Active Exploitation Details

### Oracle Identity Manager Remote Code Execution
- **Description**: A critical zero-day vulnerability in Oracle Identity Manager that allows remote code execution
- **Impact**: Attackers can achieve complete system compromise and execute arbitrary code on affected systems
- **Status**: Currently being actively exploited in the wild; CISA has added to Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2025-61757

### Windows Server Update Services (WSUS) Vulnerability
- **Description**: A recently patched security flaw in Microsoft Windows Server Update Services that enables malware distribution
- **Impact**: Threat actors can distribute malware through compromised WSUS infrastructure, achieving full system access
- **Status**: Recently patched but actively exploited by ShadowPad malware operators targeting Windows Servers

### Oracle E-Business Suite Zero-Day
- **Description**: A zero-day vulnerability in Oracle E-Business Suite that was exploited to breach corporate networks
- **Impact**: Data breach resulting in exposure of personal information from compromised enterprise systems
- **Status**: Exploited in Cox Enterprises breach, leading to significant data exposure

### Grafana Enterprise SCIM Vulnerability
- **Description**: Maximum severity vulnerability in Grafana Enterprise's SCIM implementation enabling user impersonation
- **Impact**: Attackers can treat new users as administrators or achieve privilege escalation
- **Status**: Recently patched by Grafana Labs
- **CVE ID**: CVE-2025-41115

## Affected Systems and Products

- **Oracle Identity Manager**: All versions vulnerable to remote code execution attacks
- **Microsoft Windows Server Update Services**: Windows Server systems with WSUS services deployed
- **Oracle E-Business Suite**: Enterprise installations vulnerable to zero-day exploitation
- **Grafana Enterprise**: Systems with SCIM configuration enabled face maximum severity risk
- **WhatsApp API**: Contact-discovery API exposed 3.5 billion mobile phone numbers due to lack of rate limiting
- **LINE Messaging App**: Custom protocol vulnerabilities enabling message replays and impersonation attacks

## Attack Vectors and Techniques

- **ShadowPad Malware Distribution**: Leveraging compromised WSUS infrastructure to distribute malware payloads to Windows Servers
- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in Oracle products for initial access
- **API Abuse**: Exploitation of rate-limiting failures in messaging platforms for large-scale data harvesting
- **Browser Notification Phishing**: Matrix Push C2 platform using browser notifications for fileless, cross-platform attacks
- **Third-Party Application Compromise**: Exploitation of vendor relationships to access customer data, as seen in Iberia and Salesforce incidents

## Threat Actor Activities

- **ShadowPad Operators**: Actively exploiting WSUS vulnerabilities to distribute malware and achieve full system access on Windows Server infrastructure
- **APT31**: China-linked group conducting stealthy cyberattacks against Russian IT sector using cloud services between 2024-2025
- **ShinyHunters Affiliates**: Exploiting third-party applications like Gainsight to steal Salesforce customer data in repeat attack patterns
- **Qilin Ransomware Group**: Conducting sophisticated ransomware operations with complex attack chains involving rogue ScreenConnect access
- **Scattered Lapsus$ Hunters**: Insider threat activities involving information sharing with external hackers, as detected by CrowdStrike