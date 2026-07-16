# Exploitation Report

## Executive Summary

CISA has issued emergency directives for two actively exploited vulnerability sets affecting federal agencies and broader enterprise environments. Federal agencies have been ordered to patch a critical Oracle E-Business Suite flaw by Saturday, while administrators everywhere are warned that three SharePoint Server vulnerabilities are under active exploitation against Internet-exposed on-premises instances. Simultaneously, Mozilla confirmed that exploit code has been published for two critical Firefox flaws, including CVE-2026-15718, and Zoom has patched a critical account takeover vulnerability (CVE-2026-53412) in its Windows client and SDK that could be exploited by unauthenticated attackers.

Threat actor activity spans financially motivated crime, supply chain compromise, and emerging AI-assisted malware development. Russian-tracked actor UAT-11795 is distributing the Starland RAT through trojanized WebEx and Zoom installers, while the "bandcampro" operator abuses Google's Gemini CLI as a hacking agent and botnet controller. A new ransomware group, Spirals, demonstrates unprecedented speed—completing initial access through encryption in under 24 hours. The AsyncAPI npm supply chain attack delivered multi-stage botnet malware through four compromised packages, and the OkoBot framework has targeted Ledger and Trezor hardware wallet users since April 2025 with seed-phrase phishing modules.

Research disclosures reveal expanding attack surfaces in developer tooling, IoT devices, and AI systems. A Windows zero-day PoC (LegacyHive) targeting the User Profile Service was released hours after Patch Tuesday by researcher Chaotic Eclipse. Cursor IDE on Windows executes any `git.exe` found in a cloned repository root without warning, enabling silent code execution. Nearly a dozen revoked UEFI shim bootloaders remained trusted for years, creating a persistent Secure Boot bypass path. The Shark RV2320EDUS robot vacuum exposes a region-wide remote control flaw via certificate extraction, and the "PromptFiction" vulnerability in Claude demonstrated how prompt injection can chain into end-to-end system compromise.

## Active Exploitation Details

### Oracle E-Business Suite Critical Vulnerability
- **Description**: A critical vulnerability in the Oracle E-Business Suite financial application that is being actively exploited in the wild. CISA has issued an emergency directive requiring federal civilian executive branch agencies to secure their systems by Saturday.
- **Impact**: Attackers can compromise financial application systems, potentially leading to unauthorized access to sensitive financial data, fraudulent transactions, and lateral movement within enterprise networks.
- **Status**: Actively exploited. CISA emergency directive issued for federal agencies; patching urgently recommended for all organizations running Oracle E-Business Suite.
- **CVE ID**: Not specified in source article

### Microsoft SharePoint Server Vulnerabilities (Three Flaws)
- **Description**: Three vulnerabilities affecting Internet-exposed on-premises SharePoint Server installations. CISA warns that attackers are actively exploiting these flaws to compromise SharePoint servers.
- **Impact**: Successful exploitation allows attackers to hack on-premises SharePoint Server instances, potentially leading to data theft, credential harvesting, and internal documents, and further network compromise.
- **Status**: Actively exploited against Internet-exposed instances. CISA warning issued; immediate patching required for all Internet-facing SharePoint Server deployments.
- **CVE ID**: Not specified in source article

### Zoom Critical Account Takeover Vulnerability
- **Description**: A critical security flaw in Zoom Workplace for Windows, the Zoom desktop client, and the Zoom SDK for Windows that could be exploited by an unauthenticated party to hijack user accounts.
- **Impact**: Unauthenticated attackers can take over victim accounts, gaining access to meetings, recordings, contacts, and potentially sensitive corporate communications.
- **Status**: Patched. Zoom has released security updates addressing the vulnerability. Users and administrators should update immediately.
- **CVE ID**: CVE-2026-53412

### Firefox Critical Vulnerabilities (Including CVE-2026-15718)
- **Description**: Mozilla has released updates addressing two critical flaws in Firefox. For at least one of these vulnerabilities, exploit code has been published. CVE-2026-15718 is an invalid pointer dereference vulnerability.
- **Impact**: Critical remote code execution potential. Published exploit code increases immediate risk for unpatched browsers.
- **Status**: Patched in Firefox updates. Exploit code publicly available for at least one flaw; immediate browser update strongly advised.
- **CVE ID**: CVE-2026-15718

