---
schema_version: 2
report_date: 2026-09-24
generated_at: 2026-09-24T04:11:21Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-24/
---
# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse technology stacks, ranging from network infrastructure and cloud platforms to content management systems and endpoint software. Chinese threat actor UTA0565 has weaponized a Chrome-Windows zero-day chain (CVE-2026-85046, CVE-2026-87491, CVE-2026-85880) to deploy CLEANGULP malware, while Check Point's Security Gateway VPN (CVE-2026-85102) and F5 BIG-IP APM (CVE-2026-94127) are being exploited for pre-authentication remote code execution. WordPress sites face active exploitation of CVE-2026-87902 for file write and shell command execution, and MikroTik routers are compromised via the chained "MikroTrick" vulnerabilities (CVE-2026-67279, CVE-2026-86060). An exploit has been published for an unpatched Ubuntu container escape flaw (CVE-2026-80521), creating immediate risk for containerized environments.

Supply chain and identity-based attacks are escalating in sophistication. Malicious Terraform providers and Go modules have infiltrated the HashiCorp Registry, while compromised MemTensor packages on npm and PyPI deliver the cross-platform sckit credential stealer. GitLab's automatically assigned issue email addresses function as high-privilege credentials that enable unauthorized code commits and CI/CD pipeline execution. A financially motivated actor leverages open-source AI agent frameworks to automate credit card skimming across 100+ retailer sites, harvesting 600,000+ payment records. The CLOSEDQUORUM malware demonstrates a novel AI-driven command architecture where multiple models vote on malicious actions, signaling an evolution in autonomous malware behavior.

Network management systems and cloud infrastructure are priority targets. Arista's VeloCloud Orchestrator On-Prem faces active exploitation of a zero-day, while a Kubernetes Config Connector confused-deputy issue allows organization-wide GCP takeover from a single YAML. cPanel's CalDAV/CardDAV service permits hosting accounts to execute code as root, and Next.js ImageResponse contains a critical SVG-based server code execution flaw. EDR evasion via process parameter-poisoning bypasses modern defenses without using monitored Windows APIs. ClickFix attacks now abuse the ubiquitous "third-party.com" placeholder domain to serve fake verification pages that trick users into executing PowerShell. RemControl Android banking MaaS spreads through malvertising impersonating legitimate IPTV apps, and rogue external MFA providers can intercept passwords during legitimate logins.

## Active Exploitation Details

