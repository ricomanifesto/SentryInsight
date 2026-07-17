# Exploitation Report

## Executive Summary

Critical exploitation activity this period centers on two actively exploited zero-day vulnerabilities now tracked in CISA's Known Exploited Vulnerabilities catalog. A Microsoft SharePoint Server remote code execution flaw (CVE-2026-58644) and two Fortinet FortiSandbox vulnerabilities are being weaponized in the wild, prompting emergency patching directives for federal agencies. Simultaneously, a newly released Windows zero-day exploit dubbed LegacyHive grants attackers administrative privileges on fully patched systems, with no vendor fix currently available.

North Korean threat actors linked to the Contagious Interview campaign have evolved their social engineering operations, embedding OtterCookie-aligned malware within SVG flag images delivered through fake coding tests. This steganographic technique bypasses traditional detection while targeting developers and job seekers. Meanwhile, the ClickFix social engineering framework continues to proliferate as a primary delivery vector for multiple malware families—including ACR Stealer, TELEPUZ, and new macOS threats like ClickLock—demonstrating the durability of user-interaction-dependent attack chains.

Ransomware operations maintain disruptive impact across critical sectors. The Fairlife subsidiary of Coca-Cola experienced production halts across U.S. dairy operations following a ransomware incident, while the Scattered Spider cybercrime collective saw two members sentenced for the 2024 Transport for London intrusion that caused £29 million in damages. Law enforcement actions also advanced against REvil affiliates, with an extradition request leading to a detention in Armenia. These developments underscore the convergence of active vulnerability exploitation, sophisticated social engineering, and persistent ransomware threats across both enterprise and consumer environments.

## Active Exploitation Details

### Microsoft SharePoint Server RCE Zero-Day (CVE-2026-58644)
- **Description**: A remote code execution vulnerability in Microsoft SharePoint Server that allows unauthenticated attackers to execute arbitrary code on affected servers. The flaw was patched by Microsoft in July 2026 and immediately added to CISA's Known Exploited Vulnerabilities catalog due to confirmed active exploitation.
- **Impact**: Attackers can achieve full server compromise, leading to data theft, lateral movement within organizational networks, deployment of persistent backdoors, and potential ransomware deployment across connected systems.
- **Status**: Actively exploited in the wild. Microsoft has released security updates. CISA has mandated federal agencies to apply patches immediately per Binding Operational Directive requirements.
- **CVE ID**: CVE-2026-58644

### Fortinet FortiSandbox Actively Exploited Vulnerabilities
- **Description**: Two vulnerabilities in the Fortinet FortiSandbox threat detection platform that are being actively exploited. FortiSandbox is designed to detect advanced threats through dynamic analysis, making its compromise particularly impactful for organizational security posture.
- **Impact**: Successful exploitation could allow attackers to bypass threat detection capabilities, execute arbitrary code on the sandbox appliance, access analyzed malware samples and threat intelligence, and pivot to internal network segments.
- **Status**: Actively exploited. CISA has ordered federal civilian executive branch agencies to prioritize patching by an accelerated timeline. Fortinet has released patches for the affected versions.
- **CVE ID**: CVE IDs not specified in source articles

### Windows LegacyHive Zero-Day Privilege Escalation
- **Description**: A newly disclosed Windows zero-day exploit released by a security researcher using the handle "Nightmare Eclipse." The exploit, named LegacyHive, leverages a vulnerability in Windows registry hive handling to escalate privileges from standard user to SYSTEM/Administrator on up-to-date Windows systems.
- **Impact**: Attackers with initial foothold access can achieve full administrative control over the compromised host, disable security controls, install kernel-level persistence, access credential stores, and move laterally across the domain.
- **Status**: Zero-day — publicly disclosed with functional exploit code. No vendor patch available at time of reporting. Microsoft has not yet released a security update addressing this vulnerability.
- **CVE ID**: CVE ID not assigned or disclosed in source article

