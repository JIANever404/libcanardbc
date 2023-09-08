import json
import sys
import os

# Read the JSON file
def read_json_file(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

# Generate C header file content
def generate_c_header(data, header_name):
    header = f"#ifndef _{header_name.upper()}_CANSTRUCT_H\n#define _{header_name.upper()}_CANSTRUCT_H\n\n"

    for struct in data['structs']:
        msgname = struct['msgname']+'_canVal'
        signals = struct['signals']
        period = struct['period']
        msgid = struct['msgid']

        struct_declaration = f"typedef struct\n{{\n"
        struct_members = []

        for signal_name in signals:
            struct_members.append(f"    unsigned long long {signal_name};")

        struct_declaration += "\n".join(struct_members) + "\n"
        struct_declaration += f"}} {msgname};\n"
        header += struct_declaration

        header += f"#define {msgname}_period ({period})\n"
        header += f"#define {msgname}_msgid ({msgid})\n\n"

    header += "#endif\n"

    return header


# Write the C header file
def write_c_header(header, file_name):
    with open(file_name, 'w') as file:
        file.write(header)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python json2h.py <input_json_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    header_name = os.path.splitext(os.path.basename(input_file))[0]
    output_file = header_name + ".h"

    data = read_json_file(input_file)
    c_header = generate_c_header(data, header_name)
    write_c_header(c_header, output_file)

    print(f"Generated {output_file}")
