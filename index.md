# Exploitation Report

Over the last week, defenders have observed two critical vulnerabilities being weaponized in the wild. Attackers are mass-exploiting TP-Link home/SMB routers (CVE-2023-33538) and a recently disclosed remote-code-execution flaw in the Langflow AI framework to gain initial access, build DDoS botnets, and pivot deeper into networks.  CISA’s rapid addition of the TP-Link bug to the Known Exploited Vulnerabilities (KEV) catalog underscores its severity, while the Flodrix operators’ quick adaptation highlights the growing speed at which threat actors integrate freshly disclosed issues into active campaigns.

## Active Exploitation Details

### TP-Link Router Remote Code Execution
- **Description**: A command-injection issue in the web-management interface allows unauthenticated attackers to execute arbitrary system commands on vulnerable TP-Link routers.
- **Impact**: Full takeover of the router, network reconnaissance, traffic interception, botnet enrollment, and persistence for subsequent attacks on internal assets.
- **Status**: Confirmed active exploitation; CISA added the flaw to KEV and mandated federal agencies to patch. TP-Link has released fixed firmware.
- **CVE ID**: CVE-2023-33538

### Langflow AI Server Remote Code Execution
- **Description**: Input validation weaknesses in Langflow’s flow-handling modules permit crafted requests that spawn system shells under the server account.
- **Impact**: Attackers install the Flodrix malware, turning compromised AI servers into nodes that launch distributed-denial-of-service (DDoS) attacks and potentially exfiltrate local data.
- **Status**: Actively exploited in a new Flodrix campaign. A patched version of Langflow has been published on GitHub and PyPI.

## Affected Systems and Products

- **TP-Link Wi-Fi Routers (e.g., Archer AX21, AX1800, WR series)**  
  • **Platform**: Embedded Linux-based firmware exposed on residential and small-office networks

- **Langflow Open-Source AI Framework (all releases prior to the current patched build)**  
  • **Platform**: Python-based web servers running on Linux or Windows in on-prem and cloud environments

## Attack Vectors and Techniques

- **Unauthenticated HTTP Command Injection**  
  • **Vector**: Direct requests to vulnerable CGI endpoints on TP-Link routers to append command separators (`;`, `&&`) and run arbitrary OS commands.

- **Malicious Flow Deserialization**  
  • **Vector**: Uploading or invoking specially crafted Langflow JSON flow objects that trigger `subprocess` execution when parsed by the server.

- **Botnet Enrollment & DDoS Launch**  
  • **Vector**: Post-exploitation script fetches Flodrix binaries from attacker-controlled infrastructure, adds the device to a hard-coded C2 list, and schedules periodic traffic floods.

## Threat Actor Activities

- **Flodrix Botnet Operators**  
  • **Campaign**: Leveraging the Langflow RCE to expand their botnet, primarily for Layer-4 and Layer-7 DDoS attacks against gaming and fintech targets.

- **Unidentified Mass-Scanning Clusters**  
  • **Campaign**: Wide-scale Internet scanning for TP-Link routers on ports 80/443, immediately running exploit scripts to deploy Mirai-like payloads and custom proxy modules.