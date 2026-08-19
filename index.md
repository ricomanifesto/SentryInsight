---
schema_version: 2
report_date: 2026-08-19
generated_at: 2026-08-19T12:57:09Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-08-19/
---
# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse technology stacks, with ransomware gangs and advanced threat actors leveraging flaws in enterprise software, AI platforms, and industrial systems. CISA has confirmed active exploitation of a high-severity Windows Task Host vulnerability and a critical Ray distributed computing flaw, both now listed in the Known Exploited Vulnerabilities catalog. Simultaneously, attackers are exploiting SSRF vulnerabilities in MLflow and FUXA to steal cloud credentials, while the Clop ransomware gang deploys custom web shells on compromised PTC Windchill and FlexPLM servers to decrypt credentials and exfiltrate engineering data.

Threat actor activity remains intense and varied. The Medusa ransomware gang has breached over 500 critical infrastructure organizations since mid-2021, while a China-linked operator demonstrated near-autonomous AI-driven attacks against government agencies in the APAC region. New malware frameworks like TWINLOOT operate entirely within Microsoft's trusted cloud services—abusing SharePoint Online and Teams for command-and-control—while the MacSync Stealer targets macOS through rotating domain infrastructure. Meanwhile, a persistent campaign dubbed City Forum has scraped Salesforce and ServiceNow portals across industries for over a year, and a typosquatting operation on RubyGems delivers information stealers to Windows developers.

Emerging attack vectors highlight the growing abuse of AI systems and supply chain trust. Researchers disclosed the CoSnitch technique, which manipulates Microsoft Copilot Personal into exfiltrating data from connected apps via a single crafted click. A video-call exploit chain targeting Unisoc modems demonstrates novel mobile attack surfaces, while AI "mind viruses" show self-propagation between autonomous agents through persistent prompt files. The Ransom Busters affiliate introduces a new extortion model, posing as incident-recovery services to divert ransom payments. These developments underscore the need for behavioral detection beyond signature-based controls, as prevention rates vary dramatically across techniques.

## Active Exploitation Details

