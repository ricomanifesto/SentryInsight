---
schema_version: 2
report_date: 2026-09-22
generated_at: 2026-09-22T11:24:41Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-22/
---
# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse platforms, with CISA adding two high-profile flaws to its Known Exploited Vulnerabilities catalog this week. A Windows Defender zero-day released by researcher Abdelhamid Naceri blocks antivirus updates, while CVE-2026-7273 in Zyxel GS1900 switches enables arbitrary command execution with SYSTEM privileges. WordPress faces two distinct core vulnerabilities—CVE-2026-93485 (Comment2Shell) allowing anonymous comment XSS to escalate to RCE via admin sessions, and a separate CSRF flaw dubbed Click2Shell with published proof-of-concept code. CISA also confirmed active exploitation of three Linux kernel vulnerabilities, one rated critical. These developments indicate aggressive targeting of infrastructure, endpoint, and web application layers by both researchers and threat actors.

North Korean threat groups continue expanding operations with significant financial impact. The Contagious Interview campaign has compromised over 30,000 devices across more than 100 countries, stealing $10.71 million from 7,000+ cryptocurrency wallets. Jade Sleet breached an Indian IT services provider using FLATROOF and ROOFDECK backdoors, while SideCopy extended its India-focused espionage to academic institutions via ReverseRAT spear-phishing. Simultaneously, supply chain attacks evolve: the indexed-btree npm package demonstrates runtime-based evasion of install-script defenses, and compromised Ribon application credentials enabled malicious script injection across BigCommerce merchant stores. ClickFix social engineering lures now deliver the previously undocumented ChainScript RAT with blockchain-based C2 rotation.

Emerging attack surfaces in AI tooling present novel risk vectors. Researchers escaped the OpenAI Codex sandbox to execute commands on host machines, while chained flaws in OpenAI's help forum and login systems enabled account takeover of staff credentials and internal repository access. A hidden Meta Muse setting on macOS can be manipulated by existing malware to redirect microphone input to attackers. These findings, alongside the abuse of a Microsoft-signed kernel driver in a fake LastPass installer to disable EDR, illustrate how trusted components and emerging technologies are being weaponized faster than defensive controls adapt.

## Active Exploitation Details

