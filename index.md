---
schema_version: 2
report_date: 2026-10-05
generated_at: 2026-10-05T12:32:53Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-10-05/
---
# Exploitation Report

## Executive Summary

Active exploitation of critical vulnerabilities continues across multiple high-value targets, with two zero-day vulnerabilities confirmed under active attack. Citrix NetScaler ADC and Gateway appliances are being targeted via CVE-2026-88779, a memory overflow flaw in SAML processing that has been exploited in targeted attacks to knock deployments offline, with researchers investigating potential remote code execution. Simultaneously, Rejetto HTTP File Server instances face active exploitation of CVE-2026-61500, a session forgery vulnerability stemming from a weak pseudo-random number generator that enables admin session forgery and remote code execution with a CVSS score of 9.3.

China-nexus threat actors are conducting coordinated campaigns across multiple vectors. The Warlock ransomware group continues weaponizing Microsoft SharePoint vulnerabilities—both old and new—to gain initial access against critical infrastructure, government, education, water utilities, and telecommunications providers in Portuguese- and Spanish-speaking countries. Separately, the TA419 espionage group is conducting adversary-in-the-middle phishing campaigns impersonating prominent economists, AI policymakers, and Anthropic employees to target U.S. AI policy experts at think tanks, universities, and legal organizations. A newly documented backdoor dubbed Antino leverages Microsoft Outlook and OneDrive for command and control in a campaign hitting government and policy organizations across seven Asian countries.

Law enforcement achieved a notable disruption with the reported detention of "Rey," a suspected ShinyHunters member, in Jordan, who is allegedly cooperating with the FBI to identify other group members. Meanwhile, the U.S. Treasury sanctioned eight members of the Tren de Aragua gang for ATM jackpotting attacks stealing millions. Organizations also face growing operational challenges from AI-driven noise, as Google suspended its open-source bug bounty program after being flooded with AI-generated vulnerability reports, and browser-based attacks continue evading EDR telemetry through session theft, extension abuse, and user manipulation.

## Active Exploitation Details

