# Exploitation Report

Critical zero-day vulnerabilities are being actively exploited in the wild, with the Clop ransomware gang leading a massive data theft campaign against Oracle E-Business Suite customers using CVE-2025-61882 since early August. Meanwhile, the Storm-1175 threat group has weaponized a maximum severity Fortra GoAnywhere vulnerability (CVE-2025-10035) to deploy Medusa ransomware, and a 13-year-old Redis flaw with a perfect CVSS 10.0 score threatens over 300,000 cloud instances. Additional exploitation activity includes a Zimbra zero-day attack targeting Brazil's military and North Korean hackers stealing a record-breaking $2 billion in cryptocurrency assets this year.

## Active Exploitation Details

### Oracle E-Business Suite Zero-Day
- **Description**: Critical vulnerability in Oracle E-Business Suite (EBS) software that allows unauthorized access and data theft
- **Impact**: Enables threat actors to steal sensitive enterprise data from Oracle EBS customers
- **Status**: Oracle has released an emergency patch after exploitation was discovered; actively exploited since early August 2024
- **CVE ID**: CVE-2025-61882

### Fortra GoAnywhere MFT Vulnerability
- **Description**: Maximum severity security flaw in GoAnywhere Managed File Transfer software
- **Impact**: Remote code execution leading to full system compromise and ransomware deployment
- **Status**: Actively exploited by Storm-1175 group for nearly a month in ransomware attacks
- **CVE ID**: CVE-2025-10035

### Redis Remote Code Execution Flaw
- **Description**: 13-year-old vulnerability in Redis in-memory database software allowing remote code execution
- **Impact**: Full host takeover and complete system compromise under certain circumstances
- **Status**: Maximum severity (CVSS 10.0) with patches available; over 300,000 instances currently exposed

### Zimbra Zero-Day Vulnerability
- **Description**: Previously unknown vulnerability in Zimbra email platform exploited via ICS (calendar) functionality
- **Impact**: Unauthorized access to email systems and potential data theft
- **Status**: Actively exploited in targeted attacks against military organizations

## Affected Systems and Products

- **Oracle E-Business Suite**: Enterprise resource planning software used by large organizations globally
- **Fortra GoAnywhere MFT**: Managed file transfer software used for secure data exchange
- **Redis Database**: In-memory data structure store used across cloud environments and applications
- **Zimbra Email Platform**: Enterprise email and collaboration platform
- **Cryptocurrency Exchanges**: Multiple platforms targeted by North Korean threat actors

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of previously unknown vulnerabilities in Oracle EBS and Zimbra
- **Supply Chain Attacks**: Targeting managed file transfer systems to access downstream victims
- **Social Engineering**: BatShadow group using job recruitment lures to distribute Vampire Bot malware
- **Calendar-based Attacks**: Novel technique using ICS files to exploit Zimbra systems
- **Cloud Infrastructure Targeting**: Exploitation of Redis instances in cloud environments

## Threat Actor Activities

- **Clop Ransomware Gang (Graceful Spider)**: Conducting large-scale data theft operations against Oracle EBS customers using CVE-2025-61882 since early August
- **Storm-1175**: Microsoft-tracked group actively exploiting GoAnywhere vulnerability (CVE-2025-10035) to deploy Medusa ransomware
- **BatShadow Group**: Vietnamese threat actor using new "Vampire Bot" malware in social engineering campaigns targeting job seekers
- **North Korean Hackers**: State-sponsored groups responsible for stealing over $2 billion in cryptocurrency assets in 2024, marking the largest annual total on record
- **ShinyHunters**: Cybercriminal group escalating extortion activities against Red Hat with stolen customer engagement reports
- **Unknown Threat Actor**: Group impersonating Libyan Navy's Office of Protocol to target Brazil's military using Zimbra zero-day