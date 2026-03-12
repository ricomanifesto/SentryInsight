# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms and systems, with CISA flagging an actively exploited n8n remote code execution vulnerability that affects over 24,700 exposed instances. Apple has responded to WebKit exploitation through the Coruna exploit kit by backporting security fixes to older iOS, iPadOS, and macOS devices. Additionally, threat actors are leveraging sophisticated supply chain attacks, including UNC6426's exploitation of compromised npm packages to gain AWS administrative access within 72 hours, while ransomware groups and nation-state actors continue aggressive campaigns against healthcare and critical infrastructure organizations.

## Active Exploitation Details

### n8n Remote Code Execution Vulnerability
- **Description**: Critical security flaw in the n8n workflow automation platform allowing remote code execution
- **Impact**: Attackers can execute arbitrary commands on compromised systems and access stored credentials
- **Status**: Actively exploited in the wild, CISA has added to Known Exploited Vulnerabilities catalog and ordered federal agencies to patch immediately

### Apple WebKit Vulnerability in Coruna Exploit Kit
- **Description**: Security flaw in WebKit being exploited through the Coruna exploit kit targeting older iOS devices
- **Impact**: Successful exploitation could allow attackers to compromise iOS, iPadOS, and macOS systems
- **Status**: Apple has backported security fixes to older versions of iOS, iPadOS, and macOS Sonoma

### nx npm Package Supply Chain Compromise
- **Description**: Supply chain attack targeting the nx npm package, leading to stolen credentials and keys
- **Impact**: Complete cloud environment compromise, including AWS administrative access
- **Status**: Previously compromised package exploited by UNC6426 to achieve full environment breach within 72 hours

### Microsoft Zero-Day Vulnerabilities
- **Description**: Two publicly known zero-day vulnerabilities among 84 total flaws patched in March Patch Tuesday
- **Impact**: Eight vulnerabilities rated as critical with potential for significant system compromise
- **Status**: Patches released through March 2026 Patch Tuesday updates

## Affected Systems and Products

- **n8n Workflow Automation Platform**: Over 24,700 instances remain exposed to active exploitation
- **Apple iOS/iPadOS/macOS**: Older versions targeted by Coruna WebKit exploit kit
- **WordPress Sites**: Elementor Ally plugin affecting 250,000+ installations with SQL injection vulnerability
- **Microsoft Windows**: 84 vulnerabilities including two public zero-days across various Windows components
- **Android Devices**: Six new malware families targeting Pix payments, banking apps, and crypto wallets
- **NPM Registry**: 88 malicious packages in PhantomRaven campaign targeting JavaScript developers
- **Rust Crates**: Five malicious packages masquerading as time utilities to steal developer secrets
- **AWS Cloud Environments**: Compromised through supply chain attacks on development tools

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Malicious packages in npm, Rust crates, and GitHub Actions to compromise development environments
- **WebKit Exploitation**: Coruna exploit kit targeting browser vulnerabilities in older Apple devices
- **SQL Injection**: WordPress plugin vulnerabilities allowing sensitive data theft
- **Remote Code Execution**: Critical n8n flaws enabling arbitrary command execution
- **Phishing Campaigns**: Advanced techniques designed to exhaust SOC analyst workloads
- **Zombie ZIP Technique**: New method to conceal malware payloads from security detection tools
- **Tag Poisoning**: GitHub Action compromise through malicious tag manipulation
- **EDR Evasion**: BlackSanta malware specifically designed to kill endpoint detection and response systems

## Threat Actor Activities

- **UNC6426**: Leveraged stolen npm credentials to achieve complete AWS environment compromise within 72 hours
- **BlackCat (ALPHV) Ransomware**: Continued operations with insider schemes involving DigitalMint employees as negotiators
- **INC Ransomware Group**: Targeting healthcare organizations across Oceania including Australia, New Zealand, and Tonga
- **Handala (Iranian-linked)**: Claimed responsibility for wiper malware attack against medical technology company Stryker
- **Chinese Nexus Actors**: Shifting focus to Qatar amid Iranian conflict, demonstrating rapid geopolitical pivot capabilities
- **PhantomRaven Campaign**: Ongoing supply chain attacks through malicious npm packages targeting JavaScript developers
- **Russian-speaking Actors**: Deploying BlackSanta EDR killer malware specifically targeting HR departments for over a year
- **Southeast Asian Scam Centers**: 150,000 accounts disabled by Meta in coordinated global law enforcement action