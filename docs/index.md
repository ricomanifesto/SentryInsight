# Exploitation Report

The current threat landscape is dominated by rapid exploitation of critical vulnerabilities across multiple platforms and attack vectors. Most notably, threat actors are achieving remarkably fast exploitation cycles, with the LiteLLM SQL injection vulnerability being exploited within 36 hours of disclosure. Zero-day attacks continue to pose significant risks, with CISA ordering federal agencies to patch Windows vulnerabilities actively exploited in the wild. The emergence of AI-enhanced attack methodologies is reshaping the threat landscape, with North Korean groups leveraging AI-generated content and automated tools to scale their operations. Critical infrastructure targeting remains a priority for sophisticated actors, as evidenced by the Lotus Wiper attacks against Venezuelan energy firms and the proliferation of supply chain attacks through malicious npm packages and VS Code extensions.

## Active Exploitation Details

### LiteLLM SQL Injection Vulnerability
- **Description**: A critical pre-authentication SQL injection flaw in BerriAI's LiteLLM Python package that allows attackers to access sensitive information stored in the LLM gateway
- **Impact**: Unauthorized access to sensitive data and potential complete compromise of LiteLLM deployments
- **Status**: Actively exploited within 36 hours of public disclosure, patch available
- **CVE ID**: CVE-2026-42208

### Windows Zero-Day Vulnerability
- **Description**: A Windows security flaw actively exploited in zero-day attacks targeting federal systems
- **Impact**: Unauthorized system access and potential lateral movement within government networks
- **Status**: Actively exploited in the wild, CISA has mandated federal agencies to apply patches immediately

### GitHub Remote Code Execution Flaw
- **Description**: A critical remote code execution vulnerability in GitHub.com and GitHub Enterprise Server exploitable through a single Git push operation
- **Impact**: Remote code execution and unauthorized access to millions of private repositories
- **Status**: Patched in early March 2026
- **CVE ID**: CVE-2026-3854

### ConnectWise ScreenConnect Vulnerability
- **Description**: Security flaw in ConnectWise ScreenConnect remote access software
- **Impact**: Unauthorized access to remote systems and potential lateral movement
- **Status**: Actively exploited and added to CISA's Known Exploited Vulnerabilities catalog

### Hugging Face LeRobot Vulnerability
- **Description**: Critical unauthenticated remote code execution flaw in Hugging Face's open-source robotics platform
- **Impact**: Complete system compromise without authentication requirements
- **Status**: Currently unpatched and publicly disclosed
- **CVE ID**: CVE-2026-25874

### cPanel Authentication Bypass
- **Description**: Critical authentication vulnerability affecting various authentication paths in cPanel control panel software
- **Impact**: Unauthorized access to web hosting control panels and server infrastructure
- **Status**: Security updates released, immediate patching required

## Affected Systems and Products

- **LiteLLM Python Package**: Open-source large language model gateway systems
- **Microsoft Windows**: Federal government systems and enterprise environments
- **GitHub Platform**: GitHub.com and GitHub Enterprise Server installations
- **ConnectWise ScreenConnect**: Remote access and support infrastructure
- **Hugging Face LeRobot**: Robotics platform with approximately 24,000 GitHub stars
- **cPanel Software**: Web hosting control panel systems
- **npm Package Registry**: JavaScript development environments
- **Visual Studio Code**: Development environments using Open VSX extensions
- **Venezuelan Energy Infrastructure**: Power generation and utility systems
- **Minecraft Gaming Platform**: Gaming clients and related services

## Attack Vectors and Techniques

- **AI-Enhanced Supply Chain Attacks**: Malicious npm packages inserted through AI assistance and fake company operations
- **Living-off-the-Land Techniques**: Sophisticated use of legitimate tools for malicious purposes in wiper attacks
- **OAuth Integration Exploitation**: Compromised third-party OAuth applications leading to widespread access
- **Social Engineering with AI**: Fake Zoom calls using stolen victim videos and AI-generated avatars
- **Git Repository Manipulation**: Single Git push operations triggering remote code execution
- **Pre-Authentication SQL Injection**: Direct database access without authentication requirements
- **Malicious VS Code Extensions**: Self-propagating malware through development tool extensions
- **Ransomware with Wiper Functionality**: Flawed encryption implementation causing permanent data destruction

## Threat Actor Activities

- **North Korean DPRK Groups**: Conducting AI-enhanced supply chain attacks using malicious npm packages, fake firms, and remote access trojans
- **BlueNoroff**: Using stolen victim videos, AI-generated avatars, and fake Zoom calls to target cryptocurrency executives
- **LofyGang**: Brazilian cybercrime group resurfaced after three years with Minecraft-focused LofyStealer campaigns
- **Scattered Spider**: Prolific cybercrime group with arrested member facing federal charges in the US
- **LAPSUS$ Group**: Confirmed to have leaked stolen data from Checkmarx's private GitHub repository
- **Venezuelan Energy Attackers**: Sophisticated threat actors deploying Lotus Wiper malware against critical infrastructure
- **GlassWorm Campaign**: Operators scaling supply chain attacks through malicious VS Code extensions
- **VECT 2.0 Operators**: Ransomware group with flawed encryption causing irreversible data destruction
- **Competing Ransomware Groups**: 0APT and KryBit groups feuding and exposing each other's operational data