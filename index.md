# Exploitation Report

Critical zero-day and recently disclosed vulnerabilities are experiencing widespread active exploitation across multiple platforms and systems. The most severe activity centers around an unpatched zero-day in the Gogs Git service that has already compromised over 700 servers worldwide, alongside multiple Chrome zero-day exploits and hard-coded cryptographic key vulnerabilities in Gladinet products. Threat actors are leveraging these vulnerabilities for remote code execution, unauthorized access, and system compromise, with particular focus on cloud services, development tools, and enterprise infrastructure.

## Active Exploitation Details

### Gogs Zero-Day Remote Code Execution
- **Description**: An unpatched zero-day vulnerability in Gogs, a self-hosted Git service, allows attackers to achieve remote code execution on Internet-facing instances. This vulnerability bypasses a previous RCE bug disclosed last year and has been exploited for months.
- **Impact**: Attackers can gain complete control of affected servers, with over 700 compromised instances identified across the internet
- **Status**: Currently unpatched and under active widespread exploitation

### Chrome High-Severity Zero-Day
- **Description**: An undisclosed high-severity vulnerability in Google Chrome browser that has come under active exploitation in the wild
- **Impact**: Allows attackers to execute arbitrary code through browser exploitation
- **Status**: Patched by Google in emergency security updates, marking the eighth Chrome zero-day fixed in 2025

### Gladinet Hard-Coded Cryptographic Keys
- **Description**: CentreStack and Triofox products contain hard-coded cryptographic keys that enable unauthorized access and code execution
- **Impact**: Attackers can gain unauthorized access to affected systems and execute arbitrary code, with nine organizations already confirmed compromised
- **Status**: Under active exploitation with confirmed victim organizations

### WinRAR Security Vulnerability
- **Description**: A security flaw in the WinRAR file archiver and compression utility that allows malicious exploitation
- **Impact**: Multiple threat groups are leveraging this vulnerability for attacks
- **Status**: Under active attack by multiple threat groups and added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2025-6218

### React2Shell Maximum Severity Flaw
- **Description**: A maximum-severity security flaw in React Server Components (RSC) that enables widespread exploitation
- **Impact**: Threat actors are delivering cryptocurrency miners and various malware families across multiple sectors
- **Status**: Under heavy exploitation across various industries

### .NET SOAPwn Framework Vulnerability
- **Description**: Exploitation primitives in the .NET Framework that can be leveraged through rogue WSDL files
- **Impact**: Enables file writes and remote code execution against enterprise-grade applications
- **Status**: Research disclosed exploitation methods for potential attacks

## Affected Systems and Products

- **Gogs Git Service**: Self-hosted Git service instances exposed to the internet (700+ confirmed compromised)
- **Google Chrome**: All versions prior to latest security updates released in December 2025
- **Gladinet CentreStack**: Enterprise file sync and share solutions
- **Gladinet Triofox**: File server modernization platform
- **WinRAR**: File archiver and compression utility across all affected versions
- **React Server Components**: Applications using RSC across multiple sectors
- **Microsoft Notepad++**: Text editor with WinGUp update tool vulnerability
- **.NET Framework**: Enterprise applications utilizing SOAP/WSDL functionality
- **VSCode Marketplace**: Developer environments with malicious extensions
- **PCIe 5.0+ Systems**: Hardware with Integrity and Data Encryption protocol vulnerabilities

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in widely-used software
- **Supply Chain Attacks**: Malicious VSCode Marketplace extensions targeting developers with trojans hidden in fake PNG files
- **Update Mechanism Compromise**: Exploitation of Notepad++ WinGUp update tool to push malicious executables
- **Hard-Coded Key Abuse**: Leveraging embedded cryptographic keys in enterprise software for unauthorized access
- **Browser-Based Attacks**: Chrome zero-day exploitation for code execution in web browsers
- **Social Engineering**: ConsentFix attacks abusing Azure CLI OAuth to hijack Microsoft accounts without passwords
- **Malware Distribution**: Using Google ads for ChatGPT and Grok guides to distribute AMOS infostealer malware
- **EDR Process Abuse**: Storm-0249 threat group weaponizing endpoint detection and response platforms
- **Command and Control**: NANOREMOTE malware using Google Drive API for hidden C2 communications

## Threat Actor Activities

- **Storm-0249**: Initial access broker conducting high-precision attacks by abusing EDR processes and Windows utilities for stealthy operations
- **WIRTE APT Group**: Advanced persistent threat targeting government and diplomatic entities across the Middle East using AshenLoader sideloading to install AshTag espionage backdoor
- **Multiple WinRAR Threat Groups**: Various threat actors actively exploiting WinRAR vulnerability for malicious campaigns
- **Pro-Russia Hacktivists**: Targeting US critical infrastructure through VNC connection compromises in operational technology systems
- **AMOS Infostealer Campaign**: Operators abusing Google search ads to distribute macOS malware through fake AI tool guides
- **VSCode Marketplace Attackers**: Conducting stealthy campaign with 19 malicious extensions since February targeting developers
- **React2Shell Exploiters**: Multiple threat actors leveraging RSC vulnerability to deploy cryptocurrency miners and malware across sectors