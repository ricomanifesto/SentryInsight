# Exploitation Report

The current threat landscape reveals intense supply chain attack activity, with the TeamPCP threat actor orchestrating multiple sophisticated campaigns targeting popular development tools and packages. Critical exploitation includes active abuse of cPanel vulnerabilities to deploy backdoors, the first documented AI-assisted zero-day exploit development, and widespread compromises of trusted software repositories. Notable incidents include the Shai-Hulud campaign affecting major npm and PyPI packages from TanStack, Mistral AI, and other prominent vendors, alongside active exploitation of Canvas platform vulnerabilities by the ShinyHunters extortion group.

## Active Exploitation Details

### cPanel Critical Vulnerability
- **Description**: Critical vulnerability in cPanel control panel software allowing unauthorized access and backdoor deployment
- **Impact**: Complete system compromise with persistent backdoor access via the "Filemanager" tool
- **Status**: Under active exploitation by threat actor Mr_Rot13
- **CVE ID**: CVE-2026-41940

### AI-Developed Zero-Day 2FA Bypass
- **Description**: First known zero-day exploit developed using artificial intelligence targeting a popular open-source web administration tool's two-factor authentication mechanism
- **Impact**: Complete bypass of 2FA security controls enabling unauthorized administrative access
- **Status**: Actively exploited by unknown threat actors, marking a significant milestone in AI-assisted exploit development

### Canvas Platform Vulnerability
- **Description**: Security flaw in Instructure's Canvas learning management system allowing portal modification and defacement
- **Impact**: Login portal defacement with extortion messages and potential data exposure affecting educational institutions
- **Status**: Exploited by ShinyHunters group leading to 3.65TB data theft and ransom agreement

### Dirty Frag Linux Privilege Escalation
- **Description**: Linux kernel vulnerability enabling privilege escalation, similar to previous flaws like Dirty Pipe and Copy Fail
- **Impact**: Local privilege escalation to root access on affected Linux distributions
- **Status**: May already be under limited exploitation targeting enterprise Linux environments

## Affected Systems and Products

- **cPanel Control Panel**: Web hosting control panel software vulnerable to critical backdoor deployment
- **Canvas LMS**: Educational technology platform used by universities and schools worldwide
- **npm Packages**: TanStack, UiPath, Mistral AI, OpenSearch, and Guardrails AI packages compromised
- **PyPI Packages**: Python Package Index repositories from major technology vendors
- **Jenkins Marketplace**: Checkmarx AST plugin compromised with information stealing malware
- **Hugging Face Platform**: Machine learning model repository hosting malicious OpenAI impersonation
- **Enterprise Linux Distributions**: Various Linux distros vulnerable to Dirty Frag privilege escalation
- **SAP Commerce Cloud**: Enterprise e-commerce platform with critical vulnerabilities
- **SAP S/4HANA**: Business suite software affected by critical security flaws

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Mini Shai-Hulud worm compromising trusted development packages across multiple repositories
- **Package Repository Infiltration**: Malicious packages uploaded to npm, PyPI, Jenkins Marketplace, and Hugging Face
- **Web Application Exploitation**: Direct exploitation of cPanel and Canvas vulnerabilities for backdoor deployment
- **AI-Assisted Exploit Development**: Machine learning models used to generate zero-day exploits automatically
- **Search Engine Optimization Poisoning**: Malicious Google Ads campaigns promoting fake Claude.ai downloads
- **Social Engineering via Legitimate Platforms**: Abuse of Claude.ai shared chats to distribute malware
- **Blockchain-Based C2 Communications**: TrickMo banking malware using TON blockchain for covert communications
- **Privilege Escalation**: Linux kernel exploitation for local privilege escalation attacks

## Threat Actor Activities

- **TeamPCP**: Orchestrating widespread supply chain attacks targeting npm, PyPI, and Jenkins repositories with credential-stealing malware
- **Mr_Rot13**: Actively exploiting cPanel vulnerability to deploy Filemanager backdoors on compromised hosting environments
- **ShinyHunters**: Extortion group responsible for Canvas platform breach and 3.65TB data theft, successfully negotiating ransom agreement
- **Unknown AI-Assisted Actor**: First documented threat actor using artificial intelligence to develop zero-day exploits for web administration tools
- **TrickMo Operators**: Android banking malware campaign targeting European users with enhanced blockchain-based command and control
- **Fake OpenAI Impersonators**: Malicious actors creating convincing fake repositories to distribute Rust-based information stealers
- **Mac Malware Distributors**: Sophisticated malvertising campaigns abusing Google Ads and Claude.ai platforms to target macOS users