### n8n Token Exchange Authentication Bypass
- **Description**: A flaw in n8n's token exchange mechanism on Enterprise instances configured to trust multiple external token issuers. The vulnerability causes the platform to incorrectly match an incoming JWT to a local user account from a different trusted issuer, allowing authentication bypass.
- **Impact**: Attackers possessing a valid token from one trusted identity provider can authenticate as arbitrary users from another trusted identity provider within the same n8n instance, leading to unauthorized workflow access, data exposure, and potential workflow manipulation.
- **Status**: Vulnerability disclosed by n8n. Patches or mitigation guidance expected from vendor. Exploitation requires specific multi-issuer configuration.
- **CVE ID**: CVE ID not specified in source article

### Anthropic Claude Chrome Extension Click-Jacking Flaw
- **Description**: A vulnerability in the Claude for Chrome browser extension that allows malicious extensions to simulate user clicks and trigger predefined AI actions. The extension fails to properly validate the origin of interaction events.
- **Impact**: A compromised or malicious browser extension can abuse Claude's permissions and access to perform actions on behalf of the user, potentially accessing sensitive conversation data, triggering API calls, or manipulating AI-assisted workflows without user consent.
- **Status**: Vulnerability publicly disclosed. Anthropic has been notified. Patch timeline not specified in source article.
- **CVE ID**: CVE ID not specified in source article

## Affected Systems and Products

- **Microsoft SharePoint Server**: All versions prior to July 2026 security update. On-premises deployments primarily affected; SharePoint Online mitigated by Microsoft.
- **Fortinet FortiSandbox**: Affected versions prior to vendor patches. Appliance and virtual deployments used for advanced threat detection and sandboxing.
- **Microsoft Windows**: All supported Windows versions (Windows 10, Windows 11, Windows Server 2019/2022/2025) vulnerable to LegacyHive privilege escalation until patched.
- **n8n Workflow Automation Platform**: Enterprise instances configured with multiple external token issuers (OIDC/SAML providers). Cloud and self-hosted deployments affected.
- **Anthropic Claude for Chrome Extension**: Current extension versions prior to security update. Affects users who have installed the official Claude browser extension.
- **Apple macOS**: Versions supporting the ClickLock malware's Terminal-based execution and process termination techniques. Specific version range not disclosed.
- **Google Android**: Platform-level access to microphone, camera, and screen content — subject to EU regulatory order for third-party AI assistant access.
- **Coca-Cola Fairlife Systems**: Operational technology and production systems at Fairlife dairy facilities impacted by ransomware encryption.

## Attack Vectors and Techniques

- **ClickFix Social Engineering Lures**: Attackers compromise legitimate websites or create fake pages that display convincing browser/OS error messages instructing users to copy and paste malicious PowerShell commands into Run dialog or Terminal. Used to deliver ACR Stealer, TELEPUZ, and ClickLock malware. Relies on user trust in apparent system prompts.
- **SVG Steganography in Fake Job Interviews**: North Korean Contagious Interview campaign embeds malicious payloads within SVG flag images presented as coding test materials. Payloads decode at runtime to deliver OtterCookie-aligned malware. Targets developers via LinkedIn, GitHub, and freelance platforms with fake technical assessments.
- **Residential Proxy Rotation for Carding**: Cybercriminals source "clean" residential proxies (IP addresses associated with legitimate ISPs and human traffic patterns) to bypass fraud detection during credential stuffing and carding operations. Proxies combined with browser fingerprint spoofing to mimic genuine user sessions.
- **Text Salting Against AI Security Filters**: Phishing campaigns insert invisible Unicode characters, zero-width spaces, and homoglyphs into email content to evade LLM-based and traditional content filters while rendering identically to recipients. Over 1 million emails observed using this technique.
- **Token Exchange Confusion**: Exploitation of n8n's JWT matching logic when multiple identity providers are trusted. Attacker presents valid token from Issuer A to authenticate as victim user registered under Issuer B.
- **Browser Extension Click-Jacking**: Malicious Chrome extensions simulate user interaction events (clicks, keystrokes) targeting the Claude extension's UI elements to trigger AI actions without visible user consent.
- **macOS Process Termination Loop**: ClickLock malware terminates all visible user-space processes every 210 milliseconds via Terminal commands, forcing victims to enter their system password to regain control — which the malware then captures.
- **Ransomware Encryption of Production Systems**: Fairlife attack encrypted operational technology and business systems, halting physical dairy production — demonstrating IT/OT convergence risk.

