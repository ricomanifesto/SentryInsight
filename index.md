# Exploitation Report

Current exploitation activity shows a concerning pattern of attacks targeting critical infrastructure and enterprise systems. Most notably, CISA has warned of active exploitation of a recently patched SolarWinds Serv-U vulnerability being used to crash servers. Additionally, Cisco has disclosed CVE-2026-20245, a high-severity zero-day in SD-WAN Manager enabling root privilege escalation that is currently being exploited in the wild. Threat actors are also actively exploiting a critical WordPress plugin flaw and targeting over 900 exposed gas station tank gauge systems across the United States. Supply chain attacks continue to pose significant threats, with multiple npm packages compromised by the IronWorm malware campaign and the Hola Browser suffering a supply chain compromise that delivered cryptocurrency mining malware.

## Active Exploitation Details

### SolarWinds Serv-U Vulnerability
- **Description**: A recently patched high-severity flaw in SolarWinds Serv-U that allows attackers to crash servers
- **Impact**: Denial of service attacks causing server crashes and potential service disruption
- **Status**: Actively exploited in the wild despite recent patches being available

### Cisco SD-WAN Manager Zero-Day
- **Description**: A high-severity unpatched vulnerability in Cisco Catalyst SD-WAN Manager enabling privilege escalation
- **Impact**: Attackers can gain root access to affected systems
- **Status**: Actively exploited in attacks with no patch currently available
- **CVE ID**: CVE-2026-20245

### Everest Forms Pro WordPress Plugin
- **Description**: Critical security flaw in the WordPress plugin allowing arbitrary code execution
- **Impact**: Complete site compromise and takeover
- **Status**: Actively exploited against sites with approximately 4,000 active installations

### Cisco Unified Communications Manager
- **Description**: Vulnerability allowing unauthenticated attackers to write files and escalate to root privileges
- **Impact**: Complete system compromise with root access
- **Status**: Recently patched as exploit code has gone public
- **CVE ID**: CVE-2026-20230

## Affected Systems and Products

- **SolarWinds Serv-U**: File transfer server software vulnerable to denial of service attacks
- **Cisco Catalyst SD-WAN Manager**: Network management platform with unpatched zero-day vulnerability
- **Everest Forms Pro WordPress Plugin**: Form builder plugin with approximately 4,000 active installations
- **Gas Station Tank Gauges**: Over 900 automatic tank gauge systems exposed online across US critical infrastructure
- **npm Package Repository**: Multiple packages compromised in IronWorm supply chain attack
- **Hola Browser**: Windows version compromised to deliver cryptocurrency mining malware
- **Microsoft IIS Servers**: Targeted by OP-512 threat cluster using custom web shell framework
- **Amazon AWS, Google Cloud, Microsoft Azure**: Cloud servers hijacked by PCPJack for SMTP relay network

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched Cisco SD-WAN vulnerability for privilege escalation
- **Supply Chain Attacks**: IronWorm malware targeting npm packages and browser software compromise
- **Web Shell Deployment**: OP-512 cluster using custom frameworks to maintain persistence on IIS servers
- **Credential Theft**: Polyfill-based attacks displaying fake login prompts on major websites
- **Cloud Infrastructure Hijacking**: PCPJack compromising 230 cloud servers across major providers
- **Critical Infrastructure Targeting**: Direct attacks on exposed gas station fuel monitoring systems
- **WordPress Plugin Exploitation**: Targeting vulnerable form plugins for site takeover

## Threat Actor Activities

- **UNC5221**: Chinese espionage group deploying Brickstorm backdoor, Plenet, and AgentPSD malware for persistent Microsoft 365 access
- **OP-512**: Previously unreported threat cluster targeting Microsoft IIS servers with sophisticated web shell frameworks
- **PCPJack**: Threat actor hijacking cloud infrastructure to create covert SMTP email relay networks across AWS, Google Cloud, and Azure
- **TA4922**: Chinese cybercrime group expanding operations globally beyond traditional East Asian targets
- **IronWorm Campaign**: Rust-based malware operation targeting npm supply chain with credential theft capabilities
- **Magecart Campaign**: Credit card theft operation abusing Stripe's API infrastructure to host stolen payment information