# Exploitation Report

Critical vulnerabilities are being actively exploited across multiple platforms, with threat actors targeting enterprise systems through authentication bypasses, zero-day exploits, and sophisticated malware campaigns. The most significant exploitation activity involves FortiClient Enterprise Management Server systems being compromised to deliver credential-stealing malware, while a zero-day vulnerability in Gogs self-hosted Git services allows authenticated users to execute arbitrary code. Additionally, widespread malware-as-a-service operations are targeting mobile and desktop platforms across Latin America and beyond.

## Active Exploitation Details

### FortiClient EMS Authentication Bypass
- **Description**: Authentication bypass vulnerability in FortiClient Enterprise Management Server allowing unauthorized access to management systems
- **Impact**: Attackers can deliver credential-stealing malware and gain unauthorized access to enterprise endpoint management infrastructure
- **Status**: Vulnerability is patched but actively being exploited in ongoing campaigns
- **CVE ID**: CVE-2026-35616

### Gogs Remote Code Execution Zero-Day
- **Description**: Unpatched zero-day vulnerability in Gogs self-hosted Git service that allows remote code execution
- **Impact**: Any authenticated user can execute arbitrary code on affected systems under certain conditions
- **Status**: Currently unpatched zero-day vulnerability being actively exploited
- **CVE ID**: Not provided in source articles

## Affected Systems and Products

- **FortiClient Enterprise Management Server**: All vulnerable versions prior to latest patch affected by authentication bypass
- **Gogs Git Service**: Internet-facing instances vulnerable to zero-day remote code execution
- **Android Devices**: Targeted by BTMOB remote access trojan across Latin America
- **Windows Systems**: Affected by Grandoreiro banking trojan campaigns
- **macOS Systems**: Targeted by JINX-0164 threat actor using fake recruiter lures
- **High-Performance GPU Systems**: Targeted by cryptojacking malware through SEO poisoning
- **npm Registry Users**: Exposed to malicious packages targeting Claude AI user directories

## Attack Vectors and Techniques

- **Authentication Bypass Exploitation**: Direct exploitation of FortiClient EMS authentication flaws to deploy credential stealers
- **Zero-Day Exploitation**: Active exploitation of unpatched Gogs vulnerability for remote code execution
- **Malware-as-a-Service (MaaS)**: BTMOB RAT distributed through licensing model with no-code development interface
- **Social Engineering**: Fake recruitment campaigns targeting cryptocurrency firms with macOS malware
- **SEO Poisoning**: Coordinated campaign manipulating search results and AI chatbot recommendations to spread cryptojacking malware
- **Supply Chain Attacks**: Malicious npm packages designed to steal files from Claude AI user directories
- **Physical Intrusion**: Silent Ransom Group conducting in-person social engineering at law firms

## Threat Actor Activities

- **JINX-0164**: Previously undocumented threat actor targeting cryptocurrency organizations with recruitment-themed social engineering and macOS malware for digital asset theft
- **Silent Ransom Group**: Extortion gang conducting physical intrusions at law firms, using social engineering to access servers and databases
- **ShinyHunters**: Extortion gang claiming responsibility for Carnival Cruise data breach affecting nearly 6 million people
- **BTMOB Operators**: Cybercriminals offering Android remote access trojan as a service with custom phishing payload generation
- **Latin American Cybercriminals**: Multiple groups targeting government agencies to monetize citizen data, including recent exposure of 5.8 million Uruguayan citizen records
- **GPU Mining Groups**: Threat actors conducting coordinated SEO poisoning operations to distribute cryptojacking malware targeting high-performance systems