""" Repeates each command from the CFG list NUM times """

NUM = 10

CFG = [
        """time-range tr{}
 absolute end 00:00 16 December 2025""",
        """object network on{}
 host 1.1.1.1""",
        """object-group network og{}
 network-object host 1.1.1.1
 network-object 10.1.1.0 255.255.255.0""",
        """object-group protocol obj_prot{}
 description test_og_prot
 protocol-object icmp""",
        "access-list test extended permit ip any any time-range tr{0}",
        "access-list acl_og{0} extended deny ip object-group og{0} host 8.8.8.8",
    ]

def generate(template):
    res = ""
    for i in range(NUM):
        res += template.format(i) + "\n"
    return res


def dummy_cfg_generator():
    result = ""
    for i in CFG:
        result += generate(i)
    # print(result)
    with open(
        f"fake_config_short.txt",
        "w",
    ) as f:
        f.write(result)


if __name__ == "__main__":
    dummy_cfg_generator()
    pass
