# Exploitation Report

Critical exploitation activity is currently targeting multiple vectors across enterprise and consumer systems. The ShadowV2 botnet is actively exploiting IoT devices from major vendors including D-Link and TP-Link using known vulnerabilities, while ASUS routers face a critical authentication bypass flaw affecting AiCloud-enabled devices. Supply chain attacks continue to escalate with the Shai-Hulud v2 campaign compromising over 830 npm packages and expanding to Maven ecosystems, exposing thousands of credentials. Meanwhile, threat actors are leveraging sophisticated social engineering through fake browser updates and malicious Chrome extensions to deliver multiple information stealers, and commercial spyware campaigns are actively targeting high-value users on encrypted messaging platforms.

## Active Exploitation Details

### ShadowV2 Botnet IoT Exploitation
- **Description**: New Mirai-based botnet malware targeting IoT devices from multiple vendors with exploits for known vulnerabilities
- **Impact**: Compromise of IoT devices for botnet recruitment and potential DDoS operations
- **Status**: Active exploitation ongoing, using AWS outage as testing opportunity

### ASUS AiCloud Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in ASUS routers with AiCloud functionality enabled
- **Impact**: Unauthorized access to router administration and potential network compromise
- **Status**: Firmware patches released by ASUS for nine security vulnerabilities including the critical bypass flaw

### Node-Forge Signature Verification Bypass
- **Description**: Vulnerability in the popular JavaScript cryptography library allowing crafted data to bypass signature verification
- **Impact**: Cryptographic security bypass enabling data tampering and authentication circumvention
- **Status**: Fix available for the node-forge package

### Fluent Bit Cloud Infrastructure Vulnerabilities
- **Description**: Five vulnerabilities discovered in the open-source telemetry agent that can be chained together
- **Impact**: Remote code execution and complete compromise of cloud infrastructures through stealthy intrusions
- **Status**: Vulnerabilities disclosed, patches likely available

## Affected Systems and Products

- **D-Link IoT Devices**: Multiple models targeted by ShadowV2 botnet malware
- **TP-Link IoT Devices**: Various IoT products being exploited by botnet operators
- **ASUS Routers**: AiCloud-enabled router models affected by authentication bypass vulnerability
- **Node-Forge Library**: Popular JavaScript cryptography package used across web applications
- **npm Registry**: Over 830 packages compromised in Shai-Hulud v2 supply chain attack
- **Maven Ecosystem**: Second wave of supply chain attacks expanding beyond npm
- **Chrome Extensions**: Malicious extensions targeting Solana cryptocurrency transactions
- **Fluent Bit**: Open-source telemetry agent deployed in cloud environments
- **OnSolve CodeRED**: Emergency notification platform used by government agencies

## Attack Vectors and Techniques

- **IoT Vulnerability Exploitation**: ShadowV2 botnet leveraging known vulnerabilities in consumer devices
- **Supply Chain Poisoning**: Malicious packages uploaded to software repositories with credential theft capabilities
- **Social Engineering**: Fake Windows update pop-ups on adult websites delivering multiple stealers
- **Browser Extension Abuse**: Hidden Solana transfer fee injection through malicious Chrome extensions
- **SocGholish JavaScript Loader**: RomCom threat actors using fake update mechanisms to deliver Mythic Agent
- **ClickFix Lures**: JackFix campaign combining fake updates with malicious command execution
- **Blender Asset Hijacking**: Legitimate 3D modeling files weaponized to deploy StealC V2 malware
- **Commercial Spyware**: Active campaigns targeting Signal and WhatsApp users with RATs

## Threat Actor Activities

- **ShadowV2 Operators**: Deploying new Mirai-based botnet targeting IoT infrastructure during AWS outage testing
- **Shai-Hulud v2 Attackers**: Expanding supply chain attacks from npm to Maven, compromising 25,000+ repositories
- **RomCom Group**: First-time use of SocGholish loader to deliver Mythic Agent malware to U.S. civil engineering company
- **ToddyCat APT**: Developing custom tools like TCSectorCopy for Outlook email theft and Microsoft 365 token access
- **Qilin Ransomware**: Sophisticated supply chain attack against South Korean MSP leading to 28-victim data heist
- **Scattered LAPSUS$ Hunters**: Ongoing mass extortion campaigns targeting major corporations with data theft
- **JackFix Campaign**: Adult website compromise for fake Windows update delivery of multiple information stealers
- **Commercial Spyware Operators**: CISA-warned active campaigns targeting high-value messaging app users