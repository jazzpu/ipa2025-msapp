from netmiko import ConnectHandler
import json
import os
import ntc_templates


def get_interfaces(ip, username, password):

    os.environ["NET_TEXTFSM"] = os.path.join(
        os.path.dirname(ntc_templates.__file__), "templates"
    )

    device = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": username,
        "password": password,
    }

    with ConnectHandler(**device) as conn:
        conn.enable()
        result = conn.send_command("show ip int br", use_textfsm=True)
        conn.disconnect()

    # Log the parsed result for container logs visibility
    print(json.dumps(result, indent=2))

    # Return the structured interfaces list so callers can persist/use it
    return result


if __name__ == '__main__':
    get_interfaces()
