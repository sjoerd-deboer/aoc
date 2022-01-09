version_numbers = 0

with open("input-16.txt", "r") as f:
    p = "".join([bin(int(x, 16))[2:].zfill(4) for x in f.readline().strip()])


def unpack(bit_string):
    global version_numbers
    packet_version = int(bit_string[0:3], 2)
    version_numbers += packet_version
    packet_type_id = int(bit_string[3:6], 2)
    packet_content = bit_string[6:]
    if packet_type_id == 4:
        pointer = 0
        output = ""
        while True:
            prefix = packet_content[pointer]
            output += packet_content[pointer + 1:pointer + 5]
            pointer += 5
            if prefix == "0":
                break
        return int(output, 2), packet_content[pointer:]
    else:
        r = [-1]
        left_over_bits = ""
        packet_length_type_id = packet_content[0]
        subpacket_length = 11 if int(packet_length_type_id) else 15
        subpacket_length_bits = int(packet_content[1:1 + subpacket_length], 2)
        packet_content = packet_content[subpacket_length + 1:]
        if subpacket_length == 15:
            subpacket_content = packet_content[:subpacket_length_bits]
            packet_content = packet_content[subpacket_length_bits:]
            temp = unpack(subpacket_content)
            r = [temp[0]]
            while temp[1]:
                temp = unpack(temp[1])
                r.append(temp[0])
            left_over_bits = packet_content
        elif subpacket_length == 11:
            temp = unpack(packet_content)
            r = [temp[0]]
            for x in range(subpacket_length_bits - 1):
                temp = unpack(temp[1])
                r.append(temp[0])
            left_over_bits = temp[1]
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
            return int(r[0] > r[1]), left_over_bits
        elif packet_type_id == 6:
            return int(r[0] < r[1]), left_over_bits
        elif packet_type_id == 7:
            return int(r[0] == r[1]), left_over_bits


if __name__ == "__main__":
    day2 = unpack(p)[0]
    print("Part 1:", version_numbers)
    print("Part 2:", day2)
