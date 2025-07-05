# Exploitation Report

Recent intelligence highlights two high-impact exploitation campaigns: a previously undocumented actor dubbed **NightEagle (APT-Q-95)** is weaponizing a zero-day in on-premises Microsoft Exchange Server to gain persistent footholds inside Chinese military and technology organizations, while a separate Chinese state-aligned cluster is abusing freshly discovered **Ivanti Connect Secure Appliance (CSA) zero-days** to infiltrate French government, telecom, finance, media, and transport networks. Both operations feature rapid, covert post-exploitation activity that enables credential theft, lateral movement, and long-term espionage. Emergency mitigations and vendor patches are either unavailable or only partially deployed, leaving exposed infrastructure at significant risk.

## Active Exploitation Details

### Microsoft Exchange Server Zero-Day (NightEagle Campaign)
- **Description**: An as-yet unnamed remote code execution flaw in Microsoft Exchange Server that allows unauthenticated attackers to bypass existing mitigations and drop web shells directly into the `wwwroot` directory. The zero-day is triggered through a crafted `Autodiscover/` request chain that manipulates serialization logic inside the Exchange Front-End.
- **Impact**: Full system compromise, arbitrary command execution under SYSTEM, ability to harvest mailbox data, pivot to domain controllers, and establish long-term persistence.
- **Status**: Actively exploited in the wild by NightEagle; Microsoft has not released a patch or formal advisory at this time.  
  Administrators must rely on strict perimeter filtering of Exchange endpoints and continuous integrity monitoring of key directories until an official fix is issued.

### Ivanti Connect Secure Appliance Zero-Days (Chinese State-Aligned Intrusions)
- **Description**: Two distinct zero-day flaws in Ivanti CSA VPN gateways—one enabling authentication bypass via session manipulation, the other allowing post-auth file-write leading to code execution. Chaining the bugs lets attackers implant backdoors in the `/data/runtime/tmp/` path that survive reboots and firmware upgrades.
- **Impact**: Device take-over, credential harvesting for downstream resources, traffic interception, and the creation of site-to-site tunnels into protected government and enterprise networks.
- **Status**: Confirmed active exploitation against multiple French critical-sector entities. Ivanti released interim mitigations (external integrity checker, signature updates) and promises firmware patches “in the coming days.” Appliances should be isolated, scanned for indicators, and rebuilt where compromise is suspected.

## Affected Systems and Products

- **Microsoft Exchange Server (on-premises)**: All supported cumulative update levels; both Standard and Enterprise editions on Windows Server 2016/2019/2022.  
- **Ivanti Connect Secure / Policy Secure Appliances**: Hardware and virtual appliances running all 9.x and 22.x firmware tracks, including cloud-hosted deployments.  
- **Downstream Assets**: Active Directory domain controllers, file shares, and sensitive application servers reachable from the compromised VPN or Exchange segments.

## Attack Vectors and Techniques

- **Web-Shell Implantation via Autodiscover Abuse**  
  Vector: Crafted HTTP requests leverage the zero-day to bypass Exchange authentication, writing web shells (`asp`, `aspx`) to publicly accessible paths for command execution.

- **Session Hijack & File-Write Chain on Ivanti CSA**  
  Vector: Attackers manipulate session cookies to skip login, then exploit a secondary flaw to write executable payloads that run with root privileges on the gateway.

- **Credential Dumping & Lateral Movement**  
  Technique: Post-exploitation scripts (Mimikatz variants, LSASS memory dumps) extract domain credentials, followed by Kerberos ticket abuse and SMB session hijacking.

- **Encrypted C2 over Portals & Proxies**  
  Vector: Reverse HTTPS beacons masquerade as legitimate Exchange ECP traffic or Ivanti maintenance channels to evade perimeter inspection.

## Threat Actor Activities

- **Actor/Group**: NightEagle (APT-Q-95)  
  **Campaign**: Targeted intrusions against Chinese aerospace R&D and PLA-affiliated universities. Tactics include custom PowerShell loaders, DLL side-loading, and selective exfiltration of classified project data.

- **Actor/Group**: Unnamed Chinese State-Aligned Cluster  
  **Campaign**: Multi-wave exploitation of Ivanti CSA zero-days since early June, focusing on French government ministries, telecom backbone providers, national rail infrastructure, and major banks. Observed objectives are persistent network access and intelligence collection rather than immediate monetization.