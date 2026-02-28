# Exploitation Report

The security landscape reveals significant exploitation activity across multiple critical infrastructure sectors. Most notably, a zero-day vulnerability in Cisco SD-WAN systems has been actively exploited for three years by sophisticated threat actors, while Ivanti Connect devices continue to face active exploitation through the RESURGE malware implant. North Korean threat groups APT37 and ScarCruft are deploying advanced tools to breach air-gapped networks, and over 900 Sangoma FreePBX instances remain compromised from ongoing web shell attacks. Additionally, threat actors are leveraging exposed Google Cloud API keys to access sensitive Gemini AI data, while critical vulnerabilities in Trend Micro Apex One and Juniper Networks PTX routers present immediate remote code execution risks.

## Active Exploitation Details

### Cisco SD-WAN Zero-Day Vulnerability
- **Description**: A maximum-severity zero-day vulnerability in Cisco SD-WAN systems that has been under active exploitation
- **Impact**: Full system compromise by sophisticated threat actors with minimal evidence left behind
- **Status**: Actively exploited for 3 years by unknown advanced persistent threat actors
- **CVE ID**: CVE-2026-20127

### Ivanti Connect Secure Zero-Day
- **Description**: Zero-day vulnerability exploited to deploy RESURGE malware implant on Ivanti Connect Secure devices
- **Impact**: Persistent backdoor access that can remain dormant on compromised systems
- **Status**: Active exploitation with RESURGE malware remaining on affected devices even after patching
- **CVE ID**: CVE-2025-0282

### Sangoma FreePBX Command Injection
- **Description**: Command injection vulnerability in Sangoma FreePBX systems leading to web shell deployment
- **Impact**: Remote code execution and persistent access to telecommunications systems
- **Status**: Over 900 instances remain compromised with web shells from attacks beginning in December

### Google Cloud API Key Abuse
- **Description**: Previously harmless Google API keys can now authenticate to sensitive Gemini AI endpoints
- **Impact**: Access to private data through Gemini AI assistant and unauthorized API usage
- **Status**: Thousands of exposed API keys identified with potential for ongoing abuse

## Affected Systems and Products

- **Cisco SD-WAN Systems**: All SD-WAN infrastructure vulnerable to three-year exploitation campaign
- **Ivanti Connect Secure**: Devices compromised with RESURGE malware implants
- **Sangoma FreePBX**: Over 900 instances currently infected with web shells
- **Google Cloud Services**: API keys with Gemini access exposed across thousands of projects
- **Trend Micro Apex One**: Windows systems vulnerable to critical remote code execution flaws
- **Juniper Networks PTX Series**: Routers running Junos OS Evolved at risk of full takeover
- **Windows Systems**: Air-gapped networks targeted by APT37 malware via removable drives

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Long-term exploitation of undisclosed vulnerabilities in critical infrastructure
- **Web Shell Deployment**: Command injection leading to persistent backdoor access
- **Air-Gap Bridging**: USB-based malware designed to move data between isolated and connected networks
- **API Key Abuse**: Leveraging exposed credentials to access unauthorized cloud services
- **Blockchain C2 Infrastructure**: Aeternum botnet using Polygon blockchain for resilient command and control
- **Social Engineering**: Trojanized gaming tools distributed via browsers and chat platforms
- **Supply Chain Targeting**: Malicious Go crypto modules in software repositories

## Threat Actor Activities

- **APT37 (North Korean)**: Deploying new malware tools to breach air-gapped networks using removable drives for covert surveillance operations
- **ScarCruft (North Korean)**: Using Zoho WorkDrive for C2 communications and USB malware to target air-gapped systems
- **UAT-10027**: Previously undocumented threat cluster targeting U.S. education and healthcare sectors with Dohdoor backdoor since December 2025
- **Unknown Advanced Actor**: Three-year exploitation campaign against Cisco SD-WAN infrastructure with sophisticated evasion techniques
- **Kimwolf Botnet Operators**: Operating world's largest botnet through exploited vulnerability disclosed by security researcher
- **The Com Cybercrime Collective**: 30 arrests in Europol operation targeting online criminal group exploiting children and teenagers