# Exploitation Report

Critical vulnerabilities across multiple enterprise platforms are experiencing active exploitation, with threat actors focusing on remote code execution flaws in widely-deployed management systems. The most concerning activity involves coordinated attacks against Ivanti Endpoint Manager Mobile, BeyondTrust remote access solutions, and Microsoft Configuration Manager, with a single threat actor responsible for the majority of Ivanti exploitation attempts. Nation-state groups from China, Iran, Russia, and North Korea are conducting sophisticated operations against defense contractors using zero-day vulnerabilities in edge devices, while cybercriminals are leveraging social engineering tactics through fake recruitment campaigns and physical mail-based cryptocurrency theft schemes.

## Active Exploitation Details

### **Ivanti EPMM Critical Remote Code Execution Vulnerabilities**
- **Description**: Two critical vulnerabilities in Ivanti Endpoint Manager Mobile (EPMM) allowing remote code execution
- **Impact**: Full system compromise and potential network lateral movement
- **Status**: Actively exploited with one threat actor responsible for 83% of recent attacks

### **BeyondTrust Remote Access Critical RCE Vulnerability**
- **Description**: Critical pre-authentication remote code execution vulnerability in BeyondTrust Remote Support (RS) and Privileged Remote Access (PRA) products with CVSS 9.9 severity rating
- **Impact**: Pre-authentication remote code execution allowing complete system takeover
- **Status**: Active in-the-wild exploitation observed after proof-of-concept publication

### **Microsoft Configuration Manager (SCCM) Vulnerability**
- **Description**: Critical vulnerability in Microsoft Configuration Manager patched in October 2024
- **Impact**: System compromise and potential enterprise-wide lateral movement
- **Status**: Now confirmed as exploited in attacks, CISA has ordered federal agencies to patch immediately

### **Zero-Day Vulnerabilities in Edge Devices**
- **Description**: Multiple zero-day vulnerabilities in edge network devices targeting defense contractors
- **Impact**: Initial network access for espionage operations
- **Status**: At least two dozen zero-days burned by nation-state actors in recent campaigns

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Enterprise mobile device management platform experiencing coordinated exploitation
- **BeyondTrust Remote Support and Privileged Remote Access**: Remote access management solutions with critical pre-auth RCE vulnerability
- **Microsoft Configuration Manager (SCCM)**: Enterprise configuration management platform with newly exploited vulnerability
- **Edge Network Devices**: Various manufacturers' edge devices targeted with zero-day exploits
- **Google Chrome Extensions**: Malicious extensions targeting Meta Business Suite and Facebook Business Manager data
- **Cryptocurrency Hardware Wallets**: Trezor and Ledger users targeted through physical mail campaigns
- **Windows LNK Files**: New spoofing vulnerabilities allowing malicious payload deployment

## Attack Vectors and Techniques

- **Remote Code Execution**: Pre-authentication RCE attacks against enterprise management platforms
- **Social Engineering**: Fake recruiter campaigns targeting JavaScript and Python developers with cryptocurrency-related coding challenges
- **Physical Mail Campaigns**: Traditional postal mail used to target cryptocurrency wallet users with fake security notifications
- **Malicious Browser Extensions**: Chrome extensions designed to steal business data and browsing history
- **ClickFix Campaigns**: Abuse of Claude LLM artifacts and Google Ads to deliver macOS infostealers
- **BYOVD Attacks**: Bring Your Own Vulnerable Driver attacks exploiting Windows driver security gaps
- **Supply Chain Targeting**: Attacks on defense industrial base contractors to access classified information

## Threat Actor Activities

- **Single Dominant Actor**: One threat actor responsible for 83% of recent Ivanti EPMM exploitation attempts
- **Nation-State Operations**: Coordinated campaigns from China, Iran, Russia, and North Korea targeting defense contractors
- **UAT-9921**: Previously unknown threat actor deploying VoidLink malware framework against technology and financial sectors
- **North Korean Groups**: Conducting fake recruiter campaigns with cryptocurrency-themed development challenges
- **Russian Actor**: Suspected involvement in CANFAIL malware attacks against Ukrainian organizations using previously undocumented techniques
- **Qilin Ransomware Gang**: Confirmed data theft from Romania's national oil pipeline operator Conpet S.A.
- **Cryptocurrency Scammers**: Physical mail-based campaigns targeting Trezor and Ledger hardware wallet users