### Check Point Security Gateway VPN RCE (CVE-2026-85102)
- **Description**: Pre-authentication remote code execution vulnerability in the VPN certificate-handling functionality of Check Point Security Gateway products.
- **Impact**: Attackers can achieve unauthenticated remote code execution on affected Security Gateway appliances, potentially leading to full device compromise and network pivoting.
- **Status**: Actively exploited in the wild; Check Point has confirmed exploitation and released advisories.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-85102
- **Reporting**: [Bleeping Computer — Check Point warns of hackers exploiting Security Gateway VPN RCE flaw](https://www.bleepingcomputer.com/news/security/check-point-warns-of-hackers-exploiting-security-gateway-vpn-rce-flaw/)

### WordPress Critical File Write and Code Execution (CVE-2026-87902)
- **Description**: Critical WordPress flaw allowing attackers to write arbitrary files to disk that execute shell commands when accessed via web requests.
- **Impact**: Full remote code execution on vulnerable WordPress installations, enabling site takeover, data theft, and use as a platform for further attacks.
- **Status**: Threat actors have moved from probing to active exploitation; patches available.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-87902
- **Reporting**: [Bleeping Computer — Hackers start exploiting critical WordPress flaw for code execution](https://www.bleepingcomputer.com/news/security/hackers-start-exploiting-critical-wordpress-flaw-for-code-execution/)

### MikroTrick Chain: MikroTik RouterOS SSH State-Machine Flaw (CVE-2026-67279)
- **Description**: SSH state-machine vulnerability in MikroTik RouterOS that forms the first link in the MikroTrick exploitation chain.
- **Impact**: When chained with CVE-2026-86060, allows attackers to gain full administrative control of Internet-exposed MikroTik routers without passwords, SSH keys, or completed authentication.
- **Status**: Attack logs confirm exploitation activity; chained with argument-injection bug for full takeover.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-67279
- **Reporting**: [The Hacker News — MikroTrick Chain Let Attackers Take Over MikroTik Routers Without a Password or SSH Key](https://thehackernews.com/2026/09/mikrotrick-chain-let-attackers-take.html)

### MikroTrick Chain: MikroTik RouterOS Argument-Injection Bug (CVE-2026-86060)
- **Description**: Argument-injection vulnerability in the RouterOS login process that forms the second link in the MikroTrick exploitation chain.
- **Impact**: Combined with CVE-2026-67279, enables passwordless administrative takeover of exposed MikroTik routers.
- **Status**: Actively exploited as part of MikroTrick chain; attack logs date to active campaigns.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-86060
- **Reporting**: [The Hacker News — MikroTrick Chain Let Attackers Take Over MikroTik Routers Without a Password or SSH Key](https://thehackernews.com/2026/09/mikrotrick-chain-let-attackers-take.html)

### Ubuntu Linux Kernel AF_UNIX Container Escape (CVE-2026-80521)
- **Description**: Use-after-free vulnerability in the Linux kernel's AF_UNIX socket subsystem allowing container escape to host root.
- **Impact**: Attackers inside a container can break out and gain root privileges on the host system, compromising all containers and the host.
- **Status**: Exploit publicly released; fixed upstream August 6, 2026, but Ubuntu has not patched 26.04, 24.04, or 22.04 LTS releases.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: mitigate
- **CVE IDs**: CVE-2026-80521
- **Reporting**: [The Hacker News — Exploit Released for Unpatched Ubuntu Linux Flaw Enabling Host-Root Container Escape](https://thehackernews.com/2026/09/exploit-released-for-unpatched-ubuntu.html)

### F5 BIG-IP APM OAuth Zero-Day RCE (CVE-2026-94127)
- **Description**: Critical zero-day in F5 BIG-IP Access Policy Manager (APM) when configured as an OAuth authorization server, enabling unauthenticated remote code execution.
- **Impact**: Unauthenticated attackers can execute arbitrary code on BIG-IP systems serving as OAuth authorization servers, leading to full appliance compromise.
- **Status**: Actively exploited in the wild; F5 released engineering hotfixes on September 22, 2026.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-94127
- **Reporting**: [The Hacker News — F5 Patches Critical BIG-IP APM Zero-Day Exploited for Unauthenticated RCE on OAuth Servers](https://thehackernews.com/2026/09/f5-patches-critical-big-ip-apm-zero-day.html), [Bleeping Computer — F5 patches BIG-IP APM zero-day flaw exploited in RCE attacks](https://www.bleepingcomputer.com/news/security/f5-warns-of-big-ip-apm-remote-code-execution-zero-day-exploited-in-attacks/)

### Chrome V8 Zero-Day (CVE-2026-85046)
- **Description**: Google Chrome vulnerability exploited as a zero-day in a chain targeting Windows systems.
- **Impact**: Part of a three-vulnerability chain enabling sandbox escape and remote code execution when victims visit malicious websites.
- **Status**: Actively exploited as zero-day by Chinese threat actor UTA0565 on September 3-4, 2026.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-85046
- **Reporting**: [The Hacker News — Chinese Hackers Exploit Chrome-Windows Zero-Day Chain to Deploy CLEANGULP Malware](https://thehackernews.com/2026/09/chinese-hackers-exploit-chrome-windows.html)

### Chrome V8 Zero-Day (CVE-2026-87491)
- **Description**: Second Google Chrome vulnerability in the zero-day exploit chain deployed by UTA0565.
- **Impact**: Combined with CVE-2026-85046 and CVE-2026-85880 to achieve full browser-to-kernel exploit chain for CLEANGULP malware deployment.
- **Status**: Actively exploited as zero-day in September 2026 attacks.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-87491
- **Reporting**: [The Hacker News — Chinese Hackers Exploit Chrome-Windows Zero-Day Chain to Deploy CLEANGULP Malware](https://thehackernews.com/2026/09/chinese-hackers-exploit-chrome-windows.html)

### Windows ALPC Zero-Day (CVE-2026-85880)
- **Description**: Windows Advanced Local Procedure Call (ALPC) vulnerability exploited as the final link in the Chrome-Windows zero-day chain.
- **Impact**: Enables privilege escalation from the Chrome sandbox to SYSTEM privileges, completing the exploit chain for malware deployment.
- **Status**: Actively exploited as zero-day by UTA0565 in early September 2026.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-85880
- **Reporting**: [The Hacker News — Chinese Hackers Exploit Chrome-Windows Zero-Day Chain to Deploy CLEANGULP Malware](https://thehackernews.com/2026/09/chinese-hackers-exploit-chrome-windows.html)

### Arista VeloCloud Orchestrator Zero-Day
- **Description**: Zero-day vulnerability in VeloCloud Orchestrator (VCO) On-Prem deployments actively exploited before patch availability.
- **Impact**: Allows attackers to compromise the central management platform for SD-WAN infrastructure, potentially controlling network traffic and policies across the enterprise.
- **Status**: Actively exploited; Arista released security patches addressing the flaw.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Arista patches actively exploited VeloCloud Orchestrator zero-day](https://www.bleepingcomputer.com/news/security/arista-patches-actively-exploited-velocloud-orchestrator-zero-day/)

### cPanel CalDAV/CardDAV Root Code Execution
- **Description**: Flaw in cPanel's CalDAV and CardDAV service allowing any authenticated hosting account holder to execute code as root.
- **Impact**: Complete server takeover from a standard hosting account; second vulnerability in WP Toolkit plugin allows cross-account database manipulation.
- **Status**: Actively exploitable; cPanel released fixed versions for both vulnerabilities on September 22, 2026.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — New cPanel Flaw Lets a Hosting Account Run Code as Root, Take Full Server Control](https://thehackernews.com/2026/09/new-cpanel-flaw-lets-hosting-account_0272795595.html)

### Next.js ImageResponse SVG Code Execution
- **Description**: Critical vulnerability in Next.js ImageResponse feature where attacker-controlled input (e.g., text from request URLs) passed to image generation leads to server-side code execution via crafted SVG.
- **Impact**: Remote code execution on Next.js applications using ImageResponse for Open Graph/social preview images with user-supplied data.
- **Status**: Fixed by Vercel on September 22, 2026; exploitation risk for unpatched applications.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — Critical Next.js ImageResponse Flaw Can Lead to Server Code Execution via Crafted SVG Input](https://thehackernews.com/2026/09/critical-nextjs-imageresponse-flaw-can.html)

### ClickFix Attacks via Placeholder Domain
- **Description**: The "third-party.com" domain, widely used as a placeholder in developer documentation and code examples, now serves fake Cloudflare verification pages that trick Windows users into copying and executing malicious PowerShell commands.
- **Impact**: Social engineering-driven remote code execution on Windows endpoints; leverages trust in documentation examples to reach developers and technical users.
- **Status**: Active campaign observed; domain actively serving malicious content.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Placeholder domain used in dev docs now serves ClickFix attacks](https://www.bleepingcomputer.com/news/security/placeholder-domain-used-in-dev-docs-now-serves-clickfix-attacks/)

### RemControl Android Banking MaaS
- **Description**: New Android malware-as-a-service platform distributed via malvertising campaigns impersonating the TVTap IPTV application, targeting users in Europe and Canada.
- **Impact**: Banking credential theft, financial fraud, and device compromise for Android users who install the trojanized application.
- **Status**: Active distribution through malvertising; MaaS model enables multiple threat actors.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — New RemControl Android banking malware targets users in Europe and Canada](https://www.bleepingcomputer.com/news/security/new-remcontrol-android-banking-malware-targets-users-in-europe-and-canada/)

### Malicious Terraform Providers on HashiCorp Registry
- **Description**: Go-based malware distributed through two malicious Terraform providers and two Go modules published to the official HashiCorp Registry, marking the first known abuse of this supply chain vector.
- **Impact**: Compromise of infrastructure-as-code pipelines; malicious code executes during `terraform init`/`apply` in developer and CI/CD environments.
- **Status**: Disclosed by Aikido; packages include gocommunity-io/dockerd (222 downloads) and others; active supply chain compromise.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — Attackers Use Malicious Terraform Providers to Deliver Go Malware via HashiCorp Registry](https://thehackernews.com/2026/09/attackers-use-malicious-terraform.html)

### GitLab Issue Email Address Credential Theft
- **Description**: GitLab automatically assigns each user a private incoming email address for filing issues; this address functions as a high-privilege credential allowing anyone who possesses it to commit code as the user and trigger CI/CD pipelines.
- **Impact**: Supply chain compromise via impersonation; unauthorized code merges to protected branches; malicious CI/CD job execution with victim's permissions.
- **Status**: Design flaw actively exploitable; no patch available as it is an architectural feature.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: mitigate
- **Reporting**: [Dark Reading — GitLab Email Addresses Can Be Weaponized for Supply Chain Attacks](https://www.darkreading.com/application-security/gitlab-email-addresses-supply-chain-attacks), [The Hacker News — A Leaked GitLab Issue Email Address Lets Anyone Push Code and Run CI Jobs as You](https://thehackernews.com/2026/09/a-leaked-gitlab-issue-email-address.html)

### AI-Agent Automated Credit Card Skimming
- **Description**: Financially motivated threat actor using open-source AI agent frameworks to attack hundreds of online retailers at scale, injecting payment skimmers and exfiltrating credit card data.
- **Impact**: 600,000+ credit card records stolen; 100+ e-commerce sites infected with skimmers; automated, scalable attack infrastructure.
- **Status**: Active, ongoing campaign leveraging AI for target discovery, exploitation, and persistence.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Malicious AI agents steal 600K credit cards, infect 100+ sites with skimmers](https://www.bleepingcomputer.com/news/security/malicious-ai-agents-steal-600k-credit-cards-infect-100-plus-sites-with-skimmers/)

### CLOSEDQUORUM AI-Governed Malware
- **Description**: Windows malware (CLOSEDQUORUM) that replaces traditional C2 with a voting mechanism among up to four AI models to decide malicious actions including credential theft, browser password extraction, and crypto wallet targeting.
- **Impact**: Novel resilient malware architecture; potential for autonomous decision-making and evasion of traditional C2 takedowns.
- **Status**: Proof-of-concept stage; public version non-functional; not observed in completed attacks.
- **Severity**: medium
- **Exploitation Status**: potential
- **Action**: monitor
- **Reporting**: [The Hacker News — This Windows Malware is Built to Let Up to Four AI Models Vote on Its Next Move](https://thehackernews.com/2026/09/windows-malware-is-built-to-let-up-to.html)

### Kubernetes/GCP Config Connector Privilege Escalation
- **Description**: Confused deputy vulnerability in Google Kubernetes Config Connector allowing a Kubernetes user with limited permissions to escalate to full Google Cloud organization administrator via a single malicious YAML.
- **Impact**: Organization-wide compromise of GCP resources from a seemingly restricted Kubernetes role.
- **Status**: Design flaw demonstrated by Varonis; exploitable in configurations using Config Connector.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: investigate
- **Reporting**: [Bleeping Computer — How One Kubernetes YAML Can Hand Over a GCP Organization](https://www.bleepingcomputer.com/news/security/how-one-kubernetes-yaml-can-hand-over-a-gcp-organization/)

### Compromised MemTensor Supply Chain (sckit Stealer)
- **Description**: Legitimate MemTensor packages on npm and PyPI compromised to deliver sckit, a cross-platform Go-based credential stealer targeting Windows, Linux, and macOS.
- **Impact**: Credential theft across developer workstations and CI/CD systems; multi-platform implants delivered through trusted package managers.
- **Status**: Active supply chain compromise; multiple security firms (Aikido, SafeDep, Socket, StepSecurity) reporting affected versions.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — Compromised MemTensor Packages Deliver sckit Credential Stealer via npm and PyPI](https://thehackernews.com/2026/09/compromised-memtensor-packages-deliver.html)

### EDR Evasion via Process Parameter-Poisoning
- **Description**: Technique injecting code into process initialization structures without using Windows APIs monitored by EDR solutions, effectively bypassing modern endpoint detection.
- **Impact**: Stealthy process injection enabling payload execution without triggering standard EDR telemetry.
- **Status**: Technique disclosed and demonstrated; applicable to current EDR architectures.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: monitor
- **Reporting**: [Dark Reading — EDR Evasion Stack Helps Process Injection Slip Past Defenses](https://www.darkreading.com/endpoint-security/edr-evasion-stack-helps-process-injection-slip-past-defenses)

### Rogue External MFA Provider Password Theft
- **Description**: Attack allowing privileged users to register a malicious external MFA provider that intercepts user passwords during legitimate authentication flows.
- **Impact**: Credential harvesting from valid login ceremonies; bypasses MFA protections by subverting the provider trust model.
- **Status**: Research proof-of-concept; requires privileged access to identity infrastructure.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: monitor
- **Reporting**: [Bleeping Computer — Rogue external MFA providers can steal passwords during logins](https://www.bleepingcomputer.com/news/security/rogue-external-mfa-providers-can-steal-passwords-during-logins/)

## Affected Systems and Products

- **Check Point Security Gateway**: VPN certificate-handling component; all versions prior to patched releases vulnerable to CVE-2026-85102.
- **WordPress Core**: Versions affected by CVE-2026-87902; exploitation enables file write and shell command execution.
- **MikroTik RouterOS**: Devices with SSH exposed to Internet; vulnerable to MikroTrick chain (CVE-2026-67279, CVE-2026-86060) for passwordless admin takeover.
- **Ubuntu Linux LTS Releases**: 22.04, 24.04, 26.04 lack upstream kernel fix for CVE-2026-80521 (AF_UNIX use-after-free container escape).
- **F5 BIG-IP APM**: Systems configured as OAuth authorization servers; vulnerable to CVE-2026-94127 unauthenticated RCE.
- **Google Chrome**: Versions prior to fixes for CVE-2026-85046 and CVE-2026-87491; exploited in zero-day chain.
- **Microsoft Windows**: Versions vulnerable to CVE-2026-85880 (ALPC privilege escalation); exploited in Chrome-Windows chain.
- **Arista VeloCloud Orchestrator (VCO) On-Prem**: Actively exploited zero-day; patched in recent security releases.
- **cPanel & WHM**: CalDAV/CardDAV service and WP Toolkit plugin; fixed versions released September 22, 2026.
- **Next.js (Vercel)**: Applications using ImageResponse with attacker-controlled input; fixed in versions released September 22, 2026.
- **HashiCorp Registry**: Malicious Terraform providers (gocommunity-io/dockerd, kreuzwenker/*) and Go modules published to official registry.
- **GitLab (Self-Managed and SaaS)**: All versions with incoming email issue feature; private email addresses function as high-privilege credentials.
- **npm and PyPI**: Compromised MemTensor packages (@memtensor/memos-cloud-openclaw-plugin and related) delivering sckit stealer.
- **Google Cloud Platform**: Organizations using Kubernetes Config Connector; vulnerable to confused deputy privilege escalation via Kubernetes YAML.
- **Android Devices**: Users in Europe and Canada targeted by RemControl banking MaaS via malvertising (fake TVTap IPTV app).
- **Windows Endpoints**: Targeted by ClickFix attacks abusing third-party.com placeholder domain; PowerShell execution via social engineering.

## Attack Vectors and Techniques

- **Zero-Day Exploit Chains**: UTA0565 chaining Chrome V8 vulnerabilities (CVE-2026-85046, CVE-2026-87491) with Windows ALPC flaw (CVE-2026-85880) for browser-to-kernel code execution and CLEANGULP deployment via fake websites.
- **Pre-Authentication RCE via VPN/Certificate Handling**: Exploitation of Check Point CVE-2026-85102 and F5 BIG-IP APM CVE-2026-94127 (OAuth authorization server mode) for unauthenticated network appliance compromise.
- **Supply Chain Compromise via Package Registries**: Malicious Terraform providers and Go modules on HashiCorp Registry; compromised MemTensor packages on npm/PyPI delivering cross-platform sckit credential stealer.
- **Identity Provider Subversion**: GitLab's automatic issue email addresses used as credentials for unauthorized code commits and CI/CD execution; rogue external MFA providers registered to intercept passwords during legitimate logins.
- **AI-Automated Mass Exploitation**: Open-source AI agent frameworks used to discover, exploit, and persist on 100+ e-commerce sites for credit card skimming at scale (600K+ records).
- **Malvertising and Impersonation**: RemControl Android MaaS distributed via ads impersonating legitimate TVTap IPTV application; ClickFix attacks abusing trusted placeholder domain (third-party.com) in developer documentation.
- **Container Escape via Kernel Use-After-Free**: CVE-2026-80521 exploit released for AF_UNIX socket flaw; enables host root from container on unpatched Ubuntu LTS kernels.
- **Chained Router Exploitation**: MikroTrick combines SSH state-machine flaw (CVE-2026-67279) with login argument injection (CVE-2026-86060) for passwordless administrative takeover of exposed MikroTik devices.
- **Web Application File Write to RCE**: WordPress CVE-2026-87902 exploited to write executable files to web-accessible directories for persistent shell access.
- **Cloud Privilege Escalation via Confused Deputy**: Kubernetes Config Connector authority abused via single YAML to escalate from limited K8s permissions to GCP organization admin.
- **EDR Evasion via Parameter Poisoning**: Process injection into initialization structures bypassing monitored Windows APIs, evading modern endpoint detection.
- **AI-Governed Malware Decision Making**: CLOSEDQUORUM uses ensemble voting of up to four AI models for C2-less command selection (credential theft, browser passwords, crypto wallets).
- **Server-Side Template/Code Execution via Image Processing**: Next.js ImageResponse flaw allows SVG-based code execution when attacker controls image generation input.
- **Hosting Account to Root Escalation**: cPanel CalDAV/CardDAV flaw permits standard hosting accounts to execute code as root; WP Toolkit bug enables cross-account database manipulation.

## Threat Actor Activities

- **UTA0565 (Chinese Threat Actor)**: Exploited Chrome-Windows zero-day chain (CVE-2026-85046, CVE-2026-87491, CVE-2026-85880) as zero-days on September 3-4, 2026; deployed CLEANGULP malware via fake websites; demonstrates advanced exploit development and rapid weaponization of browser/kernel vulnerabilities.
- **ShinyHunters (Cyber Extortion Group)**: Claims breach of FBI systems with theft of sensitive data on current/former agents and job applicants; posted claim on dark web leak site; extortion-focused operations targeting high-value organizations.
- **Financially Motivated AI-Agent Operator**: Unknown actor/group leveraging open-source AI agent frameworks for automated, large-scale credit card skimming across 100+ retailer sites; 600,000+ payment records stolen; represents evolution toward AI-driven offensive automation at scale.
- **RemControl MaaS Operators**: Developers and affiliates of RemControl Android banking malware-as-a-service; distributing via malvertising campaigns impersonating TVTap IPTV app targeting Europe and Canada; MaaS model lowers barrier for multiple threat actors.
- **Supply Chain Compromise Actors**: Unknown actors compromising legitimate MemTensor packages on npm/PyPI to inject sckit stealer; unknown actors publishing malicious Terraform providers/Go modules to HashiCorp Registry; both demonstrate high-trust registry abuse.
- **Ryuk Ransomware Affiliate**: Armenian national sentenced to 24 months for Ryuk ransomware attacks against U.S. companies; indicates ongoing law enforcement disruption of ransomware ecosystems.
- **Network Management System Targeting Actors**: Per InfraTrust report, unspecified actors increasingly targeting enterprise infrastructure management systems, exploiting critical vulnerabilities before or shortly after vendor disclosure.
- **AI Chatbot Manipulation Actors**: Threat actors poisoning ChatGPT, Gemini, and Google AI Overview responses by seeding malicious links/data and optimizing for search/LLM retrieval; mass disinformation and phishing campaign vector.