## Threat Actor Activities

- **North Korean Contagious Interview Campaign**: State-linked actors conducting sustained social engineering operations targeting software developers and job seekers globally. Uses fake recruiting personas, coding challenges, and steganographic SVG payloads to deliver OtterCookie malware. Campaign active since at least 2024 with evolving delivery techniques.
- **Scattered Spider (UNC3944/Scatter Swine)**: Financially motivated cybercrime collective responsible for the 2024 Transport for London intrusion causing £29M in damages. Two members (Owen Flowers, 18; Thalha Jubair, 20) sentenced to 5.5 years each in July 2026. Known for SIM swapping, social engineering, and SaaS/identity provider targeting.
- **REvil/Sodinokibi Ransomware Affiliates**: Russian-speaking ransomware-as-a-service operation. U.S. extradition request led to detention of Aleksandr Ermakov in Armenia (identity contested by defense). Ongoing law enforcement pressure on affiliate network.
- **ACR Stealer Operators**: Infostealer campaign active since 2024 leveraging ClickFix for initial access. Targets browser credential stores, session tokens, Microsoft 365 documents, and OneDrive-synced files. Focus on enterprise data exfiltration.
- **GoSerpent Espionage Actors**: Previously undocumented malware framework targeting Southeast Asian government and diplomatic entities since late 2025. Modular Go-based implant with espionage-focused capabilities. Attribution not publicly assigned; operational focus suggests state-aligned interest.
- **Fairlife Ransomware Actors**: Unidentified ransomware group that disrupted Coca-Cola's Fairlife dairy production across the United States. Attack impacted operational technology/production systems, not just IT. Ransomware variant and group affiliation not disclosed.
- **OkoBot Framework Operators**: Developers and distributors of a modular malware framework deploying 20+ payloads focused on cryptocurrency wallet seed phrases, credentials, and sensitive data. Distribution vectors not fully detailed in source.
- **TELEPUZ Malware Operators**: Modular malware campaign spreading via ClickFix-infected websites since April 2026. Full-featured implant with data theft and command execution capabilities. Actor identity unknown.
- **ClickLock Developers**: Creators of macOS info-stealer using aggressive process termination to coerce password entry. Delivered via pasted Terminal commands. Origin and distribution scale not fully characterized.

## Source Attribution