### Windows Task Host Vulnerability
- **Description**: A high-severity vulnerability in Windows Task Host that allows privilege escalation or code execution. The flaw was previously flagged as actively exploited in April 2026.
- **Impact**: Ransomware gangs leverage this vulnerability to gain elevated privileges on compromised Windows systems, facilitating lateral movement and encryption operations.
- **Status**: Actively exploited by multiple ransomware groups; patch available since April 2026.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — CISA: Windows Task Host flaw now exploited by ransomware gangs](https://www.bleepingcomputer.com/news/security/cisa-windows-task-host-flaw-now-exploited-by-ransomware-gangs/)

### Ray Distributed Computing Framework Flaw
- **Description**: A critical vulnerability in Ray, an open-source Python-native distributed computing framework for scaling AI and machine learning workloads. The flaw enables browser-based remote code execution.
- **Impact**: Attackers can achieve remote code execution on systems running Ray, potentially compromising AI/ML infrastructure and associated data.
- **Status**: Actively exploited in the wild; CISA added to KEV catalog with evidence of active exploitation.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — CISA Flags Actively Exploited Ray Flaw That Can Trigger Browser-Based RCE](https://thehackernews.com/2026/08/cisa-flags-actively-exploited-ray-flaw.html)

### MLflow SSRF Vulnerability
- **Description**: A critical server-side request forgery (SSRF) vulnerability in MLflow, an open-source AI platform for managing the machine learning lifecycle.
- **Impact**: Attackers exploit this flaw to steal cloud credentials and secrets from internal metadata services, enabling further cloud environment compromise.
- **Status**: Malicious scanning and exploitation efforts actively observed by watchTowr and VulnCheck.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Attackers Exploit MLflow SSRF Flaw to Steal Cloud Credentials and Secrets](https://thehackernews.com/2026/08/attackers-exploit-mlflow-ssrf-flaw-to.html)

### FUXA SCADA/HMI Software Vulnerability
- **Description**: A critical vulnerability in FUXA, an open-source web-based SCADA/HMI software for operational technology and industrial automation.
- **Impact**: Exploitation allows attackers to target OT environments, potentially disrupting industrial processes and stealing sensitive operational data.
- **Status**: Malicious scanning and exploitation efforts actively observed alongside MLflow attacks.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Attackers Exploit MLflow SSRF Flaw to Steal Cloud Credentials and Secrets](https://thehackernews.com/2026/08/attackers-exploit-mlflow-ssrf-flaw-to.html)

### PTC Windchill and FlexPLM Critical Flaw
- **Description**: A critical security flaw in PTC Windchill and FlexPLM product lifecycle management (PLM) servers that enables deployment of a custom JavaServer Pages (JSP) web shell.
- **Impact**: The Clop-linked web shell provides a fully equipped extortion platform capable of decrypting credentials, enumerating file repositories, mapping engineering vault data, and exfiltrating sensitive intellectual property.
- **Status**: Actively exploited; custom web shells deployed post-exploitation by Clop ransomware gang.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Clop-Linked Windchill Web Shell Decrypts Credentials and Maps Engineering Data](https://thehackernews.com/2026/08/clop-linked-windchill-web-shell.html), [Bleeping Computer — Clop created custom web shell for Windchill data theft attacks](https://www.bleepingcomputer.com/news/security/clop-created-custom-web-shell-for-windchill-data-theft-attacks/)

### GitLab GraphQL Vulnerability (CVE-2026-19478)
- **Description**: A critical zero-click vulnerability in GitLab Community Edition and Enterprise Edition's GraphQL API that allows unauthenticated attackers to remotely modify or delete public projects and user data under certain conditions.
- **Impact**: Unauthenticated attackers can destroy or alter public repositories and user data, causing data loss and integrity violations.
- **Status**: Security updates released by GitLab (CVSS 9.4); limited technical details complicate exploitation detection for self-managed instances.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-19478
- **Reporting**: [Dark Reading — Critical GitLab Zero-Click Flaw Poses Mitigation Challenges](https://www.darkreading.com/application-security/critical-gitlab-zero-click-flaw-mitigation-challenges), [The Hacker News — Critical GitLab GraphQL Flaw Could Let Unauthenticated Attackers Delete Public Projects](https://thehackernews.com/2026/08/critical-gitlab-graphql-flaw-could-let.html)

### Microsoft Copilot Personal Vulnerabilities (CoSnitch)
- **Description**: Three vulnerabilities in Microsoft Copilot Personal, collectively named CoSnitch, involving an undocumented URL parameter that enables meta-hacking techniques to manipulate the AI assistant.
- **Impact**: A single click on a crafted link can silently exfiltrate data from connected applications and information available in the victim's Copilot session.
- **Status**: Disclosed by Varonis Threat Labs; proof-of-concept demonstrated; no confirmed in-the-wild exploitation reported.
- **Severity**: unknown
- **Exploitation Status**: potential
- **Action**: investigate
- **Reporting**: [Dark Reading — 'CoSnitch' Attack Tricked Copilot into Mapping Out Architecture](https://www.darkreading.com/vulnerabilities-threats/cosnitch-attack-copilot-mapping-out-architecture), [The Hacker News — Microsoft Copilot Personal Flaws Could Let One Click Exfiltrate Data From Connected Apps](https://thehackernews.com/2026/08/microsoft-copilot-personal-flaws-could.html)

### Unisoc Modem Vulnerabilities (Video Call Exploit Chain)
- **Description**: Two vulnerabilities in Unisoc modems that can be chained together to achieve remote code execution on Android devices when a victim answers a malicious video call.
- **Impact**: Full device takeover without user interaction beyond answering a call, affecting Android devices using Unisoc baseband processors.
- **Status**: Researcher proof-of-concept demonstrated; no confirmed active exploitation in the wild.
- **Severity**: unknown
- **Exploitation Status**: potential
- **Action**: investigate
- **Reporting**: [Dark Reading — Video Call Exploit Chains Two Flaws in Unisoc Modems](https://www.darkreading.com/mobile-security/video-call-exploit-chains-two-flaws-unisoc-modems)

## Affected Systems and Products

- **Windows Task Host**: All supported Windows versions with the vulnerable component; patch released April 2026
- **Ray**: Open-source distributed computing framework for AI/ML workloads; Python-native; GitHub project with 30k+ stars
- **MLflow**: Open-source AI platform for machine learning lifecycle management; widely used in enterprise ML operations
- **FUXA**: Open-source web-based SCADA/HMI software for operational technology and industrial automation environments
- **PTC Windchill and FlexPLM**: Enterprise product lifecycle management (PLM) servers; engineering data vaults and intellectual property repositories
- **GitLab Community Edition and Enterprise Edition**: Self-managed and SaaS versions; GraphQL API endpoints
- **Microsoft Copilot Personal**: Consumer-facing AI assistant integrated with Microsoft 365 apps and connected services
- **Unisoc Modems**: Baseband processors in Android devices; specific models and versions under investigation
- **RubyGems Package Repository**: Windows developers installing typosquatted packages (ubnuler, ubnlder, ri18nr, reaker, rakier, orakw, joxn, and 9 others)
- **Salesforce and ServiceNow Customer Portals**: Multi-industry portal deployments accessed via compromised credentials or API abuse
- **Microsoft 365 Services (SharePoint Online, Teams)**: Trusted cloud services abused for command-and-control infrastructure
- **macOS Systems**: Targeted by MacSync Stealer information stealer via rotating domain infrastructure
- **SafePal Hardware Wallet Order-Tracking Plug-in**: Authorization flaw in third-party plug-in exposing customer PII
- **Microsoft Azure Infrastructure**: Fortune 500 tenant environments accessed via compromised credentials

## Attack Vectors and Techniques

- **Web Shell Deployment**: Custom JSP web shell deployed post-exploitation on Windchill/FlexPLM servers with built-in credential decryption, repository enumeration, and data staging capabilities
- **SSRF Exploitation**: Server-side request forgery against MLflow and FUXA to access cloud metadata services and steal credentials/secrets
- **AI Meta-Hacking (CoSnitch)**: Manipulation of AI assistants through undocumented parameters and crafted prompts to exfiltrate cross-application data
- **Typosquatting Supply Chain Attack**: 16 malicious RubyGems packages mimicking legitimate library names delivering Windows information stealers (browser credentials, crypto wallets)
- **Compromised Credential Abuse**: Valid credentials used to access Azure infrastructure, Salesforce portals, and ServiceNow instances across multiple Fortune 500 organizations
- **Trusted Service C2 Abuse (TWINLOOT)**: Modular Python implant operating entire command-and-control infrastructure within Microsoft SharePoint Online and Teams, using file operations and Graph API for tasking
- **Video Call Exploit Chain**: Two chained vulnerabilities in Unisoc modems triggered by answering a malicious video call, achieving zero-click RCE on Android
- **AI Agent Prompt Injection (Mind Viruses)**: Self-propagating payloads spreading between autonomous AI agents through editable system prompt files carrying state between sessions
- **Rotating Domain Infrastructure (MacSync Stealer)**: 30+ web domains correlated across endpoint and network behaviors for payload retrieval, data staging, and exfiltration
- **Ransomware-Affiliate Impersonation (Ransom Busters)**: Threat actor posing as incident-recovery service to divert ransom payments, offering to delete data from ransomware gang servers for $20k-$60k
- **Critical Infrastructure Targeting (Medusa)**: Systematic breach of 500+ critical infrastructure organizations across sectors since June 2021
- **Near-Autonomous AI Attack Framework**: Chinese-language operator using complex AI framework for automated targeting and compromise of government agencies

## Threat Actor Activities

- **Medusa Ransomware Gang**: Breached over 500 critical infrastructure organizations in the United States since June 2021; FBI-confirmed campaign targeting essential services across multiple sectors
- **Clop Ransomware Gang**: Deploys custom Windchill web shells for targeted engineering data theft; focuses on PLM systems containing intellectual property; web shell includes credential decryption and vault mapping capabilities
- **MacSync Stealer Operators**: macOS-focused information stealer infrastructure using 30+ rotating domains; Microsoft Defender Experts correlated endpoint and network behaviors across changing infrastructure
- **China-Linked APT Operator**: Demonstrated near-autonomous AI-driven attack framework targeting government agencies in APAC (likely Taiwan); first purported "near-autonomous" nation-state attack
- **Ransom Busters Affiliate**: Ransomware affiliate posing as incident-recovery service; proactively emails victims offering to delete stolen data from ransomware servers for $20,000-$60,000; anomalous extortion model
- **TWINLOOT Operators**: Deploy modular PyArmor-hardened Python implant operating entirely within Microsoft trusted services; uses SharePoint Online file operations and Teams/Graph API for C2; steals credentials and achieves persistence
- **City Forum Campaign Actor**: Single infrastructure (158.220.87.79) scraping Salesforce and ServiceNow customer portals across multiple industries since 2025; named after domain tied to attacker's IP
- **StubMaker Operators**: Typosquatting campaign on RubyGems publishing 16 malicious packages delivering Windows information stealers; discovered August 15, 2026 by OpenSourceMalware
- **Azure Data Threat Actor**: Selling 3.6 million employee records allegedly stolen from Microsoft Azure infrastructure of multiple Fortune 500 companies; initial access via compromised credentials