### Windows Defender Zero-Day (Antivirus Update Blocking)
- **Description**: Security researcher Abdelhamid Naceri (Nightmare Eclipse) released a zero-day exploit targeting Microsoft Defender that prevents antivirus definition updates from being applied, effectively disabling protection updates on affected systems.
- **Impact**: Attackers can persistently block Microsoft Defender from receiving signature and engine updates, leaving endpoints vulnerable to subsequent malware delivery without detection.
- **Status**: Zero-day exploit publicly released; no patch mentioned in source article.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [Bleeping Computer — New Windows Defender zero-day blocks Microsoft antivirus updates](https://www.bleepingcomputer.com/news/security/new-windows-defender-zero-day-blocks-microsoft-antivirus-updates/)

### Zyxel GS1900 Series Switch Buffer Overflow
- **Description**: A stack-based buffer overflow vulnerability in Zyxel GS1900 series switches tracked as CVE-2026-7273 (CVSS 8.8) that allows unauthenticated attackers to achieve arbitrary operating system command execution with SYSTEM-level privileges.
- **Impact**: Full device compromise with administrative access, enabling network pivoting, data theft, and persistent foothold in enterprise environments.
- **Status**: Patched by Zyxel; actively exploited in the wild per CISA KEV catalog inclusion; CISA ordered federal agencies to patch by Thursday.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-7273
- **Reporting**: [Bleeping Computer — CISA orders feds to patch Zyxel flaw exploited for data theft](https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-actively-exploited-zyxel-flaw-by-thursday/), [The Hacker News — Zyxel and Veeam Flaws Under Active Exploitation With Command and SYSTEM Access](https://thehackernews.com/2026/09/zyxel-and-veeam-flaws-under-active.html)

### WordPress Comment2Shell (CVE-2026-93485)
- **Description**: A WordPress core vulnerability allowing anonymous visitors to submit comments containing hidden malicious scripts. When a logged-in administrator views the comment, the script executes and achieves remote code execution on the server.
- **Impact**: Unauthenticated attackers can escalate to full server compromise via administrator session hijacking and RCE.
- **Status**: Patched in WordPress 7.1.1 released September 17; WordPress urged immediate updates.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: patch
- **CVE IDs**: CVE-2026-93485
- **Reporting**: [The Hacker News — WordPress Comment2Shell Flaw Can Turn Anonymous Comment XSS Into RCE via Admin Session](https://thehackernews.com/2026/09/wordpress-comment2shell-flaw-can-turn.html)

### WordPress Click2Shell CSRF Vulnerability
- **Description**: A cross-site request forgery vulnerability in WordPress Core component dubbed "Click2Shell" that enables attackers to execute PHP code on the server. Technical details and proof-of-concept exploit have been publicly published.
- **Impact**: Authenticated or unauthenticated attackers (depending on CSRF context) can achieve remote code execution on WordPress installations.
- **Status**: PoC publicly available; patch status not specified in source.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — WordPress Click2Shell flaw lets hackers execute PHP on the server](https://www.bleepingcomputer.com/news/security/wordpress-click2shell-flaw-lets-hackers-execute-php-on-the-server/)

### Linux Kernel Vulnerabilities (Three Flaws)
- **Description**: CISA alerted that threat actors are actively exploiting three distinct Linux kernel vulnerabilities, one of which carries a critical severity rating. Specific vulnerability details and CVE identifiers were not disclosed in the source article.
- **Impact**: Kernel-level compromise enabling privilege escalation, container escape, and persistent system access across Linux distributions.
- **Status**: Actively exploited per CISA; patch availability varies by distribution and kernel version.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — CISA alerts of active exploitation of three Linux kernel flaws](https://www.bleepingcomputer.com/news/security/cisa-alerts-of-active-exploitation-of-three-linux-kernel-flaws/)

### Meta Muse Assistant Hidden Setting Backdoor
- **Description**: A hidden configuration setting in Meta's Muse AI assistant on macOS can be modified by malware already present on the system to redirect microphone input—intended for the assistant—to an attacker-controlled destination instead.
- **Impact**: Local malware gains real-time audio interception capability, effectively converting the AI assistant into a surveillance backdoor.
- **Status**: Proof-of-concept demonstrated by researcher Patrick Wardle on September 21; no vendor patch mentioned.
- **Severity**: medium
- **Exploitation Status**: potential
- **Action**: monitor
- **Reporting**: [The Hacker News — One Hidden Meta Muse Setting Could Let Attackers Turn the AI Assistant Into a Backdoor](https://thehackernews.com/2026/09/one-hidden-meta-muse-setting-could-let.html)

### OpenAI Codex Sandbox Escape
- **Description**: Researchers discovered two methods to escape the OpenAI Codex sandbox environment, one of which allows arbitrary command execution on the host developer machine from the most locked-down configuration mode.
- **Impact**: Developers using Codex could have host systems compromised through sandboxed AI agent interactions, breaking the isolation boundary.
- **Status**: Both escape vectors patched by OpenAI following responsible disclosure.
- **Severity**: high
- **Exploitation Status**: not_observed
- **Action**: patch
- **Reporting**: [Bleeping Computer — Researchers escape OpenAI Codex sandbox to run commands on host](https://www.bleepingcomputer.com/news/security/researchers-escape-openai-codex-sandbox-to-run-commands-on-host/)

### Chained OpenAI Account Takeover Flaws
- **Description**: Researchers leveraged Anthropic's Claude Opus 5 to identify and chain two vulnerabilities—a bug in OpenAI's public help forum software and a weakness in OpenAI's login system—to compromise ChatGPT and Codex accounts of OpenAI employees and access an internal code repository.
- **Impact**: Full account takeover of privileged staff leading to internal source code exposure and potential supply chain compromise.
- **Status**: Discovered during security research; remediation status not specified beyond acknowledgment.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — Claude Opus 5 Helped Researchers Take Over OpenAI Staff Accounts via Chained Flaws](https://thehackernews.com/2026/09/claude-opus-5-helped-researchers-take.html)

## Affected Systems and Products

- **Microsoft Defender / Windows Defender**: All versions susceptible to update-blocking zero-day; Windows endpoints where Defender manages antivirus updates.
- **Zyxel GS1900 Series Switches**: All firmware versions prior to patched release; network infrastructure devices deployed in enterprise and SMB environments.
- **WordPress Core**: Versions prior to 7.1.1 affected by Comment2Shell (CVE-2026-93485); Click2Shell CSRF affects Core component with unspecified version range.
- **Linux Kernel**: Multiple kernel versions across distributions; specific affected versions not disclosed in CISA alert.
- **Meta Muse (macOS)**: macOS installations with Meta Muse AI assistant granted microphone access; requires pre-existing malware execution context.
- **OpenAI Codex**: Developer environments using Codex sandbox in locked-down mode; host machines running Codex agent.
- **OpenAI ChatGPT/Codex Accounts & Help Forum**: OpenAI employee accounts and internal systems; public help forum platform.
- **npm Ecosystem**: Developers and CI/CD pipelines consuming the malicious `indexed-btree` package (typosquat of legitimate `sorted-btree`).
- **BigCommerce Merchant Stores**: Stores with installed Ribon third-party applications using compromised credentials.
- **LastPass Authenticator (Fake Installer)**: Windows systems where users download and execute the trojanized installer from GitHub.

## Attack Vectors and Techniques

- **Antivirus Update Suppression**: Exploiting Windows Defender zero-day to permanently block signature and engine updates, blinding endpoint protection.
- **Network Device Buffer Overflow**: Unauthenticated stack-based buffer overflow (CVE-2026-7273) on Zyxel GS1900 switches yielding SYSTEM-level command execution.
- **Stored XSS to RCE via Admin Session (Comment2Shell)**: Anonymous comment injection with malicious script triggering RCE when administrator views moderation queue or post.
- **CSRF to RCE (Click2Shell)**: Cross-site request forgery against WordPress Core component enabling PHP code execution on server.
- **Kernel Exploitation**: Active exploitation of three Linux kernel flaws for privilege escalation and persistence; one critical-rated.
- **AI Assistant Configuration Manipulation**: Local malware modifies hidden plist/preference setting in Meta Muse to hijack microphone audio stream.
- **Sandbox Escape via AI Agent**: Crafted inputs to OpenAI Codex break isolation and execute commands on host developer machine.
- **Vulnerability Chaining with AI Assistance**: Using LLM (Claude Opus 5) to discover and chain help forum bug + login weakness for account takeover.
- **Runtime-Based npm Malware Evasion**: Malicious `indexed-btree` package hides payload in normal runtime execution rather than install/lifecycle scripts, bypassing static analysis and install-time defenses.
- **Supply Chain Credential Theft**: Compromised Ribon application credentials used to inject malicious scripts into BigCommerce merchant storefronts.
- **Microsoft-Signed Driver Abuse**: Fake LastPass installer deploys Microsoft Hardware Compatibility Program-signed kernel driver to disable AV/EDR before executing password stealer.
- **ClickFix Social Engineering**: Deceptive UI lures (fake CAPTCHAs, error pages) trick users into executing PowerShell commands that deploy ChainScript RAT.
- **Blockchain-Based C2 Rotation**: ChainScript RAT uses Polygon blockchain transactions to dynamically rotate command-and-control infrastructure.
- **Spear-Phishing with mshta.exe Abuse**: SideCopy uses malicious HTA files executed via `mshta.exe` to bypass script execution policies and deploy ReverseRAT.
- **Developer-Targeted Backdoors**: Jade Sleet deploys FLATROOF and ROOFDECK macOS backdoors via compromised IT service provider to access downstream developer networks.
- **Malware in Torrent Files**: Trojanized media files distributed via BitTorrent targeting users in Africa (Kenya, Uganda).

## Threat Actor Activities

- **Abdelhamid Naceri (Nightmare Eclipse)**: Independent security researcher publicly released Windows Defender zero-day exploit blocking antivirus updates; demonstrates ongoing research into anti-malware bypasses.
- **SideCopy**: Pakistan-nexus threat actor expanding India targeting from government to academic institutions; uses spear-phishing with mshta.exe-launched HTA payloads delivering ReverseRAT for persistent espionage.
- **Contagious Interview (North Korean)**: Large-scale campaign compromising 30,000+ devices across 100+ countries; stolen $10.71M from 7,000+ cryptocurrency wallets; targets web designers, engineers, and crypto specialists via fake interview lures and malicious npm packages.
- **Jade Sleet (North Korean)**: Attributed to breach of India-based IT services provider; deployed FLATROOF and ROOFDECK macOS backdoors; leverages software supply chain to reach developer networks downstream.
- **ShinyHunters**: Compromised and defaced Clop ransomware group's dark web leak site; claims possession of victim data potentially enabling re-extortion of organizations that previously paid ransoms.
- **Unknown Operators (ChainScript/ClickFix)**: Deploying previously undocumented ChainScript RAT via ClickFix lures masquerading as Spotify, Zoom Workplace, and Microsoft Teams installers; using Polygon blockchain for resilient C2 rotation.
- **Unknown Operators (indexed-btree)**: Published malicious npm package typosquatting `sorted-btree`; employs runtime-only malicious behavior to evade install-script scanning; package removed from registry after detection.
- **Unknown Operators (Ribon/BigCommerce)**: Compromised credentials for Ribon third-party applications; injected malicious scripts into BigCommerce merchant stores for data theft or skimming.
- **Unknown Operators (Fake LastPass)**: Distributing trojanized LastPass Authenticator installer on GitHub; leverages Microsoft-signed kernel driver to kill security agents before deploying credential stealer.