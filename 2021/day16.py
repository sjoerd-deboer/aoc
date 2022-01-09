version_numbers = 0


# Takes Binary, returns the literal value and the rest of the packet
def literal_value(binary):
    pointer = 0
    output = ""
    while True:
        prefix = binary[pointer]
        output += binary[pointer + 1:pointer + 5]
        pointer += 5
        if prefix == "0":
            break
    return int(output, 2), binary[pointer:]


with open("input-16.txt", "r") as f:
    p = "".join([bin(int(x, 16))[2:].zfill(4) for x in f.readline().strip()])
    print("START", p)
    # A single packet that could contain multiple


def unpack(input):
    global version_numbers
    # Packet header
    packet_version = int(input[0:3], 2)
    version_numbers += packet_version
    print("Packet_version", packet_version)
    packet_type_id = int(input[3:6], 2)
    packet_content = input[6:]
    if packet_type_id == 4:
        print("Literal Value", literal_value(packet_content))
        return literal_value(packet_content)
    else:
        r = [-1]
        left_over_bits = ""
        packet_length_type_id = packet_content[0]
        l = 11 if int(packet_length_type_id) else 15
        print(packet_length_type_id, l)
        subpacket_length_bits = int(packet_content[1:1 + l], 2)
        packet_content = packet_content[l + 1:]
        print(subpacket_length_bits)
        if l == 15:
            subpacket_content = packet_content[:subpacket_length_bits]
            packet_content = packet_content[subpacket_length_bits:]
            print(subpacket_content)
            temp = unpack(subpacket_content)
            r = [temp[0]]
            while temp[1]:
                print("Unpacking Subpacket...")
                temp = unpack(temp[1])
                r.append(temp[0])
            left_over_bits = packet_content
            # return r, packet_content
        elif l == 11:
            temp = unpack(packet_content)
            r = [temp[0]]
            for x in range(subpacket_length_bits - 1):
                temp = unpack(temp[1])
                r.append(temp[0])
            left_over_bits = temp[1]
            # return r, temp[1]
        # Perform operation
        print(r, packet_type_id)
        if packet_type_id == 0:
            return sum(r), left_over_bits
        elif packet_type_id == 1:
            q = 1
            for x in r:
                q *= x
            return q, left_over_bits
        elif packet_type_id == 2:
            return min(r), left_over_bits
        elif packet_type_id == 3:
            return max(r), left_over_bits
        elif packet_type_id == 5:
            print("Hutsefluts", r)
            return int(r[0] > r[1]), left_over_bits
        elif packet_type_id == 6:
            print("Pils met Kots", r)
            return int(r[0] < r[1]), left_over_bits
        elif packet_type_id == 7:
            return int(r[0] == r[1]), left_over_bits
    print(packet_version, packet_type_id, packet_content)


if __name__ == "__main__":
    print(unpack(p))
    print(version_numbers)
