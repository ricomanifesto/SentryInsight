# Exploitation Report

Critical vulnerability exploitation activity is currently targeting enterprise infrastructure across multiple attack vectors. Threat actors are actively exploiting authentication bypass flaws in FortiClient Enterprise Management Server deployments to deploy credential-stealing malware, while a zero-day remote code execution vulnerability in Gogs self-hosted Git service poses immediate risks to internet-facing instances. Advanced persistent threat groups including GREYVIBE and Kimsuky are leveraging AI-powered tools and sophisticated malware arsenals to conduct targeted campaigns, while cybercriminals are exploiting cloud integration weaknesses and deploying malicious package repositories to steal sensitive data and banking credentials.

## Active Exploitation Details

### FortiClient EMS Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in FortiClient Enterprise Management Server that allows unauthorized access to enterprise management systems
- **Impact**: Attackers can deploy credential-stealing malware and gain unauthorized access to managed endpoints
- **Status**: Currently being exploited in the wild, patch available
- **CVE ID**: CVE-2026-35616

### Gogs Remote Code Execution Zero-Day
- **Description**: Unpatched zero-day vulnerability in Gogs self-hosted Git service that enables remote code execution for authenticated users
- **Impact**: Complete system compromise allowing arbitrary code execution on vulnerable instances
- **Status**: Zero-day vulnerability currently unpatched, active exploitation possible

### Cloud Integration Exploit Chains
- **Description**: Complex attack chains exploiting over-permissioned roles, secrets discovery, and non-human identities in cloud automation services
- **Impact**: Complete compromise of popular automation services and associated cloud infrastructure
- **Status**: Proof-of-concept demonstrated, affects cloud integrations with insufficient permission controls

## Affected Systems and Products

- **FortiClient Enterprise Management Server**: Authentication bypass vulnerability affecting enterprise deployments
- **Gogs Self-Hosted Git Service**: Zero-day RCE vulnerability in internet-facing instances
- **Cloud Automation Services**: Over-permissioned integrations vulnerable to exploit chains
- **Android Devices**: BTMOB malware targeting mobile platforms with custom phishing payloads
- **NuGet Package Repository**: Malicious packages masquerading as legitimate Brazilian banking SDKs
- **npm Package Repository**: Malicious packages targeting cloud secrets and credentials
- **Charter Communications**: 4.9 million customer accounts compromised by ShinyHunters gang
- **Carnival Corporation**: Nearly 6 million customer records breached

## Attack Vectors and Techniques

- **Authentication Bypass**: Exploiting CVE-2026-35616 in FortiClient EMS to bypass security controls
- **Remote Code Execution**: Zero-day exploitation in Gogs for complete system compromise
- **Supply Chain Attacks**: Malicious NuGet and npm packages targeting developers and cloud infrastructure
- **AI-Generated Social Engineering**: Use of ChatGPT and Gemini to create sophisticated phishing lures
- **Mobile Malware-as-a-Service**: BTMOB builder interface for generating custom Android RAT payloads
- **Cloud Permission Exploitation**: Chaining over-permissioned roles with secrets discovery techniques
- **Package Repository Poisoning**: Deployment of credential-stealing packages in legitimate software repositories

## Threat Actor Activities

- **GREYVIBE**: Russian-linked threat group conducting persistent AI-powered attacks against Ukrainian entities using ChatGPT and Gemini for enhanced social engineering campaigns
- **Kimsuky (Velvet Chollima)**: North Korean state-sponsored group deploying HTTPSpy malware and expanding arsenal with HelloDoor tools and VS Code tunnels targeting South Korean military and corporate entities
- **ShinyHunters**: Extortion gang responsible for major data breaches affecting Charter Communications (4.9M accounts) and Carnival Corporation (6M records)
- **The Com**: Neo-Nazi-affiliated criminal organization conducting cyberattacks to fund violent activities and exploitation operations
- **FortiClient EMS Attackers**: Unknown threat actors actively exploiting CVE-2026-35616 to deploy EKZ credential stealer malware
- **BTMOB Operators**: Cybercriminal service providing Android malware builder tools for custom phishing campaigns