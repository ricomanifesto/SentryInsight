# Exploitation Report

Critical zero-day exploitation activity has been identified affecting Citrix NetScaler infrastructure, with CVE-2025-7775 being actively exploited in the wild before patches were available. Additionally, significant threat actor campaigns are targeting government entities across Central Asia and APAC regions, while new AI-powered ransomware variants are emerging with advanced capabilities. OAuth token theft campaigns are also compromising major sales automation platforms, exposing sensitive customer data across multiple organizations.

## Active Exploitation Details

### Citrix NetScaler Remote Code Execution Vulnerability
- **Description**: Critical remote code execution flaw in Citrix NetScaler ADC and NetScaler Gateway products that allows attackers to execute arbitrary code remotely
- **Impact**: Complete system compromise, unauthorized access to network infrastructure, potential lateral movement within enterprise environments
- **Status**: Actively exploited as zero-day vulnerability before patches were released; fixes now available from Citrix
- **CVE ID**: CVE-2025-7775

### PromptLock AI-Powered Ransomware
- **Description**: New ransomware strain that leverages OpenAI models to render and execute malicious code in real time, representing a significant evolution in ransomware capabilities
- **Impact**: Dynamic code generation and execution, enhanced evasion techniques, rapid adaptation to security measures
- **Status**: Newly identified and actively spreading, marking the beginning of AI-enhanced ransomware attacks

### Salesloft OAuth Token Theft
- **Description**: Widespread data theft campaign targeting OAuth and refresh tokens through compromised Drift AI chat agent integrations
- **Impact**: Unauthorized access to Salesforce customer data, potential account takeovers, exposure of sensitive business information
- **Status**: Active campaign affecting multiple organizations using Salesloft platform

## Affected Systems and Products

- **Citrix NetScaler ADC**: All versions prior to latest security updates
- **Citrix NetScaler Gateway**: All versions prior to latest security updates
- **Salesloft Platform**: Users with Drift AI chat agent integrations
- **Salesforce Systems**: Customer data exposed through compromised OAuth tokens
- **Government Networks**: 36 government entities in Central Asia and APAC regions
- **Healthcare Services Group**: Over 624,000 individuals affected by data breach

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched Citrix NetScaler vulnerabilities for remote code execution
- **OAuth Token Theft**: Compromise of authentication tokens through third-party integrations
- **Telegram Bot Command and Control**: Use of Telegram infrastructure for managing compromised systems
- **AI-Enhanced Malware**: Real-time code generation and execution using machine learning models
- **Phishing Campaigns**: Email-based social engineering targeting government officials
- **Dynamic DNS Infrastructure**: Use of constantly changing DNS records to evade detection

## Threat Actor Activities

- **ShadowSilk Group**: Conducted targeted attacks against 36 government entities across Central Asia and APAC regions using sophisticated Telegram bot infrastructure for command and control operations
- **Blind Eagle Clusters**: Five distinct activity clusters targeting Colombian organizations using remote access trojans (RATs), phishing lures, and dynamic DNS infrastructure for persistent access
- **PromptLock Operators**: Cybercriminals deploying AI-powered ransomware with advanced evasion and adaptation capabilities
- **OAuth Campaign Actors**: Coordinated effort to steal authentication tokens from sales automation platforms, affecting multiple enterprise customers