# Exploitation Report

The current threat landscape reveals active exploitation of critical vulnerabilities across multiple platforms and technologies. Most notably, threat actors are exploiting an authentication bypass vulnerability in FortiClient Enterprise Management Server to deploy credential stealing malware, while a zero-day vulnerability in the Gogs Git service allows authenticated users to execute arbitrary code. Additionally, sophisticated threat actors like GREYVIBE are leveraging AI technologies including ChatGPT and Gemini to enhance their cyberattacks against Ukrainian entities, while the North Korean group Kimsuky continues expanding their arsenal with new malware tools targeting South Korean organizations. The exploitation landscape also includes malicious package repositories targeting cloud secrets and banking credentials, highlighting the evolving nature of supply chain attacks.

## Active Exploitation Details

### FortiClient EMS Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in FortiClient Enterprise Management Server allowing unauthorized access
- **Impact**: Threat actors can deploy credential stealing malware, specifically an undocumented stealer called EKZ
- **Status**: Vulnerability is patched but continues to be actively exploited
- **CVE ID**: CVE-2026-35616

### Gogs Remote Code Execution Zero-Day
- **Description**: Unpatched zero-day vulnerability in the Gogs self-hosted Git service
- **Impact**: Allows any authenticated user to execute arbitrary code under certain conditions, leading to full system compromise
- **Status**: Currently unpatched and actively exploitable on Internet-facing instances

### Cloud Infrastructure Misconfigurations
- **Description**: Complex exploit chain combining over-permissioned roles, secrets discovery, and non-human identities
- **Impact**: Could compromise popular automation services and cloud environments
- **Status**: Ongoing research reveals widespread vulnerability in cloud integrations

## Affected Systems and Products

- **FortiClient Enterprise Management Server**: Systems vulnerable to authentication bypass leading to credential theft
- **Gogs Git Service**: Self-hosted Git installations exposed to remote code execution
- **Cloud Automation Services**: Popular automation platforms with misconfigured permissions and exposed secrets
- **Android Devices**: Targeted by BTMOB malware service generating custom phishing payloads
- **NuGet Package Repositories**: Compromised with malicious packages targeting Sicoob banking systems
- **npm Package Repositories**: Infected packages designed to steal cloud secrets and credentials
- **Visual Studio Code**: Exploited through tunneling capabilities by Kimsuky threat actors

## Attack Vectors and Techniques

- **Authentication Bypass**: Exploiting FortiClient EMS vulnerabilities to gain unauthorized access
- **Supply Chain Attacks**: Malicious packages in NuGet and npm repositories masquerading as legitimate SDKs
- **AI-Powered Social Engineering**: Use of ChatGPT and Gemini to generate convincing lures and attack content
- **Remote Access Trojans**: BTMOB service providing custom Android malware generation
- **Visual Studio Code Tunnels**: Legitimate development tools repurposed for malicious access
- **Session Cookie Theft**: Ongoing attacks targeting session credentials despite new Chrome protections
- **Phishing Infrastructure**: Fake FIFA websites and fraudulent ticket sales targeting World Cup fans

## Threat Actor Activities

- **GREYVIBE**: Russian-linked threat cluster targeting Ukrainian entities with AI-generated lures and custom malware tools since August 2025
- **Kimsuky (Velvet Chollima)**: North Korean state-sponsored group deploying HTTPSpy malware and expanding arsenal with HelloDoor and VS Code tunnels against South Korean military and corporate entities
- **ShinyHunters**: Extortion gang responsible for major data breaches affecting Charter Communications (4.9 million accounts) and Carnival Corporation (6 million people)
- **The Com**: Neo-Nazi-infested criminal gang using cyber winnings to support violence and sexploitation activities
- **Romanian Cybercriminals**: Operators targeting U.S. government networks, including Oregon state systems
- **Brazilian Banking Threats**: Groups deploying malicious Sicoob NuGet packages to steal banking credentials