#!/usr/bin/env python3
# --- Day 13: Distress Signal ---


def parse_packet(text: str) -> list:
    def recur_parse_packet(text: str) -> tuple[list, int]:
        packet: list[list | int] = []
        index = 1
        curnumber = ""
        while index < len(text):
            char = text[index]
            if char == "[":
                subpacket, chars_processed = recur_parse_packet(text[index:])
                packet.append(subpacket)
                index += chars_processed
            elif char == "]":
                if curnumber:
                    packet.append(int(curnumber))
                    curnumber = ""
                return packet, index
            elif char == ",":
                if curnumber:
                    packet.append(int(curnumber))
                    curnumber = ""
            else:
                curnumber += char
            index += 1
        return packet, index

    packet, _ = recur_parse_packet(text)
    return packet


def parse_packets(text: str) -> list[tuple[list, list]]:
    pairs = []
    lines = text.strip().split("\n")
    for i in range(0, len(lines), 3):
        pairs.append(
            (
                parse_packet(lines[i]),
                parse_packet(lines[i + 1]),
            )
        )
    return pairs


def compare_packets(left: list | int, right: list | int) -> int:
    if isinstance(left, int) and isinstance(right, int):
        return left - right
    elif isinstance(left, int) and isinstance(right, list):
        return compare_packets([left], right)
    elif isinstance(right, int) and isinstance(left, list):
        return compare_packets(left, [right])
    elif isinstance(left, list) and isinstance(right, list):
        for idx in range(min(len(left), len(right))):
            cmp = compare_packets(left[idx], right[idx])
            if cmp != 0:
                return cmp
        return len(left) - len(right)
    else:
        raise ValueError("Invalid packets {left} {right}")


def find_decoder_key(packet_pairs: list[tuple[list, list]]) -> int:
    dividers = ([[2]], [[6]])
    min_than_divider = [1, 2]
    for pair in packet_pairs:
        for i in range(2):
            for j in range(2):
                if compare_packets(pair[j], dividers[i]) < 0:
                    min_than_divider[i] += 1
    return min_than_divider[0] * min_than_divider[1]


def main() -> None:
    with open("input/day13.txt") as f:
        pairs = parse_packets(f.read())

    indices = []
    for idx, (left, right) in enumerate(pairs):
        if compare_packets(left, right) < 0:
            indices.append(idx + 1)

    print(f"Part one solution: {sum(indices)}")

    decoder_key = find_decoder_key(pairs)
    print(f"Part two solution: {decoder_key}")


if __name__ == "__main__":
    main()
