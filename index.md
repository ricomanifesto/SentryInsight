---
schema_version: 2
report_date: 2026-10-04
generated_at: 2026-10-04T04:22:21Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-10-04/
---
# Exploitation Report

## Executive Summary

Critical zero-day exploitation activity dominates the current threat landscape, with Fortinet's FortiMail appliance actively targeted via CVE-2026-104286 (CVSS 9.8), now listed on CISA's Known Exploited Vulnerabilities catalog. Simultaneously, the China-linked ransomware group Warlock continues weaponizing Microsoft SharePoint vulnerabilities—both previously known and novel flaws—to breach critical infrastructure, government, education, water utilities, and telecommunications providers across Portuguese- and Spanish-speaking regions.

Dell has disclosed two maximum-severity flaws in Container Storage Modules (CSM), including CVE-2026-63688 (CVSS 10.0), enabling unauthenticated administrative access and root compromise on Kubernetes nodes, urging immediate patching.

## Active Exploitation Details

### FortiMail Zero-Day Arbitrary File Write
- **Description**: An improper validation vulnerability in Fortinet FortiMail allows unauthenticated attackers to write arbitrary files on the underlying system, leading to remote code execution.
- **Impact**: Attackers can execute unauthorized code or commands on vulnerable FortiMail devices without authentication, achieving full system compromise.
- **Status**: Actively exploited in zero-day attacks; Fortinet has released patches. CISA added to KEV catalog on October 2026.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-104286
- **Reporting**: [The Hacker News — Critical FortiMail Zero-Day Flaw Exploited in Attacks Allows Unauthenticated Arbitrary File Writes](https://thehackernews.com/2026/10/critical-fortimail-zero-day-flaw.html), [Bleeping Computer — Fortinet warns of critical FortiMail flaw exploited in zero-day attacks](https://www.bleepingcomputer.com/news/security/fortinet-warns-of-critical-fortimail-flaw-exploited-in-zero-day-attacks/)

### Dell CSM Missing Authentication for Critical Function
- **Description**: A missing authentication vulnerability in the csm-authorization-storage gRPC server within Dell Container Storage Modules allows unauthenticated attackers to gain administrative privileges.
- **Impact**: Unauthenticated attackers can achieve admin access and root on Kubernetes nodes connected to Dell enterprise storage arrays.
- **Status**: Patched by Dell; maximum severity (CVSS 10.0). Dell urges immediate patching.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: patch
- **CVE IDs**: CVE-2026-63688
- **Reporting**: [The Hacker News — Dell CSM Flaws Enable Unauthenticated Admin Access and Root on Kubernetes Nodes](https://thehackernews.com/2026/10/dell-csm-flaws-enable-unauthenticated.html), [Bleeping Computer — Dell asks admins to patch max severity CSM flaws as soon as possible](https://www.bleepingcomputer.com/news/security/new-max-severity-dell-csm-flaws-give-hackers-admin-privileges/)

### Warlock SharePoint Vulnerability Exploitation
- **Description**: The China-linked threat actor Warlock is weaponizing Microsoft SharePoint vulnerabilities—described as both old and new flaws—to gain initial access, disable security tools, and deploy ransomware.
- **Impact**: Initial access to target networks, security tool disablement, ransomware deployment, and data theft across critical infrastructure, government, education, water utilities, and telecommunications sectors.
- **Status**: Actively exploited in ongoing campaign; specific CVE identifiers not disclosed in reporting.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Warlock Exploits SharePoint Flaws to Disable Security Tools and Deploy Ransomware](https://thehackernews.com/2026/10/warlock-exploits-sharepoint-flaws-to.html), [Bleeping Computer — Warlock ransomware breach SharePoint in water, telecom operator attacks](https://www.bleepingcomputer.com/news/security/warlock-ransomware-breach-sharepoint-in-water-telecom-operator-attacks/)

### GitLab AI Gateway Command Execution
- **Description**: A critical flaw in GitLab's AI Gateway service allows a logged-in user with Duo Agent Platform access to execute arbitrary commands on the gateway under certain conditions. Only self-hosted gateway deployments are affected.
- **Impact**: Arbitrary command execution on the AI Gateway server, potentially leading to further lateral movement or data access.
- **Status**: Patched in gateway versions 19.2.4, 19.3.2, and 19.4.1. CVSS 9.9.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — GitLab Patches Critical 9.9 AI Gateway Flaw Allowing Command Execution on Self-Hosted Servers](https://thehackernews.com/2026/10/gitlab-patches-critical-self-hosted-ai.html), [Bleeping Computer — GitLab warns of critical RCE vulnerability in AI Gateway service](https://www.bleepingcomputer.com/news/security/gitlab-warns-of-critical-rce-vulnerability-in-ai-gateway-service/)

### Frontline Education Third-Party Software Vulnerability
- **Description**: Attackers exploited a vulnerability in third-party software used by Frontline Education to gain unauthorized access to systems and steal employee data including Social Security numbers.
- **Impact**: Unauthorized access and exfiltration of sensitive PII for school district employees across multiple districts.
- **Status**: Breach disclosed; specific vulnerability and patch status not detailed in reporting.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Frontline Education breach exposes school district employee data](https://www.bleepingcomputer.com/news/security/frontline-education-data-breach-impacts-school-district-employees/)

### DTU Identity and Access Management System Breach
- **Description**: Hackers accessed the Technical University of Denmark's identity and access management system and downloaded a large amount of data affecting up to 200,000 users.
- **Impact**: Potential exposure of personal data for 200,000 users including students, employees, and alumni.
- **Status**: Breach disclosed; root cause vulnerability not specified in reporting.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Danish university DTU breach exposes data of up to 200,000 people](https://www.bleepingcomputer.com/news/security/danish-university-dtu-breach-exposes-data-of-up-to-200-000-people/)

### Dell CSM Second Maximum Severity Flaw
- **Description**: Dell disclosed a second maximum-severity vulnerability in Container Storage Modules alongside CVE-2026-63688, enabling unauthenticated admin access and root on Kubernetes nodes.
- **Impact**: Same attack surface as CVE-2026-63688—full compromise of Kubernetes nodes connected to Dell storage.
- **Status**: Patched by Dell; CVE identifier not provided in reporting.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [Bleeping Computer — Dell asks admins to patch max severity CSM flaws as soon as possible](https://www.bleepingcomputer.com/news/security/new-max-severity-dell-csm-flaws-give-hackers-admin-privileges/)

### SWIFT Banking & Government Middleware RCE
- **Description**: Vulnerabilities in middleware used in SWIFT banking and government environments enable remote code execution, with potential for hardware-based MFA bypass in ultra-sensitive environments.
- **Impact**: Remote code execution in high-value financial and government systems; potential bypass of hardware MFA.
- **Status**: Patch available per reporting; specific CVE identifiers not provided.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [Dark Reading — SWIFT Banking & Government Middleware Enables RCE](https://www.darkreading.com/cybersecurity-operations/swift-banking-govt-middleware-rce)

## Affected Systems and Products

- **Fortinet FortiMail**: All versions prior to patched releases; email security appliance deployments
- **Dell Container Storage Modules (CSM)**: Versions prior to security updates; Kubernetes environments connected to Dell enterprise storage arrays (PowerScale, PowerFlex, PowerMax, Unity XT)
- **Microsoft SharePoint**: On-premises and cloud deployments; specific vulnerable versions not disclosed in reporting
- **GitLab AI Gateway (Self-Hosted)**: Versions prior to 19.2.4, 19.3.2, and 19.4.1; only organizations hosting their own AI Gateway
- **Frontline Education Platform**: School district deployments using vulnerable third-party software component
- **Technical University of Denmark (DTU) IAM System**: Identity and access management infrastructure
- **SWIFT Middleware**: Banking and government middleware deployments; specific products not named
- **Kiteworks Data Protection Platform**: Specific versions affected by zero-day (per Dark Reading reporting)
- **Citrix Products**: Specific products affected by zero-day (per Dark Reading reporting)

## Attack Vectors and Techniques

- **Unauthenticated Arbitrary File Write**: FortiMail CVE-2026-104286 exploited via crafted requests to write files without authentication, achieving RCE
- **Missing Authentication in gRPC Service**: Dell CSM csm-authorization-storage server allows unauthenticated admin operations via gRPC calls
- **SharePoint Vulnerability Chaining**: Warlock leverages SharePoint flaws for initial access, then disables security tools (EDR/AV) before ransomware deployment
- **AI Gateway Command Injection**: Authenticated users with Duo Agent Platform access exploit input validation flaws in GitLab AI Gateway for command execution
- **Third-Party Software Supply Chain**: Frontline Education breach originated from vulnerability in vendor software component
- **Identity System Compromise**: DTU breach via direct attack on identity and access management infrastructure
- **Living-off-the-Land C2**: Antino backdoor uses legitimate Outlook and OneDrive services for command-and-control communications
- **Browser-Based Evasion**: Session theft, malicious extensions, and user manipulation techniques that evade EDR telemetry
- **Linux Implant Masquerading**: Backdoors disguised as legitimate Asian mail security products (edge solutions) for persistence
- **Autonomous AI Agent Reconnaissance**: AI agents conducting automated probing of government websites for sensitive data

## Threat Actor Activities

- **Warlock (China-linked)**: Active ransomware campaign exploiting SharePoint vulnerabilities targeting critical infrastructure, government, education, water utilities, and telecommunications in Portuguese- and Spanish-speaking countries. Uses security tool disablement and data exfiltration prior to encryption.
- **Antino Operator (China-nexus)**: Espionage campaign deploying previously undocumented Antino backdoor against government and policy organizations across Taiwan, India, Philippines, Cambodia, Pakistan, Thailand, and Myanmar. Uses Outlook and OneDrive for C2 to blend with legitimate traffic.
- **ShinyHunters**: Member "Rey" reportedly detained in Jordan and cooperating with FBI; group known for data theft and extortion operations.
- **Tren de Aragua (TdA)**: Venezuelan gang members sanctioned by U.S. Treasury for ATM jackpotting attacks stealing millions across United States.
- **KillSec Ransomware**: Operation disrupted by multi-national law enforcement; alleged mastermind identified as 16-year-old; claimed 500 victims over two years.
- **Chinese MSS (via CGTRI)**: MI5 alerts that China's Ministry of State Security funded research involving 100+ UK-linked academics through China General Technology Research Institute for intelligence gathering.
- **Unknown Operators**: Microsoft X account compromise for crypto pump-and-dump; autonomous AI agents probing US/Canadian government sites; DTU breach actors unidentified.