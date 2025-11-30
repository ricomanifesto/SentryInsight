# Exploitation Report

Current cybersecurity activities reveal a complex landscape of active exploitations, supply chain compromises, and sophisticated attack campaigns. The most critical activity includes CISA's addition of CVE-2021-26829, an actively exploited cross-site scripting vulnerability in OpenPLC ScadaBR, to their Known Exploited Vulnerabilities catalog. North Korean threat actors continue their aggressive supply chain attacks through malicious npm packages targeting the Python ecosystem, while new botnet malware like ShadowV2 exploits known vulnerabilities in IoT devices from major vendors. Multiple high-profile data breaches have impacted millions of users, including incidents at Asahi Group Holdings, OpenAI, and the French Football Federation, demonstrating the ongoing success of threat actors in compromising enterprise systems.

## Active Exploitation Details

### OpenPLC ScadaBR Cross-Site Scripting Vulnerability
- **Description**: A cross-site scripting (XSS) vulnerability in OpenPLC ScadaBR that allows attackers to execute malicious scripts in users' browsers
- **Impact**: Attackers can steal sensitive information, hijack user sessions, and perform unauthorized actions within the SCADA system
- **Status**: Actively exploited in the wild, added to CISA's KEV catalog
- **CVE ID**: CVE-2021-26829

### IoT Device Vulnerabilities Exploited by ShadowV2 Botnet
- **Description**: Known vulnerabilities in D-Link, TP-Link, and other IoT vendor devices being exploited by new Mirai-based botnet malware
- **Impact**: Remote code execution, device compromise, and botnet recruitment for distributed attacks
- **Status**: Active exploitation targeting multiple IoT vendors

## Affected Systems and Products

- **OpenPLC ScadaBR**: Industrial control systems and SCADA environments using this platform
- **D-Link IoT Devices**: Various router and networking devices with known security flaws
- **TP-Link IoT Devices**: Network infrastructure devices vulnerable to botnet recruitment
- **npm Registry**: Over 830 packages compromised in Shai-Hulud v2 supply chain attack
- **Maven Ecosystem**: Supply chain attack expansion from npm to Maven package repositories
- **PyPI Packages**: Multiple Python packages vulnerable to domain takeover attacks
- **Microsoft Teams**: Guest access feature creating cross-tenant security blind spots
- **Asahi Group Holdings Systems**: Corporate infrastructure affecting 1.9 million individuals
- **French Football Federation**: Administrative management software used by football clubs
- **OpenAI API Infrastructure**: Customer data exposure through third-party analytics provider

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Malicious packages injected into npm, Maven, and PyPI repositories
- **Cross-Site Scripting (XSS)**: Web application exploitation in SCADA systems
- **Evil Twin WiFi Networks**: Wireless network impersonation at airports and public venues
- **Domain Takeover**: Legacy Python bootstrap scripts creating takeover opportunities
- **Botnet Recruitment**: IoT device compromise through known vulnerability exploitation
- **Guest Access Exploitation**: Microsoft Teams cross-tenant security bypass techniques
- **Phishing and Social Engineering**: NetSupport RAT delivery campaigns in Central Asia
- **Third-Party Vendor Compromise**: Data breaches through analytics and service providers

## Threat Actor Activities

- **North Korean Hackers**: Deployed 197 malicious npm packages spreading updated OtterCookie malware through Contagious Interview campaign
- **Bloody Wolf**: Expanded Java-based NetSupport RAT attacks targeting Kyrgyzstan and Uzbekistan since June 2025
- **Qilin Ransomware Group**: Conducted sophisticated supply chain attack against South Korean MSP, resulting in 28-victim "Korean Leaks" data heist
- **Scattered LAPSUS$ Hunters**: Continued mass extortion campaigns targeting major corporations with data theft and public exposure tactics
- **ShadowV2 Botnet Operators**: Exploited AWS outage as testing opportunity while targeting IoT devices with Mirai-based malware
- **Airport WiFi Attackers**: 44-year-old individual sentenced for operating evil twin networks across Australian airports over extended period