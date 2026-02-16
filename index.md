# Exploitation Report

Critical exploitation activity is currently focused on several high-impact vulnerabilities across enterprise systems and social engineering campaigns. Most concerning is the active exploitation of Microsoft Configuration Manager (SCCM) vulnerabilities and Ivanti Endpoint Manager Mobile (EPMM) flaws, with CISA flagging these for immediate patching. A single threat actor is reportedly responsible for 83% of recent Ivanti RCE attacks. Additionally, BeyondTrust Remote Support and Privileged Remote Access products are facing active exploitation of a critical pre-authentication RCE vulnerability with a CVSS 9.9 rating. Beyond traditional vulnerabilities, threat actors are increasingly leveraging sophisticated social engineering through evolved ClickFix attacks that abuse DNS queries, Pastebin comments, and even Claude AI artifacts to deliver malware payloads.

## Active Exploitation Details

### Microsoft Configuration Manager (SCCM) Vulnerability
- **Description**: Critical remote code execution flaw in Microsoft Configuration Manager that was patched in October 2024
- **Impact**: Allows attackers to execute arbitrary code remotely on affected systems
- **Status**: Actively exploited in the wild; CISA has ordered federal agencies to secure systems immediately

### Ivanti Endpoint Manager Mobile (EPMM) Remote Code Execution Vulnerabilities
- **Description**: Two critical vulnerabilities in Ivanti EPMM allowing remote code execution
- **Impact**: Complete system compromise through remote code execution capabilities
- **Status**: Under active exploitation with one threat actor responsible for 83% of recent attacks

### BeyondTrust Remote Support and Privileged Remote Access RCE Vulnerability
- **Description**: Critical pre-authentication remote code execution vulnerability affecting BeyondTrust RS and PRA appliances
- **Impact**: Remote code execution without authentication required, enabling complete system compromise
- **Status**: Actively exploited in attacks following public proof-of-concept release; CVSS score of 9.9

## Affected Systems and Products

- **Microsoft Configuration Manager (SCCM)**: Enterprise system management platform used by federal agencies and organizations
- **Ivanti Endpoint Manager Mobile (EPMM)**: Mobile device management solution with widespread enterprise deployment
- **BeyondTrust Remote Support and Privileged Remote Access**: Remote access and privileged access management appliances
- **Google Chrome**: Browser targeted by malicious extensions stealing business data and browsing history
- **Windows 11 Commercial Systems**: Affected by boot failures following security updates
- **macOS Systems**: Targeted by infostealer malware through ClickFix campaigns using Claude AI artifacts

## Attack Vectors and Techniques

- **DNS-based ClickFix Attacks**: Threat actors abuse nslookup commands and DNS queries to retrieve PowerShell payloads, marking the first known use of DNS as a channel in ClickFix campaigns
- **Pastebin Comment Exploitation**: Malicious JavaScript distributed through Pastebin comments to hijack cryptocurrency transactions
- **Claude AI Artifact Abuse**: ClickFix campaigns leveraging Claude LLM artifacts combined with Google Ads to deliver macOS infostealers
- **Malicious Chrome Extensions**: Extensions designed to steal Meta Business Suite and Facebook Business Manager data
- **Fake Recruiter Campaigns**: North Korean threat actors targeting JavaScript and Python developers with cryptocurrency-related coding challenges containing malware
- **Google Groups Abuse**: Over 4,000 malicious Google Groups and 3,500+ Google-hosted URLs spreading Lumma Stealer and Ninja Browser malware
- **Physical Mail Social Engineering**: Traditional mail targeting Trezor and Ledger cryptocurrency wallet users

## Threat Actor Activities

- **Single Ivanti Attacker**: One threat actor responsible for 83% of recent Ivanti EPMM RCE exploitation, demonstrating focused and persistent targeting
- **UAT-9921**: Previously unknown threat actor deploying VoidLink malware framework against technology and financial services sectors
- **Russian Suspected Actor**: Google attributes CANFAIL malware attacks targeting Ukrainian organizations to suspected Russian threat actor
- **North Korean Groups**: Conducting fake recruiter campaigns targeting developers with malicious coding challenges
- **Multi-Nation Coordination**: China, Iran, Russia, and North Korea coordinating cyber operations against defense industrial base sector
- **CTM360-tracked Campaign**: Large-scale operation using Google infrastructure to distribute Lumma Stealer infostealer malware