- **Ernst \& Young discloses data breach after support system hack**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/ernst-and-young-discloses-data-breach-after-support-system-hack/
- **Inside the Search for "Clean" Residential Proxies for Carding**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/inside-the-search-for-clean-residential-proxies-for-carding/
- **Fake Coding Tests Deliver OtterCookie-Aligned Malware Hidden in SVG Flag Images**: The Hacker News - https://thehackernews.com/2026/07/north-korea-linked-hackers-hide.html
- **Gold Eagle Clearinghouse Targets Security Gap, But How Is Unclear**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/gold-eagle-clearinghouse-targets-security-gap
- **Google Bets 'Agentic Defense' Strategy Can Outpace Attackers**: Dark Reading - https://www.darkreading.com/cloud-security/google-bets-agentic-defense-strategy-outpace-attackers
- **E.U. Orders Google to Open Android Mic, Camera and Screen to Rival AI Assistants**: The Hacker News - https://thehackernews.com/2026/07/eu-orders-google-to-open-android-mic.html
- **The Race to Field Military Autonomy Is On, Can Trusted Information Infrastructure Keep Pace?**: The Hacker News - https://thehackernews.com/2026/07/the-race-to-field-military-autonomy-is.html
- **New Windows LegacyHive zero-day gives hackers admin privileges**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-windows-legacyhive-zero-day-exploit-grants-hackers-admin-access/
- **Armenia Detains Russian Tourist on U.S. Warrant for REvil Hacker, Lawyers Say Wrong Man**: The Hacker News - https://thehackernews.com/2026/07/armenia-detains-russian-tourist-on-us.html
- **Windows Server 2022 reach end of mainstream support in 90 days**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/windows-server-2022-reach-end-of-mainstream-support-in-90-days/
- **ACR Stealer Uses ClickFix Lures to Steal Browser Tokens and Microsoft 365 Files**: The Hacker News - https://thehackernews.com/2026/07/acr-stealer-uses-clickfix-lures-to.html
- **New GoSerpent Malware Targets Southeast Asian Governments and Diplomats for Espionage**: The Hacker News - https://thehackernews.com/2026/07/new-goserpent-malware-targets-southeast.html
- **US charges two over laundering $43 million from investment fraud**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/us-charges-two-over-laundering-43-million-from-investment-fraud/
- **CISA urges immediate action on actively exploited Fortinet flaws**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-warns-feds-to-patch-exploited-fortinet-fortisandbox-flaws-by-sunday/
- **CISA Adds Exploited SharePoint RCE Zero-Day CVE-2026-58644 to KEV**: The Hacker News - https://thehackernews.com/2026/07/cisa-adds-exploited-sharepoint-rce-zero.html
- **New ClickLock macOS malware traps users into revealing login password**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-clicklock-macos-malware-traps-users-into-revealing-login-password/
- **Coca-Cola says Fairlife ransomware attack halts US dairy production**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/coca-cola-says-fairlife-ransomware-attack-halts-us-dairy-production/
- **Agentic AI: Taming the Unpredictable**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/agentic-ai-untamable-ask-the-right-security-questions
- **1M+ Emails Use Hidden Text to Dupe AI Security Filters**: Dark Reading - https://www.darkreading.com/threat-intelligence/1m-emails-hidden-text-dupe-ai-security-filters
- **Claude Chrome extension flaw lets malicious extensions trigger AI actions**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/claude-chrome-extension-flaw-lets-malicious-extensions-trigger-ai-actions/
- **New OkoBot framework deploys 20 payloads to steal data, crypto**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-okobot-framework-deploys-20-payloads-to-steal-data-crypto/
- **Two Scattered Spider Hackers Get 5.5 Years Each for £29 Million TfL Hack**: The Hacker News - https://thehackernews.com/2026/07/two-scattered-spider-hackers-get-55.html
- **ThreatsDay: Game Cheat Spyware, 24-Hour Ransomware, Chrome Sync Stalking + 12 More Stories**: The Hacker News - https://thehackernews.com/2026/07/threatsday-game-cheat-spyware-24-hour.html
- **AI Agents Broke the Security Playbook. Here's What Replaces It.**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/ai-agents-broke-the-security-playbook-heres-what-replaces-it/
- **23andMe to pay $18 million in new genetics data breach settlement**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/23andme-to-pay-18-million-in-new-genetics-data-breach-settlement/
- **n8n Token Exchange Flaw Could Let Attackers Log In as Users From Another Issuer**: The Hacker News - https://thehackernews.com/2026/07/n8n-token-exchange-flaw-could-let.html
- **New TELEPUZ Malware Spreads via ClickFix to Steal Data and Run Commands**: The Hacker News - https://thehackernews.com/2026/07/new-telepuz-malware-spreads-via.html
- **New ClickLock macOS Stealer Kills Apps Every 210ms Until Victims Type Their Password**: The Hacker News - https://thehackernews.com/2026/07/new-clicklock-macos-stealer-kills-apps.html
- **Scattered Spider members behind TfL hack get five years in prison**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/scattered-spider-members-behind-transport-for-london-hack-get-five-years-in-prison/
- **Windows 11 24H2 Home and Pro reach end of support in 90 days**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/windows-11-24h2-home-and-pro-reach-end-of-support-in-90-days/
