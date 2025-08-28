# Exploitation Report

Current threat landscape shows significant escalation in sophisticated attack campaigns targeting both enterprise and government infrastructure. Notable activities include Storm-0501's evolution from traditional ransomware to cloud-focused data exfiltration operations, active exploitation of FreePBX zero-day vulnerabilities affecting internet-exposed systems, and the emergence of AI-powered attack tools including the experimental PromptLock ransomware. State-sponsored actors continue targeting diplomatic entities through captive portal hijacking, while widespread supply chain attacks have disrupted critical municipal services across Sweden.

## Active Exploitation Details

### FreePBX Zero-Day Vulnerability
- **Description**: Critical zero-day vulnerability in FreePBX systems with Administrator Control Panel (ACP) exposed to the internet
- **Impact**: Allows attackers to gain unauthorized access to FreePBX servers and potentially compromise entire telecommunications infrastructure
- **Status**: Actively exploited in the wild, emergency fix has been released by Sangoma FreePBX Security Team

### Storm-0501 Cloud Infrastructure Attacks
- **Description**: Advanced persistent threat actor has evolved tactics to focus on cloud-based data exfiltration and deletion rather than traditional ransomware encryption
- **Impact**: Enables large-scale data theft, extortion, and destruction of Azure cloud resources through compromised Entra ID credentials
- **Status**: Ongoing campaign with confirmed attacks against hybrid cloud environments

### Captive Portal Hijacking by Mustang Panda
- **Description**: Chinese APT group hijacking Google Chrome browsers during network connection attempts to redirect users to malicious phishing sites
- **Impact**: Enables credential harvesting and surveillance of diplomatic personnel across Asian regions
- **Status**: Active campaign targeting diplomatic entities with sophisticated browser redirection techniques

### Salesforce OAuth Token Compromise
- **Description**: Widespread attacks exploiting compromised OAuth tokens from third-party application Salesloft Drift to access Salesforce environments
- **Impact**: Enables unauthorized access to sensitive customer data and business intelligence stored in Salesforce platforms
- **Status**: Active data theft campaign attributed to threat group UNC6395

## Affected Systems and Products

- **FreePBX Systems**: Telecommunications servers with Administrator Control Panel exposed to internet
- **Microsoft Azure**: Cloud environments with Entra ID integration in hybrid configurations
- **Salesforce Platforms**: Organizations using Salesloft Drift third-party application integration
- **Google Chrome Browsers**: Users connecting to compromised captive portal networks in Asian regions
- **Miljödata IT Systems**: Municipal government systems across Sweden (200+ municipalities affected)
- **Nevada State Government**: Multiple state agency systems and services
- **Windows, macOS, Linux**: Systems targeted by PromptLock AI-powered ransomware

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched FreePBX vulnerabilities through internet-exposed management interfaces
- **OAuth Token Abuse**: Leveraging compromised third-party application tokens to bypass authentication mechanisms
- **Cloud Infrastructure Pivoting**: Moving from on-premises compromised systems to cloud environments for data exfiltration
- **Captive Portal Manipulation**: Hijacking legitimate network connection processes to redirect traffic to malicious infrastructure
- **AI-Powered Automation**: Using artificial intelligence services like Anthropic's Claude to automate reconnaissance, intrusion, and credential harvesting
- **Supply Chain Targeting**: Attacking IT service providers to impact multiple downstream organizations simultaneously

## Threat Actor Activities

- **Storm-0501**: Financially motivated group shifting from ransomware operations to cloud-focused data exfiltration and extortion campaigns targeting hybrid environments
- **Mustang Panda (Chinese APT)**: State-sponsored group conducting surveillance operations against Asian diplomatic personnel through sophisticated browser hijacking techniques
- **UNC6395**: Cybercriminal group specializing in OAuth token compromise and Salesforce environment exploitation for large-scale data theft
- **PromptLock Operators**: Experimental threat actors developing and deploying AI-powered ransomware with cross-platform capabilities
- **ZipLine Campaign**: Sophisticated phishing operation using reverse social engineering tactics where victims initiate contact with attackers
- **Miljödata Attackers**: Unknown threat actors targeting Swedish municipal IT infrastructure through supply chain compromise