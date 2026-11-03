---
schema_version: 2
report_date: 2026-09-23
generated_at: 2026-09-23T21:25:58Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-23/
---
# Exploitation Report

## Executive Summary

Active exploitation of critical zero-day and recently disclosed vulnerabilities has intensified across multiple vendor platforms in September 2026. Chinese threat actor UTA0565 chained three zero-days across Google Chrome and Microsoft Windows to deploy CLEANGULP malware, while separate campaigns actively exploit pre-authentication RCE flaws in Check Point Security Gateway VPN (CVE-2026-85102), F5 BIG-IP APM OAuth servers (CVE-2026-94127), and WordPress (CVE-2026-87902).

A MikroTik RouterOS SSH vulnerability chain (CVE-2026-67279 + CVE-2026-86060) enables passwordless administrative takeover of internet-exposed devices. Simultaneously, supply chain attacks have compromised the HashiCorp Registry with malicious Terraform providers, the npm/PyPI ecosystems with trojanized MemTensor packages, and GitLab's email-based issue submission workflow. An unpatched Ubuntu container escape (CVE-2026-80521) has a public exploit while vendor patches lag upstream fixes.

## Active Exploitation Details

### Check Point Security Gateway VPN RCE
- **Description**: Pre-authentication remote code execution vulnerability in the VPN certificate-handling functionality of Check Point Security Gateway products.
- **Impact**: Unauthenticated attackers can achieve remote code execution on affected Security Gateway appliances.
- **Status**: Actively exploited in the wild; Check Point has confirmed exploitation and released advisories.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-85102
- **Reporting**: [Bleeping Computer — Check Point warns of hackers exploiting Security Gateway VPN RCE flaw](https://www.bleepingcomputer.com/news/security/check-point-warns-of-hackers-exploiting-security-gateway-vpn-rce-flaw/)

### WordPress Critical Code Execution Flaw
- **Description**: Critical vulnerability in WordPress allowing attackers to write executable files to disk that run shell commands when accessed.
- **Impact**: Remote code execution on vulnerable WordPress sites; threat actors have moved from probing to active exploitation.
- **Status**: Active exploitation confirmed; patches available.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-87902
- **Reporting**: [Bleeping Computer — Hackers start exploiting critical WordPress flaw for code execution](https://www.bleepingcomputer.com/news/security/hackers-start-exploiting-critical-wordpress-flaw-for-code-execution/)

### MikroTik RouterOS SSH Chain (MikroTrick)
- **Description**: Two chained vulnerabilities in MikroTik RouterOS SSH: an SSH state-machine flaw (CVE-2026-67279) combined with an argument-injection bug in the login process (CVE-2026-86060). The chain allows full administrative control without password, SSH key, or completed authentication.
- **Impact**: Complete takeover of internet-exposed MikroTik routers; attack logs date back to earlier activity.
- **Status**: Actively exploited in the wild; CERT Polska tracks the chain as "MikroTrick."
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-67279, CVE-2026-86060
- **Reporting**: [The Hacker News — MikroTrick Chain Let Attackers Take Over MikroTik Routers Without a Password or SSH Key](https://thehackernews.com/2026/09/mikrotrick-chain-let-attackers-take.html)

### Ubuntu Linux AF_UNIX Container Escape
- **Description**: Use-after-free in the Linux kernel's AF_UNIX socket subsystem enabling container escape to host root. Fixed upstream on August 6, 2026, but Ubuntu has not shipped patches for 26.04, 24.04, or 22.04 LTS releases.
- **Impact**: Attackers with container access can escape to host and gain root privileges.
- **Status**: Public exploit released; Ubuntu LTS releases remain unpatched despite upstream fix.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: mitigate
- **CVE IDs**: CVE-2026-80521
- **Reporting**: [The Hacker News — Exploit Released for Unpatched Ubuntu Linux Flaw Enabling Host-Root Container Escape](https://thehackernews.com/2026/09/exploit-released-for-unpatched-ubuntu.html)

### F5 BIG-IP APM Zero-Day RCE
- **Description**: Critical zero-day in F5 BIG-IP Access Policy Manager (APM) when configured as an OAuth authorization server. Allows unauthenticated remote code execution on the BIG-IP system.
- **Impact**: Unauthenticated RCE on BIG-IP systems serving as OAuth servers; actively exploited before patch release.
- **Status**: Actively exploited; F5 released engineering hotfixes on September 22, 2026.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-94127
- **Reporting**: [The Hacker News — F5 Patches Critical BIG-IP APM Zero-Day Exploited for Unauthenticated RCE on OAuth Servers](https://thehackernews.com/2026/09/f5-patches-critical-big-ip-apm-zero-day.html), [Bleeping Computer — F5 patches BIG-IP APM zero-day flaw exploited in RCE attacks](https://www.bleepingcomputer.com/news/security/f5-warns-of-big-ip-apm-remote-code-execution-zero-day-exploited-in-attacks/)

### Chrome-Windows Zero-Day Exploit Chain (UTA0565)
- **Description**: Chinese threat actor UTA0565 exploited a chain of three zero-days—two in Google Chrome (CVE-2026-85046, CVE-2026-87491) and one in Windows Advanced Local Procedure Call (CVE-2026-85880)—via fake websites to deploy CLEANGULP malware.
- **Impact**: Full compromise via browser-to-kernel exploit chain; malware deployment on targeted systems.
- **Status**: Exploited as zero-days on September 3–4, 2026; patches presumably underway or released by vendors.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-85046, CVE-2026-87491, CVE-2026-85880
- **Reporting**: [The Hacker News — Chinese Hackers Exploit Chrome-Windows Zero-Day Chain to Deploy CLEANGULP Malware](https://thehackernews.com/2026/09/chinese-hackers-exploit-chrome-windows.html)

### Arista VeloCloud Orchestrator Zero-Day
- **Description**: Zero-day vulnerability in VeloCloud Orchestrator (VCO) On-Prem deployments actively exploited before patch availability.
- **Impact**: Compromise of VCO management infrastructure; details limited in public reporting.
- **Status**: Actively exploited; Arista released security patches on September 22, 2026.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Arista patches actively exploited VeloCloud Orchestrator zero-day](https://www.bleepingcomputer.com/news/security/arista-patches-actively-exploited-velocloud-orchestrator-zero-day/)

### cPanel CalDAV/CardDAV Root RCE
- **Description**: Flaw in cPanel's CalDAV and CardDAV service allowing any hosting account holder to execute code as root and take full server control. A second bug in the WP Toolkit plugin permits cross-account database manipulation.
- **Impact**: Complete server compromise from a standard hosting account; lateral movement across hosted accounts.
- **Status**: cPanel released fixed versions for both issues on September 22, 2026; exploitation status not explicitly confirmed but high risk.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — New cPanel Flaw Lets a Hosting Account Run Code as Root, Take Full Server Control](https://thehackernews.com/2026/09/new-cpanel-flaw-lets-hosting-account_0272795595.html)

### Next.js ImageResponse Server Code Execution
- **Description**: Vulnerability in Next.js ImageResponse feature allowing server code execution via crafted SVG input when attacker-controlled values (e.g., URL parameters) are rendered into images.
- **Impact**: Remote code execution on Next.js applications using ImageResponse with user-supplied input.
- **Status**: Fixed by Vercel in version released September 22, 2026; no confirmed exploitation reported.
- **Severity**: critical
- **Exploitation Status**: not_observed
- **Action**: patch
- **Reporting**: [The Hacker News — Critical Next.js ImageResponse Flaw Can Lead to Server Code Execution via Crafted SVG Input](https://thehackernews.com/2026/09/critical-nextjs-imageresponse-flaw-can.html)

### GitLab Email Address Supply Chain Vector
- **Description**: Automatically assigned incoming email addresses in GitLab contain highly privileged access tokens. Leaked addresses allow attackers to push code and run CI/CD jobs as the victim user, including to protected branches.
- **Impact**: Supply chain compromise via credential theft; unauthorized code commits and CI/CD execution with victim's permissions.
- **Status**: Design flaw with active risk; no patch indicated—mitigation requires treating the email address as a secret.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: mitigate
- **Reporting**: [Dark Reading — GitLab Email Addresses Can Be Weaponized for Supply Chain Attacks](https://www.darkreading.com/application-security/gitlab-email-addresses-supply-chain-attacks), [The Hacker News — A Leaked GitLab Issue Email Address Lets Anyone Push Code and Run CI Jobs as You](https://thehackernews.com/2026/09/a-leaked-gitlab-issue-email-address.html)

### Malicious Terraform Providers on HashiCorp Registry
- **Description**: First observed use of HashiCorp's centralized Terraform Registry to distribute Go-based malware via two malicious Terraform providers and two Go modules (e.g., gocommunity-io/dockerd, kreuzwenker/...).
- **Impact**: Supply chain compromise of infrastructure-as-code pipelines; malware execution during Terraform runs.
- **Status**: Disclosed by Aikido; packages identified with download counts (e.g., 222 downloads for dockerd); no CVE assigned.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — Attackers Use Malicious Terraform Providers to Deliver Go Malware via HashiCorp Registry](https://thehackernews.com/2026/09/attackers-use-malicious-terraform.html)

### Compromised MemTensor Packages (npm/PyPI)
- **Description**: Legitimate MemTensor packages on npm and PyPI compromised to deliver sckit, a cross-platform Go-based credential stealer for Windows, Linux, and macOS.
- **Impact**: Credential theft across developer environments; platform-specific implants deployed via trusted package managers.
- **Status**: Reported by Aikido, SafeDep, Socket, and StepSecurity; affected versions identified.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — Compromised MemTensor Packages Deliver sckit Credential Stealer via npm and PyPI](https://thehackernews.com/2026/09/compromised-memtensor-packages-deliver.html)

### EDR Evasion via Process Parameter Poisoning
- **Description**: Technique injecting code into process initialization structures without using Windows APIs monitored by EDR tools, evading detection during process injection.
- **Impact**: Bypass of endpoint detection and response controls; stealthy code execution.
- **Status**: Technique disclosed; no CVE assigned; exploitation potential high against unpatched EDR configurations.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: mitigate
- **Reporting**: [Dark Reading — EDR Evasion Stack Helps Process Injection Slip Past Defenses](https://www.darkreading.com/endpoint-security/edr-evasion-stack-helps-process-injection-slip-past-defenses)

### AI Agent-Driven Skimming Campaign
- **Description**: Financially motivated threat actor using open-source AI agent frameworks to attack hundreds of online retailers at scale, injecting skimmers and stealing over 600,000 credit card records.
- **Impact**: Mass payment card theft; automated compromise of e-commerce platforms.
- **Status**: Active campaign observed; infrastructure and tactics documented.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Malicious AI agents steal 600K credit cards, infect 100+ sites with skimmers](https://www.bleepingcomputer.com/news/security/malicious-ai-agents-steal-600k-credit-cards-infect-100-plus-sites-with-skimmers/)

### Network Management Systems Under Attack
- **Description**: InfraTrust report indicates attackers increasingly targeting enterprise infrastructure management systems, with several critical vulnerabilities exploited before or shortly after vendor disclosure.
- **Impact**: Potential full control of network infrastructure, lateral movement, persistence.
- **Status**: Active exploitation of multiple undisclosed vulnerabilities; specific CVEs not enumerated in reporting.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — InfraTrust report warns network management systems under attack](https://www.bleepingcomputer.com/news/security/infratrust-report-warns-network-management-systems-under-attack/)

### Kubernetes/GCP Privilege Escalation via Config Connector
- **Description**: Confused deputy problem in Google Kubernetes Config Connector allows a limited-privilege Kubernetes user to escalate to organization-wide control via a single YAML file.
- **Impact**: Full GCP organization takeover from compromised cluster workload identity.
- **Status**: Research disclosure by Varonis; no active exploitation reported; mitigation requires IAM hardening.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: mitigate
- **Reporting**: [Bleeping Computer — How One Kubernetes YAML Can Hand Over a GCP Organization](https://www.bleepingcomputer.com/news/security/how-one-kubernetes-yaml-can-hand-over-a-gcp-organization/)

### Rogue External MFA Provider Credential Theft
- **Description**: Attack allowing privileged actors to register a rogue external MFA provider that intercepts user passwords during legitimate login flows.
- **Impact**: Credential harvesting bypassing MFA protections; requires initial privileged access.
- **Status**: Proof-of-concept demonstrated by researchers; no confirmed wild exploitation.
- **Severity**: medium
- **Exploitation Status**: potential
- **Action**: monitor
- **Reporting**: [Bleeping Computer — Rogue external MFA providers can steal passwords during logins](https://www.bleepingcomputer.com/news/security/rogue-external-mfa-providers-can-steal-passwords-during-logins/)

### CLOSEDQUORUM AI-Driven Malware
- **Description**: Windows malware (CLOSEDQUORUM) using up to four AI models in a voting mechanism to decide malicious actions (credential theft, browser password extraction, crypto wallet targeting) instead of traditional C2.
- **Impact**: Autonomous, resilient malware decision-making; potential evasion of static C2 analysis.
- **Status**: Public version non-functional; Talos has not observed full operational capability.
- **Severity**: medium
- **Exploitation Status**: not_observed
- **Action**: monitor
- **Reporting**: [The Hacker News — This Windows Malware is Built to Let Up to Four AI Models Vote on Its Next Move](https://thehackernews.com/2026/09/windows-malware-is-built-to-let-up-to.html)

## Affected Systems and Products

- **Check Point Security Gateway**: VPN certificate-handling component; all versions prior to patched releases.
- **WordPress**: Core installations vulnerable to CVE-2026-87902; specific version range not disclosed in reporting.
- **MikroTik RouterOS**: Devices with SSH exposed to internet; versions affected by CVE-2026-67279 and CVE-2026-86060.
- **Ubuntu Linux**: 26.04, 24.04, and 22.04 LTS releases lacking upstream kernel fix for CVE-2026-80521 (AF_UNIX use-after-free).
- **F5 BIG-IP APM**: Systems configured as OAuth authorization servers; vulnerable to CVE-2026-94127 prior to engineering hotfixes.
- **Google Chrome**: Versions prior to fixes for CVE-2026-85046 and CVE-2026-87491.
- **Microsoft Windows**: Versions vulnerable to ALPC flaw CVE-2026-85880.
- **Arista VeloCloud Orchestrator (VCO)**: On-Prem deployments prior to September 22, 2026 patches.
- **cPanel**: CalDAV/CardDAV service and WP Toolkit plugin; fixed versions released September 22, 2026.
- **Next.js**: Applications using ImageResponse with user-controlled input; fixed in version released September 22, 2026.
- **GitLab**: All instances using email-based issue submission; incoming email addresses function as high-privilege credentials.
- **HashiCorp Terraform Registry**: Users of malicious providers `gocommunity-io/dockerd`, `kreuzwenker/...` and associated Go modules.
- **npm/PyPI**: Consumers of compromised `@memtensor/memos-cloud-openclaw-plugin` and related MemTensor packages.
- **Enterprise Network Management Systems**: Multiple vendor platforms (per InfraTrust) with critical pre-disclosure exploitation.
- **Google Cloud Platform**: Organizations using Google Kubernetes Engine with Config Connector enabled.
- **E-commerce Platforms**: Hundreds of online retailers targeted by AI-agent skimming campaign.

## Attack Vectors and Techniques

- **Pre-authentication RCE via VPN Certificate Handling**: Unauthenticated network-level exploit against Check Point Security Gateway (CVE-2026-85102).
- **WordPress File Write to RCE**: Attackers write executable PHP/webshell files to disk via CVE-2026-87902, achieving code execution on access.
- **SSH State-Machine + Argument Injection Chain**: MikroTrick chains CVE-2026-67279 (SSH state desync) with CVE-2026-86060 (login argument injection) for passwordless root access.
- **Container Escape via Kernel Use-After-Free**: CVE-2026-80521 exploits AF_UNIX socket handling to break out of containers to host root.
- **OAuth Server RCE**: Unauthenticated code execution on F5 BIG-IP APM acting as OAuth authorization server (CVE-2026-94127).
- **Browser-to-Kernel Zero-Day Chain**: UTA0565 chains Chrome renderer exploits (CVE-2026-85046, CVE-2026-87491) with Windows ALPC elevation (CVE-2026-85880) via malicious websites.
- **Supply Chain Compromise (Terraform Registry)**: Malicious providers published to official HashiCorp Registry execute Go malware during `terraform init/apply`.
- **Supply Chain Compromise (Package Managers)**: Legitimate MemTensor maintainer accounts or build pipelines compromised to inject sckit stealer into npm/PyPI packages.
- **GitLab Email Token Abuse**: Leaked per-user incoming email addresses (containing scoped tokens) used to push code and trigger CI/CD as victim.
- **CalDAV/CardDAV Root Execution**: Authenticated cPanel user exploits DAV service flaw to execute commands as root on shared hosting servers.
- **Next.js SVG Deserialization**: Attacker-controlled text passed to ImageResponse rendered as SVG leads to server-side code execution.
- **AI-Agent Orchestrated Skimming**: Autonomous AI frameworks used to discover, exploit, and inject payment skimmers across hundreds of retailers at scale.
- **EDR Evasion via Parameter Poisoning**: Code injection into process initialization structures (e.g., PEB, environment blocks) bypassing API-hooking EDR sensors.
- **Rogue MFA Provider Registration**: Privileged attacker registers malicious external authentication provider to harvest credentials during legitimate logins.
- **Kubernetes Config Connector Confused Deputy**: Low-privilege K8s service account exploits excessive IAM bindings via Config Connector to seize GCP organization ownership.
- **Multi-Model AI Malware C2**: CLOSEDQUORUM uses ensemble voting of local LLMs for command decisions, reducing C2 infrastructure footprint.

## Threat Actor Activities

- **UTA0565 (Chinese Threat Actor)**: Exploited Chrome-Windows zero-day chain (CVE-2026-85046, CVE-2026-87491, CVE-2026-85880) on September 3–4, 2026, deploying CLEANGULP malware via fake websites. Attribution by The Hacker News / industry researchers.
- **ShinyHunters (Cyber Extortion Group)**: Claimed breach of U.S. FBI, asserting theft of sensitive data on nearly all FBI agents and job applicants. Posted claim on dark web; verification pending.
- **Ryuk Ransomware Affiliate**: Armenian national sentenced to 24 months imprisonment + 3 years supervised release for Ryuk attacks against U.S. companies; indicates ongoing law enforcement pressure on ransomware ecosystems.
- **Unknown Actors - Check Point Exploitation**: Active exploitation of CVE-2026-85102 confirmed by Check Point; no attribution provided.
- **Unknown Actors - WordPress Exploitation**: Threat actors moved from scanning to active exploitation of CVE-2026-87902; no specific group identified.
- **Unknown Actors - MikroTrick Campaign**: Internet-wide scanning and exploitation of MikroTik SSH chain; attack logs predate disclosure.
- **Unknown Actors - F5 BIG-IP APM Exploitation**: Active RCE attacks against OAuth-configured BIG-IP systems prior to September 22 patch.
- **Unknown Actors - Arista VeloCloud Exploitation**: Zero-day exploited in the wild against VCO On-Prem; no attribution.
- **Unknown Actors - Supply Chain (Terraform/npm/PyPI)**: Publishers of malicious Terraform providers and compromised MemTensor packages; infrastructure linked to Go-based malware distribution.
- **Financially Motivated AI Skimming Operator**: Leverages open-source AI agent frameworks for automated, large-scale e-commerce compromise and credit card theft (600K+ records).
- **Network Infrastructure Targeters**: Per InfraTrust, actors exploiting critical vulnerabilities in enterprise network management systems pre- or post-disclosure; possible espionage or access brokerage motive.