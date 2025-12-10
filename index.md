# Exploitation Report

The current threat landscape shows significant exploitation activity across multiple critical vulnerabilities. Microsoft's December 2025 Patch Tuesday addressed three zero-day vulnerabilities, including one actively exploited in the wild. North Korean threat actors are exploiting the React2Shell vulnerability to deploy new EtherRAT malware, while ransomware groups are leveraging sophisticated packing services and EDR evasion techniques. Critical vulnerabilities have also been disclosed in SAP products, Fortinet's FortiCloud SSO systems, and Ivanti Endpoint Manager, requiring immediate attention from security teams.

## Active Exploitation Details

### Microsoft Zero-Day Vulnerabilities
- **Description**: Three zero-day vulnerabilities addressed in Microsoft's December 2025 Patch Tuesday, with one confirmed as actively exploited in the wild and two publicly disclosed
- **Impact**: Attackers can potentially achieve code execution and system compromise across Windows environments
- **Status**: Patches available through December 2025 security updates (KB5071546, KB5072033, KB5071417)

### React2Shell Vulnerability
- **Description**: Critical security flaw in React Server Components (RSC) that allows remote code execution
- **Impact**: Enables threat actors to deploy malware including the new EtherRAT implant and achieve persistent access to target systems
- **Status**: Actively exploited by North Korean threat actors with increasing attack activity
- **CVE ID**: CVE-2025-55182

### Apache Tika Maximum Severity Vulnerability
- **Description**: Critical vulnerability in Apache Tika where an earlier patch missed the full scope of the security flaw
- **Impact**: Allows attackers to achieve maximum-severity exploitation against affected Apache Tika installations
- **Status**: Updated advisory and patches released following incomplete initial fix

### Google Gemini Enterprise No-Click Vulnerability
- **Description**: Critical vulnerability allowing attackers to add malicious instructions to common documents
- **Impact**: Enables exfiltration of sensitive corporate information without user interaction
- **Status**: Fixed by Google following disclosure

## Affected Systems and Products

- **Microsoft Windows**: All supported versions affected by three zero-day vulnerabilities, patches available through KB5071546, KB5072033, and KB5071417
- **React Server Components (RSC)**: Applications using React framework vulnerable to remote code execution
- **SAP Products**: Multiple SAP solutions affected by 14 vulnerabilities including three critical-severity flaws
- **Fortinet Products**: FortiOS, FortiWeb, FortiProxy, and FortiSwitchManager vulnerable to FortiCloud SSO authentication bypass
- **Ivanti Endpoint Manager**: Critical remote code execution vulnerability in EPM solution
- **Apache Tika**: Maximum severity vulnerability affecting document processing capabilities
- **Google Gemini Enterprise**: Corporate AI platform vulnerable to prompt injection attacks
- **Visual Studio Code**: Malicious extensions targeting developer environments through VS Code Marketplace
- **Developer Package Repositories**: Malicious packages found in Go, npm, and Rust ecosystems

## Attack Vectors and Techniques

- **React2Shell Exploitation**: North Korean actors leveraging CVE-2025-55182 to deploy EtherRAT malware with five separate Linux persistence mechanisms
- **EtherRAT Communication**: Novel malware using Ethereum smart contracts for command and control communication
- **EDR Evasion**: Storm-0249 abusing endpoint detection and response solutions and trusted Windows utilities for stealthy malware execution
- **Shanya Packer-as-a-Service**: Ransomware groups using obfuscation services to hide EDR killing tools and malicious payloads
- **ClickFix Social Engineering**: Storm-0249 employing fake fix prompts to deliver fileless PowerShell attacks
- **DLL Sideloading**: Advanced threat actors using legitimate applications to load malicious libraries
- **Supply Chain Attacks**: Malicious packages in developer repositories targeting VS Code, Go, npm, and Rust environments
- **Indirect Prompt Injection**: Attacks against AI systems through malicious document content

## Threat Actor Activities

- **North Korean Actors**: Actively exploiting React2Shell vulnerability to deploy EtherRAT malware with sophisticated persistence and communication mechanisms
- **Storm-0249**: Evolved from initial access broker to full-scale ransomware operator using advanced techniques including domain spoofing, DLL sideloading, and fileless PowerShell attacks
- **STAC6565/Gold Blade**: Conducting targeted campaigns against Canadian organizations (80% of attacks) deploying QWCrypt ransomware
- **Spanish Teen Hacker**: 19-year-old arrested for stealing and attempting to sell 64 million personal records from nine companies
- **GrayBravo**: Expanding malware-as-a-service infrastructure with CastleLoader being used by four distinct threat clusters
- **Ransomware Groups**: Multiple organizations adopting Shanya packer-as-a-service to evade detection and disable security controls
- **Developer-Targeting Actors**: Threat groups distributing malicious extensions and packages across multiple development platforms to steal sensitive developer data