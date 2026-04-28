# Exploitation Report

Critical vulnerabilities are actively being exploited across multiple platforms and systems, with Microsoft confirming active exploitation of CVE-2026-32202 affecting Windows Shell. The threat landscape is marked by sophisticated campaigns targeting robotics platforms, cloud services, and development environments. Notable activities include the PhantomCore hacktivist group exploiting TrueConf vulnerabilities in targeted attacks against Russian networks, and the emergence of GlassWorm v2 malware distributed through 73 malicious VS Code extensions. Supply chain attacks continue to proliferate with compromised PyPI packages and development tools being weaponized against developers and organizations.

## Active Exploitation Details

### Windows Shell Vulnerability
- **Description**: A high-severity security flaw impacting Windows Shell that Microsoft has now acknowledged is being actively exploited in the wild
- **Impact**: Attackers can exploit this vulnerability to compromise Windows systems through Shell interactions
- **Status**: Microsoft has revised its advisory to confirm active exploitation and released a patch
- **CVE ID**: CVE-2026-32202

### Hugging Face LeRobot Remote Code Execution
- **Description**: A critical unpatched security flaw in Hugging Face's LeRobot open-source robotics platform that allows unauthenticated remote code execution
- **Impact**: Attackers can execute arbitrary code remotely without authentication on systems running the popular robotics framework
- **Status**: Currently unpatched despite being publicly disclosed, leaving nearly 24,000 GitHub users potentially vulnerable
- **CVE ID**: CVE-2026-25874

### TrueConf Video Conferencing Vulnerabilities
- **Description**: Multiple vulnerabilities in TrueConf video conferencing software actively exploited by the PhantomCore hacktivist group
- **Impact**: Successful exploitation allows attackers to breach Russian networks and compromise video conferencing infrastructure
- **Status**: Actively exploited in ongoing campaigns since September 2025

### Microsoft Entra ID Role Privilege Escalation
- **Description**: An administrative role designed for AI agents within Microsoft Entra ID that could enable privilege escalation and identity takeover attacks
- **Impact**: Attackers can escalate privileges and take over service principal identities in Microsoft cloud environments
- **Status**: Microsoft has released a patch to address this vulnerability

### PhantomRPC Windows Privilege Escalation
- **Description**: An unpatched architectural weakness in Windows' Remote Procedure Call (RPC) mechanism that handles connections to unavailable services
- **Impact**: Local attackers can escalate privileges through five different discovered exploit paths
- **Status**: Currently unpatched with multiple exploitation methods identified

## Affected Systems and Products

- **Hugging Face LeRobot**: Open-source robotics platform with nearly 24,000 GitHub stars
- **Microsoft Windows Shell**: Windows operating systems vulnerable to active exploitation
- **Microsoft Entra ID**: Cloud identity and access management service, specifically AI agent roles
- **TrueConf**: Video conferencing software deployed across Russian networks
- **Windows RPC Services**: Core Windows Remote Procedure Call infrastructure
- **VS Code Extensions**: OpenVSX repository hosting 73 malicious extensions
- **PyPI Package Repository**: Elementary-data package with 1.1 million monthly downloads compromised
- **Robinhood Trading Platform**: Account creation process exploited for phishing campaigns
- **ADT Security Systems**: Home security platform affecting 5.5 million customers
- **Checkmarx**: Supply chain security company with GitHub repository data compromised
- **Medtronic**: Medical device systems with 9 million records allegedly stolen

## Attack Vectors and Techniques

- **Unauthenticated Remote Code Execution**: Direct exploitation of unpatched LeRobot platform vulnerabilities
- **Supply Chain Poisoning**: Malicious VS Code extensions and compromised PyPI packages targeting developers
- **Social Engineering via Legitimate Platforms**: Abuse of Microsoft Teams and AWS S3 buckets by UNC6692 threat actor
- **Phishing Email Injection**: Exploitation of Robinhood account creation process to send convincing phishing emails
- **SMS Blaster Attacks**: Use of fake cellular tower devices to send phishing SMS messages to nearby phones
- **Fake CAPTCHA Schemes**: International Revenue Share Fraud (IRSF) campaigns using deceptive CAPTCHA verification
- **Privilege Escalation via RPC**: Multiple exploitation paths through Windows RPC architectural weaknesses
- **Identity Takeover**: Abuse of Microsoft Entra ID AI agent roles for privilege escalation

## Threat Actor Activities

- **PhantomCore**: Pro-Ukrainian hacktivist group actively targeting Russian TrueConf video conferencing servers since September 2025
- **Silk Typhoon**: Chinese state-sponsored group with member Xu Zewei extradited to the U.S. for cyberespionage operations targeting COVID research
- **UNC6692**: Newly discovered threat actor combining social engineering, custom "Snow" malware, and cloud service abuse in multipronged campaigns
- **ShinyHunters**: Extortion group responsible for breaching ADT security systems and stealing 5.5 million customer records
- **GlassWorm Campaign Operators**: Persistent threat actors behind 73 malicious VS Code extensions delivering information-stealing malware
- **Elementary-data Package Attackers**: Threat actors who compromised popular PyPI package to distribute cryptocurrency wallet stealing malware
- **SMS Fraud Networks**: Criminal groups operating fake cellular tower equipment for large-scale phishing SMS campaigns