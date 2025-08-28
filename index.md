# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms and systems, with several significant incidents demanding immediate attention. A zero-day vulnerability in FreePBX systems is being actively exploited against servers with exposed Administrator Control Panel interfaces, requiring emergency patching. The 's1ngularity' supply chain attack has compromised the nx build system, leading to the theft of 2,349 credentials from GitHub, cloud services, and AI platforms through malicious npm packages. Additionally, threat actors are leveraging AI services for automated data extortion campaigns, while the Storm-0501 group has evolved their operations to focus on cloud-based ransomware attacks and data theft.

## Active Exploitation Details

### FreePBX Zero-Day Vulnerability
- **Description**: A zero-day vulnerability affecting FreePBX systems with the Administrator Control Panel (ACP) exposed to the internet
- **Impact**: Allows attackers to compromise FreePBX servers and gain unauthorized access to telecommunications infrastructure
- **Status**: Actively exploited in the wild; emergency fix has been released by the Sangoma FreePBX Security Team

### 's1ngularity' Supply Chain Attack
- **Description**: Malicious versions of the nx build system npm package and auxiliary plugins were published to compromise developer environments
- **Impact**: Resulted in the theft of 2,349 credentials including GitHub tokens, cloud service credentials, and AI platform access keys
- **Status**: Attack has been identified and malicious packages removed; affected users need to rotate compromised credentials

### AI-Powered Data Extortion Campaign
- **Description**: Threat actors are abusing Anthropic's Claude Code service to automate reconnaissance, intrusions, and credential harvesting
- **Impact**: Enables automated and scalable data extortion operations with unprecedented efficiency
- **Status**: Ongoing campaign with threat actors using AI services "to an unprecedented degree"

### PromptLock AI-Powered Ransomware
- **Description**: First AI-powered ransomware using Lua scripts to steal and encrypt data across multiple operating systems
- **Impact**: Cross-platform data theft and encryption capabilities targeting Windows, macOS, and Linux systems
- **Status**: Experimental ransomware variant discovered by threat researchers

## Affected Systems and Products

- **FreePBX Systems**: Servers with Administrator Control Panel exposed to the internet
- **npm Ecosystem**: nx build system package and related auxiliary plugins
- **Developer Environments**: Systems using compromised nx packages in development workflows
- **Cloud Platforms**: GitHub, various cloud services, and AI platforms with compromised credentials
- **Anthropic Claude**: AI service being abused for automated attack operations
- **Multi-Platform Systems**: Windows, macOS, and Linux systems targeted by PromptLock ransomware

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched FreePBX vulnerability through exposed web interfaces
- **Supply Chain Compromise**: Injection of malicious code into legitimate npm packages to compromise downstream users
- **Credential Harvesting**: Automated collection of authentication tokens and API keys from compromised environments
- **AI-Assisted Automation**: Leveraging AI services to scale and automate traditional attack methodologies
- **Cross-Platform Ransomware**: Using Lua scripting to create portable ransomware capable of operating across different operating systems
- **Social Engineering**: ZipLine phishing campaign using reverse psychology where victims initiate contact first

## Threat Actor Activities

- **Storm-0501 Group**: Evolved operations from traditional device encryption to cloud-focused ransomware attacks, data theft, and extortion campaigns
- **'s1ngularity' Attackers**: Sophisticated supply chain compromise targeting the JavaScript/Node.js development ecosystem
- **AI-Assisted Threat Actors**: Leveraging Anthropic's Claude Code service for automated reconnaissance and credential harvesting operations
- **ZipLine Campaign Operators**: Running sophisticated phishing operations across multiple industry sectors affecting small, medium, and large organizations
- **PromptLock Developers**: Creating experimental AI-powered ransomware with cross-platform capabilities
- **Nevada State Cyberattackers**: Conducted successful attack against state government infrastructure, forcing shutdown of in-person services