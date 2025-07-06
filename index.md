# Exploitation Report

Over the last week, security researchers and government agencies have confirmed multiple, unrelated campaigns leveraging fresh or still-unpatched vulnerabilities. The most critical activity centers on a new Microsoft Exchange zero-day weaponized by the NightEagle APT against Chinese defense and technology networks, and two authentication-bypass zero-days in Ivanti Connect Secure appliances actively abused by a China-nexus actor to breach French government and telecom targets. Separately, large-scale opportunistic attacks continue against internet-exposed Java Debug Wire Protocol (JDWP) interfaces, enabling cryptomining payloads, while the “Hpingbot” botnet is expanding via SSH brute-force for DDoS operations. The breadth of targets—from enterprise email and VPN infrastructure to poorly secured development ports—highlights the urgency of patching, network hardening, and continuous threat hunting.

## Active Exploitation Details

### Microsoft Exchange Server Zero-Day (NightEagle Campaign)
- **Description**: A previously unknown flaw in on-premises Microsoft Exchange that permits authenticated remote code execution followed by privilege escalation to SYSTEM. NightEagle chains it with post-exploitation toolsets to implant web shells.
- **Impact**: Full server takeover, email theft, lateral movement into Active Directory, and persistent access via web shells.
- **Status**: Confirmed in-the-wild exploitation; Microsoft has not yet released a formal patch but is expected to issue out-of-band mitigations.

### Ivanti Connect Secure / Policy Secure Zero-Days
- **Description**: Two distinct vulnerabilities in Ivanti Connect Secure (formerly Pulse Secure) appliances: one allows authentication bypass, the other enables command injection through crafted HTTPS requests.
- **Impact**: Remote attackers obtain administrator privileges, extract configuration secrets, pivot into internal networks, and deploy additional malware.
- **Status**: Actively exploited in French government and telecom environments; Ivanti has issued temporary mitigation guidance with patches forthcoming.

### Exposed Java Debug Wire Protocol (JDWP) Interfaces
- **Description**: JDWP, intended for local debugging of Java applications, listens on TCP (default 8000/8001). When left exposed without authentication, it grants arbitrary code execution by injecting Java byte-code.
- **Impact**: Adversaries install cryptocurrency miners, create reverse shells, and manipulate host resources, leading to financial loss and potential follow-on attacks.
- **Status**: Ongoing mass scanning and exploitation; no vendor patch required—mitigation involves disabling or firewalling JDWP.

### Hpingbot SSH Compromise Vector
- **Description**: The Hpingbot botnet brute-forces weak SSH credentials, then deploys the open-source tool “hping3” to orchestrate high-volume UDP and TCP floods for DDoS.
- **Impact**: Server enlistment into DDoS botnets, service disruption, bandwidth exhaustion, and possible reputational damage.
- **Status**: Active global campaign; defenders must strengthen SSH hygiene and implement rate-limiting.

## Affected Systems and Products

- **Microsoft Exchange Server (On-Prem)**  
  - **Platform**: Windows Server; Exchange 2019, 2016, and older versions still under extended support

- **Ivanti Connect Secure / Policy Secure Gateways**  
  - **Platform**: Hardened Linux-based VPN/SSA appliances across enterprise and government environments

- **Java Application Servers with JDWP Enabled**  
  - **Platform**: Linux/Windows hosts running Apache Tomcat, Jetty, JBoss, or custom JVM-based services

- **Linux/Unix Servers with SSH Exposed to Internet**  
  - **Platform**: Any distribution permitting password-based SSH authentication

## Attack Vectors and Techniques

- **Zero-Day RCE via Crafted Exchange Requests**  
  - **Vector**: Malformed EWS/OWA request chain resulting in web-shell drop to `/owa/auth/` directory

- **Authentication Bypass + Command Injection on Ivanti**  
  - **Vector**: Sequence of HTTPS calls to uncommon API endpoints, bypassing SAML/LDAP checks and writing arbitrary files

- **JDWP Remote Byte-Code Injection**  
  - **Vector**: Direct socket connection on port 8000 sending `VirtualMachine/LoadAgent` commands to execute shell scripts

- **SSH Credential Stuffing / Brute Force (Hpingbot)**  
  - **Vector**: Distributed login attempts using common username/password pairs; successful logins followed by script-based installation of `hping3`

## Threat Actor Activities

- **NightEagle (APT-Q-95)**  
  - **Campaign**: Targeting Chinese military R&D and high-tech suppliers; leverages Exchange zero-day, drops custom “EagleEye” web shell, and exfiltrates defense project emails.

- **Unnamed China-Aligned Actor (Ivanti Exploits)**  
  - **Campaign**: Multi-sector intrusions in France; post-exploitation includes reconnaissance, VPN account creation, and data staging for exfiltration.

- **Cryptojacking Group Leveraging JDWP**  
  - **Campaign**: Opportunistic mining using XMRig variants; observed deploying persistence via `systemd` service files.

- **Hpingbot Botnet Operators**  
  - **Campaign**: Builds a DDoS network primarily for rent on dark-web forums; infrastructure observed launching volumetric attacks exceeding 200 Gbps.

---

**Bold** mitigation emphasis: Immediately apply vendor mitigations for Exchange and Ivanti, restrict JDWP to trusted hosts, enforce SSH key-based authentication, and monitor for web-shell and `hping3` binaries to contain active threats.