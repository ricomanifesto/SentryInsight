# Exploitation Report

Critical exploitation activity has significantly escalated across multiple attack vectors, with North Korean threat actors leading sophisticated supply chain and social engineering campaigns. The most severe incidents include the exploitation of CVE-2025-55182 affecting 766 Next.js hosts for credential harvesting, the UNC1069 group's social engineering attack on the Axios npm package maintainer, and a massive $285 million theft from Drift Protocol through durable nonce manipulation. Device code phishing attacks have surged 37 times this year, while threat actors are increasingly using cookie-controlled PHP web shells for persistent access to Linux servers.

## Active Exploitation Details

### React2Shell Vulnerability in Next.js
- **Description**: A vulnerability in Next.js framework being exploited for large-scale credential harvesting operations
- **Impact**: Threat actors have successfully breached 766 Next.js hosts and stolen database credentials, SSH private keys, and Amazon Web Services credentials
- **Status**: Actively exploited in widespread campaigns
- **CVE ID**: CVE-2025-55182

### DarkSword iOS Exploitation Tool
- **Description**: A severe mobile operating system cracking tool targeting iOS devices
- **Impact**: Capable of compromising iOS security mechanisms and gaining unauthorized access to devices
- **Status**: Apple has broken precedent by patching this vulnerability in iOS 18, indicating the severity of the threat

### Device Code Phishing Exploitation
- **Description**: Abuse of OAuth 2.0 Device Authorization Grant flow to hijack user accounts
- **Impact**: Account takeover through sophisticated phishing techniques that bypass traditional authentication
- **Status**: Attacks have surged 37 times this year with new phishing kits spreading online

### Cookie-Controlled PHP Web Shell Attacks
- **Description**: Sophisticated web shells using HTTP cookies as control channels on Linux servers
- **Impact**: Remote code execution and persistent access through cron job persistence mechanisms
- **Status**: Increasingly used by threat actors for maintaining long-term access

## Affected Systems and Products

- **Next.js Framework**: 766 hosts confirmed compromised through CVE-2025-55182 exploitation
- **iOS Devices**: Affected by DarkSword exploitation tool, patched in iOS 18
- **OAuth 2.0 Implementations**: Systems using Device Authorization Grant flow vulnerable to phishing attacks
- **Linux Servers**: Running PHP applications susceptible to cookie-controlled web shell attacks
- **npm Ecosystem**: Axios package compromised through maintainer social engineering
- **Drift Protocol**: Solana-based decentralized exchange lost $285 million
- **European Commission Cloud**: TeamPCP breach exposed data of 30 EU entities
- **Zendesk Platform**: Support ticket breach affecting Hims & Hers customer data

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Social engineering targeting package maintainers and developers
- **Social Engineering**: Sophisticated campaigns using fake Microsoft Teams error messages
- **Device Code Phishing**: Abuse of OAuth flows with proliferating phishing kits
- **Web Shell Deployment**: Cookie-controlled PHP shells with cron persistence
- **Durable Nonce Manipulation**: Advanced cryptocurrency protocol exploitation
- **Malware Distribution**: Fake GitHub repositories exploiting Claude Code leaks
- **Browser Fingerprinting**: LinkedIn secretly scanning for Chrome extensions

## Threat Actor Activities

- **UNC1069 (North Korean)**: Orchestrated sophisticated social engineering campaign against Axios npm maintainer, part of broader supply chain targeting
- **TA416 (China-linked)**: Targeting European government and diplomatic organizations with PlugX malware and OAuth-based phishing since mid-2025
- **TeamPCP**: Conducted supply chain attacks affecting European Commission and multiple organizations, with involvement from ShinyHunters and Lapsus$ groups
- **Qilin Ransomware**: Attacked German political party Die Linke, forcing IT systems outage and threatening sensitive data leaks
- **North Korean Groups**: Executed $285 million theft from Drift Protocol using advanced social engineering and protocol manipulation
- **SparkCat Operators**: Distributed new malware variant through iOS and Android apps to steal cryptocurrency wallet recovery phrases