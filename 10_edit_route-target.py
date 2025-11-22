import pexpect

# ホスト名
hosts = ["pe1", "pe2", "pe3", "pe4", "p1", "p2"]

# ラボ名
labname = "lab02"

for host in hosts:
    print(f"=== Configuring {host} ===")

    # docker execでvtyshを起動
    cmd = f"docker exec -ti clab-{labname}-{host} bash -c vtysh"
    child = pexpect.spawn(cmd)

    # プロンプト待ち: peX>
    child.expect(f"{host}#")

    # conf t
    child.sendline("conf t")
    child.expect(f"{host}\\(config\\)#")

    child.sendline(f"router bgp 64512 vrf blue")
    child.expect(f"{host}\\(config-router\\)#")
    child.sendline("address-family ipv4 unicast")
    child.expect(f"{host}\\(config-router-af\\)#")
    child.sendline("rt vpn both 64512:10")
    child.expect(f"{host}\\(config-router-af\\)#")
    child.sendline("address-family ipv6 unicast")
    child.expect(f"{host}\\(config-router-af\\)#")
    child.sendline("rt vpn both 64512:10")
    child.expect(f"{host}\\(config-router-af\\)#")

    child.sendline(f"router bgp 64512 vrf red")
    child.expect(f"{host}\\(config-router\\)#")
    child.sendline("address-family ipv4 unicast")
    child.expect(f"{host}\\(config-router-af\\)#")
    child.sendline("rt vpn both 64512:20")
    child.expect(f"{host}\\(config-router-af\\)#")
    child.sendline("address-family ipv6 unicast")
    child.expect(f"{host}\\(config-router-af\\)#")
    child.sendline("rt vpn both 64512:20")
    child.expect(f"{host}\\(config-router-af\\)#")

    # 終了
    child.sendline("exit")
    child.sendline("end")

    child.close()
