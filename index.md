# Exploitation Report

Critical exploitation activity is currently centered around several high-impact vulnerabilities and sophisticated attack campaigns. Most notably, threat actors have been actively exploiting a zero-day vulnerability in legacy Sitecore deployments to deploy WeepSteel reconnaissance malware and backdoors. This vulnerability represents a significant threat to organizations using Sitecore content management systems. Additionally, Russian state-sponsored group APT28 has been conducting targeted attacks against NATO countries using a new Microsoft Outlook backdoor called "NotDoor," demonstrating the ongoing sophistication of nation-state threat actors. The threat landscape also includes innovative phishing campaigns leveraging SVG files and ViewState attacks, as well as a large-scale phishing-as-a-service operation running undetected on major cloud platforms for over three years.

## Active Exploitation Details

### Sitecore Zero-Day Vulnerability
- **Description**: A zero-day vulnerability in legacy Sitecore content management system deployments that allows threat actors to gain unauthorized access and deploy malicious payloads
- **Impact**: Attackers can deploy WeepSteel reconnaissance malware and establish persistent backdoors on compromised systems
- **Status**: Actively exploited in the wild, represents the latest example of threat actors weaponizing exposed ASP.NET machine keys for remote injection and deserialization attacks

### Microsoft Outlook Backdoor (NotDoor)
- **Description**: A sophisticated backdoor targeting Microsoft Outlook deployed by Russian APT28 group
- **Impact**: Enables persistent access to corporate email systems and sensitive communications in targeted organizations
- **Status**: Active deployment against multiple companies across different sectors in NATO countries

### SVG-Based Phishing Campaign
- **Description**: Malicious campaign leveraging Scalable Vector Graphics (SVG) files to deploy Base64-encoded phishing pages
- **Impact**: Bypasses traditional security detection mechanisms by using legitimate file formats for malicious purposes
- **Status**: 44 undetected SVG files identified by VirusTotal, impersonating Colombian judicial system

## Affected Systems and Products

- **Sitecore Content Management Systems**: Legacy deployments vulnerable to zero-day exploitation and ViewState attacks
- **Microsoft Outlook**: Targeted by NotDoor backdoor in corporate environments across NATO countries
- **ASP.NET Applications**: Systems with exposed machine keys vulnerable to remote injection and deserialization attacks
- **Google and Cloudflare Infrastructure**: Hosting phishing-as-a-service operations for over 3 years
- **Web Browsers**: Targeted by SVG-based phishing campaigns and search engine manipulation attacks

## Attack Vectors and Techniques

- **ViewState Exploitation**: Weaponization of exposed ASP.NET machine keys for remote code injection and deserialization attacks
- **SVG File Abuse**: Using legitimate Scalable Vector Graphics files to host Base64-encoded phishing content that evades detection
- **Email Backdoor Deployment**: Installation of persistent backdoors in Microsoft Outlook for long-term access to corporate communications
- **Search Engine Manipulation**: Malicious IIS module injection to artificially boost gambling site rankings in search results
- **Cloud Infrastructure Abuse**: Leveraging legitimate cloud services from Google and Cloudflare to host phishing operations while avoiding detection

## Threat Actor Activities

- **APT28 (Russian State-Sponsored)**: Conducting targeted attacks against NATO countries using NotDoor Outlook backdoor, focusing on multiple companies across different sectors
- **GhostRedirector**: Chinese threat actor group using malicious IIS modules to inject links and manipulate Google search rankings for gambling sites
- **Colombian Judicial System Impersonators**: Threat actors conducting phishing campaigns using SVG files to impersonate legitimate government institutions
- **Phishing-as-a-Service Operators**: Global enterprise running undetected phishing operations on major cloud platforms for over three years using advanced cloaking techniques