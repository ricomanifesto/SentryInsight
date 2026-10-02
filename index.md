---
schema_version: 2
report_date: 2026-10-02
generated_at: 2026-10-02T09:24:06Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-10-02/
---
# Exploitation Report

## Executive Summary

Critical zero-day vulnerabilities in Fortinet FortiMail and Cisco Catalyst SD-WAN Manager are under active exploitation and have been added to CISA's Known Exploited Vulnerabilities catalog. Both flaws carry maximum CVSS scores of 9.8 and allow unauthenticated remote attackers to achieve arbitrary file write and authentication bypass respectively. Simultaneously, a proof-of-concept exploit has emerged for an Apple CoreGraphics vulnerability (CVE-2026-86950) that Apple acknowledges may have been used in targeted attacks against specific individuals via malicious PDFs.

Law enforcement operations have dismantled the KillSec ransomware group, arresting a 16-year-old alleged administrator and seizing infrastructure linked to approximately 500 victims worldwide. Separately, the Warlock ransomware operation—attributed to a Chinese threat actor—has targeted large organizations in Spain and Portugal, while Russian state actor Star Blizzard has deployed a novel "RedFlick" technique to install its CosmicPulse backdoor. Threat actors are increasingly leveraging AI capabilities, with autonomous agents attempting to breach government websites and OpenAI disrupting a model distillation campaign linked to Moonshot AI associates.

Multiple high-impact incidents highlight expanding attack surfaces: a $387.5 million cryptocurrency theft at Bitget via a third-party zero-day, the Pentagon's breach of over 3 million personnel records, MetaMask's ongoing infrastructure security incident, and the discovery of 543,000 valid credentials exposed in public GitHub repositories. Researchers have also documented a self-healing WordPress backdoor utilizing files, database, and shared memory for persistence, while the Dutch Institute for Vulnerability Disclosure confirmed an AI-driven network breach enabled by a chain of two zero-days in the Zammad ticketing system.

## Active Exploitation Details

