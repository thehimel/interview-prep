# Questions

Source: [Computer Networking: A Top-down Approach](https://gaia.cs.umass.edu/kurose_ross/lectures.php)

## Core Concepts

- OSI Model vs. TCP/IP Protocol Stack.
- TCP vs. UDP.
- Formats: TCP, IPv4, IPv4, Ethernet, IPSec.
- IPv4 vs. IPv6.
- NAT in IPv4.
- ARP for Ethernet.
- IPSec and VPN.
- Router Architecture.
- Routing Algorithgms: DJ and BF.
- Routing Protocols: OSPF, RIP, and BGP.

## Chapter 1: Computer Networks and the Internet

- What is a protocol? `**`
- What are routing and forwarding? `***`
- What are delay, loss, and throughput?
- OSI Model vs. TCP/IP Protocol Stack. `***`
- How various protocols stay in the TCP/IP Protocol Stack? `***`
- How does a packet traverse throguh various layers of TCP/IP Protocol Stack?
- Types of attack: Sniffing, IP Spoffing, DoS, DDoS.
- Lines of defense: Authentication, Authorization, Confidentiality, Integrity, Firewall.

## Chapter 2: The Application Layer

- Client-server architecture. `**`
- URI = URN + URL + URC. `**`
- Peer-peer (P2P) architecture.
- What is a socket? `***`
- TCP vs. UDP. `***`
- What is RTT?
- What is HTTP? Features of HTTP. `***`
- Non-persistent vs. Persistent TCP. `***`
- Non-persistent vs. Persistent HTTP. `***`
- HTTP 1.0 vs. HTTP 1.1. `***`
- HTTP 1.1 vs. HTTP 2.0. `***`
- Sequential and piplelined orders in persistent TCP. `***`
- HOL blocking in persistent TCP connection. `***`
- HTTP Request and Response Message formats. `***`
- HTTP Verbs/Methods. `***`
- HTTP respnse status codes. `***`
- How a client can manage state with cookies? What cookies can be used for?
- How caching can increase performance?
- HTTP 2.0. Multiplexing and Demultiplexing with SPDY in HTTP 2.0. How HTTP 2.0 mitigates HOL blocking? `***`
- Explain prioritization and server push in SPDY. `**`
- HTTP 3.0 and how QUIC works. How HTTP 3.0 solves HOL blocking. `***`
- DNS. Name resolution by DNS. Whay DNS is decentralized?
- Root, TLD, and Authoritative DNS Servers. `***`
- DNS records. A, AAAA, NS, CNAME, and MX records. `***`
- DDos and Spoffing attacks in DNS.
- What is CDN? Who CDN can be used to increase the performance of a website?

## Chapter 3: The Transport Layer

- Multiplexing and Demultiplexing in TCP. `***`
- UDP Packet format. `***`
- Features of TCP: Connection oriented, MUX & DEMUX, P2P, Reliability with in-order and retransmission, congestion, and flow control. `***`
- TCP Segment Structure. `***`
- TCP sequence number and ackowledgement number. `***`
- Congestion control vs. flow control.
- TCP flow control and congestion control. `***`
- 3-way handshake in TCP. `***`
- Closing a TCP connection. `***`
- QUIC.
- Well known ports: HTTP 80, HTTP 443, FTP 21, SMTP 25, and IPSec 500.

## Chapter 4: The Network Layer: the Data Plane

- Data plane vs. control plane. `***`
- Two control plane approaches: Per-router control plane and SDN. `***`
- Router architecture. `***`
- Input port functions. Lookup, forwarding, and queuing in input port. `**`
- Destination-based forwarding. `***`
- Longest Prefix Match (LPM). Routing aggregation with LPM. `***`
- Switching fabric. Switching rate in router.
- 3 major types of switching fabrics: memory, bus, and interconnection network. `***`
- Output port buffering and queuing. `***`
- Types of packet scheduling in output ports: FCFS, Prority, Round Robin (RR), Weighted Fair Queuing. `***`
- Network neutrality.
- IPv4 Datagram format. `***`
- Classful IP addressing. `**`
- Structure of IP address. What is a subnet? `**`
- Classless InterDomain Routing (CIDR). How CIDR is used for subnetting in IPv4? `**`
- Static vs. DHCP routing. `**`
- How DHCP handshake takes place between client and server? `**`
- Public IP vs. Private IP. `***`
- Network Address Translation (NAT). How NAT preserves the number of IPv4 addresses. `**`
- IPv6 Datagram format. `***`
- Why IPv6? Public IPs in IPv4 and IPv6. `***`
- Transition from IPv4 to IPv6 with tunneling. `***`
- IPv4 vs. IPv6. `***`
- IPv6 features drop compared to IPv6: Checksum, Fragmentation, and Options. `***`

## Chapter 5: The Network Layer: the Control Plane

- Different types of DHCP - OSPF, RIP, and BGP. `***`
- Routing algorithms: Dijkstra’s link-state routing algorithm, Bellman-Ford distance vector algorithm. `***`
- Intra-Domain vs. Inter-Domain routing protocols. `***`
- Intra-AS routing protocols: OSPF and RIP. `***`
- Areas in OSPF. `***`
- Two-level Hierarchical OSPF. `***`
- Count-to-infinity problem in distance vector algorithm. Solution: split horizon and router poisoning. `***`
- Count-to-infinity problem in OSPF. Solution: split horizon and router poisoning. `***`
- Inter-AS routing: BGP. eBGP vs. iBGP. `***`
- How BGP solves count-to-infinity problem? `***`
- Hot potato routing in BGP.
- DHCP attacks: DoS, and MITM.

## Chapter 6: The Link Layer

- Internet checksum.
- Cyclic Redundancy Check (CRC). `***`
- MAC address. `**`
- Address Resolution Protocol (ARP) and Reverse Address Resolution Protocol (RARP). `***`
- Man-in-the-middle (MITM) attack in ARP.
- Ethernet frame structure. `***`
- Packet Datagram Unit (PDU). Construction of a TCP/IP ethernet data packet. `***`
- Switching vs. routing. `***`
- Hub, Switch, vs. Router. `**`
- ICMP. `**`

## Chapter 8: Network Security

- IP Security (IPSec). `***`
- What is Asymmetric Encryption? How is it used in IPSec? `***`
- How does IPsec work? Key exchange, packet headers and trailers, authentication, encryption, transmission, and decryption. `***`
- What protocols are used in IPsec? Authentication Header (AH), Encapsulating Security Protocol (ESP), Security Association (SA), and Internet Protocol (IP). `***`
- What is the difference between IPsec tunnel mode and IPsec transport mode? `***`
- What port does IPsec use?
- How does IPsec impact MSS and MTU? `**`
- What is a VPN? How IPSec can be used in VPN? `***`
- VPN. Types of VPN.
- VPN vs. Proxy.
- How does a VPN work?
- Features security features: authentication, authorization, privacy, confidentiality, and integrity. `**`
