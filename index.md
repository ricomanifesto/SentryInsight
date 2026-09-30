---
schema_version: 2
report_date: 2026-09-30
generated_at: 2026-09-30T18:24:40Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-30/
---
# Exploitation Report

## Executive Summary

Multiple critical zero-day vulnerabilities are under active exploitation across diverse platforms including Cisco SD-WAN, Citrix NetScaler, Zimbra Collaboration Suite, and Apple devices. Threat actors are leveraging these flaws for initial access, privilege escalation, and persistent compromise, with several campaigns demonstrating sophisticated tradecraft such as web shell deployment, credential harvesting, and lateral movement. The exploitation landscape is further complicated by widespread credential exposure in public repositories and the weaponization of legitimate tools like RMM software and AI platforms for social engineering and malware delivery.

Active campaigns by tracked threat groups including Star Blizzard and ShinyHunters highlight the persistent targeting of high-value organizations and individuals. Star Blizzard has evolved its phishing methodology with a new "RedFlick" technique to deploy the CosmicPulse backdoor against Ukrainian-linked entities, while ShinyHunters faces law enforcement pressure following arrests. Simultaneously, financially motivated actors are exploiting Citrix NetScaler and Cisco SD-WAN zero-days for broad opportunistic compromise, and the CSuite phishing campaign combines Microsoft 365 session theft with RMM deployment for extensive account takeover.

