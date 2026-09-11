---
schema_version: 2
report_date: 2026-09-11
generated_at: 2026-09-11T16:18:47Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-11/
---
# Exploitation Report

## Executive Summary

A suspected Russian-speaking threat actor has orchestrated a large-scale, AI-driven exploitation campaign targeting PaperCut NG/MF print management servers, compromising over 440 instances across 395 organizations. The attacker leveraged hundreds of autonomous AI agents to weaponize two recently disclosed vulnerabilities, demonstrating a fundamental shift in the cyber kill chain where AI handles reconnaissance, exploit development, lateral movement, and exfiltration at machine speed. This campaign, tracked by Blackpoint Cyber and GreyNoise, represents the most significant observed use of agentic AI for offensive cyber operations to date.

Simultaneously, multiple threat clusters—including ransomware operators and state-sponsored groups—are actively exploiting two critical vulnerabilities in Cisco Secure Firewall Management Center (FMC), notably CVE-2026-20079 (CVSS 10.0), to steal credentials and deploy Qilin ransomware. Cisco Talos has identified three distinct threat clusters leveraging these flaws. In the supply chain domain, attackers have chained two vulnerabilities in JFrog Artifactory to seize administrative control of self-hosted instances and implant persistent backdoors, with active exploitation observed between August 15 and September 8 against unpatched servers.

On the zero-day front, a China-linked group (UNC3569) exploited a flaw in the ubiquitous Sogou Input Method to deploy the GRAYRABBIT backdoor, while the "BlueMoon" exploit kit has been deployed by multiple cyber-espionage actors against undisclosed zero-days in Windows and Google Chrome. The disgruntled researcher "Nightmare-Eclipse" published another Windows Defender zero-day ("ShieldCrash"), continuing a pattern of public zero-day releases. Meanwhile, Anthropic has disclosed extensive abuse of its Claude AI models by state-sponsored actors (including a Russian group designated GTG-20006) and cybercriminals for automated exploitation, malware redevelopment after detection, and mass surveillance operations.

## Active Exploitation Details

