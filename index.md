# Exploitation Report

During the past week, the most consequential exploitation activity revolves around two zero-day vulnerabilities in Ivanti Connect Secure Appliance (CSA) that are being weaponized by Chinese state-aligned actors against multiple French government and telecom targets. Parallel investigations revealed that an initial-access broker (likely China-nexus) is also abusing these same flaws, even self-patching compromised appliances to retain exclusive foothold. Separately, four Chromium zero-days—previously observed in real-world attacks against Google Chrome—remain exploitable through Grafana’s widely-deployed Image Renderer plug-in until administrators apply the latest emergency update. These vulnerabilities enable attackers to execute arbitrary code, steal credentials, and pivot deeper into enterprise environments, underscoring the urgency of rapid patching and robust network monitoring.

## Active Exploitation Details

### Ivanti Connect Secure Appliance Zero-Day Chain
- **Description**: A pair of unpatched flaws in Ivanti CSA allow remote, unauthenticated attackers to chain an authentication-bypass with a command-injection bug, achieving full control of the VPN gateway.  
- **Impact**: Attackers can run arbitrary commands, implant webshells, harvest credentials, and pivot into internal networks to exfiltrate sensitive data.  
- **Status**: Confirmed active exploitation by Chinese threat actors and by an initial-access broker who post-compromise “self-patches” the devices to block competitors. Ivanti has released interim mitigations; a permanent fix is pending.

### Grafana Image Renderer Plug-in – Embedded Chromium Zero-Days
- **Description**: The Image Renderer plug-in bundles an outdated Chromium engine containing four distinct zero-day vulnerabilities that have been exploited in the wild against Chrome users (use-after-free and type-confusion flaws).  
- **Impact**: Successful exploitation enables remote code execution in the context of the Grafana service, potentially leading to lateral movement and full-stack compromise of monitoring infrastructure.  
- **Status**: Grafana Labs issued critical updates for both the Image Renderer plug-in and the Synthetic Monitoring Agent. Exploitation has been observed in the broader Chromium ecosystem; organizations must patch immediately to remove the vulnerable engine.

## Affected Systems and Products

- **Ivanti Connect Secure Appliance (CSA)**: All supported firmware versions prior to the forthcoming security release  
  - **Platform**: Physical and virtual VPN gateways deployed in enterprise and government networks  

- **Grafana Image Renderer Plug-in**: Versions shipping with the vulnerable embedded Chromium builds (pre-patch)  
  - **Platform**: Linux and Windows servers running Grafana OSS or Enterprise; also affects Grafana Cloud users with self-hosted renderers  

## Attack Vectors and Techniques

- **VPN Appliance Exploitation**  
  - **Vector**: Direct interaction with Ivanti CSA web interface over HTTPS; attackers chain authentication bypass and command injection without valid credentials.  

- **Self-Patching Post-Exploitation**  
  - **Vector**: After compromising Ivanti appliances, the threat actor uploads modified binaries that patch the vulnerabilities locally, preventing other attackers from exploiting the same zero-days.  

- **Embedded Browser Engine RCE**  
  - **Vector**: Crafted requests rendered by Grafana’s Image Renderer force vulnerable Chromium code paths, triggering use-after-free or type-confusion bugs that yield remote code execution.

## Threat Actor Activities

- **Actor/Group**: Suspected Chinese state-aligned operators  
  - **Campaign**: Coordinated attacks against French government, telecommunications, finance, media, and transport sectors exploiting Ivanti CSA zero-days to gain persistent access and conduct reconnaissance.

- **Actor/Group**: Unnamed China-nexus Initial-Access Broker (IAB)  
  - **Campaign**: Mass exploitation of Ivanti appliances for resale of network access. The IAB uniquely “self-patches” infected devices—blocking rival intrusion attempts and solidifying its turf.

- **Actor/Group**: Opportunistic cybercriminals leveraging legacy Chromium zero-days  
  - **Campaign**: Targeting Grafana installations exposed to the Internet in order to execute malware, harvest credentials, and expand into monitoring environments often rich with infrastructure secrets.