### CVE-2026-88779 - NetScaler SAML Memory Overflow Zero-Day
- **Description**: A memory overflow vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway's SAML implementation that can lead to denial of service and is under investigation for potential remote code execution.
- **Impact**: Attackers can knock SAML deployments offline, disrupting authentication for targeted organizations. Researchers are investigating whether the flaw can also be exploited for remote code execution.
- **Status**: Emergency patches released by Citrix. Actively exploited in targeted zero-day attacks prior to patch availability.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-88779
- **Reporting**: [The Hacker News — New NetScaler Zero-Day Exploited in Targeted Attacks Can Knock SAML Deployments Offline](https://thehackernews.com/2026/10/new-netscaler-zero-day-exploited-in.html), [Bleeping Computer — Citrix patches NetScaler SAML zero-day exploited in attacks](https://www.bleepingcomputer.com/news/security/citrix-patches-netscaler-saml-zero-day-exploited-in-attacks/)

### CVE-2026-61500 - Rejetto HFS Session Forgery and RCE
- **Description**: A session forgery vulnerability in Rejetto HTTP File Server (HFS) caused by a weak pseudo-random number generator (PRNG) producing predictable keys, enabling unauthorized admin access and remote code execution.
- **Impact**: Attackers can forge admin sessions, gain unauthorized access, and achieve remote code execution on vulnerable HFS instances.
- **Status**: Actively exploited in the wild per VulnCheck observations. No patch information provided in source articles.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **CVE IDs**: CVE-2026-61500
- **Reporting**: [The Hacker News — Attackers Target Rejetto HFS Flaw That Enables Admin Session Forgery and RCE](https://thehackernews.com/2026/10/attackers-target-rejetto-hfs-flaw-that.html)

### CVE-2026-63688 - Dell CSM Missing Authentication
- **Description**: A missing authentication for critical function vulnerability in the csm-authorization-storage gRPC server within Dell Container Storage Modules (CSM), allowing unauthenticated attackers to gain admin access and root on Kubernetes nodes.
- **Impact**: Unauthenticated attackers can take over susceptible systems, gaining administrative access and root privileges on Kubernetes nodes.
- **Status**: Security updates released by Dell to address multiple critical flaws including this vulnerability.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: patch
- **CVE IDs**: CVE-2026-63688
- **Reporting**: [The Hacker News — Dell CSM Flaws Enable Unauthenticated Admin Access and Root on Kubernetes Nodes](https://thehackernews.com/2026/10/dell-csm-flaws-enable-unauthenticated.html)

### GitLab AI Gateway Command Execution
- **Description**: A critical flaw in GitLab's AI Gateway service that could allow a logged-in user with Duo Agent Platform access to execute arbitrary commands on the gateway under certain conditions. The gateway connects GitLab instances to AI models.
- **Impact**: Authenticated users with specific access can achieve command execution on self-hosted AI Gateway instances, potentially compromising the underlying server.
- **Status**: Patches released in gateway versions 19.2.4, 19.3.2, and 19.4.1. GitLab warns customers to patch immediately.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: patch
- **Reporting**: [The Hacker News — GitLab Patches Critical 9.9 AI Gateway Flaw Allowing Command Execution on Self-Hosted Servers](https://thehackernews.com/2026/10/gitlab-patches-critical-self-hosted-ai.html), [Bleeping Computer — GitLab warns of critical RCE vulnerability in AI Gateway service](https://www.bleepingcomputer.com/news/security/gitlab-warns-of-critical-rce-vulnerability-in-ai-gateway-service/)

### Microsoft SharePoint Vulnerabilities (Warlock Campaign)
- **Description**: Multiple Microsoft SharePoint vulnerabilities, both old and new, weaponized by the Warlock ransomware group for initial access, security tool disablement, and ransomware deployment.
- **Impact**: Full compromise of target organizations including critical infrastructure, government, education, water utilities, and telecommunications providers. Attackers disable security tools before deploying ransomware.
- **Status**: Actively exploited in ongoing campaign observed by Symantec and Carbon Black Threat Hunter Team.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Warlock Exploits SharePoint Flaws to Disable Security Tools and Deploy Ransomware](https://thehackernews.com/2026/10/warlock-exploits-sharepoint-flaws-to.html), [Bleeping Computer — Warlock ransomware breach SharePoint in water, telecom operator attacks](https://www.bleepingcomputer.com/news/security/warlock-ransomware-breach-sharepoint-in-water-telecom-operator-attacks/)

### Frontline Education Third-Party Software Vulnerability
- **Description**: A vulnerability in third-party software exploited by attackers to gain unauthorized access to Frontline Education systems and steal employee information including Social Security numbers.
- **Impact**: Exposure of school district employee PII including Social Security numbers across multiple districts.
- **Status**: Breach disclosed and notifications sent to affected school districts. Specific vulnerability details and patch status not provided in source.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Frontline Education breach exposes school district employee data](https://www.bleepingcomputer.com/news/security/frontline-education-data-breach-impacts-school-district-employees/)

### DTU Identity and Access Management System Compromise
- **Description**: Hackers accessed the Technical University of Denmark's identity and access management system and downloaded a large amount of data, potentially exposing information of up to 200,000 users.
- **Impact**: Potential exposure of personal data for up to 200,000 individuals including students, faculty, and staff.
- **Status**: Breach confirmed by DTU. Attack vector described as access to IAM system but specific vulnerability not identified in source.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Danish university DTU breach exposes data of up to 200,000 people](https://www.bleepingcomputer.com/news/security/danish-university-dtu-breach-exposes-data-of-up-to-200-000-people/)

## Affected Systems and Products

- **Citrix NetScaler ADC and NetScaler Gateway**: Versions vulnerable to CVE-2026-88779 SAML memory overflow. Emergency patches released.
- **Rejetto HTTP File Server (HFS)**: Versions vulnerable to CVE-2026-61500 session forgery via weak PRNG. Active exploitation observed.
- **Dell Container Storage Modules (CSM)**: csm-authorization-storage gRPC server vulnerable to CVE-2026-63688 missing authentication flaw. Security updates released.
- **GitLab AI Gateway (Self-Hosted)**: Versions prior to 19.2.4, 19.3.2, and 19.4.1 vulnerable to command execution flaw. Only self-hosted gateway deployments affected.
- **Microsoft SharePoint**: Multiple versions targeted by Warlock group exploiting both known and potentially new vulnerabilities for initial access.
- **Frontline Education Platform**: Systems compromised via third-party software vulnerability affecting school district employee data.
- **DTU Identity and Access Management System**: Compromised system leading to potential exposure of 200,000 user records.
- **macOS Full Disk Access**: Apple announced tighter controls due to AI agents leveraging FDA permissions to access files, mail, messages, and browsing history without full user knowledge.
- **Google Gemini on macOS**: Upcoming integration could grant full access to Mac files, apps, and web browsing without per-action permission prompts.

## Attack Vectors and Techniques

- **Session Forgery via Weak PRNG**: Attackers exploit predictable cryptographic keys generated by weak pseudo-random number generators to forge administrative sessions and achieve RCE (CVE-2026-61500).
  - **Vector**: Network-based attack against Rejetto HFS web interface; no authentication required.

- **SAML Memory Overflow**: Memory corruption in SAML processing leading to denial of service and potential remote code execution on NetScaler appliances.
  - **Vector**: Targeted network attacks against NetScaler Gateway/ADC SAML endpoints; exploited as zero-day prior to patch.

- **Missing Authentication in gRPC Service**: Unauthenticated access to critical administrative functions in Dell CSM's authorization storage service.
  - **Vector**: Direct gRPC calls to csm-authorization-storage service on Kubernetes nodes; no credentials required.

- **AI Gateway Command Injection**: Authenticated users with Duo Agent Platform access execute arbitrary commands on GitLab's AI Gateway service.
  - **Vector**: Authenticated API requests to self-hosted AI Gateway instances under specific conditions.

- **SharePoint Vulnerability Exploitation**: Weaponization of SharePoint flaws for initial access, followed by security tool disablement and ransomware deployment.
  - **Vector**: Web-based exploitation of SharePoint endpoints; likely includes both authenticated and unauthenticated attack paths.

- **Adversary-in-the-Middle (AitM) Phishing**: TA419 uses AitM techniques to phishing credentials from AI policy experts, impersonating economists, policymakers, and Anthropic employees.
  - **Vector**: Phishing emails with malicious links leading to AitM proxy sites capturing credentials and session tokens.

- **Cloud Service C2 via Outlook/OneDrive**: Antino backdoor leverages legitimate Microsoft Outlook and OneDrive services for command and control communications.
  - **Vector**: Malware uses Microsoft Graph API to communicate with attacker-controlled Outlook/OneDrive accounts, blending with legitimate traffic.

- **Third-Party Software Supply Chain**: Attackers exploit vulnerability in third-party software used by Frontline Education to breach systems.
  - **Vector**: Indirect compromise via vulnerable third-party component in the software supply chain.

- **Identity and Access Management System Compromise**: Direct targeting of IAM infrastructure to download bulk user data.
  - **Vector**: Unspecified access to DTU's IAM system enabling mass data exfiltration.

- **AI-Generated Vulnerability Report Spam**: Flood of AI-generated submissions overwhelms Google's Open Source Vulnerability Rewards Program, forcing suspension.
  - **Vector**: Automated submission of fabricated or low-quality vulnerability reports via bug bounty platform.

- **Browser-Based EDR Evasion**: Attacks steal sessions, abuse extensions, or manipulate users without generating endpoint artifacts detectable by EDR.
  - **Vector**: In-browser attacks including session hijacking, malicious extensions, and social engineering that leave minimal endpoint forensic traces.

## Threat Actor Activities

- **Warlock (China-Linked Ransomware Group)**: Active campaign exploiting SharePoint vulnerabilities against critical infrastructure, government, education, water utilities, and telecommunications in Portuguese- and Spanish-speaking countries. Observed by Symantec and Carbon Black Threat Hunter Team. Disables security tools before deploying ransomware.
  - **Campaign**: Ongoing multi-sector ransomware operations with confirmed breaches of a water utility, telecom provider, regional government body, and university.

- **TA419 (China-Nexus Espionage Group)**: Conducting credential phishing campaigns targeting U.S. AI policy experts at think tanks, universities, and legal organizations. Uses AitM phishing impersonating prominent economists, AI policymakers, and an Anthropic employee.
  - **Campaign**: Multiple phishing operations focused on AI policy intelligence collection; attributed to China-nexus actors.

- **ShinyHunters (Digital Extortion Group)**: Suspected member "Rey" (Saif al-Din Khader) reportedly detained in Jordan on September 29, 2026, and cooperating with FBI to identify other group members.
  - **Campaign**: Law enforcement disruption of extortion group operations; member cooperation may lead to further identifications.

- **Antino Backdoor Operator (China-Nexus)**: Deploying previously undocumented Antino backdoor against government and policy organizations in Taiwan, India, Philippines, Cambodia, Pakistan, Thailand, and Myanmar. Uses Outlook and OneDrive for C2 via Microsoft Graph API.
  - **Campaign**: Regional espionage campaign across seven Asian countries; tracked by Cisco Talos.

- **Tren de Aragua (Venezuelan Gang)**: Eight members sanctioned by U.S. Treasury for ATM jackpotting attacks stealing millions across the United States.
  - **Campaign**: Physical/cyber hybrid attacks on ATM infrastructure ("jackpotting") for financial theft.

- **Unknown Actors (Frontline Education Breach)**: Exploited third-party software vulnerability to access school district employee data including SSNs.
  - **Campaign**: Data theft targeting educational sector HR/payroll systems.

- **Unknown Actors (DTU Breach)**: Compromised university IAM system to exfiltrate data on up to 200,000 individuals.
  - **Campaign**: Large-scale academic institution data breach.