---
schema_version: 2
report_date: 2026-08-19
generated_at: 2026-08-19T12:59:31Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-08-19/
---
# Exploitation Report

## Executive Summary

CISA has added multiple critical vulnerabilities to its Known Exploited Vulnerabilities catalog, confirming active exploitation of flaws in Apple macOS (CVE-2026-65400), Microsoft Windows IKE Extension, Ray distributed computing framework, and Windows Task Host. These vulnerabilities enable remote code execution, improper authentication bypass, and browser-based code execution, with ransomware gangs specifically leveraging the Windows Task Host flaw. The GitLab zero-click vulnerability (CVE-2026-19478) presents significant mitigation challenges due to limited technical disclosure.

Threat actor activity remains diverse and sophisticated. The Clop ransomware gang has deployed a custom Java web shell targeting PTC Windchill and FlexPLM servers to decrypt credentials and exfiltrate engineering data. The Medusa ransomware operation has compromised over 500 critical infrastructure organizations since June 2021. A China-linked operator demonstrated near-autonomous AI-driven attacks against government agencies in the APAC region, while the TWINLOOT framework operates entirely within Microsoft's cloud ecosystem abusing SharePoint and Teams for command and control. The Ransom Busters affiliate has adopted a novel extortion model posing as an incident recovery service.

Supply chain and infrastructure compromise campaigns are escalating. The StopAndProtect operation leverages nearly 2,000 hacked WordPress sites as a distributed malware delivery platform. A persistent attacker has scraped Salesforce and ServiceNow portals across multiple industries since 2025 using infrastructure tied to the "City Forum" campaign. Typosquatted RubyGems packages (StubMaker campaign) target developers with credential and cryptocurrency wallet stealers, while MLflow SSRF flaws are being actively exploited to harvest cloud credentials and secrets from AI/ML workloads.

## Active Exploitation Details