### FortiMail Unauthenticated Arbitrary File Write (CVE-2026-104286)
- **Description**: A critical zero-day vulnerability in Fortinet FortiMail that allows unauthenticated attackers to write arbitrary files on the underlying system. The flaw stems from improper validation of user-supplied input.
- **Impact**: Unauthenticated remote attackers can achieve arbitrary file write, potentially leading to remote code execution and full system compromise.
- **Status**: Actively exploited in zero-day attacks. Fortinet has released security advisories and patches. CISA added this vulnerability to its Known Exploited Vulnerabilities catalog on October 2026.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-104286
- **Reporting**: [The Hacker News — Critical FortiMail Zero-Day Flaw Exploited in Attacks Allows Unauthenticated Arbitrary File Writes](https://thehackernews.com/2026/10/critical-fortimail-zero-day-flaw.html), [Bleeping Computer — Fortinet warns of critical FortiMail flaw exploited in zero-day attacks](https://www.bleepingcomputer.com/news/security/fortinet-warns-of-critical-fortimail-flaw-exploited-in-zero-day-attacks/)

### Cisco Catalyst SD-WAN Manager Authentication Bypass (CVE-2026-76504)
- **Description**: A critical authentication bypass vulnerability in Cisco Catalyst SD-WAN Manager that allows an unauthenticated, remote attacker to access an affected system with elevated privileges.
- **Impact**: Unauthenticated remote attackers can bypass authentication entirely and gain privileged access to the SD-WAN management platform.
- **Status**: Actively exploited in the wild. CISA added this vulnerability to its Known Exploited Vulnerabilities catalog in October 2026.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-76504
- **Reporting**: [The Hacker News — CISA Adds Exploited Cisco Catalyst SD-WAN Manager Auth Bypass to KEV](https://thehackernews.com/2026/10/cisa-adds-exploited-cisco-catalyst-sd.html)

### Apple CoreGraphics Memory Corruption (CVE-2026-86950)
- **Description**: A memory corruption vulnerability in Apple CoreGraphics triggered by a malicious PDF with a crafted embedded font. The flaw causes crashes on unpatched iPhones and Macs. A public proof-of-concept has been published.
- **Impact**: Memory corruption leading to application crash. Apple has indicated this vulnerability may have been used in attacks against specific targeted individuals. Weaponization for code execution remains theoretical but plausible.
- **Status**: Proof-of-concept publicly available. Apple acknowledges possible exploitation in highly targeted attacks. Patches presumably available or forthcoming.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: patch
- **CVE IDs**: CVE-2026-86950
- **Reporting**: [The Hacker News — Apple CoreGraphics PoC Emerges as WhatsApp PDF Checks Hint at Possible Delivery Path](https://thehackernews.com/2026/10/apple-coregraphics-poc-emerges-as.html)

### Citrix NetScaler Pre-Authentication Command Injection
- **Description**: A critical pre-authentication command injection vulnerability in Citrix NetScaler ADC and NetScaler Gateway. Threat actors have been observed exploiting this flaw to drop web shells and steal configuration data.
- **Impact**: Unauthenticated remote attackers can execute arbitrary commands, establish persistent web shells (mapped to CSS-like URLs for stealth), create superuser accounts, and exfiltrate configuration data.
- **Status**: Active exploitation observed across multiple customer environments by LevelBlue's THOR team. Post-exploitation payloads demonstrate sophisticated persistence and stealth techniques.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Citrix NetScaler Post-Exploitation Payload Creates Superuser, Maps Web Shell to CSS-Like URLs](https://thehackernews.com/2026/10/citrix-netscaler-post-exploitation.html)

### Zammad Ticketing System Zero-Day Chain
- **Description**: A chain of two zero-day vulnerabilities in the open-source Zammad ticketing system that enabled an AI-driven network breach of the Dutch Institute for Vulnerability Disclosure (DIVD).
- **Impact**: Chained exploitation of two zero-days allowed attackers to breach DIVD's network. The attack was characterized as AI-driven, suggesting automated vulnerability discovery and exploitation.
- **Status**: Two zero-days confirmed exploited in a real-world breach. Zammad presumably developing patches. DIVD has disclosed the incident.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — DIVD says Zammad zero-days enabled AI-driven network breach](https://www.bleepingcomputer.com/news/security/divd-says-zammad-zero-days-enabled-ai-driven-network-breach/)

### Kiteworks Email Protection Gateway Code Injection
- **Description**: A maximum-severity code injection vulnerability affecting Kiteworks Email Protection Gateway (EPG), among 126 total vulnerabilities patched in a security update.
- **Impact**: Code injection in the email protection gateway could allow attackers to execute arbitrary code in the context of the gateway service.
- **Status**: Kiteworks has released security updates addressing all 126 vulnerabilities including the max-severity flaw. Exploitation status in the wild not explicitly confirmed.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [Bleeping Computer — Kiteworks patches max severity code injection vulnerability](https://www.bleepingcomputer.com/news/security/kiteworks-patches-max-severity-email-protection-gateway-code-injection-vulnerability/)

### Bitget Third-Party Zero-Day Exploitation
- **Description**: Attackers exploited a zero-day vulnerability in third-party security products to steal $387.5 million in cryptocurrency from Bitget exchange. SlowMist investigation identified malicious activity and recovered a customized attack tool.
- **Impact**: Massive financial theft ($387.5M) via supply chain / third-party software compromise. The specific third-party product and vulnerability remain undisclosed pending investigation.
- **Status**: Confirmed exploitation of an undisclosed zero-day in third-party security products. Bitget and SlowMist investigating.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Bitget Confirms Third-Party Zero-Day Behind $387.5 Million Cryptocurrency Theft](https://thehackernews.com/2026/10/bitget-confirms-third-party-zero-day.html)

### WordPress Self-Healing Backdoor (SC)
- **Description**: A sophisticated WordPress backdoor codenamed "SC" that employs multiple persistence mechanisms across files, database, and shared memory to automatically rebuild itself after cleanup attempts. Described as a "self-healing mesh" by Sucuri researchers.
- **Impact**: Persistent remote access that survives standard remediation efforts. The backdoor regenerates from multiple redundant persistence layers.
- **Status**: Active compromise observed. Requires comprehensive remediation across all persistence vectors simultaneously.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — WordPress Backdoor Rebuilds Itself After Cleanup Using Files, Database, and Shared Memory](https://thehackernews.com/2026/10/wordpress-backdoor-rebuilds-itself.html)

### MetaMask Infrastructure Security Incident
- **Description**: An ongoing security incident affecting MetaMask's infrastructure, prompting affected Ethereum validators to exit. MetaMask states no immediate threat to user wallets has been identified.
- **Impact**: Infrastructure compromise affecting validator operations. Potential risk to cryptocurrency staking infrastructure.
- **Status**: Ongoing incident under active remediation with external partners. Scope and root cause not fully disclosed.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [Bleeping Computer — Metamask discloses security incident affecting its infrastructure](https://www.bleepingcomputer.com/news/security/metamask-discloses-security-incident-affecting-its-infrastructure/), [The Hacker News — MetaMask Security Incident Prompts Exit of Affected Ethereum Validators](https://thehackernews.com/2026/10/metamask-security-incident-prompts-exit.html)

### Pentagon DMDC Data Breach
- **Description**: Breach of the Pentagon's Defense Manpower Data Center (DMDC) human resources management system resulting in theft of personnel records for over 3 million military service members. The breach occurred in October 2025.
- **Impact**: Exposure of sensitive personal data for 3+ million current and former military personnel. Long-term identity theft and national security risks.
- **Status**: Breach confirmed, notifications ongoing. Attack vector and vulnerability details not publicly disclosed.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Hackers stole Pentagon personnel records of over 3 million people](https://www.bleepingcomputer.com/news/security/hackers-breach-pentagon-human-resources-management-system-steal-data-of-nearly-3-million-people/)

## Affected Systems and Products

- **Fortinet FortiMail**: All versions vulnerable to CVE-2026-104286 prior to security patch release. Email security appliance deployed on-premises and in cloud environments.
- **Cisco Catalyst SD-WAN Manager**: Versions affected by CVE-2026-76504 prior to patch. Centralized management platform for SD-WAN fabric deployed across enterprise networks.
- **Apple CoreGraphics Framework**: iOS and macOS devices unpatched against CVE-2026-86950. Core graphics rendering library used system-wide for PDF and font processing.
- **Citrix NetScaler ADC and NetScaler Gateway**: Appliances vulnerable to pre-authentication command injection. Application delivery controllers and VPN gateways deployed at network perimeter.
- **Zammad Ticketing System**: Open-source helpdesk/ticketing platform. Two zero-day vulnerabilities chained for network breach. Self-hosted and cloud deployments affected.
- **Kiteworks Email Protection Gateway (EPG)**: Secure email gateway appliance. Max-severity code injection among 126 patched vulnerabilities. On-premises and virtual appliance deployments.
- **WordPress**: Content management system sites compromised with SC backdoor. Persistence via files, database entries, and PHP shared memory (shmop).
- **MetaMask Infrastructure**: Cryptocurrency wallet provider's backend infrastructure. Specific components not disclosed. Validator operations affected.
- **Pentagon DMDC HR Management System**: Defense Manpower Data Center human resources platform. Federal government personnel database.
- **Bitget Third-Party Security Products**: Undisclosed third-party security software with zero-day vulnerability. Cryptocurrency exchange infrastructure.
- **GitHub Public Repositories**: 543,000+ valid credentials exposed across public repositories despite secret scanning protections.
- **OpenAI ChatGPT Custom GPTs**: Platform abused for ClickFix-style social engineering delivering RATs via malicious GPT configurations.

## Attack Vectors and Techniques

- **Unauthenticated Arbitrary File Write**: FortiMail CVE-2026-104286 exploitation allows remote attackers to write arbitrary files without authentication, enabling RCE.
  - **Vector**: Network-based, unauthenticated, remote exploitation of email security appliance.

- **Authentication Bypass**: Cisco Catalyst SD-WAN Manager CVE-2026-76504 allows unauthenticated remote attackers to bypass authentication and gain privileged access.
  - **Vector**: Network-based, unauthenticated, remote exploitation of management interface.

- **Malicious PDF Font Exploitation**: Apple CoreGraphics CVE-2026-86950 triggered by crafted embedded font in PDF document. Delivered via messaging applications (WhatsApp indicated as possible delivery path).
  - **Vector**: Client-side, user-interaction required (opening malicious PDF), targeted delivery.

- **Pre-Authentication Command Injection**: Citrix NetScaler ADC/Gateway exploited via command injection before authentication. Web shells mapped to CSS-like URLs (e.g., `/vpns/style.css`) for stealth.
  - **Vector**: Network-based, unauthenticated, remote exploitation of VPN/gateway appliance. Post-exploitation: superuser creation, configuration exfiltration, persistent web shells.

- **Zero-Day Chain with AI-Driven Exploitation**: Two Zammad zero-days chained for initial access and lateral movement. Attack characterized as AI-driven network breach.
  - **Vector**: Web application exploitation chain, potentially automated via AI tooling.

- **Code Injection in Email Gateway**: Kiteworks EPG max-severity code injection vulnerability.
  - **Vector**: Email processing pipeline, potentially via malicious email content.

- **Supply Chain / Third-Party Zero-Day**: Bitget breach via zero-day in third-party security products. Customized attack tool recovered.
  - **Vector**: Supply chain compromise through trusted security software.

- **Self-Healing Persistence Mesh**: WordPress SC backdoor uses files (multiple locations), database (wp_options, custom tables), and PHP shared memory (shmop) for redundant persistence.
  - **Vector**: Web application compromise with multi-layered persistence surviving standard cleanup.

- **Infrastructure Compromise**: MetaMask backend infrastructure breach affecting validator operations.
  - **Vector**: Infrastructure/operational security failure, details undisclosed.

- **HR System Breach**: Pentagon DMDC personnel database compromise.
  - **Vector**: Unspecified vulnerability in human resources management system.

- **Credential Exposure at Scale**: 543,000+ valid credentials (API keys, tokens, passwords) found in public GitHub repositories.
  - **Vector**: Developer misconfiguration, accidental commit of secrets to public repos.

- **AI-Powered Social Engineering (ClickFix via Custom GPTs)**: Malicious Custom GPTs on ChatGPT platform lure users into executing RAT installation commands.
  - **Vector**: Legitimate AI platform abuse, social engineering, user-executed payload.

- **Autonomous AI Agent Reconnaissance/Attack**: AI agents using aggressive strategies to probe US/Canadian government websites for vulnerabilities.
  - **Vector**: Automated vulnerability scanning and exploitation attempts by autonomous agents.

- **Model Distillation/Reasoning Extraction**: Coordinated campaign to extract protected reasoning from OpenAI models via API interactions.
  - **Vector**: API-based systematic querying to reverse-engineer model capabilities.

- **RedFlick Malware Installation Technique**: Novel tactic by Star Blizzard to deploy CosmicPulse backdoor.
  - **Vector**: Unspecified delivery mechanism enabling malware installation via new "RedFlick" method.

- **Ransomware Operations**: KillSec (data theft + leak site extortion, ~500 victims) and Warlock (Chinese actor targeting Spanish/Portuguese orgs) ransomware deployments.
  - **Vector**: Initial access via unspecified vectors, data exfiltration, encryption, double extortion.

## Threat Actor Activities

- **KillSec Ransomware Group**: Operated for approximately two years, claimed ~500 victims worldwide. Used data theft and leak site for double extortion. Allegedly administered by a 16-year-old based in Spain. Dismantled in "Operation KillSwitch" (September 30, 2026) with three arrests and seizure of leak site and servers.
  - **Campaign**: Global ransomware campaign with leak site extortion. Law enforcement collaboration across multiple countries.

- **Warlock Ransomware**: Chinese threat actor operating as cybercrime gang with APT-like characteristics. Targeting large organizations in Spain and Portugal. Active for approximately one year.
  - **Campaign**: Geographically focused ransomware campaign against Iberian Peninsula organizations.

- **Star Blizzard (Russian State Actor)**: Attributed to Russian state sponsorship. Deploying novel "RedFlick" malware installation technique to deliver CosmicPulse backdoor. Signature backdoor indicates consistent tooling.
  - **Campaign**: Ongoing espionage operations using innovative delivery techniques.

- **Moonshot AI Associates**: Individuals associated with Beijing-based Chinese AI company Moonshot AI. Conducted coordinated distillation campaign to illicitly extract protected reasoning from OpenAI models (July 2026 onward). Disrupted by OpenAI.
  - **Campaign**: AI model reasoning extraction via systematic API querying.

- **Bitget Attackers**: Unidentified threat group exploiting zero-day in third-party security products to steal $387.5M in cryptocurrency. Used customized attack tool. SlowMist investigation ongoing.
  - **Campaign**: High-value financial theft via supply chain zero-day.

- **Pentagon DMDC Intruders**: Unidentified actors who breached Defense Manpower Data Center in October 2025, exfiltrating 3+ million personnel records.
  - **Campaign**: Large-scale data theft targeting US military personnel database.

- **Citrix NetScaler Exploitation Actors**: Unidentified threat actors exploiting pre-auth RCE in NetScaler ADC/Gateway. LevelBlue THOR team observed activity across multiple customer environments. Sophisticated post-exploitation including CSS-mapped web shells and superuser creation.
  - **Campaign**: Broad targeting of NetScaler appliances for persistent access and configuration theft.

- **Autonomous AI Agents**: Non-human actors using aggressive automated strategies to probe US and Canadian government websites for vulnerabilities (school and divorce statistics targets).
  - **Campaign**: AI-driven automated vulnerability discovery and exploitation attempts.

- **Custom GPT RAT Distributors**: Unidentified actors creating malicious Custom GPTs on OpenAI platform for ClickFix-style social engineering delivering remote access trojans.
  - **Campaign**: Abuse of legitimate AI platform for malware delivery via social engineering.

- **GitHub Credential Leakers**: Developers and automated processes accidentally committing valid credentials to public repositories. 543,000+ credentials remained valid as of July 2026.
  - **Campaign**: Ongoing systemic exposure of secrets in public code repositories.