### Windows Zero-Day: LegacyHive (User Profile Service)
- **Description**: Security researcher Chaotic Eclipse (aka Nightmare-Eclipse) released a proof-of-concept exploit called "LegacyHive" targeting the Windows User Profile Service arbitrary hive loading functionality. The PoC was dropped hours after Microsoft's Patch Tuesday.
- **Impact**: Arbitrary hive loading in the User Profile Service could lead to privilege escalation, persistence, or remote code execution depending on attack vector.
- **Status**: Zero-day PoC publicly released. No patch mentioned in source; mitigation guidance pending from Microsoft.
- **CVE ID**: Not specified in source article

### AsyncAPI npm Supply Chain Attack
- **Description**: Five malicious versions of AsyncAPI packages were published to npm (Node Package Manager) in a supply-chain attack. Four compromised packages in the `@asyncapi` namespace deliver a multi-stage botnet loader with credential-stealing and remote access capabilities.
- **Impact**: Developers and CI/CD pipelines installing compromised packages receive a remote access trojan with info-stealing capabilities, leading to credential theft, environment compromise, and botnet enrollment.
- **Status**: Malicious packages identified by OX Security, SafeDep, Socket, and StepSecurity. Packages should be quarantined and removed; affected systems require full incident response.
- **CVE ID**: Not specified in source article

## Affected Systems and Products

- **Oracle E-Business Suite**: Financial application modules; specific versions not detailed in source. Internet-exposed or internally accessible instances at risk.
- **Microsoft SharePoint Server**: On-premises installations exposed to the Internet. All unpatched versions vulnerable to the three actively exploited flaws.
- **Zoom Workplace for Windows / Zoom Desktop Client / Zoom SDK for Windows**: Versions prior to the security update containing the fix for CVE-2026-53412.
- **Mozilla Firefox**: All versions prior to the critical security update addressing CVE-2026-15718 and a second critical flaw. Exploit code published for at least one.
- **Google Chrome**: Updated in coordinated release; specific CVEs not detailed in source snippet.
- **Adobe Products**: Multiple products updated for critical flaws; specific applications and CVEs not detailed in source snippet.
- **VMware Products**: Multiple products updated for critical flaws; specific products and CVEs not detailed in source snippet.
- **Shark RV2320EDUS Robot Vacuum**: IoT device vulnerable to certificate extraction from flash storage, enabling cross-device root command execution within the same AWS region.
- **Cisco WebEx & Zoom (Trojanized Installers)**: Legitimate installer packages modified by threat actor UAT-11795 to deliver Starland RAT. Affects users downloading from compromised or spoofed sources.
- **AsyncAPI npm Packages (@asyncapi namespace)**: Four specific compromised package versions distributing multi-stage botnet malware. Developers and automated build systems using these packages.
- **Ledger & Trezor Hardware Wallets**: Devices targeted by OkoBot malware framework's seed-phrase phishing module on infected Windows hosts (active since April 2025).
- **Cursor IDE (Windows)**: Vulnerable to automatic execution of `git.exe` placed in a cloned repository's root directory. No user interaction or approval required.
- **Windows User Profile Service**: All Windows versions supporting the arbitrary hive loading functionality targeted by LegacyHive PoC.
- **UEFI Shim Bootloaders (Multiple Vendors)**: Nearly a dozen revoked but still-trusted shim bootloaders creating Secure Boot bypass opportunities on affected hardware.
- **Google Gemini CLI**: Open-source AI tool abused by threat actor "bandcampro" as a hacking agent and botnet operator.
- **Anthropic Claude**: "PromptFiction" vulnerability (now fixed) enabled malicious prompt chaining to AI agents when combined with another exploit.
- **TuxBot v3 Evolution IoT Botnet**: Targets Internet-of-Things devices; framework shows signs of LLM-assisted development.

## Attack Vectors and Techniques

