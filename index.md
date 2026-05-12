# Exploitation Report

The current threat landscape shows intense exploitation activity across multiple attack vectors, with attackers leveraging critical vulnerabilities, supply chain compromises, and AI-assisted exploitation techniques. The most concerning developments include active exploitation of cPanel's CVE-2026-41940 vulnerability being used to deploy backdoors, Google's discovery of the first AI-developed zero-day exploit targeting 2FA bypass mechanisms, and extensive supply chain attacks by TeamPCP affecting major software repositories. Additionally, critical vulnerabilities in enterprise systems like Fortinet products, SAP Commerce Cloud, and Exim mail servers are creating significant risk exposure for organizations worldwide.

## Active Exploitation Details

### cPanel Critical Vulnerability
- **Description**: A critical flaw in cPanel allowing unauthorized access and backdoor deployment
- **Impact**: Attackers can deploy the "Filemanager" backdoor on compromised cPanel environments
- **Status**: Actively exploited by threat actor Mr_Rot13
- **CVE ID**: CVE-2026-41940

### AI-Developed Zero-Day 2FA Bypass
- **Description**: First known zero-day exploit developed using artificial intelligence to bypass two-factor authentication
- **Impact**: Mass exploitation capability against 2FA-protected systems
- **Status**: Actively exploited by unknown threat actors
- **CVE ID**: Not specified in articles

### Canvas Learning Management System Vulnerability
- **Description**: Security vulnerability in Instructure's Canvas LMS allowing portal defacement
- **Impact**: Hackers can modify Canvas login portals and leave extortion messages
- **Status**: Confirmed exploitation with portal defacement attacks
- **CVE ID**: Not specified in articles

### Dirty Frag Linux Privilege Escalation
- **Description**: Privilege escalation vulnerability affecting enterprise Linux distributions, similar to Copy Fail and Dirty Pipe
- **Impact**: Local privilege escalation on Linux systems
- **Status**: May already be under limited exploitation
- **CVE ID**: Not specified in articles

### Fortinet Critical RCE Vulnerabilities
- **Description**: Critical remote code execution flaws in FortiSandbox and FortiAuthenticator
- **Impact**: Attackers can run arbitrary commands or code on affected systems
- **Status**: Patches released by Fortinet
- **CVE ID**: Not specified in articles

### Exim BDAT Vulnerability
- **Description**: Severe security issue in Exim mail server affecting GnuTLS builds
- **Impact**: Memory corruption and potential code execution
- **Status**: Security updates released
- **CVE ID**: Not specified in articles

## Affected Systems and Products

- **cPanel**: Web hosting control panels vulnerable to backdoor deployment
- **Fortinet Products**: FortiSandbox and FortiAuthenticator systems affected by critical RCE flaws
- **Canvas LMS**: Instructure's learning management system with portal defacement vulnerability
- **Exim Mail Server**: GnuTLS builds vulnerable to memory corruption attacks
- **SAP Commerce Cloud**: Critical vulnerabilities in enterprise e-commerce platform
- **SAP S/4HANA**: Critical flaws in enterprise resource planning software
- **Enterprise Linux**: Multiple distributions affected by Dirty Frag privilege escalation
- **Windows 11**: Versions 25H2/24H2 and 23H2 receiving security updates
- **npm Packages**: TanStack, Mistral AI, UiPath, OpenSearch, Guardrails AI packages compromised
- **PyPI Packages**: Multiple Python packages infected with malicious code
- **RubyGems**: Package manager affected by massive malicious package upload campaign
- **Jenkins Marketplace**: Checkmarx AST plugin compromised with infostealer
- **Hugging Face Models**: AI models vulnerable to tokenizer manipulation attacks

## Attack Vectors and Techniques

- **Supply Chain Compromise**: TeamPCP conducting extensive campaigns against npm, PyPI, and Jenkins repositories
- **AI-Assisted Exploitation**: First known use of AI to develop zero-day exploits for 2FA bypass
- **Backdoor Deployment**: Filemanager backdoor installation via cPanel vulnerability exploitation
- **Package Poisoning**: Shai-Hulud worm spreading through compromised software packages
- **Portal Defacement**: Canvas login portal modification for extortion purposes
- **Memory Corruption**: Exim BDAT attacks targeting GnuTLS implementations
- **Privilege Escalation**: Dirty Frag exploit targeting Linux kernel vulnerabilities
- **Tokenizer Manipulation**: Hugging Face model hijacking through single file modifications
- **Banking Trojan Evolution**: TrickMo using TON C2 and SOCKS5 for Android network pivots

## Threat Actor Activities

- **Mr_Rot13**: Actively exploiting cPanel CVE-2026-41940 to deploy Filemanager backdoors across compromised environments
- **TeamPCP**: Conducting massive supply chain attacks targeting npm, PyPI, and Jenkins repositories with credential-stealing malware and self-propagating worms
- **Unknown AI-Assisted Actor**: Leveraging artificial intelligence to develop zero-day exploits for 2FA bypass, representing a significant evolution in attack sophistication
- **ShinyHunters**: Extortion group that breached Instructure and reached agreement to stop 3.65TB Canvas data leak
- **TrickMo Operators**: Banking trojan campaign using advanced C2 infrastructure and network pivoting capabilities on Android devices
- **Škoda Auto Attackers**: Successfully compromised online shop infrastructure leading to customer data breach