# Exploitation Report

Critical exploitation activity continues across multiple fronts with Microsoft confirming active exploitation of a Windows Shell vulnerability (CVE-2026-32202), while researchers have uncovered several significant security incidents including supply chain attacks targeting development environments, privilege escalation flaws in Microsoft's cloud infrastructure, and the discovery of pre-Stuxnet malware that rewrites the history of cyber sabotage. Notable threat actors including UNC6692, PhantomCore, and the ShinyHunters extortion group are actively targeting organizations with sophisticated attack techniques ranging from social engineering campaigns to supply chain compromises.

## Active Exploitation Details

### Windows Shell Vulnerability
- **Description**: A high-severity security flaw impacting Windows Shell that Microsoft has revised its advisory to acknowledge active exploitation
- **Impact**: Enables attackers to exploit the Windows Shell component for malicious activities
- **Status**: Patched by Microsoft, but confirmed to be actively exploited in the wild
- **CVE ID**: CVE-2026-32202

### Microsoft Entra ID Role Privilege Escalation
- **Description**: Administrative role designed for AI agents within Microsoft Entra ID contains a flaw that enables privilege escalation and identity takeover attacks
- **Impact**: Attackers can escalate privileges and take over service principal identities
- **Status**: Recently patched by Microsoft following disclosure by Silverfort researchers

### PhantomRPC Windows Privilege Escalation
- **Description**: Unpatched architectural weakness in Windows' Remote Procedure Call (RPC) mechanism that handles connections to unavailable services
- **Impact**: Enables privilege escalation through five different exploit paths
- **Status**: Currently unpatched vulnerability with multiple exploitation vectors identified

### TrueConf Video Conferencing Vulnerabilities
- **Description**: Multiple vulnerabilities in TrueConf video conferencing software actively exploited by PhantomCore hacktivist group
- **Impact**: Allows unauthorized access to video conferencing servers and network compromise
- **Status**: Actively exploited since September 2025 targeting Russian networks

## Affected Systems and Products

- **Microsoft Windows Shell**: Windows operating systems vulnerable to CVE-2026-32202
- **Microsoft Entra ID**: AI agent administrative roles susceptible to privilege escalation
- **Windows RPC Services**: All Windows systems with Remote Procedure Call mechanism
- **TrueConf Video Conferencing**: Servers running TrueConf software in Russian networks
- **OpenVSX Repository**: 73 malicious VS Code extensions delivering GlassWorm v2 malware
- **PyPI Package Index**: Elementary-data package with 1.1 million monthly downloads compromised
- **Robinhood Trading Platform**: Account creation process exploited for phishing campaigns
- **SimpleHelp Remote Support**: Added to CISA's Known Exploited Vulnerabilities catalog
- **Samsung MagicINFO 9 Server**: Vulnerabilities exploited in the wild
- **D-Link DIR-823X Routers**: Multiple router models with exploited vulnerabilities

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Attackers compromising popular software packages and development tools including PyPI packages and VS Code extensions
- **Social Engineering via Microsoft Teams**: UNC6692 threat group using legitimate business communication platforms to deploy Snow malware
- **Phishing Email Injection**: Exploitation of account creation processes to inject malicious content into legitimate service emails
- **SMS Blaster Attacks**: Use of devices that impersonate cellular towers to send phishing messages to nearby mobile devices
- **Fake CAPTCHA Schemes**: International Revenue Share Fraud (IRSF) campaigns using fake verification to trick users into sending premium SMS messages
- **Browser Extension Malware**: Deployment of malicious browser extensions as part of multi-stage attack campaigns
- **Cloud Infrastructure Abuse**: Utilization of AWS S3 buckets and other cloud services to host malicious payloads

## Threat Actor Activities

- **UNC6692**: Newly discovered threat actor combining social engineering through Microsoft Teams with custom Snow malware suite including browser extensions, tunneling tools, and backdoors
- **PhantomCore**: Pro-Ukrainian hacktivist group actively targeting Russian TrueConf video conferencing servers since September 2025
- **ShinyHunters**: Extortion group responsible for ADT data breach affecting 5.5 million individuals' personal information
- **GlassWorm Campaign**: Persistent information-stealing operation deploying 73 fake VS Code extensions on OpenVSX repository
- **Silk Typhoon**: Chinese state-sponsored group with member extradited to US for cyberespionage operations
- **Fast16 Operators**: Historical malware framework predating Stuxnet by five years, targeting engineering software with Lua-based components