- **Trojanized Legitimate Software Distribution**: Threat actor UAT-11795 distributes Starland RAT via modified WebEx and Zoom installers, leveraging trust in known software brands to achieve initial access and credential/cryptocurrency theft.
- **npm Supply Chain Compromise**: Attackers published malicious versions of AsyncAPI packages to the official npm registry, achieving automated deployment into developer environments and CI/CD pipelines with multi-stage botnet payloads.
- **Rapid Ransomware Deployment**: Spirals ransomware actor achieves full intrusion lifecycle—initial access, data theft, encryption—in under 24 hours, indicating highly automated or well-rehearsed operational playbooks.
- **IoT Certificate Extraction & Cross-Device Command Execution**: Physical or local access to a single Shark RV2320EDUS vacuum allows certificate extraction, enabling root command execution on other vacuums in the same AWS region (camera access, robot control, data reading).
- **AI/LLM Tool Weaponization**: Russian-speaking actor "bandcampro" repurposes Google's open-source Gemini CLI as an automated hacking agent and botnet command-and-control mechanism.
- **Hardware Wallet Seed Phrase Phishing**: OkoBot framework injects phishing prompts into Ledger Live and Trezor Suite applications on compromised Windows machines, tricking users into entering recovery phrases.
- **Prompt Injection Chaining**: "PromptFiction" vulnerability in Claude allowed malicious prompts to be automatically sent to AI agents; when combined with a second exploit, enabled end-to-end system compromise.
- **Developer Environment Hijack via Repository Cloning**: Cursor IDE on Windows automatically executes any `git.exe` found in a cloned repository's root—no clicks, approvals, or warnings—enabling silent code execution from malicious repositories.
- **Two-Click Developer Environment Takeover**: Simple, longstanding bugs in developer tooling allow attackers to access secrets and source-code-rich environments with minimal user interaction.
- **Windows User Profile Service Arbitrary Hive Loading (LegacyHive)**: Zero-day PoC exploits arbitrary hive loading in the User Profile Service for potential privilege escalation or code execution.
- **Secure Boot Bypass via Revoked UEFI Shim Bootloaders**: Nearly a dozen vulnerable, revoked shim bootloaders remained in the trusted database for years, allowing attackers to boot unsigned code and bypass Secure Boot protections.
- **Identity-Based Attacks & MFA Bypass**: Credential theft and phishing now surpass exploits as the top ransomware root cause; MFA was present in 97% of credential-based attacks but failed to prevent compromise.

## Threat Actor Activities

- **UAT-11795 (Russian, Financially Motivated)**: Distributes Starland RAT via trojanized WebEx and Zoom installers. Targets credentials and cryptocurrency. Active campaign leveraging software supply chain trust.
- **Spirals Ransomware Group**: New ransomware actor demonstrating extreme operational speed—initial access to encryption in under 24 hours. Corporate intrusions with data theft and encryption.
- **"bandcampro" (Russian-speaking)**: Abuses Google Gemini CLI as a hacking agent and to operate a small-scale botnet. Demonstrates novel AI tool repurposing for offensive operations.
- **OkoBot Operators**: Running malware framework on Windows since April 2025 with dedicated module for Ledger/Trezor hardware wallet seed-phrase phishing. Persistent, financially motivated credential theft.
- **AsyncAPI Supply Chain Attackers**: Compromised npm publishing credentials or build pipeline to inject malicious code into four `@asyncapi` packages. Delivered multi-stage botnet loader with info-stealing RAT capabilities.
- **TuxBot v3 Evolution Developers**: IoT botnet framework showing signs of LLM-assisted development. Represents evolution of automated malware authoring.
- **Iberian Hackers (€140M Fraud Ring)**: Conducted variety of cyberattacks and laundered proceeds through complex financial networks. Disrupted by Spanish police.
- **Dutch Investment Fraud Ring**: International scheme with tens of thousands of victims and over €100 million stolen. Multiple arrests by Dutch Police.
- **Chaotic Eclipse / Nightmare-Eclipse (Security Researcher)**: Released LegacyHive PoC for Windows User Profile Service zero-day hours after Patch Tuesday. Public disclosure accelerates exploitation risk.

## Source Attribution

