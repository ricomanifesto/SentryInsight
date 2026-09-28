---
schema_version: 2
report_date: 2026-09-28
generated_at: 2026-09-28T18:27:53Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-28/
---
# Exploitation Report

## Executive Summary

Critical exploitation activity this period centers on two distinct zero-day campaigns targeting enterprise infrastructure. Citrix NetScaler ADC and Gateway appliances face active exploitation of two remote code execution vulnerabilities (CVE-2026-88771 and CVE-2026-88772), prompting CISA to add both to the Known Exploited Vulnerabilities catalog and mandate federal patching within days. Simultaneously, the ShinyHunters extortion group has resumed mass exploitation of the Oracle PeopleSoft flaw CVE-2026-35273 (CVSS 9.8), employing a URL-encoding technique to bypass web application firewall protections and deploy web shells across multiple sectors globally.

Cloud and AI-focused threats have escalated significantly. The JadePuffer ransomware operator—tracked by Microsoft as Storm-3168—has evolved to use agentic AI-driven attacks against Azure tenants, leveraging compromised service principals to conduct reconnaissance, steal credentials, and destroy core cloud resources including storage, applications, and databases over an 18-hour destructive spree. Separately, infostealer malware has harvested AI platform credentials from over 80,000 corporate domains, fueling a growing "LLMjacking" market, while the Carbonato botnet compromises exposed Docker daemons to deploy the Hermes AI agent framework under Telegram command-and-control.

Supply chain and browser-based threats round out the landscape. A malicious Chrome extension masquerading as an ad blocker ("Poper Blocker") exfiltrated sensitive data from millions of users while bearing Google's store approval. The Mini Shai-Hulud campaign maintained persistent malicious payloads in re-enabled GitHub Actions for over a week. Lunex Stealer (distributed as Psychedelic Stealer via compromised Ukrainian sites) abuses a legitimate AMD driver to disable security monitoring and harvest browser credentials. CISA also added actively exploited flaws in Microsoft SharePoint (CVE-2026-65660) and MikroTik RouterOS to the KEV catalog, and Cloudflare patched a cross-tenant data exposure in Containers.

## Active Exploitation Details