### Apple macOS Improper Authentication Vulnerability
- **Description**: An improper authentication vulnerability in Apple macOS that could allow an attacker to bypass authentication mechanisms and gain unauthorized access to affected systems.
- **Impact**: Attackers can achieve unauthorized system access, potentially leading to full device compromise, data theft, and lateral movement within enterprise environments.
- **Status**: Actively exploited in the wild; added to CISA KEV catalog on August 12, 2026. Patch availability not specified in source.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-65400
- **Reporting**: [The Hacker News — Critical macOS, SharePoint, vCenter, and Microsoft IKE Flaws Under Active Exploitation](https://thehackernews.com/2026/08/critical-macos-sharepoint-vcenter-and.html)

### Microsoft Windows IKE Extension Remote Code Execution
- **Description**: A critical-severity remote code execution flaw in the Windows Internet Key Exchange (IKE) Service Extensions component that allows unauthenticated attackers to execute arbitrary code.
- **Impact**: Remote code execution with system-level privileges, enabling complete system compromise without user interaction.
- **Status**: Actively exploited in attacks; CISA has issued warning. Patch availability not specified in source.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-65400
- **Reporting**: [Bleeping Computer — Critical RCE flaw in Windows IKE Extension now actively exploited](https://www.bleepingcomputer.com/news/security/cisa-critical-windows-ike-extension-flaw-now-exploited-in-attacks/), [The Hacker News — Critical macOS, SharePoint, vCenter, and Microsoft IKE Flaws Under Active Exploitation](https://thehackernews.com/2026/08/critical-macos-sharepoint-vcenter-and.html)

### Ray Distributed Computing Framework Browser-Based RCE
- **Description**: A critical flaw in Ray, an open-source Python-native distributed computing framework for AI/ML workloads, that can trigger browser-based remote code execution.
- **Impact**: Attackers can achieve remote code execution through browser vectors, compromising AI/ML infrastructure and potentially accessing sensitive training data, models, and cloud credentials.
- **Status**: Actively exploited; added to CISA KEV catalog on August 11, 2026.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — CISA Flags Actively Exploited Ray Flaw That Can Trigger Browser-Based RCE](https://thehackernews.com/2026/08/cisa-flags-actively-exploited-ray-flaw.html)

### Windows Task Host Vulnerability
- **Description**: A high-severity vulnerability in Windows Task Host that was previously flagged as actively exploited in April 2026.
- **Impact**: Ransomware gangs are actively exploiting this flaw to gain initial access and deploy ransomware payloads across victim networks.
- **Status**: Confirmed exploited by ransomware gangs; CISA advisory issued.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — CISA: Windows Task Host flaw now exploited by ransomware gangs](https://www.bleepingcomputer.com/news/security/cisa-windows-task-host-flaw-now-exploited-by-ransomware-gangs/)

### GitLab Zero-Click Vulnerability
- **Description**: A critical zero-click flaw in self-managed GitLab instances that poses significant mitigation challenges due to lack of technical details in public disclosures.
- **Impact**: Potential zero-click compromise of GitLab servers, enabling source code theft, supply chain injection, and CI/CD pipeline manipulation.
- **Status**: Critical vulnerability with exploitation potential; limited technical details hinder detection and mitigation.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: investigate
- **CVE IDs**: CVE-2026-19478
- **Reporting**: [Dark Reading — Critical GitLab Zero-Click Flaw Poses Mitigation Challenges](https://www.darkreading.com/application-security/critical-gitlab-zero-click-flaw-mitigation-challenges)

### PTC Windchill and FlexPLM Critical Flaw
- **Description**: A critical security flaw in PTC Windchill and FlexPLM Product Lifecycle Management servers that enables deployment of a custom JavaServer Pages web shell.
- **Impact**: Attackers deploy a fully equipped extortion platform capable of decrypting credentials, mapping sensitive vault data, enumerating file repositories, and exfiltrating engineering intellectual property.
- **Status**: Actively exploited by Clop ransomware gang; custom web shell deployed post-exploitation.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Clop-Linked Windchill Web Shell Decrypts Credentials and Maps Engineering Data](https://thehackernews.com/2026/08/clop-linked-windchill-web-shell.html), [Bleeping Computer — Clop created custom web shell for Windchill data theft attacks](https://www.bleepingcomputer.com/news/security/clop-created-custom-web-shell-for-windchill-data-theft-attacks/)

### MLflow SSRF Vulnerability
- **Description**: A critical Server-Side Request Forgery vulnerability in MLflow, an open-source AI platform, being exploited to steal cloud credentials and secrets.
- **Impact**: Attackers can access internal cloud metadata services, extract credentials, API keys, and secrets from MLflow deployments, compromising entire ML pipelines and associated cloud infrastructure.
- **Status**: Malicious scanning and exploitation observed by watchTowr and VulnCheck.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Attackers Exploit MLflow SSRF Flaw to Steal Cloud Credentials and Secrets](https://thehackernews.com/2026/08/attackers-exploit-mlflow-ssrf-flaw-to.html)

### Microsoft Copilot Personal CoSnitch Vulnerabilities
- **Description**: Three vulnerabilities in Microsoft Copilot Personal (collectively named CoSnitch) involving an undocumented URL parameter that enables single-click data exfiltration from connected apps.
- **Impact**: A single click on a crafted link silently pulls data from connected applications and information available in the victim's Copilot session.
- **Status**: Disclosed by Varonis Threat Labs; exploitation status not confirmed in wild.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: investigate
- **Reporting**: [The Hacker News — Microsoft Copilot Personal Flaws Could Let One Click Exfiltrate Data From Connected Apps](https://thehackernews.com/2026/08/microsoft-copilot-personal-flaws-could.html), [Dark Reading — 'CoSnitch' Attack Tricked Copilot into Mapping Out Architecture](https://www.darkreading.com/vulnerabilities-threats/cosnitch-attack-copilot-mapping-out-architecture)

### FUXA SCADA/HMI Vulnerability
- **Description**: A critical vulnerability in FUXA, an open-source web-based SCADA/HMI software for operational technology and industrial automation.
- **Impact**: Potential compromise of industrial control systems, enabling manipulation of OT environments and critical infrastructure.
- **Status**: Malicious scanning and exploitation efforts observed alongside MLflow attacks.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Attackers Exploit MLflow SSRF Flaw to Steal Cloud Credentials and Secrets](https://thehackernews.com/2026/08/attackers-exploit-mlflow-ssrf-flaw-to.html)

### StopAndProtect WordPress Compromise Campaign
- **Description**: A global cybercrime operation abusing nearly 2,000 hacked WordPress websites as infrastructure for malware distribution, command and control, and data staging.
- **Impact**: Large-scale malware dissemination, host compromise, credential theft, and persistent infrastructure for criminal operations using a toolkit of criminal software.
- **Status**: Active operation with thousands of compromised sites serving as infrastructure.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — StopAndProtect Uses Nearly 2,000 Hacked WordPress Sites to Spread Malware and Steal Data](https://thehackernews.com/2026/08/stopandprotect-uses-nearly-2000-hacked.html)

### StubMaker Typosquatting Campaign (RubyGems)
- **Description**: A typosquatting campaign publishing 16 malicious RubyGems packages that deploy a Windows-based information stealer targeting browser credentials and cryptocurrency wallets.
- **Impact**: Developer credential theft, cryptocurrency wallet drainage, and potential supply chain compromise through compromised development environments.
- **Status**: Active campaign discovered August 15, 2026; packages published to RubyGems registry.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — 16 Typosquatted RubyGems Packages Steal Browser Credentials and Crypto Wallets](https://thehackernews.com/2026/08/16-typosquatted-rubygems-packages-steal.html)

### SafePal Authorization Flaw
- **Description**: An authorization flaw in an order-tracking plug-in that exposed customer PII including names, emails, shipping addresses, phone numbers, and purchase details.
- **Impact**: Data exposure of approximately 39,798 hardware wallet customers; not confirmed as actively exploited but data was accessible.
- **Status**: Disclosed by vendor; affected customers notified.
- **Severity**: medium
- **Exploitation Status**: observed
- **Action**: monitor
- **Reporting**: [The Hacker News — SafePal Hardware Wallet Maker Says Flaw Exposed Data of Nearly 40,000 Customers](https://thehackernews.com/2026/08/safepal-hardware-wallet-maker-says-flaw.html)

## Affected Systems and Products

- **Apple macOS**: Systems vulnerable to CVE-2026-65400 improper authentication flaw; specific versions not detailed in source
- **Microsoft Windows**: Windows IKE Service Extensions component (all supported versions potentially affected); Windows Task Host component exploited by ransomware gangs
- **Ray Distributed Computing Framework**: Open-source Python-native framework for AI/ML workloads; GitHub project with 30k+ stars; browser-based RCE vector
- **GitLab Self-Managed Instances**: All self-managed versions potentially affected by CVE-2026-19478 zero-click flaw; detection challenging due to limited technical details
- **PTC Windchill and FlexPLM**: Enterprise Product Lifecycle Management servers; specific versions not detailed; targeted by Clop ransomware gang
- **MLflow**: Open-source AI/ML platform deployments; SSRF flaw enables cloud credential theft
- **FUXA SCADA/HMI**: Open-source web-based industrial automation software; OT environments at risk
- **Microsoft Copilot Personal**: Consumer-facing Copilot assistant; three CoSnitch vulnerabilities enabling data exfiltration
- **WordPress**: Nearly 2,000 compromised sites used as malware distribution infrastructure in StopAndProtect operation
- **RubyGems Registry**: 16 typosquatted packages (ubnuler, ubnlder, ri18nr, reaker, rakier, orakw, joxn, and others) distributing Windows info stealer
- **SafePal Hardware Wallet Order Tracking**: Plug-in authorization flaw exposing ~39,798 customer records
- **Salesforce and ServiceNow Customer Portals**: Scraped by single attacker infrastructure (158.220.87.79) since 2025 across multiple industries

## Attack Vectors and Techniques

- **Improper Authentication Bypass**: CVE-2026-65400 in macOS allows authentication circumventing without credentials
- **Remote Code Execution via IKE Extension**: Unauthenticated RCE through Windows Internet Key Exchange Service Extensions
- **Browser-Based RCE**: Ray framework flaw triggers code execution through web browser vectors targeting AI/ML workloads
- **Zero-Click Exploitation**: GitLab CVE-2026-19478 requires no user interaction for potential compromise
- **Web Shell Deployment**: Custom JSP/Java web shells deployed post-exploitation on Windchill/FlexPLM servers with built-in credential decryption and data enumeration
- **Server-Side Request Forgery**: MLflow SSRF flaw abuses internal metadata services to extract cloud credentials and secrets
- **AI-Assisted Autonomous Attack**: China-linked operator used complex AI framework for near-autonomous compromise of government agencies
- **Living-Off-The-Land in Microsoft Cloud**: TWINLOOT operates C2 entirely within SharePoint Online and Teams, using trusted Microsoft services for tasking and exfiltration
- **Supply Chain Compromise**: StopAndProtect leverages 2,000+ hacked WordPress sites as distributed malware infrastructure
- **Typosquatting Supply Chain Attack**: 16 malicious RubyGems packages mimic legitimate library names to target developers
- **Single-Click Data Exfiltration**: CoSnitch vulnerabilities in Copilot Personal use undocumented URL parameters for silent data theft
- **Credential Scraping at Scale**: Persistent infrastructure scraping Salesforce and ServiceNow portals across industries for over a year
- **Ransomware Double Extortion**: Medusa ransomware encrypts and exfiltrates data from 500+ critical infrastructure organizations
- **Fake Recovery Service Extortion**: Ransom Busters affiliate poses as incident recovery to divert ransom payments
- **AI Agent Prompt Injection**: Self-propagating "mind viruses" spread between AI agents through persistent prompt files

## Threat Actor Activities

- **Clop Ransomware Gang**: Deployed custom Java web shell for Windchill/FlexPLM; decrypts credentials, maps engineering vaults, exfiltrates PLM data; linked to extortion operations
- **Medusa Ransomware Gang**: Breached 500+ critical infrastructure organizations in US since June 2021; FBI-confirmed campaign; double extortion model
- **China-Linked APT Operator**: Demonstrated near-autonomous AI-driven attack framework targeting government agencies in APAC (likely Taiwan); first purported "near-autonomous" nation-state attack
- **TWINLOOT Operators**: Modular PyArmor-hardened Python implant framework; operates C2 entirely within Microsoft SharePoint Online and Teams; steals credentials, achieves persistence, moves laterally
- **Ransom Busters Affiliate**: Novel extortion model posing as incident recovery service; contacts victims directly offering to delete stolen data for $20,000-$60,000; identified by GuidePoint Research
- **StopAndProtect Operators**: Global cybercrime operation managing ~2,000 hacked WordPress sites as distributed infrastructure; uses toolkit of criminal software for malware distribution and data staging
- **City Forum Campaign Actor**: Single infrastructure (158.220.87.79) scraping Salesforce and ServiceNow portals across multiple industries since 2025; tracked by Reco
- **StubMaker Campaign Operators**: Typosquatting campaign publishing 16 malicious RubyGems packages; deploys Windows info stealer targeting browser credentials and crypto wallets; discovered by OpenSourceMalware
- **MLflow/FUXA Exploitation Actors**: Active scanning and exploitation of AI/ML and OT platforms; observed by watchTowr and VulnCheck; targeting cloud credentials and industrial systems
- **MacSync Stealer Operators**: macOS-focused information stealer using 30+ rotating domains for infrastructure; tracked by Microsoft Defender Experts through endpoint and network behavior correlation