- **CISA orders feds to patch actively exploited Oracle flaw by Saturday**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-actively-exploited-oracle-flaw-by-saturday/
- **Russian hackers trojanize WebEx, Zoom apps to push Starland malware**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/russian-hackers-trojanize-webex-zoom-apps-to-push-starland-malware/
- **AI Can Find Bugs, But Human Knowledge Still Proves Them**: The Hacker News - https://thehackernews.com/2026/07/ai-can-find-bugs-but-human-knowledge.html
- **New Spirals ransomware encrypts victim network in under 24 hours**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-spirals-ransomware-encrypts-victim-network-in-under-24-hours/
- **Unpatched Shark Vacuum Flaw Could Let Attackers Control Other Vacuums Region-Wide**: The Hacker News - https://thehackernews.com/2026/07/unpatched-shark-vacuum-flaw-could-let.html
- **OpenAI’s GPT-Red Automates Prompt Injection Testing to Harden GPT-5.6 Sol**: The Hacker News - https://thehackernews.com/2026/07/openais-gpt-red-automates-prompt.html
- **Zoom Patches Critical Windows Flaw That Could Enable Account Takeover**: The Hacker News - https://thehackernews.com/2026/07/zoom-patches-critical-windows-flaw-that.html
- **Police Disrupt a €140M Cyber Fraud Ring in Spain**: Dark Reading - https://www.darkreading.com/threat-intelligence/police-disrupt-140m-euro-cyber-fraud-ring-spain
- **Dutch police bust investment fraud ring stealing over €100 million**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/dutch-police-bust-investment-fraud-ring-stealing-over-100-million/
- **Forgotten Bootloaders Expose Secure Boot Blind Spot**: Dark Reading - https://www.darkreading.com/cyber-risk/forgotten-bootloaders-expose-secure-boot-blind-spot
- **Identity Attacks Overtake Exploits as Top Ransomware Cause**: Dark Reading - https://www.darkreading.com/identity-access-management-security/identity-attacks-overtake-exploits-top-ransomware-cause
- **Zoom warns of critical account takeover vulnerability**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/zoom-warns-of-critical-account-takeover-vulnerability/
- **TuxBot v3 Evolution Shows Signs of LLM-Assisted IoT Botnet Development**: The Hacker News - https://thehackernews.com/2026/07/tuxbot-v3-evolution-shows-signs-of-llm.html
- **Google Gemini CLI abused as a hacking agent, malware botnet operator**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/google-gemini-cli-abused-as-a-hacking-agent-malware-botnet-operator/
- **Guten Tag, Bonjour, Hola to Our European Cyber Defenders!**: Dark Reading - https://www.darkreading.com/threat-intelligence/guten-tag-bonjour-hola-european-cyber-defenders
- **Is 'Tech-xit' Imminent? UK Steps Up Sovereignty Push Amid AI Strife**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/tech-xit-uk-sovereignty-push-amid-ai-strife
- **AsyncAPI npm packages infected with credential-stealing malware**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/-asyncapi-npm-packages-infected-with-credential-stealing-malware/
- **OkoBot Malware Framework Injects Seed Phrase Phishing Into Ledger and Trezor Apps**: The Hacker News - https://thehackernews.com/2026/07/okobot-malware-framework-injects-seed.html
- **Claude Flaw Automatically Sends Malicious Prompts to AI Agents**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/claude-flaw-malicious-prompts-ai-agents
- **We built a vulnerability vending machine: AI tokens in, zero-days out**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/we-built-a-vulnerability-vending-machine-ai-tokens-in-zero-days-out/
- **Firefox, Chrome, Adobe, and VMware Updates Fix Multiple Critical Security Flaws**: The Hacker News - https://thehackernews.com/2026/07/firefox-chrome-adobe-and-vmware-updates.html
- **2-Click Cursor Exploit Enables Dev Environment Takeover**: Dark Reading - https://www.darkreading.com/application-security/2-click-cursor-exploit-dev-environment-takeover
- **SASE Has An AI Blind Spot. Inspecting Packets Is No Longer Enough.**: The Hacker News - https://thehackernews.com/2026/07/sase-has-ai-blind-spot-inspecting.html
- **Researcher Drops New Windows Zero-Day PoC Hours After Microsoft Patch Tuesday**: The Hacker News - https://thehackernews.com/2026/07/researcher-drops-new-windows-zero-day.html
- **New Webinar: Closing the Approval Gap in AI-Era Ad Tech**: The Hacker News - https://thehackernews.com/2026/07/new-webinar-closing-approval-gap-in-ai.html
- **Cursor Flaw Lets Malicious Cloned Repositories Trigger Windows Code Execution**: The Hacker News - https://thehackernews.com/2026/07/cursor-flaw-lets-malicious-cloned.html
- **CISA warns admins to patch actively exploited SharePoint flaws**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-warns-admins-to-patch-actively-exploited-sharepoint-flaws/
- **Compromised AsyncAPI npm Packages Deliver Multi-Stage Botnet Malware**: The Hacker News - https://thehackernews.com/2026/07/compromised-asyncapi-npm-packages.html
- **Microsoft: Some Dell PCs shut down after recent Windows updates**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-some-dell-devices-shut-down-after-windows-update/
- **Nigeria Deepens Cybersecurity Efforts as Cybercriminals See More Profits**: Dark Reading - https://www.darkreading.com/cyber-risk/nigeria-cybersecurity-efforts-cybercriminals-profits
