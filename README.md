# SRv6 Path Control by FRRouting

Topology
![Topology Diagram](https://github.com/ishikawaya/clab-lab02-segment-routing/blob/main/images/lab02-topology.png)

- r[12] is vrf blue.
- r[56] is vrf red.

## VRF blue Path Control at PE1
- PE3 vrf blue End.DT4, End.DT6 Function
```
pe3# show ipv6 route 
Codes: K - kernel route, C - connected, L - local, S - static,
       R - RIPng, O - OSPFv3, I - IS-IS, B - BGP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, F - PBR,
       f - OpenFabric, t - Table-Direct,
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup
       t - trapped, o - offload failure

IPv6 unicast VRF default:
--- snip ---
B>* fc00:0:3:1::/128 [20/0] is directly connected, blue, seg6local End.DT4 table 10, weight 1, 00:40:48
B>* fc00:0:3:2::/128 [20/0] is directly connected, blue, seg6local End.DT6 table 10, weight 1, 00:40:48
--- snip ---
```
- Path Control Command in Linux
```bash
ip -6 route add fc00:0:3:1::/128 encap seg6 mode encap segs fc00:0:2::1,fc00:1:2::1,fc00:0:4::1,fc00:0:3::1 dev eth1
ip -6 route add fc00:0:3:2::/128 encap seg6 mode encap segs fc00:0:2::1,fc00:1:2::1,fc00:0:4::1,fc00:0:3::1 dev eth1
```
- Flow after Path Control
- ![Path Control1](https://github.com/ishikawaya/clab-lab02-segment-routing/blob/main/images/lab02-topology-path-control1.png)

## VRF blue Path Control at PE2
- PE3 vrf blue End.DT4, End.DT6 Function
```
pe3# show ipv6 route 
Codes: K - kernel route, C - connected, L - local, S - static,
       R - RIPng, O - OSPFv3, I - IS-IS, B - BGP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, F - PBR,
       f - OpenFabric, t - Table-Direct,
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup
       t - trapped, o - offload failure

IPv6 unicast VRF default:
--- snip ---
B>* fc00:0:3:3::/128 [20/0] is directly connected, red, seg6local End.DT4 table 20, weight 1, 00:40:48
B>* fc00:0:3:4::/128 [20/0] is directly connected, red, seg6local End.DT6 table 20, weight 1, 00:40:48
--- snip ---
```
- Path Control Command in Linux
```bash
ip -6 route add fc00:0:3:3::/128 encap seg6 mode encap segs fc00:0:1::1,fc00:1:1::1,fc00:1:2::1,fc00:0:4::1,fc00:0:3::1 dev eth2
ip -6 route add fc00:0:3:4::/128 encap seg6 mode encap segs fc00:0:1::1,fc00:1:1::1,fc00:1:2::1,fc00:0:4::1,fc00:0:3::1 dev eth2
```
- Flow after Path Control
- ![Path Control1](https://github.com/ishikawaya/clab-lab02-segment-routing/blob/main/images/lab02-topology-path-control2.png)
