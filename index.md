# Exploitation Report

Critical exploitation activity is currently centered around several high-severity vulnerabilities being actively exploited in the wild. The most significant threat involves a zero-day flaw in Oracle Identity Manager (CVE-2025-61757) that has been added to CISA's Known Exploited Vulnerabilities catalog due to active exploitation. This vulnerability allows for remote code execution and poses a significant risk to enterprise identity management systems. Additionally, threat actors are exploiting a recently patched Microsoft Windows Server Update Services (WSUS) vulnerability to distribute ShadowPad malware, demonstrating sophisticated supply chain attack techniques. A separate Oracle E-Business Suite zero-day vulnerability has also been confirmed as actively exploited, leading to a significant data breach at Cox Enterprises. These incidents highlight the ongoing threat posed by zero-day vulnerabilities in enterprise infrastructure components.

## Active Exploitation Details

### Oracle Identity Manager Zero-Day Vulnerability
- **Description**: A critical security flaw in Oracle Identity Manager that allows for remote code execution
- **Impact**: Attackers can achieve full system compromise and potentially gain administrative access to identity management systems
- **Status**: Actively exploited in the wild and added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2025-61757

### Microsoft Windows Server Update Services (WSUS) Vulnerability
- **Description**: A recently patched security flaw in Microsoft WSUS that enables malware distribution through the update mechanism
- **Impact**: Threat actors can distribute malware including ShadowPad to Windows servers through compromised update channels
- **Status**: Recently patched but actively exploited by threat actors to deliver malware payloads

### Oracle E-Business Suite Zero-Day Vulnerability
- **Description**: An unpatched zero-day vulnerability in Oracle E-Business Suite that allows unauthorized access to enterprise systems
- **Impact**: Complete compromise of business applications and exposure of sensitive customer and business data
- **Status**: Zero-day vulnerability actively exploited, leading to confirmed data breaches

### Grafana Enterprise SCIM Vulnerability
- **Description**: A maximum severity vulnerability in Grafana Enterprise's SCIM implementation that enables privilege escalation and user impersonation
- **Impact**: Attackers can gain administrative privileges or impersonate legitimate users within the monitoring platform
- **Status**: Patched by vendor with security updates released
- **CVE ID**: CVE-2025-41115

## Affected Systems and Products

- **Oracle Identity Manager**: Enterprise identity management systems vulnerable to remote code execution
- **Microsoft Windows Server Update Services (WSUS)**: Windows servers receiving updates through compromised WSUS infrastructure
- **Oracle E-Business Suite**: Enterprise resource planning and business application systems
- **Grafana Enterprise**: Monitoring and observability platforms using SCIM for user management
- **WhatsApp API**: Contact discovery functionality affecting mobile messaging platform users
- **LINE Messaging Application**: Encrypted messaging app with protocol vulnerabilities affecting Asian users

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Exploitation of WSUS infrastructure to distribute ShadowPad malware through legitimate update channels
- **Remote Code Execution**: Direct exploitation of Oracle Identity Manager vulnerability to gain system access
- **Zero-Day Exploitation**: Targeted attacks against unpatched Oracle E-Business Suite installations
- **Privilege Escalation**: Abuse of Grafana SCIM functionality to gain administrative access
- **API Abuse**: Exploitation of WhatsApp's contact discovery API to scrape user information at scale
- **Browser-Based C2**: Use of Matrix Push C2 platform leveraging browser notifications for fileless attacks
- **Protocol Exploitation**: Abuse of LINE messaging app's custom protocol for message replay and impersonation attacks

## Threat Actor Activities

- **ShadowPad Operators**: Actively exploiting WSUS vulnerability to distribute advanced persistent threat malware targeting Windows Server environments
- **APT31 (China-linked)**: Conducting stealthy cyberattacks against Russian IT sector using cloud services between 2024 and 2025
- **ShinyHunters Affiliated Groups**: Targeting Salesforce customers through third-party application compromise, specifically through Gainsight platform
- **Scattered Lapsus$ Hunters**: Involved in insider threat activities, obtaining screenshots from internal systems through compromised insiders
- **Qilin Ransomware Group**: Conducting sophisticated ransomware attacks using rogue ScreenConnect access and infostealer techniques
- **Matrix Push C2 Operators**: Deploying cross-platform phishing attacks using browser notifications for command and control communications