The attack surface continues to expand through novel vectors including malicious Custom ChatGPTs abusing ClickFix lures, AI coding agents inadvertently exposing sensitive data, and browser-based attack chains that never leave the browser session. Critical infrastructure remains a target, evidenced by the South African air traffic control ransomware incident. Defenders must prioritize patching of actively exploited zero-days, implement phishing-resistant authentication, monitor for RMM abuse, and address credential hygiene across development pipelines.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Authentication Bypass (CVE-2026-76504)
- **Description**: Critical zero-day authentication bypass flaw in Cisco Catalyst SD-WAN Manager that allows a remote unauthenticated attacker to use the Manager's API as the admin user, leading to full administrative control over SD-WAN networks.
- **Impact**: Attackers can escalate to admin privileges, manage SD-WAN network configurations, and potentially pivot to connected network infrastructure.
- **Status**: Actively exploited in the wild; fixed releases are available with no workaround.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-76504
- **Reporting**: [The Hacker News — Cisco Warns of Attackers Exploiting Critical Authentication Bypass in SD-WAN Manager](https://thehackernews.com/2026/09/cisco-warns-of-attackers-exploiting.html), [Bleeping Computer — Cisco warns of new SD-WAN zero-day exploited in attacks](https://www.bleepingcomputer.com/news/security/cisco-warns-of-new-sd-wan-authentication-bypass-zero-day-exploited-in-attacks/)

### Citrix NetScaler ADC and Gateway DTLS Memory Overflow (CVE-2026-88772)
- **Description**: Critical memory overflow vulnerability in the Datagram Transport Layer Security (DTLS) protocol handling of Citrix NetScaler ADC and NetScaler Gateway appliances, enabling pre-authentication shellcode execution.
- **Impact**: Attackers gain root access, deploy custom web shells and tunneling malware, steal credentials, and spread laterally into internal networks.
- **Status**: Actively exploited as a zero-day; patches released by Citrix.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-88772
- **Reporting**: [The Hacker News — Attackers Exploit NetScaler Flaw for Root Access, Deploy WHIPSHOT and SLAPSHOT](https://thehackernews.com/2026/09/attackers-exploit-netscaler-flaw-for.html), [The Hacker News — Citrix NetScaler CVE-2026-88772 Exploit Details Show Pre-Auth Path to Shellcode Execution](https://thehackernews.com/2026/09/citrix-netscaler-cve-2026-88772-exploit.html), [Bleeping Computer — Hackers exploit Citrix NetScaler zero-day to deploy web shells](https://www.bleepingcomputer.com/news/security/hackers-exploit-citrix-netscaler-zero-day-to-deploy-web-shells/)

### Zimbra Collaboration Suite Command Injection (CVE-2026-73570)
- **Description**: Unauthenticated operating system command injection flaw in Zimbra Collaboration Suite (ZCS) triggered via Simple Network Management Protocol (SNMP) that leads to remote code execution.
- **Impact**: Threat actors deploy web shells and access mailbox data, enabling persistent access to email communications and potential lateral movement.
- **Status**: Now-patched vulnerability actively weaponized; Microsoft Security Research team observed exploitation.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-73570
- **Reporting**: [The Hacker News — Attackers Exploit Zimbra Flaw to Deploy Web Shells and Harvest Authentication Secrets](https://thehackernews.com/2026/09/attackers-exploit-zimbra-flaw-to-deploy.html)

### Apple Zero-Day Out-of-Bounds Write (CVE-2026-86950)
- **Description**: Out-of-bounds write vulnerability in Apple products being exploited in an extremely sophisticated fashion in targeted attacks.
- **Impact**: Targeted compromise of Apple devices; specific impact details limited but described as highly sophisticated exploitation.
- **Status**: Actively exploited in targeted attacks; Apple has acknowledged the vulnerability.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-86950
- **Reporting**: [Dark Reading — Apple Zero-Day Vulnerability Weaponized in Targeted Attacks](https://www.darkreading.com/cyberattacks-data-breaches/apple-zero-day-vulnerability-weaponized-targeted-attacks)

### Bitget Third-Party Security Product Zero-Day
- **Description**: Zero-day vulnerability in third-party security products used by cryptocurrency exchange Bitget, exploited to breach systems and steal $387.5 million.
- **Impact**: Full system compromise leading to massive cryptocurrency theft; demonstrates supply chain risk through security tooling.
- **Status**: Actively exploited; specific product and CVE not disclosed publicly.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Bitget hacked via zero-day in third-party security products](https://www.bleepingcomputer.com/news/security/bitget-hacked-via-zero-day-in-third-party-security-products/)

### TeamViewer High-Severity Client Vulnerabilities
- **Description**: Set of high-severity vulnerabilities affecting TeamViewer client and host software requiring immediate patching.
- **Impact**: Potential remote code execution or unauthorized access through the remote access software.
- **Status**: Actively warned by vendor; patches available; exploitation status not explicitly confirmed but urgency indicates high risk.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [Bleeping Computer — TeamViewer urges users to patch severe flaws “as soon as possible”](https://www.bleepingcomputer.com/news/security/teamviewer-urges-users-to-patch-severe-flaws-as-soon-as-possible/)

### Unsloth Studio Model Inspection Code Execution
- **Description**: Patched vulnerability in Unsloth Studio that allows malicious AI models to execute arbitrary Python code during inspection via the trust_remote_code setting.
- **Impact**: Code execution on systems inspecting untrusted AI models; supply chain risk for ML/AI workflows.
- **Status**: Patched; exploitation status not confirmed in wild but proof-of-concept demonstrated.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [Dark Reading — Unsloth Studio Flaw Turns Routine Model Inspection Into Code Execution](https://www.darkreading.com/application-security/unsloth-studio-flaw-model-inspection-code-execution)

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: All versions prior to fixed releases; network management appliances for SD-WAN infrastructure
- **Citrix NetScaler ADC and NetScaler Gateway**: Appliances running vulnerable DTLS implementations; network delivery controllers and VPN gateways
- **Zimbra Collaboration Suite (ZCS)**: Versions with vulnerable SNMP implementation; enterprise email and collaboration platform
- **Apple Products**: iOS, macOS, and other Apple operating systems affected by CVE-2026-86950; specific versions not detailed in source
- **TeamViewer Client and Host Software**: All versions prior to security updates; remote access and support software across Windows, macOS, Linux
- **Unsloth Studio**: AI model development and inspection platform; versions prior to patch
- **Bitget Third-Party Security Products**: Undisclosed security tooling used by the exchange; supply chain impact
- **MikroTik RouterOS**: Critical pre-auth RCE flaw warned by CISA; router firmware across multiple models
- **MSP360 RMM Software**: Legitimate remote monitoring and management tool abused in phishing campaigns
- **ScreenConnect (ConnectWise Control)**: Remote access tool deployed as second-stage payload in dual-RMM attacks
- **Custom ChatGPT GPTs**: OpenAI's Custom GPT feature abused to host malicious lures
- **GitHub Public Repositories**: Over 543,000 valid credentials exposed across developer accounts and organizations
- **OpenSSL**: DTLS implementation in versions prior to September 29, 2026 fixes; cryptographic library
- **Linux Kernel/JIT Engines**: Spectre-v2 BTR variant affecting JIT engines in browsers, language runtimes, and OS kernels across CPU vendors

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: Attackers use fake verification prompts (CAPTCHA, "I'm not a robot") to trick users into executing malicious PowerShell commands via clipboard manipulation; deployed through Custom ChatGPTs, phishing pages, and malicious ads
- **Dual-RMM Phishing**: Phishing lures (meeting invitations, PDF themes, software updates) deliver legitimate MSP360 installer which then deploys ScreenConnect for persistent remote access; combines trusted software with social engineering
- **Credential Harvesting from Public Repositories**: Automated scanning of public GitHub repositories yields over 543,000 valid credentials including API keys, database passwords, and cloud service tokens
- **Zero-Day Exploitation for Initial Access**: Pre-authentication RCE in Citrix NetScaler (CVE-2026-88772) and authentication bypass in Cisco SD-WAN (CVE-2026-76504) provide direct administrative access without credentials
- **Web Shell Deployment**: Custom web shells deployed on compromised NetScaler and Zimbra appliances for persistent access, credential theft, and lateral movement
- **RMM Tool Abuse**: Legitimate remote monitoring and management tools (MSP360, ScreenConnect, TeamViewer) repurposed for unauthorized persistent access
- **AI Platform Weaponization**: Custom ChatGPT GPTs promoted via sponsored Google results direct victims to ClickFix malware delivery pages; AI coding agents inadvertently expose sensitive internal images and billing records
- **Browser-Based Attack Chains**: Entire attack lifecycle from initial access to exfiltration conducted within browser sessions, exploiting browser extensions, session storage, and web application vulnerabilities
- **Microsoft 365 Session Theft**: Phishing campaigns steal authenticated M365 sessions bypassing MFA, then deploy RMM tools for sustained access
- **Supply Chain via Security Products**: Zero-day in third-party security tooling used to breach cryptocurrency exchange, highlighting trust exploitation in defensive tooling
- **Malicious AI Model Inspection**: Exploitation of trust_remote_code in AI/ML model repositories to achieve code execution during routine model review
- **Spectre-v2 BTR Side-Channel**: Branch Target Reuse variant leaks memory across security boundaries in JIT engines despite existing mitigations

## Threat Actor Activities

- **Star Blizzard (APT29/Cozy Bear)**: Russian APT group abandoned ClickFix for new "RedFlick" phishing technique targeting Ukrainian-linked NGOs, think tanks, and journalists to deploy CosmicPulse backdoor; demonstrates continuous evolution of social engineering tradecraft
- **ShinyHunters**: Extortion group facing law enforcement action after Dutch arrest of alleged leader; FBI urging members to surrender; known for data theft and extortion campaigns against major corporations
- **Unknown Threat Actors (NetScaler Campaign)**: Mandiant and GTIG observed exploitation of CVE-2026-88772 targeting government, financial services, technology, education, and legal sectors in North America and Europe; deployed WHIPSHOT and SLAPSHOT malware families
- **CSuite Phishing Operators**: US-focused campaign across 351 sandbox analyses (51% US submissions) targeting technology, manufacturing, government, and consulting sectors; combines M365 session theft with RMM deployment for account takeover and fraud
- **Bitget Attackers**: Unidentified group exploited zero-day in third-party security products to steal $387.5 million from cryptocurrency exchange; demonstrates high-value financial targeting
- **Former US Air Force Members**: Two individuals sentenced to 189 months combined for multi-year BEC and phishing campaigns; insider threat element with military background
- **French Tax Administration Breach Actor**: Single attacker used stolen staff credentials to exfiltrate hundreds of thousands of taxpayer records over seven weeks undetected; low-sophistication but high-impact due to weak access controls
- **AI Supply Chain Exposers**: Developers using AI coding agents inadvertently published 13,000+ internal images (billing records, unreleased features) to public GitHub across 300+ organizations; systemic development pipeline failure