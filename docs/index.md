# Exploitation Report

Critical vulnerability exploitation activity is currently dominated by several high-impact remote code execution flaws and supply chain attacks. The most severe incidents include active exploitation of authentication bypass vulnerabilities in the Qinglong task scheduler for cryptomining operations, critical SQL injection attacks against LiteLLM platforms occurring within 36 hours of disclosure (CVE-2026-42208), and a zero-day Windows vulnerability that has prompted emergency federal patching orders. Additionally, a critical GitHub remote code execution flaw (CVE-2026-3854) has been patched that could have provided access to millions of private repositories. Supply chain attacks are proliferating through compromised npm packages targeting SAP-related systems and malicious VS Code extensions in the GlassWorm campaign, while sophisticated threat actors including North Korean groups are deploying AI-enhanced attack techniques.

## Active Exploitation Details

### Qinglong Task Scheduler Authentication Bypass
- **Description**: Two authentication bypass vulnerabilities in the open-source Qinglong task scheduling tool that allow unauthorized access
- **Impact**: Attackers can deploy cryptominers on developers' servers and gain unauthorized system access
- **Status**: Currently being actively exploited in the wild

### LiteLLM SQL Injection Vulnerability
- **Description**: Critical pre-authentication SQL injection flaw in the BerriAI LiteLLM Python package
- **Impact**: Attackers can access sensitive information stored in LLM gateway systems and potentially compromise AI infrastructure
- **Status**: Actively exploited within 36 hours of public disclosure
- **CVE ID**: CVE-2026-42208

### Windows Zero-Day Vulnerability
- **Description**: Unspecified Windows vulnerability that was exploited as a zero-day before patches were available
- **Impact**: Unknown specific impact, but significant enough to warrant emergency federal patching orders
- **Status**: CISA has ordered federal agencies to patch immediately due to active zero-day exploitation

### GitHub Remote Code Execution Flaw
- **Description**: Critical remote code execution vulnerability affecting GitHub.com and GitHub Enterprise Server
- **Impact**: Authenticated users could obtain remote code execution and potentially access millions of private repositories
- **Status**: Patched in early March 2026
- **CVE ID**: CVE-2026-3854

### cPanel Authentication Bypass
- **Description**: Critical vulnerability affecting authentication paths in cPanel and WebHost Manager (WHM) dashboard
- **Impact**: Attackers can obtain access to control panel software without authentication
- **Status**: Emergency updates released to address the vulnerability

### ConnectWise ScreenConnect Vulnerability
- **Description**: Security flaw in ConnectWise ScreenConnect remote access software
- **Impact**: Active exploitation allowing unauthorized remote access to systems
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog

## Affected Systems and Products

- **Qinglong Task Scheduler**: Open-source task scheduling tool used by developers
- **LiteLLM Python Package**: Large language model gateway platform used in AI applications
- **Microsoft Windows**: Multiple Windows systems vulnerable to zero-day exploitation
- **GitHub Enterprise**: Both GitHub.com and on-premises GitHub Enterprise Server installations
- **cPanel/WHM**: Web hosting control panel software used across hosting providers
- **ConnectWise ScreenConnect**: Remote access and support software
- **OpenEMR Platform**: Electronic health record system used by over 100,000 healthcare providers
- **SAP-related npm packages**: Development packages in the Node.js ecosystem
- **VS Code Extensions**: Visual Studio Code marketplace extensions via Open VSX

## Attack Vectors and Techniques

- **Authentication Bypass**: Exploitation of authentication mechanisms in web applications like Qinglong and cPanel
- **SQL Injection**: Pre-authentication database attacks targeting LiteLLM systems
- **Supply Chain Compromise**: Malicious code injection into legitimate software packages and extensions
- **Git Repository Exploitation**: Single Git push operations to trigger remote code execution on GitHub
- **AI-Enhanced Social Engineering**: North Korean groups using AI-generated content and fake video calls
- **Cryptomining Deployment**: Installation of cryptocurrency miners on compromised developer systems
- **Living-off-the-Land Techniques**: Use of legitimate system tools for malicious purposes in wiper attacks

## Threat Actor Activities

- **North Korean Groups (DPRK)**: Deploying AI-inserted npm malware, creating fake companies, and using remote access trojans in sophisticated supply chain attacks
- **BlueNoroff**: Using stolen victim videos, AI-generated avatars, and fake Zoom calls to target cryptocurrency executives
- **LofyGang**: Brazilian cybercrime group resurging after three years with LofyStealer malware targeting Minecraft players
- **Scattered Spider**: Prolific hacking group with members facing federal charges for widespread cybercrime activities
- **Ukrainian Gaming Account Hackers**: Criminal group that compromised over 610,000 Roblox accounts for profit
- **GlassWorm Campaign Operators**: Attackers scaling malicious VS Code extension distribution through supply chain compromise
- **Vect 2.0 Ransomware Operators**: Groups deploying broken ransomware that acts as a wiper due to design flaws
- **Lotus Wiper Attackers**: Sophisticated actors targeting Venezuelan energy firms and utilities with destructive malware