### Citrix NetScaler ADC/Gateway RCE Zero-Days (CVE-2026-88771, CVE-2026-88772)
- **Description**: Two critical remote code execution vulnerabilities in Citrix NetScaler ADC and NetScaler Gateway. CVE-2026-88771 (CVSS 9.5) is an improper input validation flaw allowing unauthenticated attackers to execute arbitrary code. CVE-2026-88772 is a companion RCE zero-day. One vulnerability affects every deployment on an affected version, including default configurations.
- **Impact**: Unauthenticated remote code execution leading to full appliance compromise, lateral movement, and potential data exfiltration or ransomware deployment.
- **Status**: Actively exploited in the wild as zero-days. Citrix has released security updates for both flaws. CISA added both to the Known Exploited Vulnerabilities catalog and ordered U.S. federal agencies to patch by September 30, 2026.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-88771, CVE-2026-88772
- **Reporting**: [The Hacker News — CISA Says Attackers Are Exploiting Two Critical Citrix NetScaler Flaws Globally](https://thehackernews.com/2026/09/cisa-says-attackers-are-exploiting-two.html), [Bleeping Computer — CISA orders feds to patch exploited Citrix flaws by Wednesday](https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-exploited-citrix-flaws-by-wednesday/), [Bleeping Computer — Citrix confirms two NetScaler RCE zero-days exploited in attacks](https://www.bleepingcomputer.com/news/security/citrix-admins-warned-to-shut-down-netscalers-over-2-exploited-zero-days/), [The Hacker News — Warning: Two Unpatched Citrix NetScaler RCE Zero-Days Under Active Exploitation](https://thehackernews.com/2026/09/warning-two-unpatched-citrix-netscaler.html)

### Oracle PeopleSoft Unauthenticated RCE (CVE-2026-35273)
- **Description**: Critical unauthenticated remote code execution vulnerability in Oracle PeopleSoft (CVSS 9.8). Originally exploited as a zero-day, the flaw has seen renewed mass exploitation after ShinyHunters developed a URL-encoding technique to bypass web application firewall mitigations.
- **Impact**: Unauthenticated remote code execution enabling web shell deployment, data theft, and persistent access to PeopleSoft applications handling sensitive HR, financial, and operational data.
- **Status**: Actively exploited in ongoing global campaign. WAF bypass technique allows exploitation despite prior mitigations. Oracle has released patches.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-35273
- **Reporting**: [Bleeping Computer — ShinyHunters uses WAF bypass trick in Oracle PeopleSoft attacks](https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/), [The Hacker News — Attackers Bypass WAFs to Exploit Oracle PeopleSoft Flaw and Deploy Web Shells](https://thehackernews.com/2026/09/attackers-bypass-wafs-to-exploit-oracle.html)

### Microsoft SharePoint Code Injection (CVE-2026-65660)
- **Description**: Code injection vulnerability in Microsoft Office SharePoint Server (CVSS 8.8) allowing remote code execution.
- **Impact**: Remote code execution in SharePoint environments, potentially leading to document theft, internal reconnaissance, and lateral movement.
- **Status**: Actively exploited in the wild. CISA added to Known Exploited Vulnerabilities catalog on September 26, 2026.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-65660
- **Reporting**: [The Hacker News — SharePoint RCE and MikroTik RouterOS Flaws Actively Exploited in the Wild](https://thehackernews.com/2026/09/sharepoint-rce-and-mikrotik-routeros.html)

### MikroTik RouterOS Flaw
- **Description**: Security flaw in MikroTik RouterOS actively exploited in the wild. Specific vulnerability details and CVE identifier not disclosed in source reporting.
- **Impact**: Compromise of routing infrastructure, potential traffic interception, network pivoting, and persistent access to organizational networks.
- **Status**: Actively exploited. CISA added to Known Exploited Vulnerabilities catalog on September 26, 2026.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — SharePoint RCE and MikroTik RouterOS Flaws Actively Exploited in the Wild](https://thehackernews.com/2026/09/sharepoint-rce-and-mikrotik-routeros.html)

### Elementor Website Builder CSRF
- **Description**: High-severity cross-site request forgery (CSRF) vulnerability in the Elementor Website Builder WordPress plugin (CVSS 8.8). Allows unauthenticated attackers to create rogue administrator accounts and take full control of a site when an administrator clicks a crafted link. No CVE identifier assigned at time of reporting.
- **Impact**: Full site takeover via administrator account creation, leading to content manipulation, malware distribution, and potential supply chain compromise.
- **Status**: Vulnerability disclosed with proof-of-concept. Affects specific versions (details in source). No CVE assigned yet.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — Elementor CSRF Flaw Lets Attackers Take Over Sites After Admin Clicks Crafted Link](https://thehackernews.com/2026/09/elementor-csrf-flaw-lets-attackers-take.html)

### Cloudflare Containers Cross-Tenant Data Exposure
- **Description**: Vulnerability in Cloudflare Containers and Sandboxes allowing customers with a Workers Paid account to recover residual data from other customers' containers on the same physical host.
- **Impact**: Cross-tenant data exposure in multi-tenant container environment, potentially leaking sensitive application data, secrets, or code.
- **Status**: Fixed by Cloudflare. No indication of active exploitation in source reporting.
- **Severity**: medium
- **Exploitation Status**: not_observed
- **Action**: patch
- **Reporting**: [Bleeping Computer — Cloudflare fixes Containers cross-tenant flaw exposing customer data](https://www.bleepingcomputer.com/news/security/cloudflare-fixes-containers-cross-tenant-flaw-exposing-customer-data/)

### Poper Blocker Chrome Extension Spyware
- **Description**: Malicious Chrome extension masquerading as an ad blocker ("Poper Blocker") hosted on the official Chrome Web Store. Exfiltrates sensitive user data including browsing history, cookies, authentication tokens, and personally identifiable information. Downloaded by millions of users benefiting from Google's store approval.
- **Impact**: Mass credential theft, session hijacking, privacy violation, and potential account takeover for millions of browser users.
- **Status**: Active in Chrome Web Store at time of reporting. Google's response not detailed in source.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Dark Reading — Chrome Store Hosts 'Poper Blocker' Spyware Downloaded by Millions](https://www.darkreading.com/application-security/chrome-store-poper-blocker-spyware-downloaded-millions)

### Carbonato Botnet Docker Compromise
- **Description**: Botnet malware targeting exposed Docker daemons to deploy the Hermes AI agent framework. The implant installs the framework unchanged, then overwrites its SOUL.md persona file with a 39-line prompt directing it to execute tasks received through Telegram command-and-control.
- **Impact**: Unauthorized AI agent deployment on compromised hosts, resource hijacking, potential lateral movement, and persistent backdoor via Telegram C2.
- **Status**: Active campaign disclosed by ThreatDown researchers.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Carbonato Botnet Compromises Docker Hosts to Deploy Telegram-Controlled Hermes AI Agent](https://thehackernews.com/2026/09/carbonato-botnet-compromises-docker.html)

### Lunex / Psychedelic Stealer AMD Driver Abuse
- **Description**: Malware-as-a-service platform (Lunex) distributing Psychedelic Stealer via compromised Ukrainian websites using ClickFix-style Cloudflare verification checks. Abuses a legitimate AMD driver to disable security monitoring (EDR/AV) and steal browser credentials, cookies, and cryptocurrency wallet data.
- **Impact**: Security control bypass, credential theft, financial fraud, and persistent compromise of Ukrainian-speaking targets.
- **Status**: Active four-stage attack chain observed by Ontinue researchers.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Lunex Stealer Abuses AMD Driver to Disable Security Monitoring and Steal Browser Credentials](https://thehackernews.com/2026/09/lunex-stealer-abuses-amd-driver-to.html)

### GitHub Actions Mini Shai-Hulud Supply Chain
- **Description**: Two third-party GitHub Actions compromised in a Mini Shai-Hulud campaign were re-enabled by their maintainer and remained accessible for more than a week despite still pointing to malicious code.
- **Impact**: Supply chain compromise affecting downstream repositories using the poisoned actions, potential credential theft, and malicious code execution in CI/CD pipelines.
- **Status**: Malicious payloads remained active for over a week after re-enabling.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — GitHub Actions re-enabled with Mini Shai-Hulud payload still active](https://www.bleepingcomputer.com/news/security/github-actions-re-enabled-with-mini-shai-hulud-payload-still-active/)

### AI Credential Theft and LLMjacking
- **Description**: Infostealer logs exposed AI account credentials and sessions tied to more than 80,000 corporate domains. Stolen credentials enable unauthorized access to AI platforms, conversation history theft, and "LLMjacking"—the resale of compromised AI model access.
- **Impact**: Intellectual property theft, sensitive conversation exposure, unauthorized AI compute consumption, and financial loss from resold API access.
- **Status**: Large-scale credential exposure documented by SOCRadar; active underground market for stolen AI logins.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — 80,000+ Organizations Had AI Logins Stolen: From Shadow AI to LLMjacking](https://www.bleepingcomputer.com/news/security/80-000-plus-organizations-had-ai-logins-stolen-from-shadow-ai-to-llmjacking/)

## Affected Systems and Products

- **Citrix NetScaler ADC and Gateway**: All deployments on affected versions, including default configurations. Specific version details in Citrix security bulletins.
- **Oracle PeopleSoft**: Vulnerable versions subject to CVE-2026-35273 exploitation. WAF mitigations bypassed via URL encoding.
- **Microsoft SharePoint Server**: Versions affected by CVE-2026-65660 code injection vulnerability.
- **MikroTik RouterOS**: Affected versions not specified in source; actively exploited in the wild.
- **Microsoft Azure**: Azure tenants targeted via compromised service principals (Entra ID / Azure AD identities).
- **Docker**: Exposed Docker daemons (unauthenticated API access) targeted by Carbonato botnet.
- **Elementor Website Builder WordPress Plugin**: Specific vulnerable versions detailed in source; no CVE assigned.
- **Google Chrome / Chromium-based browsers**: Users who installed "Poper Blocker" extension from Chrome Web Store.
- **AMD GPU Drivers**: Legitimate driver abused by Lunex Stealer to disable security monitoring (specific driver versions not disclosed).
- **GitHub Actions**: Two specific third-party actions compromised in Mini Shai-Hulud campaign (names not disclosed in source).
- **AI Platforms**: OpenAI, Anthropic, and other AI service credentials stolen via infostealers across 80,000+ corporate domains.
- **Cloudflare Containers and Sandboxes**: Workers Paid accounts affected by cross-tenant residual data exposure (now fixed).
- **Kiteworks (formerly Accellion)**: Systems targeted by credible threat intelligence; customers urged to shut down for 9-hour window.

## Attack Vectors and Techniques

- **Compromised Service Principals**: JadePuffer/Storm-3168 leveraged compromised Azure service principals (machine identities) to authenticate, conduct reconnaissance, steal credentials, and execute destructive deletion of storage, applications, and databases over ~18 hours.
- **Exposed Docker Daemons**: Carbonato botnet scans for and compromises unauthenticated Docker API endpoints to deploy Hermes AI agent framework with Telegram C2.
- **WAF Bypass via URL Encoding**: ShinyHunters uses URL-encoding trick to bypass web application firewall rules mitigating CVE-2026-35273, enabling continued Oracle PeopleSoft exploitation.
- **Legitimate Driver Abuse (BYOVD)**: Lunex Stealer abuses a signed AMD driver to disable endpoint security monitoring (EDR/AV) before credential theft—a Bring Your Own Vulnerable Driver technique.
- **ClickFix Social Engineering**: Psychedelic Stealer distribution via compromised Ukrainian websites using fake Cloudflare verification/CAPTCHA pages to trick users into executing malicious commands.
- **Malicious Browser Extension**: Poper Blocker extension uses Chrome Web Store legitimacy and broad permissions to exfiltrate browsing data, cookies, and tokens from millions of users.
- **Supply Chain Compromise (GitHub Actions)**: Mini Shai-Hulud campaign compromised third-party GitHub Actions; maintainers re-enabled them with malicious payloads still active for over a week.
- **Infostealer Credential Harvesting**: Large-scale collection of AI platform credentials (API keys, session tokens) from infected machines, fueling LLMjacking resale market.
- **Zero-Day Remote Code Execution**: Unauthenticated RCE exploitation of Citrix NetScaler (CVE-2026-88771, CVE-2026-88772) and Oracle PeopleSoft (CVE-2026-35273) in default/exposed configurations.
- **Cross-Site Request Forgery**: Elementor CSRF flaw enables rogue administrator account creation via crafted link clicked by site admin.
- **Cross-Tenant Container Data Recovery**: Cloudflare Containers flaw allowed paid Workers customers to access residual data from other tenants' containers on shared physical hosts.

## Threat Actor Activities

- **JadePuffer / Storm-3168**: Agentic AI-driven ransomware operator targeting Microsoft Azure tenants. Uses compromised service principals for initial access, conducts automated reconnaissance and credential theft, and executes destructive wiping of cloud resources (storage, apps, databases). Tracked by Microsoft as Storm-3168; attack observed in early June 2026 over ~18 hours. Represents evolution to "agentic threat actor" tradecraft.
- **ShinyHunters**: Prolific data theft and extortion group. Resumed mass exploitation of Oracle PeopleSoft CVE-2026-35273 using WAF bypass technique. Linked to theft of highly sensitive data from FBI and extortion of Russian ransomware group Cl0p following arrest of a 23-year-old member by Dutch police. Uses URL-encoding trick for WAF evasion.
- **North Korean State-Sponsored Actors (likely Lazarus Group)**: Suspected breach of Bitget cryptocurrency exchange resulting in $387.5 million theft (over $350M in Bitcoin). Bitget suspended and later resumed withdrawals.
- **Carbonato Botnet Operators**: Deploy Hermes AI agent framework via compromised Docker daemons with Telegram-based command-and-control. Uses prompt injection (SOUL.md overwrite) to direct AI agent behavior.
- **Lunex MaaS Operators**: Malware-as-a-service platform distributing Psychedelic Stealer. Targets Ukrainian-speaking users via compromised websites and ClickFix lures. Uses AMD driver abuse (BYOVD) to disable security tools.
- **Mini Shai-Hulud Campaign Operators**: Supply chain attackers compromising third-party GitHub Actions. Maintainers re-enabled compromised actions with malicious payloads still present for over a week.
- **U.S. Army Soldier (Convicted)**: Sentenced to 70 months for hacking and extorting at least 10 U.S. technology and telecommunications companies (including AT&T, Verizon) between April 2023–December 2024. Stole mobile call/text metadata for 100M+ AT&T customers. Ordered to pay ~$300K restitution.
- **Kiteworks Threat Actor (Unidentified)**: Credible threat intelligence from U.S. federal authorities indicated imminent targeting of Kiteworks (Accellion) systems, prompting 9-hour precautionary shutdown recommendation for customers.