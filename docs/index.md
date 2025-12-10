# Exploitation Report

Critical exploitation activity is currently focused on multiple high-severity vulnerabilities across major enterprise platforms. Microsoft's December 2025 Patch Tuesday addressed 57 vulnerabilities including three zero-day flaws, with one actively exploited in the wild. North Korean threat actors have been observed exploiting the recently disclosed React2Shell vulnerability in React Server Components to deploy new EtherRAT malware. Additional urgent patches have been released by Fortinet, Ivanti, and SAP to address critical authentication bypass and code execution vulnerabilities. Ransomware operations continue to evolve with new techniques including the use of Shanya packer-as-a-service to evade endpoint detection and response solutions.

## Active Exploitation Details

### React2Shell Vulnerability in React Server Components
- **Description**: Critical vulnerability in React Server Components allowing remote code execution through malicious instructions in documents
- **Impact**: Enables threat actors to deploy malware and establish persistent access to compromised systems
- **Status**: Actively exploited by North Korean threat actors; exploitation activity has increased since public disclosure
- **CVE ID**: CVE-2025-55182

### Microsoft Windows Zero-Day Vulnerability
- **Description**: Actively exploited zero-day vulnerability in Windows operating systems addressed in December 2025 Patch Tuesday
- **Impact**: Allows attackers to compromise Windows systems with proof-of-concept exploit code publicly available
- **Status**: Actively exploited in the wild; patches available through KB5071546 extended security update

### Apache Tika Maximum Severity Vulnerability
- **Description**: Critical vulnerability in Apache Tika that was incompletely patched, requiring an updated advisory
- **Impact**: Allows attackers to achieve maximum-severity compromise of affected systems
- **Status**: Previously patched fix was insufficient; updated patches and advisory issued

### Gemini Enterprise No-Click Vulnerability
- **Description**: Critical vulnerability enabling attackers to add malicious instructions to common documents
- **Impact**: Allows exfiltration of sensitive corporate information without user interaction
- **Status**: Fixed by Google; previously allowed data exposure through document-based attacks

## Affected Systems and Products

- **Microsoft Windows**: All supported versions affected by zero-day vulnerability; patches available via KB5071546, KB5072033, and KB5071417 updates
- **React Server Components**: Applications using RSC framework vulnerable to React2Shell exploitation
- **Fortinet Products**: FortiOS, FortiWeb, FortiProxy, and FortiSwitchManager affected by FortiCloud SSO authentication bypass flaws
- **Ivanti Endpoint Manager**: EPM solution vulnerable to critical remote code execution flaw
- **SAP Products**: Multiple SAP products affected by three critical vulnerabilities across product range
- **Apache Tika**: Document processing framework requiring updated patches for maximum severity vulnerability
- **Google Gemini Enterprise**: AI platform previously exposed sensitive corporate data through document manipulation

## Attack Vectors and Techniques

- **React2Shell Exploitation**: North Korean actors leveraging RSC vulnerability to deploy EtherRAT malware with Ethereum smart contract communication
- **Document-Based Attacks**: Malicious instructions embedded in common documents to exfiltrate sensitive data
- **EDR Evasion**: Ransomware groups using Shanya packer-as-a-service to hide EDR killing operations and obfuscate malware
- **DLL Sideloading**: Storm-0249 using trusted Windows utilities and DLL sideloading for stealthy malware execution
- **Fileless PowerShell Attacks**: Advanced threat actors employing fileless techniques combined with ClickFix social engineering
- **Authentication Bypass**: Exploitation of FortiCloud SSO vulnerabilities to bypass authentication mechanisms

## Threat Actor Activities

- **North Korean Threat Actors**: Actively exploiting React2Shell vulnerability to deploy previously undocumented EtherRAT malware with five Linux persistence mechanisms
- **Storm-0249**: Ransomware initial access broker evolving tactics with domain spoofing, DLL sideloading, and fileless PowerShell techniques
- **STAC6565/Gold Blade**: Canadian-focused campaign deploying QWCrypt ransomware with 80% of attacks targeting Canadian organizations
- **Ransomware Operations**: Multiple ransomware gangs adopting Shanya packer-as-a-service for improved EDR evasion and malware obfuscation
- **Malware-as-a-Service**: Four distinct threat clusters leveraging CastleLoader malware through expanded GrayBravo infrastructure
- **Supply Chain Attacks**: Threat actors deploying malicious packages across VS Code, Go, npm, and Rust ecosystems to steal developer credentials and data