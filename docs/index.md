# Exploitation Report

Critical zero-day vulnerabilities are being actively exploited across multiple platforms, with attackers targeting everything from self-hosted Git services to Chrome browsers. The most significant ongoing exploitation involves an unpatched zero-day in Gogs that has compromised over 700 servers, a Chrome zero-day marking the eighth such vulnerability exploited this year, and cryptographic flaws in Gladinet products enabling remote code execution. Additionally, threat actors are leveraging legitimate AI platforms and social engineering tactics to distribute malware, while exploiting React Server Components vulnerabilities to deliver cryptocurrency miners across multiple sectors.

## Active Exploitation Details

### Gogs Zero-Day Remote Code Execution
- **Description**: An unpatched zero-day vulnerability in Gogs self-hosted Git service that bypasses a previous RCE bug disclosed last year
- **Impact**: Attackers can gain remote code execution on Internet-facing instances, leading to complete server compromise
- **Status**: Actively exploited for months with over 700 compromised instances; remains unpatched

### Chrome High-Severity Zero-Day
- **Description**: A high-severity security flaw in Google Chrome browser under active in-the-wild exploitation
- **Impact**: Allows attackers to exploit Chrome users through targeted attacks
- **Status**: Fixed in emergency Chrome security update; represents the eighth Chrome zero-day exploited in 2025

### Gladinet CentreStack/Triofox Cryptographic Flaw
- **Description**: Vulnerability stemming from hard-coded cryptographic keys in Gladinet's CentreStack and Triofox products
- **Impact**: Enables unauthorized access and remote code execution, affecting nine organizations
- **Status**: Actively exploited in ongoing attacks

### React2Shell Maximum-Severity Vulnerability
- **Description**: Critical security flaw in React Server Components (RSC) enabling widespread exploitation
- **Impact**: Allows delivery of cryptocurrency miners and various malware payloads across multiple sectors
- **Status**: Under heavy exploitation with continuous threat actor activity

### .NET SOAPwn Framework Flaw
- **Description**: Exploitation primitives in the .NET Framework that can be leveraged via rogue WSDL files
- **Impact**: Achieves file writes and remote code execution against enterprise-grade applications
- **Status**: Newly disclosed vulnerability with demonstrated exploitation techniques

## Affected Systems and Products

- **Gogs Self-Hosted Git Service**: Internet-facing instances with over 700 confirmed compromised servers
- **Google Chrome Browser**: All versions prior to the latest emergency security update
- **Gladinet CentreStack and Triofox**: Products using hard-coded cryptographic keys for secure remote file access
- **React Server Components**: Applications utilizing RSC across multiple industry sectors
- **Notepad++**: WinGUp update tool vulnerable to malicious update file injection
- **VSCode Marketplace**: 19 malicious extensions targeting developers since February
- **Android Devices**: Systems affected by DroidLock ransomware and screen-locking capabilities
- **PCIe 5.0+ Systems**: Hardware with Integrity and Data Encryption (IDE) protocol vulnerabilities

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in Gogs and Chrome
- **Hard-Coded Key Abuse**: Leveraging embedded cryptographic keys in Gladinet products for unauthorized access
- **SEO Poisoning**: Using Google search ads to redirect users to malicious ChatGPT and Grok conversations
- **Supply Chain Attacks**: Compromising VSCode extensions and hiding malware in dependency folders
- **Social Engineering**: ClickFix and ConsentFix attacks targeting Microsoft accounts via Azure CLI
- **Update Mechanism Abuse**: Exploiting software update processes to deliver malicious payloads
- **EDR Process Weaponization**: Abusing endpoint detection and response platforms for stealthy attacks
- **AI Platform Abuse**: Using legitimate AI services like Google Drive API for command-and-control operations

## Threat Actor Activities

- **WIRTE APT Group**: Targeting government and diplomatic entities in the Middle East using AshenLoader sideloading techniques to install AshTag espionage backdoor
- **Storm-0249**: Initial access broker conducting high-precision attacks by weaponizing EDR processes and Windows utilities
- **Unknown Threat Actors**: Exploiting Gogs zero-day for months to compromise hundreds of servers worldwide
- **AMOS Campaign Operators**: Distributing macOS infostealer malware through poisoned Google ads promoting AI chatbot guides
- **Pro-Russia Hacktivists**: Targeting US critical infrastructure through VNC connection compromises in operational technology systems
- **VSCode Marketplace Attackers**: Operating stealthy campaign with 19 malicious extensions targeting developers since February
- **NANOREMOTE Operators**: Using Google Drive API for command-and-control of Windows backdoor operations