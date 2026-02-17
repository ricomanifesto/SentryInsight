# Exploitation Report

Critical exploitation activity is currently centered around several high-impact vulnerabilities across multiple platforms. A Chrome zero-day vulnerability (CVE-2026-2441) is being actively exploited in the wild, prompting emergency patches from Google. Additionally, CISA has issued urgent directives for federal agencies to patch a BeyondTrust Remote Support vulnerability within three days due to active exploitation. Threat actors are also heavily exploiting Ivanti Endpoint Manager Mobile vulnerabilities, with a single actor responsible for 83% of recent attacks. Meanwhile, social engineering campaigns have evolved to abuse DNS infrastructure through ClickFix attacks, and information-stealing malware campaigns are targeting AI agent configurations and cryptocurrency operations.

## Active Exploitation Details

### Chrome Zero-Day Vulnerability
- **Description**: High-severity vulnerability in Google Chrome browser affecting multiple versions
- **Impact**: Allows attackers to execute arbitrary code and compromise user systems through browser exploitation
- **Status**: Emergency patches released by Google, actively exploited in the wild
- **CVE ID**: CVE-2026-2441

### BeyondTrust Remote Support Vulnerability
- **Description**: Critical vulnerability in BeyondTrust Remote Support instances affecting government and enterprise systems
- **Impact**: Enables attackers to gain unauthorized remote access to systems and potentially execute commands
- **Status**: Actively exploited, CISA has ordered federal agencies to patch within three days

### Ivanti Endpoint Manager Mobile Vulnerabilities
- **Description**: Critical remote code execution vulnerabilities in Ivanti EPMM affecting mobile device management systems
- **Impact**: Allows attackers to execute arbitrary code remotely and potentially compromise entire mobile device infrastructures
- **Status**: Under active exploitation with a single threat actor responsible for 83% of recent attacks

## Affected Systems and Products

- **Google Chrome**: All versions prior to the latest security update containing CVE-2026-2441 patch
- **BeyondTrust Remote Support**: Remote support instances requiring immediate patching per CISA directive
- **Ivanti Endpoint Manager Mobile (EPMM)**: Mobile device management systems vulnerable to RCE attacks
- **OpenClaw AI Agent Framework**: Configuration files and gateway tokens being targeted by infostealers
- **Cloud Password Managers**: Bitwarden, Dashlane, and LastPass vulnerable to password recovery attacks under certain conditions
- **Chrome Browser Extensions**: 260,000+ users affected by fake AI browser extensions
- **Windows 11 Commercial Systems**: Systems experiencing boot failures after recent security updates

## Attack Vectors and Techniques

- **DNS-Based ClickFix Attacks**: Threat actors abuse DNS queries and nslookup commands to retrieve PowerShell payloads, representing the first known use of DNS as a channel in ClickFix campaigns
- **Social Engineering via Pastebin**: Attackers use Pastebin comments to distribute ClickFix-style attacks targeting cryptocurrency users with malicious JavaScript
- **Google Groups Abuse**: Over 4,000 malicious Google Groups and 3,500+ Google-hosted URLs used to spread Lumma Stealer infostealer malware
- **AI Chatbot Manipulation**: Businesses gaming AI chatbots through "Summarize with AI" prompts to manipulate recommendations
- **Fake Browser Extensions**: 30 copycat AI browser extensions tricking users and evading Google's detection systems

## Threat Actor Activities

- **Dominant Ivanti Attacker**: Single threat actor responsible for 83% of recent Ivanti EPMM exploitation attempts, demonstrating focused and persistent targeting
- **Phobos Ransomware Group**: Polish authorities arrested a 47-year-old suspect linked to the operation, with seized devices containing stolen credentials and credit card numbers
- **ShinyHunters Group**: Data extortion group claiming theft of over 600,000 Canada Goose customer records containing personal and payment data
- **GS7 Cyberthreat Group**: Operating "Operation DoppelBrand" campaign targeting US financial institutions with near-perfect imitations of corporate portals
- **ZeroDayRAT Operators**: New mobile spyware platform being advertised on Telegram for real-time surveillance and data theft capabilities
- **AI-Targeting Malware Campaigns**: Information stealers specifically designed to target OpenClaw AI agent configurations, marking the first observed targeting of this framework