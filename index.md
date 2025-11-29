# Exploitation Report

Current threat activity shows significant exploitation across multiple vectors, with North Korean threat actors leading supply chain attacks against npm and Maven repositories, while new botnet malware targets IoT devices and cybercriminals leverage AI-powered tools for enhanced attack capabilities. Notable incidents include domain takeover vulnerabilities in Python packages, signature verification bypass flaws in cryptographic libraries, and sophisticated ransomware campaigns targeting managed service providers.

## Active Exploitation Details

### ShadowV2 Botnet IoT Exploitation
- **Description**: New Mirai-based botnet malware targeting IoT devices from multiple vendors including D-Link and TP-Link
- **Impact**: Device compromise and botnet recruitment using known vulnerability exploits
- **Status**: Actively exploiting known vulnerabilities in IoT devices

### Node-forge Signature Verification Bypass
- **Description**: Vulnerability in the popular JavaScript cryptography library allowing bypass of signature verifications
- **Impact**: Attackers can craft data that appears valid, bypassing cryptographic security controls
- **Status**: Fix has been released for the vulnerability

### Python Package Domain Takeover
- **Description**: Legacy Python bootstrap scripts in PyPI packages contain vulnerable code enabling domain takeover attacks
- **Impact**: Potential supply chain compromise of Python Package Index through domain takeover
- **Status**: Multiple PyPI packages affected with domain takeover risk

### Shai-Hulud v2 Supply Chain Attack
- **Description**: Second wave of supply chain attack compromising over 830 npm packages and spreading to Maven ecosystem
- **Impact**: Exposure of thousands of secrets and potential code injection into downstream applications
- **Status**: Actively compromising packages across multiple repositories

## Affected Systems and Products

- **D-Link IoT Devices**: Multiple device models targeted by ShadowV2 botnet exploits
- **TP-Link IoT Devices**: Various router and IoT device models under active exploitation
- **node-forge JavaScript Library**: Popular cryptography library with signature bypass vulnerability
- **npm Registry**: Over 830 packages compromised in Shai-Hulud v2 campaign
- **Maven Ecosystem**: Supply chain attack expanding from npm to Maven repositories
- **PyPI Python Packages**: Multiple packages vulnerable to domain takeover attacks
- **Microsoft Teams**: Guest access feature bypassing Defender for Office 365 protections
- **Windows 11**: Lock screen password option visibility issues following recent updates
- **GitLab Public Repositories**: Over 17,000 exposed secrets across 2,800 domains
- **French Football Federation**: Administrative management software compromised

## Attack Vectors and Techniques

- **Evil Twin WiFi Networks**: Creation of malicious wireless access points to steal traveler data at airports
- **Supply Chain Poisoning**: Injection of malicious code into popular package repositories (npm, Maven, PyPI)
- **Domain Takeover**: Exploitation of legacy bootstrap scripts to compromise package infrastructure
- **Cross-Tenant Exploitation**: Bypassing security controls through Microsoft Teams guest access features
- **IoT Device Compromise**: Exploitation of known vulnerabilities in internet-connected devices
- **Malicious Browser Extensions**: Chrome extensions injecting hidden cryptocurrency transfer fees
- **AI-Powered Malware Generation**: Use of unrestricted LLMs to create functional ransomware and attack tools
- **Prompt Injection Attacks**: Targeting AI-enabled browsers and applications with malicious prompts

## Threat Actor Activities

- **North Korean Hackers**: Deploying 197 npm packages to distribute updated OtterCookie malware as part of Contagious Interview campaign
- **Bloody Wolf**: Expanding Java-based NetSupport RAT attacks targeting Kyrgyzstan and Uzbekistan since June 2025
- **Qilin Ransomware Group**: Conducting sophisticated supply chain attack against South Korean MSP, resulting in 28-victim "Korean Leaks" data heist
- **Scattered LAPSUS$ Hunters**: Prolific cybercriminal group conducting mass extortion campaigns against major corporations
- **ShadowV2 Operators**: Using AWS outage as testing opportunity for new Mirai-based botnet malware
- **Cryptocurrency Thieves**: Deploying malicious Chrome extensions to inject hidden Solana transfer fees