# Exploitation Report

Critical vulnerabilities are actively being exploited across multiple platforms and systems, with several high-severity issues demanding immediate attention. The most severe threats include a critical 9.9 CVSS vulnerability in n8n workflow automation platform allowing authenticated command execution, a 9.2 CVSS flaw in AdonisJS Bodyparser enabling arbitrary file writes, and the actively exploited MongoBleed vulnerability affecting MongoDB servers. Additionally, widespread campaigns are leveraging social engineering techniques, including ClickFix attacks using fake Blue Screen of Death screens to deliver DCRat malware, and the Kimwolf botnet has infected over 2 million Android devices through exposed ADB services. Supply chain attacks are targeting VS Code forks through malicious extension recommendations, while the RondoDox botnet is expanding its operations by exploiting React2Shell vulnerabilities.

## Active Exploitation Details

### MongoBleed Memory Leak Vulnerability
- **Description**: A memory leak security vulnerability in MongoDB servers that allows extraction of sensitive information
- **Impact**: Unauthenticated attackers can extract passwords and tokens from MongoDB servers
- **Status**: Under active attack, patches available

### n8n Workflow Automation Command Execution
- **Description**: Critical vulnerability in n8n open-source workflow automation platform
- **Impact**: Authenticated attackers can execute arbitrary system commands on the underlying server
- **Status**: Critical severity with 9.9 CVSS score, patches available

### AdonisJS Bodyparser Arbitrary File Write
- **Description**: Critical security vulnerability in "@adonisjs/bodyparser" npm package
- **Impact**: Successful exploitation could allow arbitrary file write capabilities on servers
- **Status**: Critical severity with 9.2 CVSS score, latest version available

### React2Shell Exploitation
- **Description**: Vulnerability being exploited by RondoDox botnet targeting Next.js servers
- **Impact**: Enables cryptomining, botnet payload deployment, and other malicious activities
- **Status**: Active exploitation targeting IoT networks and enterprises

### Exposed ADB Services
- **Description**: Android Debug Bridge services exposed to internet exploitation
- **Impact**: Complete device compromise and botnet recruitment
- **Status**: Actively exploited by Kimwolf botnet affecting over 2 million devices

## Affected Systems and Products

- **n8n Workflow Automation Platform**: Open-source automation platform vulnerable to command execution
- **AdonisJS Framework**: "@adonisjs/bodyparser" npm package with file write vulnerability
- **MongoDB Servers**: Database servers affected by MongoBleed memory leak issue
- **Android Devices**: Over 2 million devices infected via exposed ADB services
- **VS Code Forks**: Cursor, Windsurf, Google Antigravity, and Trae IDE platforms
- **Next.js Servers**: Web framework servers targeted by RondoDox botnet
- **ShareFile, Nextcloud, OwnCloud**: Cloud file-sharing platforms targeted for data theft
- **Viber Messaging Platform**: Used as attack vector against Ukrainian entities

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: Fake Windows Blue Screen of Death displays with malicious "fix" instructions
- **Supply Chain Attacks**: Malicious extension recommendations in VS Code forks through OpenVSX registry gaps
- **Memory Leak Exploitation**: Extraction of credentials and tokens from MongoDB server memory
- **Command Injection**: Authenticated exploitation of workflow automation platforms
- **ADB Tunneling**: Exploitation of exposed Android Debug Bridge services through proxy networks
- **Phishing Campaigns**: Fake hotel booking emails targeting hospitality sector
- **File Upload Attacks**: Arbitrary file write exploitation in web frameworks

## Threat Actor Activities

- **PHALT#BLYX Campaign**: Targeting hospitality sector in Europe with fake booking emails and ClickFix techniques
- **Zestix Threat Actor**: Offering stolen corporate data from breached file-sharing platforms
- **UAC-0184 (Russia-aligned)**: Targeting Ukrainian military and government via Viber messaging platform
- **Kimwolf Botnet Operators**: Operating massive Android botnet through residential proxy networks
- **RondoDox Botnet**: Expanding operations with React2Shell exploitation targeting IoT and enterprise networks
- **Crimson Collective**: Extortion gang claiming breach of US broadband provider Brightspeed
- **ShinyHunters**: Claiming breach of cybersecurity firm Resecurity systems
- **BlackCat/ALPHV Affiliates**: US citizens pleading guilty to ransomware operations in 2023