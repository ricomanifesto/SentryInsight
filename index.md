# Exploitation Report

Recent intelligence highlights a surge in server-side exploitation aimed at gaining initial access for espionage, cryptomining, and large-scale DDoS operations. Three campaigns stand out: (1) the newly identified NightEagle APT weaponising an unpatched Microsoft Exchange zero-day to penetrate military and technology organisations in China; (2) Chinese-state operators chaining two Ivanti Connect Secure Appliance zero-days to compromise French government, telecom, and transport networks; and (3) financially motivated crews abusing exposed Java Debug Wire Protocol (JDWP) endpoints and poorly protected SSH services to deploy cryptocurrency miners and the “Hpingbot” DDoS toolkit. All attacks deliver full remote code execution or root-level control, underscoring the critical need for immediate patching, network hardening, and continuous threat hunting on externally exposed infrastructure.

## Active Exploitation Details

### Microsoft Exchange Server Zero-Day (NightEagle Campaign)
- **Description**: A previously undocumented flaw in on-premises Microsoft Exchange allows remote, unauthenticated attackers to achieve code execution. NightEagle leverages the bug in a post-authentication chain that bypasses normal access controls.
- **Impact**: Full compromise of Exchange servers, enabling email exfiltration, credential dumping, lateral movement, and persistent backdoors.
- **Status**: Actively exploited in the wild; no official patch released at publication time. Microsoft is reportedly investigating mitigations.

### Ivanti Connect Secure Appliance Dual Zero-Days
- **Description**: Two separate, freshly discovered vulnerabilities in Ivanti CSA enable authentication bypass followed by command injection. Attackers chain them for remote takeover.
- **Impact**: Complete administrative control of VPN gateways, session hijacking, deployment of webshells, and potential pivot into internal networks.
- **Status**: French CERT confirms ongoing exploitation against multiple sectors. Temporary mitigation guidance is available; permanent patches pending vendor release.

### Exposed JDWP Interfaces (Cryptomining Operations)
- **Description**: Misconfigured Java Debug Wire Protocol endpoints left open to the Internet grant arbitrary code execution within Java applications.
- **Impact**: Threat actors install customised XMRig miners, siphoning compute resources, and potentially opening additional backdoors.
- **Status**: Widespread exploitation observed; administrators must disable remote JDWP or restrict access. No vendor patch required—remediation is configuration hardening.

### SSH Compromise via Hpingbot for DDoS
- **Description**: Attackers brute-force weak SSH credentials, deploy the lightweight “Hpingbot,” and enrol victims into reflection/amplification DDoS campaigns.
- **Impact**: Full server takeover, outbound DDoS traffic, service disruption, and potential inclusion in larger botnets.
- **Status**: Continuous, automated exploitation. Defence hinges on strong credentials, MFA, and network-level brute-force protections.

## Affected Systems and Products

- **Microsoft Exchange Server**: On-premises Exchange 2016, 2019 (Windows Server)  
  **Platform**: Windows, self-hosted email infrastructure

- **Ivanti Connect Secure Appliance** (formerly Pulse Secure) versions prior to emergency fix  
  **Platform**: Purpose-built VPN gateways, often perimeter-facing

- **Java Applications with JDWP Enabled**: Custom or packaged enterprise apps exposing JDWP (default TCP/5005, 8000, 9000)  
  **Platform**: Cross-platform (Linux, Windows, macOS)

- **Linux/Unix Servers with SSH**: Systems using default or weak credentials, assorted distributions  
  **Platform**: Primarily cloud or data-centre Linux hosts

## Attack Vectors and Techniques

- **Zero-Day Exploitation (Exchange)**  
  - **Vector**: Crafted HTTP requests against vulnerable Exchange endpoints, bypassing authentication and executing payloads through server-side logic flaws.

- **Zero-Day Chaining (Ivanti CSA)**  
  - **Vector**: External attackers bypass login, inject commands via web interface, and drop webshells for persistent access.

- **JDWP Remote Code Execution**  
  - **Vector**: Direct socket connection to exposed JDWP port, issuing Java byte-code commands to spawn reverse shells and download miners.

- **SSH Brute-Force & Hpingbot Deployment**  
  - **Vector**: Credential stuffing on port 22; on success, attackers upload and execute the Hpingbot binary, configuring it for C2-directed DDoS floods.

## Threat Actor Activities

- **NightEagle (APT-Q-95)**  
  - **Campaign**: Focused on Chinese military and technology organisations. Utilises the Exchange zero-day for initial access, followed by bespoke PowerShell loaders and Cobalt Strike beacons.

- **Unnamed Chinese State Actor**  
  - **Campaign**: French ANSSI attributes Ivanti CSA intrusions to Beijing-linked operators targeting government, telecom, media, finance, and transport verticals for intelligence collection.

- **Cryptomining Crew (JDWP)**  
  - **Campaign**: Opportunistic mass-scanning of JDWP ports; drops modified XMRig and maintains persistence via systemd services.

- **Hpingbot Operators**  
  - **Campaign**: Global SSH brute-force wave enrolling compromised Linux servers into a DDoS botnet capable of TCP/UDP floods and reflection attacks. No nation-state ties observed; activity appears profit-driven via DDoS-for-hire services.

