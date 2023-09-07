import json

# Read the JSON file
def read_json_file(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

# Generate C header file content
def generate_c_header(data):
    header = "#ifndef _STRUCT_H_\n#define _STRUCT_H_\n\n"

    for struct in data['structs']:
        msgname = struct['msgname']
        signals = struct['signals']
        period = struct['period']
        msgid = struct['msgid']

        struct_declaration = f"typedef struct\n{{\n"
        macros = []

        for signal_name, value in signals.items():
            if value == 1:
                struct_declaration += f"    uint64_t {signal_name};\n"
            if value == 0:
                macros.append(f"#define {msgname}_{signal_name} (0)")

        struct_declaration += f"}} {msgname};\n"
        header += struct_declaration

        macros.append(f"#define {msgname}_period ({period})")
        macros.append(f"#define {msgname}_msgid ({msgid})")
        header += '\n'.join(macros) + "\n\n"

    header += "#endif\n"

    return header

# Write the C header file
def write_c_header(header, file_name):
    with open(file_name, 'w') as file:
        file.write(header)

if __name__ == "__main__":
    input_file = "struct.json"
    output_file = "struct.h"

    data = read_json_file(input_file)
    c_header = generate_c_header(data)
    write_c_header(c_header, output_file)

    print(f"Generated {output_file}")