### PaperCut NG/MF Dual Vulnerability Exploitation Campaign
- **Description**: Two security flaws in PaperCut NG/MF print management software have come under active exploitation. A suspected Russian-speaking threat actor deployed hundreds of AI agents to automate the full attack lifecycle—from reconnaissance and exploit development to lateral movement and data exfiltration—compromising over 440 PaperCut instances across 395 organizations globally.
- **Impact**: Full compromise of PaperCut NG/MF servers, enabling unauthorized access to printed documents, credential theft, lateral movement into internal networks, and persistent foothold establishment.
- **Status**: Actively exploited in the wild. PaperCut has released Regular Maintenance Releases (versions 26.0.5, 25.0.13, and 24.1.10) that replace earlier emergency patches and address both flaws.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Dark Reading — Papercut AI Swarm Attack Heralds Changes for Cyber Kill Chain](https://www.darkreading.com/cyberattacks-data-breaches/papercut-ai-swarm-attack-cyber-kill-chain), [The Hacker News — PaperCut Replaces Emergency Patches With Fixes for Two Actively Exploited Flaws](https://thehackernews.com/2026/09/papercut-replaces-emergency-patches.html), [Bleeping Computer — AI-powered attack exploited PaperCut flaws to hack 395 organizations](https://www.bleepingcomputer.com/news/security/ai-powered-attack-exploited-papercut-flaws-to-hack-395-organizations/), [The Hacker News — PaperCut Attacker Uses Hundreds of AI Agents to Compromise 440+ Instances](https://thehackernews.com/2026/09/papercut-attacker-uses-hundreds-of-ai.html)

### Cisco Secure Firewall Management Center (FMC) Authentication Bypass and RCE
- **Description**: Two recently patched vulnerabilities in Cisco Secure Firewall Management Center (FMC) are being exploited by three distinct threat clusters. CVE-2026-20079 (CVSS 10.0) is an authentication bypass in the web interface allowing unauthenticated remote attackers to bypass authentication. A second vulnerability enables remote code execution. Threat actors include ransomware operators deploying Qilin ransomware and state-sponsored groups conducting credential theft.
- **Impact**: Unauthenticated remote attackers can bypass authentication, execute arbitrary code, steal administrative credentials, and deploy ransomware on FMC appliances managing enterprise firewall infrastructure.
- **Status**: Actively exploited by three threat clusters. Patches are available from Cisco.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-20079
- **Reporting**: [The Hacker News — Cisco FMC Flaws Exploited to Steal Credentials and Deploy Qilin Ransomware](https://thehackernews.com/2026/09/cisco-fmc-flaws-exploited-to-steal.html), [Bleeping Computer — Cisco FMC flaws exploited by ransomware gang, state-sponsored hackers](https://www.bleepingcomputer.com/news/security/cisco-fmc-flaws-exploited-by-ransomware-gang-state-sponsored-hackers/)

### JFrog Artifactory Chained Vulnerability Exploitation
- **Description**: Attackers are chaining two flaws in JFrog Artifactory, the repository manager used in software build pipelines, to gain administrator control of self-hosted servers and plant backdoors. The attack chain allows unauthenticated attackers to escalate privileges to admin and achieve persistent access. Exploitation was observed by Wiz between August 15 and September 8, 2026, exclusively against servers that had not applied JFrog's fixes.
- **Impact**: Full administrative control of Artifactory instances, enabling supply chain compromise through malicious artifact injection, credential theft, and persistent backdoor access to build pipelines.
- **Status**: Actively exploited in the wild against unpatched instances. JFrog has released fixes for both vulnerabilities.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Attackers Chain JFrog Artifactory Flaws to Gain Admin Control and Plant Backdoors](https://thehackernews.com/2026/09/attackers-chain-jfrog-artifactory-flaws.html)

### Sogou Input Method Zero-Day Exploitation by UNC3569
- **Description**: China-linked threat group UNC3569 exploited a vulnerability in Sogou Input Method, one of the most widely used Chinese character input tools on Windows, to deploy the GRAYRABBIT backdoor. The attack initiates via a crafted link and results in the attacker gaining the same privileges as the logged-in user.
- **Impact**: Arbitrary code execution in the context of the logged-in user, enabling deployment of the GRAYRABBIT backdoor for persistent access, data theft, and further lateral movement.
- **Status**: Actively exploited in targeted campaigns. Tencent (Sogou's owner) has been notified; patch status unclear from reporting.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — China-Linked UNC3569 Exploited Sogou Input Method Flaw to Deploy GRAYRABBIT Backdoor](https://thehackernews.com/2026/09/china-linked-unc3569-exploited-sogou.html)

### Windows Defender "ShieldCrash" Zero-Day
- **Description**: The disgruntled researcher "Nightmare-Eclipse" has published a zero-day exploit for Windows Defender, dubbed "ShieldCrash." This continues a pattern of public zero-day releases targeting Microsoft's anti-malware engine.
- **Impact**: Potential bypass or disablement of Windows Defender protections, enabling follow-on malware execution without detection.
- **Status**: Zero-day exploit publicly released; active exploitation status unconfirmed in reporting.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: monitor
- **Reporting**: [Dark Reading — Nightmare-Eclipse Strikes Again With 'ShieldCrash' Windows Exploit](https://www.darkreading.com/vulnerabilities-threats/nightmare-eclipse-strikes-again-shieldcrash-windows-exploit)

### BlueMoon Exploit Kit: Windows and Chrome Zero-Days
- **Description**: Multiple cyber-espionage groups have deployed an exploit kit dubbed "BlueMoon" that leverages zero-day vulnerabilities in Microsoft Windows and Google Chrome. The kit is used in targeted espionage operations.
- **Impact**: Remote code execution and privilege escalation on fully patched Windows and Chrome installations at time of exploitation, enabling silent installation of espionage tooling.
- **Status**: Zero-days actively exploited by multiple APT groups via the BlueMoon kit. Vendor patch status not specified in reporting.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [Bleeping Computer — New 'BlueMoon' kit exploited Windows and Chrome zero-day flaws](https://www.bleepingcomputer.com/news/security/new-bluemoon-kit-exploited-windows-and-chrome-zero-day-flaws/)

### Check Point VPN Certificate Validation Flaws
- **Description**: Check Point has disclosed two critical vulnerabilities (both rated CVSS 9.8) in VPN certificate handling across its Security Gateways and Security Management products. Both flaws could allow unauthenticated remote code execution under specific conditions that Check Point has not publicly detailed.
- **Impact**: Unauthenticated remote code execution on firewall appliances and management servers, potentially leading to full network perimeter compromise.
- **Status**: Patched by Check Point; no evidence of active exploitation in the wild reported.
- **Severity**: critical
- **Exploitation Status**: not_observed
- **Action**: patch
- **Reporting**: [The Hacker News — Check Point Discloses Two 9.8-Rated VPN Certificate Flaws Enabling Unauthenticated RCE](https://thehackernews.com/2026/09/check-point-discloses-two-98-rated-vpn.html)

### GitLab Path Traversal Vulnerability
- **Description**: A maximum-severity path traversal vulnerability in GitLab (CVE-2026-85706) allows attackers to traverse directories and potentially read or write arbitrary files on the server.
- **Impact**: Unauthorized file system access on GitLab servers, potentially leading to source code theft, credential exposure, and supply chain compromise through repository manipulation.
- **Status**: Patched by GitLab; users urged to patch immediately. No active exploitation reported in the article.
- **Severity**: critical
- **Exploitation Status**: not_observed
- **Action**: patch
- **CVE IDs**: CVE-2026-85706
- **Reporting**: [Bleeping Computer — GitLab urges users to patch max severity path traversal flaw](https://www.bleepingcomputer.com/news/security/gitlab-urges-users-to-patch-max-severity-path-traversal-flaw/)

### Anthropic Claude AI Model Abuse for Cyber Operations
- **Description**: Anthropic has identified widespread abuse of its Claude models by threat actors designated as Generative Threat Groups (GTGs) between December 2025 and August 2026. Activities include automated vulnerability exploitation and data theft across multiple victims, malware redevelopment to evade detection (notably by Russian state-sponsored group GTG-20006, aligned with Midnight Blizzard), weapons design, propaganda, and mass surveillance.
- **Impact**: Accelerated exploit development, automated large-scale data theft, rapid malware iteration to bypass defenses, and AI-assisted reconnaissance and weaponization.
- **Status**: Ongoing active abuse by multiple state-sponsored and criminal groups. Anthropic has disrupted specific campaigns and banned offending accounts.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [The Hacker News — Claude Used to Automate Exploitation and Data Theft Across Multiple Victims](https://thehackernews.com/2026/09/claude-used-to-automate-exploitation.html), [The Hacker News — Russian State-Sponsored Hackers Use Claude to Rebuild Malware After Detection](https://thehackernews.com/2026/09/russian-state-sponsored-hackers-use.html), [Bleeping Computer — How Threat Actors Are Turning Trusted AI Platforms Into an Attack Surface](https://www.bleepingcomputer.com/news/security/how-threat-actors-are-turning-trusted-ai-platforms-into-an-attack-surface/)

### Android Banking Malware Campaigns (Gigabud and Mantax Otax)
- **Description**: Two distinct Android malware families are active. Gigabud (delivered by the GoldFactory threat group) abuses Android Work Profile to install a tampered banking app inside an isolated work profile, evading malware checks. Mantax Otax combines ransomware and spyware capabilities: encrypting files, stealing sensitive data, and spamming/harassing victims. Both campaigns target users in Indonesia and potentially beyond.
- **Impact**: Financial credential theft, banking fraud, file encryption for ransom, data exfiltration, and victim harassment. Gigabud's work profile technique evades traditional security controls.
- **Status**: Active campaigns observed in the wild. GoldFactory and Mantax Otax operators actively distributing malware.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [Dark Reading — Indonesia Hit by Android Banking App-Cloning Campaign](https://www.darkreading.com/mobile-security/indonesia-android-banking-app-cloning-campaign), [Bleeping Computer — New Android malware encrypts files, steals data, and harasses victims](https://www.bleepingcomputer.com/news/security/new-android-malware-encrypts-files-steals-data-and-harasses-victims/), [The Hacker News — Gigabud Creates Android Work Profiles to Hide From Banking App Malware Checks](https://thehackernews.com/2026/09/gigabud-creates-android-work-profiles.html)

### Microsoft Graph API Abuse for BYOD Targeting
- **Description**: Threat actors are leveraging Microsoft's Graph API to identify high-value targets in bring-your-own-device (BYOD) environments, then passing access to extortion groups such as ShinyHunters for follow-on compromise and data theft.
- **Impact**: Reconnaissance and initial access to corporate Microsoft 365 data via personal devices enrolled in BYOD programs, facilitating credential theft, data exfiltration, and extortion.
- **Status**: Active technique observed in the wild. No patch available; requires configuration and monitoring hardening.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [Dark Reading — Voice Callers Exploit BYOD to Reach Microsoft 365, Corporate Data](https://www.darkreading.com/threat-intelligence/voice-callers-exploit-byod-microsoft-365-corporate-data)

### AI Platform Abuse: Weaponized Artifacts and Shared Conversations
- **Description**: Threat actors are abusing trusted AI platforms (specifically Claude Artifacts and shared AI conversations) to host malicious content, poison search results, and deliver ClickFix-style social engineering lures that trick users into installing malware.
- **Impact**: Malware delivery via trusted AI platform domains, bypassing reputation-based defenses; credential theft via fake authentication prompts; drive-by compromise through poisoned search results.
- **Status**: Active campaigns observed by Huntress targeting AI platform users.
- **Severity**: medium
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [Bleeping Computer — How Threat Actors Are Turning Trusted AI Platforms Into an Attack Surface](https://www.bleepingcomputer.com/news/security/how-threat-actors-are-turning-trusted-ai-platforms-into-an-attack-surface/)

### Google Play Early Access Abuse for Deceptive Apps
- **Description**: Threat actors are misusing Google Play's Early Access program to distribute thousands of deceptive applications that promise money, rewards, casino winnings, and premium content. Early Access apps bypass full Play Store review, allowing malicious or scam applications to reach users.
- **Impact**: Large-scale distribution of scam and potentially malicious apps to Android users, leading to financial fraud, ad fraud, and potential malware installation.
- **Status**: Ongoing abuse of the Early Access program. Google's response not detailed in reporting.
- **Severity**: medium
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [The Hacker News — Google Play Early Access Abused to Push Thousands of Deceptive Android Apps](https://thehackernews.com/2026/09/google-play-early-access-abused-to-push.html)

### Surfshark VPN Internal Server Breach
- **Description**: Hackers accessed a Surfshark internal test server after a configuration error exposed it to the internet. The breach affected testing and proxy infrastructure.
- **Impact**: Potential exposure of internal testing data and proxy server configurations; no customer VPN traffic or credentials reportedly affected.
- **Status**: Breach confirmed by Surfshark; configuration error remediated.
- **Severity**: medium
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Surfshark VPN says hackers breached internal testing, proxy servers](https://www.bleepingcomputer.com/news/security/surfshark-vpn-says-hackers-breached-internal-testing-proxy-servers/)

### IDScan Data Breach: 153 Million Driver's Licenses
- **Description**: Identity verification company IDScan confirmed hackers accessed customer data stored in its cloud platform, linked to a database containing over 153 million driver's license scans.
- **Impact**: Massive exposure of personally identifiable information (PII) including driver's license images and associated identity data, enabling identity theft and fraud.
- **Status**: Breach confirmed; investigation ongoing.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — IDScan confirms breach tied to 153 million stolen driver’s licenses](https://www.bleepingcomputer.com/news/security/idscan-confirms-breach-tied-to-153-million-stolen-drivers-licenses/)

### Trezor Phishing Campaign Post-Brevo Breach
- **Description**: Following a breach at email service provider Brevo, phishing attacks targeted 347,000 Trezor hardware wallet users' email addresses. Approximately 2,500 users clicked malicious links.
- **Impact**: Credential theft and potential cryptocurrency wallet compromise for users who entered seed phrases or credentials on phishing sites.
- **Status**: Active phishing campaign leveraging breached contact data.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [Bleeping Computer — Trezor: 347,000 users targeted in phishing attacks after Brevo breach](https://www.bleepingcomputer.com/news/security/trezor-347-000-users-targeted-in-phishing-attacks-after-brevo-breach/)

## Affected Systems and Products

- **PaperCut NG/MF**: Versions prior to 26.0.5, 25.0.13, and 24.1.10. Print management software deployed across enterprise, education, and government environments on Windows, Linux, and macOS servers.
- **Cisco Secure Firewall Management Center (FMC)**: Versions affected by CVE-2026-20079 and companion RCE flaw. Centralized management appliances for Cisco Secure Firewall deployments in enterprise and service provider networks.
- **JFrog Artifactory**: Self-hosted instances prior to JFrog's security fixes (released before August 15, 2026). Repository managers embedded in CI/CD pipelines across software development organizations.
- **Sogou Input Method**: Windows versions containing the exploited flaw. Widely deployed Chinese-language input method editor (IME) on endpoints in China and Chinese-speaking communities globally.
- **Microsoft Windows Defender**: Versions vulnerable to the "ShieldCrash" zero-day. All Windows editions with Defender enabled (Windows 10, 11, Server 2019/2022/2025).
- **Google Chrome**: Versions vulnerable to the BlueMoon exploit kit's Chrome zero-day. Windows, macOS, and Linux Chrome installations prior to the undisclosed fix.
- **Check Point Security Gateways and Security Management**: Firewall appliances and management servers running vulnerable VPN certificate validation code. Enterprise and data center network perimeters.
- **GitLab**: Self-hosted and GitLab.com instances prior to the patch for CVE-2026-85706. DevSecOps platforms hosting source code, CI/CD pipelines, and artifacts.
- **Android OS**: Devices running versions susceptible to Gigabud (Work Profile abuse) and Mantax Otax (ransomware/spyware). Campaigns initially focused on Indonesian users but infrastructure suggests broader targeting.
- **Microsoft 365 / Graph API**: Tenants with BYOD enrollments and Graph API permissions. Identity and productivity platforms across corporate environments.
- **Anthropic Claude AI Platform**: Claude models (including Artifacts and shared conversations) abused as attack infrastructure. Cloud-hosted AI services accessible via API and web interface.
- **Google Play Early Access Program**: Android app distribution channel abused for deceptive/scam app delivery. Android devices with Play Store access globally.
- **Surfshark VPN Infrastructure**: Internal testing and proxy servers exposed via misconfiguration. VPN service provider backend infrastructure.
- **IDScan Cloud Platform**: Identity verification service cloud storage containing driver's license scans. Third-party identity verification service infrastructure.
- **Trezor / Brevo Email Infrastructure**: Trezor customer email lists exposed via Brevo breach; phishing infrastructure targeting hardware wallet users. Email marketing platform and cryptocurrency hardware wallet vendor ecosystems.

## Attack Vectors and Techniques

- **AI-Agentic Exploitation Campaigns**: Autonomous AI agents conduct end-to-end attack operations—reconnaissance, vulnerability scanning, exploit generation, lateral movement, and data exfiltration—at scale and speed unattainable by human operators. Observed in the PaperCut campaign where hundreds of AI agents compromised 440+ instances.
- **Vulnerability Chaining**: Attackers combine multiple flaws (e.g., two JFrog Artifactory vulnerabilities; two Cisco FMC vulnerabilities) to escalate from unauthenticated access to full administrative control and persistent backdoor implantation.
- **AI Model Weaponization**: Threat actors use frontier AI models (Claude) for automated exploit development, malware rewriting to evade detection, vulnerability research, propaganda generation, and mass surveillance data processing. Russian group GTG-20006 used Claude to rebuild malware after detection.
- **Trusted AI Platform Abuse**: Malicious content hosted on legitimate AI platform features (Claude Artifacts, shared conversations) exploits trust in AI provider domains to bypass reputation filters and deliver ClickFix-style social engineering payloads.
- **Input Method Editor (IME) Exploitation**: Flaws in widely deployed IMEs (Sogou) exploited via crafted links to achieve code execution in user context, bypassing traditional network perimeter defenses.
- **Android Work Profile Abuse**: Malware (Gigabud) creates a managed work profile on victim devices and installs a trojanized banking app inside it, leveraging Android's enterprise isolation to evade user-space malware scanners and security controls.
- **Early Access Program Abuse**: Attackers exploit Google Play's Early Access program—which has reduced review scrutiny—to distribute thousands of deceptive apps at scale before full publication.
- **Supply Chain Credential Theft via Compromised Email Providers**: Breach of an email service provider (Brevo) enables targeted phishing against downstream customers (Trezor users) using legitimate contact data.
- **Graph API Reconnaissance for BYOD Targeting**: Attackers enumerate Microsoft 365 tenants via Graph API to identify high-value BYOD-enrolled users, then handoff access to extortion groups (ShinyHunters) for data theft and ransom.
- **Zero-Day Exploit Kits for Espionage**: The BlueMoon kit packages Windows and Chrome zero-days for use by multiple cyber-espionage groups, indicating a shared exploitation framework or supplier.
- **Public Zero-Day Disclosure as Harassment**: Researcher "Nightmare-Eclipse" publishes Windows Defender zero-days (ShieldCrash) as part of a vendetta, lowering the barrier for malicious use.
- **Ransomware Deployment via Network Management Appliances**: Qilin ransomware deployed through compromised Cisco FMC appliances, turning security infrastructure into an attack distribution point.
- **Backdoor Implantation in Build Pipelines**: Compromised JFrog Artifactory instances backdoored to enable persistent supply chain access and malicious artifact injection.

## Threat Actor Activities

- **Suspected Russian-Speaking PaperCut Actor (AI-Agentic Campaign)**: Operates from IP 45.142.193[.]132 (linked to prior malicious activity). Deploys hundreds of AI agents to automate exploitation of PaperCut flaws, compromising 440+ instances across 395 organizations. Represents a new class of AI-native threat actor.
- **GTG-20006 (Russian State-Sponsored, Aligned with Midnight Blizzard)**: Uses Anthropic's Claude to rebuild malware after detection, maintaining operational continuity. Part of Anthropic's "Generative Threat Groups" designation. Conducts cyber espionage with AI-assisted workflow acceleration.
- **Multiple Generative Threat Groups (GTGs)**: Diverse state-sponsored and financially motivated actors identified by Anthropic abusing Claude for automated exploitation, data theft, weapons design, propaganda, and mass surveillance between December 2025–August 2026.
- **Three Distinct Cisco FMC Threat Clusters**: Identified by Cisco Talos. Includes ransomware operators deploying Qilin and state-sponsored groups conducting credential theft. All exploit CVE-2026-20079 and a companion RCE flaw.
- **UNC3569 (China-Linked)**: Exploited Sogou Input Method zero-day to deploy GRAYRABBIT backdoor in targeted campaigns. Attribution by Gen Digital.
- **BlueMoon Exploit Kit Operators (Multiple Cyber-Espionage Groups)**: Multiple APT groups deploying the BlueMoon kit leveraging Windows and Chrome zero-days. Indicates shared exploit provider or collaborative framework.
- **Nightmare-Eclipse (Disgruntled Researcher)**: Publishes Windows Defender zero-days (including "ShieldCrash") as part of a vendetta against Microsoft. Not financially motivated; seeks to embarrass vendor and force fixes through public disclosure.
- **GoldFactory Threat Group**: Delivers Gigabud banking trojan via Android Work Profile abuse, targeting Indonesian banking users. Sophisticated evasion of mobile security controls.
- **Mantax Otax Operators**: Deploy hybrid ransomware/spyware Android malware that encrypts files, steals data, and harasses victims. Active in Indonesia.
- **ShinyHunters (Extortion Group)**: Receives handoff access from initial access brokers who use Graph API to identify BYOD targets. Conducts data theft and extortion against corporate victims.
- **Conti Ransomware Gang (Historical)**: Ukrainian member sentenced to four years for role in 2021–2022 attacks. Indicates ongoing law enforcement pressure on ransomware ecosystems.
- **Unknown Actors (JFrog Artifactory, Check Point, GitLab, Surfshark, IDScan, Google Play Early Access)**: Exploitation or abuse observed but specific attribution not provided in source reporting.