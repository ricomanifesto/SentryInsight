# Exploitation Report

Current exploitation activity reveals a diverse threat landscape dominated by supply chain attacks, critical infrastructure vulnerabilities, and sophisticated social engineering campaigns. The Shai-Hulud v2 campaign has expanded from npm to Maven ecosystems, compromising over 830 packages and exposing thousands of secrets. Critical authentication bypass vulnerabilities in ASUS routers pose immediate risks to network infrastructure, while the Qilin ransomware group has executed a sophisticated supply chain attack against South Korea's financial sector through MSP compromise. Additionally, threat actors are increasingly leveraging AI technologies to enhance their attack capabilities, from deepfake creation to runtime malware evasion techniques.

## Active Exploitation Details

### ASUS AiCloud Authentication Bypass Vulnerability
- **Description**: Critical authentication bypass flaw in ASUS routers with AiCloud functionality enabled
- **Impact**: Attackers can bypass authentication mechanisms and gain unauthorized access to router systems
- **Status**: ASUS has released firmware patches to address nine security vulnerabilities including this critical flaw

### Node-forge Signature Verification Bypass
- **Description**: Vulnerability in the popular JavaScript cryptography library 'node-forge' that allows bypassing signature verifications
- **Impact**: Attackers can craft malicious data that appears valid, potentially compromising cryptographic operations
- **Status**: Fix has been released for the vulnerability

### OnSolve CodeRED Platform Compromise
- **Description**: Cyberattack against Crisis24's OnSolve CodeRED emergency notification platform
- **Impact**: Disruption of emergency alert systems used by state and local governments and police departments nationwide
- **Status**: Attack confirmed, systems disrupted

### Chrome Extension Solana Transfer Injection
- **Description**: Malicious Chrome Web Store extension that injects hidden Solana transfer fees into Raydium swap transactions
- **Impact**: Stealthy theft of cryptocurrency funds during legitimate transactions
- **Status**: Extension discovered on Chrome Web Store, actively stealing funds

## Affected Systems and Products

- **ASUS Routers**: AiCloud-enabled routers affected by critical authentication bypass vulnerability
- **Node-forge Library**: Popular JavaScript cryptography library with signature verification bypass flaw
- **OnSolve CodeRED**: Emergency notification platform serving state and local governments
- **Chrome Browser**: Malicious extension targeting Solana cryptocurrency transactions
- **npm and Maven Ecosystems**: Over 830 packages compromised in Shai-Hulud v2 supply chain attack
- **South Korean MSP Infrastructure**: Financial sector targets through managed service provider compromise
- **London Council Systems**: Royal Borough of Kensington and Chelsea and Westminster City Council IT systems
- **JSONFormatter and CodeBeautify**: Online tools exposing thousands of passwords and API keys

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Shai-Hulud v2 campaign spreading across package repositories to steal secrets and credentials
- **Social Engineering**: SocGholish fake update attacks delivering Mythic Agent malware to engineering companies
- **Ransomware as a Service**: Qilin ransomware leveraging MSP compromise for multi-victim attacks
- **Browser Extension Malware**: Malicious Chrome extensions performing cryptocurrency theft through transaction injection
- **AI-Enhanced Attacks**: Threat actors using large language models for runtime malware evasion and deepfake creation
- **Phishing Impersonation**: Cybercriminals impersonating financial institutions for account takeover attacks
- **Hardware-Based Attacks**: Cheap hardware modules bypassing AMD and Intel memory encryption protections

## Threat Actor Activities

- **Shai-Hulud Campaign Operators**: Expanded operations from npm to Maven ecosystems, compromising 830+ packages to steal credentials and secrets
- **RomCom Group**: First observed using SocGholish JavaScript loader to deliver Mythic Agent malware to U.S. civil engineering companies
- **Qilin Ransomware Group**: Executed sophisticated supply chain attack against South Korean MSP, leading to "Korean Leaks" data heist affecting 28 victims in financial sector
- **Scattered LAPSUS$ Hunters**: Prolific cybercriminal group conducting mass data theft and extortion campaigns against major corporations
- **DPRK FlexibleFerret**: Continuing "Contagious Interview" campaign with refined tactics targeting macOS users for credential theft
- **Financial Institution Impersonators**: Account takeover fraud schemes resulting in $262 million in losses since January 2025
- **Iranian Cyber Operations**: Deploying "cyber-enabled kinetic targeting" to support physical missile attacks against maritime and land-based targets