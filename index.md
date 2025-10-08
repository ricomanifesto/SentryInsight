# Exploitation Report

The current threat landscape reveals several critical zero-day vulnerabilities and active exploitation campaigns targeting enterprise infrastructure. The most concerning developments include the Clop ransomware gang's exploitation of a critical Oracle E-Business Suite zero-day vulnerability since early August, the Storm-1175 threat actor's active exploitation of a maximum severity GoAnywhere MFT flaw to deploy Medusa ransomware, and the discovery of a 13-year-old Redis vulnerability with a perfect 10.0 CVSS score enabling remote code execution. Additionally, cybercriminals are exploiting Zimbra zero-day vulnerabilities through sophisticated calendar invitation attacks, while various threat actors continue leveraging social engineering and credential-based attacks across multiple platforms.

## Active Exploitation Details

### Oracle E-Business Suite Zero-Day
- **Description**: Critical zero-day vulnerability in Oracle E-Business Suite being actively exploited by the Clop ransomware gang
- **Impact**: Enables data theft attacks against Oracle EBS customers, with wide-ranging targeting across multiple organizations
- **Status**: Zero-day vulnerability exploited since early August 2024, recently disclosed but exploitation ongoing
- **CVE ID**: CVE-2025-61882

### Fortra GoAnywhere MFT Critical Flaw
- **Description**: Maximum severity vulnerability in GoAnywhere managed file transfer software enabling remote code execution
- **Impact**: Facilitates deployment of Medusa ransomware and complete system compromise
- **Status**: Actively exploited by Storm-1175 threat actor for nearly a month in ransomware campaigns
- **CVE ID**: CVE-2025-10035

### Redis Remote Code Execution Flaw
- **Description**: 13-year-old vulnerability in Redis in-memory database software with maximum CVSS 10.0 severity score
- **Impact**: Allows complete remote code execution and full host takeover under certain circumstances
- **Status**: Over 300,000 Redis instances currently exposed to exploitation

### Zimbra Zero-Day Calendar Exploit
- **Description**: Zero-day vulnerability in Zimbra email platform exploited through malicious calendar invitations (ICS files)
- **Impact**: Enables targeted attacks against military and government organizations
- **Status**: Actively exploited by threat actors impersonating official entities like the Libyan Navy

### Figma MCP Server Vulnerability
- **Description**: Severe vulnerability in the figma-developer-mcp Model Context Protocol server
- **Impact**: Allows attackers to achieve remote code execution on affected systems
- **Status**: Now patched but required immediate attention due to code execution capabilities

## Affected Systems and Products

- **Oracle E-Business Suite**: Enterprise resource planning software targeted in widespread data theft campaigns
- **Fortra GoAnywhere MFT**: Managed file transfer solution compromised for ransomware deployment
- **Redis Database**: In-memory data structure store with 300,000+ exposed instances vulnerable to takeover
- **Zimbra Email Platform**: Collaboration software targeted through calendar-based attack vectors
- **Figma MCP Server**: Developer tool server vulnerable to remote code execution
- **Salesforce Platform**: Customer relationship management system targeted in widespread data theft attacks
- **DraftKings Platform**: Sports betting platform compromised through credential stuffing attacks
- **Asahi Brewery Systems**: Manufacturing systems disrupted by ransomware affecting beer production and distribution

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in Oracle EBS, GoAnywhere, and Zimbra systems
- **Calendar Invitation Attacks**: Malicious ICS files used to exploit Zimbra zero-day vulnerabilities
- **Credential Stuffing**: Automated attacks using compromised credentials against DraftKings and other platforms
- **Social Engineering**: BatShadow group targeting job seekers and digital marketing professionals with Go-based malware
- **AI-Assisted Malware Development**: North Korean, Russian, and Chinese threat actors misusing ChatGPT for cyberattack facilitation
- **ASCII Smuggling**: New attack technique against Google Gemini AI to manipulate model behavior and provide false information
- **Spam Content Hiding**: "Salt" technique used to hide malicious content in spam emails to evade security filters

## Threat Actor Activities

- **Clop Ransomware Gang**: Actively exploiting Oracle EBS zero-day since August for data theft across multiple customer organizations
- **Storm-1175**: Cybercrime group exploiting GoAnywhere vulnerability to deploy Medusa ransomware in targeted attacks
- **Graceful Spider**: Threat actor attributed to Oracle EBS exploitation campaigns with moderate confidence
- **BatShadow Group**: Vietnamese threat actor using "Vampire Bot" Go-based malware to target job seekers through social engineering
- **North Korean Hackers**: Stole over $2 billion in cryptocurrency assets in 2024, marking the largest annual total on record
- **ShinyHunters Gang**: Now extorting Red Hat following data breach, leaking customer engagement reports on dark web
- **Multiple Nation-State Actors**: Russian, North Korean, and Chinese groups disrupted for misusing ChatGPT in cyberattack development