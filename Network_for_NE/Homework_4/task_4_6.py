ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
template = """
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
"""
ospf_list = ospf_route.replace(",", "").split()
print(
    template.format(
        ospf_list[0], ospf_list[1].strip("[]"), ospf_list[3], ospf_list[4], ospf_list[5]
    )
)
