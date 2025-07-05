# Exploitation Report

The last 48 hours reveal a sharp uptick in zero-day exploitation against perimeter infrastructure and misconfigured services. The most critical activity involves a previously unknown Microsoft Exchange vulnerability abused by the newly identified NightEagle APT and a tandem of zero-days targeting Ivanti Connect Secure Appliances leveraged by Chinese state-aligned actors against French government and telecom networks. In parallel, opportunistic attackers are mass-scanning for exposed Java Debug Wire Protocol (JDWP) interfaces to gain remote code execution for cryptomining, while the Hpingbot botnet continues its aggressive SSH-brute-force campaign, converting compromised Linux hosts into DDoS launch pads.

## Active Exploitation Details

### Microsoft Exchange Server Zero-Day exploited by NightEagle
- **Description**: An undisclosed flaw in on-premises Microsoft Exchange Server allowing unauthenticated remote code execution followed by web-shell deployment. The bug is being used as an initial access vector in a targeted attack chain.
- **Impact**: Full server takeover, email theft, lateral movement into internal Active Directory environments.
- **Status**: Actively exploited in the wild; no official patch released at reporting time, only mitigations (URL rewrite rules and removal of dropped web-shells).

### Ivanti Connect Secure Appliance (CSA) Zero-Day Chain
- **Description**: Two previously unknown vulnerabilities (one authentication bypass, one command injection) chained to achieve root-level access on Ivanti CSA VPN gateways.
- **Impact**: Complete device compromise enabling credential harvesting, traffic interception, and deployment of persistent backdoors.
- **Status**: Actively exploited against French government, telecom, media, finance, and transport entities; emergency patches and signatures released by Ivanti, with guidance from CERT-FR.

### Exposed Java Debug Wire Protocol (JDWP) Interfaces
- **Description**: JDWP left open to the Internet (default port 8787) grants attackers interactive code-execution within Java virtual machines.
- **Impact**: Remote code execution leading to download and execution of Monero cryptominers, privilege escalation, and potential lateral movement.
- **Status**: Ongoing mass-exploitation campaign; no vendor patch required—remediation involves disabling or properly binding JDWP to localhost.

### Hpingbot SSH Brute-Force Campaign
- **Description**: The Hpingbot botnet aggressively brute-forces SSH credentials, installs its payload, and arms compromised Linux servers with packet-crafting capabilities for large-scale DDoS.
- **Impact**: Service disruption for targeted organizations, bandwidth consumption, and reputational damage.
- **Status**: Active; defenders advised to enforce key-based auth and rate-limit SSH.

## Affected Systems and Products

- **Microsoft Exchange Server**: All on-prem versions; particularly unpatched installations exposed to the Internet  
  **Platform**: Windows Server environments  
- **Ivanti Connect Secure Appliance**: All supported firmware versions prior to emergency hotfix  
  **Platform**: Hardware/virtual VPN gateways (CSA)  
- **Java-based Application Servers** (Tomcat, JBoss, WebLogic, custom JVM services) with JDWP enabled and externally reachable  
  **Platform**: Linux and Windows servers running Java  
- **Linux Servers with SSH Exposed to Internet**: Systems lacking strong authentication protections  
  **Platform**: Primarily cloud and on-prem Linux distributions  

## Attack Vectors and Techniques

- **Exchange Web-Shell Deployment**  
  - **Vector**: Crafted HTTP request exploits Exchange zero-day, drops China-Chopper-style web-shell under /owa or /ecp paths.
- **Ivanti CSA Command Injection via Web Interface**  
  - **Vector**: Chained auth bypass + parameter manipulation in maintenance API, executes root-level shell commands.
- **JDWP Remote Code Execution**  
  - **Vector**: Direct socket connection to TCP/8787, use of JDWP commands (VirtualMachine/InvokeMethod) to run bash one-liners that fetch miners.  
- **SSH Credential Stuffing & Brute Force**  
  - **Vector**: Distributed SSH login attempts using common/default credentials; on success, hping3-based bot binary is installed.

## Threat Actor Activities

- **NightEagle (APT-Q-95)**  
  - **Campaign**: Zero-day exploitation of Microsoft Exchange to infiltrate Chinese military R&D institutes and defense-adjacent tech companies. Post-exploitation involves Cobalt Strike beacons and custom backdoor “WingFalcon.”
- **Unnamed Chinese State-Aligned Group** (linked by CERT-FR)  
  - **Campaign**: Systematic compromise of Ivanti CSA gateways across French critical sectors to harvest VPN credentials and pivot into internal networks.
- **Cryptomining Operators (JDWP Campaign)**  
  - **Campaign**: Opportunistic attacks against globally exposed JDWP interfaces; drop GitHub-hosted shell scripts that install XMRig, using proxy pools for evasion.
- **Hpingbot Botnet Maintainers**  
  - **Campaign**: Ongoing SSH brute-force wave adding servers to a DDoS-for-hire network; observed leveraging spoofed source IPs to flood gaming and finance targets.

