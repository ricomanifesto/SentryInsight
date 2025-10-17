# Exploitation Report

Critical vulnerability exploitation activity continues to escalate across multiple platforms, with threat actors actively targeting network infrastructure, enterprise applications, and development tools. Recent campaigns have exploited zero-day vulnerabilities in file-sharing software and networking devices, while ransomware groups are leveraging fraudulent code-signing certificates to distribute malware through trusted applications. North Korean threat actors are advancing their techniques by combining malware capabilities and utilizing blockchain smart contracts for malware distribution. The discovery of sophisticated rootkits targeting Linux systems and the exploitation of SNMP vulnerabilities in Cisco devices highlight the evolving threat landscape affecting enterprise infrastructure.

## Active Exploitation Details

### Gladinet CentreStack Zero-Day Vulnerability
- **Description**: A local file inclusion vulnerability in Gladinet's CentreStack business solution that was actively exploited as a zero-day
- **Impact**: Allows attackers to access sensitive files and potentially gain unauthorized system access
- **Status**: Patched by Gladinet after active exploitation was detected since late in the attack timeline
- **CVE ID**: CVE-2025-11371

### Cisco SNMP Remote Code Execution Vulnerability
- **Description**: A remote code execution flaw in Cisco IOS Software and IOS XE Software SNMP functionality
- **Impact**: Enables deployment of rootkits and complete system compromise on Cisco networking devices
- **Status**: Recently patched but actively exploited in "Zero Disco" campaign targeting unprotected Linux systems
- **CVE ID**: CVE-2025-20352

### WatchGuard Fireware Critical Security Flaw
- **Description**: A critical security vulnerability in WatchGuard Fireware that allows unauthenticated remote code execution
- **Impact**: Attackers can execute arbitrary code and potentially take over VPN devices
- **Status**: Recently patched, details disclosed by cybersecurity researchers

### Microsoft ASP.NET Core High-Severity Vulnerability
- **Description**: A vulnerability rated as the highest severity ever received by an ASP.NET Core security flaw
- **Impact**: Significant security risk to ASP.NET Core applications
- **Status**: Patched by Microsoft earlier this week

## Affected Systems and Products

- **Gladinet CentreStack**: File-sharing business solution vulnerable to local file inclusion attacks
- **Cisco IOS/IOS XE Devices**: Network switches and routers vulnerable to SNMP-based rootkit deployment
- **WatchGuard Fireware**: VPN and firewall devices susceptible to unauthenticated remote code execution
- **Microsoft ASP.NET Core**: Web application framework affected by critical vulnerability
- **F5 BIG-IP Instances**: Over 266,000 instances exposed online following security breach disclosure
- **Microsoft Visual Studio Code Marketplace**: Supply chain risks from exposed secrets in extensions
- **WordPress Sites**: Infected sites used for blockchain-based malware distribution
- **Microsoft Teams**: Targeted by fraudulent installers in ransomware campaigns

## Attack Vectors and Techniques

- **SNMP Exploitation**: Threat actors leveraging SNMP vulnerabilities to deploy LinkPro rootkits on Linux systems
- **EtherHiding Technique**: North Korean hackers hiding malware inside blockchain smart contracts for cryptocurrency theft
- **Blockchain Smart Contract Abuse**: UNC5142 threat group distributing information stealers through smart contracts
- **Fraudulent Code Signing**: Over 200 certificates used to sign malicious binaries in ransomware attacks
- **Email Bombing**: Exploitation of lax authentication in Zendesk to flood targeted inboxes
- **Magic TCP Packet Activation**: LinkPro rootkit uses eBPF technology and activates via specific TCP packets
- **Supply Chain Compromise**: Secrets exposed in VS Code marketplace creating development environment risks

## Threat Actor Activities

- **Vanilla Tempest**: Microsoft-tracked group using fraudulent certificates in Rhysida ransomware campaigns targeting Teams users
- **North Korean Groups**: Advanced campaigns combining BeaverTail and OtterCookie malware, utilizing EtherHiding and blockchain techniques for cryptocurrency theft
- **UNC5142**: Financially motivated threat actor distributing Atomic (AMOS), Lumma, and other information stealers via blockchain smart contracts
- **Zero Disco Campaign**: Attackers exploiting Cisco SNMP vulnerabilities to deploy sophisticated Linux rootkits on compromised infrastructure
- **Chinese Threat Actors**: Testing AI-optimized attack chains in operations targeting Taiwan
- **SIM Box Operation**: European law enforcement dismantled SIMCARTEL operation enabling over 3,200 fraud cases with 4.5 million euros in losses