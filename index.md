# Exploitation Report

The current threat landscape is dominated by active exploitation of industrial control systems, sophisticated supply chain attacks, and evolving malware campaigns targeting critical infrastructure. CISA has added CVE-2021-26829, a cross-site scripting vulnerability in OpenPLC ScadaBR, to its Known Exploited Vulnerabilities catalog due to evidence of active exploitation. Meanwhile, North Korean threat actors continue their Contagious Interview campaign with 197 malicious npm packages spreading OtterCookie malware, and the Qilin ransomware group has executed a devastating supply chain attack against South Korea's financial sector through a managed service provider compromise affecting 28 organizations.

## Active Exploitation Details

### OpenPLC ScadaBR Cross-Site Scripting Vulnerability
- **Description**: A cross-site scripting (XSS) vulnerability affecting OpenPLC ScadaBR industrial control systems
- **Impact**: Allows attackers to execute malicious scripts in users' browsers, potentially leading to credential theft, session hijacking, and unauthorized access to industrial control systems
- **Status**: Actively exploited in the wild according to CISA, requiring immediate patching
- **CVE ID**: CVE-2021-26829

### ShadowV2 Botnet IoT Exploitation
- **Description**: A Mirai-based botnet malware targeting IoT devices with known vulnerability exploits
- **Impact**: Compromised devices are recruited into a botnet for distributed denial-of-service attacks and other malicious activities
- **Status**: Active exploitation campaign targeting D-Link, TP-Link, and other vendor devices

## Affected Systems and Products

- **OpenPLC ScadaBR**: Industrial control system software vulnerable to XSS attacks
- **IoT Devices**: D-Link and TP-Link devices targeted by ShadowV2 botnet malware
- **npm Registry**: 197 malicious packages spreading OtterCookie malware
- **Maven Ecosystem**: Over 830 compromised packages in the Shai-Hulud v2 supply chain attack
- **South Korean MSP**: Managed service provider compromised leading to 28 victim organizations
- **Microsoft Teams**: Guest access feature creating security blind spots in cross-tenant environments
- **PyPI Packages**: Legacy Python packages with domain takeover vulnerabilities

## Attack Vectors and Techniques

- **Cross-Site Scripting**: Exploitation of XSS vulnerabilities in industrial control systems
- **Supply Chain Compromise**: Malicious package injection into npm and Maven repositories
- **Evil Twin WiFi Networks**: Rogue access points capturing traveler credentials at airports
- **Guest Access Exploitation**: Bypassing Microsoft Defender protections through Teams guest access
- **Domain Takeover**: Exploiting legacy Python bootstrap scripts for package compromise
- **Ransomware Deployment**: Qilin ransomware distribution through MSP infrastructure
- **Botnet Recruitment**: IoT device compromise for distributed attack capabilities

## Threat Actor Activities

- **North Korean Hackers**: Continuing Contagious Interview campaign with 197 npm packages deploying updated OtterCookie malware targeting software developers
- **Bloody Wolf**: Expanding Java-based NetSupport RAT attacks in Kyrgyzstan and Uzbekistan since June 2025
- **Qilin Ransomware Group**: Executed sophisticated supply chain attack against South Korean financial sector through MSP compromise, affecting 28 organizations in "Korean Leaks" operation
- **Scattered LAPSUS$ Hunters**: Prolific cybercriminal group conducting mass data theft and extortion campaigns against major corporations
- **Shai-Hulud Operators**: Second wave campaign spreading from npm to Maven ecosystem, exposing thousands of secrets across compromised packages